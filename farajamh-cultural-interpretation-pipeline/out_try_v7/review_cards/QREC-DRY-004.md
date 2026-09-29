# Review card — QREC-DRY-004
Package `MRP-QREC-DRY-004-qrec-dryrun-v7` · priority **high** · backend `live`

## Step 1 — Your own reading first (blind pass)
**Utterance:** They have made me not do my work, and unable to take care of things at home, also I cant get along with people
**Expression:** They have made me not do my work, and unable to take care of things at home, also I cant get along with people
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Walinifanya nisiweze kufanya kazi yangu, na pia nisiongee kuangalia mambo nyumbani, pia sielewi na watu.` (language sw)
- edit: `They have made me not do my work` → `Walinifanya nisiweze kufanya kazi yangu` (orthographic) Standard Swahili construction for 'They made me not do my work'
- edit: `and unable to take care of things at home` → `na pia nisiongee kuangalia mambo nyumbani` (orthographic) Standard Swahili construction for 'and unable to take care of things at home'
- edit: `also I cant get along with people` → `pia sielewi na watu` (orthographic) Standard Swahili construction for 'also I cant get along with people'

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | They-me-to-make I-not-be-able to-do work my, and also they-me-to-prevent to-look things home, also I-understand-not with people. | They've made it so I can't do my work, and they've also prevented me from being able to deal with things at home, and I can't get along with people. | not run |  |
| T2 | qwen2.5:7b | I can't do my work, and also I don't want to look at things at home, also I feel sad and people. | I can't do my work, and also I don't want to look at things at home, also I feel sad and people. | not run |  |
| T3 | llama3.1:8b | They made me not be able to do my work, and also I am confused to look at home affairs, also I do not understand people. | They've made it impossible for me to work, and I'm also struggling to cope with family problems, and I'm finding it hard to understand people. | not run | The expression 'nisiongee kuangalia mambo nyumbani' is idiomatic in Swahili, and it's not clear what exactly the speaker means by 'confused to look at home affairs'. It could be related to family problems, financial issues, or other personal matters. |

### How the models read it, by category (labels aside)
- **emotional_state**: 2/3 models (gemma3:12b, llama3.1:8b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **social_or_relational**: 2/3 models (llama3.1:8b, qwen2.5:7b)
- **somatic_experience**: 1/3 models (qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | overwhelmed | emotional_state | minority | gemma3:12b |
| C3 | work_difficulty | somatic_experience | minority | qwen2.5:7b |
| C4 | social_isolation | social_or_relational | minority | qwen2.5:7b |
| C5 | emotional_state | emotional_state | minority | llama3.1:8b |
| C6 | social_or_relational | social_or_relational | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, overwhelmed): The speaker feels unable to manage their responsibilities and relationships. — *The speaker explicitly states they are 'unable to take care of things at home' and 'can't get along with people,' indicating a sense of being overwhelmed by their circumstances.* — evidence: utterance_span: “Walinifanya nisiweze kufanya kazi yangu, na pia nisiongee kuangalia mambo nyumbani, pia sielewi na watu.”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially hyperbolic, expresses a significant inability to function and may indicate distress warranting further assessment. — *The phrasing 'unable to take care of things at home' and 'can't get along with people' could be a hyperbolic expression of distress, but it also indicates a significant disruption in the speaker's ability to function and may require further investigation to assess for potential harm or self-neglect. The phrasing may be idiomatic.* — evidence: utterance_span: “Walinifanya nisiweze kufanya kazi yangu, na pia nisiongee kuangalia mambo nyumbani, pia sielewi na watu.”
- **S3** (qwen2.5:7b, work_difficulty): Experiencing difficulty in performing work and household tasks. — *The speaker mentions being unable to do work and take care of things at home, indicating a practical difficulty in daily activities.* — evidence: utterance_span: “They've made it so I can't do my work, and they've also prevented me from being able to deal with things at home”
- **S4** (qwen2.5:7b, social_isolation): Struggling to interact with others and maintain social relationships. — *The speaker states they can't get along with people, indicating social difficulties.* — evidence: utterance_span: “and I can't get along with people”
- **S5** (llama3.1:8b, emotional_state): Feeling overwhelmed and unable to cope with daily responsibilities. — *The speaker mentions being unable to do their work and take care of things at home, which suggests a sense of overwhelm and inability to cope.* — evidence: utterance_span: “Walinifanya nisiweze kufanya kazi yangu, na pia nisiongee kuangalia mambo nyumbani”
- **S6** (llama3.1:8b, social_or_relational): Difficulty getting along with people due to external factors. — *The speaker mentions not being able to get along with people, which suggests a difficulty in social relationships.* — evidence: utterance_span: “pia sielewi na watu”
- **S7** (llama3.1:8b, risk_or_safety): Potential harm or injury to oneself due to external pressures. — *The speaker mentions being unable to do their work and take care of things at home, which may indicate a risk of harm or injury to themselves.* — evidence: utterance_span: “Walinifanya nisiweze kufanya kazi yangu, na pia nisiongee kuangalia mambo nyumbani”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000027` terror [llama3.1:8b→skos:relatedMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C5**: `MFOEM:000043` serenity [] — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C6**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.883, 'translation_agreement': 0.224, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.976, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
