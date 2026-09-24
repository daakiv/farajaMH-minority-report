# Review card — PILOT-P09
Package `MRP-PILOT-P09-pilot-dryrun` · priority **high** · backend `fixture_simulated`

> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Siku hizi sina mawazo mengi kama zamani.
**Expression:** sina mawazo mengi
**Context:** TZ/TZ-lake, dialect standard, speaker participant, setting hdss_survey, negation negated, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Siku hizi sina mawazo mengi kama zamani.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | sim-model-A | days these I-have-no thoughts many like before | These days I don't think too much like I used to. | Siku hizi siwazi sana kama zamani. (0.167) |  |
| T2 | sim-model-B | days these I-have-no thoughts many like past | Nowadays I don't have as much on my mind as before. | Siku hizi sina mambo mengi akilini kama zamani. (0.5) |  |
| T3 | sim-model-C | days these I-have-no worries many like before | These days I don't worry as much as I did. | Siku hizi sina wasiwasi mwingi kama zamani. (0.333) |  |

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | thinking too much | cognitive_process | majority | sim-model-A, sim-model-B |
| C2 | worry | emotional_state | minority | sim-model-C |

<details><summary>Rationale and evidence per model</summary>

- **S1** (sim-model-A, thinking too much): The 'thinking too much' idiom, reported as ABSENT or reduced now. — *Negated form; polarity must be kept.* — evidence: utterance_span: “sina mawazo mengi”; context_field: “negated”
- **S2** (sim-model-B, thinking too much): Reports improvement: no longer thinking too much. — *Negation plus 'kama zamani' implies improvement.* — evidence: utterance_span: “kama zamani”; context_field: “negated”
- **S3** (sim-model-C, worry): Worry reduced compared with before. — *Negated worry.* — evidence: utterance_span: “sina mawazo mengi”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `SCTID:LOOKUP-worrying` <lookup: worrying> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `SCTID:LOOKUP-rumination` <lookup: rumination> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C2**: `SCTID:LOOKUP-worrying` <lookup: worrying> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `MFOEM:LOOKUP-anxiety` <lookup: anxiety> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A

### Signals
- Risk flags: back_translation_mismatch, cultural_term_lost_in_back_translation, placeholder_ids_not_verified, polarity_negated, possible_semantic_gap, translation_divergence
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.733, 'translation_agreement': 0.287, 'back_translation_similarity_min': 0.167, 'top_cluster_support': 0.667, 'sense_entropy': 0.918, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
