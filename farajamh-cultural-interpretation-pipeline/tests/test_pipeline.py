"""Tests for the rules that must hold whatever the models say."""
import copy
import json
from pathlib import Path

import jsonschema
import pytest
import yaml

from mr_farajamh.approve import ApprovalError, build_outputs
from mr_farajamh.backends import FixtureBackend
from mr_farajamh.pipeline import run_package
from mr_farajamh.policy import PolicyViolation
from mr_farajamh.terminology import FixtureTerminology, TerminologyHub

ROOT = Path(__file__).resolve().parent.parent
UTTS = {json.loads(l)["utterance_id"]: json.loads(l) for l in (ROOT / "pilot/utterances.jsonl").read_text().splitlines()}
SCHEMA = lambda n: json.loads((ROOT / f"schemas/{n}.schema.json").read_text())


@pytest.fixture
def env():
    cfg = yaml.safe_load((ROOT / "config/pilot.yaml").read_text())
    cfg["_run_id"] = "test"
    cfg["models"]["normaliser"] = {"model_ref": "sim-model-A", "family": "f1"}
    cfg["models"]["interpreters"] = [{"model_ref": f"sim-model-{x}", "family": f"f{i}"} for i, x in enumerate("ABC")]
    return cfg, FixtureBackend(ROOT / "pilot/fixtures/simulated_responses.json"), \
        TerminologyHub(fixture=FixtureTerminology(ROOT / "pilot/fixtures/terminology_fixture.json"))


def test_all_inputs_valid():
    for u in UTTS.values():
        jsonschema.validate(u, SCHEMA("utterance_input"))
        assert u["original_text"][u["expression_span"]["start"]:u["expression_span"]["end"]] == u["expression_span"]["text"]


def test_packages_valid_and_never_approved(env):
    for uid, u in UTTS.items():
        p = run_package(u, *env)
        assert p["status"] in ("awaiting_review", "blocked_pending_safety_escalation")
        if p["status"] == "awaiting_review":
            jsonschema.validate(p, SCHEMA("candidate_package"))
            assert p["L1_original"]["original_text"] == u["original_text"]  # original never altered


def test_safety_gate_blocks_until_escalated(env):
    p = run_package(UTTS["PILOT-P08"], *env)
    assert p["status"] == "blocked_pending_safety_escalation" and "L3_translation" not in p


def test_minority_readings_kept(env):
    p = run_package(UTTS["PILOT-P05"], *env)
    labels = {c["label"]: c["standing"] for c in p["L5_agreement"]["sense_clusters"]}
    assert labels["persecutory belief"] == "minority"
    assert "over_medicalisation_risk" in p["L7_review_signals"]["risk_flags"]


def test_negation_and_attribution_surface(env):
    assert "polarity_negated" in run_package(UTTS["PILOT-P09"], *env)["L7_review_signals"]["risk_flags"]
    assert "experiencer_not_speaker" in run_package(UTTS["PILOT-P10"], *env)["L7_review_signals"]["risk_flags"]


def test_ranker_cannot_invent_ids(env):
    cfg, backend, terms = env
    orig = backend._simulated_rank
    backend._simulated_rank = lambda m, k: {"ranked": [{"id": "SCTID:999999", "rank": 1, "proposed_predicate": "skos:exactMatch",
                                                        "rationale": "invented"}], "no_adequate_match": False}
    p = run_package(UTTS["PILOT-P02"], cfg, backend, terms)
    backend._simulated_rank = orig
    ids = {x["id"] for pc in p["L6_concept_candidates"]["per_cluster"] for x in pc["candidates"]}
    assert "SCTID:999999" not in ids
    assert all(not x["ranking"] for pc in p["L6_concept_candidates"]["per_cluster"] for x in pc["candidates"])


def test_model_diversity_enforced(env):
    cfg, backend, terms = env
    cfg = copy.deepcopy(cfg)
    cfg["models"]["interpreters"] = [{"model_ref": f"sim-model-{x}", "family": "same"} for x in "ABC"]
    with pytest.raises(PolicyViolation):
        run_package(UTTS["PILOT-P02"], cfg, backend, terms)


def test_restricted_data_needs_local_host(env):
    u = copy.deepcopy(UTTS["PILOT-P02"])
    u["data_classification"] = "restricted"
    with pytest.raises(PolicyViolation):
        run_package(u, *env)


def test_no_sssom_without_final_decision_and_no_placeholders(env, tmp_path):
    p = run_package(UTTS["PILOT-P02"], *env)
    decisions = [json.loads(l) for l in (ROOT / "pilot/review_decisions_SIMULATED.jsonl").read_text().splitlines()]
    d02 = [d for d in decisions if d["package_id"] == "MRP-PILOT-P02-pilot-dryrun"]
    for d in d02:
        d["package_id"] = p["package_id"]
    nonfinal = [d for d in d02 if not d["final"]]
    assert build_outputs({p["package_id"]: p}, nonfinal, tmp_path, "t", demo_placeholders=True)["sssom_rows"] == 0
    with pytest.raises(ApprovalError):
        build_outputs({p["package_id"]: p}, d02, tmp_path, "t", demo_placeholders=False)
    res = build_outputs({p["package_id"]: p}, d02, tmp_path, "t", demo_placeholders=True)
    assert res == {"local_concepts": 1, "sssom_rows": 2, "gaps": 0}
    assert "\tNot\t" in (tmp_path / "mappings.sssom.tsv").read_text()


def test_terminology_failure_degrades_instead_of_crashing(env, monkeypatch):
    """An unreachable terminology service must not lose the model work already done."""
    cfg, backend, _ = env

    class Dead:
        system = "MFOEM"
        version = "x"
        endpoint = "https://unreachable.invalid"

        def search(self, query):
            raise TimeoutError("read timed out")

    from mr_farajamh.terminology import TerminologyHub
    hub = TerminologyHub(clients=[Dead()])
    p = run_package(UTTS["PILOT-P05"], cfg, backend, hub)
    jsonschema.validate(p, SCHEMA("candidate_package"))
    assert p["status"] == "awaiting_review"
    assert "terminology_lookup_failed" in p["L7_review_signals"]["risk_flags"]
    assert p["L7_review_signals"]["review_priority"] == "high"
    assert all(pc["retrieval_status"].startswith("unavailable") for pc in p["L6_concept_candidates"]["per_cluster"])
    assert p["provenance"]["terminology_errors"]


def test_degenerate_back_translation_is_not_assessed(env):
    """A repeated-word back-translation must not be scored as a mismatch."""
    from mr_farajamh.agreement import back_translation_similarity, looks_degenerate
    assert looks_degenerate("Ndiyo kusimamia kusimamia kusimamia")
    assert back_translation_similarity("Ndiyo kusimamia kusimamia kusimamia", "Moyo wangu unauma") is None
    assert back_translation_similarity("Moyo wangu unauma sana", "Moyo wangu unauma") is not None


def test_back_translation_can_be_switched_off(env):
    cfg, backend, terms = env
    cfg = copy.deepcopy(cfg)
    cfg["models"]["back_translation"] = "off"
    p = run_package(UTTS["PILOT-P02"], cfg, backend, terms)
    jsonschema.validate(p, SCHEMA("candidate_package"))
    assert all("back_translation" not in t for t in p["L3_translation"]["candidates"])
    assert "back_translation_disabled" in p["L7_review_signals"]["risk_flags"]


def test_embeddings_merge_synonymous_senses(env):
    """With embeddings, 'sadness' and 'emotional pain' land in one cluster instead of two."""
    cfg, backend, terms = env
    cfg = copy.deepcopy(cfg)
    cfg["models"]["embedding_model"] = "fake-embed"
    near = {"sadness": [1.0, 0.0], "emotional pain": [0.97, 0.24], "chest heaviness": [0.0, 1.0],
            "morning reluctance": [0.1, 0.99]}
    backend.embed = lambda model, texts: [near.get(t.split(":")[0], [0.5, 0.5]) for t in texts]
    p = run_package(UTTS["PILOT-P02"], cfg, backend, terms)
    assert p["L5_agreement"]["clustering_method"] == "embeddings"
    labels = [c["label"] for c in p["L5_agreement"]["sense_clusters"]]
    assert len(labels) < 3  # the three P02 senses collapse once meaning, not wording, decides
    del backend.embed


def test_unassessed_back_translation_still_validates(env):
    """A 'not assessed' similarity (null) must be allowed by the package schema."""
    cfg, backend, terms = env
    real = backend.generate_json

    def degenerate(model, prompt, key=None):
        if (key or {}).get("stage") == "back_translate":
            return {"text": "Ndiyo kusimamia kusimamia kusimamia"}
        return real(model, prompt, key)

    backend.generate_json = degenerate
    p = run_package(UTTS["PILOT-P02"], cfg, backend, terms)
    backend.generate_json = real
    jsonschema.validate(p, SCHEMA("candidate_package"))
    assert all(t["back_translation"]["similarity_to_normalised"] is None for t in p["L3_translation"]["candidates"])
    assert "back_translation_not_assessed" in p["L7_review_signals"]["risk_flags"]


def test_invalid_model_output_is_repaired_and_recorded(env):
    """Models invent enum values. The run must survive, stay schema-valid, and say what was repaired."""
    cfg, backend, terms = env
    real = backend.generate_json

    def messy(model, prompt, key=None):
        r = real(model, prompt, key)
        if (key or {}).get("stage") == "interpret":
            r["senses"][0]["evidence"].append({"type": "translations", "ref": "T1", "quote": "My heart aches."})
            r["senses"][0]["category"] = "emotional-state"      # wrong spelling
            r["senses"][0]["register"] = "everyday"             # not in the list
            r["senses"][0]["self_reported_plausibility"] = "high"
        return r

    backend.generate_json = messy
    p = run_package(UTTS["PILOT-P02"], cfg, backend, terms)
    backend.generate_json = real
    jsonschema.validate(p, SCHEMA("candidate_package"))
    assert "model_output_coerced" in p["L7_review_signals"]["risk_flags"]
    repaired = {n["field"] for n in p["L7_review_signals"]["nonconformances"]}
    assert {"evidence.type", "category", "register", "self_reported_plausibility"} <= repaired
    raw = {n["model_value"] for n in p["L7_review_signals"]["nonconformances"]}
    assert "translations" in raw and "everyday" in raw     # the raw value is kept, not lost


def test_no_usable_senses_fails_cleanly(env):
    cfg, backend, terms = env
    real = backend.generate_json
    backend.generate_json = lambda model, prompt, key=None: ({"senses": []} if (key or {}).get("stage") == "interpret"
                                                             else real(model, prompt, key))
    p = run_package(UTTS["PILOT-P02"], cfg, backend, terms)
    backend.generate_json = real
    assert p["status"] == "failed"


def test_cross_category_senses_do_not_merge_easily(env):
    """A somatic reading must not be absorbed into an emotional cluster just because the vectors are close."""
    from mr_farajamh.agreement import cluster_senses, finalise_clusters
    senses = [
        {"sense_id": "S1", "model_ref": "m1", "sense_key": "sadness", "gloss": "feeling sad",
         "category": "emotional_state", "register": "everyday_cultural"},
        {"sense_id": "S2", "model_ref": "m2", "sense_key": "emotional pain", "gloss": "emotional pain or distress",
         "category": "emotional_state", "register": "everyday_cultural"},
        {"sense_id": "S3", "model_ref": "m3", "sense_key": "chest pain", "gloss": "literal pain in the chest",
         "category": "somatic_experience", "register": "clinical"},
    ]
    # S3 sits above the same-category bar (0.85) but below the cross-category bar (0.93)
    vectors = {"S1": [1.0, 0.0], "S2": [0.98, 0.2], "S3": [0.8, 0.6]}
    out = finalise_clusters(cluster_senses(senses, 0.34, vectors, 0.85, 0.93), 3, 0.5)
    assert len(out) == 2
    assert {c["category"] for c in out} == {"emotional_state", "somatic_experience"}
    assert any(c["standing"] == "minority" for c in out)


def test_category_support_is_reported(env):
    """Category-level agreement survives models labelling the same reading differently."""
    from mr_farajamh.agreement import category_support
    senses = [{"model_ref": "m1", "category": "emotional_state"}, {"model_ref": "m2", "category": "emotional_state"},
              {"model_ref": "m3", "category": "emotional_state"}, {"model_ref": "m1", "category": "somatic_experience"}]
    out = category_support(senses, 3)
    assert out[0] == {"category": "emotional_state", "models": ["m1", "m2", "m3"], "support_ratio": 1.0}
    assert out[1]["support_ratio"] == 0.333
    p = run_package(UTTS["PILOT-P02"], *env)
    assert p["L5_agreement"]["category_support"]
