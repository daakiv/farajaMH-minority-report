# Review card — KISWA-STORY-02
Package `MRP-KISWA-STORY-02-indep-shared-s7` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `leave the world` in *sense/S6/gloss* — ……ed to the point of wanting to escape or leave the world…
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 3 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.80, 0.00 — poorly calibrated on small models; weigh the grounding above it.
>
> This is separate from the lexicon screen above and fires independently of it. A model reading is a proposal, not a finding — but a proposal about risk is not one to leave to the bottom of the card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Ni kama kuna jiwe kifuani kwangu, halitoki.
**Expression:** kuna jiwe kifuani kwangu
**Context:** KE/KE-western, dialect standard, speaker participant, setting home_visit, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Ni kama kuna jiwe kifuani kwangu, halitoki.` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | there is stone on chest my, it-does-not-leave | I feel like there's a stone on my chest that won't go away. | not run | None |
| T2 | qwen2.5:7b | If I have a heavy heart in my chest, I do not laugh. | When my heart is heavy, I don't laugh. | not run |  |
| T3 | llama3.1:8b | there is a stone on my forehead | I feel like there's a weight on my mind | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **somatic_experience**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | emotional distress | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | somatic experience | somatic_experience | minority | gemma3:12b |
| C4 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, emotional distress): The speaker feels burdened by a heavy emotional weight. — *The phrase 'kuna jiwe kifuani kwangu' (there's a stone on my chest) is a metaphor for a heavy burden, likely emotional. The affirmed negation 'halitoki' (it won't go away) suggests a persistent and distressing feeling.* — evidence: utterance_span: “kuna jiwe kifuani kwangu”; utterance_span: “halitoki”; conversation_turn: “Sijambo, lakini moyo wangu umekuwa mzito tangu majuma matatu.”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially figurative, expresses a desire for relief from a distressing condition that may be impacting their well-being, and warrants consideration for potential harm. — *The metaphor of a stone on the chest, combined with the statement that it 'won't go away,' suggests a persistent and distressing condition. While the phrasing may be idiomatic, it's crucial to consider the possibility that the speaker is experiencing significant emotional distress and may be at risk. It is not possible to determine from the available information whether this is a literal statement of risk, or a figurative expression of distress. It is safest to treat it as a statement of risk.* — evidence: utterance_span: “kuna jiwe kifuani kwangu”; utterance_span: “halitoki”
- **S3** (gemma3:12b, somatic experience): The speaker is experiencing a physical sensation of heaviness or pressure. — *The metaphor 'jiwe kifuani' (stone on the chest) could be a literal description of a physical sensation, although it is more likely figurative. The phrase describes a feeling of weight or pressure in the chest area.* — evidence: utterance_span: “jiwe kifuani”
- **S4** (qwen2.5:7b, sadness): The speaker feels a heavy burden in their heart that prevents them from laughing. — *The speaker uses the metaphor of a stone on their chest, which is a common expression of feeling weighed down by sadness or grief.* — evidence: utterance_span: “Ni kama kuna jiwe kifuani kwangu, halitoki.”
- **S5** (llama3.1:8b, sadness): Feeling weighed down by a heavy heart — *The speaker mentions their heart being heavy, which is a common metaphor for sadness or emotional pain.* — evidence: conversation_turn: “moyo wangu umekuwa mzito”
- **S6** (llama3.1:8b, risk_or_safety): Feeling overwhelmed or burdened to the point of wanting to escape or leave the world — *The speaker's use of 'kuna jiwe kifuani kwangu' may be idiomatic, but the phrase 'halitoki' suggests a sense of being trapped or unable to move forward.* — evidence: utterance_span: “halitoki”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000055` shame []; `MFOEM:000052` compassion []; `MFOEM:000216` gloomy mood [llama3.1:8b→skos:broadMatch]; `MFOMD:0000187` abstinence syndrome []; `MFOMD:0000013` depressed mood episode [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOMD:0000101` delusion [] — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode [llama3.1:8b→skos:broadMatch]; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 4 place(s): gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: moyo wangu umekuwa mzito" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.074, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.959, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
