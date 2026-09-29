# Review card — PILOT-P10
Package `MRP-PILOT-P10-batch-01` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `suicidal ideation` in *gap_note/C2* — ……rofound sadness, grief, and potentially suicidal ideation, while acknowledging the cultural conte……
> - `nife` in *gap_note/C3* — ……sadness as an emotion or its outward manifestations (facial expression, vocalizatio……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Mama yangu hana raha tangu baba afariki.
**Expression:** hana raha
**Context:** KE/KE-coast, dialect standard, speaker family_member, setting home_visit, negation affirmed, temporality current, experiencer family_member

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Mama yangu hana raha tangu baba afariki.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | mother my has not comfort since father died. | My mother hasn't been well since my father died. | not run |  |
| T2 | qwen2.5:7b | I do not have the strength | I don't have the energy | not run | uncertain |
| T3 | llama3.1:8b | Mother my has happiness not since father died | My mother has been unhappy since my father passed away | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | distress | emotional_state | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, distress): The mother is experiencing a state of suffering or discomfort. — *The phrase 'hana raha' suggests a lack of ease or comfort, indicating distress. The context of the father's death strongly suggests a cause for this distress.* — evidence: utterance_span: “hana raha”
- **S2** (gemma3:12b, risk_or_safety): The mother's distress may be a veiled expression of a desire to end her suffering, or a statement of a wish to be with her deceased husband. — *The phrasing 'hana raha' following the death of a spouse could be a hyperbolic expression of profound grief, potentially hinting at a desire to escape the pain. While likely idiomatic, the possibility of a statement of risk warrants inclusion.* — evidence: utterance_span: “hana raha”; context_field: “family_member”
- **S3** (qwen2.5:7b, sadness): My mother feels sad since my father died. — *The phrase 'hana raha' is translated as 'hasn't been well', which implies a state of distress. Given the context of the father's death, this sense of sadness is highly plausible.* — evidence: utterance_span: “Mama yangu hana raha”
- **S4** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker mentions that their father has died, which is often a cause of sadness and grief.* — evidence: utterance_span: “baba afariki”
- **S5** (llama3.1:8b, risk_or_safety): concern about the speaker's or their mother's well-being — *The speaker's statement may be hyperbolic, but it still expresses concern about their mother's well-being and potential risk to her safety.* — evidence: utterance_span: “hana raha”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance [] — **no adequate match** per gemma3:12b
- **C1**: `MFOEM:000031` crying []; `MFOEM:000052` compassion []; `MFOEM:000055` shame []; `MFOEM:000216` gloomy mood [llama3.1:8b→skos:relatedMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b

### Signals
- Risk flags: back_translation_disabled, experiencer_not_speaker, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.111, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.96, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
