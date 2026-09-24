# Review card — PILOT-P01
Package `MRP-PILOT-P01-pilot-dryrun` · priority **high** · backend `fixture_simulated`

> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Tangu msiba ule, roho yangu imeondoka.
**Expression:** roho yangu imeondoka
**Context:** KE/KE-coast, dialect Kiamu, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Tangu msiba ule, roho yangu imeondoka.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | sim-model-A | since bereavement that, soul my has-left | Since that death, I feel as if my spirit has left me. | Tangu kifo kile, nahisi kama roho yangu imeniacha. (0.222) |  |
| T2 | sim-model-B | since funeral that, spirit my it-has-gone | Since that funeral I have felt empty inside. | Tangu mazishi yale nimejisikia mtupu ndani. (0.0) | 'roho' can mean soul, spirit, heart or life-breath. |
| T3 | sim-model-C | since loss that, heart my has-gone | Since that loss, my heart has gone out of me. | Tangu msiba ule, moyo wangu umenitoka. (0.25) | Could also describe losing courage, or a fright. |

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | inner emptiness | emotional_state | majority | sim-model-A, sim-model-B |
| C2 | grief | emotional_state | majority | sim-model-A, sim-model-C |
| C3 | spiritual loss | spiritual_or_supernatural | minority | sim-model-B |
| C4 | loss of vitality | somatic_experience | minority | sim-model-C |
| C5 | fright | emotional_state | minority | sim-model-C |

<details><summary>Rationale and evidence per model</summary>

- **S1** (sim-model-A, inner emptiness): A feeling of inner emptiness or numbness after the loss. — *'Roho imeondoka' is used for a sense that one's inner life has gone.* — evidence: utterance_span: “roho yangu imeondoka”; utterance_span: “Tangu msiba ule”
- **S2** (sim-model-A, grief): Grief following a death. — *'Msiba' marks a death or funeral as the onset.* — evidence: utterance_span: “Tangu msiba ule”
- **S3** (sim-model-B, inner emptiness): Feeling empty inside since the funeral. — *My translation reads the phrase as emptiness.* — evidence: utterance_span: “roho yangu imeondoka”
- **S4** (sim-model-B, spiritual loss): A felt loss of one's spirit or spiritual connection, possibly tied to the dead person. — *Roho has a spiritual sense; the loss may be understood spiritually.* — evidence: utterance_span: “roho”; model_background_knowledge: “”
- **S5** (sim-model-C, grief): Grief reaction to a bereavement. — *Onset tied to msiba.* — evidence: utterance_span: “Tangu msiba ule”
- **S6** (sim-model-C, loss of vitality): Loss of life-energy or will: feeling that one's life-force has gone. — *Roho as life-breath suggests reduced vitality.* — evidence: utterance_span: “roho”; model_background_knowledge: “”
- **S7** (sim-model-C, fright): Having been badly shaken or frightened. — *Roho expressions are also used for fright; less likely given the bereavement onset.* — evidence: model_background_knowledge: “”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `SCTID:LOOKUP-feeling-empty` <lookup: feeling empty> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C2**: `SCTID:LOOKUP-grief` <lookup: grief> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `SCTID:LOOKUP-bereavement-finding` <lookup: bereavement finding> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `MFOEM:LOOKUP-grief-related-emotion` <lookup: grief-related emotion> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C3**: `SCTID:LOOKUP-spiritual-concern` <lookup: spiritual concern> [sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A, sim-model-B
- **C4**: `SCTID:LOOKUP-lack-of-energy` <lookup: lack of energy> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]
- **C5**: `SCTID:LOOKUP-fear` <lookup: fear> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `MFOEM:LOOKUP-fear` <lookup: fear> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A

### Signals
- Risk flags: back_translation_mismatch, cultural_term_lost_in_back_translation, placeholder_ids_not_verified, possible_semantic_gap, sense_divergence, translation_divergence
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.6, 'translation_agreement': 0.111, 'back_translation_similarity_min': 0.0, 'top_cluster_support': 0.667, 'sense_entropy': 0.963, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
