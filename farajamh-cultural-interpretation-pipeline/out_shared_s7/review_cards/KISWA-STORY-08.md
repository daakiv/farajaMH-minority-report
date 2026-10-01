# Review card — KISWA-STORY-08
Package `MRP-KISWA-STORY-08-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *gap_note/C4* — ……ion or a mixed episode) or a specific manifestation (like a facial expression or voi……
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
> Self-reported plausibility for these senses: 0.50, 0.40 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Sijui. Labda ni kweli. Lakini pia nachoka tu.
**Expression:** nachoka tu
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Sijui. Labda ni kweli. Lakini pia nachoka tu.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I feel/become just tired | I'm just feeling worn out. | not run | The phrase 'nachoka tu' is commonly used to express a general feeling of exhaustion, overwhelm, or being emotionally drained. It doesn't necessarily imply a clinical condition, but rather a state of being depleted. The 'tu' emphasizes the simplicity and immediacy of the feeling. |
| T2 | qwen2.5:7b | I am confused. It is true. But also my heart hurts a lot. | I am confused. It is true. But also my heart is hurting a lot. | not run |  |
| T3 | llama3.1:8b | I don't know. Maybe it's true. But I am tired only. | I'm not sure, but I'm exhausted. | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **somatic_experience**: 2/3 models (gemma3:12b, llama3.1:8b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | exhaustion | somatic_experience | majority | gemma3:12b, llama3.1:8b |
| C2 | emotional_pain | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C4 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, exhaustion): The speaker is expressing a feeling of being worn out or depleted. — *The translation 'I'm just feeling worn out' directly reflects the phrase 'nachoka tu'.* — evidence: translation_candidate: “I'm just feeling worn out.”
- **S2** (gemma3:12b, emotional_pain): The speaker is experiencing emotional distress, possibly related to the family's concerns and the suggestion to visit a traditional healer. — *The translation 'my heart is hurting a lot' suggests emotional pain, which could be linked to the situation described in the conversation.* — evidence: translation_candidate: “my heart is hurting a lot.”
- **S3** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially idiomatic, expresses a desire to escape or disengage from their current situation, which warrants consideration for risk and safety. — *The phrase 'nachoka tu' could be a hyperbolic expression of feeling overwhelmed and wanting to leave, even if not a literal statement of intent to harm oneself or others. The family's suggestion to see a traditional healer indicates a potential concern about the speaker's well-being.* — evidence: utterance_span: “nachoka tu”
- **S4** (qwen2.5:7b, heart_hurting): The speaker is experiencing emotional distress, likely related to their heart feeling hurt. — *The phrase 'nachoka tu' directly translates to 'my heart is hurting a lot,' indicating emotional distress.* — evidence: utterance_span: “nachoka tu”
- **S5** (llama3.1:8b, sadness): feeling a strong sense of sorrow or emotional pain — *The word 'nachoka' is a verb that means 'to feel sorrow' or 'to be sad', and the phrase 'tu' is an intensifier that emphasizes the extent of the feeling.* — evidence: model_background_knowledge: “”
- **S6** (llama3.1:8b, exhaustion): feeling extremely tired or drained of energy — *The word 'nachoka' can also mean 'to feel worn out' or 'to be exhausted', and the phrase 'tu' emphasizes the extent of the feeling.* — evidence: model_background_knowledge: “”
- **S7** (llama3.1:8b, risk_or_safety): expressing a desire to end one's life or harm oneself — *The phrase 'nachoka tu' may be idiomatic or hyperbolic, but it could also be interpreted as an expression of a desire to end one's life or harm oneself, given the speaker's emotional state and the context of the conversation.* — evidence: utterance_span: “nachoka tu”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000112` feeling exhausted [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]
- **C2**: `MFOEM:000203` feeling of pain []; `MFOEM:000194` valence []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.056, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.975, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
