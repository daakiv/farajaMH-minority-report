# Review card — QREC-DRY-014
Package `MRP-QREC-DRY-014-qrec-dryrun-v7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/rationale* — ……mportant to consider the possibility of self-harm or other risks.…
> - `self-harm` in *gap_note/C2* — ……bes a complex state involving potential self-harm or reluctance to seek help, possibly ex……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** No, I dont need to talk to anyone
**Expression:** No, I dont need to talk to anyone
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Hapana, sielewi lazima niongee na mtu yeyote` (language sw)
- edit: `No,` → `Hapana,` (orthographic) 
- edit: `I dont` → `sielewi` (orthographic) 
- edit: `need` → `lazima` (orthographic) 
- edit: `to talk` → `niongee` (orthographic) 
- edit: `to anyone` → `na mtu yeyote` (orthographic) 

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | No, I-don't-understand must I-speak with person any | No, I don't understand; I absolutely have to talk to someone. | not run | The phrase 'lazima niongee na mtu yeyote' expresses a strong compulsion or need to speak with someone, not necessarily a request. It implies a feeling of being unable to cope without that interaction. |
| T2 | qwen2.5:7b | No, souls must not see everyone | No, my soul must not see everyone | not run | uncertain |
| T3 | llama3.1:8b | No, I don't understand that I must be killed by anyone | I don't understand why I have to be hurt by anyone | not run |  |

### How the models read it, by category (labels aside)
- **risk_or_safety**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **emotional_state**: 2/3 models (gemma3:12b, qwen2.5:7b)
- **social_or_relational**: 1/3 models (llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C1 | rejection | emotional_state | minority | gemma3:12b |
| C3 | sadness | emotional_state | minority | qwen2.5:7b |
| C4 | social_isolation | social_or_relational | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, rejection): The speaker is refusing to engage in a conversation or seek help. — *The utterance 'Hapana, sielewi lazima niongee na mtu yeyote' directly expresses a refusal to talk to anyone. The negation 'Hapana' and the phrase 'sielewi lazima' (I don't need to) reinforce this rejection.* — evidence: utterance_span: “Hapana, sielewi lazima niongee na mtu yeyote”
- **S2** (gemma3:12b, risk_or_safety): The speaker's refusal to talk to anyone may indicate a risk of harm to themselves or others, or a reluctance to seek help for a serious problem; this may be hyperbolic. — *While the phrasing may be idiomatic or hyperbolic, a refusal to talk to anyone, especially when prompted by a clinician, can be a sign of distress or a barrier to receiving necessary support. It is important to consider the possibility of self-harm or other risks.* — evidence: utterance_span: “Hapana, sielewi lazima niongee na mtu yeyote”
- **S3** (qwen2.5:7b, sadness): The speaker feels sad and does not want to engage with others. — *The speaker is negating the need to talk to anyone, which could indicate a desire to avoid social interaction, often associated with sadness.* — evidence: utterance_span: “Hapana, sielewi lazima niongee na mtu yeyote”
- **S4** (qwen2.5:7b, risk_or_safety): The speaker may be expressing a sense of wanting to avoid social interaction due to feeling unsafe or at risk. — *While the phrasing is not explicitly about dying or harming oneself, the context of a clinical setting and the negation of social interaction could indicate a risk of social withdrawal or avoidance, which may be related to feeling unsafe.* — evidence: utterance_span: “Hapana, sielewi lazima niongee na mtu yeyote”
- **S5** (llama3.1:8b, social_isolation): I don't need to interact with anyone. — *The speaker says 'no' to talking to anyone, indicating a desire for solitude.* — evidence: utterance_span: “Hapana”
- **S6** (llama3.1:8b, risk_or_safety): I may be harmed by talking to someone. — *The speaker's response may be idiomatic, but the phrase 'lazima niongee na mtu yeyote' could imply a risk of harm or injury.* — evidence: utterance_span: “lazima niongee na mtu yeyote”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000025` jealousy [] — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance [] — **no adequate match** per gemma3:12b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.083, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.896, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
