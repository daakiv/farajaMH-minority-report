# Review card — PILOT-P02
Package `MRP-PILOT-P02-batch-01` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/gloss* — ……that warrants assessment for potential self-harm or a desire to escape a difficult situa……
> - `nife` in *gap_note/C1* — ……do not fit, as they describe specific manifestations of sadness rather than the emot……
> - `suicidal ideation` in *gap_note/C2* — ……epts relating to severe emotional pain, suicidal ideation, or a strong urge to flee would be rele……
> - `self-harm` in *gap_note/C2* — ……essing distress, potentially related to self-harm or escape from a difficult situation. |……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Moyo wangu ni mzito kila asubuhi.
**Expression:** Moyo wangu ni mzito
**Context:** KE/KE-western, dialect standard, speaker participant, setting clinic, negation affirmed, temporality recurrent, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Moyo wangu ni mzito kila asubuhi.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | heart my is heavy | My heart feels heavy. | not run |  |
| T2 | qwen2.5:7b | My heart is heavy every day. | I feel heavy-hearted every day. | not run |  |
| T3 | llama3.1:8b | My heart is heavy every morning | I wake up feeling weighed down every day | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sadness): The speaker is experiencing a persistent feeling of sadness or dejection. — *The phrase 'Moyo wangu ni mzito' (My heart is heavy) is a common metaphor for sadness or emotional burden. The recurrent nature ('kila asubuhi' - every morning) suggests a chronic or persistent feeling.* — evidence: utterance_span: “Moyo wangu ni mzito”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a degree of distress that warrants assessment for potential self-harm or a desire to escape a difficult situation. — *The phrase 'Moyo wangu ni mzito' (My heart is heavy) could be a hyperbolic expression of deep distress. Although it may be idiomatic, the clinical context requires consideration of potential risk. It is not possible to determine whether this is a literal statement of risk or an expression of distress.* — evidence: utterance_span: “Moyo wangu ni mzito”
- **S3** (qwen2.5:7b, sadness): I feel sad every day. — *The speaker is using the term 'mzito', which can mean 'heavy' or 'weighed down', and is attributing this feeling to their heart ('moyo'), indicating a daily emotional state of sadness.* — evidence: utterance_span: “Moyo wangu ni mzito kila asubuhi.”
- **S4** (llama3.1:8b, sadness): feeling a sense of heaviness or sorrow — *The speaker affirms the statement, indicating a personal experience of heaviness.* — evidence: utterance_span: “Moyo wangu ni mzito”
- **S5** (llama3.1:8b, risk_or_safety): feeling overwhelmed or burdened to the point of considering harm — *The speaker's use of 'mzito' may be idiomatic, but the context of a clinic and the speaker's affirmation of the statement suggest a possible risk of harm.* — evidence: utterance_span: “Moyo wangu ni mzito”; context_field: “clinic”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.139, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.971, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
