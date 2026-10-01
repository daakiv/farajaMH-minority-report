# Review card — KISWA-STORY-07
Package `MRP-KISWA-STORY-07-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `suicidal` in *sense/S3/rationale* — ……icult situation, even if not explicitly suicidal.…
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
| T1 | gemma3:12b | I am-said have-been-struck/affected. Auntie told me to go to the traditional healer. | People say I've been bewitched. My auntie told me to see a traditional healer. | not run | The term 'roogwa' carries a strong cultural weight related to beliefs about witchcraft and spiritual influence. The precise nature of the distress is not clear without further context, but it is presented as a belief about the cause of the distress. |
| T2 | qwen2.5:7b | I feel sad. Depression they tell me is for doctor. | I feel sad. They say depression is for the doctor. | not run | uncertain |
| T3 | llama3.1:8b | I have been overwhelmed | I'm feeling completely overwhelmed | not run |  |

### How the models read it, by category (labels aside)
- **spiritual_or_supernatural**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | distress | emotional_state | minority | gemma3:12b |
| C2 | spiritual_trouble | spiritual_or_supernatural | minority | gemma3:12b |
| C4 | bewitched | spiritual_or_supernatural | minority | qwen2.5:7b |
| C5 | bewitchment | spiritual_or_supernatural | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, distress): The speaker is experiencing a state of significant emotional distress. — *The phrase 'nimerogwa' is translated as 'I've been bewitched' or 'I feel completely overwhelmed', both of which suggest a state of significant distress. The speaker's prior statement about a recent loss ('Tangu mume wangu aondoke') further supports this.* — evidence: utterance_span: “nimerogwa”
- **S2** (gemma3:12b, spiritual_trouble): The speaker believes they are experiencing a problem caused by supernatural forces. — *The phrase 'nimerogwa' is translated as 'I've been bewitched', indicating a belief that the speaker's condition is due to witchcraft or a similar spiritual cause. The aunt's advice to see a traditional healer reinforces this belief.* — evidence: utterance_span: “nimerogwa”; translation_candidate: “People say I've been bewitched”
- **S3** (gemma3:12b, risk_or_safety): The speaker's statement, even if expressed metaphorically, suggests a desire for intervention or an escape from a difficult situation. — *While 'nimerogwa' may be an idiomatic expression, the context of the conversation and the aunt's advice to seek help from a traditional healer suggest the speaker is experiencing significant distress that warrants attention. It is possible that the speaker is expressing a desire to escape a difficult situation, even if not explicitly suicidal.* — evidence: utterance_span: “nimerogwa”
- **S4** (qwen2.5:7b, bewitched): The speaker believes they have been bewitched. — *The speaker directly states that people say they have been bewitched, and the negation is affirmed, indicating a personal belief.* — evidence: utterance_span: “nimerogwa”
- **S5** (llama3.1:8b, bewitchment): Being under a curse or spell, often attributed to supernatural forces. — *The speaker mentions being 'bewitched' and is advised to see a traditional healer, which suggests a supernatural explanation.* — evidence: utterance_span: “nimerogwa”
- **S6** (llama3.1:8b, risk_or_safety): Expressing a desire to harm oneself or end one's life. — *The speaker's statement 'nimerogwa' may be idiomatic, but it refers to being 'bewitched' and implies a sense of being overwhelmed or trapped, which could be a statement of intent.* — evidence: utterance_span: “nimerogwa”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000031` crying []; `MFOEM:000052` compassion []; `MFOEM:000055` shame []; `MFOEM:000216` gloomy mood [llama3.1:8b→skos:broadMatch]; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000151` binge-eating disorder []; `MFOMD:0000004` mental disorder []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000187` abstinence syndrome [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C5**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.867, 'translation_agreement': 0.026, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.97, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
