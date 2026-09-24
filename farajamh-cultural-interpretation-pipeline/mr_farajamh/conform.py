"""Make model output conform to the schema, and record every repair.

Small models do not reliably stay inside an enum or return every field. Crashing at the end of a run
throws away the model work; silently accepting anything would let junk into the package. So each
repair is applied AND recorded in L7_review_signals.nonconformances, and the package carries the flag
`model_output_coerced` so a reviewer knows the raw reply was not schema-clean.
"""
from __future__ import annotations

EVIDENCE_TYPES = {"utterance_span", "context_field", "conversation_turn", "translation_candidate",
                  "model_background_knowledge", "local_concept_layer"}
CATEGORIES = {"emotional_state", "cognitive_process", "somatic_experience", "spiritual_or_supernatural",
              "social_or_relational", "clinical_symptom", "risk_or_safety", "other"}
REGISTERS = {"everyday_cultural", "clinical", "mixed"}
EDIT_TYPES = {"orthographic", "phonological_variant", "sheng_lexical", "code_switch_marked",
              "asr_correction", "spacing_punctuation"}


def _note(log: list, where: str, what: str, original, used):
    log.append({"where": where, "field": what, "model_value": str(original)[:80], "used_instead": str(used)})


def sense(s: dict, model_ref: str, log: list) -> dict:
    if s.get("category") not in CATEGORIES:
        _note(log, f"{model_ref}/interpret", "category", s.get("category"), "other")
        s["category"] = "other"
    if s.get("register") not in REGISTERS:
        _note(log, f"{model_ref}/interpret", "register", s.get("register"), "mixed")
        s["register"] = "mixed"
    for field, default in (("sense_key", "unlabelled"), ("gloss", ""), ("rationale", "")):
        if not isinstance(s.get(field), str) or not s.get(field):
            _note(log, f"{model_ref}/interpret", field, s.get(field), default or "(empty)")
            s[field] = default
    ev = []
    for e in s.get("evidence") or []:
        if not isinstance(e, dict):
            _note(log, f"{model_ref}/interpret", "evidence", e, "dropped")
            continue
        if e.get("type") not in EVIDENCE_TYPES:
            # A model citing something outside the list is usually pointing at the translations it was
            # shown, or at its own knowledge. Keep the claim, label it honestly as the weakest type.
            _note(log, f"{model_ref}/interpret", "evidence.type", e.get("type"), "model_background_knowledge")
            e["type"] = "model_background_knowledge"
        e.setdefault("ref", "")
        ev.append({k: v for k, v in e.items() if k in {"type", "ref", "quote"} and isinstance(v, str)} | {"type": e["type"]})
    s["evidence"] = ev
    p = s.get("self_reported_plausibility")
    if not isinstance(p, (int, float)):
        _note(log, f"{model_ref}/interpret", "self_reported_plausibility", p, 0)
        s["self_reported_plausibility"] = 0
    deps = s.get("context_dependencies")
    s["context_dependencies"] = [d for d in deps if isinstance(d, str)] if isinstance(deps, list) else []
    return s


def translation(t: dict, model_ref: str, log: list) -> dict:
    for field in ("literal_gloss", "idiomatic_translation"):
        if not isinstance(t.get(field), str) or not t.get(field):
            _note(log, f"{model_ref}/translate", field, t.get(field), "(empty)")
            t[field] = ""
    pts = []
    for pt in t.get("preserved_terms") or []:
        if isinstance(pt, dict) and isinstance(pt.get("term"), str):
            pts.append({"term": pt["term"], "reason": str(pt.get("reason", ""))})
        else:
            _note(log, f"{model_ref}/translate", "preserved_terms", pt, "dropped")
    t["preserved_terms"] = pts
    if not isinstance(t.get("self_reported_confidence"), (int, float)):
        _note(log, f"{model_ref}/translate", "self_reported_confidence", t.get("self_reported_confidence"), 0)
        t["self_reported_confidence"] = 0
    if not isinstance(t.get("uncertainty_note"), str):
        t["uncertainty_note"] = ""
    return t


def normalisation(n: dict, model_ref: str, original_text: str, expression: str, log: list) -> dict:
    for field, default in (("normalised_text", original_text), ("normalised_expression", expression)):
        if not isinstance(n.get(field), str) or not n.get(field):
            _note(log, f"{model_ref}/normalise", field, n.get(field), "original text kept")
            n[field] = default
    edits = []
    for e in n.get("edits") or []:
        if not isinstance(e, dict) or not isinstance(e.get("from"), str) or not isinstance(e.get("to"), str):
            _note(log, f"{model_ref}/normalise", "edits", e, "dropped")
            continue
        if e.get("type") not in EDIT_TYPES:
            _note(log, f"{model_ref}/normalise", "edits.type", e.get("type"), "orthographic")
            e["type"] = "orthographic"
        edits.append({k: v for k, v in e.items() if k in {"from", "to", "type", "note"}})
    n["edits"] = edits
    if not isinstance(n.get("language_id"), str) or not n["language_id"]:
        _note(log, f"{model_ref}/normalise", "language_id", n.get("language_id"), "sw")
        n["language_id"] = "sw"
    for field in ("code_switch_segments", "dialect_hypotheses"):
        if not isinstance(n.get(field), list):
            n[field] = []
        n[field] = [x for x in n[field] if isinstance(x, dict)]
    return n
