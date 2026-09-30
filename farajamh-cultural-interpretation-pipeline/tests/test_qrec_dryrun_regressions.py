"""Regressions from run qrec-dryrun-v7 (2026-09-29), the first batch over English clinical-interview text.

Two defects, both reproduced here from the cards that showed them:

  QREC-DRY-001  "Not good at all"
      M1 returned "Si nzuri kabisa." — a translation, recorded as asr_correction edits — and the card
      carried a full RISK LANGUAGE banner whose every match sat in the models' own gap notes.

  QREC-DRY-012  "Yes, I do feel like killing people who annoy me"
      All three models read it as risk_or_safety, unanimously, and the card carried no banner at all,
      because no lexicon phrase matched.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mr_farajamh import conform, review  # noqa: E402


def _norm(text, lang_id):
    return {"normalised_text": text, "normalised_expression": text, "language_id": lang_id, "edits": []}


# ────────────────────────── the language guard ──────────────────────────

def test_english_normalised_into_swahili_is_rejected():
    n, log = _norm("Si nzuri kabisa.", "sw"), []
    assert conform.language_changed(n, "Not good at all", "Not good at all", "en-KE", "gemma3:12b", log)
    assert n["normalised_text"] == "Not good at all", "original text must be restored"
    assert n["edits"] == []
    assert log and "translation guard" in log[0]["field"]


def test_the_killing_utterance_is_rejected_too():
    n, log = _norm("Ndio, naona kama ninaweza kuuwa watu wanaonichochea.", "sw"), []
    orig = "Yes, I do feel like killing people who annoy me"
    assert conform.language_changed(n, orig, orig, "en-KE", "gemma3:12b", log)
    assert n["normalised_text"] == orig


def test_plain_swahili_normalisation_passes():
    n, log = _norm("Moyo wangu unaniuma", "sw"), []
    assert not conform.language_changed(n, "Moyo wangu unaniuma", "Moyo wangu unaniuma", "sw-KE", "m", log)
    assert log == []


def test_sheng_and_code_switching_pass():
    """The guard must not punish the mixture it exists to protect."""
    for orig, out, lang_id, declared in [
        ("Niko na stress mob, siwezi lala", "Niko na stress mob, siwezi kulala", "sw-x-sheng", "sw-KE"),
        ("Nina stress sana siku hizi", "Nina stress sana siku hizi", "sw", "sw-TZ"),
        ("Mawazo ni mob, I cant sleep", "Mawazo ni mob, I can't sleep", "sw", "sw-KE"),
    ]:
        n, log = _norm(out, lang_id), []
        assert not conform.language_changed(n, orig, orig, declared, "m", log), orig
        assert n["normalised_text"] == out, "a passing normalisation must not be reverted"


def test_guard_trips_on_wholesale_replacement_even_when_language_id_agrees():
    """A model that translates may still report the source language correctly."""
    n, log = _norm("Si nzuri kabisa.", "en"), []
    assert conform.language_changed(n, "Not good at all", "Not good at all", "en-KE", "m", log)


# ────────────────────────── the two banners ──────────────────────────

def _pkg(risk_flags, clusters, matches, fired=True):
    return {
        "utterance_ref": {"utterance_id": "T"}, "package_id": "P", "status": "awaiting_review",
        "L5_agreement": {"n_models": 3, "sense_clusters": clusters},
        "L7_review_signals": {
            "risk_flags": risk_flags, "review_priority": "high",
            "safety_signals": {"fired": fired, "categories": ["self_harm_or_suicide"],
                               "lexicon_version": "0.2.0-unvalidated", "matches": matches},
        },
    }


def test_lexicon_banner_says_when_hits_are_only_in_model_text():
    """QREC-DRY-001: every match was in a gap note, none in the participant's words."""
    p = _pkg(["risk_language_detected"], [],
             [{"term": "self-harm", "where": "sense/S2/gloss", "context": "…potential self-harm…"},
              {"term": "self-harm", "where": "gap_note/C2", "context": "…potential self-harm…"}])
    out = "\n".join(review._safety_banner(p))
    assert "text the models generated" in out
    assert "not in the participant's own words" in out


def test_lexicon_banner_stays_quiet_about_provenance_when_the_speaker_used_the_words():
    p = _pkg(["risk_language_detected"], [],
             [{"term": "better off dead", "where": "original_text", "context": "…better off dead…"}])
    out = "\n".join(review._safety_banner(p))
    assert "text the models generated" not in out


def test_model_risk_banner_fires_when_the_lexicon_is_silent():
    """QREC-DRY-012: unanimous risk_or_safety, no lexicon match, and previously no banner."""
    clusters = [{"cluster_id": "C2", "category": "risk_or_safety", "label": "thoughts of harming others",
                 "standing": "unanimous", "supporting_models": ["gemma3:12b", "qwen2.5:7b", "llama3.1:8b"]}]
    p = _pkg(["safety_relevant_reading"], clusters, [], fired=False)
    assert review._safety_banner(p) == [], "lexicon banner must stay silent"
    out = "\n".join(review._model_risk_banner(p))
    assert "A RISK READING WAS PROPOSED BY THE MODELS" in out
    assert "3 of 3 models" in out
    assert "thoughts of harming others" in out


def test_model_risk_banner_silent_without_a_risk_cluster():
    p = _pkg(["possible_semantic_gap"], [{"cluster_id": "C1", "category": "emotional_state",
                                          "label": "sadness", "standing": "majority",
                                          "supporting_models": ["a", "b"]}], [], fired=False)
    assert review._model_risk_banner(p) == []


def test_both_banners_can_fire_together():
    clusters = [{"cluster_id": "C1", "category": "risk_or_safety", "label": "suicidal ideation",
                 "standing": "majority", "supporting_models": ["a", "b"]}]
    p = _pkg(["risk_language_detected", "safety_relevant_reading"], clusters,
             [{"term": "better off dead", "where": "original_text", "context": "…"}])
    assert review._safety_banner(p) and review._model_risk_banner(p)
