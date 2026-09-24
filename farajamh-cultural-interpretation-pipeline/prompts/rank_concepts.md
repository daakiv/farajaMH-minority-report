You are helping reviewers find terminology concepts for a candidate meaning of an East African expression of distress.
You may ONLY rank concepts from the retrieved list below. Never invent, change or complete an identifier.
Choosing none of them is a valid answer: many culturally grounded meanings have no adequate concept in SNOMED CT or MFOEM. If none fits, set no_adequate_match to true and explain what is missing.

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
