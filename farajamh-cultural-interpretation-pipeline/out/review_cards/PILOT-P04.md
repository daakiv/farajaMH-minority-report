# Review card — PILOT-P04
Package `MRP-PILOT-P04-pilot-dryrun` · priority **high** · backend `fixture_simulated`

> SIMULATED run: candidates come from hand-written fixtures and concept IDs are placeholders.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Mawazo yananichoma kichwa usiku.
**Expression:** Mawazo yananichoma kichwa
**Context:** KE/KE-western, dialect standard, speaker participant, setting chat_platform, negation affirmed, temporality recurrent, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Mawazo yananichoma kichwa usiku.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | sim-model-A | thoughts they-are-burning-me head at-night | At night my thoughts burn in my head. | Usiku mawazo yananiunguza kichwani. (0.333) |  |
| T2 | sim-model-B | thoughts burn-me head night | At night, thoughts make my head burn. | Usiku, mawazo yanafanya kichwa changu kiungue. (0.429) |  |
| T3 | sim-model-C | thoughts pierce-me head night | At night I get headaches from thinking. | Usiku napata maumivu ya kichwa kwa kufikiri. (0.286) | '-choma' can mean burn or pierce. |

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | thinking too much | cognitive_process | unanimous | sim-model-A, sim-model-B, sim-model-C |
| C2 | burning head sensation | somatic_experience | minority | sim-model-A |
| C3 | night-time intrusive thoughts | cognitive_process | minority | sim-model-B |
| C4 | headache | clinical_symptom | minority | sim-model-C |

<details><summary>Rationale and evidence per model</summary>

- **S1** (sim-model-A, thinking too much): Troubling thoughts experienced as heat or burning in the head. — *Idiom joins thinking too much with a bodily metaphor.* — evidence: utterance_span: “Mawazo yananichoma kichwa”
- **S2** (sim-model-A, burning head sensation): A bodily burning or heat sensation in the head. — *Somatic idioms of distress are common.* — evidence: utterance_span: “kichwa”
- **S3** (sim-model-B, night-time intrusive thoughts): Unwanted thoughts that keep coming at night. — *'Usiku' places it at night; may affect sleep.* — evidence: utterance_span: “usiku”
- **S4** (sim-model-B, thinking too much): Thinking too much at night. — *Idiom reading.* — evidence: utterance_span: “Mawazo”
- **S5** (sim-model-C, headache): Headache caused by thinking. — *Literal reading of kichwa + choma.* — evidence: utterance_span: “kichwa”
- **S6** (sim-model-C, thinking too much): Excessive thinking. — *Mawazo.* — evidence: utterance_span: “Mawazo”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `SCTID:LOOKUP-worrying` <lookup: worrying> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]; `SCTID:LOOKUP-rumination` <lookup: rumination> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C2**: `SCTID:LOOKUP-burning-sensation-of-head` <lookup: burning sensation of head> [sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch] — **no adequate match** per sim-model-A
- **C3**: `SCTID:LOOKUP-intrusive-thoughts` <lookup: intrusive thoughts> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]
- **C4**: `SCTID:LOOKUP-headache` <lookup: headache> [sim-model-A→skos:broadMatch, sim-model-B→skos:broadMatch, sim-model-C→skos:exactMatch]

### Signals
- Risk flags: cultural_term_lost_in_back_translation, minority_clinical_reading, over_medicalisation_risk, placeholder_ids_not_verified, possible_semantic_gap, register_divergence_clinical_vs_everyday
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.617, 'translation_agreement': 0.356, 'back_translation_similarity_min': 0.286, 'top_cluster_support': 1.0, 'sense_entropy': 0.896, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
