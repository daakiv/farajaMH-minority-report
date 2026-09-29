# Review card — QREC-DRY-010
Package `MRP-QREC-DRY-010-qrec-dryrun-v7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `suicidal ideation` in *sense/S3/gloss* — ……ess may indicate a risk of self-harm or suicidal ideation, even if expressed hyperbolically.…
> - `self-harm` in *sense/S3/gloss* — ……ed, and hopeless may indicate a risk of self-harm or suicidal ideation, even if expressed……
> - `nife` in *gap_note/C1* — ……do not fit, as they describe specific manifestations of sadness rather than the stat……
> - `suicidal ideation` in *gap_note/C3* — ……ially indicating a risk of self-harm or suicidal ideation, even when expressed hyperbolically. |……
> - `self-harm` in *gap_note/C3* — ……eless, potentially indicating a risk of self-harm or suicidal ideation, even when express……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** I feel down, depressed, and hopeless
**Expression:** I feel down, depressed, and hopeless
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Nahisi nimeendea chini, nimeendea unyogovu, na nimeendea bila tumaini.` (language sw)
- edit: `I feel down` → `Nahisi nimeendea chini` (orthographic) Replacing 'I feel down' with a standard Swahili equivalent.
- edit: `depressed` → `niyogovu` (orthographic) Replacing 'depressed' with the Swahili word for depression.
- edit: `hopeless` → `bila tumaini` (orthographic) Replacing 'hopeless' with a standard Swahili equivalent.
- edit: `and` → `na` (orthographic) Replacing 'and' with the Swahili conjunction 'na'.

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I feel I have gone down, I have gone into depression, and I have gone without hope. | I feel like I'm sinking, I'm falling into depression, and I'm going without hope. | not run | The phrase 'Nimeendea' is repeated, which emphasizes the speaker's experience. The precise nuance of 'going' or 'sinking' might vary depending on the speaker's individual expression. |
| T2 | qwen2.5:7b | Yesterday I am sad, I am sad without hope, I am sad without peace. | Yesterday I felt very sad, without hope, and without peace. | not run |  |
| T3 | llama3.1:8b | I am suffering, I have suffered a blow, and I have suffered without hope. | I'm really struggling, I've hit rock bottom, and I've lost all hope. | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **cognitive_process**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | sadness | emotional_state | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C3 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C2 | hopelessness | cognitive_process | minority | gemma3:12b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, sadness): The speaker is experiencing a state of sadness and unhappiness. — *The speaker explicitly states 'Nahisi nimeendea chini' and 'unyogovu' which translate to 'I feel like I'm sinking' and 'depression' respectively, indicating sadness.* — evidence: utterance_span: “Nahisi nimeendea chini”; utterance_span: “unyogovu”
- **S2** (gemma3:12b, hopelessness): The speaker feels a lack of hope for the future. — *The speaker states 'nimeendea bila tumaini,' which translates to 'going without hope,' directly expressing a sense of hopelessness.* — evidence: utterance_span: “nimeendea bila tumaini”
- **S3** (gemma3:12b, risk_or_safety): The speaker's expression of feeling down, depressed, and hopeless may indicate a risk of self-harm or suicidal ideation, even if expressed hyperbolically. — *The phrasing 'down, depressed, and hopeless' can be indicative of severe emotional distress and, potentially, thoughts of harming oneself. It is crucial to consider this a potential risk, regardless of whether the speaker intends a literal statement.* — evidence: utterance_span: “I feel down, depressed, and hopeless”
- **S4** (qwen2.5:7b, sadness): The speaker is experiencing a deep sense of sadness and hopelessness. — *The speaker uses the word 'hopeless' which directly indicates a lack of positive outlook or optimism, a common feature of sadness.* — evidence: utterance_span: “Nahisi nimeendea chini, nimeendea unyogovu, na nimeendea bila tumaini.”
- **S5** (llama3.1:8b, sadness): feeling extremely sad or depressed — *The speaker uses the words 'chini', 'unyogovu', and 'bila tumaini', which are all associated with negative emotions and a lack of hope.* — evidence: utterance_span: “Nahisi nimeendea chini, nimeendea unyogovu, na nimeendea bila tumaini.”
- **S6** (llama3.1:8b, risk_or_safety): expressing a desire to end one's life or be better off gone — *The speaker uses the phrase 'bila tumaini', which can be translated to 'without hope', and the overall tone of the sentence suggests a sense of desperation and hopelessness.* — evidence: utterance_span: “Nahisi nimeendea bila tumaini.”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.933, 'translation_agreement': 0.108, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.921, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
