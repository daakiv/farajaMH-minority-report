"""Enforces the FarajaMH ODRL duties (policy/farajamh_mr_odrl.jsonld) in code, the same way upstream api.py
enforces its ODRL policy at runtime."""


class PolicyViolation(Exception):
    pass


def check_before_run(utt: dict, backend, interpreters: list[dict], min_families: int) -> str | None:
    """Returns a blocking status, raises on violations, or None when processing may proceed."""
    # D1: restricted data only to DSA-approved hosts
    if utt["data_classification"] == "restricted" and backend.host_locality not in ("local_dsa_approved",):
        raise PolicyViolation("D1: restricted utterance cannot be sent to a non-approved model host")
    # D2: safety gate
    if utt["safety"]["flag"] and not utt["safety"]["escalated"]:
        return "blocked_pending_safety_escalation"
    # D5: model diversity
    fams = {m["family"] for m in interpreters}
    if len(interpreters) < 3 or len(fams) < min_families:
        raise PolicyViolation(f"D5: need >=3 interpreters from >={min_families} families, got {len(interpreters)}/{len(fams)}")
    return None


def enforce_id_origin(candidates: list[dict], live: bool) -> list[dict]:
    """D3: in live mode drop anything not verified by a terminology service in this run."""
    return [c for c in candidates if c.get("id_verified")] if live else candidates


def assert_not_approved(package: dict):
    # P2
    if package.get("status") not in ("awaiting_review", "blocked_pending_safety_escalation", "failed"):
        raise PolicyViolation("P2: the AI layer cannot set an approved status")
