# Review card — KISWA-STORY-08
Package `MRP-KISWA-STORY-08-indep-solo` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *gap_note/C4* — ……or a mixed episode), a physiological manifestation (facial expression or voice), or……
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
> Self-reported plausibility for these senses: 0.60, 0.60 — poorly calibrated on small models; weigh the grounding above it.
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
| T1 | gemma3:12b | I feel/become just tired | I'm just feeling worn out. | not run | The phrase 'nachoka tu' is commonly used to express a general feeling of exhaustion, discouragement, or being overwhelmed. It doesn't necessarily imply a clinical state of fatigue, but rather a sense of being depleted. The 'tu' emphasizes the simplicity and immediacy of the feeling. |
| T2 | qwen2.5:7b | I am confused. It is true. But also my heart is heavy too. | I am confused. It is true, but my heart is heavy too. | not run | uncertain |
| T3 | llama3.1:8b | I don't know. Maybe it's true. But I am tired only. | I'm not sure, but I'm exhausted. | not run |  |

### How the models read it, by category (labels aside)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **emotional_state**: 2/3 models (llama3.1:8b, qwen2.5:7b)
- **somatic_experience**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | weariness | somatic_experience | minority | gemma3:12b |
| C3 | uncertainty | emotional_state | minority | qwen2.5:7b |
| C4 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, weariness): The speaker feels tired or exhausted. — *The phrase 'nachoka tu' literally translates to 'I am tired' or 'I am getting tired'. The context of a home visit and discussion about health suggests a possible physical or emotional exhaustion.* — evidence: utterance_span: “nachoka tu”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, even if seemingly casual, expresses a desire to exit or be free from a difficult situation, and warrants consideration as a potential expression of distress. — *The phrase 'nachoka tu' could be a hyperbolic expression of wanting to escape a situation, even if not a literal statement of intent to harm oneself. The preceding conversation about being 'rogwa' (cursed) and being sent to a traditional healer suggests a stressful situation. It may be idiomatic, but the potential for underlying distress necessitates a risk assessment.* — evidence: utterance_span: “nachoka tu”
- **S3** (qwen2.5:7b, uncertainty): Expressing a lack of certainty or confusion about one's feelings or situation. — *The speaker uses 'sijui' (I don't know) and 'nachoka tu' (I'm not sure), indicating uncertainty.* — evidence: utterance_span: “nachoka tu”
- **S4** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker says 'Sijui' (I don't know) and then 'Labda ni kweli' (maybe it's true), which suggests a sense of uncertainty or doubt. The phrase 'nachoka tu' (I'm just fed up) implies a feeling of frustration or sadness.* — evidence: utterance_span: “nachoka tu”
- **S5** (llama3.1:8b, risk_or_safety): expressing a desire to leave or exit the world — *The speaker mentions being 'roga' (tired) and considering going to a 'mganga' (traditional healer), which may imply a sense of desperation or hopelessness. The phrase 'nachoka tu' could be interpreted as a desire to leave or exit the current situation.* — evidence: conversation_turn: “Wanasema nimerogwa”; utterance_span: “nachoka tu”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000170` dubious []; `MFOEM:000173` confusion [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]
- **C4**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output repaired in 1 place(s): llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Wanasema nimerogwa" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.056, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.961, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
