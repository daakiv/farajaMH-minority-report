"""Guards for the two things that can silently put a false claim into a published artefact:

  1. A mapping set that declares CC-BY-4.0 while carrying identifiers from a terminology we are not
     licensed to redistribute.
  2. A mapping whose object_source_version is a placeholder, which reads like a pin and is not one.
"""
from __future__ import annotations

import json

import pytest

from mr_farajamh import terminology
from mr_farajamh.approve import NON_REDISTRIBUTABLE_PREFIXES, build_outputs


def _package(package_id="MRP-T-1", candidates=None):
    return {
        "package_id": package_id,
        "status": "awaiting_review",
        "L1_original": {"expression_span": {"text": "afadhali nisiwepo"},
                        "context_as_received": {"dialect_declared": "standard", "region": "KE-western"}},
        "L2_normalisation": {"normalised_expression": "afadhali nisiwepo", "language_id": "sw"},
        "L5_agreement": {"sense_clusters": [{"cluster_id": "C1", "label": "sadness", "category": "emotional_state"}]},
        "L6_concept_candidates": {"per_cluster": [{"cluster_id": "C1", "candidates": candidates or [
            {"id": "MFOEM:000056", "system_version": "2025-03-01"},
            {"id": "SCTID:310190000", "system_version": "http://snomed.info/sct/900000000000207008/version/20251017"},
        ]}]},
    }


def _decision(concepts, package_id="MRP-T-1"):
    return {
        "decision_id": "D-1", "package_id": package_id, "final": True,
        "reviewer": {"reviewer_id": "fmhr:r1"}, "decided_at": "2026-10-01T09:00:00+00:00",
        "local_concept_action": {"action": "create", "local_concept_id": "FMHLC:0001",
                                 "pref_label_sw": "afadhali nisiwepo", "pref_label_en": "better if I were not here",
                                 "definition": "x"},
        "layer_decisions": {"translation": {"final_translation": "I wish I weren't here"},
                            "interpretation": {"accepted_cluster_ids": ["C1"], "clinical_status": "unclear", "note": ""},
                            "concepts": concepts},
    }


def _rows(out):
    lines = [ln for ln in (out / "mappings.sssom.tsv").read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    header = lines[0].split("\t")
    return [dict(zip(header, ln.split("\t"))) for ln in lines[1:] if ln.strip()]


def _header(out):
    return [ln for ln in (out / "mappings.sssom.tsv").read_text(encoding="utf-8").splitlines() if ln.startswith("#")]


# --- the guard -------------------------------------------------------------------------------

def test_sctid_mapping_is_withheld_and_mfoem_is_kept(tmp_path):
    decisions = [_decision([
        {"decision": "approve", "id": "MFOEM:000056", "label": "sadness", "predicate_id": "skos:broadMatch"},
        {"decision": "approve", "id": "SCTID:310190000", "label": "Mental health counselor", "predicate_id": "skos:broadMatch"},
    ])]
    summary = build_outputs({"MRP-T-1": _package()}, decisions, tmp_path, "0.2.5")
    objects = [r["object_id"] for r in _rows(tmp_path)]
    assert "MFOEM:000056" in objects
    assert "SCTID:310190000" not in objects
    assert summary["withheld"] == 1
    assert summary["sssom_rows"] == 1


def test_withheld_decision_is_recorded_not_lost(tmp_path):
    decisions = [_decision([
        {"decision": "approve", "id": "SCTID:310190000", "label": "Mental health counselor", "predicate_id": "skos:broadMatch"},
    ])]
    build_outputs({"MRP-T-1": _package()}, decisions, tmp_path, "0.2.5")
    held = [json.loads(ln) for ln in (tmp_path / "withheld_mappings.jsonl").read_text(encoding="utf-8").splitlines() if ln.strip()]
    assert len(held) == 1
    assert held[0]["object_id"] == "SCTID:310190000"
    assert held[0]["subject_id"] == "FMHLC:0001"
    assert held[0]["decision"] == "approve"
    assert held[0]["prefix"] == "SCTID"


def test_mapping_set_states_that_it_is_incomplete(tmp_path):
    decisions = [_decision([
        {"decision": "approve", "id": "SCTID:310190000", "label": "x", "predicate_id": "skos:broadMatch"},
    ])]
    build_outputs({"MRP-T-1": _package()}, decisions, tmp_path, "0.2.5")
    comment = " ".join(_header(tmp_path))
    assert "not licensed for redistribution" in comment
    assert "SCTID" in comment
    assert "withheld_mappings.jsonl" in comment


def test_absence_rows_are_not_withheld(tmp_path):
    """sssom:NoTermFound against SNOMED names no SNOMED concept. The gap is ours to publish."""
    decisions = [_decision([
        {"decision": "no_adequate_concept", "system": "SNOMEDCT", "cluster_id": "C1",
         "justification": "nothing adequate", "predicate_id": "skos:exactMatch"},
    ])]
    summary = build_outputs({"MRP-T-1": _package()}, decisions, tmp_path, "0.2.5")
    rows = _rows(tmp_path)
    assert len(rows) == 1
    assert rows[0]["object_id"] == "sssom:NoTermFound"
    assert rows[0]["object_source"] == "http://snomed.info/sct"
    assert rows[0]["mapping_cardinality"] == "1:0"
    assert summary["withheld"] == 0
    assert summary["gaps"] == 1


def test_negative_assertion_to_a_blocked_system_is_also_withheld(tmp_path):
    """predicate_modifier=Not still publishes the identifier, so it is withheld too."""
    decisions = [_decision([
        {"decision": "reject", "negative_assertion": True, "id": "SCTID:310190000", "label": "x",
         "predicate_id": "skos:exactMatch"},
    ])]
    summary = build_outputs({"MRP-T-1": _package()}, decisions, tmp_path, "0.2.5")
    assert summary["sssom_rows"] == 0
    assert summary["withheld"] == 1


def test_guard_is_overridable_when_a_licence_exists(tmp_path):
    decisions = [_decision([
        {"decision": "approve", "id": "SCTID:310190000", "label": "x", "predicate_id": "skos:broadMatch"},
    ])]
    summary = build_outputs({"MRP-T-1": _package()}, decisions, tmp_path, "0.2.5", non_redistributable=set())
    rows = _rows(tmp_path)
    assert summary["withheld"] == 0
    assert rows[0]["object_id"] == "SCTID:310190000"
    assert rows[0]["object_source_version"] == "http://snomed.info/sct/900000000000207008/version/20251017"


def test_sctid_is_blocked_by_default():
    assert "SCTID" in NON_REDISTRIBUTABLE_PREFIXES
    assert "MFOEM" not in NON_REDISTRIBUTABLE_PREFIXES
    assert "MFOMD" not in NON_REDISTRIBUTABLE_PREFIXES


# --- versions --------------------------------------------------------------------------------

@pytest.mark.parametrize("value", [None, "", "   ", "<pin release>", "<version>"])
def test_placeholder_versions_are_recognised(value):
    assert terminology.is_unpinned_version(value) is True


@pytest.mark.parametrize("value", ["2025-03-01", "http://snomed.info/sct/900000000000207008/version/20251017"])
def test_real_versions_are_left_alone(value):
    assert terminology.is_unpinned_version(value) is False


def test_version_comes_from_versionIri_not_the_null_version_field(monkeypatch):
    """OLS reports the release in config.versionIri and leaves version null."""
    monkeypatch.setattr(terminology, "fetch_json", lambda *a, **k: {
        "version": None,
        "config": {"version": None, "versionIri": "http://snomed.info/sct/900000000000207008/version/20251017"},
    })
    assert terminology.ols_ontology_version("https://x/api", "snomed") == \
        "http://snomed.info/sct/900000000000207008/version/20251017"


def test_unresolvable_version_is_recorded_as_unversioned(monkeypatch):
    def boom(*a, **k):
        raise RuntimeError("no network")
    monkeypatch.setattr(terminology, "fetch_json", boom)
    c = terminology.OLSClient("https://x/api", "mfoem")
    assert c.version == terminology.UNVERSIONED


def test_placeholder_version_in_config_is_resolved(monkeypatch):
    monkeypatch.setattr(terminology, "fetch_json", lambda *a, **k: {"config": {"versionIri": "v-2025-10-17"}})
    c = terminology.OLSClient("https://x/api", "snomed", "<pin release>")
    assert c.version == "v-2025-10-17"


def test_explicit_version_skips_the_lookup(monkeypatch):
    def boom(*a, **k):
        raise AssertionError("should not have called the network")
    monkeypatch.setattr(terminology, "fetch_json", boom)
    c = terminology.OLSClient("https://x/api", "mfoem", "2025-03-01")
    assert c.version == "2025-03-01"


# --- CURIEs ----------------------------------------------------------------------------------

def test_ols_snomed_hit_becomes_an_sctid_curie(monkeypatch):
    monkeypatch.setattr(terminology, "fetch_json", lambda *a, **k: {"response": {"docs": [
        {"iri": "http://snomed.info/id/310190000", "obo_id": "SNOMED:310190000", "label": "Mental health counselor"},
    ]}})
    c = terminology.OLSClient("https://x/api", "snomed", "v1", system="SNOMEDCT", prefix="SCTID")
    hit = c.search("mental health")[0]
    assert hit["id"] == "SCTID:310190000"
    assert hit["system"] == "SNOMEDCT"
    assert hit["system_version"] == "v1"


def test_mfoem_curies_are_unchanged_without_a_prefix(monkeypatch):
    monkeypatch.setattr(terminology, "fetch_json", lambda *a, **k: {"response": {"docs": [
        {"iri": "http://purl.obolibrary.org/obo/MFOEM_000056", "obo_id": "MFOEM:000056", "label": "sadness"},
    ]}})
    c = terminology.OLSClient("https://x/api", "mfoem", "v1", system="MFOEM")
    assert c.search("sadness")[0]["id"] == "MFOEM:000056"


def test_curie_falls_back_to_the_iri_when_obo_id_is_absent(monkeypatch):
    monkeypatch.setattr(terminology, "fetch_json", lambda *a, **k: {"response": {"docs": [
        {"iri": "http://snomed.info/id/310190000", "label": "x"},
    ]}})
    c = terminology.OLSClient("https://x/api", "snomed", "v1", prefix="SCTID")
    assert c.search("x")[0]["id"] == "SCTID:310190000"


def test_hits_with_no_identifier_are_dropped(monkeypatch):
    monkeypatch.setattr(terminology, "fetch_json", lambda *a, **k: {"response": {"docs": [
        {"label": "no id at all"},
        {"iri": "http://snomed.info/id/1", "obo_id": "SNOMED:1", "label": "fine"},
    ]}})
    c = terminology.OLSClient("https://x/api", "snomed", "v1", prefix="SCTID")
    assert [h["id"] for h in c.search("x")] == ["SCTID:1"]
