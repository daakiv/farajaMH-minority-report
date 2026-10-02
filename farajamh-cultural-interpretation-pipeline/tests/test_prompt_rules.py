"""Prompt rules that came from measured failures, so they do not regress silently.

example-v2 (2 October 2026): 25 of 70 proposed senses used `risk_or_safety` as their sense_key — every
risk sense, all three models, all twelve utterances. The cluster label derives from sense_key and the
label is a terminology search term, so the search string for a risk cluster was the literal enum text.
gemma3:12b separately returned a rank-1 concept AND no_adequate_match on the same cluster.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES = {"emotional_state", "cognitive_process", "somatic_experience", "spiritual_or_supernatural",
              "social_or_relational", "clinical_symptom", "risk_or_safety", "other"}


def interpret() -> str:
    return (ROOT / "prompts" / "interpret.md").read_text(encoding="utf-8")


def rank() -> str:
    return (ROOT / "prompts" / "rank_concepts.md").read_text(encoding="utf-8")


def test_sense_key_may_not_be_a_category_value():
    t = interpret()
    assert "must NOT be one of the category values" in t
    assert "`risk_or_safety`" in t and "`somatic experience`" in t


def test_the_reason_is_given_so_a_model_can_act_on_it():
    """A rule a model is told the purpose of is followed more often than a bare prohibition."""
    assert "becomes the search term" in interpret()


def test_the_risk_rule_names_the_sense_rather_than_handing_over_the_category_string():
    t = interpret()
    assert "whose CATEGORY is `risk_or_safety`" in t, "the MUST clause must not read as naming the sense"
    assert "never `risk_or_safety`" in t


@pytest.mark.parametrize("example", ["wish not to be here", "thoughts of dying", "harm to self"])
def test_risk_senses_have_naming_examples(example):
    """Without an example for a risk sense, models reuse the only string the section gives them."""
    assert example in interpret()


def test_no_sense_key_example_in_the_prompt_is_itself_a_category():
    """The examples are what models copy, so none of them may demonstrate the fault."""
    line = next(l for l in interpret().splitlines() if l.strip().startswith("- sense_key:"))
    quoted = {q.strip().lower().replace(" ", "_") for q in re.findall(r'"([^"]+)"', line)}
    offenders = quoted & CATEGORIES
    assert not offenders, f"sense_key examples name categories: {offenders}"


def test_the_risk_rule_still_overrides_and_cannot_be_argued_away():
    """Guardrails from the 26 September safety failure must survive edits to this section."""
    t = interpret()
    assert "overrides" in t
    assert "not a literal statement of risk" in t
    assert "Always err towards proposing the sense." in t


def test_ranker_cannot_return_a_ranking_and_no_adequate_match_together():
    t = rank()
    assert "mutually exclusive" in t
    assert "`ranked` must be empty" in t


def test_ranker_guardrails_survive():
    t = rank()
    assert "Start from the assumption that NONE" in t
    assert "Terror" in t and "different emotion" in t
    assert "system | id | label | definition" in t
