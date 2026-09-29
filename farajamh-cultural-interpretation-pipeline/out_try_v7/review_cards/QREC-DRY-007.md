# Review card — QREC-DRY-007
Package `MRP-QREC-DRY-007-qrec-dryrun-v7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `leave the world` in *sense/S5/rationale* — ……be an expression of a desire to exit or leave the world, which could be a risk or threat to the……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** My energy has really gone down
**Expression:** My energy has really gone down
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Nguvu yangu imeshuka sana.` (language sw)
- edit: `My energy has really gone down` → `Nguvu yangu imeshuka sana.` (orthographic) Replaced English phrase with standard Swahili equivalent.
- edit: `My` → `Nguvu` (orthographic) Replaced 'My' with 'Nguvu' (strength/energy).
- edit: `energy` → `yangu` (orthographic) Replaced 'energy' with 'yangu' (my).
- edit: `has really gone down` → `imeshuka sana` (orthographic) Replaced 'has really gone down' with 'imeshuka sana' (has decreased a lot).

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | strength my has gone down very much. | My strength has really diminished. | not run |  |
| T2 | qwen2.5:7b | Strength my is seeing much. | I am feeling very weak. | not run |  |
| T3 | llama3.1:8b | My strength has fallen very much. | I feel drained and exhausted. | not run |  |

### How the models read it, by category (labels aside)
- **somatic_experience**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | weakness | somatic_experience | majority | gemma3:12b, qwen2.5:7b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | energy_low | somatic_experience | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, weakness): The speaker is experiencing a significant reduction in their physical or mental strength. — *The phrase 'Nguvu yangu imeshuka sana' directly translates to 'My strength has really diminished,' indicating a feeling of weakness or lack of power.* — evidence: utterance_span: “Nguvu yangu imeshuka sana.”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a significant decline in energy that could be indicative of underlying health concerns or a desire to withdraw from activities. — *The speaker reports a significant decrease in energy ('imeshuka sana'), which, while potentially hyperbolic, warrants consideration as a potential indicator of underlying distress or a reluctance to engage in daily life. The context of a simulated patient interaction with a clinician further emphasizes the need to assess for potential risk.* — evidence: utterance_span: “Nguvu yangu imeshuka sana.”
- **S3** (qwen2.5:7b, weakness): The speaker feels a significant decrease in their physical strength. — *The speaker directly states a decrease in their strength.* — evidence: utterance_span: “My strength has really diminished.”
- **S4** (llama3.1:8b, energy_low): Having a reduced amount of physical or mental energy. — *The word 'nguvu' means 'strength' or 'energy', and the verb 'imeshuka' means 'has decreased'. The speaker is describing a physical or mental state.* — evidence: utterance_span: “Nguvu yangu imeshuka sana.”
- **S5** (llama3.1:8b, risk_or_safety): Expressing a potential risk or threat to one's physical or mental well-being. — *The speaker's statement may be an expression of a desire to exit or leave the world, which could be a risk or threat to their safety.* — evidence: utterance_span: “Nguvu yangu imeshuka sana.”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000119` feeling weak [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000115` limb weakening []; `MFOEM:000006` subjective affective feeling []
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.0, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
