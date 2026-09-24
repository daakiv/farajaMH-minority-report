# Review card — PILOT-P03
Package `MRP-PILOT-P03-pilot-dryrun` · priority **high** · backend `fixture_simulated`

> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Nina mawazo mengi, siwezi kufanya kazi.
**Expression:** Nina mawazo mengi
**Context:** TZ/TZ-lake, dialect standard, speaker participant, setting hdss_survey, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Nina mawazo mengi, siwezi kufanya kazi.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | sim-model-A | I-have thoughts many, I-cannot do work | I am thinking too much; I can't work. | Nawaza sana; siwezi kufanya kazi. (0.375) |  |
| T2 | sim-model-B | I-have thoughts many, I-cannot do work | I have a lot on my mind, I can't work. | Nina mambo mengi akilini, siwezi kufanya kazi. (0.625) |  |
| T3 | sim-model-C | I-have worries many, I-cannot work | I am worrying a lot and cannot work. | Nina wasiwasi mwingi na siwezi kufanya kazi. (0.5) | Rendered 'mawazo' as worries. |

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | thinking too much | cognitive_process | majority | sim-model-A, sim-model-B |
| C2 | worry | emotional_state | majority | sim-model-A, sim-model-C |
| C3 | life stressors | social_or_relational | minority | sim-model-B |
| C4 | rumination | clinical_symptom | minority | sim-model-C |
| C5 | functional impairment | clinical_symptom | minority | sim-model-C |

<details><summary>Rationale and evidence per model</summary>

- **S1** (sim-model-A, thinking too much): The 'thinking too much' idiom of distress: persistent troubling thoughts, often about life problems. — *'Mawazo mengi' is a widely reported East African idiom of distress.* — evidence: utterance_span: “mawazo mengi”; model_background_knowledge: “”
- **S2** (sim-model-A, worry): Worry about problems. — *Overlaps with worry.* — evidence: utterance_span: “mawazo”
- **S3** (sim-model-B, thinking too much): Thinking too much about one's problems. — *Standard reading of the idiom.* — evidence: utterance_span: “Nina mawazo mengi”
- **S4** (sim-model-B, life stressors): Preoccupation with social or economic problems (money, family, work). — *The idiom often refers to concrete hardship.* — evidence: utterance_span: “siwezi kufanya kazi”; model_background_knowledge: “”
- **S5** (sim-model-C, worry): Excessive worry. — *Mawazo as worries.* — evidence: utterance_span: “mawazo mengi”
- **S6** (sim-model-C, rumination): Repetitive negative thinking. — *Could correspond to rumination.* — evidence: utterance_span: “mawazo mengi”
- **S7** (sim-model-C, functional impairment): Unable to work because of the thoughts. — *Second clause reports impact on work.* — evidence: utterance_span: “siwezi kufanya kazi”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `SCTID:LOOKUP-worrying` <lookup: worrying> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `SCTID:LOOKUP-rumination` <lookup: rumination> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C2**: `SCTID:LOOKUP-worrying` <lookup: worrying> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `MFOEM:LOOKUP-anxiety` <lookup: anxiety> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C3**: none retrieved — **no adequate match** per sim-model-A, sim-model-B, sim-model-C
- **C4**: `SCTID:LOOKUP-rumination` <lookup: rumination> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]
- **C5**: `SCTID:LOOKUP-difficulty-performing-work` <lookup: difficulty performing work> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]

### Signals
- Risk flags: cultural_term_lost_in_back_translation, minority_clinical_reading, over_medicalisation_risk, placeholder_ids_not_verified, possible_semantic_gap, register_divergence_clinical_vs_everyday, sense_divergence, translation_divergence
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.733, 'translation_agreement': 0.278, 'back_translation_similarity_min': 0.375, 'top_cluster_support': 0.667, 'sense_entropy': 0.963, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
