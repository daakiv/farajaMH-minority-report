"""Command line.

  python -m mr_farajamh.cli try      "Moyo wangu unauma"            # one typed expression, live models
  python -m mr_farajamh.cli run      --input pilot/utterances.jsonl --out out --fixture
  python -m mr_farajamh.cli approve  --out out --decisions pilot/review_decisions_SIMULATED.jsonl --demo-placeholders
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import jsonschema
import yaml

from . import __version__
from .approve import build_outputs
from .backends import FixtureBackend, OllamaBackend
from .pipeline import run_package
from .review import export_review_sheet, review_card
from .terminology import FixtureTerminology, OLSClient, SnowstormClient, TerminologyHub

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = lambda n: json.loads((ROOT / "schemas" / f"{n}.schema.json").read_text())


def load_jsonl(p):
    return [json.loads(l) for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()]


def _live_env(config_path: str, run_id: str):
    """Config, Ollama backend and terminology clients for a live run.
    Terminology systems whose endpoint is still a placeholder are skipped with a warning."""
    cfg = yaml.safe_load(Path(config_path).read_text())
    cfg["_run_id"] = run_id
    backend = OllamaBackend(cfg["ollama_hosts"], cfg["models"].get("options", {}))
    t = cfg["terminologies"]
    configured = lambda name: name in t and "<" not in t[name]["endpoint"]
    clients = []
    if configured("SNOMEDCT"):
        c = t["SNOMEDCT"]
        clients.append(SnowstormClient(c["endpoint"], c["branch"], c["version"], c.get("ecl_scope"), c["limit"]))
    if configured("MFOEM"):
        c = t["MFOEM"]
        clients.append(OLSClient(c["endpoint"], c["ontology"], c["version"], c["limit"]))
    skipped = [name for name in ("SNOMEDCT", "MFOEM") if not configured(name)]
    if skipped:
        print(f"WARNING: no endpoint configured for {', '.join(skipped)}; these systems are not searched in this run.")
    return cfg, backend, TerminologyHub(clients=clients)


def _fixture_env(config_path: str, run_id: str):
    cfg = yaml.safe_load(Path(config_path).read_text())
    cfg["_run_id"] = run_id
    cfg["models"]["normaliser"] = {"model_ref": "sim-model-A", "family": "sim-family-1"}
    cfg["models"]["interpreters"] = [{"model_ref": f"sim-model-{x}", "family": f"sim-family-{i + 1}"} for i, x in enumerate("ABC")]
    return cfg, FixtureBackend(ROOT / "pilot/fixtures/simulated_responses.json"), \
        TerminologyHub(fixture=FixtureTerminology(ROOT / "pilot/fixtures/terminology_fixture.json"))


def cmd_run(a):
    cfg, backend, terms = (_fixture_env if a.fixture else _live_env)(a.config, a.run_id)
    in_schema, pkg_schema = SCHEMA("utterance_input"), SCHEMA("candidate_package")
    out = Path(a.out)
    (out / "packages").mkdir(parents=True, exist_ok=True)
    (out / "review_cards").mkdir(parents=True, exist_ok=True)
    pkgs = []
    for utt in load_jsonl(a.input):
        jsonschema.validate(utt, in_schema)
        p = run_package(utt, cfg, backend, terms)
        if p["status"] == "awaiting_review":
            jsonschema.validate(p, pkg_schema)
        pkgs.append(p)
        (out / "packages" / f"{p['package_id']}.json").write_text(json.dumps(p, ensure_ascii=False, indent=1), encoding="utf-8")
        (out / "review_cards" / f"{utt['utterance_id']}.md").write_text(review_card(p), encoding="utf-8")
    export_review_sheet(pkgs, out / "review_sheet.csv")
    print(json.dumps({p["utterance_ref"]["utterance_id"]: p["status"] for p in pkgs}, indent=1))


def print_summary(p: dict):
    """Readable terminal summary of one candidate package."""
    w = print
    if p["status"] != "awaiting_review":
        w(f"\nSTATUS: {p['status']}\n{p.get('note', '')}")
        return
    n = p["L2_normalisation"]
    w("\n" + "=" * 78)
    w(f"INPUT      {p['L1_original']['original_text']}")
    w(f"EXPRESSION {p['L1_original']['expression_span']['text']}")
    ctx = p["L1_original"]["context_as_received"]
    w(f"CONTEXT    {ctx['country']}/{ctx.get('region', '?')} · dialect {ctx.get('dialect_declared', '?')} · "
      f"speaker {ctx['speaker_role']} · {ctx['setting']} · negation {ctx['negation']['value']} · "
      f"experiencer {ctx['attribution']['value']}")
    w("=" * 78)
    w(f"\nNORMALISED  {n['normalised_text']}   [{n['language_id']}]")
    for e in n["edits"]:
        w(f"   edit  {e['from']} -> {e['to']}  ({e['type']}) {e.get('note', '')}")
    w("\nTRANSLATIONS (each model on its own)")
    for t in p["L3_translation"]["candidates"]:
        w(f"   {t['candidate_id']} {t['model_ref']}")
        w(f"      literal   {t['literal_gloss']}")
        w(f"      idiomatic {t['idiomatic_translation']}")
        for pt in t.get("preserved_terms", []):
            w(f"      keeps     {pt.get('term')} — {pt.get('reason', '')}")
        if t.get("uncertainty_note"):
            w(f"      unsure    {t['uncertainty_note']}")
        bt = t["back_translation"]
        w(f"      back      {bt['text']}  (similarity {bt['similarity_to_normalised']})")
    cs = p["L5_agreement"].get("category_support") or []
    if cs:
        w("\nHOW THE MODELS READ IT, BY CATEGORY (labels aside)")
        for x in cs:
            w(f"   {len(x['models'])}/{p['L5_agreement']['n_models']}  {x['category']}  ({', '.join(x['models'])})")
    w("\nCANDIDATE MEANINGS (clustered across models; nothing wins)")
    senses = {s["sense_id"]: s for s in p["L4_interpretation"]["candidates"]}
    concepts = {pc["cluster_id"]: pc for pc in p["L6_concept_candidates"]["per_cluster"]}
    for c in p["L5_agreement"]["sense_clusters"]:
        w(f"   [{c['standing'].upper()} {len(c['supporting_models'])}/{p['L5_agreement']['n_models']}] "
          f"{c['label']}  ({c['category']})")
        for sid in c["member_sense_ids"]:
            s = senses[sid]
            w(f"      - {s['model_ref']}: {s['gloss']}")
            w(f"        why: {s['rationale']}")
        pc = concepts[c["cluster_id"]]
        if pc["candidates"]:
            for x in pc["candidates"][:5]:
                preds = ", ".join(f"{r['model_ref']}->{r['proposed_predicate']}" for r in x["ranking"]) or "not ranked"
                w(f"        concept: {x['id']}  {x['label']}  [{preds}]")
        else:
            w(f"        concept: none retrieved ({pc.get('retrieval_status', 'ok')})")
        if pc["no_adequate_match_votes"]:
            w(f"        'no adequate concept' per {', '.join(pc['no_adequate_match_votes'])}")
    sig = p["L7_review_signals"]
    w(f"\nREVIEW PRIORITY {sig['review_priority']}")
    w(f"FLAGS           {', '.join(sig['risk_flags']) or 'none'}")
    w(f"REVIEWERS       {', '.join(sig['suggested_reviewer_roles'])}")
    w("\nThis is a proposal. No meaning or mapping is accepted until reviewers decide.\n")


def cmd_try(a):
    """One typed expression through the whole pipeline, printed to the terminal."""
    text = a.text.strip()
    expr = (a.expression or text).strip()
    if expr not in text:
        raise SystemExit(f"--expression {expr!r} is not part of the utterance {text!r}")
    start = text.find(expr)
    utt = {
        "schema_version": "0.1.0", "utterance_id": f"TRY-{abs(hash(text)) % 10**6:06d}",
        "silver_record_ref": {"record_id": "typed-by-hand", "silver_version": "n/a", "sha256": ""},
        "source": {"modality": "constructed_pilot_example", "transcription_method": "none"},
        "original_text": text, "language_declared": f"sw-{a.country}",
        "expression_span": {"start": start, "end": start + len(expr), "text": expr},
        "conversational_context": {"window_policy": "none", "preceding_turns": [], "following_turns": []},
        "context": {"country": a.country, "region": a.region, "site_id": "adhoc", "dialect_declared": a.dialect,
                    "speaker_role": a.speaker, "setting": a.setting,
                    "negation": {"value": a.negation, "source": "annotator"},
                    "temporality": {"value": a.temporality, "source": "annotator"},
                    "attribution": {"value": a.attribution, "source": "annotator"}},
        "triage": {"route": "new_expression"},
        "safety": {"flag": a.safety_flagged, "escalated": False},
        "data_classification": "synthetic",
    }
    utt["silver_record_ref"]["sha256"] = __import__("hashlib").sha256(text.encode()).hexdigest()
    jsonschema.validate(utt, SCHEMA("utterance_input"))
    print("NOTE: this command has no safety detection. Use it for constructed examples only, never for "
          "participant data, and set --safety-flagged yourself for anything safety-critical.")
    cfg, backend, terms = _live_env(a.config, a.run_id)
    p = run_package(utt, cfg, backend, terms)
    if p["status"] == "awaiting_review":
        jsonschema.validate(p, SCHEMA("candidate_package"))
    out = Path(a.out)
    (out / "packages").mkdir(parents=True, exist_ok=True)
    (out / "review_cards").mkdir(parents=True, exist_ok=True)
    (out / "packages" / f"{p['package_id']}.json").write_text(json.dumps(p, ensure_ascii=False, indent=1), encoding="utf-8")
    card = out / "review_cards" / f"{utt['utterance_id']}.md"
    card.write_text(review_card(p), encoding="utf-8")
    print_summary(p)
    print(f"Full package: {out / 'packages' / (p['package_id'] + '.json')}")
    print(f"Review card:  {card}")


def cmd_approve(a):
    pkgs = {json.loads(f.read_text())["package_id"]: json.loads(f.read_text()) for f in (Path(a.out) / "packages").glob("*.json")}
    decisions = load_jsonl(a.decisions)
    schema = SCHEMA("review_decision")
    for d in decisions:
        jsonschema.validate(d, schema)
    print(build_outputs(pkgs, decisions, Path(a.out) / "approved", __version__, a.demo_placeholders))


def main():
    ap = argparse.ArgumentParser(prog="mr_farajamh")
    sub = ap.add_subparsers(required=True)
    r = sub.add_parser("run")
    r.add_argument("--config", default=str(ROOT / "config/pilot.yaml"))
    r.add_argument("--input", required=True)
    r.add_argument("--out", required=True)
    r.add_argument("--run-id", default="pilot-dryrun")
    r.add_argument("--fixture", action="store_true", help="Use SIMULATED fixture responses and placeholder terminology")
    r.set_defaults(fn=cmd_run)
    t = sub.add_parser("try", help="Run one typed expression through the pipeline with live models")
    t.add_argument("text", help='The utterance, e.g. "Moyo wangu unauma"')
    t.add_argument("--expression", help="The part of the utterance to focus on (default: the whole utterance)")
    t.add_argument("--config", default=str(ROOT / "config/pilot.yaml"))
    t.add_argument("--out", default="out_try")
    t.add_argument("--run-id", default="try")
    t.add_argument("--country", default="KE", choices=["KE", "TZ"])
    t.add_argument("--region", default="KE-nairobi")
    t.add_argument("--dialect", default="standard")
    t.add_argument("--speaker", default="participant",
                   choices=["participant", "family_member", "chw", "clinician", "peer_supporter", "simulated_patient", "unknown"])
    t.add_argument("--setting", default="chat_platform",
                   choices=["home_visit", "clinic", "hospital_ward", "chat_platform", "peer_support", "hdss_survey", "simulation", "unknown"])
    t.add_argument("--negation", default="affirmed", choices=["affirmed", "negated", "uncertain"])
    t.add_argument("--temporality", default="current", choices=["current", "past", "recurrent", "hypothetical", "unknown"])
    t.add_argument("--attribution", default="self", choices=["self", "family_member", "other_person", "generic", "unknown"])
    t.add_argument("--safety-flagged", action="store_true", help="Mark as safety-critical; the pipeline will refuse to process it")
    t.set_defaults(fn=cmd_try)
    p = sub.add_parser("approve")
    p.add_argument("--out", required=True)
    p.add_argument("--decisions", required=True)
    p.add_argument("--demo-placeholders", action="store_true")
    p.set_defaults(fn=cmd_approve)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
