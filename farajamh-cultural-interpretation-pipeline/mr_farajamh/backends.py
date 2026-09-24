"""LLM backends.

OllamaBackend follows the upstream Minority Report pattern (Ollama hosts, model-to-host routing, JSON repair)
and adds what FarajaMH needs for replicability: model digest, fixed options/seed, and a host-locality check.

FixtureBackend returns SIMULATED responses from pilot/fixtures so the pipeline mechanics can be tested
without a model server. Fixture responses were written by hand for testing. They are not model outputs
and not validated interpretations.
"""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path


def repair_json(text: str) -> dict:
    """Parse JSON from a model reply; same tolerant strategy as upstream orchestrator._query_model."""
    text = (text or "").strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.M).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.S)
        if m:
            candidate = re.sub(r",\s*([}\]])", r"\1", m.group(0))
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                pass
    raise ValueError(f"Model reply is not parseable JSON: {text[:120]!r}")


class OllamaBackend:
    mode = "live"

    def __init__(self, hosts: list[str], options: dict, host_locality: str = "local_dsa_approved", timeout: int = 300):
        self.hosts = hosts
        self.options = options
        self.host_locality = host_locality
        self.timeout = timeout
        self._alloc: dict[str, str] = {}
        self._digests: dict[str, str] = {}

    def _host_for(self, model: str) -> str:
        # Upstream ModelRouter: allocate each model to the least-loaded host, then keep it there.
        if model not in self._alloc:
            load = {h: 0 for h in self.hosts}
            for h in self._alloc.values():
                load[h] += 1
            self._alloc[model] = min(load, key=load.get)
        return self._alloc[model]

    def _post(self, host: str, path: str, payload: dict) -> dict:
        req = urllib.request.Request(host.rstrip("/") + path, data=json.dumps(payload).encode(),
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read())

    def digest(self, model: str) -> str:
        if model not in self._digests:
            try:
                tags = json.loads(urllib.request.urlopen(self._host_for(model).rstrip("/") + "/api/tags", timeout=30).read())
                self._digests[model] = next((m["digest"] for m in tags.get("models", []) if m["name"] == model), "unknown")
            except Exception:
                self._digests[model] = "unknown"
        return self._digests[model]

    def embed(self, model: str, texts: list[str]) -> list[list[float]]:
        """Sentence embeddings for sense clustering. Needs an embedding model pulled in Ollama."""
        host = self._host_for(model)
        try:
            r = self._post(host, "/api/embed", {"model": model, "input": texts})
            if r.get("embeddings"):
                return r["embeddings"]
        except Exception:  # noqa: BLE001 - older Ollama exposes /api/embeddings, one text at a time
            pass
        return [self._post(host, "/api/embeddings", {"model": model, "prompt": t})["embedding"] for t in texts]

    def generate_json(self, model: str, prompt: str, key: dict | None = None) -> dict:
        reply = self._post(self._host_for(model), "/api/chat", {
            "model": model, "stream": False, "format": "json", "options": self.options,
            "messages": [{"role": "user", "content": prompt}],
        })
        return repair_json(reply["message"]["content"])


class FixtureBackend:
    """Replays hand-written SIMULATED responses keyed by utterance, stage and model."""
    mode = "fixture_simulated"
    host_locality = "fixture"

    def __init__(self, fixture_path: Path):
        self.data = json.loads(Path(fixture_path).read_text(encoding="utf-8"))

    def digest(self, model: str) -> str:
        return "fixture"

    def generate_json(self, model: str, prompt: str, key: dict | None = None) -> dict:
        key = key or {}
        uid, stage = key.get("utterance_id"), key.get("stage")
        if stage == "rank":
            return self._simulated_rank(model, key)
        try:
            if stage == "normalise":
                return self.data[uid]["normalise"]
            if stage == "back_translate":
                return self.data[uid]["back_translate"][key["source_model"]]
            return self.data[uid][stage][model]
        except KeyError as e:
            raise KeyError(f"No fixture for {uid}/{stage}/{model}") from e

    @staticmethod
    def _simulated_rank(model: str, key: dict) -> dict:
        """Deterministic stand-in for concept ranking. Model A is conservative, model C over-eager,
        so the pilot exercises concept-level disagreement. This is not a model's behaviour."""
        cands, cat, reg = key["retrieved"], key["sense_category"], key["sense_register"]
        if not cands:
            return {"ranked": [], "no_adequate_match": True, "gap_note": "No concepts retrieved for this meaning."}
        if model.endswith("A") and (cat in {"spiritual_or_supernatural", "social_or_relational"} or reg == "everyday_cultural"):
            return {"ranked": [], "no_adequate_match": True,
                    "gap_note": "Retrieved concepts are narrower or more medical than the everyday meaning."}
        if cat == "spiritual_or_supernatural" and not model.endswith("C"):
            return {"ranked": [], "no_adequate_match": True, "gap_note": "No concept covers the spiritual reading."}
        pred = ("skos:exactMatch" if model.endswith("C") else
                "skos:broadMatch" if cat in {"emotional_state", "cognitive_process", "clinical_symptom", "somatic_experience"} else
                "skos:relatedMatch")
        order = cands if not model.endswith("B") else list(reversed(cands))
        return {"ranked": [{"id": c["id"], "rank": i + 1, "proposed_predicate": pred,
                            "rationale": "SIMULATED ranking for pipeline testing."} for i, c in enumerate(order[:3])],
                "no_adequate_match": False, "gap_note": ""}
