# Review card — KISWA-STORY-11
Package `MRP-KISWA-STORY-11-snomed-v1` · priority **high** · backend `live`

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
> - `self-harm` in *sense/S2/rationale* — ……risk. the preceding conversation about self-harm further elevates this concern.…
> - `self-harm` in *gap_note/C2* — ……vers a desire to not be here, potential self-harm ideation, and hyperbolic expressions of……
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
> Self-reported plausibility for these senses: 0.90, 0.70 — poorly calibrated on small models; weigh the grounding above it.
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
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | desire_for_absence | emotional_state | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, desire_for_absence): The speaker expresses a wish or feeling that they would be better off not existing. — *The phrase 'afadhali nisiwepo' directly translates to 'it would be better if I weren't here,' indicating a desire to not be present.* — evidence: utterance_span: “afadhali nisiwepo”
- **S2** (gemma3:12b, risk_or_safety): The speaker expresses a desire to not be here, which may be a hyperbolic expression of distress but requires consideration for potential self-harm ideation. — *The phrasing 'afadhali nisiwepo' expresses a desire to not exist, which, while potentially idiomatic, warrants assessment for risk. The preceding conversation about self-harm further elevates this concern.* — evidence: utterance_span: “afadhali nisiwepo”; conversation_turn: “Je, umewahi kuwa na mawazo ya kujidhuru?”
- **S3** (qwen2.5:7b, sadness): The speaker expresses a sense of sadness and considering not being here. — *The speaker uses the phrase 'afadhali nisiwepo' which suggests a desire not to be present, indicating sadness.* — evidence: utterance_span: “afadhali nisiwepo”
- **S4** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker mentions being 'down sana' and having 'stress imezidi', indicating a negative emotional state.* — evidence: conversation_turn: “Niko down sana, stress imezidi. Sina mood ya kitu.”
- **S5** (llama3.1:8b, risk_or_safety): expressing a desire to end one's life — *The speaker says 'afadhali nisiwepo', which can be translated to 'it would be better if I weren't here', a phrase that may be idiomatic but still expresses a risk to one's safety.* — evidence: utterance_span: “Kuna siku nafikiri afadhali nisiwepo.”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: `SCTID:22071000175105` Behavior poses safety risk to staff (finding) [] — **no adequate match** per qwen2.5:7b
- **C3**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [llama3.1:8b→skos:broadMatch]; `SCTID:72323006` Saddle-billed stork []; `SCTID:1187255000` Paresthesia of saddle area (finding) []; `SCTID:112081003` Sadistic torture []; `SCTID:1157202002` Reduced level of persistent sadness []
- **C1**: `MFOMD:0000081` sexual desire disorder [] — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 1 place(s): llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Niko down sana, stress imezidi. Sina mood ya kitu." → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.983, 'translation_agreement': 0.097, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
