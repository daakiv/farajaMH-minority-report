# Review card — KISWA-STORY-04
Package `MRP-KISWA-STORY-04-indep-solo` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/gloss* — ……at warrants consideration for potential self-harm or harm to others, given the context of……
> - `self-harm` in *gap_note/C2* — ……specific context of distress, potential self-harm or harm to others, and the elements of……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 1 quote from the utterance itself; 1 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.90, 0.00 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Mawazo ya deni, ya watoto, ya kazi. Yananijaa kichwani.
**Expression:** Yananijaa kichwani
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Mawazo ya deni, ya watoto, ya kazi. Yananijaa kichwani.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Thoughts of debt, of children, of work. They fill my head. | I'm overwhelmed with thoughts of debt, my children, and my work. It's all consuming me. | not run | None |
| T2 | qwen2.5:7b | Thoughts of death, of children, of work. They make me feel heavy. | Thinking about death, children, and work makes me feel weighed down. | not run |  |
| T3 | llama3.1:8b | Thoughts of debt, of children, of work. They are shouting at my head. | I'm overwhelmed by worries about my family's financial struggles, my kids, and my job. | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **cognitive_process**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C4 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | worry | emotional_state | minority | gemma3:12b |
| C3 | cognitive_process | cognitive_process | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, worry): The speaker's head is filled with worries about debts, children, and work. — *The phrase 'Mawazo ya deni, ya watoto, ya kazi' directly translates to 'thoughts of debt, of children, of work,' which are common sources of worry. The phrase 'Yananijaa kichwani' means 'they fill my head,' suggesting the speaker is overwhelmed by these thoughts.* — evidence: utterance_span: “Mawazo ya deni, ya watoto, ya kazi”; utterance_span: “Yananijaa kichwani”
- **S2** (gemma3:12b, risk_or_safety): The speaker's expression, while potentially hyperbolic, indicates a level of distress that warrants consideration for potential self-harm or harm to others, given the context of sleeplessness and worry. — *The speaker's statement, 'Mawazo ya deni, ya watoto, ya kazi. Yananijaa kichwani,' expresses significant distress and sleeplessness. While the phrasing may be idiomatic or hyperbolic, the combination of these factors warrants a risk assessment. The speaker's inability to sleep and the overwhelming nature of their worries could be indicative of underlying distress that requires further exploration.* — evidence: conversation_turn: “Usingizi umenikimbia. Nakesha hadi alfajiri nikiwaza.”
- **S3** (gemma3:12b, cognitive_process): The speaker is experiencing intrusive or obsessive thoughts related to debts, children, and work. — *The phrase 'Yananijaa kichwani' suggests the thoughts are pervasive and difficult to escape, potentially indicating a cognitive process beyond simple worry. The speaker's sleeplessness further supports this interpretation.* — evidence: utterance_span: “Yananijaa kichwani”
- **S4** (qwen2.5:7b, sadness): Expressing a sense of sadness or melancholy. — *The speaker is affirming a negative state, and the use of 'kichwani' (sadness) directly supports this sense.* — evidence: utterance_span: “Yananijaa kichwani”
- **S5** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker is affirming the statement, which suggests a strong emotional state. The use of 'yananijaa' implies a sense of being overwhelmed or consumed by emotions.* — evidence: utterance_span: “Yananijaa kichwani”
- **S6** (llama3.1:8b, risk_or_safety): feeling overwhelmed or consumed by emotions to the point of wanting to escape or flee — *The speaker's use of 'yananijaa' may be idiomatic, but it implies a sense of being overwhelmed or consumed by emotions, which could be a statement of intent to escape or flee.* — evidence: utterance_span: “Yananijaa kichwani”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []
- **C1**: `MFOEM:000171` worry [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000168` concern []; `MFOMD:0000184` nervousness [] — **no adequate match** per gemma3:12b
- **C3**: `MFOEM:000005` affective appraisal [llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 3 place(s): gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.107, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.959, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
