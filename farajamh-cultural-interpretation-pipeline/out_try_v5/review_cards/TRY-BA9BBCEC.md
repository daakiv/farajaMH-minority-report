# Review card — TRY-BA9BBCEC
Package `MRP-TRY-BA9BBCEC-try` · priority **high** · backend `live`

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
| T1 | gemma3:12b | I feel spirit very much I want I leave world | I feel deeply overwhelmed, I just want to disappear. | Nipo kusikitisha kusikitishwa, ni wakati unafaa kufanya niweke. (0.0) | The intensity of the feeling is difficult to convey precisely without more context. The phrase 'nitoke duniani' is hyperbolic, expressing a strong desire to escape, rather than a literal suicidal statement. It's crucial to avoid clinical interpretations. |
| T2 | qwen2.5:7b | And because I am feeling very sad I want to leave the world | And because I am feeling very sad, I want to leave the world | Na kwa kuwa nina hisia ya kuchukua, nataka kuondoka duniani (0.182) | uncertain |
| T3 | llama3.1:8b | My heart is very deeply troubled, I want to leave the world | I'm feeling really troubled to my core, I just want to escape this world | Ninahisi huzuni sana ndani yangu, nataka tu nisiwezo ulimwengu huu. (0.143) | The phrase 'nitoke duniani' could be interpreted in different ways, but in this context, it seems to convey a sense of wanting to escape or leave the world due to emotional distress. |

### How the models read it, by category (labels aside)
- **emotional_state**: 3/3 models (gemma3:12b, llama3.1:8b, qwen2.5:7b)
- **social_or_relational**: 1/3 models (gemma3:12b)

### Candidate meanings, clustered across models
| Cluster | Meaning | Category | Standing | Models |
|---|---|---|---|---|
| C3 | sadness | emotional_state | majority | qwen2.5:7b, llama3.1:8b |
| C1 | overwhelm | emotional_state | minority | gemma3:12b |
| C2 | desire_to_escape | social_or_relational | minority | gemma3:12b |
| C4 | overwhelmed | emotional_state | minority | llama3.1:8b |

<details><summary>Rationale and evidence per model</summary>

- **S1** (gemma3:12b, overwhelm): The speaker expresses a feeling of being deeply overwhelmed by circumstances. — *The phrase 'kiroho sana' suggests a profound emotional state, and 'nataka nitoke duniani' implies a desire to escape a difficult situation, consistent with feeling overwhelmed.* — evidence: utterance_span: “kiroho sana”
- **S2** (gemma3:12b, desire_to_escape): The speaker expresses a wish to leave the world, indicating a desire to escape from a difficult situation. — *The phrase 'nataka nitoke duniani' directly translates to 'I want to leave the world,' indicating a desire to escape.* — evidence: utterance_span: “nataka nitoke duniani”
- **S3** (qwen2.5:7b, sadness): I feel extremely sad and want to leave the world. — *The speaker is expressing a strong emotional state of sadness and a desire to escape, which aligns with the proposed translation.* — evidence: utterance_span: “I feel deeply overwhelmed, I just want to disappear.”
- **S4** (llama3.1:8b, sadness): feeling deeply sad and wanting to escape the world — *The speaker uses the word 'kiroho' which means 'heart' or 'core', indicating a strong emotional response.* — evidence: utterance_span: “Na kwazika kiroho sana”
- **S5** (llama3.1:8b, overwhelmed): feeling deeply overwhelmed and wanting to escape the world — *The speaker uses the word 'kwazika' which means 'deeply' or 'very', indicating a strong emotional response.* — evidence: utterance_span: “Na kwazika kiroho sana”

</details>

### Candidate concepts (retrieved from terminology services; ranked by models)
- **C3**: `MFOEM:000056` sadness [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:exactMatch]; `MFOEM:000182` canonical sad facial expression [gemma3:12b→skos:relatedMatch]; `MFOEM:000188` canonical sad voice utterance [gemma3:12b→skos:relatedMatch]
- **C1**: `MFOEM:000027` terror [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b
- **C2**: none retrieved — **no adequate match** per gemma3:12b, qwen2.5:7b
- **C4**: `MFOEM:000027` terror [gemma3:12b→skos:broadMatch, qwen2.5:7b→skos:broadMatch, llama3.1:8b→skos:broadMatch] — **no adequate match** per gemma3:12b

### Signals
- Risk flags: back_translation_mismatch, cultural_term_lost_in_back_translation, possible_semantic_gap, translation_divergence
- Model output was schema-clean
- Suggested reviewers: linguist, cultural_expert, clinician, lived_experience
- Confidence components (not a probability): `{'translation_self_reported_mean': 0.817, 'translation_agreement': 0.149, 'back_translation_similarity_min': 0.0, 'top_cluster_support': 0.667, 'sense_entropy': 0.961, 'context_fields_resolved': 1.0}`

## Step 3 — Decide (record in the review sheet or review_decision JSON)
Accept, edit or reject each layer separately. Choosing 'no adequate concept' is a valid outcome and is recorded as a semantic gap.
