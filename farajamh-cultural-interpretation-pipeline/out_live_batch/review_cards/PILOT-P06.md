# Review card — PILOT-P06
Package `MRP-PILOT-P06-batch-01` · priority **high** · backend `live`

## Step 1 — Your own reading first (blind pass)
**Utterance:** Niko na stress mob, siwezi lala.
**Expression:** Niko na stress mob
**Context:** KE/KE-nairobi, dialect Sheng, speaker participant, setting chat_platform, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Niko na stress mob, siwezi lala.` (language sw-x-sheng)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I have stress much, I cannot sleep. | I'm really stressed, I can't sleep. | not run | None |
| T2 | qwen2.5:7b | I have stress mob, cannot sleep. | I am stressed and cannot sleep. | not run |  |
| T3 | llama3.1:8b | I am with stress mob | I'm feeling overwhelmed and anxious all the time | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **somatic_experience**: 2/3 models (gemma3:12b, llama3.1:8b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **clinical_symptom**: 1/3 models (qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | stress | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C4 | sleep difficulty | clinical_symptom | majority | qwen2.5:7b, llama3.1:8b |
| C2 | sleeplessness | somatic_experience | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, stress): The speaker is experiencing a significant amount of stress. — *The phrase 'Niko na stress mob' directly indicates the presence of stress. 'Mob' intensifies the feeling.* — evidence: utterance_span: “Niko na stress mob”
- **S2** (gemma3:12b, sleeplessness): The speaker is unable to sleep. — *The phrase 'siwezi lala' directly translates to 'I cannot sleep'.* — evidence: utterance_span: “siwezi lala”
- **S3** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially hyperbolic, expresses a desire to avoid a current state and may indicate underlying distress warranting further assessment. — *The combination of stress and sleeplessness, even if expressed idiomatically, suggests a level of distress that could be indicative of a need for support or intervention. The phrasing may be hyperbolic, but the expression of inability to sleep and feeling overwhelmed requires consideration for potential risk.* — evidence: utterance_span: “Niko na stress mob, siwezi lala”
- **S4** (qwen2.5:7b, stress): The speaker is feeling stressed and overwhelmed. — *The speaker is directly stating their current state of feeling stressed and overwhelmed.* — evidence: utterance_span: “Niko na stress mob”
- **S5** (qwen2.5:7b, sleep difficulty): The speaker is having trouble sleeping due to stress. — *The speaker is stating they cannot sleep, which is a common symptom of stress.* — evidence: utterance_span: “siwezi lala”
- **S6** (llama3.1:8b, stress): feeling overwhelmed and anxious — *The speaker affirms the presence of stress, indicating a current emotional state.* — evidence: utterance_span: “Niko na stress mob”
- **S7** (llama3.1:8b, sleep difficulty): inability to sleep — *The speaker explicitly states that they cannot sleep, indicating a somatic experience.* — evidence: utterance_span: “siwezi lala”
- **S8** (llama3.1:8b, risk_or_safety): potential harm to self due to stress — *The speaker's stress and inability to sleep may indicate a risk to their safety or well-being.* — evidence: model_background_knowledge: “”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000029` stress (emotion) [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.208, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.953, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
