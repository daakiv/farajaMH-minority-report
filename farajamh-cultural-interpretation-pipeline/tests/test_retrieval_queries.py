"""Regression tests for the snomed-v1 retrieval failure (2026-10-01).

Cluster C3 of KISWA-STORY-01 was a unanimous risk_or_safety reading. Its search string was the literal
enum text "risk_or_safety", which retrieved SCTID:22071000175105 "Behavior poses safety risk to staff
(finding)" as the ONLY candidate — a concept about danger to clinicians offered for a reading about
danger to the speaker.
"""
from __future__ import annotations

from mr_farajamh.pipeline import retrieval_queries


def test_category_only_label_is_not_searched():
    """The exact C3 case: label and category are both risk_or_safety."""
    cluster = {"cluster_id": "C3", "label": "risk_or_safety", "category": "risk_or_safety"}
    rep = {"gloss": "The speaker's statement expresses a degree of distress that warrants concern for "
                    "their well-being."}
    qs = retrieval_queries(cluster, rep)
    assert qs == ["The speaker's statement expresses a degree of distress that warrants concern for their well-being."]
    assert not any("risk_or_safety" in q for q in qs)


def test_underscores_never_reach_the_service():
    cluster = {"cluster_id": "C9", "label": "desire_for_absence", "category": "emotional_state"}
    rep = {"gloss": "A wish not to exist"}
    qs = retrieval_queries(cluster, rep)
    assert qs[0] == "desire for absence"
    assert all("_" not in q for q in qs)


def test_a_real_label_is_kept_and_leads():
    cluster = {"cluster_id": "C1", "label": "sadness", "category": "emotional_state"}
    rep = {"gloss": "The speaker expresses a feeling of sadness or dejection."}
    assert retrieval_queries(cluster, rep) == ["sadness",
                                               "The speaker expresses a feeling of sadness or dejection."]


def test_label_equal_to_gloss_is_searched_once():
    cluster = {"cluster_id": "C1", "label": "worry", "category": "cognitive_process"}
    assert retrieval_queries(cluster, {"gloss": "worry"}) == ["worry"]


def test_category_match_is_case_and_space_insensitive():
    cluster = {"cluster_id": "C3", "label": "Risk Or Safety", "category": "risk_or_safety"}
    assert retrieval_queries(cluster, {"gloss": "at risk of self-harm"}) == ["at risk of self-harm"]


def test_falls_back_to_the_category_as_a_phrase_when_nothing_else_exists(capsys):
    """Retrieving nothing is worse for a reviewer than a warned low-precision search."""
    cluster = {"cluster_id": "C3", "label": "risk_or_safety", "category": "risk_or_safety"}
    assert retrieval_queries(cluster, {"gloss": ""}) == ["risk or safety"]
    assert "low precision" in capsys.readouterr().out


def test_no_label_and_no_gloss_and_no_category_searches_nothing():
    assert retrieval_queries({"cluster_id": "C4"}, {}) == []


def test_missing_gloss_key_does_not_raise():
    cluster = {"cluster_id": "C1", "label": "sadness", "category": "emotional_state"}
    assert retrieval_queries(cluster, {}) == ["sadness"]
