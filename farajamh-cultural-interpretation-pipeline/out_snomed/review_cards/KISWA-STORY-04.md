# Review card — KISWA-STORY-04
Package `MRP-KISWA-STORY-04-snomed-v1` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 2 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.80, 0.60 — poorly calibrated on small models; weigh the grounding above it.
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
| T1 | gemma3:12b | Thoughts of debt, of children, of work. They fill my head. | I'm overwhelmed with thoughts of debt, my children, and my work. It's all consuming me. | not run | None |
| T2 | qwen2.5:7b | Thoughts of death, of children, of work. They make me feel heavy. | Thinking about death, children, and work makes me feel weighed down. | not run |  |
| T3 | llama3.1:8b | Thoughts of debt, of children, of work. They are shouting at my head. | I'm overwhelmed by worries about my family's financial struggles, my kids, and my job. | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | worry | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | overwhelmed | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, worry): The speaker expresses being overwhelmed by thoughts and worries. — *The phrase 'Mawazo ya...' (thoughts of...) followed by specific concerns (debt, children, work) suggests a state of worry and being overwhelmed. The translation 'I'm overwhelmed...' supports this interpretation.* — evidence: utterance_span: “Mawazo ya deni, ya watoto, ya kazi. Yananijaa kichwani.”
- **S2** (gemma3:12b, risk_or_safety): The speaker's expression of being overwhelmed by worries about debt, children, and work may indicate a risk of harm to themselves or others, or a desire to escape a difficult situation. — *While the phrasing may be idiomatic and hyperbolic, the expression of being 'consumed' by worries about significant life stressors warrants consideration as a potential indicator of risk. The context of sleep difficulty further elevates this concern.* — evidence: utterance_span: “Mawazo ya deni, ya watoto, ya kazi. Yananijaa kichwani.”
- **S3** (qwen2.5:7b, overwhelmed): The speaker feels overwhelmed by various concerns. — *The speaker uses the term 'yananijaa kichwani' which means 'it's all consuming me', indicating a sense of being overwhelmed.* — evidence: utterance_span: “Yananijaa kichwani”
- **S4** (llama3.1:8b, overwhelmed): feeling burdened by too many thoughts or worries — *The speaker mentions being overwhelmed by thoughts of debt, children, and work, which suggests a state of emotional overwhelm.* — evidence: utterance_span: “Yananijaa kichwani”
- **S5** (llama3.1:8b, risk_or_safety): expressing a desire to escape or leave the situation — *The speaker's use of 'yananijaa' may be idiomatic, but the context suggests a desire to escape or leave the situation, which could be interpreted as a risk to the speaker's safety.* — evidence: utterance_span: “Yananijaa kichwani”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000171` worry [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000168` concern [qwen2.5:7b→skos:broadMatch]; `MFOMD:0000184` nervousness []; `SCTID:225639004` Worried about not coping with baby []; `SCTID:225640002` Worried about being a bad father []; `SCTID:225641003` Worried about being a bad mother []; `SCTID:225978002` Allowing time to listen to worries [] — **no adequate match** per gemma3:12b
- **C2**: `SCTID:22071000175105` Behavior poses safety risk to staff (finding) [] — **no adequate match** per qwen2.5:7b
- **C3**: `MFOEM:000027` terror []; `MFOMD:0000076` dissociative fugue [llama3.1:8b→skos:relatedMatch]; `SCTID:700050004` Overwhelming infection in asplenic patient []; `SCTID:718456009` SCORE Index of Family Function and Change 15 Dimension 2 Overwhelmed by Difficulties average score []; `SCTID:720196002` SCORE Index of Family Function and Change 15 Dimension 2 Overwhelmed by Difficulties total score []; `SCTID:720562002` SCORE Index of Family Function and Change 15 Dimension 2 Overwhelmed by Difficulties [] — **no adequate match** per gemma3:12b, qwen2.5:7b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.107, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
