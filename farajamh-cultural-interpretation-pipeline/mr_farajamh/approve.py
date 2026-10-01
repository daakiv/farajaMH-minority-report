"""After human review: final decisions -> Local Concept Layer entries, SSSOM rows, gap register.

This is the only path from Minority Report output to anything reusable, and it requires a final human
decision (policy P1). Candidates that no human approved never leave the package.
"""
from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

PREFIXES = {
    "FMHLC": "https://w3id.org/farajamh/lc/",
    "SCTID": "http://snomed.info/id/",
    "MFOEM": "http://purl.obolibrary.org/obo/MFOEM_",
    "MFOMD": "http://purl.obolibrary.org/obo/MFOMD_",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "semapv": "https://w3id.org/semapv/vocab/",
    "sssom": "https://w3id.org/sssom/",
    "obo": "http://purl.obolibrary.org/obo/",
    "orcid": "https://orcid.org/",
    "fmhr": "https://w3id.org/farajamh/reviewer/",
}
SOURCES = {"SCTID": "http://snomed.info/sct", "MFOEM": "obo:mfoem", "MFOMD": "obo:mfomd"}
SSSOM_COLS = ["subject_id", "subject_label", "predicate_id", "predicate_modifier", "object_id", "object_label", "object_source",
              "object_source_version", "mapping_justification", "mapping_cardinality", "author_id", "reviewer_id", "creator_id",
              "mapping_tool", "mapping_tool_version", "confidence", "mapping_date", "comment"]

# Prefixes whose content FarajaMH is not licensed to redistribute.
#
# A candidate from one of these may be retrieved, reviewed, and recorded in a candidate package — that
# is our own audit trail. It must not appear as an object_id in the published mapping set, which
# declares CC-BY-4.0 over its contents and would otherwise be asserting a licence we have no right to
# grant over someone else's terminology.
#
# Rows recording an ABSENCE (object_id = sssom:NoTermFound) are NOT withheld. They carry no identifier
# and no content from the terminology; "we searched SNOMED CT and found nothing adequate" is our
# finding to publish, and it is the scientifically useful half of this output.
#
# SCTID is here because SNOMED CT is licensed content: queryable through a third-party terminology
# service, not redistributable by us. Remove it only when a licence permitting redistribution is in
# place, and record that decision where the licence is recorded.
NON_REDISTRIBUTABLE_PREFIXES = {"SCTID"}


class ApprovalError(Exception):
    pass


def build_outputs(packages: dict[str, dict], decisions: list[dict], out: Path, tool_version: str,
                  demo_placeholders: bool = False, non_redistributable: set[str] | None = None):
    out.mkdir(parents=True, exist_ok=True)
    blocked = set(NON_REDISTRIBUTABLE_PREFIXES if non_redistributable is None else non_redistributable)
    final = [d for d in decisions if d["final"]]
    lcl, rows, gaps, withheld = [], [], [], []
    for d in final:
        p = packages.get(d["package_id"])
        if p is None or p["status"] != "awaiting_review":
            raise ApprovalError(f"{d['decision_id']}: package {d['package_id']} missing or not reviewable")
        reviewers = sorted({r["reviewer"]["reviewer_id"] for r in decisions if r["package_id"] == d["package_id"]})
        lca = d.get("local_concept_action", {})
        interp = d["layer_decisions"]["interpretation"]
        if lca.get("action") in ("create", "add_variant"):
            lcl.append({
                "local_concept_id": lca["local_concept_id"], "action": lca["action"],
                "pref_label_sw": lca.get("pref_label_sw"), "pref_label_en": lca.get("pref_label_en"), "definition": lca.get("definition"),
                "clinical_status": interp.get("clinical_status"),
                "variant": {"text": p["L1_original"]["expression_span"]["text"], "normalised": p["L2_normalisation"]["normalised_expression"],
                            "language": p["L2_normalisation"]["language_id"],
                            "dialect": p["L1_original"]["context_as_received"].get("dialect_declared"),
                            "region": p["L1_original"]["context_as_received"].get("region")},
                "approved_translation": d["layer_decisions"]["translation"].get("final_translation"),
                "approved_interpretation": interp.get("human_sense") or "; ".join(
                    f"{c['label']} ({c['category']})" for c in p["L5_agreement"]["sense_clusters"]
                    if c["cluster_id"] in interp.get("accepted_cluster_ids", [])),
                "reviewer_note": interp.get("note", ""),
                "evidence_package": p["package_id"], "approved_by": reviewers, "approved_at": d["decided_at"],
            })
        subj = lca.get("local_concept_id")
        for c in d["layer_decisions"].get("concepts", []):
            if not subj:
                raise ApprovalError(f"{d['decision_id']}: concept decisions need a local concept (subject)")
            base = {"subject_id": subj, "subject_label": lca.get("pref_label_sw", ""), "mapping_justification": "semapv:ManualMappingCuration",
                    "author_id": "|".join(reviewers), "reviewer_id": d["reviewer"]["reviewer_id"], "creator_id": "",
                    "mapping_tool": "farajamh-minority-report", "mapping_tool_version": tool_version,
                    "mapping_date": d["decided_at"][:10], "predicate_modifier": "", "mapping_cardinality": ""}
            note = f"{c.get('justification', '')} | AI candidate package {p['package_id']}"
            if c["decision"] == "no_adequate_concept":
                system = c.get("system", "SNOMEDCT")
                prefix = "SCTID" if system == "SNOMEDCT" else system
                # 1:0 — one subject, no object. The SSSOM field that says this row records an absence
                # rather than a mapping, and the counterpart to 1:1 on an approved row. Kept even for
                # a non-redistributable system: it names no concept from it.
                rows.append(base | {"predicate_id": c.get("predicate_id", "skos:exactMatch"), "object_id": "sssom:NoTermFound",
                                    "object_label": "", "object_source": SOURCES.get(prefix, system), "object_source_version": "",
                                    "mapping_cardinality": "1:0",
                                    "confidence": c.get("confidence", ""), "comment": "Semantic gap. " + note})
                gaps.append({"local_concept_id": subj, "system": system, "cluster_id": c.get("cluster_id"),
                             "reason": c.get("justification", ""), "package_id": p["package_id"], "recorded_at": d["decided_at"],
                             "proposed_action": "ontology extension request / keep local"})
                continue
            if c["decision"] not in ("approve", "reject"):
                continue  # defer: nothing leaves the package
            if c["decision"] == "reject" and not c.get("negative_assertion"):
                continue  # plain rejection stays in the audit trail only
            is_placeholder = "LOOKUP-" in c["id"]
            if is_placeholder and not demo_placeholders:
                raise ApprovalError(f"{d['decision_id']}: {c['id']} is a placeholder, not a verified identifier")
            prefix = c["id"].split(":")[0]
            if prefix in blocked:
                # The human approved this mapping and that decision stands in the package and here.
                # What is withheld is PUBLICATION of the identifier, not the review outcome.
                withheld.append({"decision_id": d["decision_id"], "package_id": p["package_id"],
                                 "subject_id": subj, "predicate_id": c["predicate_id"], "object_id": c["id"],
                                 "object_label": c.get("label", ""), "prefix": prefix,
                                 "decision": c["decision"], "decided_at": d["decided_at"],
                                 "reason": f"{prefix} identifiers are not licensed for redistribution in the published mapping set"})
                continue
            ver = next((x["system_version"] for pc in p["L6_concept_candidates"]["per_cluster"] for x in pc["candidates"] if x["id"] == c["id"]),
                       "reviewer-supplied")
            rows.append(base | {"predicate_id": c["predicate_id"], "object_id": c["id"], "object_label": c.get("label", ""),
                                "object_source": SOURCES.get(prefix, prefix), "object_source_version": ver,
                                "predicate_modifier": "Not" if c["decision"] == "reject" else "",
                                "mapping_cardinality": "1:1",
                                "confidence": c.get("confidence", ""),
                                "comment": ("DEMO PLACEHOLDER ID. " if is_placeholder else "") + note})

    set_id = "https://w3id.org/farajamh/mappings/idioms-of-distress" + ("-DEMO-NOT-FOR-REGISTRATION" if demo_placeholders else "")
    header = ["# curie_map:"] + [f"#   {k}: {v}" for k, v in PREFIXES.items()] + [
        f"# mapping_set_id: {set_id}", f"# mapping_set_version: {date.today().isoformat()}",
        "# license: https://creativecommons.org/licenses/by/4.0/",
        "# mapping_set_description: FarajaMH local concepts (idioms of distress) to external terminologies. Human-approved only."]
    if withheld:
        held = ", ".join(sorted({w["prefix"] for w in withheld}))
        # Stated in the file itself: an incomplete set that does not say so is a misleading set, and the
        # CC-BY-4.0 line above would otherwise imply this is everything the reviewers approved.
        header.append(f"# comment: {len(withheld)} human-approved mapping(s) are NOT in this set. "
                      f"{held} identifiers are not licensed for redistribution. The decisions are recorded in "
                      f"withheld_mappings.jsonl and in the candidate packages; only publication is withheld.")
    if demo_placeholders:
        header.append("# comment: DEMO built from SIMULATED review decisions and placeholder IDs. Do not register or load.")
    with open(out / "mappings.sssom.tsv", "w", newline="", encoding="utf-8") as f:
        f.write("\n".join(header) + "\n")
        w = csv.DictWriter(f, fieldnames=SSSOM_COLS, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    (out / "local_concept_layer.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lcl), encoding="utf-8")
    (out / "gap_register.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in gaps), encoding="utf-8")
    (out / "withheld_mappings.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in withheld), encoding="utf-8")
    if withheld:
        held = ", ".join(sorted({w["prefix"] for w in withheld}))
        print(f"    {len(withheld)} approved mapping(s) withheld from mappings.sssom.tsv ({held} not redistributable). "
              f"See withheld_mappings.jsonl.")
    return {"local_concepts": len(lcl), "sssom_rows": len(rows), "gaps": len(gaps), "withheld": len(withheld)}
