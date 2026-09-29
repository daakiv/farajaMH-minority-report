"""Model-independent detection of risk language.

Added after the TRY-BA9BBCEC run (2026-09-25), in which three models processed
"Na kwazika kiroho sana nataka nitoke duniani" — "...I want to leave the world" — and not one of them
proposed a risk_or_safety sense. One of them wrote in its uncertainty note that the phrase was
"hyperbolic ... rather than a literal suicidal statement. It's crucial to avoid clinical
interpretations." A 12B model ruled out suicidal ideation. That judgement belongs to a clinician and a
lived-experience reviewer.

So risk detection cannot depend on the models. This module is a plain lexicon check that runs whatever
the models say, over the original utterance, the normalisation, every translation, every sense gloss and
rationale, and the concept-ranking gap notes.

WHAT THIS IS NOT. It is a screening heuristic for a curation pipeline, not a clinical instrument and not
a triage tool. It is deliberately over-inclusive: it does not resolve negation, so "sitaki kufa" ("I do
not want to die") fires, and idiomatic uses of kufa fire too. A false positive costs a banner on a review
card. A false negative is the failure this module exists to prevent. Any change that makes it quieter
needs a clinician's sign-off, and the lexicon needs review by LEAB members and the Swahili linguists
before it goes anywhere near participant data — the terms below are a starting list, not a validated one.

The v10 architecture runs its own safety check before triage. This does not replace it; it is the net
underneath it, for the curation stage.
"""
from __future__ import annotations

import re
import unicodedata

LEXICON_VERSION = "0.1.0-unvalidated"

# Swahili. Substring matching on a space-normalised, lower-cased string: Swahili agglutination means
# a phrase fragment ("toke duniani") catches inflected forms that a word-list would miss.
SW_SELF_HARM = [
    "nitoke duniani", "toke duniani", "kuondoka duniani", "kutoka duniani", "niondoke duniani",
    "niache dunia", "kuacha dunia", "sitaki kuishi", "sitaki kuwa hai", "sitaki kuendelea kuishi",
    "nataka kufa", "ningependa kufa", "afadhali nife", "afadhali kufa", "heri nife", "nife",
    "kujiua", "nijiue", "anataka kujiua", "kujitoa uhai", "kujiangamiza",
    "kujinyonga", "nijinyonge", "kujidhuru", "nijidhuru", "kujiumiza", "nijiumize",
    "kumaliza maisha", "kuyamaliza maisha", "maisha yangu yaishe", "nimechoka na maisha",
    "sina sababu ya kuishi", "sina haja ya kuishi", "dunia haina maana",
]
SW_HARM_OTHERS = ["nimuue", "kumuua", "nitawaua", "kuwaua"]

# English, for the translations and the model rationales — where the TRY-BA9BBCEC signal actually surfaced.
EN_SELF_HARM = [
    "kill myself", "killing myself", "end my life", "ending my life", "take my life", "taking my life",
    "want to die", "wish i were dead", "wish i was dead", "better off dead", "rather be dead",
    "leave the world", "leaving the world", "leave this world", "disappear forever",
    "don't want to be here", "do not want to be here", "don't want to live", "do not want to live",
    "no reason to live", "nothing to live for", "end it all",
    "harm myself", "harming myself", "hurt myself", "hurting myself", "self-harm", "self harm",
    "suicide", "suicidal", "suicidal ideation", "take his own life", "take her own life", "own life",
]
EN_HARM_OTHERS = ["kill him", "kill her", "kill them", "hurt them", "harm others"]

CATEGORIES = {
    "self_harm_or_suicide": SW_SELF_HARM + EN_SELF_HARM,
    "harm_to_others": SW_HARM_OTHERS + EN_HARM_OTHERS,
}


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "").lower()
    text = text.replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", text)


def scan(text: str, where: str) -> list[dict]:
    """Every lexicon hit in one string, with the surrounding words so a reviewer can judge it."""
    hay = normalise(text)
    hits = []
    for category, terms in CATEGORIES.items():
        for term in terms:
            i = hay.find(term)
            if i < 0:
                continue
            start, end = max(0, i - 40), min(len(hay), i + len(term) + 40)
            hits.append({"category": category, "term": term, "where": where,
                         "context": ("…" if start else "") + hay[start:end].strip() + ("…" if end < len(hay) else "")})
    return hits


def _dedupe(hits: list[dict]) -> list[dict]:
    """One line per finding.

    The lexicon holds overlapping phrases on purpose ("nitoke duniani" and "toke duniani", so inflection
    does not slip through), which makes one phrase report twice. Keep the longest match in each field and
    show the participant's own words before anything a model wrote.
    """
    seen, out = set(), []
    for h in sorted(hits, key=lambda x: -len(x["term"])):
        if any(o["where"] == h["where"] and h["term"] in o["term"] for o in out):
            continue
        k = (h["category"], h["term"], h["where"])
        if k not in seen:
            seen.add(k)
            out.append(h)
    order = {"original_text": 0, "normalised_text": 1}
    return sorted(out, key=lambda h: (order.get(h["where"], 2 + h["where"].startswith("gap_note/")), h["where"]))


def detect_in_utterance(utt: dict) -> dict:
    """Pre-model check, on the participant's own words only."""
    return result(_dedupe(scan(utt["original_text"], "original_text")))


def detect_in_package(pkg_parts: dict) -> dict:
    """Post-model check over everything the pipeline produced.

    The TRY-BA9BBCEC package is the case for scanning the gap notes: the ranker wrote "the candidate
    meaning includes a desire to end one's life (suicidal ideation)" while no interpreter proposed a
    risk sense, so the signal existed in L6 and never reached L7.
    """
    hits = scan(pkg_parts.get("original_text", ""), "original_text")
    hits += scan(pkg_parts.get("normalised_text", ""), "normalised_text")
    for t in pkg_parts.get("translations", []):
        for field in ("literal_gloss", "idiomatic_translation", "uncertainty_note"):
            hits += scan(t.get(field, ""), f"translation/{t.get('candidate_id', '?')}/{field}")
    for s in pkg_parts.get("senses", []):
        for field in ("gloss", "rationale"):
            hits += scan(s.get(field, ""), f"sense/{s.get('sense_id', '?')}/{field}")
    for pc in pkg_parts.get("per_cluster", []):
        hits += scan(pc.get("gap_note", ""), f"gap_note/{pc.get('cluster_id', '?')}")
    return result(_dedupe(hits))


def result(hits: list[dict]) -> dict:
    return {"fired": bool(hits), "lexicon_version": LEXICON_VERSION,
            "categories": sorted({h["category"] for h in hits}), "matches": hits[:20],
            "note": "Over-inclusive lexicon screen, not a clinical assessment. Negation is not resolved."}


def models_missed_it(detector: dict, clusters: list[dict]) -> bool:
    """True when the lexicon found risk language and no model proposed a risk_or_safety sense.

    This is the TRY-BA9BBCEC signature and it is the single most important flag on the card.
    """
    return bool(detector["fired"]) and not any(c.get("category") == "risk_or_safety" for c in clusters)
