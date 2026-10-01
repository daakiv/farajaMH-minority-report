# Review card — KISWA-STORY-11
Package `MRP-KISWA-STORY-11-indep-solo-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/gloss* — ……ut requires consideration for potential self-harm ideation.…
> - `self-harm` in *sense/S2/rationale* — ……risk. the preceding conversation about self-harm increases the need for caution.…
> - `self-harm` in *sense/S5/gloss* — …considering self-harm or suicide…
> - `suicide` in *sense/S5/gloss* — …considering self-harm or suicide…
> - `kujidhuru` in *sense/S5/rationale* — …the speaker mentions having 'mawazo ya kujidhuru', which may be an idiomatic expression……
> - `suicidal ideation` in *gap_note/C2* — ……s relating to hopelessness, despair, or suicidal ideation would be relevant, but the current list……
> - `self-harm` in *gap_note/C2* — ……to not be present and the potential for self-harm ideation. | a concept would need to cov……
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
> Self-reported plausibility for these senses: 0.80, 0.70 — poorly calibrated on small models; weigh the grounding above it.
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
| T1 | gemma3:12b | There days I think it is better I not be [present/exist]. | There are days when I think it would be better if I weren't here. | not run |  |
| T2 | qwen2.5:7b | please think for me today but children need. | Please think of me today, but the children need you. | not run | uncertain |
| T3 | llama3.1:8b | it would be better for me not to exist | I wish I wasn't here | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | desire_for_absence | emotional_state | minority | gemma3:12b |
| C3 | stress | emotional_state | minority | qwen2.5:7b |
| C4 | sadness | emotional_state | minority | llama3.1:8b |
| C5 | worry | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, desire_for_absence): The speaker expresses a wish that they were not present. — *The phrase 'afadhali nisiwepo' directly translates to 'it would be better if I were not here,' indicating a desire to not be present.* — evidence: utterance_span: “afadhali nisiwepo”
- **S2** (gemma3:12b, risk_or_safety): The speaker expresses a desire to not be here, which may be a hyperbolic expression of distress but requires consideration for potential self-harm ideation. — *The phrase 'afadhali nisiwepo' expresses a desire to not exist, which, even if hyperbolic, warrants assessment for potential risk. The preceding conversation about self-harm increases the need for caution.* — evidence: utterance_span: “afadhali nisiwepo”
- **S3** (qwen2.5:7b, stress): The speaker is experiencing significant stress. — *The speaker explicitly mentions being stressed and having a bad mood.* — evidence: conversation_turn: “stress imezidi. Sina mood ya kitu.”
- **S4** (llama3.1:8b, sadness): feeling extremely sad or depressed — *The speaker mentions being 'down sana' and having 'stress imezidi', which suggests a high level of emotional distress.* — evidence: conversation_turn: “Niko down sana, stress imezidi”
- **S5** (llama3.1:8b, risk_or_safety): considering self-harm or suicide — *The speaker mentions having 'mawazo ya kujidhuru', which may be an idiomatic expression but requires careful consideration due to its potential implications.* — evidence: conversation_turn: “Je, umewahi kuwa na mawazo ya kujidhuru?”
- **S6** (llama3.1:8b, worry): feeling anxious or concerned about something — *The speaker's use of 'nafikiri' suggests they are thinking about something and may be worried.* — evidence: utterance_span: “Kuna siku nafikiri afadhali nisiwepo”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOMD:0000081` sexual desire disorder [] — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000029` stress (emotion) [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOMD:0000152` chronic stress [llama3.1:8b→skos:broadMatch]; `MFOMD:0000076` dissociative fugue []; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000135` suicide []; `MFOMD:0000147` nightmare []; `MFOMD:0000167` defense mechanism []
- **C4**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode [gemma3:12b→skos:broadMatch]; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []
- **C5**: `MFOEM:000171` worry [gemma3:12b→skos:relatedMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000168` concern [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOMD:0000184` nervousness [gemma3:12b→skos:relatedMatch]

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output repaired in 3 place(s): qwen2.5:7b/interpret evidence.type (quote not in the utterance)="utterance_span: stress imezidi. Sina mood ya kitu." → conversation_turn; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Niko down sana, stress imezidi" → conversation_turn; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Je, umewahi kuwa na mawazo ya kujidhuru?" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.054, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.97, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
