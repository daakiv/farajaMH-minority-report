# Review card — KISWA-STORY-04
Package `MRP-KISWA-STORY-04-indep-solo-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 2 from the surrounding conversation or a translation, not from this utterance.
>
> Self-reported plausibility for these senses: 0.90, 0.60 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Mawazo ya deni, ya watoto, ya kazi. Yananijaa kichwani.
**Expression:** Yananijaa kichwani
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Mawazo ya deni, ya watoto, ya kazi. Yananijaa kichwani.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Thoughts of debt, of children, of work. They fill my head. | I'm overwhelmed with thoughts of debt, my children, and my work. My head is full. | not run | None |
| T2 | qwen2.5:7b | They make me feel bad, children, work. They make me feel very heavy. | They weigh on me, children, work. They make me feel very heavy. | not run |  |
| T3 | llama3.1:8b | Thoughts of debt, of children, of work. They are screaming in my head. | I'm overwhelmed by worries about my debts, my kids, and my job. It's all weighing on my mind. | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | worry | emotional_state | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, worry): The speaker's head is filled with worries. — *The phrase 'Mawazo ya...' indicates thoughts, and the context reveals these thoughts are causing distress. 'Yananijaa kichwani' suggests being overwhelmed by these thoughts.* — evidence: utterance_span: “Mawazo ya deni, ya watoto, ya kazi. Yananijaa kichwani”
- **S2** (gemma3:12b, risk_or_safety): The speaker's expression, while potentially hyperbolic, conveys a sense of being overwhelmed by responsibilities and anxieties that could lead to harm or distress. — *While 'Yananijaa kichwani' may be a figurative expression of being overwhelmed, the context of sleep deprivation and worry suggests a potential for significant distress. It is important to consider that the speaker may be expressing a feeling of being unable to cope, which could be a risk factor. The phrasing may be idiomatic or hyperbolic.* — evidence: conversation_turn: “Usingizi umenikimbia. Nakesha hadi alfajiri nikiwaza.”
- **S3** (qwen2.5:7b, sadness): Expressing a sense of sadness or dissatisfaction. — *The speaker is affirming a negative state, and the use of 'kichwani' (which can mean 'enough' or 'sufficient') suggests a feeling of dissatisfaction or sadness.* — evidence: utterance_span: “Yananijaa kichwani”
- **S4** (llama3.1:8b, sadness): Feeling unhappy or sorrowful — *The speaker says 'yananijaa kichwani', which can be translated to 'they are nagging me' or 'they are bothering me'. The use of 'kuchwani' implies a sense of annoyance or frustration.* — evidence: utterance_span: “yananijaa kichwani”
- **S5** (llama3.1:8b, risk_or_safety): Feeling overwhelmed or trapped — *The speaker says 'usingizi umenikimbia', which can be translated to 'sleep has run away from me'. This phrase may be idiomatic, but it implies a sense of desperation or feeling overwhelmed.* — evidence: conversation_turn: “usingizi umenikimbia”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode []
- **C1**: `MFOEM:000171` worry [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000168` concern []; `MFOMD:0000184` nervousness [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 1 place(s): llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: usingizi umenikimbia" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.09, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
