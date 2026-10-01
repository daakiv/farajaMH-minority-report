# Review card — KISWA-STORY-09
Package `MRP-KISWA-STORY-09-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/rationale* — ……d interaction and potentially a risk of self-harm or harm to others. it is important to a……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 2 quotes from the utterance itself.
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
| C1 | isolation | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, isolation): The speaker expresses a desire to be alone and avoid contact with others. — *The phrase 'Sitaki kuona mtu' directly translates to 'I don't want to see anyone,' indicating a wish to avoid social contact and suggesting a feeling of isolation.* — evidence: utterance_span: “Sitaki kuona mtu”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a desire to avoid others and may indicate a need for safety assessment. — *The phrase 'Nimejifungia ndani' (I've locked myself in) and 'Sitaki kuona mtu' (I don't want to see anyone) could be hyperbolic expressions of distress, but they also suggest a desire to avoid interaction and potentially a risk of self-harm or harm to others. It is important to assess the speaker's safety and well-being.* — evidence: utterance_span: “Nimejifungia ndani. Sitaki kuona mtu.”
- **S3** (qwen2.5:7b, isolation): The speaker feels isolated and does not want to see anyone. — *The speaker explicitly states they do not want to see anyone, indicating a desire for isolation.* — evidence: utterance_span: “Sitaki kuona mtu.”
- **S4** (llama3.1:8b, isolation): feeling trapped or shut away from others — *The speaker says 'Nimejifungia ndani', which means 'I've locked myself in', suggesting a physical or emotional sense of being trapped.* — evidence: utterance_span: “Nimejifungia ndani”
- **S5** (llama3.1:8b, risk_or_safety): expressing a desire to harm oneself or escape the situation — *The speaker says 'Sitaki kuona mtu', which means 'I don't want to see anyone', and given the context of feeling overwhelmed and isolated, this may be a statement of intent to harm oneself or escape the situation.* — evidence: utterance_span: “Sitaki kuona mtu”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000023` residual schizophrenia [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.883, 'translation_agreement': 0.03, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.971, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
