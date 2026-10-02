"""One surface form per meaning before clustering, the card, or a terminology search.

example-v3 (2 October 2026): seven of twelve packages carried clusters that were the same meaning
twice — `wish not to be here` beside `wish_not_to_be_here`, `heart heavy` beside `heart_heaviness` —
each splitting one majority into two minorities. Minority clusters went 21 -> 46 against example-v2.
"""
from __future__ import annotations

import pytest

from mr_farajamh.conform import normalise_sense_key, sense


@pytest.mark.parametrize("raw,expected", [
    ("wish_not_to_be_here", "wish not to be here"),
    ("wish not to be here", "wish not to be here"),
    ("Heart_Heaviness", "heart heaviness"),
    ("heart  heavy", "heart heavy"),
    ("feeling-trapped", "feeling trapped"),
    (" Overwhelmed_By_Stress ", "overwhelmed by stress"),
    ("somatic_experience", "somatic experience"),
    ("god knows", "god knows"),
])
def test_surface_forms_collapse(raw, expected):
    assert normalise_sense_key(raw) == expected


def test_the_exact_v3_pair_collapses():
    assert normalise_sense_key("wish_not_to_be_here") == normalise_sense_key("wish not to be here")


@pytest.mark.parametrize("raw", ["", None])
def test_empty_input_is_survivable(raw):
    assert normalise_sense_key(raw) == ""


def test_apostrophes_survive():
    """A key like "can't cope" must not become two words."""
    assert normalise_sense_key("can't cope") == "can't cope"


def test_morphological_variants_are_NOT_merged_here():
    """Deliberate. Merging `exhausted` with `exhaustion` is the clustering stage's job, on the gloss.
    Doing it by string rule here would hide the clustering question rather than answer it."""
    assert normalise_sense_key("exhausted") != normalise_sense_key("exhaustion")


def test_conform_applies_it_and_records_the_change():
    log = []
    out = sense({"sense_key": "wish_not_to_be_here", "gloss": "g", "rationale": "r",
                 "category": "risk_or_safety", "register": "mixed", "evidence": [],
                 "self_reported_plausibility": 0.5}, "m1", log)
    assert out["sense_key"] == "wish not to be here"
    entry = next(n for n in log if n["field"] == "sense_key")
    assert entry["model_value"] == "wish_not_to_be_here"
    assert entry["used_instead"] == "wish not to be here"


def test_an_already_tidy_key_records_nothing():
    """Nonconformances are a signal; a no-op edit must not add noise to them."""
    log = []
    out = sense({"sense_key": "sadness", "gloss": "g", "rationale": "r", "category": "emotional_state",
                 "register": "mixed", "evidence": [], "self_reported_plausibility": 0.5}, "m1", log)
    assert out["sense_key"] == "sadness"
    assert not [n for n in log if n["field"] == "sense_key"]
