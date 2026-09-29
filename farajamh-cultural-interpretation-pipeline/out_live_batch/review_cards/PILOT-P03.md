# Review card — PILOT-P03
Package `MRP-PILOT-P03-batch-01` · priority **high** · backend `live`

## Step 1 — Your own reading first (blind pass)
**Utterance:** Nina mawazo mengi, siwezi kufanya kazi.
**Expression:** Nina mawazo mengi
**Context:** TZ/TZ-lake, dialect standard, speaker participant, setting hdss_survey, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Nina mawazo mengi, siwezi kufanya kazi.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I thoughts many, I cannot do work. | I have a lot on my mind, I can't work. | not run | None |
| T2 | qwen2.5:7b | I have many thoughts, cannot do work. | I have so many thoughts, I can't do my work. | not run |  |
| T3 | llama3.1:8b | I have many thoughts, I cannot do work | I'm overwhelmed with thoughts and can't cope with work | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | overwhelmed | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | worry | emotional_state | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, worry): The speaker is experiencing a state of worry or anxiety. — *The phrase 'Nina mawazo mengi' (I have many thoughts) often indicates a state of worry or preoccupation. The subsequent statement 'siwezi kufanya kazi' (I cannot work) reinforces this, suggesting the thoughts are causing distress.* — evidence: utterance_span: “Nina mawazo mengi”
- **S2** (gemma3:12b, risk_or_safety): The speaker's inability to work, following a statement about having many thoughts, may indicate a risk to their well-being or ability to function. — *The statement 'siwezi kufanya kazi' (I cannot work) expresses an inability to perform a basic function. While this may be a hyperbolic expression of distress, it could also indicate a more serious issue impacting the speaker's ability to function. It is important to assess the speaker's safety and well-being.* — evidence: utterance_span: “siwezi kufanya kazi”
- **S3** (qwen2.5:7b, overwhelmed): I have a lot on my mind, I can't work. — *The speaker is expressing a state of having too many thoughts to manage, which is preventing them from working.* — evidence: utterance_span: “Nina mawazo mengi, siwezi kufanya kazi.”
- **S4** (llama3.1:8b, overwhelmed): feeling overwhelmed by thoughts — *The speaker says 'mawazo mengi', which translates to 'a lot of thoughts' or 'many thoughts', indicating a sense of being overwhelmed.* — evidence: translation_candidate: “I have so many thoughts, I can't do my work”
- **S5** (llama3.1:8b, risk_or_safety): expressing inability to cope with work due to thoughts — *The speaker says 'siwezi kufanya kazi', which translates to 'I can't do my work', indicating a potential risk to their work or well-being.* — evidence: utterance_span: “siwezi kufanya kazi”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000027` terror [] — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000171` worry [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000168` concern []

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.225, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
