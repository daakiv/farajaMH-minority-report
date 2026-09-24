# Review card — PILOT-P05
Package `MRP-PILOT-P05-pilot-dryrun` · priority **high** · backend `fixture_simulated`

> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Nimelogwa, ndiyo maana siwezi kulala.
**Expression:** Nimelogwa
**Context:** KE/KE-coast, dialect Kimvita, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Nimerogwa, ndiyo maana siwezi kulala.` (language sw)
- edit: `Nimelogwa` → `Nimerogwa` (phonological_variant) l/r alternation (-loga / -roga). DRAFT: linguist to confirm which form FarajaMH treats as standard.

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | sim-model-A | I-have-been-bewitched, that-is why I-cannot sleep | I have been bewitched; that is why I can't sleep. | Nimerogwa; ndiyo sababu siwezi kulala. (0.6) |  |
| T2 | sim-model-B | I-have-been-bewitched, that-is reason I-cannot sleep | I've been bewitched, that's why I cannot sleep. | Nimerogwa, ndiyo maana siwezi kulala. (1.0) |  |
| T3 | sim-model-C | I-have-been-cursed, therefore I-cannot sleep | I've been cursed, that's why I can't sleep. | Nimelaaniwa, ndiyo maana siwezi kulala. (0.6) |  |

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | bewitchment explanation | spiritual_or_supernatural | unanimous | sim-model-A, sim-model-B, sim-model-C |
| C2 | sleep difficulty | somatic_experience | minority | sim-model-A |
| C3 | interpersonal conflict | social_or_relational | minority | sim-model-B |
| C4 | persecutory belief | clinical_symptom | minority | sim-model-C |

<details><summary>Rationale and evidence per model</summary>

- **S1** (sim-model-A, bewitchment explanation): The speaker attributes their problem to witchcraft; a culturally shared explanation of misfortune. — *Explanatory model, not in itself a symptom.* — evidence: utterance_span: “Nimelogwa”
- **S2** (sim-model-A, sleep difficulty): Difficulty sleeping. — *Second clause.* — evidence: utterance_span: “siwezi kulala”
- **S3** (sim-model-B, bewitchment explanation): Attributing distress to bewitchment. — *Culturally normative explanation.* — evidence: utterance_span: “Nimelogwa”
- **S4** (sim-model-B, interpersonal conflict): Witchcraft accusations can signal conflict or suspicion within family or community. — *Common social meaning of bewitchment talk.* — evidence: model_background_knowledge: “”
- **S5** (sim-model-C, bewitchment explanation): Belief in being bewitched. — *Direct reading.* — evidence: utterance_span: “Nimelogwa”
- **S6** (sim-model-C, persecutory belief): A belief of being harmed by others that could be clinically relevant if fixed and out of keeping with local norms. — *Include for clinician check only; culturally shared beliefs are not delusions.* — evidence: utterance_span: “Nimelogwa”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: none retrieved — **no adequate match** per sim-model-A, sim-model-B, sim-model-C
- **C2**: `SCTID:LOOKUP-difficulty-sleeping` <lookup: difficulty sleeping> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]
- **C3**: `SCTID:LOOKUP-interpersonal-relationship-problem` <lookup: interpersonal relationship problem> [sim-model-B→skos:relatedMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C4**: `SCTID:LOOKUP-persecutory-delusion` <lookup: persecutory delusion> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]

### Signals
- Risk flags: minority_clinical_reading, over_medicalisation_risk, placeholder_ids_not_verified, possible_semantic_gap, register_divergence_clinical_vs_everyday
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.817, 'translation_agreement': 0.533, 'back_translation_similarity_min': 0.6, 'top_cluster_support': 1.0, 'sense_entropy': 0.896, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
