# Review card — KISWA-STORY-01
Package `MRP-KISWA-STORY-01-indep-solo-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/gloss* — ……at warrants consideration for potential self-harm or a desire to avoid further suffering.…
> - `suicidal ideation` in *gap_note/C2* — ……otional distress, potentially including suicidal ideation or a strong wish to escape overwhelming……
> - `self-harm` in *gap_note/C2* — ……emotional state of distress related to self-harm or avoidance of further suffering. | co……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 3 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.80, 0.30 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Sijambo, lakini moyo wangu umekuwa mzito tangu majuma matatu.
**Expression:** moyo wangu umekuwa mzito
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Sijambo, lakini moyo wangu umekuwa mzito tangu majuma matatu.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I am not well, but my heart has become heavy since three weeks. | I'm not doing well, but my heart has been heavy for three weeks. | not run |  |
| T2 | qwen2.5:7b | My heart has become heavy from three days. | My heart has become heavy these past three days. | not run |  |
| T3 | llama3.1:8b | my heart is heavy every day since three weeks | I've been feeling really down since three weeks | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sadness): The speaker expresses a feeling of sadness or heaviness. — *The phrase 'moyo wangu umekuwa mzito' (my heart has become heavy) is a common metaphor for sadness or emotional distress. The speaker's initial statement 'Sijambo' (I am not well) further supports this interpretation.* — evidence: utterance_span: “moyo wangu umekuwa mzito”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a degree of distress that warrants consideration for potential self-harm or a desire to avoid further suffering. — *The phrase 'moyo wangu umekuwa mzito' (my heart has become heavy) could be a veiled expression of a desire to end suffering. While it may be a common idiom, it's crucial to acknowledge the potential for underlying distress and risk. The initial statement 'Sijambo' (I am not well) reinforces the need for careful assessment.* — evidence: utterance_span: “Sijambo, lakini moyo wangu umekuwa mzito tangu majuma matatu”
- **S3** (qwen2.5:7b, sadness): My heart feels heavy. — *The speaker is expressing a current, self-attributed emotional state of heaviness in the heart, which is a common way to express sadness in everyday language.* — evidence: utterance_span: “moyo wangu umekuwa mzito”
- **S4** (llama3.1:8b, heart_heaviness): My heart feels heavy — *The speaker says 'moyo wangu umekuwa mzito', which means 'my heart has become heavy'. This is a common idiomatic expression in Swahili to describe feeling emotionally burdened or overwhelmed.* — evidence: utterance_span: “moyo wangu umekuwa mzito”
- **S5** (llama3.1:8b, risk_or_safety): The speaker may be at risk of emotional or mental health issues — *The speaker says 'sijambo', which means 'I am not fine', and 'moyo wangu umekuwa mzito', which means 'my heart has become heavy'. This may be an expression of distress or a cry for help.* — evidence: utterance_span: “sijambo”; utterance_span: “moyo wangu umekuwa mzito”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.191, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.971, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
