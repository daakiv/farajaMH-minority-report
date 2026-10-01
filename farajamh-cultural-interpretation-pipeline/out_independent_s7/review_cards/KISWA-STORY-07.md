# Review card — KISWA-STORY-07
Package `MRP-KISWA-STORY-07-indep-solo-s7` · priority **high** · backend `live`

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
> - `suicidal ideation` in *gap_note/C2* — ……tentially including concepts related to suicidal ideation, crisis states, or threats of violence.……
> - `self-harm` in *gap_note/C2* — ……at warrants consideration for potential self-harm or harm to others. | concepts would nee……
> - `nife` in *gap_note/C3* — ……ific emotion like sadness, a specific manifestation like a facial expression, or a c……
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
> Self-reported plausibility for these senses: 0.60, 0.60 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Wanasema nimerogwa. Shangazi ameniambia niende kwa mganga.
**Expression:** nimerogwa
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Wanasema nimerogwa. Shangazi ameniambia niende kwa mganga.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I am-said have-been-struck/affected. Auntie told me to go to the traditional healer. | People say I've been bewitched. My auntie told me to see a traditional healer. | not run | The term 'roogwa' carries a strong cultural weight related to beliefs about witchcraft and spiritual influence. The precise nature of the distress is not clear without further context, but it is presented as a belief about the cause of the distress. |
| T2 | qwen2.5:7b | I feel sad. Depression they tell me is for doctor. | I feel sad. They say depression is for the doctor. | not run | uncertain |
| T3 | llama3.1:8b | I have been overwhelmed | I'm feeling completely overwhelmed | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | distress | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, distress): The speaker is experiencing significant emotional distress. — *The phrase 'Wanasema nimerogwa' suggests the speaker is perceived by others as being in a state of disarray or suffering, and the context of a recent loss amplifies the likelihood of emotional distress.* — evidence: utterance_span: “Wanasema nimerogwa”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a level of distress that warrants consideration for potential self-harm or harm to others. — *The phrase 'nimerogwa' implies a state of being broken or disrupted, which, combined with the advice to see a traditional healer, could be a veiled expression of a desire to end suffering or a feeling of being overwhelmed. It may be idiomatic, but the potential for harm necessitates a risk assessment.* — evidence: utterance_span: “Wanasema nimerogwa”
- **S3** (qwen2.5:7b, sadness): The speaker is expressing sadness or distress. — *The speaker is using the term 'nimerogwa' to express a current negative state, and the negation indicates a denial of a previous state, suggesting a change in emotional state.* — evidence: utterance_span: “nimerogwa”
- **S4** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker mentions that their situation is new since their husband left, and the family members are expressing concern, which suggests that the speaker is experiencing sadness.* — evidence: conversation_turn: “Tangu mume wangu aondoke”
- **S5** (llama3.1:8b, risk_or_safety): expressing a desire to leave or exit the world — *The speaker says 'nimerogwa', which may be idiomatic or hyperbolic, but given the context, it could be interpreted as a statement of intent to leave or exit the world.* — evidence: utterance_span: “nimerogwa”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000031` crying [qwen2.5:7b→skos:broadMatch]; `MFOEM:000052` compassion []; `MFOEM:000055` shame []; `MFOEM:000216` gloomy mood [llama3.1:8b→skos:broadMatch]; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000151` binge-eating disorder []; `MFOMD:0000004` mental disorder []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000187` abstinence syndrome [] — **no adequate match** per gemma3:12b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 1 place(s): llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Tangu mume wangu aondoke" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.867, 'translation_agreement': 0.026, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
