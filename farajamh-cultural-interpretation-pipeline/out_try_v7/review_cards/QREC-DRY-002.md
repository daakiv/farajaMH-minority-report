# Review card — QREC-DRY-002
Package `MRP-QREC-DRY-002-qrec-dryrun-v7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S3/gloss* — ……le indication of distress and potential self-harm or harm to others.…
> - `nife` in *gap_note/C1* — ……t, as they describe specific physical manifestations of sadness, not the emotional s……
> - `self-harm` in *gap_note/C3* — ……elf-doubt, shame, and the potential for self-harm or harm to others, possibly related to……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Yes, I feel bad about myself and I feel that I have let my family down
**Expression:** Yes, I feel bad about myself and I feel that I have let my family down
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Ndio, najisikia vibaya kuhusu mimi mwenyewe na najisikia kwamba nimevichezea wazazi wangu.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Yes, I feel badly about myself and I feel that I have played with my parents. | Yes, I feel bad about myself, and I feel like I've messed with my parents. | not run | The phrase 'nimevichezea wazazi wangu' is culturally complex. It doesn't literally mean 'played games' in the sense of amusement. It suggests a deep disrespect, betrayal, or causing significant distress to one's parents, potentially through actions they disapprove of or that have brought shame upon the family. It's a strong expression of guilt and regret. The degree of severity implied is difficult to ascertain without more context. |
| T2 | qwen2.5:7b | I am sad about myself and I am sad that I want to hurt my parents. | I am feeling sad about myself and I am worried that I might want to hurt my parents. | not run | uncertain |
| T3 | llama3.1:8b | Yes, I feel bad about myself and I feel that I have deceived my parents. | I'm really struggling with myself and I feel like I've let my parents down. | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **social_or_relational**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C2 | disappointment | social_or_relational | minority | gemma3:12b |
| C4 | guilt | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sadness): The speaker expresses a feeling of unhappiness and disappointment regarding themselves. — *The phrase 'najisikia vibaya' directly translates to 'I feel bad', indicating a state of sadness or unhappiness.* — evidence: utterance_span: “najisikia vibaya”
- **S2** (gemma3:12b, disappointment): The speaker expresses regret and disappointment about failing to meet their family's expectations. — *The phrase 'nimevichezea wazazi wangu' suggests a feeling of having disappointed or let down their parents.* — evidence: utterance_span: “nimevichezea wazazi wangu”
- **S3** (gemma3:12b, risk_or_safety): The speaker's expression of feeling bad about themselves and letting their family down, while potentially idiomatic, warrants consideration as a possible indication of distress and potential self-harm or harm to others. — *The phrasing, while potentially hyperbolic, expresses a negative self-perception and a sense of failing family obligations. This could be a veiled expression of distress and a need for safety assessment. The translations include 'hurt my parents', which raises a safety concern.* — evidence: translation_candidate: “I am worried that I might want to hurt my parents.”; utterance_span: “najisikia vibaya kuhusu mimi mwenyewe na najisikia kwamba nimevichezea wazazi wangu”
- **S4** (qwen2.5:7b, sadness): The speaker feels bad about themselves and believes they have let their family down. — *The speaker explicitly states feeling bad about themselves and letting their family down.* — evidence: utterance_span: “najisikia vibaya kuhusu mimi mwenyewe na najisikia kwamba nimevichezea wazazi wangu”
- **S5** (llama3.1:8b, sadness): feeling unhappy or sorrowful about oneself — *The speaker uses the word 'vibaya' which means 'bad' or 'unhappy' in Swahili, indicating a negative emotional state.* — evidence: utterance_span: “najisikia vibaya kuhusu mimi mwenyewe”
- **S6** (llama3.1:8b, guilt): feeling responsible for a wrongdoing or mistake — *The speaker mentions 'nimevichezea wazazi wangu' which means 'I have let my parents down' in Swahili, indicating a sense of guilt or responsibility.* — evidence: utterance_span: “nimevichezea wazazi wangu”
- **S7** (llama3.1:8b, risk_or_safety): expressing a desire to harm oneself or others — *The speaker's statement 'nimevichezea wazazi wangu' could be interpreted as a desire to harm or punish themselves or their parents, which is a risk to their safety.* — evidence: utterance_span: “nimevichezea wazazi wangu”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance [] — **no adequate match** per gemma3:12b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: `MFOEM:000051` disappointment [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]
- **C4**: `MFOEM:000053` guilt [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.9, 'translation_agreement': 0.224, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.921, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
