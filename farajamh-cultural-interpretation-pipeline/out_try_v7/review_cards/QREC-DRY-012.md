# Review card — QREC-DRY-012
Package `MRP-QREC-DRY-012-qrec-dryrun-v7` · priority **high** · backend `live`

## Step 1 — Your own reading first (blind pass)
**Utterance:** Yes, I do feel like killing people who annoy me
**Expression:** Yes, I do feel like killing people who annoy me
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Ndio, naona kama ninaweza kuuwa watu wanaonichochea.` (language sw)
- edit: `Yes` → `Ndio` (code_switch_marked) English affirmation replaced with Swahili equivalent.
- edit: `I do feel like` → `ninaona kama` (orthographic) Expressing feeling.
- edit: `killing` → `kuuwa` (orthographic) Verb 'to kill' in Swahili.
- edit: `people` → `watu` (orthographic) Swahili word for 'people'
- edit: `who annoy me` → `wanaonichochea` (orthographic) People who provoke/annoy me.

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Yes, I see like I can kill people who provoke me. | Yes, I feel like I could kill the people who are provoking me. | not run | None |
| T2 | qwen2.5:7b | Today, I see that I could be one of those people who are suffering. | Today, I see that I could be one of those people who are suffering. | not run |  |
| T3 | llama3.1:8b | Yes, I see as if I can be people who are annoying me. | Yes, I feel like I'm at my wit's end with people who are driving me crazy. | not run |  |

### How the models read it, by category (labels aside)
- **risk_or_safety**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **emotional_state**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C1 | anger | emotional_state | majority | gemma3:12b, llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, anger): The speaker expresses intense frustration and a desire for retribution against those who irritate them. — *The phrase 'kuuwa watu wanaonichochea' (kill people who provoke me) indicates a strong emotional reaction, likely anger or intense frustration.* — evidence: utterance_span: “kuuwa watu wanaonichochea”
- **S2** (gemma3:12b, risk_or_safety): The speaker expresses a thought of harming others, which may indicate a potential risk to others and requires further assessment. — *The utterance explicitly mentions 'kuuwa' (kill), which constitutes risk language. Even if hyperbolic, the statement warrants careful consideration and assessment of potential harm.* — evidence: utterance_span: “kuuwa”
- **S3** (qwen2.5:7b, risk_or_safety): The speaker expresses thoughts of harming others, indicating a risk of violence. — *The speaker explicitly states a desire to kill people who annoy them, which is a direct expression of harmful intent.* — evidence: utterance_span: “Yes, I do feel like killing people who annoy me”
- **S4** (llama3.1:8b, anger): Feeling intense anger towards people who annoy me. — *The speaker uses the phrase 'kama ninaweza kuuwa' which implies a strong feeling of anger or frustration.* — evidence: utterance_span: “naona kama ninaweza kuuwa”
- **S5** (llama3.1:8b, risk_or_safety): The speaker has thoughts of harming others, which poses a risk to their safety and the safety of others. — *The speaker's statement directly references harming others, which indicates a risk to safety.* — evidence: utterance_span: “naona kama ninaweza kuuwa”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000009` anger [qwen2.5:7b→skos:broadMatch]; `MFOEM:000011` irritation []; `MFOEM:000012` annoyance []; `MFOEM:000013` fury [llama3.1:8b→skos:broadMatch]; `MFOEM:000014` rage []; `MFOEM:000018` contempt []; `MFOEM:000025` jealousy []; `MFOEM:000172` canonical angry facial expression [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.983, 'translation_agreement': 0.25, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.971, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
