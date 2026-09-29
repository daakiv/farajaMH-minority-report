# Review card — PILOT-P01
Package `MRP-PILOT-P01-batch-01` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `suicidal ideation` in *sense/S3/rationale* — ……onsider the possibility of self-harm or suicidal ideation, even if the phrasing is idiomatic or h……
> - `self-harm` in *sense/S3/rationale* — ……mportant to consider the possibility of self-harm or suicidal ideation, even if the phras……
> - `suicidal ideation` in *sense/S5/gloss* — ……ker may be expressing a risk of harm or suicidal ideation due to the use of 'roho yangu imeondoka……
> - `suicidal ideation` in *sense/S5/rationale* — ……spirit has left, which can be a sign of suicidal ideation. the speaker's self-attribution and cur……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Tangu msiba ule, roho yangu imeondoka.
**Expression:** roho yangu imeondoka
**Context:** KE/KE-coast, dialect Kiamu, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Tangu msiba ule, roho yangu imeondoka.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Since disaster that, soul my has departed. | Ever since that tragedy, my spirit has left me. | not run | The phrase 'roho yangu imeondoka' suggests a profound emotional impact following a loss. It doesn't necessarily imply a clinical condition, but rather a feeling of being fundamentally changed or emptied by the experience. |
| T2 | qwen2.5:7b | My heart is heavy today | I am feeling very sad today | not run |  |
| T3 | llama3.1:8b | Since the grief, my spirit has gone out. | Since the grief, I've lost my spirit. | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **somatic_experience**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C3 | risk_or_safety | risk_or_safety | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | loss | somatic_experience | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sadness): The speaker is experiencing a profound sense of sadness following a tragedy. — *The translation 'I am feeling very sad today' suggests a state of sadness. The phrase 'roho yangu imeondoka' can be interpreted metaphorically as a loss of vitality or spirit, which is often associated with sadness and grief.* — evidence: translation_candidate: “I am feeling very sad today”
- **S2** (gemma3:12b, loss): The speaker feels as though a vital part of themselves, their spirit, has departed. — *The phrase 'roho yangu imeondoka' literally translates to 'my spirit has left me,' suggesting a sense of loss or departure of something essential.* — evidence: utterance_span: “roho yangu imeondoka”
- **S3** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially hyperbolic, expresses a deep sense of distress that warrants concern for their well-being; it may reflect a desire to escape overwhelming emotional pain. — *The phrasing 'my spirit has left me' could be a metaphorical expression of a desire to escape a difficult situation or a feeling of being overwhelmed. It is important to consider the possibility of self-harm or suicidal ideation, even if the phrasing is idiomatic or hyperbolic.* — evidence: utterance_span: “roho yangu imeondoka”
- **S4** (qwen2.5:7b, sadness): The speaker feels very sad since the tragedy. — *The speaker uses the term 'roho' (spirit) to indicate a state of being, and 'imeondoka' (has left) suggests a sense of loss, which aligns with sadness.* — evidence: utterance_span: “roho yangu imeondoka”
- **S5** (qwen2.5:7b, risk_or_safety): The speaker may be expressing a risk of harm or suicidal ideation due to the use of 'roho yangu imeondoka', which can be interpreted metaphorically as feeling like one's spirit has left, indicating a desire to end one's life. — *The phrase 'roho yangu imeondoka' can be interpreted metaphorically as feeling like one's spirit has left, which can be a sign of suicidal ideation. The speaker's self-attribution and current state make this interpretation plausible.* — evidence: utterance_span: “roho yangu imeondoka”
- **S6** (llama3.1:8b, sadness): feeling sad or grief-stricken — *The speaker mentions a 'msiba ule' (tragedy) and says their 'roho yangu' (spirit) has left them, suggesting a strong emotional response to the event.* — evidence: utterance_span: “roho yangu imeondoka”
- **S7** (llama3.1:8b, risk_or_safety): expressing a desire to leave or exit the world — *The speaker says their 'roho yangu' (spirit) has left them, which may be an idiomatic expression of feeling overwhelmed or wanting to escape their current situation.* — evidence: utterance_span: “roho yangu imeondoka”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: `MFOEM:000106` appraisal of loss []; `MFOEM:000030` despair [qwen2.5:7b→skos:broadMatch]; `MFOEM:000016` grief [llama3.1:8b→skos:broadMatch]; `MFOEM:000056` sadness [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, multiple_components_in_utterance, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.983, 'translation_agreement': 0.083, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.914, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
