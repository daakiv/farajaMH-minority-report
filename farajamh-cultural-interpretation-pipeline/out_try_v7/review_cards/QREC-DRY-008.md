# Review card — QREC-DRY-008
Package `MRP-QREC-DRY-008-qrec-dryrun-v7` · priority **high** · backend `live`

## Step 1 — Your own reading first (blind pass)
**Utterance:** I have had trouble concentrating on things such as reading news papers or watching TV
**Expression:** I have had trouble concentrating on things such as reading news papers or watching TV
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Mimi nimekuwa na matatizo ya kuzingatia mambo kama kusoma magazeti au kutazama runinga.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I have been with troubles of to concentrate things like reading newspapers or watching television. | I've been having trouble concentrating on things like reading newspapers or watching television. | not run |  |
| T2 | qwen2.5:7b | I am having a sadness like when reading newspapers or watching videos. | I am feeling sad when I read newspapers or watch videos. | not run |  |
| T3 | llama3.1:8b | I have been having troubles of thinking about things like reading newspapers or watching TV. | I've been having a lot on my mind, and even simple things like reading the news or watching TV are a struggle. | not run |  |

### How the models read it, by category (labels aside)
- **cognitive_process**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | difficulty concentrating | cognitive_process | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, difficulty concentrating): The speaker is experiencing difficulty focusing on tasks like reading or watching television. — *The phrase 'matatizo ya kuzingatia' directly translates to 'trouble concentrating,' and the examples provided (reading newspapers, watching television) illustrate the types of activities affected.* — evidence: utterance_span: “Mimi nimekuwa na matatizo ya kuzingatia mambo kama kusoma magazeti au kutazama runinga.”
- **S2** (gemma3:12b, risk_or_safety): The speaker's difficulty concentrating, while potentially idiomatic or hyperbolic, may indicate underlying distress or a desire to avoid engagement with the world. — *The speaker's report of difficulty concentrating, while seemingly a description of a cognitive function, could be a veiled expression of a deeper issue. It may be a way of expressing a desire to withdraw or avoid responsibility, or a symptom of a more serious condition. The phrasing may be idiomatic or hyperbolic.* — evidence: utterance_span: “Mimi nimekuwa na matatizo ya kuzingatia mambo kama kusoma magazeti au kutazama runinga.”
- **S3** (qwen2.5:7b, concentration_difficulty): Difficulty in focusing on tasks such as reading newspapers or watching TV. — *The speaker explicitly mentions trouble concentrating on reading newspapers or watching TV.* — evidence: utterance_span: “Mimi nimekuwa na matatizo ya kuzingatia mambo kama kusoma magazeti au kutazama runinga.”
- **S4** (llama3.1:8b, concentration difficulty): Having trouble focusing one's attention — *The speaker mentions 'matatizo ya kuzingatia mambo', which translates to 'trouble concentrating on things'.* — evidence: utterance_span: “Mimi nimekuwa na matatizo ya kuzingatia mambo”
- **S5** (llama3.1:8b, risk_or_safety): Potential for harm or injury due to concentration difficulties — *The speaker mentions trouble concentrating, which may lead to accidents or injuries, such as while reading or watching TV.* — evidence: utterance_span: “Mimi nimekuwa na matatizo ya kuzingatia mambo”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.14, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.971, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
