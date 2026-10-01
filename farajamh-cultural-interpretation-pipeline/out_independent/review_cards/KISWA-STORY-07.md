# Review card — KISWA-STORY-07
Package `MRP-KISWA-STORY-07-indep-solo` · priority **high** · backend `live`

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
> - `nife` in *gap_note/C1* — ……t specifying a particular disorder or manifestation. | the concepts do not fully cap……
> - `suicidal ideation` in *gap_note/C2* — ……tentially including concepts related to suicidal ideation, crisis states, or threats of violence.……
> - `self-harm` in *gap_note/C2* — ……ession of distress related to potential self-harm or harm to others. | concepts would nee……
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
> Self-reported plausibility for these senses: 0.90, 0.60 — poorly calibrated on small models; weigh the grounding above it.
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
| T1 | gemma3:12b | I am-said have-been-struck/affected. Auntie told-me to-go to the traditional healer. | People say I've been bewitched. My auntie told me to go see a traditional healer. | not run | The term 'nimerogwa' is deeply embedded in beliefs about witchcraft and spiritual influence. The literal translation attempts to show the sense of being affected by an external force, but the full meaning is tied to cultural understandings of magic and curses. Without further context, it's difficult to know the precise nature of the distress being expressed. |
| T2 | qwen2.5:7b | I feel sad. The pain they tell me is to see a doctor. | I feel sad. They say the pain is to see a doctor. | not run | uncertain |
| T3 | llama3.1:8b | I have been worn out | I'm exhausted, drained, and feeling overwhelmed | not run |  |

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

- **S1** (gemma3:12b, distress): The speaker is experiencing a state of significant emotional distress. — *The phrase 'nimerogwa' suggests a feeling of being deeply affected or disrupted, which aligns with a state of distress. The conversation confirms a recent loss and a new, negative experience.* — evidence: utterance_span: “nimerogwa”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a level of distress that warrants consideration for potential self-harm or harm to others. — *The phrase 'nimerogwa' conveys a strong negative emotional state. While it may be an idiomatic expression, the context of a recent loss and the advice to seek help from a traditional healer ('mganga') suggests a need to assess for potential risk. The phrase may be hyperbolic, but it is not possible to rule out a literal statement of distress.* — evidence: utterance_span: “nimerogwa”
- **S3** (qwen2.5:7b, sadness): The speaker feels sad or upset. — *The speaker uses the term 'nimerogwa', which is a Swahili word meaning 'to cry' or 'to be sad'. The speaker is affirming this state.* — evidence: utterance_span: “Wanasema nimerogwa.”
- **S4** (llama3.1:8b, sadness): I am feeling unhappy or depressed. — *The speaker mentions that their husband has left, which is a common cause of sadness in many cultures.* — evidence: model_background_knowledge: “”
- **S5** (llama3.1:8b, risk_or_safety): I am at risk of harm or injury, possibly due to my husband's departure. — *The speaker mentions that their husband has left, which may put them at risk of harm or injury, especially if they are financially or emotionally dependent on him.* — evidence: utterance_span: “nimerogwa”; context_field: “participant”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000031` crying []; `MFOEM:000052` compassion []; `MFOEM:000055` shame []; `MFOEM:000216` gloomy mood [llama3.1:8b→skos:broadMatch]; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000151` binge-eating disorder []; `MFOMD:0000004` mental disorder []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000187` abstinence syndrome [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode [gemma3:12b→skos:broadMatch]; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.867, 'translation_agreement': 0.048, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
