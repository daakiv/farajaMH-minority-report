"""Re-cluster saved packages under different settings, without re-running the pipeline.

Clustering is deterministic post-processing over senses that are already in the packages, so the two
open questions in DESIGN §11 — what to embed, and where to set the threshold — can be answered in
seconds against runs you already have. A full pipeline run takes about two hours and tells you nothing
about clustering that this cannot.

    python pilot/cluster_sweep.py --runs runs/example-v2 runs/example-v3
    python pilot/cluster_sweep.py --runs runs/example-v3 --show gloss 0.80

Only the embedding model is called, so Ollama must be up, but nothing is generated and no model is
asked to reason. `--raw-keys` reproduces behaviour before conform.normalise_sense_key, for comparison.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yaml  # noqa: E402

from mr_farajamh import agreement as ag  # noqa: E402
from mr_farajamh.backends import OllamaBackend  # noqa: E402
from mr_farajamh.conform import normalise_sense_key  # noqa: E402

# What gets embedded for each sense. The pipeline currently uses key+gloss.
INPUTS = {
    "key+gloss": lambda s: f"{s['sense_key']}: {s['gloss']}",
    "gloss": lambda s: s["gloss"],
    "key": lambda s: s["sense_key"],
}


def packages(run: str) -> list[dict]:
    out = []
    for f in sorted(glob.glob(os.path.join(run, "packages", "*.json"))):
        p = json.load(open(f, encoding="utf-8"))
        if p.get("status") == "awaiting_review" and p.get("L4_interpretation"):
            out.append(p)
    return out


def duplicate_label_packages(all_clusters: list[list[dict]]) -> int:
    """Packages containing two clusters whose labels are the same meaning in different words.

    The artefact example-v3 exposed. A crude proxy — it catches surface variants, not `exhausted`
    against `exhaustion` — so treat it as a floor on fragmentation, never a measure of correctness.
    """
    n = 0
    for cs in all_clusters:
        labels = Counter(normalise_sense_key(c["label"]) for c in cs)
        if any(v > 1 for v in labels.values()):
            n += 1
    return n


def run_setting(pkgs, vectors_by_text, scheme, threshold, cross, minority_below, raw_keys):
    rows, all_clusters = [], []
    for p in pkgs:
        senses = []
        for s in p["L4_interpretation"]["candidates"]:
            s = dict(s)
            if not raw_keys:
                s["sense_key"] = normalise_sense_key(s["sense_key"]) or s["sense_key"]
            senses.append(s)
        vecs = {s["sense_id"]: vectors_by_text[INPUTS[scheme](s)] for s in senses}
        cs = ag.finalise_clusters(
            ag.cluster_senses(senses, 0.34, vecs, threshold, cross),
            p["L5_agreement"]["n_models"], minority_below)
        all_clusters.append(cs)
        rows.extend(cs)
    st = Counter(c["standing"] for c in rows)
    return {
        "clusters": len(rows),
        "unanimous": st["unanimous"], "majority": st["majority"], "minority": st["minority"],
        "dup_label_pkgs": duplicate_label_packages(all_clusters),
        "mean_members": round(sum(len(c["member_sense_ids"]) for c in rows) / max(len(rows), 1), 2),
        "_clusters": all_clusters,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--config", default="config/laptop.yaml")
    ap.add_argument("--inputs", nargs="+", default=["key+gloss", "gloss"], choices=sorted(INPUTS))
    ap.add_argument("--thresholds", nargs="+", type=float, default=[0.75, 0.80, 0.85, 0.90])
    ap.add_argument("--cross", type=float, default=None, help="cross-category threshold (default: from config)")
    ap.add_argument("--raw-keys", action="store_true", help="skip sense_key normalisation, as before 2 Oct")
    ap.add_argument("--show", nargs=2, metavar=("INPUT", "THRESHOLD"),
                    help="print every cluster label at one setting instead of the table")
    a = ap.parse_args()

    cfg = yaml.safe_load(open(a.config, encoding="utf-8"))
    acfg = cfg["agreement"]
    cross = a.cross if a.cross is not None else acfg.get("embedding_cross_category_threshold", 0.93)
    model = cfg["models"].get("embedding_model")
    if not model:
        raise SystemExit(f"{a.config} configures no embedding_model; this sweep needs one.")
    backend = OllamaBackend(cfg["ollama_hosts"], cfg["models"].get("options", {}))

    for run in a.runs:
        pkgs = packages(run)
        if not pkgs:
            print(f"{run}: no reviewable packages found"); continue

        # Embed every distinct text once, across all schemes.
        texts = sorted({INPUTS[sch](dict(s, sense_key=(s["sense_key"] if a.raw_keys
                                                       else normalise_sense_key(s["sense_key"]) or s["sense_key"])))
                        for p in pkgs for s in p["L4_interpretation"]["candidates"] for sch in a.inputs})
        print(f"{run}: {len(pkgs)} packages, embedding {len(texts)} distinct texts with {model} ...",
              flush=True)
        vectors = dict(zip(texts, backend.embed(model, texts)))

        if a.show:
            sch, th = a.show[0], float(a.show[1])
            res = run_setting(pkgs, vectors, sch, th, cross, acfg["minority_below"], a.raw_keys)
            for p, cs in zip(pkgs, res["_clusters"]):
                print(f"  {p['utterance_ref']['utterance_id']}")
                for c in cs:
                    print(f"      [{c['standing']:<9} {c['support_ratio']}] {c['label']}  ({c['category']})")
            continue

        print(f"  {'input':<10} {'thresh':>6} {'clusters':>9} {'unan':>5} {'maj':>5} {'min':>5} "
              f"{'dup-label pkgs':>15} {'mean/cluster':>13}")
        for sch in a.inputs:
            for th in a.thresholds:
                r = run_setting(pkgs, vectors, sch, th, cross, acfg["minority_below"], a.raw_keys)
                star = "  <- current" if (sch == "key+gloss" and abs(th - acfg.get("embedding_similarity_threshold", 0.85)) < 1e-9) else ""
                print(f"  {sch:<10} {th:>6.2f} {r['clusters']:>9} {r['unanimous']:>5} {r['majority']:>5} "
                      f"{r['minority']:>5} {r['dup_label_pkgs']:>15} {r['mean_members']:>13}{star}")
        print()

    print("Read the table by what you want clustering to do: group senses that mean the same thing,\n"
          "without absorbing a somatic or clinical reading into an emotional one. Fewer clusters is not\n"
          "automatically better — collapsing everything into one would score well on every column here.\n"
          "Use --show to read the labels at a setting before choosing it.")


if __name__ == "__main__":
    main()
