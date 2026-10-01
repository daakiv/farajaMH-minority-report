"""print_summary must survive a package built with back-translation disabled.

`models.back_translation: "off"` has been the default since v0.2.4 — small models produce ungrammatical
Swahili, so the similarity score measured model competence rather than translation fidelity. With it off,
pipeline.py never sets `back_translation` on a translation candidate. cmd_run does not call print_summary,
so this only surfaced on `try`, where it crashed AFTER the package and review card had been written.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mr_farajamh import cli  # noqa: E402


def _pkg(translation):
    return {
        "utterance_ref": {"utterance_id": "T"}, "package_id": "P", "status": "awaiting_review",
        "L1_original": {"original_text": "Moyo wangu unaniuma", "expression_span": {"text": "Moyo wangu unaniuma"},
                        "context_as_received": {"country": "KE", "region": "KE-nairobi", "dialect_declared": "standard",
                                                "speaker_role": "participant", "setting": "chat_platform",
                                                "negation": {"value": "affirmed"}, "temporality": {"value": "current"},
                                                "attribution": {"value": "self"}}},
        "L2_normalisation": {"normalised_text": "Moyo wangu unaniuma", "normalised_expression": "Moyo wangu unaniuma",
                             "edits": [], "language_id": "sw"},
        "L3_translation": {"candidates": [translation]},
        "L4_interpretation": {"candidates": []},
        "L5_agreement": {"n_models": 3, "sense_clusters": [], "category_support": []},
        "L6_concept_candidates": {"per_cluster": []},
        "L7_review_signals": {"review_priority": "low", "risk_flags": [], "confidence_components": {},
                              "suggested_reviewer_roles": [], "nonconformances": []},
        "provenance": {"backend_mode": "live"},
    }


BASE = {"candidate_id": "T1", "model_ref": "gemma3:12b", "literal_gloss": "Heart my is hurting-me",
        "idiomatic_translation": "My heart aches.", "preserved_terms": [], "uncertainty_note": ""}


def test_summary_survives_back_translation_disabled(capsys):
    cli.print_summary(_pkg(dict(BASE)))
    out = capsys.readouterr().out
    assert "not run" in out and "disabled" in out
    assert "My heart aches." in out


def test_summary_prints_a_similarity_when_one_exists(capsys):
    t = dict(BASE) | {"back_translation": {"by_model": "qwen2.5:7b", "text": "My heart hurts",
                                           "similarity_to_normalised": 0.62}}
    cli.print_summary(_pkg(t))
    assert "similarity 0.62" in capsys.readouterr().out


def test_summary_reports_an_unassessed_back_translation(capsys):
    """Degenerate output is recorded as not assessed rather than scored zero (v0.2, DESIGN §10)."""
    t = dict(BASE) | {"back_translation": {"by_model": "qwen2.5:7b", "text": "Ndiyo kusimamia kusimamia",
                                           "similarity_to_normalised": None,
                                           "note": "output unusable for comparison (degenerate or too short)"}}
    cli.print_summary(_pkg(t))
    assert "unusable for comparison" in capsys.readouterr().out
