# Review card — KISWA-STORY-02
Package `MRP-KISWA-STORY-02-indep-solo` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *sense/S1/rationale* — ……s or pressure, which can be a somatic manifestation of emotional distress. the phras……
> - `self-harm` in *sense/S2/gloss* — ……that warrants assessment for potential self-harm or significant psychological distress.…
> - `self-harm` in *sense/S2/rationale* — ……mportant to consider the possibility of self-harm or a severe mental health crisis, even……
> - `self-harm` in *gap_note/C2* — ……eaning of distress related to potential self-harm or significant psychological distress i……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 2 quotes from the utterance itself; 1 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.80, 0.60 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Ni kama kuna jiwe kifuani kwangu, halitoki.
**Expression:** kuna jiwe kifuani kwangu
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Ni kama kuna jiwe kifuani kwangu, halitoki.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | there is stone on chest my, it-does-not-leave | I feel like there's a heavy stone on my chest that won't go away. | not run | None |
| T2 | qwen2.5:7b | If I have a heavy heart in my chest, I do not laugh. | When my heart is heavy, I don't laugh. | not run |  |
| T3 | llama3.1:8b | there is a stone on my head | I feel weighed down, like a burden is on my head | not run |  |

### How the models read it, by category (labels aside)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 2/3 models (llama3.1:8b, qwen2.5:7b)
- **somatic_experience**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | burden | somatic_experience | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, burden): The speaker feels a heavy weight or burden on their chest. — *The phrase 'kuna jiwe kifuani kwangu' literally translates to 'there is a stone on my chest.' This suggests a feeling of heaviness or pressure, which can be a somatic manifestation of emotional distress. The phrase 'halitoki' ('it doesn't go away') reinforces the persistent nature of this feeling.* — evidence: utterance_span: “kuna jiwe kifuani kwangu”; utterance_span: “halitoki”
- **S2** (gemma3:12b, risk_or_safety): The speaker's expression, while potentially figurative, conveys a sense of distress that warrants assessment for potential self-harm or significant psychological distress. — *The imagery of a stone on the chest, combined with the feeling that it won't go away, could be a metaphorical expression of overwhelming distress. While it may be idiomatic, the phrasing expresses a desire for relief and a sense of being trapped, which necessitates a risk assessment. It is important to consider the possibility of self-harm or a severe mental health crisis, even if the expression is figurative.* — evidence: utterance_span: “kuna jiwe kifuani kwangu”; utterance_span: “halitoki”
- **S3** (qwen2.5:7b, sadness): The speaker is feeling sad about something related to their heart. — *The speaker uses the term 'jiwe kifuani' which is related to the heart, and states that their mood has been bad for three months, indicating sadness.* — evidence: utterance_span: “kuna jiwe kifuani kwangu”
- **S4** (llama3.1:8b, sadness): I feel unhappy and burdened — *The speaker mentions their heart has been heavy for three days, indicating a negative emotional state.* — evidence: conversation_turn: “moyo wangu umekuwa mzito”
- **S5** (llama3.1:8b, risk_or_safety): I feel overwhelmed and may be at risk of emotional harm — *The speaker's heart being heavy for three days may indicate a sense of emotional overload, which could potentially lead to risk of emotional harm.* — evidence: conversation_turn: “moyo wangu umekuwa mzito”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 2 place(s): llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: moyo wangu umekuwa mzito" → conversation_turn; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: moyo wangu umekuwa mzito" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.056, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
