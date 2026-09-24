"""Generates FarajaMH_MinorityReport_Architecture_v1.svg in the v10 palette."""
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 1700, 990
NAVY, TEAL, BLUE, RED, ORANGE, GREEN, GREY, INK = "#17356B", "#1A7E8C", "#3B4FA8", "#C0392B", "#D97E1F", "#17694A", "#9AA5AA", "#1A2E35"
o = []


def rect(x, y, w, h, stroke, fill="#FFFFFF", sw=1.6, rx=9, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def text(x, y, s, size=10, color=INK, weight="400", anchor="start", italic=False):
    st = ' font-style="italic"' if italic else ""
    o.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}"{st}>{escape(s)}</text>')


def lines(x, y, items, size=9.5, color=INK, lh=13.5, bullet=True):
    for i, s in enumerate(items):
        text(x, y + i * lh, ("•  " if bullet else "") + s, size, color)


def header(x, y, w, title, color, h=26):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{color}"/>')
    o.append(f'<rect x="{x}" y="{y + h - 9}" width="{w}" height="9" fill="{color}"/>')
    text(x + w / 2, y + 17.5, title, 11, "#FFFFFF", "700", "middle")


def arrow(path, color, marker, sw=1.8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="{sw}"{d} marker-end="url(#{marker})"/>')


def chip(x, y, label, color, w=None):
    w = w or (len(label) * 5.6 + 14)
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="16" rx="8" fill="{color}" opacity="0.14"/>')
    text(x + 7, y + 11.5, label, 8.5, color, "700")
    return w


o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="DejaVu Sans, sans-serif">')
o.append("<defs>" + "".join(
    f'<marker id="{n}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
    f'<path d="M2 1L8 5L2 9" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></marker>'
    for n, c in (("ab", BLUE), ("ar", RED), ("ao", ORANGE), ("ag", GREEN), ("an", NAVY), ("ay", GREY))) + "</defs>")
o.append(f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>')

text(W / 2, 38, "FARAJAMH-ADAPTED MINORITY REPORT", 30, NAVY, "700", "middle")
text(W / 2, 64, "Stage 1 of the v10 architecture: AI-assisted translation & candidate interpretation, from raw utterance to human-approved meaning", 14, TEAL, "700", "middle")
rect(20, 78, W - 40, 30, NAVY, "#F2F6FA", 1.4, 8)
text(W / 2, 98, "AI proposes  →  models compare & disagree  →  humans interpret & validate  →  local concept first  →  semantic mappings only after approval", 13, NAVY, "700", "middle")

# ---- Silver input
rect(20, 140, 160, 420, GREY, "#F4F6F7")
header(20, 140, 160, "INPUT (from Silver)", "#5C6A70")
lines(30, 188, ["Original utterance", "Expression span", "Modality / ASR info", "Context resolved", "in Silver:", "– negation", "– temporality", "– attribution", "– speaker, setting", "– region, dialect", "Conversation window", "Triage route:", "– NEW or NEAR MATCH", "   (different concept)", "Safety flag", "Data class"], 9.3, INK, 14.5, False)
text(100, 425 + 110, "schema: utterance_input", 8.5, "#5C6A70", "400", "middle", True)

# ---- safety gate
rect(194, 140, 142, 420, RED, "#FDF0EF")
header(194, 140, 142, "SAFETY GATE", "#A3161C")
lines(204, 190, ["Runs before triage", "(v10 step 1).", "", "Flagged and NOT", "escalated →", "BLOCKED.", "No model sees it.", "", "Clinician escalation", "never waits for", "interpretation.", "", "Curation may follow", "after escalation is", "recorded."], 9.3, INK, 14.5, False)
text(265, 545, "policy D2", 8.5, RED, "700", "middle")
arrow("M180 350 L192 350", GREY, "ay")
arrow("M336 350 L348 350", BLUE, "ab")

# ---- Minority Report container
MX, MY, MW, MH = 350, 140, 650, 420
rect(MX, MY, MW, MH, BLUE, "#F7F8FD", 2)
header(MX, MY, MW, "FARAJAMH MINORITY REPORT  —  AI candidate generation & disagreement detection (never decides)", BLUE, 28)
stages = [
    ("M1  NORMALISE", ["1 model + rule list", "l/r variants, Sheng, ASR", "Every edit recorded", "Code-switch segments", "Original never altered"], "adapted: new prompt"),
    ("M2  TRANSLATE × N", ["Each model independently", "Literal gloss + idiomatic", "Keep roho / moyo / mawazo", "Ring back-translation", "Flag lost cultural terms"], "modified: voter prompt"),
    ("M3  INTERPRET × N", ["1–4 senses per model", "Blind to other models", "Non-medical readings kept", "Rationale + evidence spans", "Uses Silver context"], "new"),
    ("M4  COMPARE", ["Code, not an LLM", "Cluster senses; no winner", "Unanimous/majority/minority", "Divergence & risk flags", "Minority readings kept"], "replaces arbitrator"),
    ("M5  CONCEPT CANDIDATES", ["Query SNOMED CT (Snowstorm)", "+ MFOEM (OLS) in parallel", "Every model ranks", "IDs only from retrieval", "'No adequate match' valid"], "extends ontoportal.py"),
    ("M6  PACKAGE", ["Layers L1–L7, provenance", "Model digests, prompt hashes", "Review priority + roles", "Confidence as components", "status = awaiting_review"], "extends Croissant/PROV"),
]
bw, bh = 200, 176
for i, (t, items, reuse) in enumerate(stages):
    cx, cy = MX + 14 + (i % 3) * (bw + 12), MY + 42 + (i // 3) * (bh + 14)
    rect(cx, cy, bw, bh, BLUE, "#FFFFFF", 1.3, 7)
    text(cx + 10, cy + 20, t, 11, BLUE, "700")
    lines(cx + 10, cy + 42, items, 9.2, INK, 15)
    col = GREEN if reuse.startswith(("adapted", "extends")) else (ORANGE if reuse.startswith(("modified", "replaces")) else RED)
    chip(cx + 10, cy + bh - 26, reuse, col)
    if i % 3 < 2:
        arrow(f"M{cx + bw} {cy + bh / 2} L{cx + bw + 10} {cy + bh / 2}", BLUE, "ab", 1.5)
# row wrap arrow M3 -> M4
x3 = MX + 14 + 2 * (bw + 12) + bw / 2
x4 = MX + 14 + bw / 2
arrow(f"M{x3} {MY + 42 + bh} L{x3} {MY + 42 + bh + 7} L{x4} {MY + 42 + bh + 7} L{x4} {MY + 42 + bh + 12}", BLUE, "ab", 1.5)
arrow(f"M{MX + MW} 350 L{MX + MW + 12} 350", BLUE, "ab")

# ---- Human review
HX = 1014
rect(HX, 140, 186, 420, RED, "#FFFFFF", 1.8)
header(HX, 140, 186, "HUMAN REVIEW (stage 2)", RED)
lines(HX + 10, 188, ["Linguist", "Cultural expert", "Clinician", "Lived experience (LEAB)"], 9.5, INK, 14.5)
lines(HX + 10, 256, ["1. Blind first pass on a", "   sample: own reading", "   before seeing AI", "2. Decide each layer", "   separately: normalise,", "   translate, interpret,", "   context, concepts", "3. May add a sense no", "   model proposed", "4. Adjudicator records", "   final decision", "", "AI candidates are", "evidence, not defaults."], 9.3, INK, 14.5, False)
text(HX + 93, 545, "schema: review_decision", 8.5, RED, "400", "middle", True)
arrow(f"M{HX + 186} 350 L{HX + 198} 350", RED, "ar")

# ---- right column
RX, RW = 1212, 468
rect(RX, 140, RW, 112, ORANGE, "#FFFDF8", 1.8)
header(RX, 140, RW, "LOCAL CONCEPT LAYER (stage 2.5) — written only after a final decision", ORANGE)
lines(RX + 10, 186, ["Create a concept or add a variant (dialect, region, spelling); approved translation and meaning",
                     "clinical_status: non-clinical cultural / possible indicator / symptom expression / safety-relevant",
                     "Valid even with no external concept. Holds meaning, not patient data."], 9.3, INK, 15)
rect(RX, 264, RW, 104, GREEN, "#F0F7F3", 1.6)
header(RX, 264, RW, "CONCEPT DECISION per approved meaning (v10 stages 3–4)", GREEN)
lines(RX + 10, 308, ["approve → predicate (exact / broad / narrow / related) + reviewer confidence",
                     "reject with 'Not' → recorded negative mapping (e.g. bewitchment ≠ persecutory delusion)",
                     "no adequate concept → semantic gap (not a failure)      defer → nothing leaves the package"], 9.3, INK, 15)
arrow(f"M{RX + RW / 2} 252 L{RX + RW / 2} 262", ORANGE, "ao")
rect(RX, 382, 228, 108, NAVY, "#FFFFFF", 1.8)
header(RX, 382, 228, "SSSOM (governed output)", NAVY)
lines(RX + 10, 426, ["subject = local concept (FMHLC)", "ManualMappingCuration", "author / reviewer IDs", "tool + version, dates", "package ID in comment"], 9, INK, 13)
rect(RX + 240, 382, 228, 108, RED, "#FDF0EF", 1.6, dash="6 3")
header(RX + 240, 382, 228, "SEMANTIC GAP", RED)
lines(RX + 250, 426, ["object_id = sssom:NoTermFound", "Gap Register entry", "→ ontology extension request", "Concept stays usable locally", "(OMOP custom concept)"], 9, INK, 13)
arrow(f"M{RX + 114} 368 L{RX + 114} 380", NAVY, "an")
arrow(f"M{RX + 354} 368 L{RX + 354} 380", RED, "ar")
rect(RX, 504, RW, 56, GREY, "#F4F6F7", 1.3)
text(RX + 10, 524, "OMOP (downstream, out of scope here)", 10, NAVY, "700")
text(RX + 10, 539, "exact / broad → candidate 'Maps to' a standard concept; related & gaps → local custom concept", 9, INK)
text(RX + 10, 552, "(ID > 2 billion). Which predicates produce 'Maps to' is to be agreed with the OMOP team.", 9, "#5C6A70", italic=True)

# feedback loop
arrow(f"M{RX + 30} 140 L{RX + 30} 126 L{MX + 538} 126 L{MX + 538} 138", ORANGE, "ao", 1.6, "7 4")
rect(MX + 552, 119, 290, 14, "#FFFFFF", "#FFFFFF", 0, 3)
text(MX + 697, 130, "approved local concepts feed M3 context & triage (versioned)", 9, ORANGE, "400", "middle", True)

# ---- layer separation band
text(20, 594, "WHAT EACH LAYER HOLDS — kept separate so any output can be traced back and reviewed", 13, NAVY, "700")
layers = [
    ("L1 Original utterance", "Silver (copied)", BLUE, "restricted", ["Exact text + span", "Never edited"]),
    ("L2 Normalised", "AI", BLUE, "restricted", ["Standard spelling", "Edit list"]),
    ("L3 Translations", "AI × N", BLUE, "restricted", ["Literal + idiomatic", "Back-translations"]),
    ("L4 Interpretations", "AI × N", BLUE, "restricted", ["Candidate senses", "Rationale, evidence"]),
    ("L5 Agreement", "Code", BLUE, "restricted", ["Clusters, standing", "Divergence flags"]),
    ("L6 Concept candidates", "Service + AI rank", BLUE, "restricted", ["Retrieved IDs only", "No-match votes"]),
    ("L7 Review signals", "Code", BLUE, "restricted", ["Priority, risk flags", "Confidence parts"]),
    ("L8 Reviewer decisions", "Humans", RED, "restricted", ["Per reviewer, per layer", "Blind pass"]),
    ("L9 Approved meaning", "Adjudicated humans", ORANGE, "reusable", ["Local concept +", "SSSOM / gap"]),
]
lw, gap = 178, 7
for i, (t, who, col, dc, items) in enumerate(layers):
    x = 21 + i * (lw + gap)
    rect(x, 604, lw, 118, col, "#FFFFFF", 1.4, 7)
    o.append(f'<rect x="{x}" y="604" width="{lw}" height="6" rx="3" fill="{col}"/>')
    text(x + 9, 628, t, 10, col, "700")
    text(x + 9, 645, "by: " + who, 9, INK, "700")
    lines(x + 9, 663, items, 9, INK, 14, False)
    chip(x + 9, 698, dc + (" data" if dc == "restricted" else " — no patient data"), RED if dc == "restricted" else GREEN)
text(20, 742, "Only L9 leaves the DSA-approved environment. L1–L8 form the audit trail: package JSON + decisions, hashed and versioned with the run.", 10, "#5C6A70", italic=True)

# ---- guards band
text(20, 776, "GUARDS ENFORCED IN CODE (policy/farajamh_mr_odrl.jsonld, which extends the upstream ODRL policy)", 13, NAVY, "700")
guards = [
    ("D1", "Restricted data → only local, DSA-approved model hosts (upstream Gemini CLI path off)"),
    ("D2", "Safety-flagged utterances blocked until escalation is recorded"),
    ("D3", "Concept IDs only from terminology-service responses; invented IDs dropped"),
    ("D4", "No winner: minority readings retained and labelled"),
    ("D5", "≥ 3 interpreter models from ≥ 2 families"),
    ("P1", "No SSSOM, local concept or OMOP row without a final human decision; placeholders refused"),
    ("P2", "Package status can never be 'approved'"),
]
for i, (k, s) in enumerate(guards):
    x, y = 20 + (i % 2) * 835, 790 + (i // 2) * 26
    rect(x, y, 825, 22, NAVY, "#F2F6FA", 1, 5)
    o.append(f'<rect x="{x}" y="{y}" width="34" height="22" rx="5" fill="{NAVY}"/>')
    text(x + 17, y + 15, k, 10, "#FFFFFF", "700", "middle")
    text(x + 44, y + 15, s, 10, INK)

# ---- legend
ly = 905
rect(20, ly, W - 40, 72, GREY, "#FCFDFD", 1.2)
text(34, ly + 20, "LEGEND", 11, NAVY, "700")
for i, (c, lab) in enumerate(((BLUE, "AI / automation"), (RED, "Human decision / safety"), (ORANGE, "FarajaMH local concept"),
                              (GREEN, "External ontology"), (NAVY, "Governed output"), (GREY, "Upstream / downstream (context)"))):
    x = 34 + i * 200
    o.append(f'<rect x="{x}" y="{ly + 30}" width="13" height="13" rx="3" fill="{c}"/>')
    text(x + 20, ly + 41, lab, 9.5)
cx = 34
text(cx, ly + 63, "Relation to upstream Minority Report code:", 9.5, INK, "700")
cx += 238
for lab, col in (("adapted / extends: reused with changes", GREEN), ("modified / replaces: logic rewritten", ORANGE), ("new: not in upstream", RED)):
    cx += chip(cx, ly + 51, lab, col) + 10
text(W - 30, ly + 63, "v1 · 22 Sep 2026 · pairs with FarajaMH Semantic Architecture v10", 9, "#5C6A70", "400", "end")
o.append("</svg>")
out = Path(__file__).parent / "FarajaMH_MinorityReport_Architecture_v1.svg"
out.write_text("\n".join(o), encoding="utf-8")
print(out)
