# Review card — KISWA-STORY-10
Package `MRP-KISWA-STORY-10-snomed-v1` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 1 from the surrounding conversation or a translation, not from this utterance; 1 sense resting only on model background knowledge.
>
> Self-reported plausibility for these senses: 0.80, 0.60 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Niko down sana, stress imezidi. Sina mood ya kitu.
**Expression:** Niko down sana
**Context:** KE/KE-western, dialect Sheng, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Niko down sana, stress imezidi. Sina mood ya kitu.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I am down very, stress has exceeded. I have mood of nothing. | I'm really feeling low, the stress has gotten too much. I don't feel like doing anything. | not run |  |
| T2 | qwen2.5:7b | I am very sad, my heart is heavy. | I am feeling very sad. | not run |  |
| T3 | llama3.1:8b | I am down very much | I'm feeling really down, overwhelmed with stress | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **cognitive_process**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C2 | stress | cognitive_process | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sadness): The speaker is expressing a state of sadness or unhappiness. — *The phrase 'Niko down sana' is commonly used to express feelings of sadness or being low. The translation 'I'm really feeling low' supports this interpretation.* — evidence: utterance_span: “Niko down sana”
- **S2** (gemma3:12b, stress): The speaker is experiencing a significant level of stress. — *The phrase 'stress imezidi' directly indicates that the speaker's stress levels have increased.* — evidence: utterance_span: “stress imezidi”
- **S3** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially hyperbolic, expresses a desire to avoid interaction and a feeling of being overwhelmed, which warrants consideration for risk and safety. — *The combination of feeling 'down' and withdrawing from social contact ('Sitaki kuona mtu') could indicate a more serious underlying issue. While 'Niko down sana' may be idiomatic, the overall context suggests a need for assessment. It is important to consider whether this is a literal statement of risk or an expression of distress.* — evidence: conversation_turn: “Sitaki kuona mtu”
- **S4** (qwen2.5:7b, sadness): The speaker is feeling very sad and down. — *The speaker uses the phrase 'Niko down sana' which directly translates to 'I am feeling really down', indicating a state of sadness.* — evidence: utterance_span: “Niko down sana”
- **S5** (llama3.1:8b, sadness): feeling very sad or depressed — *The speaker says 'Niko down sana', which translates to 'I'm really feeling low' or 'I'm feeling very sad'. This suggests a strong emotional state of sadness.* — evidence: translation_candidate: “I'm really feeling low”
- **S6** (llama3.1:8b, risk_or_safety): expressing a desire to escape or withdraw from the world due to emotional distress — *The speaker says 'Niko down sana' and 'Sina mood ya kitu', which translates to 'I'm really feeling low' and 'I don't feel like doing anything'. This may be an expression of a desire to escape or withdraw from the world due to emotional distress.* — evidence: model_background_knowledge: “Niko down sana, Sina mood ya kitu”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [llama3.1:8b→skos:broadMatch]; `SCTID:72323006` Saddle-billed stork []; `SCTID:1187255000` Paresthesia of saddle area (finding) []; `SCTID:112081003` Sadistic torture []; `SCTID:1157202002` Reduced level of persistent sadness []
- **C3**: `SCTID:22071000175105` Behavior poses safety risk to staff (finding) [] — **no adequate match** per qwen2.5:7b
- **C2**: `MFOEM:000029` stress (emotion) [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch]; `MFOMD:0000152` chronic stress [llama3.1:8b→skos:broadMatch]; `MFOMD:0000076` dissociative fugue []; `MFOMD:0000081` sexual desire disorder []; `MFOMD:0000135` suicide []; `MFOMD:0000147` nightmare []; `MFOMD:0000167` defense mechanism []; `SCTID:262188008` Stress []; `SCTID:73595000` Stress []; `SCTID:162218007` Stress-related problem []; `SCTID:413101007` Stress-induced epilepsy []

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 2 place(s): gemma3:12b/normalise language_id="['sw', 'en']" → sw; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Niko down sana, Sina mood ya kitu" → model_background_knowledge
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.077, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.921, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
