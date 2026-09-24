"""Stages M1–M6: raw utterance -> candidate interpretation package (never an approved interpretation)."""
from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from . import agreement as ag
from . import conform
from .policy import assert_not_approved, check_before_run, enforce_id_origin

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = {n: (ROOT / "prompts" / f"{n}.md").read_text(encoding="utf-8")
           for n in ("normalise", "translate", "back_translate", "interpret", "rank_concepts")}


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fill(template: str, **kw) -> str:
    for k, v in kw.items():
        template = template.replace("{{" + k + "}}", v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))
    return template


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def run_package(utt: dict, cfg: dict, backend, terms, local_concepts: list[dict] | None = None) -> dict:
    started = now()
    interpreters = cfg["models"]["interpreters"]
    model_refs = [m["model_ref"] for m in interpreters]
    ctx = utt["context"]
    key = lambda stage, **extra: {"utterance_id": utt["utterance_id"], "stage": stage, **extra}
    base = {
        "schema_version": "0.1.0",
        "package_id": f"MRP-{utt['utterance_id']}-{cfg.get('_run_id') or uuid.uuid4().hex[:8]}",
        "utterance_ref": {"utterance_id": utt["utterance_id"], "input_sha256": sha(json.dumps(utt, sort_keys=True, ensure_ascii=False))},
    }
    blocked = check_before_run(utt, backend, interpreters, cfg["agreement"]["min_model_families"])
    if blocked:
        # The package records only that it was held. No model sees the utterance.
        return base | {"status": blocked, "note": "Safety-flagged and not yet escalated. Escalate first (v10 step 1); curation can follow."}

    # ---- M1 normalisation (single model + recorded edits; original is never altered)
    norm_model = cfg["models"]["normaliser"]["model_ref"]
    norm = backend.generate_json(norm_model, fill(PROMPTS["normalise"], original_text=utt["original_text"],
                                 expression_text=utt["expression_span"]["text"], country=ctx["country"],
                                 region=ctx.get("region", "unknown"), dialect_declared=ctx.get("dialect_declared", "unknown")),
                                 key("normalise"))
    nonconformances: list[dict] = []
    norm = conform.normalisation(norm, norm_model, utt["original_text"], utt["expression_span"]["text"], nonconformances)

    # ---- M2 translation: every interpreter translates independently; ring back-translation
    trans = []
    for m in model_refs:
        t = backend.generate_json(m, fill(PROMPTS["translate"], normalised_text=norm["normalised_text"],
                                  normalised_expression=norm["normalised_expression"], country=ctx["country"],
                                  region=ctx.get("region", "unknown"), speaker_role=ctx["speaker_role"], setting=ctx["setting"]),
                                  key("translate"))
        trans.append({"candidate_id": f"T{len(trans) + 1}", "model_ref": m} | conform.translation(t, m, nonconformances))
    bt_mode = cfg["models"].get("back_translation", "ring")
    if bt_mode != "off":
        for i, t in enumerate(trans):
            bt_model = bt_mode if bt_mode not in ("ring",) else model_refs[(i + 1) % len(model_refs)]
            bt = backend.generate_json(bt_model, fill(PROMPTS["back_translate"], idiomatic_translation=t["idiomatic_translation"]),
                                       key("back_translate", source_model=t["model_ref"]))
            sim = ag.back_translation_similarity(bt["text"], norm["normalised_text"])
            t["back_translation"] = {"by_model": bt_model, "text": bt["text"], "similarity_to_normalised": sim}
            if sim is None:
                # unusable Swahili from the back-translator: say so rather than scoring it zero
                t["back_translation"]["note"] = "output unusable for comparison (degenerate or too short)"

    # ---- M3 interpretation: independent, blind to each other's senses (they see translations only)
    senses = []
    conv = utt.get("conversational_context", {})
    for m in model_refs:
        r = backend.generate_json(m, fill(PROMPTS["interpret"], original_text=utt["original_text"],
                                  normalised_text=norm["normalised_text"], normalised_expression=norm["normalised_expression"],
                                  translations=[t["idiomatic_translation"] for t in trans], country=ctx["country"],
                                  region=ctx.get("region", "unknown"), dialect_declared=ctx.get("dialect_declared", "unknown"),
                                  speaker_role=ctx["speaker_role"], setting=ctx["setting"], negation=ctx["negation"]["value"],
                                  temporality=ctx["temporality"]["value"], attribution=ctx["attribution"]["value"],
                                  conversation=conv.get("preceding_turns", []) + conv.get("following_turns", []),
                                  local_concepts=local_concepts or []), key("interpret"))
        for s in (r.get("senses") or []):
            if not isinstance(s, dict):
                conform._note(nonconformances, f"{m}/interpret", "sense", s, "dropped")
                continue
            senses.append({"sense_id": f"S{len(senses) + 1}", "model_ref": m} | conform.sense(s, m, nonconformances))
    if not senses:
        return base | {"status": "failed", "note": "No usable senses returned by any model."}

    # ---- M4 agreement / disagreement (deterministic code, no winner)
    acfg = cfg["agreement"]
    vectors, embed_model = None, cfg["models"].get("embedding_model")
    if embed_model and hasattr(backend, "embed"):
        try:
            vecs = backend.embed(embed_model, [f"{s['sense_key']}: {s['gloss']}" for s in senses])
            vectors = {s["sense_id"]: v for s, v in zip(senses, vecs)}
        except Exception as e:  # noqa: BLE001 - fall back to lexical clustering rather than losing the run
            print(f"    WARNING: embedding model {embed_model} unavailable ({type(e).__name__}); "
                  f"falling back to word-overlap clustering, which splits synonyms.")
    clusters = ag.finalise_clusters(
        ag.cluster_senses(senses, acfg["cluster_jaccard_threshold"], vectors,
                          acfg.get("embedding_similarity_threshold", 0.85),
                          acfg.get("embedding_cross_category_threshold", 0.93)),
        len(model_refs), acfg["minority_below"])
    t_agree = ag.translation_agreement(trans)
    bt_sims = [t["back_translation"]["similarity_to_normalised"] for t in trans if "back_translation" in t]
    families = [m["family"] for m in interpreters]
    flags = ag.divergence_flags(clusters, t_agree, bt_sims, families, acfg, ctx)
    lost = ag.cultural_terms_lost(trans)
    if lost:
        flags.append("cultural_term_lost_in_back_translation")

    # ---- M5 concept candidates: retrieve -> every model ranks -> record agreement; LLM never originates IDs
    per_cluster, concept_agree = [], {}
    live = backend.mode == "live"
    for c in clusters:
        rep = next(s for s in senses if s["sense_id"] == c["member_sense_ids"][0])
        before = len(getattr(terms, "errors", []))
        # Query the model-coined label AND the reviewer-facing gloss: a label like "emotional distress"
        # retrieves poor candidates on its own. Results are merged and de-duplicated by id.
        queries = [c["label"]] + ([rep["gloss"]] if rep.get("gloss") and rep["gloss"] != c["label"] else [])
        retrieved, seen = [], set()
        for q in queries:
            for hit in enforce_id_origin(terms.search(q), live):
                if hit["id"] not in seen:
                    seen.add(hit["id"])
                    retrieved.append(hit)
        failed = [e["system"] for e in getattr(terms, "errors", [])[before:]]
        listing = "\n".join(f"{r['system']} | {r['id']} | {r['label']}" for r in retrieved) or "(none retrieved)"
        rankings = {}
        for m in model_refs:
            rk = backend.generate_json(m, fill(PROMPTS["rank_concepts"], sense_gloss=rep["gloss"], sense_category=c["category"],
                                       sense_register=rep["register"], normalised_expression=norm["normalised_expression"], retrieved=listing),
                                       key("rank", retrieved=retrieved, sense_category=c["category"], sense_register=rep["register"]))
            valid = {r["id"] for r in retrieved}
            rk["ranked"] = [x for x in rk.get("ranked", []) if x["id"] in valid]  # drop any ID not retrieved
            rankings[m] = rk
        for r in retrieved:
            r["ranking"] = [{"model_ref": m, **{k: x[k] for k in ("rank", "proposed_predicate", "rationale")}}
                            for m, rk in rankings.items() for x in rk["ranked"] if x["id"] == r["id"]]
        ca = ag.concept_agreement(rankings)
        concept_agree[c["cluster_id"]] = ca
        per_cluster.append({"cluster_id": c["cluster_id"], "candidates": retrieved,
                            "retrieval_status": "ok" if not failed else f"unavailable: {', '.join(failed)}",
                            "no_adequate_match_votes": ca["no_adequate_match_votes"],
                            "gap_note": " | ".join(sorted({rk.get("gap_note", "") for rk in rankings.values() if rk.get("gap_note")}))})

    # ---- M6 review signals
    risk = list(flags)
    if any(c["category"] in ag.CLINICAL_CATEGORIES for c in clusters) and any(c["category"] not in ag.CLINICAL_CATEGORIES for c in clusters):
        risk.append("over_medicalisation_risk")
    if any(c["category"] == "risk_or_safety" for c in clusters):
        risk.append("safety_relevant_reading")
    if not live:
        risk.append("placeholder_ids_not_verified")
    if bt_mode == "off":
        risk.append("back_translation_disabled")
    if any(pc["no_adequate_match_votes"] for pc in per_cluster):
        risk.append("possible_semantic_gap")
    if nonconformances:
        risk.append("model_output_coerced")
    if getattr(terms, "errors", []):
        # A terminology service was unreachable: "no adequate match" here may just be a missed lookup.
        risk.append("terminology_lookup_failed")
    high = {"back_translation_mismatch", "cultural_term_lost_in_back_translation", "terminology_lookup_failed", "minority_clinical_reading", "over_medicalisation_risk", "safety_relevant_reading",
            "translation_divergence", "experiencer_not_speaker", "polarity_negated", "context_incomplete"}
    priority = "high" if high & set(risk) else ("medium" if risk and set(risk) - {"placeholder_ids_not_verified"} else "low")
    roles = ["linguist", "cultural_expert", "lived_experience"]
    if any(c["category"] in ag.CLINICAL_CATEGORIES | {"emotional_state", "cognitive_process", "somatic_experience"} for c in clusters):
        roles.insert(2, "clinician")

    pkg = base | {
        "status": "awaiting_review",
        "provenance": {
            "pipeline": "farajamh-minority-report", "pipeline_version": cfg["pipeline_version"], "upstream": cfg["upstream"],
            "run_id": cfg.get("_run_id", "adhoc"), "started_at": started, "ended_at": now(), "backend_mode": backend.mode,
            "models": [{"model_ref": norm_model, "family": cfg["models"]["normaliser"]["family"], "role": "normaliser",
                        "digest": backend.digest(norm_model), "host_locality": backend.host_locality, "options": cfg["models"].get("options", {})}] +
                      [{"model_ref": m["model_ref"], "family": m["family"], "role": "translator+interpreter+ranker",
                        "digest": backend.digest(m["model_ref"]), "host_locality": backend.host_locality, "options": cfg["models"].get("options", {})}
                       for m in interpreters],
            "prompts": [{"name": n, "sha256": sha(t)} for n, t in PROMPTS.items()],
            "terminologies": terms.describe(),
            "terminology_errors": getattr(terms, "errors", []),
            "policy": cfg["policy"],
        },
        "L1_original": {"original_text": utt["original_text"], "expression_span": utt["expression_span"], "context_as_received": ctx},
        "L2_normalisation": norm | {"producer": norm_model},
        "L3_translation": {"candidates": trans},
        "L4_interpretation": {"candidates": senses},
        "L5_agreement": {"n_models": len(model_refs), "model_families": sorted(set(families)), "sense_clusters": clusters,
                         "clustering_method": "embeddings" if vectors else "word_overlap",
                         "category_support": ag.category_support(senses, len(model_refs)),
                         "metrics": {"translation_agreement": t_agree, "back_translation_similarity": bt_sims, "cultural_terms_lost": lost,
                                     "sense_entropy": ag.sense_entropy(clusters), "n_clusters": len(clusters),
                                     "n_minority_clusters": sum(c["standing"] == "minority" for c in clusters),
                                     "concept_agreement": concept_agree},
                         "divergence_flags": flags},
        "L6_concept_candidates": {"per_cluster": per_cluster},
        "L7_review_signals": {
            "review_priority": priority, "risk_flags": sorted(set(risk)), "suggested_reviewer_roles": roles,
            "nonconformances": nonconformances,
            "confidence_components": {
                "note": "Separate signals for reviewers. Not a probability and not used to approve anything.",
                "translation_self_reported_mean": round(sum(t.get("self_reported_confidence", 0) for t in trans) / len(trans), 3),
                "translation_agreement": t_agree,
                "back_translation_similarity_min": min([x for x in bt_sims if x is not None], default=None),
                "top_cluster_support": clusters[0]["support_ratio"] if clusters else 0,
                "sense_entropy": ag.sense_entropy(clusters),
                "context_fields_resolved": sum(ctx[k]["source"] != "not_resolved" for k in ("negation", "temporality", "attribution")) / 3,
            },
        },
    }
    assert_not_approved(pkg)
    return pkg
