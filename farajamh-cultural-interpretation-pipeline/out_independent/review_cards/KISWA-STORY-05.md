# Review card — KISWA-STORY-05
Package `MRP-KISWA-STORY-05-indep-solo` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 2 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.90, 0.60 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Siwezi kulima tena. Nikianza, nguvu zinaisha mara moja.
**Expression:** nguvu zinaisha mara moja
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Siwezi kulima tena. Nikianza, nguvu zinaisha mara moja.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I-cannot plough again. If-I-start, strength they-end immediately. | I can't plough again. As soon as I start, my strength just vanishes. | not run | None |
| T2 | qwen2.5:7b | strength my is heavy one day | I feel very weak today | not run |  |
| T3 | llama3.1:8b | strengths finish once | I lose my energy immediately | not run |  |

### How the models read it, by category (labels aside)
- **somatic_experience**: 2/3 models (gemma3:12b, llama3.1:8b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 1/3 models (qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | exhaustion | somatic_experience | minority | gemma3:12b |
| C3 | worry | emotional_state | minority | qwen2.5:7b |
| C4 | physical_exhaustion | somatic_experience | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, exhaustion): The speaker states that their strength ends immediately upon starting a task. — *The phrase 'nguvu zinaisha mara moja' directly translates to 'strength ends immediately'. The context of discussing worries about work and family suggests this refers to physical exhaustion related to labor.* — evidence: utterance_span: “nguvu zinaisha mara moja”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially hyperbolic, expresses a sense of being overwhelmed and unable to continue, which could indicate a risk of harm due to inability to sustain essential tasks. — *While 'nguvu zinaisha mara moja' may be an idiomatic expression for extreme tiredness, the context of financial and familial worries suggests a potential for distress that could lead to self-neglect or other harmful behaviors. It is safer to propose this sense than to assume it is purely figurative.* — evidence: utterance_span: “nguvu zinaisha mara moja”
- **S3** (qwen2.5:7b, worry): I worry sometimes. — *The speaker is expressing that they worry sometimes, which is indicated by the phrase 'nguvu zinaisha mara moja' (I worry sometimes).* — evidence: utterance_span: “nguvu zinaisha mara moja”
- **S4** (llama3.1:8b, physical_exhaustion): Physical strength or energy ends quickly — *The speaker mentions that their strength or energy ends quickly, which suggests a physical or bodily experience.* — evidence: utterance_span: “nguvu zinaisha mara moja”
- **S5** (llama3.1:8b, risk_or_safety): The speaker may be at risk of physical harm or injury — *The speaker's physical strength or energy ends quickly, which may indicate a risk of physical harm or injury, especially if they are engaging in physically demanding activities.* — evidence: utterance_span: “nguvu zinaisha mara moja”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000112` feeling exhausted [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b
- **C3**: `MFOEM:000171` worry [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000168` concern []; `MFOMD:0000184` nervousness [] — **no adequate match** per gemma3:12b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.0, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.961, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
