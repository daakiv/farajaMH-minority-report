# Review card — PILOT-P04
Package `MRP-PILOT-P04-batch-01` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/gloss* — ……ed' by thoughts, may indicate a risk of self-harm or a need for immediate support; this p……
> - `nife` in *gap_note/C1* — ……eing limited to a specific behavioral manifestation (like crying) or a specific emot……
> - `self-harm` in *gap_note/C2* — ……tal distress, and the potential risk of self-harm or need for immediate support, possibly……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Mawazo yananichoma kichwa usiku.
**Expression:** Mawazo yananichoma kichwa
**Context:** KE/KE-western, dialect standard, speaker participant, setting chat_platform, negation affirmed, temporality recurrent, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Mawazo yananishoma kichwa usiku.` (language sw)
- edit: `Mawazo yananichoma` → `Mawazo yananishoma` (orthographic) Corrected verb conjugation to standard form 'yananishoma' from 'yananichoma'.

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | Thoughts they-are-piercing head my night. | My thoughts are piercing my head at night. | not run | The verb 'kunashoma' (to pierce) is quite strong and suggests a significant level of distress. It's possible the speaker is experiencing intense anxiety or intrusive thoughts. |
| T2 | qwen2.5:7b | Thoughts stay heavy night | My thoughts are heavy at night | not run |  |
| T3 | llama3.1:8b | Thoughts are hitting the head at night | I have thoughts that are weighing heavily on my mind at night | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 2/3 models (gemma3:12b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **somatic_experience**: 1/3 models (llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C1 | distress | emotional_state | minority | gemma3:12b |
| C3 | thoughts_heavy | emotional_state | minority | qwen2.5:7b |
| C4 | thought burden | somatic_experience | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, distress): The speaker is experiencing significant mental discomfort or anguish. — *The verb 'yananishoma' (piercing/burning) suggests a painful and distressing experience. The phrase describes a recurring event ('usiku' - at night), indicating ongoing suffering.* — evidence: utterance_span: “Mawazo yananishoma kichwa”
- **S2** (gemma3:12b, risk_or_safety): The speaker's description of intense mental distress, potentially involving feelings of being 'burned' or 'pierced' by thoughts, may indicate a risk of self-harm or a need for immediate support; this phrasing may be idiomatic or hyperbolic. — *The phrasing 'burning' or 'piercing' the head, while potentially metaphorical, could also reflect a severe mental state where the speaker is experiencing significant distress and may be at risk. It is crucial to consider this as a potential indicator of harm, regardless of whether the phrasing is intended literally.* — evidence: utterance_span: “Mawazo yananishoma kichwa”
- **S3** (qwen2.5:7b, thoughts_heavy): My thoughts are heavy at night. — *The speaker is affirming the statement, and the context indicates a recurrent, self-reported issue.* — evidence: translation_candidate: “I have thoughts that are weighing heavily on my mind at night”
- **S4** (llama3.1:8b, thought burden): Having thoughts that feel heavy or oppressive at night. — *The word 'yananishoma' is translated to 'piercing' or 'heavy', which suggests a physical or bodily experience.* — evidence: translation_candidate: “My thoughts are piercing my head at night.”
- **S5** (llama3.1:8b, risk_or_safety): Feeling overwhelmed by thoughts to the point of considering harm to oneself. — *The speaker affirms the statement, which may indicate a sense of urgency or desperation.* — evidence: utterance_span: “Mawazo yananishoma kichwa usiku”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C1**: `MFOEM:000031` crying []; `MFOEM:000052` compassion []; `MFOEM:000055` shame []; `MFOEM:000216` gloomy mood [llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.933, 'translation_agreement': 0.34, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.961, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
