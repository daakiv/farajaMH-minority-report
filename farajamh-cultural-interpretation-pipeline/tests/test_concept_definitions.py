"""Definitions must reach the ranking stage.

On TRY-ED93AEBF (2026-10-01) the ranking prompt was given labels only. MFOEM:000056 "sadness",
MFOEM:000182 "canonical sad facial expression" and MFOEM:000188 "canonical sad voice utterance" sat
indistinguishably in one list offered for an emotional-state reading, and llama3.1:8b proposed a
relatedMatch to MFOMD:0000149 "mixed episode". OLS serves definitions for both ontologies; the client
was discarding them.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from mr_farajamh import terminology
from mr_farajamh.pipeline import concept_line

ROOT = Path(__file__).resolve().parent.parent

# Exactly as EBI OLS4 returned them on 2026-10-01 for q=sadness&ontology=mfoem.
MFOEM_DOCS = [
    {"iri": "http://purl.obolibrary.org/obo/MFOEM_000056", "obo_id": "MFOEM:000056", "label": "sadness",
     "description": ["A negative emotion felt when an event is appraised as unpleasant and resulting in loss or failure."]},
    {"iri": "http://purl.obolibrary.org/obo/MFOEM_000182", "obo_id": "MFOEM:000182",
     "label": "canonical sad facial expression",
     "description": ["The canonical facial expression associated with the experience of sadness. "]},
]
# And for q=sadness&ontology=snomed — description is an empty list on every concept.
SNOMED_DOCS = [
    {"iri": "http://snomed.info/id/72323006", "obo_id": "SNOMED:72323006",
     "label": "Saddle-billed stork", "description": []},
]


# --- extraction -------------------------------------------------------------------------------

def test_definition_is_lifted_from_the_description_list():
    assert terminology.concept_definition(MFOEM_DOCS[0]) == \
        "A negative emotion felt when an event is appraised as unpleasant and resulting in loss or failure."


def test_trailing_whitespace_in_a_definition_is_normalised():
    """MFOEM:000182's definition ships with a trailing space."""
    out = terminology.concept_definition(MFOEM_DOCS[1])
    assert out == "The canonical facial expression associated with the experience of sadness."
    assert out == out.strip()


@pytest.mark.parametrize("doc", [{"description": []}, {"description": None}, {"description": [""]}, {}])
def test_missing_definitions_give_an_empty_string_not_an_error(doc):
    assert terminology.concept_definition(doc) == ""


def test_a_plain_string_description_is_accepted():
    assert terminology.concept_definition({"description": "a definition"}) == "a definition"


# --- clients ----------------------------------------------------------------------------------

def test_ols_candidates_carry_their_definition(monkeypatch):
    monkeypatch.setattr(terminology, "fetch_json", lambda *a, **k: {"response": {"docs": MFOEM_DOCS}})
    hits = terminology.OLSClient("https://x/api", "mfoem", "v1", system="MFOEM").search("sadness")
    assert hits[0]["definition"].startswith("A negative emotion")
    assert hits[1]["definition"].startswith("The canonical facial expression")


def test_snomed_through_ols_carries_an_empty_definition(monkeypatch):
    """Not an error — OLS serves no definitions for SNOMED CT. The key must still be present."""
    monkeypatch.setattr(terminology, "fetch_json", lambda *a, **k: {"response": {"docs": SNOMED_DOCS}})
    hit = terminology.OLSClient("https://x/api", "snomed", "v1", system="SNOMEDCT", prefix="SCTID").search("sadness")[0]
    assert hit["definition"] == ""
    assert hit["id"] == "SCTID:72323006"


def test_codebook_definitions_are_no_longer_dropped(tmp_path):
    f = tmp_path / "codebook.csv"
    f.write_text("code,label,definition,synonyms\nLOW_MOOD,low mood,Persistent sadness or flat affect,sadness|feeling down\n",
                 encoding="utf-8")
    hit = terminology.CodebookClient(f, "FARAJAMH_LOCAL", "v1", prefix="FMHLC").search("low mood sadness")[0]
    assert hit["definition"] == "Persistent sadness or flat affect"


def test_fixture_candidates_declare_no_definition():
    fx = terminology.FixtureTerminology(ROOT / "tests" / "_fixture_terms.json") if \
        (ROOT / "tests" / "_fixture_terms.json").exists() else None
    if fx is None:
        pytest.skip("fixture file not present in this checkout")
    assert all(h["definition"] == "" for h in fx.search_all("sadness"))


# --- what the ranker is shown -----------------------------------------------------------------

def test_the_two_concepts_a_label_cannot_separate_are_separated_by_definition():
    lines = [concept_line({"system": "MFOEM", "id": "MFOEM:000056", "label": "sadness",
                           "definition": "A negative emotion felt when an event is appraised as unpleasant."}),
             concept_line({"system": "MFOEM", "id": "MFOEM:000182", "label": "canonical sad facial expression",
                           "definition": "The canonical facial expression associated with the experience of sadness."})]
    assert "A negative emotion" in lines[0]
    assert "facial expression associated with" in lines[1]
    assert lines[0] != lines[1]


def test_absent_definition_is_stated_rather_than_left_blank():
    line = concept_line({"system": "SNOMEDCT", "id": "SCTID:72323006", "label": "Saddle-billed stork",
                         "definition": ""})
    assert line.endswith("NO DEFINITION PROVIDED BY THIS TERMINOLOGY")
    assert "| |" not in line


def test_concept_line_survives_a_candidate_with_no_definition_key():
    line = concept_line({"system": "MFOEM", "id": "MFOEM:1", "label": "x"})
    assert "NO DEFINITION" in line


def test_concept_line_collapses_newlines_so_the_listing_stays_one_line_per_concept():
    line = concept_line({"system": "MFOEM", "id": "MFOEM:1", "label": "x",
                         "definition": "first line\n  second line\t third"})
    assert "\n" not in line
    assert "first line second line third" in line


# --- schema and prompt ------------------------------------------------------------------------

def test_schema_declares_definition_on_a_concept_candidate():
    schema = json.loads((ROOT / "schemas" / "candidate_package.schema.json").read_text())
    props = schema["$defs"]["concept_candidate"]["properties"]
    assert props["definition"]["type"] == "string"
    assert "definition" not in schema["$defs"]["concept_candidate"]["required"]


def test_ranking_prompt_tells_the_model_to_use_the_definition():
    t = (ROOT / "prompts" / "rank_concepts.md").read_text()
    assert "system | id | label | definition" in t
    assert "Judge each concept on its DEFINITION" in t
    assert "FACE, not a feeling" in t
    assert "NO DEFINITION PROVIDED BY THIS TERMINOLOGY" in t
    # the pre-existing guardrails must survive the edit
    assert "Start from the assumption that NONE" in t
    assert "Terror" in t and "different emotion" in t
