# Minority Report for FarajaMH: assessment and adaptation design


---

## Contents

- [Current state](#current-state)
- [1. How the Minority Report works today, and what is reusable](#1-how-the-minority-report-works-today-and-what-is-reusable)
- [2. Mapping Minority Report components to the FarajaMH workflow](#2-mapping-minority-report-components-to-the-farajamh-workflow)
- [3. What needs to change or be added](#3-what-needs-to-change-or-be-added)
- [4. Input and output schemas](#4-input-and-output-schemas)
- [5. Connecting to the Local Concept Layer, the mapping workflow and SSSOM](#5-connecting-to-the-local-concept-layer-the-mapping-workflow-and-sssom)
- [6. Keeping the layers separate](#6-keeping-the-layers-separate)
- [7. Risks](#7-risks)
- [8. Architecture](#8-architecture)
- [9. Pilot: 10 constructed Swahili expressions](#9-pilot-10-constructed-swahili-expressions)
- [10. Run log](#10-run-log)
- [11. Open decisions](#11-open-decisions)

---

## Current state

*Updated 30 September 2026 · pipeline `0.2.5` · lexicon `0.2.0-unvalidated` · upstream pinned at `a7cb9cb`*

| | |
|---|---|
| **Runs** | End to end on constructed Kiswahili and English examples, with live local models and live terminology lookups. Four live runs to date; see §10. |
| **Models** | Three interpreters from three families on a laptop via Ollama (Gemma 3 12B, Qwen 2.5 7B, Llama 3.1 8B), one of them also normalising. |
| **Terminologies** | **MFOEM** and **MFOMD** live via EMBL-EBI OLS4. **SNOMED CT** configured but disabled: no licence covering Kenya or Tanzania, and no terminology server. |
| **Outputs** | Candidate packages, review cards, Local Concept Layer, SSSOM mappings and gap records. Demo outputs use placeholder identifiers and are marked not for registration. |
| **Tests** | 66, covering the rules that must hold whatever the models say. |
| **Not yet done** | No participant data. Kiswahili not validated by linguists. Risk lexicon not reviewed by clinicians or LEAB. Reviewer panel not constituted. |

**What the design assumes, and why**

1. **Reuse the Minority Report's infrastructure and patterns, not its decision logic.** Multi-model dispatch on Ollama, model-to-host routing, JSON repair, prompt-as-file templates, ODRL-as-runtime-policy, the OntoPortal client, Croissant/PROV provenance and SHA-256 hashing all carry over. The consensus mechanism does not: it forces one "most standard" term, counts exact string matches, and its arbitrator picks a winner or synthesises a new one. That is the opposite of what FarajaMH needs.
2. **The name already describes the fix.** Upstream, dissenting outputs are labelled "Arbitration lost" and left out of the metadata. This adaptation keeps the minority reading and labels it, because for idioms of distress the dissenting reading is often the one reviewers need to see.
3. **The two projects have different tasks.** The Minority Report translates *English technical terms with authoritative definitions* into European and UN languages. FarajaMH interprets *Kiswahili and Sheng expressions, often code-mixed and with no definition*. The source language, the prompts, the validation rule (translation ≥ 40% of source length) and the IAEA/WMO proofreader do not transfer.

**Decisions still outstanding** — which models sit on the DSA-approved host, SNOMED CT licence coverage, the reviewer roster per role, and whether the SSSOM subject is the local concept rather than the raw expression (recommended; §5). The full list is in §11.

## 1. How the Minority Report works today, and what is reusable

### Current workflow (`translation-skill/scripts/orchestrator.py`, 1,246 lines)

1. **Ingest.** It scrapes a PreventionWeb HIPS page, or an OntoPortal concept page, to get a *term* and a *scope note* (the definition).
2. **Keyword extraction** (optional "rl" method). A small model (`gemma4:e2b`) extracts domain phrases from the scope note, caches them to disk and appends them to the context.
3. **Voter round.** Each model in `--models` (the defaults and documentation use `gpt-oss`, `gemma3:27b` and `deepseek-r1:14b` on Ollama, plus an optional Gemini CLI path) translates the term into all target languages in parallel. The voter prompt requires *"ONLY the single most standard, officially recognized technical term… Do NOT provide synonyms."* The output is `{lang: {translation, confidence_score}}`.
4. **Consensus.** Per language, translations are lower-cased and counted. Two or more identical strings means "Consensus reached".
5. **Arbitration.** Without consensus, every model is shown the candidates and asked to select or *synthesise* the best one. A candidate with two or more arbitration votes wins; the others are marked "Arbitration lost".
6. **Long text** (full HIPS articles). The primary model translates using a four-step self-critique prompt with Wikipedia/Wikidata synonyms. The output is then length-checked (≥ 40% of source) and proofread against IAEA/WMO terminology, with a changelog.
7. **Outputs.** It writes a CSV (`term, translation, context, language, confidence, winning_model, consensus, version, code, url`), Croissant JSON-LD with a SHA-256 per file and PROV links from each translation to its model, metric extraction to CDIF JSON, and a central "semantic Croissant" catalogue.
8. **Governance.** An ODRL policy (`ODRL/translation_pipeline_odrl.jsonld`) is checked at runtime by `api.py` (environment variables, length duty, retry consequence).
9. **Interfaces.** It exposes a CLI, a FastAPI service, an MCP server (`understand_and_translate`, `open_page_and_translate`, `find_hazards`) and spaCy/Gemma training scripts.

### Reusability verdict

| Component | Verdict for FarajaMH | Why |
|---|---|---|
| Ollama client + `ModelRouter` (multi-host allocation) | **Reuse** | Runs open-weights models on local hosts, which is what the DSA requires. |
| Parallel multi-model dispatch (`ThreadPoolExecutor`) | **Reuse** | This is the independence the design needs. |
| `repair_json` + regex fallback | **Reuse** | Small models often return malformed JSON. |
| Prompt templates as Markdown files with `{{placeholders}}` | **Reuse pattern** | Prompts become versionable, hashable artefacts. |
| ODRL policy enforced at runtime | **Reuse pattern, new duties** | A good governance mechanism, but its HIPS duties do not apply (§3). |
| `ontoportal.py` (`OntoPortalClient`) | **Reuse for MFOEM** (BioPortal/OntoPortal) | SNOMED CT needs a licensed server (Snowstorm or Ontoserver) instead. |
| Croissant generator, SHA-256, PROV links to model | **Reuse for the catalogue record** of the candidate dataset | Fits your Croissant/catalogue work. It needs FarajaMH fields and must not publish restricted text. |
| Row-level `winning_model` provenance | **Extend** | Also record model digest, prompt hash, options and seed. Slava's replicability question needs these. |
| Voter prompt | **Replace** | It forces one term and forbids alternatives. |
| Exact-string consensus (≥ 2 identical) | **Replace** | Paraphrases count as disagreement, and a single reading counts as agreement. |
| Arbitrator (select or synthesise a winner) | **Remove** | The AI must not choose. Synthesis invents text that no model independently proposed. |
| Keyword-extraction and Wikipedia-expert prompts | **Drop for now** | They assume English technical source text. Idioms of distress have no authoritative Wikipedia terms. |
| Long-text translation, 40% length rule, HIPS proofreader | **Drop** | Built for articles, not short utterances. |
| Metrics extraction (CDIF), spaCy hazard NER, Gemma fine-tuning | **Not relevant** to Stage 1 | — |
| MCP server | **Optional later** | Useful for reviewers' tools once the pipeline is stable. |

Things to raise with Slava:
- An internal Ollama IP address is hard-coded as the default.
- `croissant_generator.py` imports from an absolute path on a CODATA machine.
- `SKILL.md` describes a "flag consensus below 0.7 for manual review" rule and `rai_flags`. I found neither in the code.
- One further item concerns a credential in the upstream repository. It is raised with the maintainer directly rather than in this document, which is public.

---

## 2. Mapping Minority Report components to the FarajaMH workflow

| FarajaMH step (Stage 1 in v10) | Minority Report today | FarajaMH-adapted component (this kit) |
|---|---|---|
| Safety check (before triage) | none | `policy.check_before_run`: block if flagged and not escalated (D2) |
| Dialect/language normalisation | none (English source assumed) | **M1** `prompts/normalise.md`: edit list, language ID, code-switch segments |
| AI-assisted translation keeping cultural meaning | voter prompt (one term per language) | **M2** `prompts/translate.md` × N models: literal gloss + idiomatic + preserved terms; ring back-translation (`back_translate.md`) |
| Context-aware interpretation | scope note as context | **M3** `prompts/interpret.md` × N: reads the Silver context (negation, temporality, attribution, speaker, setting, region, dialect, conversation window) |
| Multiple candidate interpretations | forbidden by prompt | M3 returns 1–4 senses per model, including non-medical readings |
| Agreement/disagreement | exact-match count + arbitration | **M4** `agreement.py`: sense clustering, unanimous/majority/minority standing, divergence flags, no winner |
| Candidate concept matching (MFOEM, MFOMD, SNOMED CT) | OntoPortal definition lookup (enrichment only) | **M5** `terminology.py`: one client per configured system — OLS4 for MFOEM and MFOMD, Snowstorm for SNOMED CT → every model ranks → invented IDs dropped |
| Rationale, evidence, confidence | `reasoning` + `final_confidence_score` from the arbitrator | per-sense rationale + evidence spans; confidence reported as separate components (§3) |
| Structured package for review | CSV + Croissant | **M6** `candidate_package.schema.json` (layers L1–L7) + review card + review sheet |
| Human validation | "Antigravity Manager Surface" (described, not in code) | `review_decision.schema.json`: per role, per layer, blind first pass, adjudication |
| Local Concept Layer / SSSOM | none | `approve.py`: runs only on final decisions → `local_concept_layer.jsonl`, `mappings.sssom.tsv`, `gap_register.jsonl` |

---

## 3. What needs to change or be added

**Swahili and dialect/regional variation**
- Make the source language a parameter. The upstream code assumes English source and uses its own language codes (`ch`, `dk`, `ua`); use BCP 47 (`sw`, `sw-KE`, `sw-TZ`, `en-KE`).
- BCP 47 has no subtags for most Swahili dialects (Kiamu, Kimvita, Kiunguja) or for Sheng. Keep a controlled FarajaMH dialect list in `context.dialect_declared`, and add Glottolog IDs where one exists. The pilot uses `sw-x-sheng` as a private-use tag.
- M1 records every edit with a type (l/r alternation, Sheng forms such as a dropped *ku-*, ASR corrections). It never overwrites the original. Dialect remains a *hypothesis* for the linguist to confirm.
- Build a small FarajaMH rule list (known variants, Sheng lexicon) with linguists. Do not rely on the model alone.

**Culturally specific expressions and idioms**
- The translation prompt asks for a literal gloss next to the idiomatic rendering, so the metaphor (*moyo mzito*, *mawazo mengi*) stays visible to reviewers.
- Culturally loaded words (*roho, moyo, mawazo, raha*) are listed as preserved terms. The pipeline flags when a back-translation loses them. Its current substring check is crude (it misses *nawaza* as the stem of *mawazo*); a morphological analyser should replace it.
- The interpretation prompt explicitly asks for non-medical readings and forbids diagnosis names.

**Context-aware interpretation**
- Following v10, context resolution happens in Silver. The Minority Report *reads* it, *cites* it as evidence and *flags* inconsistencies; it does not re-resolve it.
- Negated, non-self or unresolved context raises review priority: `polarity_negated`, `experiencer_not_speaker`, `context_incomplete`.

**MFOEM, MFOMD and SNOMED CT candidate mapping**
- Concepts are *retrieved* first, then *ranked*. An LLM never originates an identifier, which matches the v10 rule. Any ID that did not come back from the terminology service in the same run is dropped (tested).
- SNOMED CT retrieval is scoped by ECL to the Clinical finding hierarchy by default. Widening the scope is an explicit configuration decision.
- MFOEM (emotion, mood and appraisal) and MFOMD (mental disorder) are queried in parallel as optional enrichment, in line with the decision to make them a parallel step rather than a mandatory hop. Each configured system is built from its own `client` key, so adding an ontology is a configuration change; the system name is carried per client, because a shared constant would stamp every MFOMD concept as MFOEM and the provenance would be wrong.
- A broader ontology returns more noise. In `kiswa-story-v1` a model ranked 38% of the MFOEM candidates offered and 13% of the MFOMD ones, and some MFOMD candidates were clinically loaded and irrelevant. Retrieval scope per system is a tuning decision, not a default (§10).
- "No adequate match" is a first-class answer, recorded per model.
- Pin terminology versions in the configuration and record them in provenance.

**Multiple candidate interpretations** — Each model gives 1–4 senses independently. Models do not see each other's senses, which limits herding.

**Agreement/disagreement recording**
- Senses are clustered: same `sense_key`, or same category with similar glosses. The pilot uses token Jaccard; production should use multilingual sentence embeddings.
- Each cluster records its supporting models, support ratio and standing: unanimous, majority or minority.
- Divergence is recorded at three levels:
  - translation (pairwise similarity);
  - sense (competing readings versus multiple components of one utterance, such as P06's "stress" plus "can't sleep");
  - concept (top-1 agreement, predicate disagreement, no-match votes).
- Nothing is discarded, and nothing wins.

**Rationale and evidence capture**
- Every sense carries a rationale and typed evidence: `utterance_span`, `context_field`, `conversation_turn`, `local_concept_layer` or `model_background_knowledge`.
- The last type is kept separate on purpose. It marks a claim that rests only on the model's general knowledge, which reviewers should weigh differently from a quoted span.

**Confidence scoring**
- LLM self-reported confidence is poorly calibrated. The upstream pipeline records it but does not use it in the consensus rule.
- The package therefore reports *components*, not one score: self-reported mean, translation agreement, minimum back-translation similarity, top-cluster support, sense entropy and fraction of context resolved. These drive **review priority**, not acceptance.
- The only confidence that reaches SSSOM is the **reviewer's** confidence in the approved mapping.
- Calibrate the components against human decisions during the pilot before adding weights.

**Provenance and auditability**
- Each package records:
  - the pipeline version and the upstream commit;
  - the run ID and timestamps;
  - for each model: name, family, role, Ollama digest, host locality and options (temperature, seed);
  - the SHA-256 of every prompt;
  - terminology endpoints and versions;
  - the policy file;
  - the input hash.
- Review decisions carry the reviewer ID (ORCID or a pseudonymous LEAB ID), role and time.
- SSSOM rows cite the package ID.

**Human-in-the-loop review**
- Review cards place a **blind first pass** before the AI candidates, so anchoring can be measured.
- Decisions are taken layer by layer. Reviewers can add a sense no model proposed.
- An adjudicator records the single `final` decision.
- Roles follow v10: linguist, cultural expert, clinician, lived experience.

**Governance (replaces the HIPS ODRL duties)** — `policy/farajamh_mr_odrl.jsonld`, enforced in `policy.py` and `approve.py`:

| Rule | What it enforces |
|---|---|
| D1 | Restricted data goes only to DSA-approved local hosts; the Gemini CLI path is off |
| D2 | Safety gate |
| D3 | IDs come only from retrieval |
| D4 | Minority readings are retained |
| D5 | At least 3 models from at least 2 families |
| P1 | No SSSOM, local concept or OMOP output without a final human decision; placeholder IDs are refused |
| P2 | A package can never be marked approved |

---

## 4. Input and output schemas

Full JSON Schemas (draft 2020-12) are in `schemas/`. All pilot inputs and generated packages validate against them.

**Input: `utterance_input`** (one per utterance, from Silver)
- `utterance_id`, `silver_record_ref` {record_id, silver_version, sha256}
- `source` {modality, transcription_method, asr_model, asr_confidence}
- `original_text`, `language_declared`, `expression_span` {start, end, text}
- `conversational_context` {window_policy, preceding_turns[], following_turns[]}
- `context` {country, region, site_id, dialect_declared, speaker_role, setting, negation, temporality, attribution, applicability, onset_or_duration}. Each resolved value has the form {value, source, confidence}.
- `triage` {route: `near_match_different_concept` | `new_expression`, nearest_local_concept}
- `safety` {flag, escalated, escalation_ref}
- `data_classification` (`restricted` | `deidentified` | `synthetic`), `consent_scope_ref`

**Output: `candidate_package`** (one per utterance; status can only be `awaiting_review`, `blocked_pending_safety_escalation` or `failed`)
- `provenance` (see §3)
- `L1_original` — the exact text, span and context as received
- `L2_normalisation` — normalised text and expression, typed edits, language ID, code-switch segments, dialect hypotheses
- `L3_translation.candidates[]` — model, literal gloss, idiomatic translation, preserved terms, uncertainty note, self-reported confidence, back-translation {by_model, text, similarity}
- `L4_interpretation.candidates[]` — sense_id, model, sense_key, gloss, category, register (`everyday_cultural` | `clinical` | `mixed`), context dependencies, rationale, evidence[], plausibility
- `L5_agreement` — sense_clusters[] {members, supporting_models, support_ratio, standing}, metrics, divergence_flags
- `L6_concept_candidates.per_cluster[]` — retrieved concepts {system, id, label, id_verified, retrieved_from, query, rank, version, ranking[] by model with proposed predicate}, no_adequate_match_votes, gap_note
- `L7_review_signals` — review_priority, risk_flags, confidence_components, suggested_reviewer_roles

**Human output: `review_decision`** (one per reviewer; the adjudicator's record has `final: true`)
- blind_first_pass {own_translation, own_interpretation}
- layer_decisions: normalisation / translation / interpretation (+ `clinical_status`) / context / concepts[] {decision `approve` | `reject` | `defer` | `no_adequate_concept`, predicate, `negative_assertion`, confidence, justification}
- local_concept_action {create | add_variant, local_concept_id, labels, definition}

Example outputs from the dry run are in `out/packages/`, `out/review_cards/` and `out/approved/`.

---

## 5. Connecting to the Local Concept Layer, the mapping workflow and SSSOM

1. **Package → human review.** The package is the evidence file for review, never an input to the concept layer.
2. **Final decision → Local Concept Layer first.** The approved meaning is written as a FarajaMH local concept (`FMHLC:nnnn`). It holds:
   - a Swahili preferred label and an English label;
   - a definition;
   - `clinical_status`: non-clinical cultural / possible symptom indicator / symptom expression / safety-relevant;
   - the expression as a *variant*, with dialect, region, language and normalised form;
   - the approved translation;
   - the evidence package ID and the approvers.

   This happens whether or not any external concept fits.
3. **Concept decision → SSSOM, only for the local concept.** I recommend one change to the v10 panel. It shows the SSSOM *subject* as the local expression; I recommend the **local concept** instead:
   - Expression variants then attach to the concept through triage path B ("add variant") without new mappings.
   - One mapping row serves every variant.
   - Mappings can be reviewed once per meaning rather than once per spelling.
4. **Predicates.**
   - Use `skos:exactMatch`, `broadMatch`, `narrowMatch` or `relatedMatch`.
   - Expect `broadMatch` or `relatedMatch` most of the time: the cultural meaning is usually richer than the SNOMED CT finding.
   - v10's "is evidence for" is not a standard mapping predicate. If you want that relation, define it in a FarajaMH namespace and document it in the mapping-set metadata. Otherwise SSSOM consumers cannot interpret it.
5. **Justification and authorship.**
   - `mapping_justification: semapv:ManualMappingCuration`
   - every configured terminology needs a CURIE prefix and an `object_source` in `approve.py`; a retrieved concept that has neither cannot be published as a mapping
   - `author_id` = the reviewers; `reviewer_id` = the adjudicator; `mapping_tool` = `farajamh-minority-report` with its version
   - `confidence` = the reviewer's confidence
   - `comment` cites the package ID, so each row links back to the AI rationale without copying restricted text
6. **Semantic gaps are recorded, not forced.** "No adequate concept" becomes an SSSOM row with `object_id: sssom:NoTermFound` (defined in the SSSOM spec for exactly this case) plus a Gap Register entry. The local concept stays usable.
7. **Negative mappings.** A reviewer can assert that a tempting mapping is wrong (for example, *kurogwa* ≠ persecutory delusion). It is exported with `predicate_modifier: Not`. This protects the idiom from re-mapping when a later model or annotator suggests the same thing.
8. **Downstream OMOP.**
   - Only `exactMatch`/`broadMatch` rows are candidates for a "Maps to" to a standard concept.
   - `relatedMatch` rows and gaps keep the local concept as an OMOP custom concept (concept_id above 2,000,000,000).
   - Agree the exact predicate-to-"Maps to" rules with the team building the OMOP tables.
9. **Feedback loop.** Approved local concepts (versioned) are fed back to M3 as context and to triage. Future occurrences then resolve as KNOWN, which is v10's health metric.
10. **Registration.** The SSSOM set can be registered in the Mental Health Data Catalogue once it contains verified IDs. `approve.py` refuses placeholder IDs unless `--demo-placeholders` is set, and then marks the whole set "DEMO — NOT FOR REGISTRATION".

---

## 6. Keeping the layers separate

| Layer | Holds | Produced by | Stored in | Leaves the restricted environment? |
|---|---|---|---|---|
| Original utterance | exact text + span | Silver (copied) | package L1 | No |
| Normalised utterance | standard spelling + edit list | AI (M1) | package L2 | No |
| Translated text | literal + idiomatic + back-translation, per model | AI × N (M2) | package L3 | No |
| AI interpretation | candidate senses per model | AI × N (M3) | package L4 | No |
| Model agreement | clusters, standing, divergence metrics | code (M4) | package L5 | No |
| Candidate ontology concepts | retrieved IDs + model rankings + no-match votes | terminology service + AI (M5) | package L6 | No |
| AI rationale/evidence | per-sense rationale, typed evidence | AI (M3), inside L4 | package L4 | No |
| Human reviewer decision | per reviewer, per layer, blind pass | humans | review_decision records | No (audit trail) |
| Final approved interpretation | local concept + variant + approved translation and meaning; mappings or gap | adjudicated humans | Local Concept Layer, SSSOM, Gap Register | Yes. It holds meaning, not patient data. |

Two implementation details keep these separate:
- The package schema has no "approved" status.
- `approve.py` is the only code that writes to the concept layer or SSSOM, and it reads only `final: true` decisions.

---

## 7. Risks

| Risk | Where it arises | Mitigation in this design | What remains |
|---|---|---|---|
| **Hallucinated translation** | M2, especially rare dialect or Sheng forms | Literal gloss beside idiomatic; uncertainty note allowed; ring back-translation with similarity and lost-term flags; linguist review of every item | Back-translation by a similar model can repeat the same error. Token metrics are crude. |
| **Over-medicalisation of cultural expressions** | M3, and M5 ranking. Models tend to read distress as symptoms. | Prompt asks for non-medical readings and bans diagnoses; `register` and `category` fields; `over_medicalisation_risk` and `minority_clinical_reading` flags; `clinical_status` set by humans; negative mappings (`Not`) | Clinicians on the panel can pull the other way. Keep lived-experience and cultural reviewers as equal voices. |
| **Under-medicalisation / missed risk** | Normalising away a safety signal | Safety gate before the Minority Report; `risk_or_safety` category raises priority; the Minority Report never gates escalation | Safety detection upstream is outside this component. Test it separately. |
| **Premature ontology mapping** | M5; pressure to fill SSSOM | Local concept first; "no adequate match" is a valid answer; approval-only export; placeholders refused; `NoTermFound` + gap register | Reviewers may still choose a weak `relatedMatch`. Audit a sample. |
| **False model consensus** | M3–M4. Models share English-centric training data, so agreement can be correlated error (P06 "stress" is a likely case). | Diversity rule (≥ 2 families); independence (blind senses); `full_agreement_audit_candidate` flag; unanimity never auto-approves; blind human pass on a sample to measure it | Model families overlap in training data. Add a non-LLM MT baseline (e.g. NLLB-200) as a different kind of voter. |
| **Anchoring of reviewers on AI output** | Review | Blind first pass; candidates framed as evidence; human can add senses | Measure it in the pilot (agreement blind vs unblinded). |
| **Negation, attribution and temporality lost** | Silver → Minority Report | Context carried and cited; `polarity_*`, `experiencer_not_speaker` and `context_incomplete` flags; reviewers confirm context | Relies on the quality of Silver resolution. |
| **Dialect misattribution** | M1 | Dialect as hypothesis with evidence; linguist confirms | Needs dialect-competent reviewers per region. |
| **ASR errors mistaken for dialect** | Voice transcripts | `asr_correction` edit type; ASR confidence in input | — |
| **Training-data circularity** | Approved packages feed WP2 annotation and fine-tuning | Keep the fine-tuned FarajaMH model (Llama 4 Scout per the grant) out of the interpreter panel; record which model proposed what | Base-model priors can still enter through other models. |
| **Privacy / DSA** | Utterances are participant data | D1 (local hosts only; Gemini path off); package stays in the restricted environment; only L9 leaves | Free text in conversation windows can re-identify. Minimise the window. |
| **Licensing** | SNOMED CT | Pinned licensed server | **Confirm Kenya/Tanzania SNOMED CT licence coverage** and any conditions on publishing SSSOM files that contain SNOMED IDs and labels before release. |
| **Reproducibility** | Model updates and non-determinism | Digest, seed, options and prompt hashes recorded | Ollama output is not bit-identical across hardware. Treat runs as evidence, not as reproducible truth. |
| **Model capability below the task** | M1–M3, on small local models | Diversity rule; conformance repair recorded; blind human pass | Measured in `kiswa-story-v1`: two of three laptop models proposed a risk reading on every utterance and cited text from other turns as if it were the utterance, where a large model on the identical prompt proposed it on 5 of 12 with calibrated confidence. Prompt constraints assume a model that can follow them. Model scale in the interpretation stage is an open infrastructure decision (§11). |
| **Context mistaken for the utterance** | M3, when a conversation window is supplied | Typed evidence with a `conversation_turn` category distinct from `utterance_span` | Small models tag context quotes as `utterance_span`. A code-side check that evidence tagged `utterance_span` appears in the utterance is queued, not yet built. |
| **Retrieval noise from a broad ontology** | M5, with more than one system configured | "No adequate match" is a first-class answer, recorded per model; retrieval scope configurable per system | A clinically loaded but irrelevant candidate in front of a tired reviewer is a risk even when the models decline it. Audit ranked-versus-offered rates per system. |
| **Upstream drift** | Minority Report changes | Pin the upstream commit; adapt as a module, not a fork of `orchestrator.py` | Needs agreement with Slava on what goes upstream. |

---

## 8. Architecture

The diagram is in `architecture/FarajaMH_MinorityReport_Architecture_v1.svg` (PNG alongside). It uses the v10 palette.

The flow:

**Silver record → Safety gate → M1 Normalise → M2 Translate × N (+ back-translate) → M3 Interpret × N (blind) → M4 Compare (code; no winner) → M5 Retrieve concepts (SNOMED CT, MFOEM) → every model ranks → M6 Package → Human review (blind pass → per-layer decisions → adjudication) → Local Concept Layer → concept decision → SSSOM row, or `NoTermFound` + Gap Register → (OMOP downstream).**

Approved local concepts feed back into M3 context and triage.

---

## 9. Pilot: 10 constructed Swahili expressions

**Why constructed.** The pilot uses constructed utterances (`data_classification: synthetic`), not participant data, so it can run before DSA questions are settled and on any model host. The Swahili wording and dialect labels in `pilot/build_pilot_inputs.py` are drafts. **Swahili linguists and LEAB members should correct them before the run.**

| ID | Utterance (expression in bold) | What it tests |
|---|---|---|
| P01 | Tangu msiba ule, **roho yangu imeondoka** (Kiamu) | The v10 worked example; several readings; likely semantic gap |
| P02 | **Moyo wangu ni mzito** kila asubuhi | "My heart is heavy" (grant); heart ≠ cardiac; literal vs idiomatic |
| P03 | **Nina mawazo mengi**, siwezi kufanya kazi | "Thinking too much" — related to but not the same as worry or rumination |
| P04 | **Mawazo yananichoma kichwa** usiku | "Thoughts burn my head" (grant); somatic metaphor vs literal headache |
| P05 | **Nimelogwa**, ndiyo maana siwezi kulala | Bewitchment; l/r normalisation; must not become "delusion" |
| P06 | **Niko na stress mob**, siwezi lala (Sheng) | Code-mixing; two components; likely false consensus |
| P07 | **Sina raha** siku hizi | Positive control (low mood/anhedonia); *raha* = joy / peace / ease |
| P08 | **Nimechoka na maisha**, sitaki kuendelea | Safety gate must block |
| P09 | Siku hizi **sina mawazo mengi** kama zamani | Negation (improvement) must reach reviewers |
| P10 | Mama yangu **hana raha** tangu baba afariki | Experiencer is the mother; bereavement onset |

**Dry-run results (SIMULATED fixtures; these test mechanics, not language ability):**

| ID | Sense clusters (standing) | Transl. agreement | Priority: flags |
|---|---|---|---|
| P01 | inner emptiness (maj), grief (maj), spiritual loss (min), loss of vitality (min), fright (min) | 0.11 | high: translation + sense divergence, back-translation mismatch, *roho* lost, possible gap |
| P02 | sadness (unanimous), morning reluctance (min), chest heaviness (min) | 0.63 | high: minority clinical reading, over-medicalisation risk |
| P03 | thinking too much (maj), worry (maj), life stressors, rumination, functional impairment (min) | 0.28 | high: sense + register divergence, over-medicalisation risk |
| P04 | thinking too much (unanimous), burning head, intrusive thoughts, headache (min) | 0.36 | high: minority clinical reading ("headache") |
| P05 | bewitchment explanation (unanimous), sleep difficulty, interpersonal conflict, persecutory belief (min) | 0.53 | high: minority clinical reading, over-medicalisation risk |
| P06 | stress (unanimous), sleep difficulty (unanimous) | 0.70 | high: multiple components, full-agreement audit candidate |
| P07 | low mood (maj), loss of pleasure (min), lack of peace (min) | 0.33 | high: translation divergence (joy / happy / peace) |
| P08 | — | — | **blocked_pending_safety_escalation** (no model call made) |
| P09 | thinking too much (maj), worry (min) | 0.29 | high: `polarity_negated` |
| P10 | grief (maj), low mood (min), lack of peace (min) | 0.47 | high: `experiencer_not_speaker` |

The simulated review decisions for P02, P03 and P05 produced:
- 3 local concepts;
- 6 SSSOM rows: 2 approved, 2 `Not`, 2 `NoTermFound`;
- 2 gap-register entries.

These are in `out/approved/`, labelled DEMO. One honest finding from the dry run: **almost everything is "high" priority.** The flag thresholds are not yet discriminating. Calibrating them on live output is one of the pilot's jobs.

**Protocol**
1. **Correct the inputs** with 2 linguists (one Kenyan coast, one Tanzanian) and 2 LEAB members. For P01, P03 and P07 add a second context variant each (e.g. *roho imeondoka* after a fright rather than a death) to test context sensitivity: about 13 items.
2. **Live run.** At least 3 models from at least 2 families on the project Ollama host (e.g. Gemma 3 27B, Qwen 3 32B, Llama 3.3 70B; check Swahili quality first). Add an NLLB-200 translation as a non-LLM baseline in M2. Point Snowstorm at a licensed SNOMED CT edition and OLS at MFOEM, with versions pinned. Run twice with different seeds to see run-to-run variation.
3. **Review.**
   - 4 roles (linguist, cultural expert, clinician, lived experience) review every item.
   - Half of the reviewers do the blind first pass on half of the items.
   - An adjudicator records final decisions.
   - Time each review.
4. **Measure**, with criteria set in advance:

   | Metric | Definition | Suggested target |
   |---|---|---|
   | Sense recall | Approved meaning appears in at least one AI cluster | ≥ 80% |
   | Minority value | Share of approved meanings that were a *minority* cluster | Report; above 0 justifies keeping minorities |
   | False-consensus rate | Unanimous clusters that reviewers rejected | Report; target low |
   | Over-medicalisation rate | Items approved as non-clinical where any model proposed a clinical sense | Report per model |
   | ID validity | Package IDs that exist in the pinned release | 100% (a hard requirement) |
   | Translation adequacy | Linguist rating 1–5 per candidate | Median ≥ 4 for at least one candidate |
   | Anchoring | Reviewer–AI agreement, blind vs unblinded | Report |
   | Review time per item | Minutes | Decides whether the approach scales |

5. **Decide.** Compare the results with the targets, then decide whether to integrate with the Silver → Stage 1 interface, and recalibrate the flag thresholds.

**How to run the kit**
```bash
pip install jsonschema pyyaml pytest
python pilot/build_pilot_inputs.py && python pilot/build_fixtures.py
python -m mr_farajamh.cli run --input pilot/utterances.jsonl --out out --fixture       # simulated
python -m mr_farajamh.cli approve --out out --decisions pilot/review_decisions_SIMULATED.jsonl --demo-placeholders
python -m pytest -q tests                                                               # 66 tests
# live: edit config/pilot.yaml (hosts, models, Snowstorm/OLS endpoints, versions), then run without --fixture
```

---

## 10. Run log

Newest first. Each entry records what a run showed and what changed because of it. Runs are evidence,
not reproducible truth: Ollama output is not bit-identical across hardware.

### 30 September 2026 · `kiswa-story-v1` · twelve-turn Kiswahili session, both ontologies live

Twelve turns of one simulated home visit, in standard Kiswahili and Sheng, each carrying the CHW
question that prompted it. MFOEM and MFOMD both live. First run on connected conversational context
rather than isolated utterances.

**What worked.** Turn 07, *"Wanasema nimerogwa"* — the family says she has been bewitched — produced
spiritual clusters with no concepts retrieved and a unanimous "no adequate match". A culturally
normative explanation was recorded as a gap rather than forced onto a delusion concept, with
`over_medicalisation_risk` and `possible_semantic_gap` both raised. The language guard held: the Sheng
turn (*"Niko down sana, stress imezidi"*) passed normalisation unchanged and no package raised
`normalisation_changed_language`.

**What failed.** `risk_or_safety` was proposed on **all twelve** utterances, including one about who
supports the speaker. By model: Gemma 12/12 (43% of all senses it proposed), Llama 12/12 (46%), Qwen
1/12 (9%). Seven risk senses cited text from a *different turn*, or from the CHW's own question, tagged
`utterance_span`. And the clustering rewarded it: on turn 05 three models said one thing in three
wordings and produced three separate *minority* clusters, while the rote risk sense, phrased almost
identically by two models, merged into a *majority*. Standing was measuring phrasing similarity, not
agreement about meaning.

**The controlled comparison.** The same twelve prompts, with the same upstream normalisations and
translations, were run through a single large model. It proposed `risk_or_safety` on **5 of 12**, cited
zero quotes outside the utterance, tagged context from other turns as `conversation_turn` rather than
`utterance_span`, and spread its plausibility from 0.15 to 0.92 — with 0.92 on the one genuinely
risk-bearing turn. The small models rated fabricated risk senses at 0.8 and 0.9.

**The conclusion, which changed the planned fix.** The prompt is not at fault. The risk rule in
`interpret.md` is followed correctly by a capable model; rewriting it to suit a 7B model would break it
for any model the project moves to later. What this run argues for is the evidence check below, and a
decision about model scale in the interpretation stage that is a governance and infrastructure
question, not a prompt question.

**Retrieval.** MFOEM offered 45 candidates across the twelve packages and a model ranked 17 of them
(38%). MFOMD offered 60 and a model ranked 8 (13%), including `binge-eating disorder` and
`abstinence syndrome` against a Kiswahili distress idiom. The models declined them correctly, but
clinically loaded noise in front of a tired reviewer is itself a risk. MFOMD retrieval needs tightening
or parking; that decision is open.

**Changes queued, not yet made:** `conform.sense()` to verify that evidence tagged `utterance_span`
actually appears in the utterance, downgrading it otherwise; the model-risk banner to key on standing
rather than presence.

### 29 September 2026 · `qrec-dryrun-v7` · English clinical-interview answers

Thirty-four patient answers from another system's Question Recommender dry run — English, elicited by
PHQ-9 and GAD-7 items rather than volunteered. The wrong material for interpretation and the right
material for testing the safety screen.

| Fault | Cause | Fix |
|---|---|---|
| M1 translated English into Kiswahili — *"Not good at all"* became *"Si nzuri kabisa"*, with the substitutions recorded as `asr_correction`, and *"killing"* recorded as an `orthographic` edit. Every later stage ran on Kiswahili the pipeline invented, and the edit log claimed spelling fixes. | `normalise.md` never received `language_declared`, and its framing ("normalise to standard Swahili") made translation the obedient reading. | `conform.language_changed`: rejects a normalisation whose primary language subtag differs from the declared one, or that retains too few of the original tokens, and restores the original text. Code-switching and Sheng pass by design. `normalise.md` reframed around the languages present. |
| The risk banner fired backwards. *"Not good at all"* carried a full banner whose every lexicon match sat in the models' own gap notes — one of them `nife` matched inside the word *manifestations*. *"Yes, I do feel like killing people who annoy me"*, read as `risk_or_safety` by all three models unanimously, carried no banner at all. | `_safety_banner` fired only on the lexicon. Model consensus on a risk reading raised nothing. | Two banners, firing independently: one for the lexicon, one for a model-proposed risk reading. The lexicon banner now says when every match is in model-generated text. |
| MFOMD retrieved real concepts and the package was rejected at validation, after the models had run and before anything was written. | Clients were made config-driven; the `system` enum in the package schema and the CURIE prefixes in `approve.py` were not. | Both updated, plus tests asserting that every configured terminology appears in the schema enum and has a prefix and an `object_source`. |

**The safety measurement.** Nine of the 34 turns were risk-bearing in context. The lexicon reached
**two**. Six were reachable only because the *question* was a risk question — a detector that does not
exist. One (*"Dying maybe"*, answering *"what would help you feel better"*) was reachable by neither and
had to be hand-marked. The `nife` false positive is a substring match fixed in lexicon `0.2.0`; the
0.1.0 screen was still deployed.

### 26 September 2026 · v0.2.4 · a safety failure, and what it changed

Run `TRY-BA9BBCEC`, on the expression **"Na kwazika kiroho sana nataka nitoke duniani"** — *…I want to leave the world*.

Three models (Gemma 3 12B, Qwen 2.5 7B, Llama 3.1 8B) proposed five senses between them. Not one carried the category `risk_or_safety`. Category support read `emotional_state 3/3, social_or_relational 1/3`. The package went to `awaiting_review` with four risk flags, none of them about safety, and a review card whose first substantive content was "sadness / overwhelm" and three MFOEM emotion concepts.

Gemma 3 wrote, in the `uncertainty_note` that is printed on the card:

> "The phrase 'nitoke duniani' is hyperbolic, expressing a strong desire to escape, rather than a literal suicidal statement. It's crucial to avoid clinical interpretations."

A 12B model ruled out suicidal ideation. That is not a judgement any model in this pipeline is entitled to make.

**Three failures stacked, and each one is instructive.**

1. *The prompt caused it.* After the false-consensus fault in §9b, `interpret.md` was rewritten with "Give a clinical reading only if the context supports it" and "Many expressions of distress are ordinary language, not symptoms of a disorder." That guard against over-medicalisation had no exception for risk, so it suppressed the one reading where a false negative is dangerous and a false positive is nearly free. **A guard written against one failure mode created another.** Every prompt constraint in this pipeline should now be checked for what it forbids as well as what it permits.

2. *The models were the only net.* Duty D2 holds any utterance where `safety.flag` is true, but that flag is set upstream by the v10 safety check, which does not run on the curation path. The `try` command printed a warning about exactly this. The design assumed a detector that was not there.

3. *The signal existed and never surfaced.* The concept ranker wrote, in a gap note in the same package, "the candidate meaning includes a desire to end one's life (suicidal ideation)". L7 computed risk flags from sense categories only, so L6 could contain the words "suicidal ideation" while the card said `sadness`.

**Changes**

| Change | Where |
|---|---|
| Model-independent lexicon screen over the utterance, normalisation, every translation, every sense gloss and rationale, and every gap note. Deliberately over-inclusive; does not resolve negation. | new `mr_farajamh/safety.py` |
| `interpret.md` now requires a `risk_or_safety` sense whenever the utterance touches dying, leaving the world, not wanting to live, ending things, or harm to self or others — as an addition to other senses, overriding the anti-over-medicalisation rules, and with an explicit ban on arguing a risk reading away | `prompts/interpret.md` |
| `translate.md` forbids softening risk language or using `uncertainty_note` to rule it out | `prompts/translate.md` |
| New flags `risk_language_detected` and `risk_language_missed_by_models`; both force `high` priority and add a clinician to the reviewer roles | `pipeline.py`, `L7_review_signals.safety_signals` |
| Warning banner at the **top** of the review card, above the blind pass — a reviewer who has already read "sadness" is anchored | `review.py` |
| On `run`, risk language in non-synthetic data raises `safety.flag` with `flag_source: curation_lexicon_screen`, so D2 holds the package and no model sees the utterance. On `try` (constructed examples only) it is recorded and shown loudly but does not block, because the vocabulary has to be able to cover these expressions. | `cli.py` |
| Ranker starts from the assumption that no retrieved concept fits | `prompts/rank_concepts.md` |

Replaying the original package through the new code produces 17 matches across six fields and both flags.

**The limitation to state plainly:** the lexicon is a keyword screen written without clinical input, versioned `0.1.0-unvalidated`. It must be reviewed by clinicians, LEAB members and the Swahili linguists before this pipeline touches participant data, and it will miss indirect phrasings — which is the argument for keeping the model-side requirement as well. Neither net is sufficient alone.

**The general lesson.** The design principle is *AI proposes → models compare → humans interpret and validate*. This run shows the principle has a gap: **models can also propose the absence of something**, and a shared absence is invisible to a disagreement detector. Nothing in the agreement machinery can flag a reading that no model offered. Wherever a missing candidate is dangerous rather than merely incomplete, there must be a check that does not run on model output.

---

### 23 September 2026 · v0.2 · first live run

The first run with real models (Gemma 3 12B, Qwen 2.5 7B, Llama 3.1 8B on a laptop, expression *moyo wangu unauma*) exposed three faults. All three are fixed in v0.2; none of them was visible in the simulated run.

| Fault seen | Cause | Fix in v0.2 |
|---|---|---|
| "Spiritual affliction" proposed by all three models, and therefore recorded as **unanimous** | `interpret.md` listed "spiritual" among the example categories and used "spiritual affliction" as an example `sense_key`. The prompt manufactured the consensus it was supposed to detect. | The prompt now asks only for readings the model can support from the words or context, forbids a supernatural reading unless something in the utterance or context points to it, tells the model that fewer senses is a better answer, caps plausibility at 0.3 for senses resting only on background knowledge, and rejects empty rationales. |
| Every back-translation similarity was 0.0 ("Ndiyo kusimamia kusimamia kusimamia"), so the mismatch flag fired on everything | Models of this size translate English into Swahili badly. Unusable output was being scored as disagreement. | Degenerate output (repeated or very short) is detected and recorded as **not assessed** rather than 0. The new flag is `back_translation_not_assessed`. The stage can be pointed at a dedicated translation model or switched `off`, which raises `back_translation_disabled`. The lost-cultural-term check now skips unusable back-translations. |
| One meaning split across three clusters ("sadness", "emotional pain", "somatic experience" / "physical discomfort") | Clustering compared words, not meaning. | Optional sentence embeddings via Ollama (`models.embedding_model`, threshold `agreement.embedding_similarity_threshold`). Cluster labels and categories are now decided by majority among members. Packages record `clustering_method`, so a reviewer can see whether words or meaning did the grouping. Without an embedding model it falls back to word overlap and says so. |

Two lessons worth carrying into the wider pilot:
- **Agreement among models is only evidence when the prompt has not steered them.** Prompt wording should be reviewed as carefully as the design, and the blind human pass is what catches this.
- **A quality check that always fires is worse than none**, because it trains reviewers to ignore flags. Prefer "not assessed" to a false signal.

---

## 11. Open decisions

1. SSSOM subject: local concept (recommended) or raw expression, as in v10 now.
2. Whether to keep "is evidence for" as a FarajaMH predicate or use SKOS mapping predicates only.
3. Which models are on the DSA-approved host, and whether any Swahili-specialised model is available to add to the panel.
4. SNOMED CT licence coverage for Kenya/Tanzania, and publication conditions for mapping files.
5. Reviewer roster per role and site, pseudonymous IDs for LEAB members, and who adjudicates.
6. Upstream strategy with Slava. I suggest contributing three general features back to the Minority Report and keeping FarajaMH logic in its own module:
   - pluggable consensus/arbitration;
   - a source-language parameter;
   - model digest and prompt hash in provenance.
