# Review card — KISWA-STORY-01
Package `MRP-KISWA-STORY-01-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *sense/S3/rationale* — ……hest or heart, which may be a somatic manifestation of emotional distress. while met……
> - `suicidal ideation` in *sense/S5/gloss* — ……ker may be expressing a risk of harm or suicidal ideation.…
> - `suicidal ideation` in *sense/S5/rationale* — ……n, which may indicate a risk of harm or suicidal ideation. the speaker is affirming the statement……
> - `nife` in *gap_note/C1* — ……retrieved concepts focus on specific manifestations of sadness (facial expression,……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 3 of 3 models proposed a `risk_or_safety` reading (unanimous): **risk_or_safety**.
>
> Grounding: 3 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.80, 0.70, 0.00 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Sijambo, lakini moyo wangu umekuwa mzito tangu majuma matatu.
**Expression:** moyo wangu umekuwa mzito
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Sijambo, lakini moyo wangu umekuwa mzito tangu majuma matatu.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I am not well, but my heart has become heavy since three weeks. | I'm not doing well, but my heart has been heavy for three weeks. | not run |  |
| T2 | qwen2.5:7b | My heart has become heavy from three days. | My heart has become heavy these past three days. | not run |  |
| T3 | llama3.1:8b | my heart is heavy every day since three weeks | I've been feeling really down since three weeks | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **somatic_experience**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | risk_or_safety | risk_or_safety | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C3 | somatic_experience | somatic_experience | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sadness): The speaker expresses a feeling of sadness or dejection. — *The phrase 'moyo wangu umekuwa mzito' (my heart has been heavy) is a metaphorical expression often used to convey sadness, grief, or emotional burden. The speaker's initial statement 'Sijambo' (I am not doing well) reinforces this interpretation.* — evidence: utterance_span: “moyo wangu umekuwa mzito”; utterance_span: “Sijambo”
- **S2** (gemma3:12b, risk_or_safety): The speaker's expression of a heavy heart over a prolonged period may indicate underlying distress requiring further assessment; the phrasing may be hyperbolic, but should not be discounted as a statement of risk. — *While 'moyo wangu umekuwa mzito' is likely a metaphorical expression, the speaker's report of this feeling persisting for three weeks warrants consideration as a potential indicator of significant distress. It is crucial to assess the speaker's well-being and rule out any underlying issues, even if the phrasing is hyperbolic.* — evidence: utterance_span: “moyo wangu umekuwa mzito tangu majuma matatu”
- **S3** (gemma3:12b, somatic_experience): The speaker is describing a physical sensation of heaviness in their chest or heart. — *The phrase 'moyo wangu umekuwa mzito' can be interpreted literally as a feeling of heaviness in the chest or heart, which may be a somatic manifestation of emotional distress.  While metaphorical, the speaker may be genuinely experiencing a physical sensation.* — evidence: utterance_span: “moyo wangu umekuwa mzito”
- **S4** (qwen2.5:7b, sadness): The speaker is feeling sad and down. — *The speaker uses the phrase 'moyo wangu umekuwa mzito', which directly translates to 'my heart has become heavy', indicating a state of sadness or dejection.* — evidence: utterance_span: “moyo wangu umekuwa mzito”
- **S5** (qwen2.5:7b, risk_or_safety): The speaker may be expressing a risk of harm or suicidal ideation. — *The phrase 'moyo wangu umekuwa mzito' could be a hyperbolic or idiomatic expression of feeling extremely down, which may indicate a risk of harm or suicidal ideation. The speaker is affirming the statement, making it more likely to be a literal expression of distress.* — evidence: utterance_span: “moyo wangu umekuwa mzito”
- **S6** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker says 'sijambo' which means 'I'm not doing well', and then describes their heart as 'mzito' which means 'heavy'. This suggests a negative emotional state.* — evidence: utterance_span: “Sijambo, lakini moyo wangu umekuwa mzito”
- **S7** (llama3.1:8b, risk_or_safety): expressing a desire to leave or exit the world — *The speaker's heart being 'mzito' could be an idiomatic expression for feeling overwhelmed or wanting to escape their situation. The phrase 'tangu majuma matatu' suggests a prolonged period of distress.* — evidence: utterance_span: “moyo wangu umekuwa mzito tangu majuma matatu”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOMD:0000101` delusion [] — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, multiple_components_in_utterance, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output repaired in 3 place(s): gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.191, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.914, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
