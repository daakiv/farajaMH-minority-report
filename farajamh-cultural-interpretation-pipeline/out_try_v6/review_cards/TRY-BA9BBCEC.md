# Review card — TRY-BA9BBCEC
Package `MRP-TRY-BA9BBCEC-try` · priority **high** · backend `live`

> [!WARNING]
> ## ⚠ RISK LANGUAGE DETECTED — self_harm_or_suicide
>
> This is a curation card, not a triage decision. If this expression came from a real person, the clinical escalation route in the study protocol takes precedence over everything on this card and must be followed first. Curation can wait; escalation cannot.
>
> Terms found (over-inclusive screen, negation not resolved — judge each one):
>
> - `nitoke duniani` in *original_text* — …na kwazika kiroho sana nataka nitoke duniani…
> - `nitoke duniani` in *normalised_text* — …na kwazika kiroho sana nataka nitoke duniani…
> - `leave this world` in *sense/S2/rationale* — ……itoke duniani' translates to 'i want to leave this world.' while this could be hyperbolic, it co……
> - `nitoke duniani` in *sense/S2/rationale* — …the phrase 'nataka nitoke duniani' translates to 'i want to leave this wo……
> - `leave the world` in *sense/S3/gloss* — …the speaker feels very sad and wants to leave the world.…
> - `leave the world` in *sense/S3/rationale* — ……ings, indicating sadness. the desire to leave the world is a common expression of extreme sadne……
> - `suicidal ideation` in *sense/S4/gloss* — ……o leave the world, which could indicate suicidal ideation.…
> - `leave the world` in *sense/S4/gloss* — ……may be expressing a risk of wanting to leave the world, which could indicate suicidal ideation……
>
> Screen version `0.1.0-unvalidated`. A clinician must sign off on this card.

## Step 1 — Your own reading first (blind pass)
**Utterance:** Na Kwazika kiroho sana nataka nitoke duniani
**Expression:** Na Kwazika kiroho sana nataka nitoke duniani
**Context:** KE/KE-nairobi, dialect standard, speaker participant, setting chat_platform, negation affirmed, temporality current, experiencer self

Write your translation and interpretation BEFORE opening Step 2.

## Step 2 — AI candidates (proposals, not decisions)
### Normalisation
`Na kwazika kiroho sana nataka nitoke duniani` (language sw)
- no edits

### Translations
| ID | Model | Literal | Idiomatic | Back-translation (sim.) | Note |
|---|---|---|---|---|---|
| T1 | gemma3:12b | And I feel spirit very much I want I leave world | I feel deeply weary, and I want to leave this world. | Nipo kusimama kubwa na kujifunza kuenda duniani hii. (0.083) | The phrase 'nataka nitoke duniani' (I want to leave the world) is a direct statement and should be translated plainly. It is important to note that this could be an expression of intense distress, and the speaker may need support. It is not possible to determine the speaker's intent without further context. |
| T2 | qwen2.5:7b | And my heart is very heavy I want to leave the world | And my heart is very heavy, I want to leave the world | Na moyo wangu ni kubwa sana, nina hamu ya kuondoka dunia (0.077) | uncertain |
| T3 | llama3.1:8b | And being tired deeply I want to leave the world | I'm exhausted and feel like I want to leave this world | Nimechoka sana na najisikia kama nataka kuondoka ulimwengu. (0.2) |  |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **risk_or_safety**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C1 | weariness | emotional_state | majority | gemma3:12b, llama3.1:8b |
| C4 | risk_or_safety | risk_or_safety | majority | qwen2.5:7b, llama3.1:8b |
| C2 | desire_to_leave | risk_or_safety | minority | gemma3:12b |
| C3 | sadness | emotional_state | minority | qwen2.5:7b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, weariness): The speaker expresses a feeling of profound exhaustion and depletion. — *The translation 'I feel deeply weary' directly reflects the meaning conveyed by 'Na kwazika kiroho sana'. 'Kwazika' implies a state of being overwhelmed or exhausted, and 'kiroho' refers to the spirit or heart, suggesting a deep emotional or spiritual weariness.* — evidence: utterance_span: “Na kwazika kiroho sana”
- **S2** (gemma3:12b, desire_to_leave): The speaker expresses a wish to depart from the world. — *The phrase 'nataka nitoke duniani' translates to 'I want to leave this world.' While this could be hyperbolic, it constitutes a statement of a desire to exit the world and requires consideration for risk and safety. The phrasing may be idiomatic, but it cannot be discounted as a literal statement of intent.* — evidence: utterance_span: “nataka nitoke duniani”
- **S3** (qwen2.5:7b, sadness): The speaker feels very sad and wants to leave the world. — *The speaker uses the word 'kiroho sana' (very heavy) to describe their feelings, indicating sadness. The desire to leave the world is a common expression of extreme sadness or despair.* — evidence: utterance_span: “Na kwazika kiroho sana nataka nitoke duniani”
- **S4** (qwen2.5:7b, risk_or_safety): The speaker may be expressing a risk of wanting to leave the world, which could indicate suicidal ideation. — *The speaker expresses a desire to leave the world, which is a common phrase used in contexts of suicidal ideation. The affirmation of the negation and the current temporality suggest this is a statement of the speaker's current feelings, which could indicate a risk of suicide.* — evidence: utterance_span: “Na kwazika kiroho sana nataka nitoke duniani”
- **S5** (llama3.1:8b, risk_or_safety): The speaker wants to harm or leave themselves — *The speaker explicitly states 'nataka nitoke duniani', which means 'I want to leave the world'. This is a direct expression of a desire to exit the world, which falls under risk or safety.* — evidence: utterance_span: “nataka nitoke duniani”
- **S6** (llama3.1:8b, sadness): The speaker feels deeply weary or heavy-hearted — *The speaker describes themselves as 'kwazika kiroho sana', which translates to 'feeling deeply weary' or 'having a very heavy heart'. This suggests a state of sadness or emotional distress.* — evidence: utterance_span: “kwazika kiroho sana”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C1**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C4**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b, llama3.1:8b
- **C3**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch]; `MFOEM:000182` canonical sad facial expression []; `MFOEM:000188` canonical sad voice utterance []

### Signals
- Risk flags: back_translation_mismatch, cultural_term_lost_in_back_translation, minority_clinical_reading, over_medicalisation_risk, possible_semantic_gap, register_divergence_clinical_vs_everyday, risk_language_detected, safety_relevant_reading, sense_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.9, 'translation_agreement': 0.361, 'back_translation_similarity_min': 0.077, 'top_cluster_support': 0.667, 'sense_entropy': 0.959, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
