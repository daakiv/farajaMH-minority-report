# Review card — QREC-DRY-005
Package `MRP-QREC-DRY-005-qrec-dryrun-v7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `self-harm` in *sense/S2/gloss* — ……l context, may indicate a potential for self-harm or a desire to escape a difficult situa……
> - `nife` in *sense/S2/rationale* — ……metaphor for a desire to escape or a manifestation of distress.…
> - `self-harm` in *gap_note/C2* — ……of physical restlessness and potential self-harm/escape desire, possibly with a hyperbol……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** I have been restless and unable to sit still always
**Expression:** I have been restless and unable to sit still always
**Context:** KE/?, dialect ?, speaker simulated_patient, setting simulation, negation unknown, temporality unknown, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Mimi nimekuwa kimya na hawezi kukaa mtuli bila ya kusimama daima.` (language sw)
- edit: `I` → `Mimi` (orthographic) Replacing English pronoun with Swahili equivalent.
- edit: `have been restless` → `nimekuwa kimya` (orthographic) Replacing 'restless' with 'kimya' which conveys a similar sense of unease.
- edit: `and unable to sit still` → `na hawezi kukaa mtuli` (orthographic) Replacing 'unable to sit still' with 'hawezi kukaa mtuli' (cannot sit calmly).
- edit: `always` → `daima` (orthographic) Replacing 'always' with 'daima' (always).

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | I have been quiet and he/she cannot sit still without of standing always. | I've been quiet, and they can't stay still, they always have to be up and doing. | not run | The pronoun 'hawezi' is ambiguous, potentially referring to a male or female person. The phrase 'kusimama daima' literally means 'to stand always,' but in this context, it conveys a sense of restlessness and constant activity, not necessarily physical standing. |
| T2 | qwen2.5:7b | I am heavy in heart and cannot rise early without thinking always. | I am feeling very down and struggle to get up early every day, always thinking. | not run |  |
| T3 | llama3.1:8b | I have been dull and cannot sit idle without standing always. | I've been feeling really down and can't just sit around without getting up all the time. | not run |  |

### How the models read it, by category (labels aside)
- **somatic_experience**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | restlessness | somatic_experience | unanimous | gemma3:12b, qwen2.5:7b, llama3.1:8b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, restlessness): The speaker describes a persistent inability to remain still. — *The normalised utterance 'hawezi kukaa mtuli bila ya kusimama' directly translates to 'they can't stay still without standing,' indicating a physical restlessness.* — evidence: utterance_span: “hawezi kukaa mtuli bila ya kusimama”
- **S2** (gemma3:12b, risk_or_safety): The speaker's description of being unable to sit still, combined with the clinical context, may indicate a potential for self-harm or a desire to escape a difficult situation; this phrasing may be hyperbolic. — *While the phrasing may be idiomatic, the combination of restlessness and the clinical setting warrants consideration of potential risk. The inability to 'sit still' could be a metaphor for a desire to escape or a manifestation of distress.* — evidence: conversation_turn: “Over the last two weeks, how often have you been bothered by the following problems? Being so restless that it is hard to sit still”
- **S3** (qwen2.5:7b, restlessness): Feeling and acting restless, unable to sit still. — *The speaker describes feeling restless and being unable to sit still, which directly corresponds to the given utterance.* — evidence: utterance_span: “Mimi nimekuwa kimya na hawezi kukaa mtuli bila ya kusimama daima.”
- **S4** (llama3.1:8b, restlessness): Having an excessive urge to move or be active — *The speaker uses the word 'kimya' which can be translated to 'quiet' or 'still', but in this context, it seems to be used to contrast with the speaker's actual state of being restless and unable to sit still.* — evidence: utterance_span: “Mimi nimekuwa kimya na hawezi kukaa mtuli bila ya kusimama daima”
- **S5** (llama3.1:8b, risk_or_safety): Expressing a desire to exit or harm oneself — *The speaker's use of 'bila ya kusimama daima' (without getting up all the time) may be an idiomatic expression, but it could also be interpreted as a statement of intent to harm oneself.* — evidence: conversation_turn: “Being so restless that it is hard to sit still”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000111` feeling restless [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b

### Signals
- Risk flags: back_translation_disabled, context_incomplete, over_medicalisation_risk, polarity_unknown, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.933, 'translation_agreement': 0.116, 'back_translation_similarity_min': None, 'top_cluster_support': 1.0, 'sense_entropy': 0.971, 'context_fields_resolved': 0.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
