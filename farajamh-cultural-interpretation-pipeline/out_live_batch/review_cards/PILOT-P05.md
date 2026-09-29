# Review card — PILOT-P05
Package `MRP-PILOT-P05-batch-01` · priority **high** · backend `live`

## Step 1 — Your own reading first (blind pass)
**Utterance:** Nimelogwa, ndiyo maana siwezi kulala.
**Expression:** Nimelogwa
**Context:** KE/KE-coast, dialect Kimvita, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Nimegundua, ndiyo maana siwezi kulala.` (language sw)
- edit: `NimeLogwa` → `Nimegundua` (orthographic) Replacing 'Logwa' with 'Gundua' based on context and common usage. 'Logwa' is not a standard Swahili verb. 'Gundua' means 'to realize' or 'to discover'.

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I-have-realized, that is why I-cannot sleep. | I've realized something, that's why I can't sleep. | not run |  |
| T2 | qwen2.5:7b | I am sad, but the meaning cannot be understood. | I am sad, but you can't understand it. | not run | Uncertain |
| T3 | llama3.1:8b | I have discovered, it is true I cannot sleep | I've realized I'm too anxious to sleep | not run |  |

### How the models read it, by category (labels aside)
- **cognitive_process**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 2/3 models (gemma3:12b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **clinical_symptom**: 1/3 models (qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | realization | cognitive_process | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C2 | distress | emotional_state | minority | gemma3:12b |
| C4 | sleeplessness | clinical_symptom | minority | qwen2.5:7b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, realization): The speaker has come to a new understanding or awareness. — *The normalised utterance 'Nimegundua' directly translates to 'I've realized'. This indicates a cognitive process of understanding something new.* — evidence: utterance_span: “Nimegundua”
- **S2** (gemma3:12b, distress): The speaker is experiencing significant emotional discomfort. — *The phrase 'ndiyo maana siwezi kulala' (that's why I can't sleep) implies a negative consequence stemming from the realization, suggesting distress.* — evidence: utterance_span: “ndiyo maana siwezi kulala”
- **S3** (gemma3:12b, risk_or_safety): The speaker's inability to sleep, following a realization, may indicate a potential risk to their well-being, requiring further assessment. — *The speaker's inability to sleep following a realization, while potentially idiomatic, warrants consideration as a potential indicator of distress or a need for support. It is not possible to determine from the given information whether this is a literal statement of risk or an expression of distress.* — evidence: utterance_span: “siwezi kulala”
- **S4** (qwen2.5:7b, realization): I have realized something important. — *The speaker is using the verb 'gundua' which means 'realize' or 'understand', and the negation 'siwezi' (can't) is applied to 'kulala' (sleep), suggesting a realization about sleeplessness.* — evidence: utterance_span: “Nimegundua”
- **S5** (qwen2.5:7b, sleeplessness): I can't sleep. — *The speaker is directly stating that they cannot sleep, which is a common clinical symptom.* — evidence: utterance_span: “ndiyo maana siwezi kulala”
- **S6** (llama3.1:8b, realization): I have come to understand or know something. — *The word 'gundua' means 'to realize' or 'to discover', which suggests that the speaker has gained new insight or understanding.* — evidence: model_background_knowledge: “gundua (v) to realize, to discover”; utterance_span: “Nimegundua”
- **S7** (llama3.1:8b, risk_or_safety): The speaker may be at risk of harming themselves or others, or may be in a situation where they feel unsafe. — *The speaker says they 'can't sleep' because of what they've realized, which may indicate that they're experiencing distress or anxiety that's affecting their ability to rest.* — evidence: utterance_span: “ndiyo maana siwezi kulala”; model_background_knowledge: “Inability to sleep is often a symptom of emotional distress”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: `MFOEM:000031` crying []; `MFOEM:000052` compassion []; `MFOEM:000055` shame []; `MFOEM:000216` gloomy mood [llama3.1:8b→skos:relatedMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C4**: `MFOEM:000080` feeling tired [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, minority_clinical_reading, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 1 place(s): gemma3:12b/normalise edits.type="lexical" → orthographic
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.111, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.921, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
