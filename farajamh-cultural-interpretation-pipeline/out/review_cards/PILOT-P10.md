# Review card — PILOT-P10
Package `MRP-PILOT-P10-pilot-dryrun` · priority **high** · backend `fixture_simulated`

> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Mama yangu hana raha tangu baba afariki.
**Expression:** hana raha
**Context:** KE/KE-coast, dialect standard, speaker family_member, setting home_visit, negation affirmed, temporality current, experiencer family_member

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Mama yangu hana raha tangu baba afariki.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | sim-model-A | mother my she-has-no joy since father died | My mother has had no joy since father died. | Mama yangu hana furaha tangu baba afariki. (0.714) |  |
| T2 | sim-model-B | mother my has-no happiness since father passed | My mother has been unhappy since my father passed away. | Mama yangu hana furaha tangu baba yangu afariki dunia. (0.625) |  |
| T3 | sim-model-C | mother my has-no peace since father died | My mother has had no peace since father died. | Mama yangu hana amani tangu baba afariki. (0.714) |  |

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | grief | emotional_state | majority | sim-model-B, sim-model-C |
| C1 | low mood | emotional_state | minority | sim-model-A |
| C3 | lack of peace | emotional_state | minority | sim-model-C |

<details><summary>Rationale and evidence per model</summary>

- **S1** (sim-model-A, low mood): The MOTHER (not the speaker) has been unhappy. — *Experiencer is the mother.* — evidence: utterance_span: “Mama yangu hana raha”; context_field: “family_member”
- **S2** (sim-model-B, grief): The mother's grief after her husband's death. — *Onset is the death.* — evidence: utterance_span: “tangu baba afariki”; context_field: “family_member”
- **S3** (sim-model-C, grief): Bereavement reaction in the mother. — *Onset tied to death.* — evidence: utterance_span: “tangu baba afariki”
- **S4** (sim-model-C, lack of peace): The mother is unsettled, without peace. — *Raha as peace.* — evidence: utterance_span: “hana raha”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: `SCTID:LOOKUP-grief` <lookup: grief> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `SCTID:LOOKUP-bereavement-finding` <lookup: bereavement finding> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `MFOEM:LOOKUP-grief-related-emotion` <lookup: grief-related emotion> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C1**: `SCTID:LOOKUP-low-mood` <lookup: low mood> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `MFOEM:LOOKUP-sadness` <lookup: sadness> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C3**: `SCTID:LOOKUP-feeling-restless` <lookup: feeling restless> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A

### Signals
- Risk flags: experiencer_not_speaker, placeholder_ids_not_verified, possible_semantic_gap
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.783, 'translation_agreement': 0.472, 'back_translation_similarity_min': 0.625, 'top_cluster_support': 0.667, 'sense_entropy': 0.946, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
