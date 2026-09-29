# Review card — QREC-DRY-003
Package `MRP-QREC-DRY-003-qrec-dryrun-v7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *gap_note/C6* — ……ion like sadness, nor on the physical manifestation of sadness (facial expression or……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Yes, I have been Moving or speaking so slowly that other people could have noticed and also being so fidgety or restless
**Expression:** Yes, I have been Moving or speaking so slowly that other people could have noticed and also being so fidgety or restless
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Ndio, nimekuwa nikihama au kuzungumza polepole sana hivi kwamba watu wengine wangekuwa wamegundua na pia kuwa na wasiwasi au kutofurahi.` (language sw)
- edit: `Moving` → `kuhama` (orthographic) Standard Swahili equivalent for 'moving'
- edit: `speaking` → `kuzungumza` (orthographic) Standard Swahili equivalent for 'speaking'
- edit: `so slowly` → `polepole sana hivi` (orthographic) More natural phrasing for 'so slowly'
- edit: `noticed` → `waligundua` (orthographic) Past tense of 'to notice'
- edit: `being so fidgety or restless` → `kuwa na wasiwasi au kutofurahi` (orthographic) Standard Swahili equivalents for 'fidgety or restless'
- edit: `Yes` → `Ndio` (orthographic) Standard Swahili equivalent for 'Yes'

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Yes, I have been moving or speaking very slowly so that other people would have noticed and also being with worry or unhappiness. | Yes, I've been moving and speaking so slowly that other people would have noticed, and I've also been feeling worried and down. | not run |  |
| T2 | qwen2.5:7b | Now, I have been thinking a lot lately because other people seem to be worried and also have thoughts and are anxious. | Now, I've been thinking a lot lately because other people seem to be worried and also have anxious thoughts. | not run |  |
| T3 | llama3.1:8b | Yes, I have been speaking or speaking slowly very much so that others would have noticed and also have worries or be unhappy. | I've been feeling so down that others would have noticed and I'm worried they'll be unhappy too. | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 2/3 models (gemma3:12b, llama3.1:8b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **cognitive_process**: 1/3 models (gemma3:12b)
- **somatic_experience**: 1/3 models (qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | anxiety | emotional_state | minority | gemma3:12b |
| C2 | self-consciousness | cognitive_process | minority | gemma3:12b |
| C4 | slow movement | somatic_experience | minority | qwen2.5:7b |
| C5 | restlessness | somatic_experience | minority | qwen2.5:7b |
| C6 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, anxiety): The speaker describes feeling worried or uneasy, possibly due to their observed behavior. — *The phrase 'kuwa na wasiwasi' directly translates to 'feeling worried' or 'anxious'.* — evidence: utterance_span: “na pia kuwa na wasiwasi au kutofurahi”
- **S2** (gemma3:12b, self-consciousness): The speaker is concerned that their slow movements and restlessness have been noticed by others. — *The phrase 'watu wengine wangekuwa wamegundua' implies the speaker is worried about what others have observed.* — evidence: utterance_span: “wakati watu wengine wangekuwa wamegundua”
- **S3** (gemma3:12b, risk_or_safety): The speaker's description of slow movements and restlessness, combined with the expression of worry, may indicate a potential risk to their safety or well-being, even if expressed hyperbolically. — *While the phrasing may be idiomatic or hyperbolic, the description of physical and emotional distress warrants consideration of potential risk. The clinical context emphasizes assessment of potential harm.* — evidence: conversation_turn: “Over the last two weeks, how often have you been bothered by the following problems?”
- **S4** (qwen2.5:7b, slow movement): Experiencing a significant reduction in physical activity and movement. — *The speaker mentions moving or speaking so slowly that others could have noticed, which directly relates to the clinical question posed by the clinician.* — evidence: utterance_span: “nimekuwa nikihama au kuzungumza polepole sana”
- **S5** (qwen2.5:7b, restlessness): Feeling a strong need to move around or be active, often to the point of being unable to sit still. — *The speaker mentions being so fidgety or restless, which directly corresponds to the clinical question about increased activity.* — evidence: utterance_span: “kuwa na wasiwasi au kutofurahi”
- **S6** (llama3.1:8b, sadness): feeling down or unhappy — *The speaker uses the phrase 'nimekuwa nikihama au kuzungumza polepole sana' which implies a lack of energy or enthusiasm, and 'kutofurahi' which means 'unhappy' or 'sad'.* — evidence: utterance_span: “nimekuwa nikihama au kuzungumza polepole sana”
- **S7** (llama3.1:8b, risk_or_safety): expressing a desire to harm oneself or others — *The speaker's slow movement and speech may be an expression of a desire to withdraw from the world, and the phrase 'wangekuwa wamegundua' implies a concern for how others might perceive them. The phrasing may be idiomatic, but it is not clear if the speaker is expressing a desire to harm themselves or others.* — evidence: utterance_span: “wangekuwa wamegundua”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000028` anxiety [qwen2.5:7b→skos:broadMatch]; `MFOEM:000196` anxious mood [llama3.1:8b→skos:broadMatch]; `MFOEM:000026` fear []; `MFOEM:000124` feeling nervous []; `MFOEM:000025` jealousy [] — **no adequate match** per gemma3:12b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C5**: `MFOEM:000111` feeling restless [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]
- **C6**: `MFOEM:000056` sadness [qwen2.5:7b→skos:exactMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.213, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.976, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
