"""Terminology retrieval. Identifiers enter the package ONLY through these clients (policy D3).

Live clients:
  - SnowstormClient: SNOMED CT via a licensed Snowstorm instance (IHTSDO open-source terminology server).
  - OLSClient: MFOEM via EMBL-EBI OLS4 (or swap for BioPortal via upstream ontoportal.OntoPortalClient).
Check both endpoints against your deployment before the pilot; they are written to the public API docs
but were not called from this sandbox.

FixtureTerminology returns PLACEHOLDER candidates (ids like SCTID:LOOKUP-feeling-sad, id_verified=false).
They copy the '<lookup>' convention in the v10 diagram and are not real codes.
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

RETRIES = 3
BACKOFF = 4  # seconds, doubled after each failed attempt


def fetch_json(url: str, headers: dict | None = None, timeout: int = 30, retries: int = RETRIES) -> dict:
    """GET with retries. Network failures are common on unstable links; a retry is cheaper than
    losing a whole run. Raises the last error if every attempt fails."""
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers or {"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read())
        except Exception as e:  # noqa: BLE001 - any network or parse failure is retryable here
            last = e
            if attempt < retries - 1:
                wait = BACKOFF * (2 ** attempt)
                print(f"    terminology lookup failed ({type(e).__name__}); retrying in {wait}s")
                time.sleep(wait)
    raise last


class SnowstormClient:
    system = "SNOMEDCT"

    def __init__(self, endpoint: str, branch: str, version: str, ecl_scope: str | None = None, limit: int = 8):
        self.endpoint, self.branch, self.version, self.ecl, self.limit = endpoint.rstrip("/"), branch, version, ecl_scope, limit

    def search(self, query: str) -> list[dict]:
        params = {"term": query, "activeFilter": "true", "limit": self.limit}
        if self.ecl:
            params["ecl"] = self.ecl
        url = f"{self.endpoint}/{self.branch}/concepts?{urllib.parse.urlencode(params)}"
        data = fetch_json(url, {"Accept": "application/json", "Accept-Language": "en"})
        return [{"system": self.system, "id": f"SCTID:{it['conceptId']}",
                 "label": (it.get("pt") or it.get("fsn") or {}).get("term", ""),
                 "id_verified": True, "retrieved_from": self.endpoint, "system_version": self.version}
                for it in data.get("items", [])]


class OLSClient:
    system = "MFOEM"

    def __init__(self, endpoint: str, ontology: str, version: str, limit: int = 8):
        self.endpoint, self.ontology, self.version, self.limit = endpoint.rstrip("/"), ontology, version, limit

    def search(self, query: str) -> list[dict]:
        params = {"q": query, "ontology": self.ontology, "rows": self.limit, "type": "class", "local": "true"}
        data = fetch_json(f"{self.endpoint}/search?{urllib.parse.urlencode(params)}")
        return [{"system": self.system, "id": d.get("obo_id") or d.get("iri"), "label": d.get("label", ""),
                 "id_verified": True, "retrieved_from": self.endpoint, "system_version": self.version}
                for d in data.get("response", {}).get("docs", [])]


class FixtureTerminology:
    def __init__(self, path: Path):
        self.data = json.loads(Path(path).read_text(encoding="utf-8"))

    def search_all(self, query: str) -> list[dict]:
        out = []
        for system, labels in self.data.get(query, {}).items():
            for lab in labels:
                slug = lab.lower().replace(" ", "-").replace("/", "-")
                prefix = "SCTID" if system == "SNOMEDCT" else system
                out.append({"system": system, "id": f"{prefix}:LOOKUP-{slug}", "label": f"<lookup: {lab}>",
                            "id_verified": False, "retrieved_from": "fixture-placeholder", "system_version": "placeholder"})
        return out


class TerminologyHub:
    """Queries every configured system with the same query and merges results."""

    def __init__(self, clients: list | None = None, fixture: FixtureTerminology | None = None):
        self.clients, self.fixture = clients or [], fixture
        self.errors: list[dict] = []  # systems that could not be reached, per query

    def describe(self) -> list[dict]:
        if self.fixture:
            return [{"system": "SNOMEDCT+MFOEM", "version": "placeholder", "endpoint": "fixture-placeholder"}]
        return [{"system": c.system, "version": c.version, "endpoint": c.endpoint} for c in self.clients]

    def search(self, query: str) -> list[dict]:
        """Returns whatever could be retrieved. A system that cannot be reached is recorded in
        self.errors and left out, so a network failure degrades the package instead of losing the run."""
        if self.fixture:
            res = self.fixture.search_all(query)
        else:
            res = []
            for c in self.clients:
                try:
                    res += c.search(query)
                except Exception as e:  # noqa: BLE001
                    self.errors.append({"system": c.system, "query": query, "error": f"{type(e).__name__}: {e}"})
                    print(f"    WARNING: {c.system} could not be reached for '{query}'. "
                          f"Recorded as a retrieval failure; candidates for this meaning are incomplete.")
        for i, r in enumerate(res):
            r["retrieval_query"], r["retrieval_rank"] = query, i + 1
        return res
