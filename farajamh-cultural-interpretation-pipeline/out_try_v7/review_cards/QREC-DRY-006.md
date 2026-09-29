# Review card — QREC-DRY-006
Package `MRP-QREC-DRY-006-qrec-dryrun-v7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `leave the world` in *sense/S7/gloss* — …expressing a desire to exit or leave the world due to overwhelming worry…
> - `leave the world` in *sense/S7/rationale* — ……g', which may imply a desire to exit or leave the world due to overwhelming worry.…
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** I worry about everything
**Expression:** I worry about everything
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Ninawajali kila kitu` (language sw)
- edit: `I` → `Ninawajali` (asr_correction) Assuming 'I worry' is intended to be 'Ninawajali' (I care/worry).
- edit: `everything` → `kila kitu` (asr_correction) Assuming 'everything' is intended to be 'kila kitu' (every thing)

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I-care every thing | I care about everything. | not run | The utterance is straightforward and doesn't contain culturally specific terms requiring explanation. It expresses a feeling of being overwhelmed or deeply concerned. |
| T2 | qwen2.5:7b | I have lost everything | I have lost everything | not run |  |
| T3 | llama3.1:8b | I am tired of everything | I'm fed up with everything | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | worry | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C4 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C2 | loss | emotional_state | minority | gemma3:12b |
| C3 | frustration | emotional_state | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, worry): The speaker expresses a general feeling of anxiety and concern about all aspects of life. — *The utterance 'Ninawajali kila kitu' directly translates to 'I care about everything,' which, in this context following a clinician's question about worrying, suggests a pervasive sense of worry.* — evidence: utterance_span: “Ninawajali kila kitu”
- **S2** (gemma3:12b, loss): The speaker feels as though they have lost everything, expressing a sense of despair and overwhelm. — *One of the proposed translations suggests a sense of loss, which could be a metaphorical expression of feeling overwhelmed by worries. The phrase 'kila kitu' (everything) could imply a complete sense of depletion.* — evidence: translation_candidate: “I have lost everything”
- **S3** (gemma3:12b, frustration): The speaker is feeling fed up and exasperated with the situation. — *Another proposed translation suggests frustration and being fed up, which could be a reaction to feeling overwhelmed by worries. The phrase 'kila kitu' (everything) could imply a complete sense of depletion.* — evidence: translation_candidate: “I'm fed up with everything”
- **S4** (gemma3:12b, risk_or_safety): The speaker's expression, while potentially idiomatic, indicates a level of distress that warrants consideration for risk, as they express concern about 'everything'. — *Even if the phrase 'Ninawajali kila kitu' is a hyperbolic expression of worry, the fact that the speaker is reporting worrying about 'everything' in response to a clinician's question raises a potential safety concern. The phrasing may be idiomatic, but it is not possible to rule out the possibility of a statement of intent.* — evidence: utterance_span: “Ninawajali kila kitu”
- **S5** (qwen2.5:7b, worry): I am concerned about various matters. — *The speaker is directly stating their state of being concerned about different things.* — evidence: utterance_span: “Ninawajali kila kitu”
- **S6** (llama3.1:8b, worry): feeling anxious or apprehensive about many things — *The speaker is responding to a question about being bothered by worrying too much about different things, and the utterance uses the verb 'ninawajali' which means 'to worry' or 'to be anxious about'.* — evidence: conversation_turn: “Worrying too much about different things”
- **S7** (llama3.1:8b, risk_or_safety): expressing a desire to exit or leave the world due to overwhelming worry — *The speaker's utterance may be idiomatic or hyperbolic, but it contains language that could be interpreted as a statement of risk, such as 'I worry about everything', which may imply a desire to exit or leave the world due to overwhelming worry.* — evidence: utterance_span: “Ninawajali kila kitu”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000171` worry [qwen2.5:7b→skos:broadMatch]; `MFOEM:000168` concern [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: `MFOEM:000106` appraisal of loss [gemma3:12b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000030` despair [qwen2.5:7b→skos:broadMatch]; `MFOEM:000016` grief []; `MFOEM:000056` sadness []
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 1.0, 'translation_agreement': 0.206, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.921, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
