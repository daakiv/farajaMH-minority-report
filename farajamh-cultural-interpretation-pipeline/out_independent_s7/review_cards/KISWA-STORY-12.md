# Review card — KISWA-STORY-12
Package `MRP-KISWA-STORY-12-indep-solo-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S1/rationale* — ……ss. the context of a conversation about self-harm further supports this interpretation.…
> - `leave the world` in *sense/S5/gloss* — …expressing a desire to die or leave the world…
> - `leave the world` in *sense/S5/rationale* — ……be an expression of a desire to die or leave the world, despite the idiomatic phrasing.…
> - `nife` in *gap_note/C3* — ……ic emotion like sadness, a particular manifestation of sadness (facial expression or……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 2 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.90, 0.80 — poorly calibrated on small models; weigh the grounding above it.
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
| C1 | distress | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, distress): The speaker is expressing a general sense of distress or suffering. — *The utterance 'Mwenyezi Mungu tu' (God alone) can be an expression of feeling overwhelmed and isolated, often accompanying distress. The context of a conversation about self-harm further supports this interpretation.* — evidence: utterance_span: “Mwenyezi Mungu tu”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a desire to not be present, which warrants consideration as a potential statement of risk. — *The phrase 'nafikiri afadhali nisiwepo' (I think it would be better if I wasn't here) directly expresses a wish to not exist. While it may be hyperbolic, this phrasing requires assessment for risk, given the preceding conversation.* — evidence: conversation_turn: “Lakini watoto wananihitaji.”
- **S3** (qwen2.5:7b, sadness): The speaker is expressing sadness or distress. — *The speaker uses a negation ('tu' meaning 'not') to affirm a distressing statement, indicating sadness or distress.* — evidence: utterance_span: “Mwenyezi Mungu tu. Na jirani mmoja.”
- **S4** (llama3.1:8b, sadness): Feeling unhappy or sorrowful — *The speaker says 'Kuna siku nafikiri afadhali nisiwepo', which implies a sense of sadness or regret.* — evidence: conversation_turn: “Kuna siku nafikiri afadhali nisiwepo”
- **S5** (llama3.1:8b, risk_or_safety): Expressing a desire to die or leave the world — *The speaker says 'Kuna siku nafikiri afadhali nisiwepo', which may be an expression of a desire to die or leave the world, despite the idiomatic phrasing.* — evidence: conversation_turn: “Kuna siku nafikiri afadhali nisiwepo”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000031` crying []; `MFOEM:000052` compassion []; `MFOEM:000055` shame []; `MFOEM:000216` gloomy mood [llama3.1:8b→skos:broadMatch]; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000151` binge-eating disorder []; `MFOMD:0000004` mental disorder []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000187` abstinence syndrome [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 2 place(s): llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Kuna siku nafikiri afadhali nisiwepo" → conversation_turn; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Kuna siku nafikiri afadhali nisiwepo" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.9, 'translation_agreement': 0.083, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
