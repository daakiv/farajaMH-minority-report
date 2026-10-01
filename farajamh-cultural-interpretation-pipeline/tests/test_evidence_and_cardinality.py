"""Fixes arising from run kiswa-story-v1 (2026-09-30).

Across twelve turns of one Kiswahili session, seven risk senses cited text belonging to a different
turn — or to the interviewer's own question — and tagged it `utterance_span`. The same twelve prompts
through a larger model produced none. The check below therefore separates careful output from careless
output rather than penalising model size.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mr_farajamh import approve, conform, review  # noqa: E402

SOURCES = {
    "utterance": "Mwenyezi Mungu tu. Na jirani mmoja.",
    "conversation": ["Je, umewahi kuwa na mawazo ya kujidhuru?",
                     "Kuna siku nafikiri afadhali nisiwepo. Lakini watoto wananihitaji.",
                     "Nani anakusaidia kwa sasa?"],
    "translations": ["Only God knows.", "God, me, and one neighbour."],
}


def _sense(quote, etype="utterance_span"):
    return {"category": "risk_or_safety", "register": "mixed", "sense_key": "k", "gloss": "g",
            "rationale": "r", "self_reported_plausibility": 0.7,
            "evidence": [{"type": etype, "ref": "", "quote": quote}]}


def _type_after(quote):
    log = []
    out = conform.sense(_sense(quote), "gemma3:12b", log, sources=SOURCES)
    return out["evidence"][0]["type"], log


# ───────────────────────── the evidence check ─────────────────────────

def test_a_quote_from_the_utterance_is_left_alone():
    t, log = _type_after("Mwenyezi Mungu tu")
    assert t == "utterance_span"
    assert log == [], "a correct citation must not be recorded as a repair"


def test_a_quote_from_another_turn_becomes_conversation_turn():
    """Card 12 of kiswa-story-v1 quoted turn 11 as though it were its own utterance."""
    t, log = _type_after("Kuna siku nafikiri afadhali nisiwepo")
    assert t == "conversation_turn"
    assert log and "not in the utterance" in log[0]["field"]


def test_a_quote_from_the_interviewers_question_becomes_conversation_turn():
    t, _ = _type_after("Je, umewahi kuwa na mawazo ya kujidhuru?")
    assert t == "conversation_turn"


def test_a_quote_from_a_translation_becomes_translation_candidate():
    t, _ = _type_after("Only God knows.")
    assert t == "translation_candidate"


def test_a_quote_from_nowhere_becomes_background_knowledge():
    t, _ = _type_after("speakers in this region often mean resignation")
    assert t == "model_background_knowledge"


def test_the_claim_survives_re_attribution():
    """Nothing is dropped: the sense keeps its evidence, correctly labelled."""
    out = conform.sense(_sense("Kuna siku nafikiri afadhali nisiwepo"), "m", [], sources=SOURCES)
    assert len(out["evidence"]) == 1
    assert out["evidence"][0]["quote"] == "Kuna siku nafikiri afadhali nisiwepo"


def test_punctuation_and_case_do_not_cause_false_re_attribution():
    t, _ = _type_after("mwenyezi mungu tu.")
    assert t == "utterance_span"


def test_the_check_is_skipped_when_no_sources_are_supplied():
    out = conform.sense(_sense("anything at all"), "m", [])
    assert out["evidence"][0]["type"] == "utterance_span"


# ───────────────────────── the banner's grounding line ─────────────────────────

def _pkg(evidence_types):
    senses = [{"sense_id": f"S{i}", "model_ref": "m", "category": "risk_or_safety",
               "self_reported_plausibility": 0.8,
               "evidence": [{"type": et, "ref": "", "quote": "q"}]}
              for i, et in enumerate(evidence_types, 1)]
    return {"utterance_ref": {"utterance_id": "T"}, "package_id": "P", "status": "awaiting_review",
            "L4_interpretation": {"candidates": senses},
            "L5_agreement": {"n_models": 3, "sense_clusters": [
                {"cluster_id": "C1", "category": "risk_or_safety", "label": "wish to be gone",
                 "standing": "majority", "supporting_models": ["a", "b"],
                 "member_sense_ids": [s["sense_id"] for s in senses]}]},
            "L7_review_signals": {"risk_flags": ["safety_relevant_reading"], "review_priority": "high",
                                  "safety_signals": {"fired": False, "categories": [], "matches": []}}}


def test_banner_says_when_the_reading_quotes_the_utterance():
    out = "\n".join(review._model_risk_banner(_pkg(["utterance_span", "utterance_span"])))
    assert "2 quotes from the utterance itself" in out


def test_banner_says_when_the_reading_rests_on_other_turns():
    """The kiswa-story-v1 signature: a risk reading grounded in a different turn."""
    out = "\n".join(review._model_risk_banner(_pkg(["conversation_turn", "conversation_turn"])))
    assert "not from this utterance" in out


def test_banner_names_senses_resting_only_on_background_knowledge():
    out = "\n".join(review._model_risk_banner(_pkg(["model_background_knowledge"])))
    assert "background knowledge" in out


def test_banner_warns_that_plausibility_is_poorly_calibrated():
    out = "\n".join(review._model_risk_banner(_pkg(["utterance_span"])))
    assert "poorly calibrated" in out


# ───────────────────────── SSSOM cardinality ─────────────────────────

def _rows(tmp_path):
    out = tmp_path / "ap"
    root = Path(__file__).resolve().parents[1]
    import subprocess
    subprocess.run([sys.executable, "-m", "mr_farajamh.cli", "run", "--input", "pilot/utterances.jsonl",
                    "--out", str(out), "--fixture"], cwd=root, check=True, capture_output=True)
    subprocess.run([sys.executable, "-m", "mr_farajamh.cli", "approve", "--out", str(out),
                    "--decisions", "pilot/review_decisions_SIMULATED.jsonl", "--demo-placeholders"],
                   cwd=root, check=True, capture_output=True)
    lines = [l for l in (out / "approved" / "mappings.sssom.tsv").read_text(encoding="utf-8").splitlines()
             if not l.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def test_gap_rows_are_one_to_zero_and_mapped_rows_one_to_one(tmp_path):
    rows = _rows(tmp_path)
    assert rows, "no SSSOM rows produced"
    for r in rows:
        want = "1:0" if r["object_id"] == "sssom:NoTermFound" else "1:1"
        assert r["mapping_cardinality"] == want, f"{r['subject_id']} -> {r['object_id']}"
    assert any(r["mapping_cardinality"] == "1:0" for r in rows), "no gap row in the demo set"


def test_cardinality_is_a_declared_column(tmp_path):
    assert "mapping_cardinality" in approve.SSSOM_COLS
    assert "mapping_cardinality" in _rows(tmp_path)[0]
