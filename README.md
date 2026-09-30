# FarajaMH Minority Report

FarajaMH Minority Report is a FarajaMH-specific adaptation of the [CODATA Minority Report](https://github.com/codata/the-minority-report) by Slava Tykhonov (CODATA). It applies a multi-model translation and interpretation approach to culturally grounded mental-health expressions, including Kiswahili, Sheng and code-switched language.

## What “Minority Report” means here

The name is the upstream project's, from Philip K. Dick's 1956 story: three predictors are asked the same question, the two whose accounts overlap most become the *majority report*, and the dissenting third — the *minority report* — is buried. The framework is named for that dissenting account.

In this adaptation it is also the design decision. When models suggest different plausible meanings, a less-supported reading should not disappear just because more models proposed another one. The workflow keeps majority and minority readings visible for review. A minority reading is a candidate, not a conclusion.

**AI proposes. Models compare and surface disagreement. Human experts interpret and validate.** The system does not diagnose, accept an interpretation, or approve a semantic mapping.

## What this adaptation changes

The upstream framework translates authoritative technical terminology into European and UN languages, and resolves disagreement: an arbitrator selects one "most standard" term, and dissenting outputs are recorded as *"Arbitration lost"*.

FarajaMH removes the arbitrator. For expressions of distress there is no authoritative source term to converge on, and the reading supported by fewest models is disproportionately likely to be the culturally specific one — the reading a Kiswahili-speaking reviewer most needs to see. Nothing decides between the models; disagreement is carried to a human reviewer and labelled.

The infrastructure carries over largely intact: multi-model dispatch on Ollama, model-to-host routing, JSON repair, prompt-as-file templates, ODRL policy enforced at runtime, the OntoPortal client, and PROV and SHA-256 provenance.

## How it works

![The FarajaMH interpretation workflow in six steps, grouped under three headings. Nothing is lost or unscreened: step one preserves the source and its context; step two is a safety screen using a fixed risk lexicon, before any model call. Disagreement is kept, not resolved away: step three is candidate generation, where one normaliser feeds three models that translate and interpret separately; step four is the Minority Report step, comparing readings and ranking concepts, where a majority emotional reading and a minority somatic reading both continue to review. A person decides, and the record says so: step five is human review, where experts validate meaning and mapping; step six is a governed record — a local concept, an approved mapping, or a recorded gap — only after approval. Safety runs twice, on the input and on everything the models generate. Models run locally or inside the approved environment, and restricted participant data never goes to an external model host.](images/farajamh-interpretation-workflow.png)

Six steps, grouped under three commitments.

**Nothing is lost or unscreened.** The original wording is kept exactly as it was said, with its context (1). Before any model is called, a fixed risk lexicon screens the text — a word list, not a model, so it does not depend on the models noticing anything (2).

**Disagreement is kept, not resolved away.** One model normalises spelling and dialect variation, recording every edit; three models then translate and interpret separately (3). Their readings are clustered, and a reading supported by fewer models is retained and labelled rather than dropped (4). Concepts retrieved from the terminology services are ranked here too — the models rank what was retrieved and never originate an identifier.

**A person decides, and the record says so.** Experts validate the meaning first, in a blind pass before they see the AI candidates, and only then consider whether an external concept fits (5). What leaves the pipeline is one of three things: an approved local concept, an approved mapping, or a recorded semantic gap — and only after approval (6).

Safety runs twice: once on the source before any model call, and once on everything the models generated, including their reasoning. Models run locally or inside the approved environment; restricted participant data is not sent to external model hosts.

## FarajaMH context

The pilot covers the candidate-generation stage before human review. It keeps the original utterance and relevant context distinct from normalised wording, translations, interpretations and ontology candidates. Models can propose multiple readings and rank concepts retrieved from terminology services. A model never originates a concept identifier; identifiers come only from a live terminology service response.

The current configuration includes **MFOEM** for emotion-related concepts and **MFOMD** for mental-disorder concepts, both via EMBL-EBI OLS4. **SNOMED CT** is configured but not enabled: it requires a licence covering Kenya and Tanzania, and a terminology server. These are candidate sources for reviewers to assess; they are not mandatory destinations for every expression. If no external concept adequately captures a validated meaning, FarajaMH can retain it in the **Local Concept Layer** and record the semantic gap. A mapping is created only after human approval.

## Design and implementation

The [detailed design](farajamh-cultural-interpretation-pipeline/DESIGN.md) explains the upstream assessment, how CODATA components were adapted, the proposed workflow and schemas, governance risks, and the constructed-utterance pilot.

The [implementation and pilot README](farajamh-cultural-interpretation-pipeline/README.md) describes the code, configuration, test fixtures and how to run the pilot.

## Pilot status

This is a research pilot for workflow development and evaluation. Constructed examples and simulated outputs test the software mechanics; they do not establish linguistic or clinical validity. Expressions, interpretations and mappings require review by relevant linguistic, cultural, clinical and lived-experience experts before any use with participant data or downstream systems.

Limitations identified in live runs — including the extent to which interpretation is independent, and how model scale affects the proposal of risk-related readings — are recorded in the design document rather than left implicit.
