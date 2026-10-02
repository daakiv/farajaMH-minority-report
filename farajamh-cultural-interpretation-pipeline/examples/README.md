# Worked examples

Two packages from run `example-v2` (2 October 2026), produced with `config/laptop.yaml` — the default
configuration, so these are what the pipeline produces on a clean clone. Each comes with the reviewer
card generated from it.

```
KISWA-STORY-03.package.json      KISWA-STORY-03.review-card.md
KISWA-STORY-07.package.json      KISWA-STORY-07.review-card.md
```

**This is constructed data.** The twelve-turn Kiswahili session in `pilot/kiswahili_story.jsonl` was
written with model assistance to exercise the pipeline. It has not been reviewed by Kiswahili speakers
and is not validated linguistic material. No participant data appears anywhere in this repository.

Read the card first — it is what a reviewer sees. Read the package when you want the provenance:
model digests, prompt hashes, terminology releases, the evidence each model cited, and the agreement
metrics.

## 03 — a mapping found, and a gap beside it

> Usingizi umenikimbia. Nakesha hadi alfajiri nikiwaza.
> *(Sleep has fled me. I stay awake until dawn, thinking.)*

| cluster | reading | standing | concept |
|---|---|---|---|
| C1 | sleep difficulty | unanimous, 3/3 | `MFOMD:0000116` insomnia — ranked 1 by all three |
| C2 | sadness | majority, 2/3 | `MFOEM:000056` sadness — ranked 1 by all three |
| C3 | risk or safety | majority, 2/3 | **nothing retrieved**, unanimous "no adequate concept" |

The whole mechanism in one package. A unanimous somatic reading maps cleanly. A majority emotional
reading maps cleanly. A majority *risk* reading finds no adequate concept in either vocabulary and is
recorded as a semantic gap rather than forced onto the nearest clinical term — which is what the
FarajaMH Local Concept Layer exists for. `over_medicalisation_risk` is raised because clinical and
everyday readings coexist.

## 07 — a culturally normative explanation, not a delusion

> Wanasema nimerogwa. Shangazi ameniambia niende kwa mganga.
> *(They say I have been bewitched. My aunt has told me to go to a traditional healer.)*

| cluster | reading | standing | concept |
|---|---|---|---|
| C1 | distress | majority, 2/3 | nine candidates; only `MFOEM:000031` crying ranked, by one model |
| C2 | risk or safety | majority, 2/3 | nothing retrieved, unanimous no adequate concept |
| C3 | spiritual disruption | minority, 1/3 | nothing retrieved, unanimous no adequate concept |
| C4 | bewitchment | minority, 1/3 | nothing retrieved, unanimous no adequate concept |

This is the case the adaptation was built for. Two spiritual readings survive as **minority** clusters
rather than being resolved away, and no vocabulary offers a concept for either. An arbitration step
would have selected the majority reading; MFOEM and MFOMD between them would have offered a delusion or
paranoia concept for an explanation that is culturally normative in this setting. Neither happened. The
gap is recorded, four reviewer roles are requested, and nothing is decided.

## Three things in these outputs that are wrong

Shown rather than hidden, because a worked example that only demonstrates success is not evidence.

**llama3.1:8b proposes `exactMatch` almost everywhere.** It did so twelve times across the twelve
utterances in this run, including on both clusters in 03, against a prompt that asks for `broadMatch`
where the cultural meaning is richer than the concept. gemma3:12b and qwen2.5:7b both comply. See the
1 October run-log entry in DESIGN.md.

**On 07, `MFOEM:000031 crying` is ranked `exactMatch` for a distress reading**, by that same model. The
other two voted no adequate concept. The disagreement is visible on the card, which is the point, but
the proposal is wrong.

**gemma3:12b returns a ranked concept and "no adequate match" at the same time.** On 03 it ranks
insomnia first *and* votes no-adequate-match on the same cluster. Both are recorded, so the card shows
a contradiction. The human decision in `approve.py` is taken on the reviewer's verdict rather than on
model votes, so no incoherent mapping can be produced from it — but the card is confusing and the
ranking prompt should forbid it.

## What is not in these examples

SNOMED CT. It is configured but not enabled: `config/laptop.yaml` explains why, and the 1 October
run-log entry has the measurements. `config/laptop_snomed.yaml` reproduces that experiment.
