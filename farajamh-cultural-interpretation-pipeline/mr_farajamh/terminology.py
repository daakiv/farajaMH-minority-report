"""Terminology retrieval. Identifiers enter the package ONLY through these clients (policy D3).

Live clients:
  - SnowstormClient: SNOMED CT via a licensed Snowstorm instance (IHTSDO open-source terminology server).
  - OLSClient: one ontology on an OLS instance — MFOEM, MFOMD and (licence permitting) SNOMED CT via
    EMBL-EBI OLS4, one client each (or swap for BioPortal via upstream ontoportal.OntoPortalClient).
  - CodebookClient: another team's controlled vocabulary, held locally as a file — used to crosswalk
    FarajaMH local concepts onto, for example, an annotation codebook, without touching their pipeline.
Check both endpoints against your deployment before the pilot; they are written to the public API docs
but were not called from this sandbox.

FixtureTerminology returns PLACEHOLDER candidates (ids like SCTID:LOOKUP-feeling-sad, id_verified=false).
They copy the '<lookup>' convention in the v10 diagram and are not real codes.
"""
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

RETRIES = 3
BACKOFF = 4  # seconds, doubled after each failed attempt

UNVERSIONED = "unversioned"


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


def is_unpinned_version(value) -> bool:
    """True when a configured version is not an actual release identifier.

    Covers empty, None, and the '<pin release>' style placeholder that sat in the configs: a
    placeholder in provenance is worse than an absent version, because it reads like a pin.
    """
    if not value:
        return True
    return isinstance(value, str) and (not value.strip() or value.strip().startswith("<"))


def ols_ontology_version(endpoint: str, ontology: str) -> str | None:
    """The release an OLS instance currently serves for one ontology, or None if undeterminable.

    OLS reports the release in `config.versionIri` and leaves the top-level `version` field null, so
    reading `version` alone gets you nothing. For SNOMED CT on EBI OLS4 this returns, for example,
    http://snomed.info/sct/900000000000207008/version/20251017 — module and release date, which is
    exactly what a mapping to a SNOMED identifier needs in order to be unambiguous.

    One extra call per client, at construction. Never raises: failing to resolve a version must
    degrade provenance, not kill a run.
    """
    try:
        data = fetch_json(f"{endpoint.rstrip('/')}/ontologies/{urllib.parse.quote(ontology)}", retries=1)
    except Exception:  # noqa: BLE001 - version resolution is best-effort by design
        return None
    cfg = data.get("config") or {}
    for candidate in (cfg.get("versionIri"), cfg.get("version"), data.get("version")):
        if candidate:
            return str(candidate)
    return None


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
    """One ontology on an OLS instance (EBI OLS4 by default).

    `system` is what the retrieved identifiers are labelled with, and it must come from the config key
    rather than a class constant: with MFOEM and MFOMD both configured, a shared constant would stamp
    every MFOMD concept as MFOEM and the provenance in the package would be wrong.

    `prefix` overrides the CURIE prefix OLS itself reports. Needed where OLS's preferred prefix is not
    the one this pipeline's curie_map declares: OLS returns SNOMED:310190000, while PREFIXES in
    approve.py — and SnowstormClient — use SCTID. Left unset, the OLS-native obo_id is used unchanged,
    which is correct for MFOEM and MFOMD.

    `version` may be left unset or given as a placeholder, in which case the release is resolved from
    the OLS ontology record at construction. Pass a real release string to pin it and skip the call.
    """

    def __init__(self, endpoint: str, ontology: str, version: str | None = None, limit: int = 8,
                 system: str | None = None, prefix: str | None = None):
        self.endpoint, self.ontology, self.limit = endpoint.rstrip("/"), ontology, limit
        self.system = system or ontology.upper()
        self.prefix = prefix
        if is_unpinned_version(version):
            resolved = ols_ontology_version(self.endpoint, self.ontology)
            if resolved is None:
                print(f"    WARNING: no release version available for {self.system} at {self.endpoint}; "
                      f"recording '{UNVERSIONED}'. Mappings to this system will not name a release.")
            self.version = resolved or UNVERSIONED
        else:
            self.version = version

    def _curie(self, doc: dict) -> str | None:
        """CURIE for one OLS search hit, under this client's configured prefix."""
        native = doc.get("obo_id") or ""
        iri = doc.get("iri") or ""
        if not self.prefix:
            return native or iri or None
        local = native.split(":")[-1] if native else iri.rstrip("/").rsplit("/", 1)[-1].rsplit("#", 1)[-1]
        return f"{self.prefix}:{local}" if local else None

    def search(self, query: str) -> list[dict]:
        params = {"q": query, "ontology": self.ontology, "rows": self.limit, "type": "class", "local": "true"}
        data = fetch_json(f"{self.endpoint}/search?{urllib.parse.urlencode(params)}")
        out = []
        for doc in data.get("response", {}).get("docs", []):
            cid = self._curie(doc)
            if not cid:
                continue
            out.append({"system": self.system, "id": cid, "label": doc.get("label", ""),
                        "id_verified": True, "retrieved_from": self.endpoint, "system_version": self.version})
        return out


class CodebookClient:
    """A local controlled vocabulary held in a file — for crosswalking to another team's codebook.

    The annotation team keeps their codebook; we map our local concepts onto it and publish the result
    as an SSSOM set. Nothing about their pipeline has to change, and the mapping is reviewed by the same
    panel under the same rules as any external mapping.

    Identifiers are marked id_verified=True because they come from a file the other team owns and the
    file's version is recorded in provenance — the D3 guarantee is "not invented by a model", not
    "fetched over a network".

    File format: CSV or JSON, one row/object per code, with at least `code` and `label`.
    Optional `definition` and `synonyms` (pipe-separated) widen the match.

        code,label,definition,synonyms
        LOW_MOOD,low mood,"Persistent sadness or flat affect",sadness|feeling down
    """

    def __init__(self, path, system: str, version: str, limit: int = 8, prefix: str | None = None):
        self.system, self.version, self.limit = system, version, limit
        self.prefix = prefix or system
        self.path = Path(path)
        raw = self.path.read_text(encoding="utf-8")
        if self.path.suffix.lower() == ".json":
            rows = json.loads(raw)
        else:
            import csv
            import io
            rows = list(csv.DictReader(io.StringIO(raw)))
        self.codes = []
        for r in rows:
            code, label = (r.get("code") or "").strip(), (r.get("label") or "").strip()
            if not code or not label:
                continue
            syn = [s.strip() for s in (r.get("synonyms") or "").split("|") if s.strip()]
            self.codes.append({"code": code, "label": label, "definition": (r.get("definition") or "").strip(),
                               "haystack": " ".join([label, r.get("definition") or "", *syn]).lower()})

    def search(self, query: str) -> list[dict]:
        """Token-overlap search over label, definition and synonyms.

        Deliberately generous: it is proposing candidates for a human panel to reject, and a missed
        candidate is worse than a spurious one. It is NOT deciding anything.
        """
        q = {w for w in re.findall(r"[\w']+", (query or "").lower()) if len(w) > 2}
        scored = []
        for c in self.codes:
            if not q:
                continue
            hay = set(re.findall(r"[\w']+", c["haystack"]))
            overlap = len(q & hay)
            if overlap:
                scored.append((overlap / len(q), c))
        scored.sort(key=lambda x: -x[0])
        return [{"system": self.system, "id": f"{self.prefix}:{c['code']}", "label": c["label"],
                 "id_verified": True, "retrieved_from": str(self.path), "system_version": self.version}
                for _, c in scored[:self.limit]]


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
