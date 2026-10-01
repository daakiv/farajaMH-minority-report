# Review card — KISWA-STORY-04
Package `MRP-KISWA-STORY-04-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/gloss* — ……at warrants consideration for potential self-harm or harm to others.…
> - `suicidal ideation` in *gap_note/C2* — ……tentially including concepts related to suicidal ideation, aggression, or crisis states. the curr……
> - `self-harm` in *gap_note/C2* — ……at warrants consideration for potential self-harm or harm to others, and be specific to e……
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
> Self-reported plausibility for these senses: 0.80, 0.30 — poorly calibrated on small models; weigh the grounding above it.
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
| T1 | gemma3:12b | Thoughts of debt, of children, of work. They fill my head. | I'm overwhelmed with thoughts of debt, my children, and my work. My head is full. | not run | None |
| T2 | qwen2.5:7b | They make me feel bad, children, work. They make me feel very heavy. | They weigh on me, children, work. They make me feel very heavy. | not run |  |
| T3 | llama3.1:8b | Thoughts of debt, of children, of work. They are screaming in my head. | I'm overwhelmed by worries about my debts, my kids, and my job. It's all weighing on my mind. | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | mental_burden | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | overwhelmed | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, mental_burden): The speaker feels burdened by thoughts related to debt, children, and work. — *The phrase 'Yananijaa kichwani' literally translates to 'They fill my head,' suggesting a feeling of being overwhelmed or burdened by thoughts. The preceding conversation confirms the speaker is experiencing worry.* — evidence: utterance_span: “Yananijaa kichwani”
- **S2** (gemma3:12b, risk_or_safety): The speaker's expression, while potentially hyperbolic, indicates a level of distress that warrants consideration for potential self-harm or harm to others. — *The expression 'They fill my head' could be a hyperbolic way of expressing intense distress. Given the context of sleep difficulties and worry, it is necessary to consider the possibility of risk, even if the phrasing is idiomatic.* — evidence: utterance_span: “Yananijaa kichwani”
- **S3** (qwen2.5:7b, overwhelmed): The speaker feels burdened by thoughts of debt, children, and work. — *The speaker uses the phrase 'yananijaa kichwani' which means 'they weigh on me', indicating a sense of being burdened by multiple concerns.* — evidence: utterance_span: “Yananijaa kichwani”
- **S4** (llama3.1:8b, overwhelmed): feeling overwhelmed by worries and responsibilities — *The speaker mentions specific worries (debt, children, work) and describes their head as 'full' or 'weighing on' them.* — evidence: utterance_span: “Yananijaa kichwani”
- **S5** (llama3.1:8b, risk_or_safety): feeling overwhelmed to the point of considering harm or injury — *The speaker describes their thoughts as 'weighing on' them, which may be an idiomatic expression for feeling overwhelmed to the point of considering harm or injury.* — evidence: utterance_span: “Yananijaa kichwani”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000027` terror []; `MFOMD:0000076` dissociative fugue [llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.09, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
