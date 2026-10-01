# Review card — KISWA-STORY-11
Package `MRP-KISWA-STORY-11-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/rationale* — ……risk. the preceding conversation about self-harm increases the importance of this readin……
> - `self-harm` in *sense/S4/gloss* — ……t, which may indicate a risk of harm or self-harm.…
> - `self-harm` in *sense/S4/rationale* — ……t, which may indicate a risk of harm or self-harm, especially given the context of stress……
> - `kujidhuru` in *sense/S6/rationale* — ……us conversation about having 'mawazo ya kujidhuru' (thoughts of harming oneself) and thei……
> - `suicidal ideation` in *gap_note/C1* — ……uld need to cover existential distress, suicidal ideation, or similar emotional states. | the can……
> - `better off dead` in *gap_note/C1* — ……e idea of wishing one were not alive or better off dead, which is a specific emotional state re……
> - `nife` in *gap_note/C3* — ……retrieved concepts focus on specific manifestations of sadness (facial expressions,……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 3 of 3 models proposed a `risk_or_safety` reading (unanimous): **risk_or_safety**.
>
> Grounding: 2 quotes from the utterance itself; 1 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.70, 0.70, 0.60 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Kuna siku nafikiri afadhali nisiwepo. Lakini watoto wananihitaji.
**Expression:** afadhali nisiwepo
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Kuna siku nafikiri afadhali nisiwepo. Lakini watoto wananihitaji.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | There days I think it is better I not be [present/exist]. | There are days when I think it would be better if I weren't here. | not run |  |
| T2 | qwen2.5:7b | please think for me today but children need. | Please think of me today, but the children need you. | not run | uncertain |
| T3 | llama3.1:8b | it would be better for me not to exist | I wish I wasn't here | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C1 | desire_for_absence | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C3 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, desire_for_absence): The speaker expresses a wish or feeling that they would be better off not existing. — *The phrase 'afadhali nisiwepo' directly translates to 'it would be better if I weren't here,' indicating a desire to not be present.* — evidence: utterance_span: “afadhali nisiwepo”
- **S2** (gemma3:12b, risk_or_safety): The speaker expresses a desire to not be here, which may be a statement of intent or a hyperbolic expression of distress. — *The phrase 'afadhali nisiwepo' expresses a desire to not exist, which, regardless of its literal meaning, requires assessment for risk. The preceding conversation about self-harm increases the importance of this reading.* — evidence: utterance_span: “afadhali nisiwepo”
- **S3** (qwen2.5:7b, sadness): The speaker is expressing a desire not to be present, indicating sadness or a wish to be absent. — *The speaker uses the expression 'afadhali nisiwepo' which translates to 'it would be better if I weren't here', indicating a desire to be absent.* — evidence: utterance_span: “afadhali nisiwepo”
- **S4** (qwen2.5:7b, risk_or_safety): The speaker is expressing a wish not to be present, which may indicate a risk of harm or self-harm. — *The expression 'afadhali nisiwepo' suggests a desire to be absent, which may indicate a risk of harm or self-harm, especially given the context of stress and mood issues.* — evidence: utterance_span: “afadhali nisiwepo”
- **S5** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker mentions being 'down sana' and having 'stress imezidi', indicating a negative emotional state. The phrase 'afadhali nisiwepo' can be seen as an expression of this sadness, a feeling of being overwhelmed and wishing to escape.* — evidence: conversation_turn: “Niko down sana, stress imezidi. Sina mood ya kitu.”
- **S6** (llama3.1:8b, risk_or_safety): expressing a desire to harm oneself — *The speaker's previous conversation about having 'mawazo ya kujidhuru' (thoughts of harming oneself) and their current emotional state of being 'down sana' and having 'stress imezidi' suggest that the phrase 'afadhali nisiwepo' may be more than just an expression of sadness. It may be a genuine expression of a desire to escape or harm oneself.* — evidence: conversation_turn: “Je, umewahi kuwa na mawazo ya kujidhuru?”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOMD:0000081` sexual desire disorder [] — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 1 place(s): llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Niko down sana, stress imezidi. Sina mood ya kitu." → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.054, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.921, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
