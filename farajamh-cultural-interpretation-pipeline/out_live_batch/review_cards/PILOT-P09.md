# Review card — PILOT-P09
Package `MRP-PILOT-P09-batch-01` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *gap_note/C4* — ……s a specific emotion and a particular manifestation of it (facial expression, voice)……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Siku hizi sina mawazo mengi kama zamani.
**Expression:** sina mawazo mengi
**Context:** TZ/TZ-lake, dialect standard, speaker participant, setting hdss_survey, negation negated, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Siku hizi sina mawazo mengi kama zamani.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I these days I have thoughts many as old times. | Lately, I haven't been thinking as much as I used to. | not run | None |
| T2 | qwen2.5:7b | These days I have much thinking as before. | These days I have a lot on my mind. | not run |  |
| T3 | llama3.1:8b | I have few thoughts as before. | I'm not thinking clearly like I used to. | not run |  |

### How the models read it, by category (labels aside)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 2/3 models (llama3.1:8b, qwen2.5:7b)
- **cognitive_process**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | reduced_thought | cognitive_process | minority | gemma3:12b |
| C3 | thinking_less | emotional_state | minority | qwen2.5:7b |
| C4 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, reduced_thought): The speaker is experiencing a decrease in their usual level of thought or mental activity. — *The phrase 'sina mawazo mengi' directly translates to 'I don't have many thoughts,' indicating a reduction in thought processes. The comparison 'kama zamani' (like before) suggests a change from a previous state.* — evidence: utterance_span: “sina mawazo mengi”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a change in mental state that could be indicative of underlying distress or a desire to avoid thinking about difficult circumstances; it warrants further assessment. — *While 'sina mawazo mengi' may be a casual observation about reduced thought, a sudden or significant decrease in cognitive activity can be a sign of distress or a coping mechanism to avoid difficult emotions or situations. The phrasing may be hyperbolic, but the potential for underlying risk necessitates a safety assessment.* — evidence: utterance_span: “Siku hizi sina mawazo mengi kama zamani”
- **S3** (qwen2.5:7b, thinking_less): I am not thinking as much as I used to. — *The speaker is negating the presence of a lot of thought, indicating a reduction in cognitive activity.* — evidence: utterance_span: “sina mawazo mengi kama zamani”
- **S4** (llama3.1:8b, sadness): feeling unhappy or depressed — *The speaker uses the negated form 'sina mawazo mengi', which implies a lack or decrease in thoughts, which can be associated with feelings of sadness or depression.* — evidence: utterance_span: “sina mawazo mengi”
- **S5** (llama3.1:8b, risk_or_safety): expressing a desire to escape or end one's situation — *The speaker's statement 'sina mawazo mengi' may be idiomatic, but the negation and current temporality suggest a possible expression of distress or desire to escape one's situation.* — evidence: utterance_span: “sina mawazo mengi”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, polarity_negated, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.983, 'translation_agreement': 0.083, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.961, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
