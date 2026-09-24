# Review card — PILOT-P06
Package `MRP-PILOT-P06-pilot-dryrun` · priority **high** · backend `fixture_simulated`

> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Niko na stress mob, siwezi lala.
**Expression:** Niko na stress mob
**Context:** KE/KE-nairobi, dialect Sheng, speaker participant, setting chat_platform, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Niko na stress mob, siwezi kulala.` (language sw-x-sheng)
- edit: `stress` → `stress` (code_switch_marked) English loanword kept.
- edit: `mob` → `mob` (code_switch_marked) Sheng intensifier ('a lot'); kept.
- edit: `siwezi lala` → `siwezi kulala` (sheng_lexical) Colloquial infinitive without ku-.

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | sim-model-A | I-am with stress a-lot, I-cannot sleep | I'm really stressed, I can't sleep. | Niko na stress sana, siwezi kulala. (0.667) |  |
| T2 | sim-model-B | I-am with stress much, I-cannot sleep | I'm very stressed and can't sleep. | Nina msongo mkubwa na siwezi kulala. (0.25) |  |
| T3 | sim-model-C | I-am with stress lots, I-cannot sleep | I'm so stressed, I can't sleep. | Nina stress sana, siwezi kulala. (0.429) |  |

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | stress | emotional_state | unanimous | sim-model-A, sim-model-B, sim-model-C |
| C2 | sleep difficulty | somatic_experience | unanimous | sim-model-A, sim-model-B, sim-model-C |

<details><summary>Rationale and evidence per model</summary>

- **S1** (sim-model-A, stress): Feeling under heavy pressure or strain. — *Loanword used as in everyday Kenyan speech.* — evidence: utterance_span: “stress mob”
- **S2** (sim-model-A, sleep difficulty): Difficulty sleeping. — *Second clause.* — evidence: utterance_span: “siwezi lala”
- **S3** (sim-model-B, stress): Feeling under heavy pressure or strain. — *Loanword used as in everyday Kenyan speech.* — evidence: utterance_span: “stress mob”
- **S4** (sim-model-B, sleep difficulty): Difficulty sleeping. — *Second clause.* — evidence: utterance_span: “siwezi lala”
- **S5** (sim-model-C, stress): Feeling under heavy pressure or strain. — *Loanword used as in everyday Kenyan speech.* — evidence: utterance_span: “stress mob”
- **S6** (sim-model-C, sleep difficulty): Difficulty sleeping. — *Second clause.* — evidence: utterance_span: “siwezi lala”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `SCTID:LOOKUP-feeling-stressed` <lookup: feeling stressed> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `MFOEM:LOOKUP-stress-related-emotion` <lookup: stress-related emotion> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]
- **C2**: `SCTID:LOOKUP-difficulty-sleeping` <lookup: difficulty sleeping> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]

### Signals
- Risk flags: cultural_term_lost_in_back_translation, full_agreement_audit_candidate, multiple_components_in_utterance, placeholder_ids_not_verified
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.85, 'translation_agreement': 0.7, 'back_translation_similarity_min': 0.25, 'top_cluster_support': 1.0, 'sense_entropy': 1.0, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
