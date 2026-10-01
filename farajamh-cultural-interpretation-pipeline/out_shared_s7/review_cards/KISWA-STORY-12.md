# Review card — KISWA-STORY-12
Package `MRP-KISWA-STORY-12-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/gloss* — ……ich requires consideration of potential self-harm risk.…
> - `self-harm` in *sense/S4/rationale* — …the speaker mentions having thoughts of self-harm and feeling overwhelmed, which suggests……
> - `self-harm` in *gap_note/C2* — ……ire to not exist, considering potential self-harm risk, and potentially idiomatic. | the……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 3 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.90, 0.90 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Mwenyezi Mungu tu. Na jirani mmoja.
**Expression:** Mwenyezi Mungu tu
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Mwenyezi Mungu tu. Na jirani mmoja.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | God Almighty only | Only God knows. | not run | The phrase 'Only God knows' is often used to express frustration, overwhelm, or a sense of helplessness about a situation. It implies that the speaker feels the situation is beyond their understanding or control. |
| T2 | qwen2.5:7b | God is the moon. God is the moon. | God is the moon. | not run | Uncertain |
| T3 | llama3.1:8b | God alone is heavy on my heart | I'm feeling overwhelmed and burdened by my problems | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | overwhelmed | emotional_state | majority | gemma3:12b, llama3.1:8b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | only_god | emotional_state | minority | qwen2.5:7b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, overwhelmed): The speaker expresses a feeling of being burdened and unable to cope. — *The translation candidate 'I'm feeling overwhelmed and burdened by my problems' aligns with the speaker's prior statement indicating a desire to not exist, suggesting a sense of being overwhelmed.* — evidence: translation_candidate: “I'm feeling overwhelmed and burdened by my problems”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a desire to not exist, which requires consideration of potential self-harm risk. — *The phrase 'Lakini watoto wananihitaji' may be hyperbolic, but the preceding statement 'Kuna siku nafikiri afadhali nisiwepo' indicates a desire to not be here, which necessitates a risk assessment.* — evidence: conversation_turn: “Kuna siku nafikiri afadhali nisiwepo.”; conversation_turn: “Je, umewahi kuwa na mawazo ya kujidhuru?”
- **S3** (qwen2.5:7b, only_god): Only God knows the speaker's thoughts or situation. — *The speaker uses the phrase 'Mwenyezi Mungu tu' which means 'Only God knows' in Swahili, indicating uncertainty or a belief that their thoughts or situation are unknown to others.* — evidence: utterance_span: “Mwenyezi Mungu tu. Na jirani mmoja.”
- **S4** (llama3.1:8b, overwhelmed): feeling burdened by problems — *The speaker mentions having thoughts of self-harm and feeling overwhelmed, which suggests a state of emotional distress.* — evidence: conversation_turn: “Kuna siku nafikiri afadhali nisiwepo”
- **S5** (llama3.1:8b, risk_or_safety): expressing a desire to harm oneself — *The speaker's statement 'Kuna siku nafikiri afadhali nisiwepo' may be idiomatic, but it explicitly mentions a desire to be absent, which could be interpreted as a risk to one's safety.* — evidence: conversation_turn: “Kuna siku nafikiri afadhali nisiwepo”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000027` terror []; `MFOMD:0000076` dissociative fugue [llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000081` appraisal as caused supernaturally [llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, multiple_components_in_utterance, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output repaired in 3 place(s): gemma3:12b/interpret evidence.type (quote not in the utterance)="utterance_span: Kuna siku nafikiri afadhali nisiwepo." → conversation_turn; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Kuna siku nafikiri afadhali nisiwepo" → conversation_turn; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Kuna siku nafikiri afadhali nisiwepo" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.9, 'translation_agreement': 0.083, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
