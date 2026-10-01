# Review card — KISWA-STORY-01
Package `MRP-KISWA-STORY-01-snomed-v1` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `suicidal ideation` in *sense/S5/gloss* — ……ker may be expressing a risk of harm or suicidal ideation.…
> - `suicidal` in *sense/S7/gloss* — …feeling overwhelmed or suicidal…
> - `suicidal` in *sense/S7/rationale* — ……ree weeks, which may indicate a risk of suicidal thoughts or feelings of being overwhelm……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 3 of 3 models proposed a `risk_or_safety` reading (unanimous): **risk_or_safety**.
>
> Grounding: 4 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.80, 0.70, 0.30 — poorly calibrated on small models; weigh the grounding above it.
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
| T2 | qwen2.5:7b | My heart has become heavy since three days ago | My heart has become heavy since three days ago | not run |  |
| T3 | llama3.1:8b | my heart has become heavy since three weeks | I've been feeling weighed down by my heart for three weeks now | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **cognitive_process**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C3 | risk_or_safety | risk_or_safety | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | worry | cognitive_process | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sadness): The speaker expresses a feeling of sadness or dejection. — *The phrase 'sijambo' (I am not well) suggests a general feeling of unhappiness or distress. The subsequent statement about the heart being heavy reinforces this sense of sadness.* — evidence: utterance_span: “Sijambo”
- **S2** (gemma3:12b, worry): The speaker is experiencing worry or anxiety related to an unspecified issue. — *A heavy heart can be a metaphorical expression of worry or anxiety. The phrase 'tangu majuma matatu' (for three weeks) indicates a prolonged period of distress, suggesting a potential source of worry.* — evidence: utterance_span: “moyo wangu umekuwa mzito tangu majuma matatu”; context_field: “current”
- **S3** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a degree of distress that warrants concern for their well-being. — *While 'moyo wangu umekuwa mzito' may be a figurative expression, the speaker's self-reported state of not being well ('sijambo') and the duration of the distress ('three weeks') raise concerns. It is essential to consider the possibility that this is a statement of distress that requires further assessment, even if the phrasing is hyperbolic.* — evidence: utterance_span: “Sijambo”; utterance_span: “moyo wangu umekuwa mzito tangu majuma matatu”
- **S4** (qwen2.5:7b, sadness): The speaker feels sad or down. — *The speaker uses the phrase 'moyo wangu umekuwa mzito', which directly translates to 'my heart has become heavy', indicating a feeling of sadness or being down.* — evidence: utterance_span: “moyo wangu umekuwa mzito”
- **S5** (qwen2.5:7b, risk_or_safety): The speaker may be expressing a risk of harm or suicidal ideation. — *The phrase 'moyo wangu umekuwa mzito' could be hyperbolic or idiomatic, but given the context of a home visit and the speaker's self-report of feeling 'heavy', it is prudent to consider the possibility of underlying risk or safety concerns.* — evidence: utterance_span: “moyo wangu umekuwa mzito”
- **S6** (llama3.1:8b, sadness): feeling a heavy heart — *The speaker uses the word 'mzito' to describe their heart, which is a common metaphor for feeling sad or weighed down.* — evidence: utterance_span: “moyo wangu umekuwa mzito”
- **S7** (llama3.1:8b, risk_or_safety): feeling overwhelmed or suicidal — *The speaker's heart has been heavy for three weeks, which may indicate a risk of suicidal thoughts or feelings of being overwhelmed.* — evidence: utterance_span: “moyo wangu umekuwa mzito tangu majuma matatu”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []; `SCTID:72323006` Saddle-billed stork []; `SCTID:1187255000` Paresthesia of saddle area (finding) []; `SCTID:112081003` Sadistic torture []; `SCTID:1157202002` Reduced level of persistent sadness []
- **C3**: `SCTID:22071000175105` Behavior poses safety risk to staff (finding) [] — **no adequate match** per qwen2.5:7b
- **C2**: `MFOEM:000171` worry [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000168` concern [qwen2.5:7b→skos:broadMatch]; `MFOMD:0000184` nervousness [qwen2.5:7b→skos:relatedMatch]; `SCTID:225639004` Worried about not coping with baby []; `SCTID:225640002` Worried about being a bad father []; `SCTID:225641003` Worried about being a bad mother []; `SCTID:225978002` Allowing time to listen to worries []

### Signals
- Risk flags: back_translation_disabled, multiple_components_in_utterance, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.983, 'translation_agreement': 0.237, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.914, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
