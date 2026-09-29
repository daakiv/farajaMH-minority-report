# Review card — QREC-DRY-009
Package `MRP-QREC-DRY-009-qrec-dryrun-v7` · priority **high** · backend `live`

## Step 1 — Your own reading first (blind pass)
**Utterance:** Always
**Expression:** Always
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Daima` (language sw)
- edit: `Always` → `Daima` (orthographic) Standard Swahili equivalent.

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Always | Always. | not run | This is a single word, 'daima'. Without context, it's impossible to determine its meaning or emotional significance. It could express a state of being, a feeling, or a response to a question. It could be an adverb meaning 'constantly' or 'forever'. |
| T2 | qwen2.5:7b | Daima | Always | not run |  |
| T3 | llama3.1:8b | Always my heart is not at peace | I'm always feeling restless and troubled | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **cognitive_process**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | restlessness | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C2 | persistence | cognitive_process | minority | gemma3:12b |
| C4 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, restlessness): The speaker is experiencing a persistent feeling of unease and agitation. — *The translation 'I'm always feeling restless and troubled' directly indicates a state of restlessness. This aligns with the clinician's inquiry about concentration, which can be affected by emotional distress.* — evidence: translation_candidate: “I'm always feeling restless and troubled”
- **S2** (gemma3:12b, persistence): The speaker is indicating that something has been happening continuously. — *The translation 'Always' suggests a continuous or repeated experience. This could refer to the feeling of restlessness or another issue the speaker is experiencing.* — evidence: translation_candidate: “Always”
- **S3** (gemma3:12b, risk_or_safety): The speaker may be expressing a desire to end a difficult situation, although this may be hyperbolic. — *The word 'always' can be used hyperbolically to express a desire for relief from a difficult situation, potentially implying a wish that the situation would end. While the phrasing may be idiomatic, it warrants consideration as a potential indicator of distress.* — evidence: translation_candidate: “Always”
- **S4** (qwen2.5:7b, always): The speaker is indicating a persistent state of feeling restless and troubled. — *The speaker is using the word 'Always' to describe a continuous state of feeling restless and troubled.* — evidence: utterance_span: “I'm always feeling restless and troubled”
- **S5** (llama3.1:8b, sadness): feeling persistently unhappy or sorrowful — *The speaker is responding to a question about problems they've been bothered by, which suggests they're describing their emotional state.* — evidence: conversation_turn: “how often have you been bothered by the following problems?”
- **S6** (llama3.1:8b, risk_or_safety): expressing a desire to exit the world or harm oneself — *The speaker's response to a question about problems they've been bothered by may be idiomatic, but it's essential to consider the possibility of a risk or safety concern.* — evidence: conversation_turn: “how often have you been bothered by the following problems?”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000111` feeling restless [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.733, 'translation_agreement': 0.5, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.959, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
