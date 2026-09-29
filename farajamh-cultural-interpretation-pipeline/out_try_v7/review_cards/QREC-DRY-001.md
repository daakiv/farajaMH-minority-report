# Review card — QREC-DRY-001
Package `MRP-QREC-DRY-001-qrec-dryrun-v7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/gloss* — ……at warrants consideration for potential self-harm or harm to others.…
> - `self-harm` in *gap_note/C2* — ……at warrants consideration for potential self-harm or harm to others. | concepts would nee……
> - `nife` in *gap_note/C3* — ……retrieved concepts focus on specific manifestations of sadness (facial expression,……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Not good at all
**Expression:** Not good at all
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Si nzuri kabisa.` (language sw)
- edit: `Not` → `Si` (asr_correction) Common Swahili negation
- edit: `good` → `nzuri` (asr_correction) Standard Swahili for 'good'
- edit: `at all` → `kabisa` (asr_correction) Standard Swahili for 'completely' or 'at all'

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Not good completely. | I'm not doing well at all. | not run | The phrase 'Si nzuri kabisa' is a common expression of general distress or discomfort. It doesn't necessarily imply a specific emotional state, but indicates a feeling of being unwell or not okay. |
| T2 | qwen2.5:7b | I am not good at all. | I am not doing well at all. | not run |  |
| T3 | llama3.1:8b | Not good at all | I'm not doing well at all | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | discomfort | emotional_state | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, discomfort): The speaker is expressing a general feeling of unease or dissatisfaction. — *The phrase 'Not good at all' directly indicates a negative assessment of the speaker's current state. The translations provided support this interpretation as a general feeling of not doing well.* — evidence: utterance_span: “Not good at all”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a level of distress that warrants consideration for potential self-harm or harm to others. — *The phrase 'Not good at all' could be a hyperbolic expression of severe distress. It is crucial to consider the possibility of underlying risk factors, even if the phrasing appears casual. The context of a simulated patient interaction further necessitates a cautious approach.* — evidence: utterance_span: “Not good at all”
- **S3** (qwen2.5:7b, sadness): Expressing a state of feeling unhappy or displeased. — *The phrase 'Not good at all' directly conveys a negative emotional state.* — evidence: utterance_span: “Si nzuri kabisa.”
- **S4** (llama3.1:8b, sadness): Feeling unhappy or unwell. — *The word 'nzuri' typically means 'good', but in this context, it's negated, suggesting a negative emotional state.* — evidence: utterance_span: “Si nzuri kabisa”
- **S5** (llama3.1:8b, risk_or_safety): Expressing a desire to exit or leave the current situation. — *The phrase 'not good at all' may be idiomatic, but it could also be interpreted as a statement of intent to leave or exit the current situation.* — evidence: utterance_span: “Not good at all”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance [] — **no adequate match** per gemma3:12b
- **C1**: `MFOEM:000122` experiencing discomfort in the stomach []; `MFOEM:000164` panic []; `MFOEM:000205` feeling of hunger []; `MFOEM:000206` feeling of thirst []; `MFOEM:000222` feeling of need [llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.983, 'translation_agreement': 0.833, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
