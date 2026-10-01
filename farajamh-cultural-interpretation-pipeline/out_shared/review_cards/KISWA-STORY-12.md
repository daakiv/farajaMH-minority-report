# Review card — KISWA-STORY-12
Package `MRP-KISWA-STORY-12-indep-shared` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/rationale* — ……ven the context of a conversation about self-harm. the speaker's reliance on god may be a……
> - `self-harm` in *sense/S3/rationale* — ……n the context of the conversation about self-harm.…
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
> Self-reported plausibility for these senses: 0.90, 0.00 — poorly calibrated on small models; weigh the grounding above it.
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
| T1 | gemma3:12b | God Almighty only | Only God knows. | not run | The phrase 'Only God knows' is often used to express overwhelming distress, frustration, or a sense of being beyond comprehension. It's a way of saying 'I can't even begin to explain how I feel' or 'This is beyond my understanding'. |
| T2 | qwen2.5:7b | God my is. And one neighbor. | God, me, and one neighbor. | not run | uncertain |
| T3 | llama3.1:8b | God alone is my concern | My only worry is God | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 2/3 models (gemma3:12b, llama3.1:8b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **social_or_relational**: 1/3 models (gemma3:12b)
- **spiritual_or_supernatural**: 1/3 models (qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | worry | emotional_state | minority | gemma3:12b |
| C3 | reliance | social_or_relational | minority | gemma3:12b |
| C4 | god知晓 | spiritual_or_supernatural | minority | qwen2.5:7b |
| C5 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, worry): The speaker expresses that their only concern or focus is God. — *The phrase 'Mwenyezi Mungu tu' can be interpreted as a statement of preoccupation or sole focus, implying a significant worry or reliance on God in a difficult situation. The translations 'God, me, and one neighbor' and 'My only worry is God' support this reading.* — evidence: translation_candidate: “God, me, and one neighbor.”; translation_candidate: “My only worry is God.”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a desire to not exist, which warrants consideration as a potential expression of distress or a statement of intent. — *The phrase 'nafikiri afadhali nisiwepo' (I think it would be better if I didn't exist) directly expresses a desire to not be here. While this may be hyperbolic, it necessitates a risk assessment given the context of a conversation about self-harm. The speaker's reliance on God may be a coping mechanism or a reflection of their emotional state.* — evidence: conversation_turn: “Lakini watoto wananihitaji.”; conversation_turn: “Kuna siku nafikiri afadhali nisiwepo.”
- **S3** (gemma3:12b, reliance): The speaker is expressing a dependence on God for support or understanding. — *The phrase 'Mwenyezi Mungu tu' can be interpreted as a statement of reliance, indicating that the speaker is turning to God for comfort or guidance in a difficult situation. This is especially relevant given the context of the conversation about self-harm.* — evidence: utterance_span: “Mwenyezi Mungu tu.”
- **S4** (qwen2.5:7b, god知晓): 表达对上帝的依赖或信任。 — *表达中使用了‘Mwenyezi Mungu’，意为‘上帝’，表明了对上帝的依赖或信任。* — evidence: utterance_span: “Mwenyezi Mungu tu.”
- **S5** (llama3.1:8b, sadness): Feeling sad or unhappy about something. — *The speaker mentions thinking it would be better if they weren't there, which suggests a negative emotional state.* — evidence: conversation_turn: “Kuna siku nafikiri afadhali nisiwepo”
- **S6** (llama3.1:8b, risk_or_safety): Expressing a desire to harm oneself or be gone. — *The speaker says 'afadhali nisiwepo', which can be translated to 'it would be better if I wasn't here', which may be an expression of a desire to leave or exit the world.* — evidence: conversation_turn: “Kuna siku nafikiri afadhali nisiwepo”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000171` worry []; `MFOEM:000168` concern [llama3.1:8b→skos:broadMatch]; `MFOMD:0000184` nervousness [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C5**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output repaired in 7 place(s): gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret evidence.type (quote not in the utterance)="utterance_span: Lakini watoto wananihitaji." → conversation_turn; gemma3:12b/interpret evidence.type (quote not in the utterance)="utterance_span: Kuna siku nafikiri afadhali nisiwepo." → conversation_turn; gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Kuna siku nafikiri afadhali nisiwepo" → conversation_turn …
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.9, 'translation_agreement': 0.3, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.97, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
