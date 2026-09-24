"""Human-in-the-loop hand-off: review sheet (CSV, one row per sense cluster) and a per-package review card.

The review card puts the blind first pass BEFORE the AI candidates. For a sample of items, reviewers
write their own reading first so the pilot can measure how much AI candidates anchor human judgement.
"""
from __future__ import annotations

import csv
from pathlib import Path

DECISION_COLS = ["reviewer_id", "reviewer_role", "blind_translation", "blind_interpretation", "translation_decision",
                 "final_translation", "interpretation_decision", "clinical_status", "context_confirmed",
                 "concept_decision", "concept_id", "predicate_id", "negative_assertion", "confidence", "justification"]


def export_review_sheet(packages: list[dict], path: Path):
    rows = []
    for p in packages:
        if p["status"] != "awaiting_review":
            rows.append({"package_id": p["package_id"], "utterance_id": p["utterance_ref"]["utterance_id"], "status": p["status"]})
            continue
        trans = " | ".join(f"{t['candidate_id']}: {t['idiomatic_translation']}" for t in p["L3_translation"]["candidates"])
        concepts = {pc["cluster_id"]: pc for pc in p["L6_concept_candidates"]["per_cluster"]}
        senses = {s["sense_id"]: s for s in p["L4_interpretation"]["candidates"]}
        for c in p["L5_agreement"]["sense_clusters"]:
            pc = concepts[c["cluster_id"]]
            rows.append({
                "package_id": p["package_id"], "utterance_id": p["utterance_ref"]["utterance_id"], "status": p["status"],
                "review_priority": p["L7_review_signals"]["review_priority"],
                "original": p["L1_original"]["original_text"], "normalised": p["L2_normalisation"]["normalised_text"],
                "translations": trans, "cluster_id": c["cluster_id"], "cluster_label": c["label"], "category": c["category"],
                "standing": c["standing"], "support": f"{len(c['supporting_models'])}/{p['L5_agreement']['n_models']}",
                "glosses": " || ".join(senses[i]["gloss"] for i in c["member_sense_ids"]),
                "concept_candidates": " ; ".join(f"{x['id']} {x['label']} [" + ",".join(r["proposed_predicate"] for r in x["ranking"]) + "]"
                                                 for x in pc["candidates"]) or "(none retrieved)",
                "no_match_votes": ",".join(pc["no_adequate_match_votes"]),
                "risk_flags": ",".join(p["L7_review_signals"]["risk_flags"]),
            } | {k: "" for k in DECISION_COLS})
    cols = list(dict.fromkeys(k for r in rows for k in r))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def review_card(p: dict) -> str:
    uid = p["utterance_ref"]["utterance_id"]
    if p["status"] != "awaiting_review":
        return f"# {uid} — {p['status']}\n\n{p.get('note', '')}\n"
    ctx = p["L1_original"]["context_as_received"]
    L = [f"# Review card — {uid}", f"Package `{p['package_id']}` · priority **{p['L7_review_signals']['review_priority']}** · "
         f"backend `{p['provenance']['backend_mode']}`", ""]
    if p["provenance"]["backend_mode"] != "live":
        L += ["> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.", ""]
    L += ["## Step 1 — Your own reading first (blind pass)",
          f"**Utterance:** {p['L1_original']['original_text']}",
          f"**Expression:** {p['L1_original']['expression_span']['text']}",
          f"**Context:** {ctx['country']}/{ctx.get('region', '?')}, dialect {ctx.get('dialect_declared', '?')}, speaker {ctx['speaker_role']}, "
          f"setting {ctx['setting']}, negation {ctx['negation']['value']}, temporality {ctx['temporality']['value']}, "
          f"experiencer {ctx['attribution']['value']}",
          "", "Write your translation and interpretation BEFORE opening Step 2.", "",
          "## Step 2 — AI candidates (proposals, not decisions)", "### Normalisation"]
    n = p["L2_normalisation"]
    L.append(f"`{n['normalised_text']}` (language {n['language_id']})")
    L += [f"- edit: `{e['from']}` → `{e['to']}` ({e['type']}) {e.get('note', '')}" for e in n["edits"]] or ["- no edits"]
    L += ["", "### Translations", "| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |", "|---|---|---|---|---|---|"]
    for t in p["L3_translation"]["candidates"]:
        bt = t.get("back_translation")
        if not bt:
            shown = "not run"
        elif bt["similarity_to_normalised"] is None:
            shown = f"{bt['text']} (not assessed)"
        else:
            shown = f"{bt['text']} ({bt['similarity_to_normalised']})"
        L.append(f"| {t['candidate_id']} | {t['model_ref']} | {t['literal_gloss']} | {t['idiomatic_translation']} | "
                 f"{shown} | {t.get('uncertainty_note', '')} |")
    cs = p["L5_agreement"].get("category_support") or []
    if cs:
        L += ["", "### How the models read it, by category (labels aside)"]
        L += [f"- **{x['category']}**: {len(x['models'])}/{p['L5_agreement']['n_models']} models ({', '.join(x['models'])})" for x in cs]
    L += ["", "### Candidate meanings, clustered across models", "| Cluster | Meaning | Category | Standing | Models |", "|---|---|---|---|---|"]
    for c in p["L5_agreement"]["sense_clusters"]:
        L.append(f"| {c['cluster_id']} | {c['label']} | {c['category']} | {c['standing']} | {', '.join(c['supporting_models'])} |")
    senses = p["L4_interpretation"]["candidates"]
    L += ["", "<details><summary>Rationale and evidence per model</summary>", ""]
    for s in senses:
        ev = "; ".join(f"{e['type']}: “{e.get('quote', '')}”" for e in s["evidence"])
        L.append(f"- **{s['sense_id']}** ({s['model_ref']}, {s['sense_key']}): {s['gloss']} — *{s['rationale']}* — evidence: {ev}")
    L += ["", "</details>", "", "### Candidate concepts (retrieved from terminology services; ranked by models)"]
    for pc in p["L6_concept_candidates"]["per_cluster"]:
        L.append(f"- **{pc['cluster_id']}**: " + ("; ".join(f"`{x['id']}` {x['label']} [{', '.join(r['model_ref'] + '→' + r['proposed_predicate'] for r in x['ranking'])}]"
                                                             for x in pc["candidates"]) or "none retrieved")
                 + (f" — **no adequate match** per {', '.join(pc['no_adequate_match_votes'])}" if pc["no_adequate_match_votes"] else ""))
    nc = p["L7_review_signals"].get("nonconformances") or []
    L += ["", "### Signals", f"- Risk flags: {', '.join(p['L7_review_signals']['risk_flags']) or 'none'}",
          (f"- Model output repaired in {len(nc)} place(s): "
           + "; ".join(f"{n['where']} {n['field']}=\"{n['model_value']}\" → {n['used_instead']}" for n in nc[:6])
           + (" …" if len(nc) > 6 else "")) if nc else "- Model output was schema-clean",
          f"- Suggested reviewers: {', '.join(p['L7_review_signals']['suggested_reviewer_roles'])}",
          f"- Confidence components (not a probability): `{ {k: v for k, v in p['L7_review_signals']['confidence_components'].items() if k != 'note'} }`",
          "", "## Step 3 — Decide (record in the review sheet or review_decision JSON)",
          "Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.", ""]
    return "\n".join(L)
