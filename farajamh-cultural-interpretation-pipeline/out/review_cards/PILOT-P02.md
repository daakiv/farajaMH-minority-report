# Review card — PILOT-P02
Package `MRP-PILOT-P02-pilot-dryrun` · priority **high** · backend `fixture_simulated`

> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Moyo wangu ni mzito kila asubuhi.
**Expression:** Moyo wangu ni mzito
**Context:** KE/KE-western, dialect standard, speaker participant, setting clinic, negation affirmed, temporality recurrent, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Moyo wangu ni mzito kila asubuhi.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | sim-model-A | heart my is heavy every morning | Every morning my heart feels heavy. | Kila asubuhi moyo wangu unakuwa mzito. (0.833) |  |
| T2 | sim-model-B | heart my is heavy each morning | Every morning I feel heavy-hearted. | Kila asubuhi najisikia moyo mzito. (0.667) |  |
| T3 | sim-model-C | heart my is heavy every morning | My heart is heavy every morning. | Moyo wangu ni mzito kila asubuhi. (1.0) |  |

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | sim-model-A, sim-model-B, sim-model-C |
| C2 | morning reluctance | emotional_state | minority | sim-model-B |
| C3 | chest heaviness | clinical_symptom | minority | sim-model-C |

<details><summary>Rationale and evidence per model</summary>

- **S1** (sim-model-A, sadness): Sadness or sorrow, felt as heaviness of the heart. — *Common idiom of sorrow.* — evidence: utterance_span: “Moyo wangu ni mzito”
- **S2** (sim-model-B, sadness): Low, sorrowful mood. — *Heaviness of heart = sorrow.* — evidence: utterance_span: “Moyo wangu ni mzito”
- **S3** (sim-model-B, morning reluctance): Dread or reluctance on waking to face the day. — *'Kila asubuhi' points to a morning pattern.* — evidence: utterance_span: “kila asubuhi”
- **S4** (sim-model-C, sadness): Sad mood. — *Idiom of sorrow.* — evidence: utterance_span: “Moyo wangu ni mzito”
- **S5** (sim-model-C, chest heaviness): A physical sensation of heaviness in the chest. — *A literal reading of 'moyo' as the chest; include for clinician check.* — evidence: utterance_span: “Moyo”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `SCTID:LOOKUP-feeling-sad` <lookup: feeling sad> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `MFOEM:LOOKUP-sadness` <lookup: sadness> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C2**: none retrieved — **no adequate match** per sim-model-A, sim-model-B, sim-model-C
- **C3**: `SCTID:LOOKUP-chest-heaviness` <lookup: chest heaviness> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]

### Signals
- Risk flags: minority_clinical_reading, over_medicalisation_risk, placeholder_ids_not_verified, possible_semantic_gap, register_divergence_clinical_vs_everyday
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.817, 'translation_agreement': 0.633, 'back_translation_similarity_min': 0.667, 'top_cluster_support': 1.0, 'sense_entropy': 0.865, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
