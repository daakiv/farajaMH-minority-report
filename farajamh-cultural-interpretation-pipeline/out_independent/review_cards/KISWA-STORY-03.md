# Review card — KISWA-STORY-03
Package `MRP-KISWA-STORY-03-indep-solo` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *gap_note/C3* — ……retrieved concepts focus on specific manifestations of sadness (facial expression,……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 3 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.60, 0.60 — poorly calibrated on small models; weigh the grounding above it.
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
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 2/3 models (llama3.1:8b, qwen2.5:7b)
- **somatic_experience**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | sleeplessness | somatic_experience | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sleeplessness): The speaker is experiencing difficulty sleeping. — *The utterance 'Usingizi umenikimbia' can be interpreted as 'sleep has abandoned me,' indicating a lack of sleep. The subsequent phrase 'Nakesha hadi alfajiri nikiwaza' (I stayed awake until dawn, worrying) reinforces this sense of sleeplessness and mental distress.* — evidence: utterance_span: “Usingizi umenikimbia”; utterance_span: “Nakesha hadi alfajiri nikiwaza”
- **S2** (gemma3:12b, risk_or_safety): The speaker's expression of sleeplessness and worry may be a veiled indication of distress or a desire to end their current situation, requiring further assessment. — *While the phrasing 'Usingizi umenikimbia' and 'Nakesha hadi alfajiri nikiwaza' may be idiomatic expressions of distress, they could also reflect a deeper desire to escape a difficult situation. It is crucial to assess the speaker's intent and safety.* — evidence: utterance_span: “Usingizi umenikimbia”; utterance_span: “Nakesha hadi alfajiri nikiwaza”
- **S3** (qwen2.5:7b, sadness): The speaker is feeling sad and uninterested in activities. — *The speaker uses the phrase 'umenikimbia' which implies a lack of interest or unwillingness to engage, often associated with sadness.* — evidence: utterance_span: “Usingizi umenikimbia.”
- **S4** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker says 'Usingizi umenikimbia' which can be translated to 'Sleep has fled' or 'Sleep has run away'. This suggests that the speaker is experiencing a sense of loss or absence of sleep.* — evidence: utterance_span: “Usingizi umenikimbia”
- **S5** (llama3.1:8b, risk_or_safety): expression of distress related to dying or wanting to die — *The speaker says 'Usingizi umenikimbia' which can be translated to 'Sleep has fled' or 'Sleep has run away'. This phrase may be idiomatic, but it could also be interpreted as a statement of intent to leave or exit the world.* — evidence: utterance_span: “Usingizi umenikimbia”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.026, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
