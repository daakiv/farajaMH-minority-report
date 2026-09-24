# farajamh-minority-report (pilot kit v0.1)

This kit adapts the CODATA Minority Report (github.com/codata/the-minority-report @ a7cb9cb) for FarajaMH Stage 1: AI-assisted translation and candidate interpretation of Swahili idioms of distress, with human review before anything is accepted.

Start with **DESIGN.md**, which covers the assessment, component mapping, schemas, risks and pilot plan. The architecture diagram is in `architecture/`.

| Path | What it is |
|---|---|
| `schemas/` | JSON Schemas: utterance input, candidate package (layers L1–L7), review decision |
| `prompts/` | normalise, translate, back_translate, interpret, rank_concepts |
| `policy/farajamh_mr_odrl.jsonld` | ODRL duties D1–D5, P1–P2 (enforced in `mr_farajamh/policy.py`, `approve.py`) |
| `config/pilot.yaml` | model hosts and panel, terminology endpoints and versions, thresholds |
| `mr_farajamh/` | pipeline (M1–M6), agreement, terminology clients, review export, approval → LCL/SSSOM/gap |
| `pilot/` | 10 constructed Swahili utterances, SIMULATED fixtures, SIMULATED review decisions |
| `out/` | dry-run output: packages, review cards, review sheet, approved/ (DEMO) |
| `tests/` | 9 tests for the rules that must hold whatever the models say |

```bash
pip install -r requirements.txt
python -m mr_farajamh.cli run --input pilot/utterances.jsonl --out out --fixture
python -m mr_farajamh.cli approve --out out --decisions pilot/review_decisions_SIMULATED.jsonl --demo-placeholders
python -m pytest -q tests
```

**Important:**
- The fixtures are hand-written stand-ins for model output.
- Concept IDs such as `SCTID:LOOKUP-feeling-sad` are placeholders, not codes.
- The Swahili examples need correcting by linguists and LEAB members before the live pilot.
