# Review card — KISWA-STORY-02
Package `MRP-KISWA-STORY-02-queryfix-v1` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> **Every match below is in text the models generated, not in the participant's own words.** The screen reads model output too, on purpose — a model naming risk that it then drops is a signal. But nothing here says the speaker used risk language.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nife` in *gap_note/C5* — ……ific emotion like sadness, a physical manifestation of sadness, or a clinical depres……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

> [!WARNING]
> ## ⚠ A RISK READING WAS PROPOSED BY THE MODELS
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> 2 of 3 models proposed a `risk_or_safety` reading (majority): **risk_or_safety**.
>
> Grounding: 2 quotes from the utterance itself.
>
> Self-reported plausibility for these senses: 0.70, 0.00 — poorly calibrated on small models; weigh the grounding above it.
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
| T1 | gemma3:12b | there is stone on chest my, it-does-not-leave | I feel like there's a heavy stone on my chest that won't go away. | not run | None |
| T2 | qwen2.5:7b | If I have a heavy heart in my chest, I do not laugh. | When my heart is heavy, I don't laugh. | not run |  |
| T3 | llama3.1:8b | there is a stone on my head | I feel weighed down, like a burden is on my head | not run |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 2/3 models (gemma3:12b, llama3.1:8b)
- **somatic_experience**: 2/3 models (gemma3:12b, llama3.1:8b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | emotional distress | emotional_state | majority | gemma3:12b, qwen2.5:7b |
| C2 | risk_or_safety | risk_or_safety | majority | gemma3:12b, llama3.1:8b |
| C3 | somatic experience | somatic_experience | minority | gemma3:12b |
| C4 | heaviness | somatic_experience | minority | llama3.1:8b |
| C5 | sadness | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, emotional distress): The speaker feels burdened and weighed down by an unspecified emotional difficulty. — *The phrase 'kuna jiwe kifuani kwangu' (there's a stone on my chest) is a metaphor for a heavy, persistent feeling. The preceding statement about a heavy heart ('moyo wangu umekuwa mzito') reinforces this sense of emotional burden.* — evidence: utterance_span: “Ni kama kuna jiwe kifuani kwangu”; conversation_turn: “Sijambo, lakini moyo wangu umekuwa mzito tangu majuma matatu.”
- **S2** (gemma3:12b, risk_or_safety): The speaker's statement, while potentially figurative, expresses a desire to be free from a distressing condition, which could indicate a risk of harm or a need for support. — *The phrase 'halitoki' (it won't go away) suggests a persistent and unwelcome condition. While the metaphor may be idiomatic, the speaker's desire for relief from this condition could indicate underlying distress that poses a risk. It is important to consider this as a potential indicator of a need for support, even if the phrasing is not a literal statement of risk.* — evidence: utterance_span: “halitoki”
- **S3** (gemma3:12b, somatic experience): The speaker is experiencing a physical sensation of heaviness or pressure in their chest. — *The metaphor 'jiwe kifuani' (stone on the chest) suggests a physical sensation of weight or pressure. While likely metaphorical, it could also reflect a genuine physical discomfort associated with emotional distress.* — evidence: utterance_span: “kuna jiwe kifuani kwangu”
- **S4** (qwen2.5:7b, sadness): The speaker feels weighed down by a heavy burden in their heart. — *The speaker uses the metaphor of a heavy stone on their chest, indicating a feeling of heaviness and burden.* — evidence: utterance_span: “Ni kama kuna jiwe kifuani kwangu, halitoki.”
- **S5** (llama3.1:8b, heaviness): feeling weighed down or burdened — *The speaker mentions their heart being 'mzito' (heavy) which is a physical sensation.* — evidence: conversation_turn: “moyo wangu umekuwa mzito”
- **S6** (llama3.1:8b, sadness): feeling unhappy or sorrowful — *The speaker says they are not feeling well ('Sijambo') and their heart is heavy, which suggests they are experiencing sadness.* — evidence: conversation_turn: “Sijambo”
- **S7** (llama3.1:8b, risk_or_safety): expressing a desire to escape or leave the situation — *The speaker says 'halitoki' which means 'it won't go away', but in the context of feeling weighed down, it may imply a desire to escape or leave the situation.* — evidence: utterance_span: “halitoki”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: `MFOEM:000055` shame []; `MFOEM:000052` compassion []; `MFOEM:000216` gloomy mood [llama3.1:8b→skos:broadMatch]; `MFOMD:0000187` abstinence syndrome []; `MFOMD:0000013` depressed mood episode [] — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: `MFOMD:0000185` paranoia [] — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C5**: `MFOEM:000056` sadness [qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []; `MFOMD:0000013` depressed mood episode []; `MFOMD:0000143` major depressive episode []; `MFOMD:0000147` nightmare []; `MFOMD:0000149` mixed episode [] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_disabled, model_output_coerced, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence, translation_divergence
- Model output repaired in 5 place(s): gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0; gemma3:12b/interpret self_reported_plausibility="None" → 0; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: moyo wangu umekuwa mzito" → conversation_turn; llama3.1:8b/interpret evidence.type (quote not in the utterance)="utterance_span: Sijambo" → conversation_turn
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.95, 'translation_agreement': 0.056, 'back_translation_similarity_min': None, 'top_cluster_support': 0.667, 'sense_entropy': 0.963, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
