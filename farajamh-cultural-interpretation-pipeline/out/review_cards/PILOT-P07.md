# Review card — PILOT-P07
Package `MRP-PILOT-P07-pilot-dryrun` · priority **high** · backend `fixture_simulated`

> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.

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
| T1 | sim-model-A | I-have-no joy days these | I have no joy these days. | Sina furaha siku hizi. (0.333) |  |
| T2 | sim-model-B | I-have-no happiness days these | I am not happy these days. | Sina furaha siku hizi. (0.333) |  |
| T3 | sim-model-C | I-have-no peace days these | I have no peace these days. | Sina amani siku hizi. (0.333) |  |

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | low mood | emotional_state | majority | sim-model-A, sim-model-B |
| C2 | loss of pleasure | clinical_symptom | minority | sim-model-B |
| C3 | lack of peace | emotional_state | minority | sim-model-C |

<details><summary>Rationale and evidence per model</summary>

- **S1** (sim-model-A, low mood): Persistently low or unhappy mood. — *Common way to report unhappiness.* — evidence: utterance_span: “Sina raha”
- **S2** (sim-model-B, loss of pleasure): Not finding pleasure in things. — *Could indicate anhedonia.* — evidence: utterance_span: “Sina raha”
- **S3** (sim-model-B, low mood): Feeling unhappy. — *Plain reading.* — evidence: utterance_span: “Sina raha”
- **S4** (sim-model-C, lack of peace): No inner peace or ease; feeling unsettled. — *Raha as ease/peace.* — evidence: utterance_span: “raha”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `SCTID:LOOKUP-low-mood` <lookup: low mood> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `MFOEM:LOOKUP-sadness` <lookup: sadness> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C2**: `SCTID:LOOKUP-anhedonia` <lookup: anhedonia> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]
- **C3**: `SCTID:LOOKUP-feeling-restless` <lookup: feeling restless> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A

### Signals
- Risk flags: cultural_term_lost_in_back_translation, minority_clinical_reading, over_medicalisation_risk, placeholder_ids_not_verified, possible_semantic_gap, register_divergence_clinical_vs_everyday, translation_divergence
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.733, 'translation_agreement': 0.333, 'back_translation_similarity_min': 0.333, 'top_cluster_support': 0.667, 'sense_entropy': 0.946, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
