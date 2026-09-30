"""Two OLS ontologies configured at once must stay distinguishable.

MFOEM and MFOMD are both served by the same OLS instance through the same client class. Before this,
OLSClient.system was a class constant set to "MFOEM", so an MFOMD concept would have been recorded in
the package — and later in the SSSOM row — as having come from MFOEM. The identifier would have been
real and the provenance wrong, which is the harder kind of error to notice.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mr_farajamh.terminology import OLSClient, TerminologyHub  # noqa: E402

OLS = "https://www.ebi.ac.uk/ols4/api"


def test_system_name_comes_from_the_config_key():
    emo = OLSClient(OLS, "mfoem", "v1", 8, system="MFOEM")
    dis = OLSClient(OLS, "mfomd", "v1", 8, system="MFOMD")
    assert (emo.system, dis.system) == ("MFOEM", "MFOMD")
    assert emo.system != dis.system, "two ontologies must not share one system label"


def test_system_falls_back_to_the_ontology_name():
    assert OLSClient(OLS, "mfomd", "v1").system == "MFOMD"


def test_hub_describes_each_system_separately():
    hub = TerminologyHub(clients=[OLSClient(OLS, "mfoem", "2026-01", 8, system="MFOEM"),
                                  OLSClient(OLS, "mfomd", "2020-04", 8, system="MFOMD")])
    systems = {d["system"] for d in hub.describe()}
    assert systems == {"MFOEM", "MFOMD"}


def test_results_carry_their_own_system_and_version(monkeypatch):
    """A retrieved concept must name the ontology it actually came from."""
    import mr_farajamh.terminology as term

    def fake(url, *a, **k):
        onto = "mfomd" if "mfomd" in url else "mfoem"
        return {"response": {"docs": [{"obo_id": f"{onto.upper()}_0000001", "label": f"{onto} concept"}]}}

    monkeypatch.setattr(term, "fetch_json", fake)
    hub = TerminologyHub(clients=[term.OLSClient(OLS, "mfoem", "2026-01", 8, system="MFOEM"),
                                  term.OLSClient(OLS, "mfomd", "2020-04", 8, system="MFOMD")])
    got = {(r["system"], r["id"], r["system_version"]) for r in hub.search("sadness")}
    assert ("MFOEM", "MFOEM_0000001", "2026-01") in got
    assert ("MFOMD", "MFOMD_0000001", "2020-04") in got


def test_shipped_configs_declare_a_client_for_every_terminology():
    """_live_env dispatches on `client`; an entry without one is silently unsearched."""
    for name in ("config/pilot.yaml",):
        cfg = yaml.safe_load((Path(__file__).resolve().parents[1] / name).read_text())
        for system, c in (cfg.get("terminologies") or {}).items():
            assert c.get("client") in {"snowstorm", "ols", "codebook"}, f"{name}: {system} has no usable client"


def test_pilot_config_includes_mfomd():
    cfg = yaml.safe_load((Path(__file__).resolve().parents[1] / "config/pilot.yaml").read_text())
    mfomd = (cfg.get("terminologies") or {}).get("MFOMD")
    assert mfomd, "MFOMD should be configured"
    assert mfomd["client"] == "ols" and mfomd["ontology"] == "mfomd"


# ────────── a configured terminology must be declared everywhere, not just in the config ──────────

def test_every_configured_system_is_allowed_by_the_package_schema():
    """Run kiswa-story-v1 died here: MFOMD was in the config and in the client, but the package
    schema's `system` enum still read ["SNOMEDCT", "MFOEM", "FARAJAMH_LOCAL"]. Concepts were
    retrieved, the package was built, and validation rejected it — after the models had run and
    before anything was written to disk. Config-driven clients need config-driven checks."""
    import json

    root = Path(__file__).resolve().parents[1]
    schema = json.loads((root / "schemas/candidate_package.schema.json").read_text())

    def system_enums(node):
        """Every `system` enum anywhere in the schema — a fixed path is the brittleness that caused this."""
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "system" and isinstance(v, dict) and "enum" in v:
                    yield set(v["enum"])
                yield from system_enums(v)
        elif isinstance(node, list):
            for v in node:
                yield from system_enums(v)

    enums = list(system_enums(schema))
    assert enums, "no `system` enum found in the package schema — has it moved?"
    enum = set.intersection(*enums)
    for name in ("config/pilot.yaml",):
        cfg = yaml.safe_load((root / name).read_text())
        for system in (cfg.get("terminologies") or {}):
            assert system in enum, f"{name} configures {system}, which the package schema will reject"


def test_every_configured_system_can_be_written_as_sssom():
    """A retrieved concept that cannot be given a CURIE prefix cannot be published as a mapping."""
    root = Path(__file__).resolve().parents[1]
    from mr_farajamh.approve import PREFIXES, SOURCES
    cfg = yaml.safe_load((root / "config/pilot.yaml").read_text())
    for system in (cfg.get("terminologies") or {}):
        if system == "SNOMEDCT":
            assert "SCTID" in PREFIXES and "SCTID" in SOURCES
            continue
        assert system in PREFIXES, f"{system} has no CURIE prefix in approve.PREFIXES"
        assert system in SOURCES, f"{system} has no object_source in approve.SOURCES"
