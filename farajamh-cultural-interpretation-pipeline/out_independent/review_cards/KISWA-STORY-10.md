# Review card — KISWA-STORY-10
Package `MRP-KISWA-STORY-10-indep-solo` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `harming myself` in *sense/S5/gloss* — ……'m feeling so down that i'm considering harming myself…
> - `self-harm` in *sense/S5/rationale* — ……and context suggest a possible risk of self-harm.…
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 3 quotes from the utterance itself; 1 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.80, 0.60 — poorly calibrated on small models; weigh the grounding above it.
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
| T1 | gemma3:12b | I am down very, stress has exceeded. I have mood of nothing. | I'm really feeling low, the stress has gotten too much. I don't feel like doing anything. | not run |  |
| T2 | qwen2.5:7b | I am very sad, my heart is heavy. | I am feeling very sad. | not run |  |
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

- **S1** (gemma3:12b, sadness): The speaker is feeling very sad or depressed. — *The phrase 'Niko down sana' suggests a low mood. The statement 'Sina mood ya kitu' reinforces this, indicating a lack of interest or enthusiasm.* — evidence: utterance_span: “Niko down sana”; utterance_span: “Sina mood ya kitu”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a desire to isolate and avoid interaction, which warrants consideration for risk and safety. — *The phrase 'Niko down sana' and the subsequent statements about lacking motivation and avoiding social contact, combined with the refusal to see people, may be a veiled expression of distress or a potential indicator of a desire to withdraw from life. It is important to assess the speaker's safety and well-being, even if the phrasing is hyperbolic.* — evidence: utterance_span: “Niko down sana”; conversation_turn: “Nimejifungia ndani. Sitaki kuona mtu.”; utterance_span: “Sina mood ya kitu”
- **S3** (qwen2.5:7b, sadness): Niko feels very sad. — *The phrase 'Niko down sana' directly conveys a strong emotional state, and the speaker attributes this to themselves.* — evidence: utterance_span: “Niko down sana”
- **S4** (llama3.1:8b, sadness): I'm feeling extremely down — *The speaker uses the word 'sana' to emphasize their emotional state, and the context indicates that they are affirming their feelings rather than denying them.* — evidence: utterance_span: “Niko down sana”
- **S5** (llama3.1:8b, risk_or_safety): I'm feeling so down that I'm considering harming myself — *The speaker's use of 'sana' to describe their emotional state may be idiomatic, but the overall tone and context suggest a possible risk of self-harm.* — evidence: utterance_span: “Niko down sana”; model_background_knowledge: “”

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
