# Review card — KISWA-STORY-06
Package `MRP-KISWA-STORY-06-queryfix-v1` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *gap_note/C4* — ……retrieved concepts focus on specific manifestations of sadness (facial expressions,……
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
| T1 | gemma3:12b | this is new | This is new, since my husband left. | not run | The phrase 'hii ni mpya' literally means 'this is new'. In this context, it implies that the speaker is experiencing a new or recent feeling of distress related to her husband leaving. It doesn't necessarily mean a clinical diagnosis of depression or anxiety, but rather a fresh wave of grief or hardship. |
| T2 | qwen2.5:7b | This is new. Since my father started to forget. | This is new. Since my father started forgetting. | not run |  |
| T3 | llama3.1:8b | This is new | This is all too much for me | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | overwhelm | emotional_state | minority | gemma3:12b |
| C3 | new_situation | emotional_state | minority | qwen2.5:7b |
| C4 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, overwhelm): The speaker is experiencing something new and difficult since their husband left. — *The phrase 'hii ni mpya' literally translates to 'this is new.' Given the context of a home visit and the speaker's previous statement about being unable to farm, 'new' likely refers to a new and overwhelming experience related to their husband's departure.* — evidence: utterance_span: “hii ni mpya”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, may indicate a desire to escape a difficult situation or a feeling of being unable to cope, requiring further assessment for safety. — *While 'hii ni mpya' may be a common expression for something overwhelming, the context of a home visit and the speaker's previous statement about being unable to farm raises a flag for potential distress and a need to assess for safety. The phrasing may be hyperbolic, but it warrants further inquiry.* — evidence: utterance_span: “hii ni mpya”
- **S3** (qwen2.5:7b, new_situation): The speaker is describing a new situation or challenge. — *The speaker uses 'hii ni mpya' (this is new) to introduce a current situation.* — evidence: utterance_span: “La, hii ni mpya. Tangu mume wangu aondoke.”
- **S4** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker mentions their husband leaving, which is often a source of sadness.* — evidence: utterance_span: “hii ni mpya”
- **S5** (llama3.1:8b, risk_or_safety): concern about dying or wanting to die — *The speaker says 'hii ni mpya' and mentions their husband leaving, which may imply a sense of desperation or hopelessness.* — evidence: utterance_span: “hii ni mpya”; context_field: “mume wangu aondoke”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000027` terror []; `MFOMD:0000076` dissociative fugue [llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.095, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.961, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
