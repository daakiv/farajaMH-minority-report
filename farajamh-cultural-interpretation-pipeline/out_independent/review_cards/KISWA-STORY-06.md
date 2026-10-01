# Review card — KISWA-STORY-06
Package `MRP-KISWA-STORY-06-indep-solo` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S6/gloss* — ……elmed or trapped and may be considering self-harm.…
> - `nife` in *gap_note/C1* — …the other concepts focus on specific manifestations or valence of surprise, but do……
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
> Self-reported plausibility for these senses: 0.70, 0.60 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** La, hii ni mpya. Tangu mume wangu aondoke.
**Expression:** hii ni mpya
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`La, hii ni mpya. Tangu mume wangu aondoke.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | this is new | This is new, since my husband left. | not run | The phrase 'hii ni mpya' literally means 'this is new'. In this context, it implies that the speaker is experiencing a new or recent feeling of distress related to her husband leaving. It doesn't necessarily mean a clinical diagnosis of depression or anxiety, but rather a fresh wave of grief or hardship. |
| T2 | qwen2.5:7b | This is new. Since my father started to forget. | This is new. Since my father started forgetting. | not run |  |
| T3 | llama3.1:8b | This is new | This is all too much for me | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **cognitive_process**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | surprise | emotional_state | minority | gemma3:12b |
| C2 | novelty | cognitive_process | minority | gemma3:12b |
| C4 | new | emotional_state | minority | qwen2.5:7b |
| C5 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, surprise): The speaker is expressing surprise at something. — *The utterance 'La, hii ni mpya' can be interpreted as an expression of surprise or unexpectedness. The 'La' often signals a reaction to something new or unexpected. The context of a home visit and discussion of daily work suggests the 'mpya' refers to a new development or situation.* — evidence: utterance_span: “La, hii ni mpya”
- **S2** (gemma3:12b, novelty): The speaker is describing something as new or recent. — *The word 'mpya' directly translates to 'new' or 'recent'. The speaker may be describing a new feeling, situation, or experience that has arisen since their husband left.* — evidence: utterance_span: “hii ni mpya”
- **S3** (gemma3:12b, risk_or_safety): The speaker is expressing a feeling of being overwhelmed or unable to cope, potentially indicating a need for support or intervention; this phrasing may be hyperbolic. — *The phrase 'hii ni mpya' following 'Tangu mume wangu aondoke' (Since my husband left) could be a hyperbolic expression of distress, implying that the speaker's current state is a new and difficult experience. The preceding conversation about inability to work and loss of strength suggests a potential risk to the speaker's well-being. It may be idiomatic.* — evidence: utterance_span: “hii ni mpya”; conversation_turn: “Siwezi kulima tena. Nikianza, nguvu zinaisha mara moja.”
- **S4** (qwen2.5:7b, new): This is new. — *The speaker is using the phrase 'hii ni mpya' to indicate that something is new or recent.* — evidence: utterance_span: “La, hii ni mpya. Tangu mume wangu aondoke.”
- **S5** (llama3.1:8b, sadness): This is a new experience of sadness. — *The speaker says 'La, hii ni mpya' which can be translated to 'No, this is new'. The negation and the use of 'new' suggest that the speaker is experiencing something unpleasant.* — evidence: utterance_span: “hii ni mpya”
- **S6** (llama3.1:8b, risk_or_safety): The speaker feels overwhelmed or trapped and may be considering self-harm. — *The speaker says 'Tangu mume wangu aondoke' which can be translated to 'Since my husband left'. The use of 'since' and the context of the conversation suggest that the speaker may be feeling overwhelmed or trapped. The phrase 'hii ni mpya' may be idiomatic, but it could also be a statement of intent.* — evidence: utterance_span: “Tangu mume wangu aondoke”; model_background_knowledge: “”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000032` surprise [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000189` canonical surprised voice utterance []; `MFOEM:000190` canonical surprised facial expression []; `MFOEM:000209` positive surprise []; `MFOEM:000210` negative surprise []
- **C2**: `MFOEM:000033` interest [llama3.1:8b→skos:relatedMatch]; `MFOMD:0000083` orgasmic disorder [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C4**: `MFOMD:0000053` process addiction [llama3.1:8b→skos:broadMatch]; `MFOMD:0000076` dissociative fugue []; `MFOMD:0000084` sexual pain disorder [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C5**: `MFOEM:000056` sadness []; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b, qwen2.5:7b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.095, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.97, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
