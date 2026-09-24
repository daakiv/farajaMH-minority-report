"""Builds SIMULATED model responses for the offline pilot run.

These were written by hand to exercise the pipeline mechanics: normalisation edits, divergent translations,
minority clinical readings, back-translation checks, concept no-match votes and so on. They are NOT
outputs of any model and NOT validated interpretations of the expressions. Replace them with live runs
(OllamaBackend) and treat every reading below as a hypothesis for reviewers.
"""
import json
from pathlib import Path

A, B, C = "sim-model-A", "sim-model-B", "sim-model-C"


def N(text, expr, edits=(), lang="sw", segs=(), dialect=()):
    return {"normalised_text": text, "normalised_expression": expr, "edits": list(edits), "language_id": lang,
            "code_switch_segments": list(segs), "dialect_hypotheses": list(dialect)}


def T(lit, idi, conf, preserved=(), unc=""):
    return {"literal_gloss": lit, "idiomatic_translation": idi, "self_reported_confidence": conf,
            "preserved_terms": [{"term": t, "reason": r} for t, r in preserved], "uncertainty_note": unc}


def S(key, gloss, cat, reg, rationale, evidence, plaus, deps=()):
    return {"sense_key": key, "gloss": gloss, "category": cat, "register": reg, "context_dependencies": list(deps),
            "rationale": rationale, "evidence": [{"type": t, "ref": r, "quote": q} for t, r, q in evidence],
            "self_reported_plausibility": plaus}


def U(text):  # evidence: utterance span
    return ("utterance_span", "original_text", text)


def CX(field, value):
    return ("context_field", f"context.{field}", value)


BG = ("model_background_knowledge", "general", "")
ROHO = ("roho", "soul / spirit / life-breath / heart; no single English equivalent")
MOYO = ("moyo", "heart as seat of emotion; not the cardiac organ in this use")
MAWAZO = ("mawazo", "thoughts / worries; 'mawazo mengi' carries the 'thinking too much' idiom")

F = {}

F["PILOT-P01"] = {
    "normalise": N("Tangu msiba ule, roho yangu imeondoka.", "roho yangu imeondoka",
                   dialect=[{"dialect": "Kiamu (declared)", "evidence": "No Kiamu-specific forms in this utterance; standard spelling already."}]),
    "translate": {
        A: T("since bereavement that, soul my has-left", "Since that death, I feel as if my spirit has left me.", 0.7, [ROHO]),
        B: T("since funeral that, spirit my it-has-gone", "Since that funeral I have felt empty inside.", 0.6, [ROHO],
             "'roho' can mean soul, spirit, heart or life-breath."),
        C: T("since loss that, heart my has-gone", "Since that loss, my heart has gone out of me.", 0.5, [ROHO],
             "Could also describe losing courage, or a fright."),
    },
    "back_translate": {
        A: {"text": "Tangu kifo kile, nahisi kama roho yangu imeniacha."},
        B: {"text": "Tangu mazishi yale nimejisikia mtupu ndani."},
        C: {"text": "Tangu msiba ule, moyo wangu umenitoka."},
    },
    "interpret": {
        A: {"senses": [
            S("inner emptiness", "A feeling of inner emptiness or numbness after the loss.", "emotional_state", "everyday_cultural",
              "'Roho imeondoka' is used for a sense that one's inner life has gone.", [U("roho yangu imeondoka"), U("Tangu msiba ule")], 0.6,
              ["bereavement context", "duration since loss"]),
            S("grief", "Grief following a death.", "emotional_state", "everyday_cultural",
              "'Msiba' marks a death or funeral as the onset.", [U("Tangu msiba ule")], 0.6)]},
        B: {"senses": [
            S("inner emptiness", "Feeling empty inside since the funeral.", "emotional_state", "everyday_cultural",
              "My translation reads the phrase as emptiness.", [U("roho yangu imeondoka")], 0.5),
            S("spiritual loss", "A felt loss of one's spirit or spiritual connection, possibly tied to the dead person.",
              "spiritual_or_supernatural", "everyday_cultural", "Roho has a spiritual sense; the loss may be understood spiritually.",
              [U("roho"), BG], 0.4, ["speaker's religious framing", "local beliefs about the dead"])]},
        C: {"senses": [
            S("grief", "Grief reaction to a bereavement.", "emotional_state", "everyday_cultural",
              "Onset tied to msiba.", [U("Tangu msiba ule")], 0.6),
            S("loss of vitality", "Loss of life-energy or will: feeling that one's life-force has gone.", "somatic_experience", "mixed",
              "Roho as life-breath suggests reduced vitality.", [U("roho"), BG], 0.3),
            S("fright", "Having been badly shaken or frightened.", "emotional_state", "everyday_cultural",
              "Roho expressions are also used for fright; less likely given the bereavement onset.", [BG], 0.2)]},
    },
}

F["PILOT-P02"] = {
    "normalise": N("Moyo wangu ni mzito kila asubuhi.", "Moyo wangu ni mzito"),
    "translate": {
        A: T("heart my is heavy every morning", "Every morning my heart feels heavy.", 0.85, [MOYO]),
        B: T("heart my is heavy each morning", "Every morning I feel heavy-hearted.", 0.8, [MOYO]),
        C: T("heart my is heavy every morning", "My heart is heavy every morning.", 0.8, [MOYO]),
    },
    "back_translate": {A: {"text": "Kila asubuhi moyo wangu unakuwa mzito."}, B: {"text": "Kila asubuhi najisikia moyo mzito."},
                       C: {"text": "Moyo wangu ni mzito kila asubuhi."}},
    "interpret": {
        A: {"senses": [S("sadness", "Sadness or sorrow, felt as heaviness of the heart.", "emotional_state", "everyday_cultural",
                         "Common idiom of sorrow.", [U("Moyo wangu ni mzito")], 0.8)]},
        B: {"senses": [S("sadness", "Low, sorrowful mood.", "emotional_state", "everyday_cultural", "Heaviness of heart = sorrow.",
                         [U("Moyo wangu ni mzito")], 0.8),
                       S("morning reluctance", "Dread or reluctance on waking to face the day.", "emotional_state", "everyday_cultural",
                         "'Kila asubuhi' points to a morning pattern.", [U("kila asubuhi")], 0.4, ["temporality: recurrent"])]},
        C: {"senses": [S("sadness", "Sad mood.", "emotional_state", "mixed", "Idiom of sorrow.", [U("Moyo wangu ni mzito")], 0.7),
                       S("chest heaviness", "A physical sensation of heaviness in the chest.", "clinical_symptom", "clinical",
                         "A literal reading of 'moyo' as the chest; include for clinician check.", [U("Moyo")], 0.2)]},
    },
}

F["PILOT-P03"] = {
    "normalise": N("Nina mawazo mengi, siwezi kufanya kazi.", "Nina mawazo mengi"),
    "translate": {
        A: T("I-have thoughts many, I-cannot do work", "I am thinking too much; I can't work.", 0.75, [MAWAZO]),
        B: T("I-have thoughts many, I-cannot do work", "I have a lot on my mind, I can't work.", 0.75, [MAWAZO]),
        C: T("I-have worries many, I-cannot work", "I am worrying a lot and cannot work.", 0.7, [],
             "Rendered 'mawazo' as worries."),
    },
    "back_translate": {A: {"text": "Nawaza sana; siwezi kufanya kazi."}, B: {"text": "Nina mambo mengi akilini, siwezi kufanya kazi."},
                       C: {"text": "Nina wasiwasi mwingi na siwezi kufanya kazi."}},
    "interpret": {
        A: {"senses": [S("thinking too much", "The 'thinking too much' idiom of distress: persistent troubling thoughts, often about life problems.",
                         "cognitive_process", "everyday_cultural", "'Mawazo mengi' is a widely reported East African idiom of distress.",
                         [U("mawazo mengi"), BG], 0.8),
                       S("worry", "Worry about problems.", "emotional_state", "everyday_cultural", "Overlaps with worry.", [U("mawazo")], 0.5)]},
        B: {"senses": [S("thinking too much", "Thinking too much about one's problems.", "cognitive_process", "everyday_cultural",
                         "Standard reading of the idiom.", [U("Nina mawazo mengi")], 0.8),
                       S("life stressors", "Preoccupation with social or economic problems (money, family, work).", "social_or_relational",
                         "everyday_cultural", "The idiom often refers to concrete hardship.", [U("siwezi kufanya kazi"), BG], 0.4)]},
        C: {"senses": [S("worry", "Excessive worry.", "emotional_state", "mixed", "Mawazo as worries.", [U("mawazo mengi")], 0.6),
                       S("rumination", "Repetitive negative thinking.", "clinical_symptom", "clinical", "Could correspond to rumination.",
                         [U("mawazo mengi")], 0.4),
                       S("functional impairment", "Unable to work because of the thoughts.", "clinical_symptom", "clinical",
                         "Second clause reports impact on work.", [U("siwezi kufanya kazi")], 0.5)]},
    },
}

F["PILOT-P04"] = {
    "normalise": N("Mawazo yananichoma kichwa usiku.", "Mawazo yananichoma kichwa"),
    "translate": {
        A: T("thoughts they-are-burning-me head at-night", "At night my thoughts burn in my head.", 0.7, [MAWAZO]),
        B: T("thoughts burn-me head night", "At night, thoughts make my head burn.", 0.65, [MAWAZO]),
        C: T("thoughts pierce-me head night", "At night I get headaches from thinking.", 0.5, [],
             "'-choma' can mean burn or pierce."),
    },
    "back_translate": {A: {"text": "Usiku mawazo yananiunguza kichwani."}, B: {"text": "Usiku, mawazo yanafanya kichwa changu kiungue."},
                       C: {"text": "Usiku napata maumivu ya kichwa kwa kufikiri."}},
    "interpret": {
        A: {"senses": [S("thinking too much", "Troubling thoughts experienced as heat or burning in the head.", "cognitive_process",
                         "everyday_cultural", "Idiom joins thinking too much with a bodily metaphor.", [U("Mawazo yananichoma kichwa")], 0.7),
                       S("burning head sensation", "A bodily burning or heat sensation in the head.", "somatic_experience", "everyday_cultural",
                         "Somatic idioms of distress are common.", [U("kichwa")], 0.4)]},
        B: {"senses": [S("night-time intrusive thoughts", "Unwanted thoughts that keep coming at night.", "cognitive_process", "mixed",
                         "'Usiku' places it at night; may affect sleep.", [U("usiku")], 0.5, ["sleep context"]),
                       S("thinking too much", "Thinking too much at night.", "cognitive_process", "everyday_cultural", "Idiom reading.",
                         [U("Mawazo")], 0.6)]},
        C: {"senses": [S("headache", "Headache caused by thinking.", "clinical_symptom", "clinical", "Literal reading of kichwa + choma.",
                         [U("kichwa")], 0.5),
                       S("thinking too much", "Excessive thinking.", "cognitive_process", "mixed", "Mawazo.", [U("Mawazo")], 0.5)]},
    },
}

F["PILOT-P05"] = {
    "normalise": N("Nimerogwa, ndiyo maana siwezi kulala.", "Nimerogwa",
                   edits=[{"from": "Nimelogwa", "to": "Nimerogwa", "type": "phonological_variant",
                           "note": "l/r alternation (-loga / -roga). DRAFT: linguist to confirm which form FarajaMH treats as standard."}],
                   dialect=[{"dialect": "Kimvita (declared)", "evidence": "l/r alternation is widespread; not diagnostic of dialect."}]),
    "translate": {
        A: T("I-have-been-bewitched, that-is why I-cannot sleep", "I have been bewitched; that is why I can't sleep.", 0.85),
        B: T("I-have-been-bewitched, that-is reason I-cannot sleep", "I've been bewitched, that's why I cannot sleep.", 0.85),
        C: T("I-have-been-cursed, therefore I-cannot sleep", "I've been cursed, that's why I can't sleep.", 0.75),
    },
    "back_translate": {A: {"text": "Nimerogwa; ndiyo sababu siwezi kulala."}, B: {"text": "Nimerogwa, ndiyo maana siwezi kulala."},
                       C: {"text": "Nimelaaniwa, ndiyo maana siwezi kulala."}},
    "interpret": {
        A: {"senses": [S("bewitchment explanation", "The speaker attributes their problem to witchcraft; a culturally shared explanation of misfortune.",
                         "spiritual_or_supernatural", "everyday_cultural", "Explanatory model, not in itself a symptom.",
                         [U("Nimelogwa")], 0.8, ["community beliefs", "whether others share the explanation"]),
                       S("sleep difficulty", "Difficulty sleeping.", "somatic_experience", "mixed", "Second clause.", [U("siwezi kulala")], 0.8)]},
        B: {"senses": [S("bewitchment explanation", "Attributing distress to bewitchment.", "spiritual_or_supernatural", "everyday_cultural",
                         "Culturally normative explanation.", [U("Nimelogwa")], 0.8),
                       S("interpersonal conflict", "Witchcraft accusations can signal conflict or suspicion within family or community.",
                         "social_or_relational", "everyday_cultural", "Common social meaning of bewitchment talk.", [BG], 0.3)]},
        C: {"senses": [S("bewitchment explanation", "Belief in being bewitched.", "spiritual_or_supernatural", "mixed", "Direct reading.",
                         [U("Nimelogwa")], 0.7),
                       S("persecutory belief", "A belief of being harmed by others that could be clinically relevant if fixed and out of keeping with local norms.",
                         "clinical_symptom", "clinical", "Include for clinician check only; culturally shared beliefs are not delusions.",
                         [U("Nimelogwa")], 0.2, ["cultural normativity", "other psychotic features"])]},
    },
}

F["PILOT-P06"] = {
    "normalise": N("Niko na stress mob, siwezi kulala.", "Niko na stress mob",
                   edits=[{"from": "stress", "to": "stress", "type": "code_switch_marked", "note": "English loanword kept."},
                          {"from": "mob", "to": "mob", "type": "code_switch_marked", "note": "Sheng intensifier ('a lot'); kept."},
                          {"from": "siwezi lala", "to": "siwezi kulala", "type": "sheng_lexical", "note": "Colloquial infinitive without ku-."}],
                   lang="sw-x-sheng", segs=[{"text": "Niko na", "lang": "sw"}, {"text": "stress", "lang": "en"},
                                            {"text": "mob", "lang": "sw-x-sheng"}, {"text": "siwezi kulala", "lang": "sw"}],
                   dialect=[{"dialect": "Sheng (declared)", "evidence": "'mob', dropped ku- infinitive"}]),
    "translate": {
        A: T("I-am with stress a-lot, I-cannot sleep", "I'm really stressed, I can't sleep.", 0.85, [("stress", "loanword; local sense may be broader than English")]),
        B: T("I-am with stress much, I-cannot sleep", "I'm very stressed and can't sleep.", 0.85),
        C: T("I-am with stress lots, I-cannot sleep", "I'm so stressed, I can't sleep.", 0.85),
    },
    "back_translate": {A: {"text": "Niko na stress sana, siwezi kulala."}, B: {"text": "Nina msongo mkubwa na siwezi kulala."},
                       C: {"text": "Nina stress sana, siwezi kulala."}},
    "interpret": {
        m: {"senses": [S("stress", "Feeling under heavy pressure or strain.", "emotional_state", "mixed", "Loanword used as in everyday Kenyan speech.",
                         [U("stress mob")], 0.8),
                       S("sleep difficulty", "Difficulty sleeping.", "somatic_experience", "mixed", "Second clause.", [U("siwezi lala")], 0.8)]}
        for m in (A, B, C)
    },
}

F["PILOT-P07"] = {
    "normalise": N("Sina raha siku hizi.", "Sina raha"),
    "translate": {
        A: T("I-have-no joy days these", "I have no joy these days.", 0.75, [("raha", "joy / comfort / peace / ease")]),
        B: T("I-have-no happiness days these", "I am not happy these days.", 0.75),
        C: T("I-have-no peace days these", "I have no peace these days.", 0.7, [("raha", "can mean peace or ease, not only happiness")]),
    },
    "back_translate": {A: {"text": "Sina furaha siku hizi."}, B: {"text": "Sina furaha siku hizi."}, C: {"text": "Sina amani siku hizi."}},
    "interpret": {
        A: {"senses": [S("low mood", "Persistently low or unhappy mood.", "emotional_state", "everyday_cultural", "Common way to report unhappiness.",
                         [U("Sina raha")], 0.7)]},
        B: {"senses": [S("loss of pleasure", "Not finding pleasure in things.", "clinical_symptom", "mixed", "Could indicate anhedonia.",
                         [U("Sina raha")], 0.5),
                       S("low mood", "Feeling unhappy.", "emotional_state", "everyday_cultural", "Plain reading.", [U("Sina raha")], 0.6)]},
        C: {"senses": [S("lack of peace", "No inner peace or ease; feeling unsettled.", "emotional_state", "everyday_cultural",
                         "Raha as ease/peace.", [U("raha")], 0.6)]},
    },
}

F["PILOT-P09"] = {
    "normalise": N("Siku hizi sina mawazo mengi kama zamani.", "sina mawazo mengi"),
    "translate": {
        A: T("days these I-have-no thoughts many like before", "These days I don't think too much like I used to.", 0.75, [MAWAZO]),
        B: T("days these I-have-no thoughts many like past", "Nowadays I don't have as much on my mind as before.", 0.75),
        C: T("days these I-have-no worries many like before", "These days I don't worry as much as I did.", 0.7),
    },
    "back_translate": {A: {"text": "Siku hizi siwazi sana kama zamani."}, B: {"text": "Siku hizi sina mambo mengi akilini kama zamani."},
                       C: {"text": "Siku hizi sina wasiwasi mwingi kama zamani."}},
    "interpret": {
        A: {"senses": [S("thinking too much", "The 'thinking too much' idiom, reported as ABSENT or reduced now.", "cognitive_process",
                         "everyday_cultural", "Negated form; polarity must be kept.", [U("sina mawazo mengi"), CX("negation", "negated")], 0.7)]},
        B: {"senses": [S("thinking too much", "Reports improvement: no longer thinking too much.", "cognitive_process", "everyday_cultural",
                         "Negation plus 'kama zamani' implies improvement.", [U("kama zamani"), CX("negation", "negated")], 0.7)]},
        C: {"senses": [S("worry", "Worry reduced compared with before.", "emotional_state", "everyday_cultural", "Negated worry.",
                         [U("sina mawazo mengi")], 0.6)]},
    },
}

F["PILOT-P10"] = {
    "normalise": N("Mama yangu hana raha tangu baba afariki.", "hana raha"),
    "translate": {
        A: T("mother my she-has-no joy since father died", "My mother has had no joy since father died.", 0.8),
        B: T("mother my has-no happiness since father passed", "My mother has been unhappy since my father passed away.", 0.8),
        C: T("mother my has-no peace since father died", "My mother has had no peace since father died.", 0.75),
    },
    "back_translate": {A: {"text": "Mama yangu hana furaha tangu baba afariki."}, B: {"text": "Mama yangu hana furaha tangu baba yangu afariki dunia."},
                       C: {"text": "Mama yangu hana amani tangu baba afariki."}},
    "interpret": {
        A: {"senses": [S("low mood", "The MOTHER (not the speaker) has been unhappy.", "emotional_state", "everyday_cultural",
                         "Experiencer is the mother.", [U("Mama yangu hana raha"), CX("attribution", "family_member")], 0.7)]},
        B: {"senses": [S("grief", "The mother's grief after her husband's death.", "emotional_state", "everyday_cultural",
                         "Onset is the death.", [U("tangu baba afariki"), CX("attribution", "family_member")], 0.7)]},
        C: {"senses": [S("grief", "Bereavement reaction in the mother.", "emotional_state", "mixed", "Onset tied to death.",
                         [U("tangu baba afariki")], 0.6),
                       S("lack of peace", "The mother is unsettled, without peace.", "emotional_state", "everyday_cultural", "Raha as peace.",
                         [U("hana raha")], 0.4)]},
    },
}

# Placeholder terminology results keyed by cluster label (the retrieval query). Labels are search hints, not codes.
TERMS = {
    "inner emptiness": {"SNOMEDCT": ["feeling empty"]},
    "grief": {"SNOMEDCT": ["grief", "bereavement finding"], "MFOEM": ["grief-related emotion"]},
    "spiritual loss": {"SNOMEDCT": ["spiritual concern"]},
    "loss of vitality": {"SNOMEDCT": ["lack of energy"]},
    "fright": {"SNOMEDCT": ["fear"], "MFOEM": ["fear"]},
    "sadness": {"SNOMEDCT": ["feeling sad"], "MFOEM": ["sadness"]},
    "morning reluctance": {},
    "chest heaviness": {"SNOMEDCT": ["chest heaviness"]},
    "thinking too much": {"SNOMEDCT": ["worrying", "rumination"]},
    "worry": {"SNOMEDCT": ["worrying"], "MFOEM": ["anxiety"]},
    "life stressors": {},
    "rumination": {"SNOMEDCT": ["rumination"]},
    "functional impairment": {"SNOMEDCT": ["difficulty performing work"]},
    "burning head sensation": {"SNOMEDCT": ["burning sensation of head"]},
    "night-time intrusive thoughts": {"SNOMEDCT": ["intrusive thoughts"]},
    "headache": {"SNOMEDCT": ["headache"]},
    "bewitchment explanation": {},
    "interpersonal conflict": {"SNOMEDCT": ["interpersonal relationship problem"]},
    "persecutory belief": {"SNOMEDCT": ["persecutory delusion"]},
    "sleep difficulty": {"SNOMEDCT": ["difficulty sleeping"]},
    "stress": {"SNOMEDCT": ["feeling stressed"], "MFOEM": ["stress-related emotion"]},
    "low mood": {"SNOMEDCT": ["low mood"], "MFOEM": ["sadness"]},
    "loss of pleasure": {"SNOMEDCT": ["anhedonia"]},
    "lack of peace": {"SNOMEDCT": ["feeling restless"]},
}

if __name__ == "__main__":
    d = Path(__file__).parent / "fixtures"
    d.mkdir(exist_ok=True)
    (d / "simulated_responses.json").write_text(json.dumps(
        {"_warning": "SIMULATED fixture responses written by hand for pipeline testing. Not model outputs. Not validated interpretations."} | F,
        ensure_ascii=False, indent=1), encoding="utf-8")
    (d / "terminology_fixture.json").write_text(json.dumps(TERMS, indent=1), encoding="utf-8")
    print(f"{len(F)} utterances with fixtures; {len(TERMS)} placeholder term queries")
