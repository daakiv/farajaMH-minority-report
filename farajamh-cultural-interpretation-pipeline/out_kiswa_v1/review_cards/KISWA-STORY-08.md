# Review card — KISWA-STORY-08
Package `MRP-KISWA-STORY-08-kiswa-story-v1` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S5/gloss* — …considering self-harm or suicide…
> - `suicide` in *sense/S5/gloss* — …considering self-harm or suicide…
> - `suicidal` in *sense/S5/rationale* — ……ould be a sign of emotional distress or suicidal thoughts.…
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Sijui. Labda ni kweli. Lakini pia nachoka tu.
**Expression:** nachoka tu
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Sijui. Labda ni kweli. Lakini pia nachoka tu.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I feel/become just tired | I'm just feeling worn out. | not run | The phrase 'nachoka tu' is commonly used to express a general feeling of exhaustion, discouragement, or being overwhelmed. It doesn't necessarily imply a clinical state of fatigue, but rather a sense of being depleted. The 'tu' emphasizes the simplicity and immediacy of the feeling. |
| T2 | qwen2.5:7b | I am confused. It is true. But also my heart is heavy too. | I am confused. It is true, but my heart is heavy too. | not run | uncertain |
| T3 | llama3.1:8b | I don't know. Maybe it's true. But I am tired only. | I'm not sure, but I'm exhausted. | not run |  |

### How the models read it, by category (labels aside)
- **somatic_experience**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | exhaustion | somatic_experience | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, exhaustion): The speaker is expressing a feeling of being worn out or depleted. — *The translation 'I'm just feeling worn out' directly reflects the meaning of 'nachoka tu'.* — evidence: utterance_span: “nachoka tu”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, even if expressed idiomatically or hyperbolically, may indicate a desire to escape a difficult situation or a feeling of being overwhelmed. — *The phrase 'nachoka tu' could be a way of expressing a desire to escape a difficult situation, even if the speaker doesn't intend to act on it. The family's recommendation to see a traditional healer suggests a potentially serious underlying issue.* — evidence: utterance_span: “nachoka tu”
- **S3** (qwen2.5:7b, exhaustion): The speaker feels extremely tired and worn out. — *The speaker uses the phrase 'nachoka tu' which directly translates to feeling worn out or exhausted.* — evidence: utterance_span: “nachoka tu”
- **S4** (llama3.1:8b, exhaustion): feeling worn out — *The word 'nachoka' is translated as 'exhausted' or 'worn out', which suggests a physical or emotional state of fatigue.* — evidence: translation_candidate: “I'm just feeling worn out.”
- **S5** (llama3.1:8b, risk_or_safety): considering self-harm or suicide — *The speaker mentions being 'nimerogwa', which is translated as 'exhausted' or 'worn out', and is also told to go see a traditional healer. This could be a sign of emotional distress or suicidal thoughts.* — evidence: utterance_span: “Wanasema nimerogwa.”; utterance_span: “Shangazi ameniambia niende kwa mganga.”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000112` feeling exhausted [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.917, 'translation_agreement': 0.056, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.971, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
