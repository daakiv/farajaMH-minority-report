# Review card — KISWA-STORY-03
Package `MRP-KISWA-STORY-03-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *sense/S2/rationale* — ……ggests underlying distress that could manifest as anxiety.…
> - `self-harm` in *sense/S3/rationale* — ……mportant to consider the possibility of self-harm or a desire to end the distress, even i……
> - `leave the world` in *sense/S7/gloss* — …expressing a desire to escape or leave the world…
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
> Self-reported plausibility for these senses: 0.60, 0.50 — poorly calibrated on small models; weigh the grounding above it.
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
| T3 | llama3.1:8b | Sleep has run away from me. I am still until dawn I am worried. | I'm having trouble sleeping. I'm lying awake until dawn, feeling anxious. | not run |  |

### How the models read it, by category (labels aside)
- **somatic_experience**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 2/3 models (gemma3:12b, llama3.1:8b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **clinical_symptom**: 1/3 models (qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sleeplessness | somatic_experience | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C2 | anxiety | emotional_state | minority | gemma3:12b |
| C4 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sleeplessness): The speaker is experiencing difficulty sleeping. — *The phrase 'Usingizi umenikimbia' translates to 'Sleep has abandoned me,' directly indicating a lack of sleep. The phrase 'Nakesha hadi alfajiri' (I stayed/lay awake until dawn) reinforces this.* — evidence: utterance_span: “Usingizi umenikimbia”; utterance_span: “Nakesha hadi alfajiri”
- **S2** (gemma3:12b, anxiety): The speaker is feeling anxious or worried. — *The phrase 'Nikiwaza' can be interpreted as 'I am worrying' or 'I am feeling anxious.' The speaker's description of a 'stone in my chest' in the previous turn suggests underlying distress that could manifest as anxiety.* — evidence: utterance_span: “Nikiwaza”; conversation_turn: “Ni kama kuna jiwe kifuani kwangu, halitoki.”
- **S3** (gemma3:12b, risk_or_safety): The speaker's expression of sleeplessness and anxiety, while potentially idiomatic, may indicate a desire to express distress and a need for support or intervention. — *The phrasing 'Sleep has abandoned me' and the description of feeling anxious until dawn, even if hyperbolic, could be a cry for help or an indication of underlying distress that warrants further investigation. It is important to consider the possibility of self-harm or a desire to end the distress, even if not explicitly stated.* — evidence: utterance_span: “Usingizi umenikimbia”; utterance_span: “Nikiwaza”
- **S4** (qwen2.5:7b, sleep_difficulty): The speaker is experiencing trouble sleeping. — *The speaker directly states that sleep has abandoned them, indicating current difficulty in sleeping.* — evidence: utterance_span: “Usingizi umenikimbia.”
- **S5** (llama3.1:8b, sleep difficulty): Having trouble sleeping — *The speaker mentions lying awake until dawn, which suggests difficulty sleeping.* — evidence: utterance_span: “Usingizi umenikimbia”
- **S6** (llama3.1:8b, sadness): Feeling sad or sorrowful — *The speaker mentions feeling sad until dawn, which suggests an emotional state of sadness.* — evidence: utterance_span: “Nakesha hadi alfajiri nikiwaza”
- **S7** (llama3.1:8b, risk_or_safety): Expressing a desire to escape or leave the world — *The speaker says 'Sleep has abandoned me', which may be an idiomatic expression but could also be interpreted as a statement of risk or safety.* — evidence: utterance_span: “Usingizi umenikimbia”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: `MFOEM:000028` anxiety [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000196` anxious mood [gemma3:12b→skos:relatedMatch]; `MFOEM:000026` fear []; `MFOEM:000124` feeling nervous [gemma3:12b→skos:relatedMatch]; `MFOEM:000025` jealousy []; `MFOMD:0000197` substance-induced anxiety disorder []; `MFOMD:0000117` pathological anxiety []; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000147` nightmare []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000046` addiction disorder []; `MFOMD:0000102` apprehension []; `MFOMD:0000107` compulsion []
- **C4**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.051, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.921, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
