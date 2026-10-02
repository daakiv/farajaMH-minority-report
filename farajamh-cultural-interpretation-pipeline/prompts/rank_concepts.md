You are helping reviewers find terminology concepts for a candidate meaning of an East African expression of distress.
You may ONLY rank concepts from the retrieved list below. Never invent, change or complete an identifier.

Start from the assumption that NONE of the retrieved concepts fits. The list was produced by a keyword search, not by a person who understood the meaning, so it often contains concepts that merely share a word or a general mood with the candidate meaning. Your job is to reject those, not to find the best of a bad set.

Rank a concept only if you would defend the mapping to a terminologist. Apply this test to each one: if the retrieved concept names a DIFFERENT emotion, state or event from the candidate meaning, it does not fit, however intense or related it sounds. "Terror" is not a broader concept than "overwhelm"; it is a different emotion, and ranking it would be wrong. A concept is a broadMatch only when the candidate meaning is genuinely a KIND of that concept.

Judge each concept on its DEFINITION, not its label. The definitions are the fourth field of each line below. Two concepts can share almost every word in their labels and be different kinds of thing: "sadness" is defined as "a negative emotion felt when an event is appraised as unpleasant", while "canonical sad facial expression" is defined as "the canonical facial expression associated with the experience of sadness". The second one is a FACE, not a feeling. An expression, utterance, assessment, or measurement OF a state is never a match for the state itself, and a definition naming a duration, an episode or a diagnostic threshold is not a match for a candidate meaning that names none of those.

Where the definition reads NO DEFINITION PROVIDED BY THIS TERMINOLOGY, you have only a label. That is a reason for more caution, not less: say in your rationale that you are judging from the label alone, and prefer rejecting the concept over guessing what it means.

`no_adequate_match` and a non-empty `ranked` list are mutually exclusive. If you rank even one concept, `no_adequate_match` is false. If you set it to true, `ranked` must be empty. Returning both makes the reviewer's card contradict itself.

If nothing survives that test, return an empty `ranked` list, set `no_adequate_match` to true, and use `gap_note` to say what a concept would need to cover. An empty list is a good answer and is recorded as a semantic gap for human review. Returning a poor match is worse than returning nothing, because several models rationalising the same poor match looks like agreement.

For each concept you rank, propose a predicate:
- skos:exactMatch (same meaning)
- skos:broadMatch (the concept is broader than the candidate meaning)
- skos:narrowMatch (the concept is narrower)
- skos:relatedMatch (related, not hierarchical)
Prefer broadMatch or relatedMatch over exactMatch when the cultural meaning is richer than the concept.

Candidate meaning: {{sense_gloss}} (category: {{sense_category}}, register: {{sense_register}})
Expression: {{normalised_expression}}
Retrieved concepts (system | id | label | definition):
{{retrieved}}

In each rationale, quote or paraphrase the part of the DEFINITION that decided you, so a reviewer can check your reasoning against the terminology rather than against your wording.

Return ONLY JSON: {"ranked": [{"id": "...", "rank": 1, "proposed_predicate": "skos:broadMatch", "rationale": "..."}], "no_adequate_match": false, "gap_note": "..."}
