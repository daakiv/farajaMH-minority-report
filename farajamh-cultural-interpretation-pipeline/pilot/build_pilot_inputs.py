"""Builds pilot/utterances.jsonl — 10 CONSTRUCTED Swahili pilot examples (no participant data).

Each example is chosen to test one failure mode. The Swahili wording and the dialect labels are
drafts for Swahili linguists and LEAB members to correct before the pilot runs.
"""
import hashlib
import json
from pathlib import Path


def ctx(value, source="annotator", conf=None):
    d = {"value": value, "source": source}
    if conf is not None:
        d["confidence"] = conf
    return d


EXAMPLES = [
    # id, utterance, expression, extras, test purpose
    dict(id="P01", text="Tangu msiba ule, roho yangu imeondoka.", expr="roho yangu imeondoka",
         country="KE", region="KE-coast", dialect="Kiamu", speaker="participant", setting="home_visit",
         neg="affirmed", temp="current", attr="self",
         before=[{"speaker_role": "chw", "text": "Unajisikiaje siku hizi?"}],
         purpose="v10 worked example. Many readings (emptiness, spiritual loss, fright). Tests multiple candidates and a probable semantic gap."),
    dict(id="P02", text="Moyo wangu ni mzito kila asubuhi.", expr="Moyo wangu ni mzito",
         country="KE", region="KE-western", dialect="standard", speaker="participant", setting="clinic",
         neg="affirmed", temp="recurrent", attr="self", before=[],
         purpose="Grant example 'my heart is heavy'. Heart metaphor must not be read as a cardiac complaint. Tests literal vs idiomatic translation."),
    dict(id="P03", text="Nina mawazo mengi, siwezi kufanya kazi.", expr="Nina mawazo mengi",
         country="TZ", region="TZ-lake", dialect="standard", speaker="participant", setting="hdss_survey",
         neg="affirmed", temp="current", attr="self", before=[],
         purpose="'Thinking too much' idiom. The literature describes it as neither exactly rumination nor worry. Tests over-medicalisation and a relatedMatch or gap outcome."),
    dict(id="P04", text="Mawazo yananichoma kichwa usiku.", expr="Mawazo yananichoma kichwa",
         country="KE", region="KE-western", dialect="standard", speaker="participant", setting="chat_platform",
         neg="affirmed", temp="recurrent", attr="self", before=[],
         purpose="Grant example 'thoughts burn my head'. Somatic metaphor: the risk is a literal 'headache' reading or an automatic cognitive-symptom reading."),
    dict(id="P05", text="Nimelogwa, ndiyo maana siwezi kulala.", expr="Nimelogwa",
         country="KE", region="KE-coast", dialect="Kimvita", speaker="participant", setting="home_visit",
         neg="affirmed", temp="current", attr="self", before=[],
         purpose="'I have been bewitched' (kuroga, with l/r variation). Tests normalisation and the risk of labelling a cultural explanation as a delusion. Should NOT map clinically without clinician context."),
    dict(id="P06", text="Niko na stress mob, siwezi lala.", expr="Niko na stress mob",
         country="KE", region="KE-nairobi", dialect="Sheng", speaker="participant", setting="chat_platform",
         neg="affirmed", temp="current", attr="self", before=[],
         purpose="Sheng and English code-mixing ('mob' = a lot). Tests code-switch handling and the second concept in the utterance (sleep)."),
    dict(id="P07", text="Sina raha siku hizi.", expr="Sina raha",
         country="TZ", region="TZ-lake", dialect="standard", speaker="participant", setting="clinic",
         neg="affirmed", temp="current", attr="self", before=[],
         purpose="Positive control: likely candidate for a low-mood or anhedonia concept. 'Sina' is lexical negation (I have no joy); the expression itself is AFFIRMED."),
    dict(id="P08", text="Nimechoka na maisha, sitaki kuendelea.", expr="Nimechoka na maisha",
         country="KE", region="KE-western", dialect="standard", speaker="participant", setting="chat_platform",
         neg="affirmed", temp="current", attr="self", before=[],
         safety={"flag": True, "escalated": False},
         purpose="Safety-critical (v10 example). The pipeline must refuse to process until escalation is recorded. Tests the safety gate."),
    dict(id="P09", text="Siku hizi sina mawazo mengi kama zamani.", expr="sina mawazo mengi",
         country="TZ", region="TZ-lake", dialect="standard", speaker="participant", setting="hdss_survey",
         neg="negated", temp="current", attr="self", before=[],
         purpose="Negated form of P03 ('I no longer think too much'). Tests that Silver negation reaches reviewers and is not dropped."),
    dict(id="P10", text="Mama yangu hana raha tangu baba afariki.", expr="hana raha",
         country="KE", region="KE-coast", dialect="standard", speaker="family_member", setting="home_visit",
         neg="affirmed", temp="current", attr="family_member", before=[],
         onset="since father's death",
         purpose="Attribution to another person, plus bereavement onset. Tests that the experiencer is not assumed to be the speaker."),
]


def build():
    out = []
    for e in EXAMPLES:
        start = e["text"].find(e["expr"])
        assert start >= 0, e["id"]
        rec = {
            "schema_version": "0.1.0",
            "utterance_id": f"PILOT-{e['id']}",
            "silver_record_ref": {
                "record_id": f"constructed-{e['id']}",
                "silver_version": "n/a-constructed",
                "sha256": hashlib.sha256(e["text"].encode()).hexdigest(),
            },
            "source": {"modality": "constructed_pilot_example", "transcription_method": "none"},
            "original_text": e["text"],
            "language_declared": "sw-" + e["country"],
            "expression_span": {"start": start, "end": start + len(e["expr"]), "text": e["expr"]},
            "conversational_context": {"window_policy": "constructed", "preceding_turns": e["before"], "following_turns": []},
            "context": {
                "country": e["country"], "region": e["region"], "site_id": "pilot",
                "dialect_declared": e["dialect"], "speaker_role": e["speaker"], "setting": e["setting"],
                "negation": ctx(e["neg"]), "temporality": ctx(e["temp"]), "attribution": ctx(e["attr"]),
            },
            "triage": {"route": "new_expression"},
            "safety": e.get("safety", {"flag": False, "escalated": False}),
            "data_classification": "synthetic",
        }
        if "onset" in e:
            rec["context"]["onset_or_duration"] = e["onset"]
        out.append(rec)
    p = Path(__file__).parent / "utterances.jsonl"
    p.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in out) + "\n", encoding="utf-8")
    (Path(__file__).parent / "test_purposes.json").write_text(
        json.dumps({f"PILOT-{e['id']}": e["purpose"] for e in EXAMPLES}, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


if __name__ == "__main__":
    print(len(build()), "pilot utterances written")
