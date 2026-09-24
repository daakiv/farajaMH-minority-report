"""Agreement and disagreement between AI candidates.

This replaces the upstream consensus rule (exact lower-cased string match by at least 2 models, then an
arbitration vote that picks a winner). Here nothing wins: senses are clustered, every cluster is kept,
and minority clusters are labelled rather than dropped. That is the 'minority report'.

The similarity functions are deliberately simple (token Jaccard) so the pilot runs anywhere. For
production, use multilingual sentence embeddings for clustering and chrF for translation and back-translation similarity.
"""
from __future__ import annotations

import itertools
import math
import re
from collections import Counter

STOP_EN = set("a an the i my me is am are was be been have has had of to in on at for and or but it its that this "
              "these those as from with by so not no do does did can cannot can't feel feeling".split())
STOP_SW = set("na ya wa za la kwa ni si ndiyo kama tangu siku hizi".split())
CLINICAL_CATEGORIES = {"clinical_symptom", "risk_or_safety"}
CULTURAL_CATEGORIES = {"spiritual_or_supernatural", "social_or_relational"}


def tokens(text: str, stop: set[str]) -> set[str]:
    return {t for t in re.findall(r"[\w']+", (text or "").lower()) if t not in stop and len(t) > 1}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a | b else 1.0


def translation_agreement(cands: list[dict]) -> float:
    toks = [tokens(c["idiomatic_translation"], STOP_EN) for c in cands]
    pairs = list(itertools.combinations(toks, 2))
    return round(sum(jaccard(a, b) for a, b in pairs) / len(pairs), 3) if pairs else 1.0


def looks_degenerate(text: str) -> bool:
    """Small models sometimes emit a repeated word ('kusimamia kusimamia kusimamia') or a single token.
    Scoring that as a similarity of 0 would fire the mismatch flag on every item, so it is reported as
    unusable output instead."""
    toks = re.findall(r"[\w']+", (text or "").lower())
    if len(toks) < 3:
        return True
    if len(set(toks)) / len(toks) < 0.5:
        return True
    return any(toks[i] == toks[i + 1] == toks[i + 2] for i in range(len(toks) - 2))


def back_translation_similarity(back: str, normalised: str) -> float | None:
    """Returns None when the back-translation is unusable, so it is 'not assessed' rather than 'mismatched'."""
    if looks_degenerate(back):
        return None
    return round(jaccard(tokens(back, STOP_SW), tokens(normalised, STOP_SW)), 3)


def cosine(a: list[float], b: list[float]) -> float:
    num = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a)) or 1e-9
    nb = math.sqrt(sum(x * x for x in b)) or 1e-9
    return num / (na * nb)


def cluster_senses(senses: list[dict], threshold: float, vectors: dict | None = None,
                   embedding_threshold: float = 0.85, cross_category_threshold: float = 0.93) -> list[dict]:
    """Greedy clustering of senses proposed by different models.

    With `vectors` (sense_id -> embedding) senses are grouped by meaning, so "sadness", "emotional pain"
    and "feeling low" land in one cluster. Without them it falls back to sense_key equality or
    same-category token overlap, which fragments synonyms — see DESIGN.md §3.

    Senses in DIFFERENT categories need a higher similarity to merge. Embedding models score any two
    distress sentences as similar, and merging across categories hides exactly what reviewers must see:
    a somatic or clinical reading disappearing inside an emotional cluster.
    """
    clusters: list[dict] = []
    for s in senses:
        key, cat, gt = s["sense_key"].strip().lower(), s["category"], tokens(s["gloss"], STOP_EN)
        vec = (vectors or {}).get(s["sense_id"])
        home = None
        for c in clusters:
            if vec is not None and c["_vecs"]:
                sim = max(cosine(vec, v) for v in c["_vecs"])
                needed = embedding_threshold if cat in c["_cats"] else cross_category_threshold
                if key == c["_key"] or sim >= needed:
                    home = c
                    break
                continue
            if key == c["_key"] or (cat == c["category"] and jaccard(gt, c["_tokens"]) >= threshold):
                home = c
                break
        if home is None:
            home = {"cluster_id": f"C{len(clusters) + 1}", "label": key, "category": cat, "_key": key,
                    "_tokens": gt, "_vecs": [], "_keys": [], "_cats": [], "member_sense_ids": [],
                    "supporting_models": [], "_registers": set()}
            clusters.append(home)
        if vec is not None:
            home["_vecs"].append(vec)
        home["_keys"].append(key)
        home["_cats"].append(cat)
        home["member_sense_ids"].append(s["sense_id"])
        home["_registers"].add(s["register"])
        if s["model_ref"] not in home["supporting_models"]:
            home["supporting_models"].append(s["model_ref"])
    return clusters


def finalise_clusters(clusters: list[dict], n_models: int, minority_below: float) -> list[dict]:
    out = []
    for c in clusters:
        # label and category by majority among the members, so a merged cluster is named by its commonest reading
        c["label"] = Counter(c.get("_keys") or [c["label"]]).most_common(1)[0][0]
        cats = Counter(c.get("_cats") or [c["category"]])
        c["category"] = cats.most_common(1)[0][0]
        c["member_categories"] = sorted(cats)
        ratio = round(len(c["supporting_models"]) / n_models, 3)
        standing = "unanimous" if ratio == 1 else ("majority" if ratio >= minority_below else "minority")
        out.append({k: v for k, v in c.items() if not k.startswith("_")} |
                   {"support_ratio": ratio, "standing": standing, "registers": sorted(c["_registers"])})
    return sorted(out, key=lambda c: -c["support_ratio"])


def sense_entropy(clusters: list[dict]) -> float:
    """Normalised entropy of sense mass across clusters (0 = one reading, 1 = spread evenly)."""
    counts = [len(c["member_sense_ids"]) for c in clusters]
    total = sum(counts)
    if len(counts) < 2:
        return 0.0
    h = -sum(n / total * math.log(n / total) for n in counts)
    return round(h / math.log(len(counts)), 3)


def divergence_flags(clusters, t_agree, bt_sims, families, cfg, context) -> list[str]:
    flags = []
    cats = {c["category"] for c in clusters}
    if t_agree < cfg["translation_divergence_below"]:
        flags.append("translation_divergence")
    sig = [c for c in clusters if c["support_ratio"] >= 1 / 3]
    competing = any(set(a["supporting_models"]) != set(b["supporting_models"]) for a, b in itertools.combinations(sig, 2))
    if competing:
        flags.append("sense_divergence")
    elif len(sig) > 1:
        flags.append("multiple_components_in_utterance")  # every model proposes the same set of readings
    if cats & CLINICAL_CATEGORIES and (cats - CLINICAL_CATEGORIES):
        flags.append("register_divergence_clinical_vs_everyday")
    if any(c["standing"] == "minority" and c["category"] in CLINICAL_CATEGORIES for c in clusters):
        flags.append("minority_clinical_reading")
    scored = [s for s in bt_sims if s is not None]
    if bt_sims and not scored:
        # every back-translation was unusable (common with small models); the check tells us nothing
        flags.append("back_translation_not_assessed")
    elif bt_sims and len(scored) * 2 < len(bt_sims):
        # most were unusable, so one low score is not evidence of a translation problem
        flags.append("back_translation_mostly_unassessed")
    elif any(s < cfg["back_translation_mismatch_below"] for s in scored):
        flags.append("back_translation_mismatch")
    if len(set(families)) < cfg["min_model_families"]:
        flags.append("insufficient_model_diversity")
    if clusters and all(c["standing"] == "unanimous" for c in clusters):
        flags.append("full_agreement_audit_candidate")  # possible false consensus: sample for blind human review
    if context["negation"]["value"] != "affirmed":
        flags.append(f"polarity_{context['negation']['value']}")
    if context["attribution"]["value"] not in ("self",):
        flags.append("experiencer_not_speaker")
    if any(context[k]["source"] == "not_resolved" for k in ("negation", "temporality", "attribution")):
        flags.append("context_incomplete")
    return flags


def concept_agreement(rankings: dict[str, dict]) -> dict:
    """rankings: model_ref -> rank reply. Returns top-1 agreement and no-match votes."""
    top1 = {m: (r["ranked"][0]["id"] if r.get("ranked") else None) for m, r in rankings.items()}
    picks = [v for v in top1.values() if v]
    none_votes = [m for m, r in rankings.items() if r.get("no_adequate_match")]
    agree = max((picks.count(p) for p in set(picks)), default=0) / len(rankings) if rankings else 0.0
    preds = {r["ranked"][0]["proposed_predicate"] for r in rankings.values() if r.get("ranked")}
    return {"top1_by_model": top1, "top1_agreement": round(agree, 3), "no_adequate_match_votes": none_votes,
            "predicate_disagreement": len(preds) > 1}


def cultural_terms_lost(trans: list[dict]) -> list[str]:
    """Terms any translator marked as culturally specific that disappear in a back-translation.

    Only usable back-translations are checked: a degenerate one tells us nothing about lost meaning.
    The check is substring-based, so it misses morphological relatives (mawazo / nawaza) and
    over-reports; a morphological analyser should replace it (DESIGN.md §3).
    """
    terms = {pt["term"].lower() for t in trans for pt in t.get("preserved_terms", []) if pt.get("term")}
    lost = []
    for t in trans:
        bt = t.get("back_translation")
        if not bt or bt.get("similarity_to_normalised") is None:
            continue
        text = bt["text"].lower()
        lost += [f"{t['candidate_id']}:{term}" for term in sorted(terms) if term not in text]
    return lost


def category_support(senses: list[dict], n_models: int) -> list[dict]:
    """How many models proposed at least one sense in each category.

    Cluster labels are model-coined, so two clusters can hold the same reading ("sadness" and
    "emotional distress") and each look like a 2/3 majority. This coarser view is harder to fool:
    it says plainly that all three models read the expression as emotional, and that one also read
    it as somatic.
    """
    by_cat: dict[str, set] = {}
    for s in senses:
        by_cat.setdefault(s["category"], set()).add(s["model_ref"])
    return sorted(({"category": c, "models": sorted(m), "support_ratio": round(len(m) / n_models, 3)}
                   for c, m in by_cat.items()), key=lambda x: -x["support_ratio"])
