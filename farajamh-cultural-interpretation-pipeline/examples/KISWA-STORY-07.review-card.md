# Review card — KISWA-STORY-07
Package `MRP-KISWA-STORY-07-example-v2` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S6/gloss* — …considering self-harm or seeking help from a traditional heal……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 1 quote from the utterance itself; 2 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.80, 0.00 — poorly calibrated on small models; weigh the grounding above it.
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
- **emotional_state**: 2/3 models (gemma3:12b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **spiritual_or_supernatural**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | distress | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | spiritual_disruption | spiritual_or_supernatural | minority | gemma3:12b |
| C4 | bewitchment | spiritual_or_supernatural | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, distress): The speaker is experiencing a state of significant emotional distress. — *The phrase 'nimerogwa' is translated as 'I feel sad' and 'I'm exhausted, drained, and feeling overwhelmed', both of which indicate distress. The context of a recent loss ('Tangu mume wangu aondoke') further supports this.* — evidence: translation_candidate: “I feel sad.”; conversation_turn: “La, hii ni mpya. Tangu mume wangu aondoke.”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, even if expressed idiomatically or hyperbolically, may indicate a desire to end their current state or seek escape from a difficult situation. — *The phrase 'nimerogwa' is translated as 'I'm exhausted, drained, and feeling overwhelmed', which, while potentially idiomatic, could also reflect a desire to escape a painful situation. The instruction to see a traditional healer may be a sign of desperation.* — evidence: translation_candidate: “I'm exhausted, drained, and feeling overwhelmed”; utterance_span: “Shangazi ameniambia niende kwa mganga”
- **S3** (gemma3:12b, spiritual_disruption): The speaker believes they have been affected by a supernatural force or curse. — *The phrase 'nimerogwa' is translated as 'People say I've been bewitched', suggesting a belief in supernatural interference. The aunt's advice to see a traditional healer reinforces this interpretation, as traditional healers often deal with spiritual matters.* — evidence: translation_candidate: “People say I've been bewitched”
- **S4** (qwen2.5:7b, sadness): The speaker feels sad and is experiencing emotional distress. — *The speaker uses the term 'nimerogwa' which is associated with sadness and emotional distress. The speaker also mentions that their auntie told them to see a traditional healer, suggesting they are seeking help for their emotional state.* — evidence: utterance_span: “nimerogwa”
- **S5** (llama3.1:8b, bewitchment): Being accused of being bewitched by others — *The speaker mentions that 'People say I've been bewitched', which suggests a supernatural or spiritual explanation for their current situation.* — evidence: utterance_span: “Wanasema nimerogwa”
- **S6** (llama3.1:8b, risk_or_safety): Considering self-harm or seeking help from a traditional healer — *The speaker's auntie advises them to go see a traditional healer, which may be a response to a perceived risk or safety issue.* — evidence: conversation_turn: “Shangazi ameniambia niende kwa mganga”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000031` crying [llama3.1:8b→skos:exactMatch]; `MFOEM:000052` compassion []; `MFOEM:000055` shame []; `MFOEM:000216` gloomy mood []; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000151` binge-eating disorder []; `MFOMD:0000004` mental disorder []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000187` abstinence syndrome [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 3 place(s): gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.867, 'translation_agreement': 0.048, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.959, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
