# Review card — KISWA-STORY-10
Package `MRP-KISWA-STORY-10-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/rationale* — ……ki kuona mtu.'), may indicate a risk of self-harm or social withdrawal. the phrasing may……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 1 quote from the utterance itself; 2 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.80, 0.70 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Niko down sana, stress imezidi. Sina mood ya kitu.
**Expression:** Niko down sana
**Context:** KE/KE-western, dialect Sheng, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Niko down sana, stress imezidi. Sina mood ya kitu.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I am down very, stress has exceeded. I have mood of nothing. | I'm feeling really low, the stress has gotten too much. I don't feel like doing anything. | not run |  |
| T2 | qwen2.5:7b | I am very down, my mood is heavy. | I am feeling very sad, my mood is heavy. | not run |  |
| T3 | llama3.1:8b | I am down very much | I'm feeling really down, overwhelmed with stress | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sadness): The speaker is experiencing a profound sense of sadness or dejection. — *The phrase 'Niko down sana' is commonly used to express feeling low or sad. The subsequent statement 'stress imezidi' and 'Sina mood ya kitu' reinforces this sense of emotional distress.* — evidence: utterance_span: “Niko down sana”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially hyperbolic, expresses a desire to isolate and avoid interaction, which warrants consideration for safety. — *The phrase 'Niko down sana' and the subsequent statements, taken together with the speaker's expressed desire to isolate themselves ('Nimejifungia ndani. Sitaki kuona mtu.'), may indicate a risk of self-harm or social withdrawal. The phrasing may be idiomatic or hyperbolic, but this does not negate the need to assess the speaker's safety.* — evidence: conversation_turn: “Nimejifungia ndani. Sitaki kuona mtu.”
- **S3** (qwen2.5:7b, sadness): The speaker is feeling very sad and down. — *The speaker uses the phrase 'Niko down sana' which directly translates to 'I am feeling really down', indicating a state of sadness.* — evidence: utterance_span: “Niko down sana, stress imezidi. Sina mood ya kitu.”
- **S4** (llama3.1:8b, sadness): feeling very sad or depressed — *The speaker says 'Niko down sana', which means 'I'm feeling really low' or 'I'm feeling very sad'. This is a common way to express sadness in Sheng.* — evidence: translation_candidate: “I'm feeling really low, the stress has gotten too much.”
- **S5** (llama3.1:8b, risk_or_safety): expressing a desire to withdraw from the world due to emotional distress — *The speaker says 'Niko down sana' and 'Sina mood ya kitu', which means 'I'm feeling really low' and 'I don't feel like doing anything'. This may be an expression of a desire to withdraw from the world due to emotional distress.* — evidence: utterance_span: “Niko down sana, stress imezidi. Sina mood ya kitu.”; conversation_turn: “Nimejifungia ndani. Sitaki kuona mtu.”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 1 place(s): gemma3:12b/normalise language_id="['sw', 'en']" → sw
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.077, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.971, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
