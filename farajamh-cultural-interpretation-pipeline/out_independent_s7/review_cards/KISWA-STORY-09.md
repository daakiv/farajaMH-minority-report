# Review card — KISWA-STORY-09
Package `MRP-KISWA-STORY-09-indep-solo-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 3 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.70, 0.70 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Nimejifungia ndani. Sitaki kuona mtu.
**Expression:** Nimejifungia ndani
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Nimejifungia ndani. Sitaki kuona mtu.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I-have-locked myself inside. I-do-not want to see person. | I've locked myself in. I don't want to see anyone. | not run |  |
| T2 | qwen2.5:7b | We are feeling inside. Because we see a person. | We are feeling upset. Because we see a person. | not run | uncertain |
| T3 | llama3.1:8b | I have locked myself inside | I'm feeling overwhelmed and isolated | not run |  |

### How the models read it, by category (labels aside)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 2/3 models (llama3.1:8b, qwen2.5:7b)
- **social_or_relational**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | withdrawal | social_or_relational | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, withdrawal): The speaker is expressing a desire to isolate themselves from others. — *The phrase 'Sitaki kuona mtu' directly translates to 'I don't want to see anyone,' indicating a desire to avoid social contact.* — evidence: utterance_span: “Sitaki kuona mtu”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a desire to avoid others, which warrants consideration as a potential indicator of distress or a need for safety. — *The phrase 'Sitaki kuona mtu' could be a hyperbolic expression of distress, or a statement of intent to avoid contact, and requires assessment for risk. It may be idiomatic, but this does not negate the need to consider it as a potential indicator of distress.* — evidence: utterance_span: “Sitaki kuona mtu”
- **S3** (qwen2.5:7b, sadness): The speaker feels sad or down. — *The speaker uses the word 'jifungia' which can mean feeling down or sad, and affirms this state.* — evidence: utterance_span: “Nimejifungia ndani”
- **S4** (llama3.1:8b, sadness): Feeling overwhelmed and wanting to withdraw from social interactions. — *The speaker says 'Nimejifungia ndani' which means 'I have locked myself inside', implying a desire to withdraw from the outside world. The phrase 'Sitaki kuona mtu' means 'I don't want to see anyone', further supporting this sense.* — evidence: utterance_span: “Nimejifungia ndani”; utterance_span: “Sitaki kuona mtu”
- **S5** (llama3.1:8b, risk_or_safety): The speaker may be at risk of harming themselves or others due to their emotional state. — *The speaker's desire to withdraw from social interactions and not see anyone may be a sign of emotional distress that could potentially lead to harm to themselves or others.* — evidence: utterance_span: “Nimejifungia ndani”; utterance_span: “Sitaki kuona mtu”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []
- **C1**: `MFOMD:0000202` craving (withdrawal) [llama3.1:8b→skos:broadMatch]; `MFOMD:0000046` addiction disorder []; `MFOMD:0000021` catatonic schizophrenia []; `MFOMD:0000013` depressed mood episode [] — **no adequate match** per gemma3:12b, qwen2.5:7b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.883, 'translation_agreement': 0.03, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
