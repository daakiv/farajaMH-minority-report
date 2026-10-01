# Review card — KISWA-STORY-06
Package `MRP-KISWA-STORY-06-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S6/gloss* — …the speaker may be considering self-harm or harm to others due to their distress……
> - `self-harm` in *sense/S6/rationale* — ……l pain, which could potentially lead to self-harm or harm to others.…
> - `nife` in *gap_note/C5* — ……disorder or a specific physiological manifestation (facial expression, voice) or dr……
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
| T1 | gemma3:12b | this is new | This is new, since my husband left. | not run | The phrase 'hii ni mpya' literally means 'this is new'. In this context, it indicates a recent and significant emotional shift or experience related to the husband's departure. It doesn't necessarily mean something is literally new, but rather that the speaker's feelings are a recent development. |
| T2 | qwen2.5:7b | This is new. Since my father started to forget. | This is new. Since my father started forgetting. | not run |  |
| T3 | llama3.1:8b | This is new | This is all new to me | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **social_or_relational**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | novelty | emotional_state | minority | gemma3:12b |
| C2 | loss | social_or_relational | minority | gemma3:12b |
| C4 | new | emotional_state | minority | qwen2.5:7b |
| C5 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, novelty): The speaker is describing a situation or feeling as new or unfamiliar. — *The phrase 'hii ni mpya' directly translates to 'this is new'. The context of a home visit and discussion about daily work suggests the speaker is experiencing something new related to their circumstances.* — evidence: utterance_span: “hii ni mpya”
- **S2** (gemma3:12b, loss): The speaker is experiencing a sense of disorientation and change following a loss, specifically the departure of their husband. — *The phrase 'tangu mume wangu aondoke' ('since my husband left') indicates a temporal connection between the newness and the husband's departure. This suggests the speaker's experience is shaped by this loss.* — evidence: utterance_span: “Tangu mume wangu aondoke”
- **S3** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a significant change in their life following their husband's departure, which could indicate distress or vulnerability and warrants consideration for safety. — *The phrase 'hii ni mpya' following 'Tangu mume wangu aondoke' suggests a significant life change that may be associated with distress or vulnerability. While the phrasing may be idiomatic, it's crucial to consider the potential for underlying risk.* — evidence: utterance_span: “hii ni mpya”
- **S4** (qwen2.5:7b, new): This is a recent development. — *The speaker is affirming that this is new, and the context supports a current, self-reported state.* — evidence: utterance_span: “hii ni mpya”
- **S5** (llama3.1:8b, sadness): Feeling unhappy or sorrowful due to a recent event. — *The speaker mentions their husband leaving, which is likely the cause of their sadness.* — evidence: utterance_span: “hii ni mpya”
- **S6** (llama3.1:8b, risk_or_safety): The speaker may be considering self-harm or harm to others due to their distress. — *The speaker's statement may be an expression of their emotional pain, which could potentially lead to self-harm or harm to others.* — evidence: utterance_span: “hii ni mpya”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000033` interest [llama3.1:8b→skos:broadMatch]; `MFOMD:0000083` orgasmic disorder [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C2**: `MFOEM:000106` appraisal of loss [gemma3:12b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000030` despair []; `MFOEM:000016` grief []; `MFOEM:000056` sadness []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000011` full-blown manic mood episode []; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000099` cataplexy []; `MFOMD:0000141` REM sleep behaviour disorder []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000162` akinesia [] — **no adequate match** per qwen2.5:7b
- **C4**: `MFOMD:0000053` process addiction []; `MFOMD:0000076` dissociative fugue []; `MFOMD:0000084` sexual pain disorder []; `MFOMD:0000153` caffeine intoxication [llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C5**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.983, 'translation_agreement': 0.217, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.97, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
