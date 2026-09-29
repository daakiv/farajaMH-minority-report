# Review card — PILOT-P07
Package `MRP-PILOT-P07-batch-01` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/rationale* — ……assess whether this reflects a risk of self-harm or other harmful actions, even if the p……
> - `nife` in *gap_note/C3* — ……retrieved concepts focus on specific manifestations of sadness (facial expression a……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Sina raha siku hizi.
**Expression:** Sina raha
**Context:** TZ/TZ-lake, dialect standard, speaker participant, setting clinic, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Sina raha siku hizi.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I pleasure not these days. | I'm not enjoying things these days. | not run | None |
| T2 | qwen2.5:7b | I do not have peace | I am not at peace | not run |  |
| T3 | llama3.1:8b | I have happiness not | I'm feeling unhappy these days | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | unhappiness | emotional_state | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, unhappiness): The speaker is expressing a general feeling of unhappiness or discontent. — *The phrase 'Sina raha' directly translates to 'I have no enjoyment/peace,' which is indicative of unhappiness. The affirmed negation strengthens this interpretation.* — evidence: utterance_span: “Sina raha”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a desire to escape a difficult situation, and requires assessment for risk. — *The expression conveys a lack of enjoyment and peace, which, while potentially hyperbolic, could indicate a desire to escape a situation. It is crucial to assess whether this reflects a risk of self-harm or other harmful actions, even if the phrasing is not a literal statement of intent.* — evidence: utterance_span: “Sina raha”
- **S3** (qwen2.5:7b, sadness): I am not enjoying things these days. — *The speaker is using a negation to express a current state of not enjoying things, which aligns with the proposed translation.* — evidence: utterance_span: “Sina raha siku hizi.”
- **S4** (llama3.1:8b, sadness): feeling unhappy or unfulfilled — *The speaker uses the word 'sina' (not) and 'raha' (peace/enjoyment) to express a negative emotional state.* — evidence: utterance_span: “Sina raha”
- **S5** (llama3.1:8b, risk_or_safety): expressing a desire to escape or leave the current situation — *The speaker's statement may be idiomatic, but it contains language related to not having enjoyment, which could be interpreted as a desire to leave or escape the current situation.* — evidence: utterance_span: “Sina raha”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance [] — **no adequate match** per gemma3:12b
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.133, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
