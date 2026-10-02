# Review card — KISWA-STORY-03
Package `MRP-KISWA-STORY-03-example-v2` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 3 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.90, 0.70 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Usingizi umenikimbia. Nakesha hadi alfajiri nikiwaza.
**Expression:** Usingizi umenikimbia
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Usingizi umenikimbia. Nakesha hadi alfajiri nikiwaza.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Sleep has run away from me. | Sleep has abandoned me. | not run | None |
| T2 | qwen2.5:7b | Sadness is entering me. I feel sad until dawn I cry. | Sadness is entering me. I feel so sad until dawn, I cry. | not run | uncertain |
| T3 | llama3.1:8b | Sleep has fled. I am still until dawn I am crying. | I'm having trouble sleeping. I'm still awake at dawn, feeling overwhelmed. | not run |  |

### How the models read it, by category (labels aside)
- **somatic_experience**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 2/3 models (gemma3:12b, llama3.1:8b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **clinical_symptom**: 1/3 models (qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sleep difficulty | somatic_experience | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | sadness | emotional_state | majority | gemma3:12b, llama3.1:8b |
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sleeplessness): The speaker is experiencing difficulty sleeping. — *The phrase 'Usingizi umenikimbia' translates to 'Sleep has abandoned me,' directly indicating a lack of sleep. The subsequent phrase 'Nakesha hadi alfajiri' ('I stayed awake until dawn') reinforces this.* — evidence: utterance_span: “Usingizi umenikimbia”; utterance_span: “Nakesha hadi alfajiri”
- **S2** (gemma3:12b, sadness): The speaker is feeling sadness or grief. — *One translation candidate suggests 'Sadness is entering me.' While this may be a metaphorical expression of distress, it indicates a feeling of sadness or grief.* — evidence: translation_candidate: “Sadness is entering me.”
- **S3** (gemma3:12b, risk_or_safety): The speaker's expression, while potentially hyperbolic, indicates a desire to not be in their current state and warrants assessment for risk. — *The phrase 'Sleep has abandoned me' and the description of prolonged wakefulness and distress, even if expressed metaphorically, could indicate a desire to escape a difficult situation. It is crucial to assess the speaker's safety and well-being.* — evidence: utterance_span: “Usingizi umenikimbia”; utterance_span: “Nakesha hadi alfajiri nikiwaza”
- **S4** (qwen2.5:7b, sleep difficulty): The speaker is experiencing trouble sleeping. — *The speaker directly states that sleep has abandoned them, indicating current difficulty in sleeping.* — evidence: utterance_span: “Usingizi umenikimbia.”
- **S5** (llama3.1:8b, sleep difficulty): Having trouble sleeping. — *The speaker mentions being awake at dawn, which suggests difficulty sleeping.* — evidence: utterance_span: “Usingizi umenikimbia”
- **S6** (llama3.1:8b, sadness): Feeling sad or overwhelmed. — *The speaker mentions feeling sad until dawn and crying, which suggests experiencing sadness.* — evidence: utterance_span: “Nakesha hadi alfajiri nikiwaza”
- **S7** (llama3.1:8b, risk_or_safety): Feeling overwhelmed or in distress, potentially indicating a risk to one's safety. — *The speaker mentions feeling overwhelmed and crying until dawn, which may indicate a risk to their safety or well-being.* — evidence: utterance_span: “Nakesha hadi alfajiri nikiwaza”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOMD:0000116` insomnia [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOMD:0000142` delayed sleep-phase syndrome []; `MFOMD:0000088` primary sleep disorder: dyssomnia []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode [] — **no adequate match** per gemma3:12b
- **C2**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.026, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.982, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
