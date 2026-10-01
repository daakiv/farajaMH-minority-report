"""How much of the models' apparent agreement is caused by sharing their translations?

THE QUESTION. Each interpreter is shown all three translations (`prompts/interpret.md`, the
`{{translations}}` line). In run TRY-BA9BBCEC an interpreter quoted another model's translation back
as though it were the participant's words, and in kiswa-story-v1 seven risk senses cited text from
outside their own utterance. So the three interpretations are not fully independent — which matters,
because standing (unanimous / majority / minority) is only meaningful if the models arrived at their
readings separately. The deck and the README both state this limitation. This script replaces the
statement with a number.

THE METHOD. Run the same corpus twice, changing one thing:

    config: models.share_translations: true     ->  out_shared/
    config: models.share_translations: false    ->  out_independent/

Then compare. If agreement is unchanged, the sharing is not doing the work and the caveat can be
retired. If agreement falls, the drop is the portion of observed consensus that the shared translations
account for, and standing should be read accordingly.

    python pilot/independence_experiment.py --shared out_shared --independent out_independent

WHAT IT DOES NOT SHOW. Two runs of three small models on one corpus. Run-to-run variation is not
controlled here: to separate the effect of sharing from ordinary nondeterminism, run each arm twice
with different seeds and compare the gap between arms against the gap within them.
"""
from __future__ import annotations

import argparse
import json
import statistics as st
from pathlib import Path


def load(out: Path) -> dict[str, dict]:
    pkgs = {}
    for f in sorted((out / "packages").glob("*.json")):
        p = json.loads(f.read_text(encoding="utf-8"))
        if p.get("status") == "awaiting_review":
            pkgs[p["utterance_ref"]["utterance_id"]] = p
    return pkgs


def measure(p: dict) -> dict:
    clusters = p["L5_agreement"]["sense_clusters"]
    n = p["L5_agreement"].get("n_models") or 0
    standings = [c.get("standing") for c in clusters]
    supports = [c.get("support_ratio") for c in clusters if isinstance(c.get("support_ratio"), (int, float))]
    senses = p["L4_interpretation"]["candidates"]
    ev = [e.get("type") for s in senses for e in (s.get("evidence") or [])]
    return {
        "clusters": len(clusters),
        "unanimous": standings.count("unanimous"),
        "majority": standings.count("majority"),
        "minority": standings.count("minority"),
        "top_support": max(supports) if supports else 0.0,
        "mean_support": st.mean(supports) if supports else 0.0,
        "senses": len(senses),
        "senses_per_model": len(senses) / n if n else 0.0,
        "cites_translation": ev.count("translation_candidate"),
        "cites_utterance": ev.count("utterance_span"),
        "risk_clusters": sum(1 for c in clusters if c.get("category") == "risk_or_safety"),
    }


KEYS = [
    ("top_support", "Top cluster support ratio", "lower means less apparent consensus"),
    ("mean_support", "Mean cluster support ratio", ""),
    ("unanimous", "Unanimous clusters", "the headline number: consensus that may be manufactured"),
    ("majority", "Majority clusters", ""),
    ("minority", "Minority clusters", "higher means more dissent survived"),
    ("clusters", "Clusters per utterance", ""),
    ("senses_per_model", "Senses proposed per model", ""),
    ("cites_translation", "Evidence citing a translation", "should fall to zero in the independent arm"),
    ("cites_utterance", "Evidence citing the utterance", ""),
    ("risk_clusters", "risk_or_safety clusters", ""),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shared", type=Path, required=True, help="output dir from the run WITH shared translations")
    ap.add_argument("--independent", type=Path, required=True, help="output dir from the run WITHOUT them")
    a = ap.parse_args()

    A, B = load(a.shared), load(a.independent)
    for name, d, path in (("shared", A, a.shared), ("independent", B, a.independent)):
        if not d:
            print(f"no reviewable packages in {path}")
            return 1
        arm = {p["provenance"].get("share_translations") for p in d.values()}
        print(f"{name:<12} {len(d):>3} packages   provenance.share_translations = "
              f"{', '.join(str(x) for x in arm)}")
    if True in {p["provenance"].get("share_translations") for p in B.values()}:
        print("\nWARNING: the 'independent' run reports share_translations = True. "
              "Set models.share_translations: false in that arm's config and re-run.")

    common = sorted(set(A) & set(B))
    print(f"\n{len(common)} utterances in both arms\n")
    if not common:
        return 1

    ma = {u: measure(A[u]) for u in common}
    mb = {u: measure(B[u]) for u in common}

    print(f"{'metric':<34}{'shared':>9}{'independent':>14}{'change':>10}")
    print("-" * 79)
    for key, label, note in KEYS:
        x = st.mean(ma[u][key] for u in common)
        y = st.mean(mb[u][key] for u in common)
        delta = y - x
        arrow = "→" if abs(delta) < 1e-9 else ("↓" if delta < 0 else "↑")
        print(f"{label:<34}{x:>9.2f}{y:>14.2f}{arrow + f' {abs(delta):.2f}':>10}")
        if note:
            print(f"{'':<34}{note}")

    print()
    u_a = sum(ma[u]["unanimous"] for u in common)
    u_b = sum(mb[u]["unanimous"] for u in common)
    if u_a:
        print(f"Unanimous clusters: {u_a} shared -> {u_b} independent "
              f"({(u_a - u_b) / u_a:.0%} of them did not survive withholding the translations).")
    else:
        print("No unanimous clusters in the shared arm; nothing to lose.")
    print("\nPer-utterance top-cluster support:")
    print(f"  {'utterance':<18}{'shared':>9}{'independent':>14}{'change':>10}")
    for u in common:
        d = mb[u]["top_support"] - ma[u]["top_support"]
        print(f"  {u:<18}{ma[u]['top_support']:>9.2f}{mb[u]['top_support']:>14.2f}{d:>+10.2f}")

    print("\nRead this as: the change is an upper bound on the effect of sharing, because it also "
          "contains ordinary run-to-run variation. Run each arm twice with different seeds to separate them.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
