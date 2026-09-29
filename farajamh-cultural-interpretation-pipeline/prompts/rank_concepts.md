You are helping reviewers find terminology concepts for a candidate meaning of an East African expression of distress.
You may ONLY rank concepts from the retrieved list below. Never invent, change or complete an identifier.

Start from the assumption that NONE of the retrieved concepts fits. The list was produced by a keyword search, not by a person who understood the meaning, so it often contains concepts that merely share a word or a general mood with the candidate meaning. Your job is to reject those, not to find the best of a bad set.

Rank a concept only if you would defend the mapping to a terminologist. Apply this test to each one: if the retrieved concept names a DIFFERENT emotion, state or event from the candidate meaning, it does not fit, however intense or related it sounds. "Terror" is not a broader concept than "overwhelm"; it is a different emotion, and ranking it would be wrong. A concept is a broadMatch only when the candidate meaning is genuinely a KIND of that concept.

If nothing survives that test, return an empty `ranked` list, set `no_adequate_match` to true, and use `gap_note` to say what a concept would need to cover. An empty list is a good answer and is recorded as a semantic gap for human review. Returning a poor match is worse than returning nothing, because several models rationalising the same poor match looks like agreement.

For each concept you rank, propose a predicate:
- skos:exactMatch (same meaning)
- skos:broadMatch (the concept is broader than the candidate meaning)
- skos:narrowMatch (the concept is narrower)
- skos:relatedMatch (related, not hierarchical)
Prefer broadMatch or relatedMatch over exactMatch when the cultural meaning is richer than the concept.

Candidate meaning: {{sense_gloss}} (category: {{sense_category}}, register: {{sense_register}})
Expression: {{normalised_expression}}
Retrieved concepts (system | id | label):
{{retrieved}}

Return ONLY JSON: {"ranked": [{"id": "...", "rank": 1, "proposed_predicate": "skos:broadMatch", "rationale": "..."}], "no_adequate_match": false, "gap_note": "..."}
