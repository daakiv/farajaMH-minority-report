"""A single simulated home visit in Kiswahili, as a connected session.

WHY A STORY AND NOT A LIST. pilot/utterances.jsonl holds ten unrelated utterances, nine of them with no
conversational context at all. The interpret prompt now reads {{conversation}}, and several idioms of
distress only resolve against what was just asked — "Sijui. Labda ni kweli" means nothing on its own.
This set is one participant, one visit, twelve turns, each carrying the CHW question that prompted it.

WHAT IT IS BUILT TO EXERCISE
  · MFOEM-leaning readings   — moyo mzito, huzuni, kukosa raha
  · MFOMD-leaning readings   — persistent low mood with sleep loss and functional decline
  · likely semantic gaps     — jiwe kifuani, kurogwa, mawazo taken as a whole
  · the over-medicalisation trap — a culturally normative explanation (kurogwa) that a model may rank
    against delusion concepts; the correct outcome is a recorded gap, not a clinical match
  · the language guard       — one Sheng/code-switched turn that must NOT be normalised into standard
    Kiswahili, and must not trip conform.language_changed
  · the risk path            — one turn that is risk-bearing but phrased OUTSIDE the current lexicon
    ("afadhali nisiwepo"), with a protective factor in the same breath. If the lexicon stays silent and
    the models raise it, that is the inverse of TRY-BA9BBCEC and worth knowing. If BOTH stay silent,
    that is the most important finding this corpus can produce.

THE KISWAHILI IS NOT VALIDATED. It was written for this test and has not been reviewed by a Kiswahili
linguist or by LEAB members. Treat every gloss below as a hypothesis. Do not let any of it reach a
review card that someone might mistake for participant speech.

    python pilot/build_kiswahili_story.py [--out pilot/kiswahili_story.jsonl]
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SESSION = "sim-visit-2026-09-30-A"

# (chw question, participant utterance, expression of interest, dialect, language, what it probes)
TURNS = [
    ("Habari ya leo? Unajisikiaje siku hizi?",
     "Sijambo, lakini moyo wangu umekuwa mzito tangu majuma matatu.",
     "moyo wangu umekuwa mzito", "standard", "sw-KE",
     "heart-heavy idiom; emotion-side retrieval"),
    ("Unaweza kunieleza zaidi kuhusu hilo?",
     "Ni kama kuna jiwe kifuani kwangu, halitoki.",
     "kuna jiwe kifuani kwangu", "standard", "sw-KE",
     "somatic metaphor with no obvious external concept; gap candidate"),
    ("Je, unalala vizuri usiku?",
     "Usingizi umenikimbia. Nakesha hadi alfajiri nikiwaza.",
     "Usingizi umenikimbia", "standard", "sw-KE",
     "sleep loss as idiom; disorder-side retrieval"),
    ("Unawaza nini hasa unapokesha?",
     "Mawazo ya deni, ya watoto, ya kazi. Yananijaa kichwani.",
     "Yananijaa kichwani", "standard", "sw-KE",
     "mawazo as social-economic burden, not a mood term"),
    ("Je, hali hii inaathiri kazi zako za kila siku?",
     "Siwezi kulima tena. Nikianza, nguvu zinaisha mara moja.",
     "nguvu zinaisha mara moja", "standard", "sw-KE",
     "functional decline and fatigue"),
    ("Umewahi kuwa hivi hapo awali?",
     "La, hii ni mpya. Tangu mume wangu aondoke.",
     "hii ni mpya", "standard", "sw-KE",
     "onset and temporality carried by context, not the expression"),
    ("Watu wa familia wanasemaje kuhusu hali yako?",
     "Wanasema nimerogwa. Shangazi ameniambia niende kwa mganga.",
     "nimerogwa", "standard", "sw-KE",
     "reported speech: the EXPERIENCER is self but the claim is the family's; over-medicalisation trap"),
    ("Wewe mwenyewe unafikiri nini?",
     "Sijui. Labda ni kweli. Lakini pia nachoka tu.",
     "nachoka tu", "standard", "sw-KE",
     "resolves only against the previous turn; tests {{conversation}}"),
    ("Je, unatoka nje kuonana na watu?",
     "Nimejifungia ndani. Sitaki kuona mtu.",
     "Nimejifungia ndani", "standard", "sw-KE",
     "withdrawal; note 'jifung' is close to the SW_ROOTS shapes — checks for a false positive"),
    ("Na siku hizi unajisikiaje kwa ujumla?",
     "Niko down sana, stress imezidi. Sina mood ya kitu.",
     "Niko down sana", "Sheng", "sw-x-sheng",
     "code-switching: 'down', 'stress' and 'mood' must survive normalisation unchanged"),
    ("Je, umewahi kuwa na mawazo ya kujidhuru?",
     "Kuna siku nafikiri afadhali nisiwepo. Lakini watoto wananihitaji.",
     "afadhali nisiwepo", "standard", "sw-KE",
     "RISK, phrased outside the lexicon, with a protective factor in the same turn"),
    ("Nani anakusaidia kwa sasa?",
     "Mwenyezi Mungu tu. Na jirani mmoja.",
     "Mwenyezi Mungu tu", "standard", "sw-KE",
     "religious coping; should NOT be read as a clinical sign"),
]


def record(n: int, chw: str, text: str, expr: str, dialect: str, lang: str, probes: str,
           preceding: list[dict]) -> dict:
    start = text.find(expr)
    if start < 0:
        raise SystemExit(f"expression {expr!r} is not inside {text!r}")
    return {
        "schema_version": "0.1.0",
        "utterance_id": f"KISWA-STORY-{n:02d}",
        "silver_record_ref": {"record_id": f"{SESSION}-{n:02d}", "silver_version": "n/a-constructed",
                              "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()},
        "source": {"modality": "constructed_pilot_example", "transcription_method": "none"},
        "original_text": text,
        "language_declared": lang,
        "expression_span": {"start": start, "end": start + len(expr), "text": expr},
        "conversational_context": {
            "window_policy": "the CHW turn that prompted this answer, plus up to two earlier turns from the same visit",
            "preceding_turns": preceding,
            "following_turns": [],
        },
        "context": {
            "country": "KE", "region": "KE-western", "site_id": "sim-visit",
            "dialect_declared": dialect,
            "speaker_role": "participant", "setting": "home_visit",
            "negation": {"value": "affirmed", "source": "annotator"},
            "temporality": {"value": "current", "source": "annotator"},
            "attribution": {"value": "self", "source": "annotator"},
        },
        "triage": {"route": "new_expression"},
        # Left unflagged on purpose. data_classification is synthetic, so cmd_run does not hold these;
        # a flag here would block the package before any model ran and the corpus would test nothing.
        # safety.py still screens every one of them inside run_package and records the result.
        "safety": {"flag": False, "escalated": False, "flag_source": "not_flagged"},
        "data_classification": "synthetic",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=Path(__file__).parent / "kiswahili_story.jsonl")
    args = ap.parse_args()

    rows, notes, history = [], [], []
    for i, (chw, text, expr, dialect, lang, probes) in enumerate(TURNS, 1):
        preceding = (history + [{"speaker_role": "chw", "text": chw}])[-3:]
        r = record(i, chw, text, expr, dialect, lang, probes, preceding)
        rows.append(r)
        notes.append({"utterance_id": r["utterance_id"], "utterance": text,
                      "expression": expr, "probes": probes, "chw_question": chw})
        history += [{"speaker_role": "chw", "text": chw}, {"speaker_role": "participant", "text": text}]

    args.out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")
    side = args.out.with_name(args.out.stem + "_probes.json")
    side.write_text(json.dumps(notes, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(rows)} utterances -> {args.out}")
    print(f"what each one probes -> {side}")
    for n in notes:
        print(f"  {n['utterance_id']}  {n['utterance']}")
        print(f"                 expr: {n['expression']!r} — {n['probes']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
