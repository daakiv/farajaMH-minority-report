# Review card — KISWA-STORY-11
Package `MRP-KISWA-STORY-11-indep-solo` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S1/rationale* — ……given the preceding conversation about self-harm, must be treated as a potential stateme……
> - `self-harm` in *sense/S5/gloss* — …considering self-harm or suicide…
> - `suicide` in *sense/S5/gloss* — …considering self-harm or suicide…
> - `kujidhuru` in *sense/S5/rationale* — …the speaker mentions having 'mawazo ya kujidhuru' (thoughts of harming oneself) in the p……
> - `suicidal ideation` in *gap_note/C4* — ……ncepts would need to cover self-harm or suicidal ideation, with a focus on the cultural context o……
> - `self-harm` in *gap_note/C4* — ……ver the specific meaning of considering self-harm or suicide in the context of an east af……
> - `suicide` in *gap_note/C4* — ……fic meaning of considering self-harm or suicide in the context of an east african expre……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (minority): **desire_to_not_exist**; **risk_or_safety**.
>
> Grounding: 1 quote from the utterance itself; 1 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.90, 0.80 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Kuna siku nafikiri afadhali nisiwepo. Lakini watoto wananihitaji.
**Expression:** afadhali nisiwepo
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Kuna siku nafikiri afadhali nisiwepo. Lakini watoto wananihitaji.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | There days I think it is better I not be (to exist). | There are days when I think it would be better if I weren't here. But my children need me. | not run |  |
| T2 | qwen2.5:7b | please think for me today. But children need too. | Please think of me today. But the children need it too. | not run |  |
| T3 | llama3.1:8b | it is better I do not exist | I wish I wasn't here | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | sadness | emotional_state | majority | gemma3:12b, llama3.1:8b |
| C1 | desire_to_not_exist | risk_or_safety | minority | gemma3:12b |
| C3 | stress | emotional_state | minority | qwen2.5:7b |
| C4 | risk_or_safety | risk_or_safety | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, desire_to_not_exist): The speaker expresses a wish that they were not present. — *The phrase 'afadhali nisiwepo' directly translates to 'it would be better if I were not here,' which, given the preceding conversation about self-harm, must be treated as a potential statement of risk, even if it is potentially idiomatic or hyperbolic. The context of a home visit and a question about self-harm thoughts further reinforces the need to consider this as a risk factor.* — evidence: utterance_span: “afadhali nisiwepo”
- **S2** (gemma3:12b, sadness): The speaker is feeling deeply sad or down. — *The speaker's previous statement 'Niko down sana, stress imezidi. Sina mood ya kitu.' indicates a state of sadness and low mood, which could be contributing to the desire to not exist.* — evidence: conversation_turn: “Niko down sana, stress imezidi. Sina mood ya kitu.”
- **S3** (qwen2.5:7b, stress): The speaker is feeling stressed and overwhelmed. — *The speaker explicitly mentions feeling stressed and having a bad mood.* — evidence: conversation_turn: “stress imezidi. Sina mood ya kitu.”
- **S4** (llama3.1:8b, sadness): feeling extremely unhappy or depressed — *The speaker mentions being 'down sana' and having 'stress imezidi', which suggests they are experiencing strong negative emotions.* — evidence: conversation_turn: “Niko down sana, stress imezidi”
- **S5** (llama3.1:8b, risk_or_safety): considering self-harm or suicide — *The speaker mentions having 'mawazo ya kujidhuru' (thoughts of harming oneself) in the previous conversation, and the current utterance uses the phrase 'afadhali nisiwepo', which may be idiomatic but could be interpreted as a statement of intent.* — evidence: conversation_turn: “Je, umewahi kuwa na mawazo ya kujidhuru?”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000029` stress (emotion) [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOMD:0000152` chronic stress []; `MFOMD:0000076` dissociative fugue []; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000135` suicide []; `MFOMD:0000147` nightmare []; `MFOMD:0000167` defense mechanism []
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, minority_clinical_reading, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output repaired in 2 place(s): qwen2.5:7b/interpret evidence.type (quote not in the utterance)="utterance_span: stress imezidi. Sina mood ya kitu." → conversation_turn; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Niko down sana, stress imezidi" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.983, 'translation_agreement': 0.097, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.961, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
