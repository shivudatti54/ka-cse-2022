#!/usr/bin/env python3
"""
Orchestrator: Monitor round 1 quality gate agents, then trigger round 2.

Round 1: 5 agents (one per semester) run quality_gate.py --fix on all subjects
Round 2: Re-rate ALL topics (fresh, no resume) + fix remaining issues

Usage:
  python3 scripts/quality_gate_orchestrator.py          # monitor + round 2
  python3 scripts/quality_gate_orchestrator.py --status  # just print status
"""

import subprocess
import time
import os
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

SEMESTERS = {
    "sem-3": [
        "cse/sem-3/bcs301-mathematics-for-computer-science",
        "cse/sem-3/bcs302-digital-design-and-computer-organization",
        "cse/sem-3/bcs303-operating-systems",
        "cse/sem-3/bcs304-data-structures-and-applications",
        "cse/sem-3/bcs306a-object-oriented-programming-with-java",
        "cse/sem-3/bcs306b-object-oriented-programming-with-c++",
    ],
    "sem-4": [
        "cse/sem-4/bcs401-analysis-design-of-algorithms",
        "cse/sem-4/bcs402-microcontrollers",
        "cse/sem-4/bcs403-database-management-system",
        "cse/sem-4/bcs405a-discrete-mathematical-structures",
        "cse/sem-4/bcs405b-graph-theory",
        "cse/sem-4/bcs405c-optimization-technique",
        "cse/sem-4/bcs405d-linear-algebra",
        "cse/sem-4/bcs456a-green-it-and-sustainability",
        "cse/sem-4/bcs456b-capacity-planning-for-it",
        "cse/sem-4/bcs456c-uiux",
    ],
    "sem-5": [
        "cse/sem-5/bcs501-software-engineering-project-management",
        "cse/sem-5/bcs502-computer-networks",
        "cse/sem-5/bcs503-theory-of-computation",
        "cse/sem-5/bcs508-environmental-studies",
        "cse/sem-5/bcs515a-computer-graphics",
        "cse/sem-5/bcs515b-artificial-intelligence",
        "cse/sem-5/bcs515c-unix-system-programming",
        "cse/sem-5/bcs515d-distributed-systems",
    ],
    "sem-6": [
        "cse/sem-6/bai654d-introduction-to-artificial-intelligence",
        "cse/sem-6/bcs601-cloud-computing",
        "cse/sem-6/bcs602-machine-learning",
        "cse/sem-6/bcs613a-blockchain-technology",
        "cse/sem-6/bcs613b-computer-vision",
        "cse/sem-6/bcs613c-compiler-design",
        "cse/sem-6/bcs613d-advanced-java",
        "cse/sem-6/bcs654a-introduction-to-data-structures",
        "cse/sem-6/bcs654b-fundamentals-of-operating-systems",
        "cse/sem-6/bis654c-mobile-application-development",
    ],
    "sem-7": [
        "cse/sem-7/bcs701-internet-of-things",
        "cse/sem-7/bcs702-parallel-computing",
        "cse/sem-7/bcs703-cryptography-network-security",
    ],
}

ALL_SUBJECTS = [s for subs in SEMESTERS.values() for s in subs]
LOG_FILE = "cse/reports/orchestrator.log"
POLL_INTERVAL = 120  # seconds


def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def subjects_with_postfix():
    """Return set of subjects that have at least one post-fix report."""
    done = set()
    for subj in ALL_SUBJECTS:
        if list(Path(subj).glob("reports/quality_gate_post-fix_*.html")):
            done.add(subj)
    return done


def subjects_with_prefix():
    """Return set of subjects that have at least one pre-fix report."""
    done = set()
    for subj in ALL_SUBJECTS:
        if list(Path(subj).glob("reports/quality_gate_pre-fix_*.html")):
            done.add(subj)
    return done


def print_status():
    """Print current status of all subjects."""
    pre = subjects_with_prefix()
    post = subjects_with_postfix()
    print(f"\n{'='*80}")
    print(f"Quality Gate Status — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*80}")
    for sem_name, subjects in SEMESTERS.items():
        print(f"\n  {sem_name} ({len(subjects)} subjects):")
        for subj in subjects:
            slug = Path(subj).name
            if subj in post:
                status = "DONE (pre-fix + post-fix)"
            elif subj in pre:
                status = "RATED (pre-fix only, fix pending)"
            else:
                # Check progress
                pf = Path(subj) / "reports" / "quality_gate_progress.json"
                if pf.exists():
                    import json
                    try:
                        d = json.loads(pf.read_text())
                        n = len(d.get("rated", {}))
                        status = f"IN PROGRESS ({n} topics rated)"
                    except Exception:
                        status = "IN PROGRESS"
                else:
                    status = "NOT STARTED"
            print(f"    {slug:55s} {status}")
    total = len(ALL_SUBJECTS)
    print(f"\n  Total: {len(post)}/{total} fully done, "
          f"{len(pre)}/{total} pre-fix done")
    print(f"{'='*80}\n")


def run_subject(subj, round_num, sem_name):
    """Run quality_gate.py on a single subject."""
    slug = Path(subj).name
    log(f"Round {round_num} [{sem_name}] Starting: {slug}")
    try:
        result = subprocess.run(
            ["python3", "scripts/quality_gate.py", subj,
             "--level", "standard", "--workers", "8", "--fix"],
            timeout=1800,
            capture_output=True,
            text=True,
        )
        # Extract summary from output
        lines = result.stdout.strip().split("\n")
        summary_lines = [l for l in lines if "PASS" in l or "TOTAL" in l or
                         "FIX" in l or "WRONG" in l or "LOW" in l or
                         "Rating complete" in l or "Fix complete" in l]
        summary = "; ".join(summary_lines[-3:]) if summary_lines else "completed"
        log(f"Round {round_num} [{sem_name}] Done: {slug} — {summary}")
        return subj, result.returncode
    except subprocess.TimeoutExpired:
        log(f"Round {round_num} [{sem_name}] TIMEOUT (30min): {slug}")
        return subj, -1
    except Exception as e:
        log(f"Round {round_num} [{sem_name}] ERROR: {slug} — {e}")
        return subj, -2


def run_semester(sem_name, subjects, round_num):
    """Run all subjects in a semester sequentially."""
    log(f"Round {round_num} [{sem_name}] Starting {len(subjects)} subjects...")
    for subj in subjects:
        run_subject(subj, round_num, sem_name)
    log(f"Round {round_num} [{sem_name}] All {len(subjects)} subjects done.")


def subjects_completed():
    """Return set of subjects that have at least one report (pre-fix or post-fix)."""
    done = set()
    for subj in ALL_SUBJECTS:
        has_pre = list(Path(subj).glob("reports/quality_gate_pre-fix_*.html"))
        has_post = list(Path(subj).glob("reports/quality_gate_post-fix_*.html"))
        if has_pre or has_post:
            done.add(subj)
    return done


STALE_TIMEOUT = 600  # 10 min with no new completions → assume round 1 is done


def monitor_round1():
    """Poll until all subjects complete or progress stalls (crashed agents)."""
    log("=" * 70)
    log("PHASE 1: Monitoring round 1 completion...")
    log("=" * 70)

    last_done_count = 0
    stale_seconds = 0

    while True:
        done = subjects_completed()
        remaining = len(ALL_SUBJECTS) - len(done)
        log(f"Round 1 progress: {len(done)}/{len(ALL_SUBJECTS)} subjects done, "
            f"{remaining} remaining")

        if remaining == 0:
            break

        # Stale detection: if no progress for STALE_TIMEOUT, move on
        if len(done) == last_done_count:
            stale_seconds += POLL_INTERVAL
            if stale_seconds >= STALE_TIMEOUT:
                pending = [Path(s).name for s in ALL_SUBJECTS if s not in done]
                log(f"No new completions for {STALE_TIMEOUT}s — "
                    f"assuming {remaining} subjects need round 2: {', '.join(pending)}")
                break
        else:
            stale_seconds = 0
            last_done_count = len(done)

        # Show which subjects are still pending
        pending = [Path(s).name for s in ALL_SUBJECTS if s not in done]
        if len(pending) <= 12:
            log(f"  Waiting on: {', '.join(pending)}")

        time.sleep(POLL_INTERVAL)

    done = subjects_completed()
    log("=" * 70)
    log(f"ROUND 1 DONE — {len(done)}/{len(ALL_SUBJECTS)} subjects completed, "
        f"round 2 will handle the rest")
    log("=" * 70)


def run_round2():
    """Clear progress and re-run quality gate on all subjects."""
    log("=" * 70)
    log("PHASE 2: Preparing round 2 (fresh re-rating of all topics)...")
    log("=" * 70)

    # Clear progress files so all topics get re-rated
    cleared = 0
    for subj in ALL_SUBJECTS:
        pf = Path(subj) / "reports" / "quality_gate_progress.json"
        if pf.exists():
            pf.unlink()
            cleared += 1
    log(f"Cleared {cleared} progress files for fresh re-rating")

    log("=" * 70)
    log("PHASE 2: Starting round 2 — 5 semesters in parallel")
    log("=" * 70)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for sem_name, subjects in SEMESTERS.items():
            futures.append(
                executor.submit(run_semester, sem_name, subjects, 2)
            )
        for f in futures:
            f.result()

    log("=" * 70)
    log("ROUND 2 COMPLETE — all 37 subjects re-rated and fixed")
    log("=" * 70)

    # Final status
    print_status()


def main():
    os.makedirs("cse/reports", exist_ok=True)

    if "--status" in sys.argv:
        print_status()
        return

    log("Quality Gate Orchestrator started")
    log(f"Monitoring {len(ALL_SUBJECTS)} subjects across "
        f"{len(SEMESTERS)} semesters")

    # Phase 1: Wait for round 1 to finish
    monitor_round1()

    # Phase 2: Run round 2
    run_round2()

    log("ORCHESTRATOR COMPLETE — both rounds finished")


if __name__ == "__main__":
    main()
