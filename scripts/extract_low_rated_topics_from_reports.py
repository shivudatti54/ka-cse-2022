#!/usr/bin/env python3
"""Extract low-rated topic paths from reports JSON files.

- Scans a reports directory for JSON rating reports.
- Uses ONLY topic-level ratings: coverage_rating and content_quality_rating.
- Ignores nested file_ratings.
- Writes full topic paths to a .txt file (one per line), ready for topic_upgrader_parallel_async.py.
"""

import argparse
import json
from datetime import datetime
from pathlib import Path


def iter_topics(topics_obj):
    if isinstance(topics_obj, dict):
        return topics_obj.values()
    if isinstance(topics_obj, list):
        return topics_obj
    return []


def is_low_rated_topic(topic: dict, threshold: float, apis_filter: set[str] | None) -> bool:
    ratings = topic.get("ratings")
    if not isinstance(ratings, dict):
        return False

    for api_name, api_payload in ratings.items():
        if apis_filter and api_name not in apis_filter:
            continue
        if not isinstance(api_payload, dict):
            continue

        rating = api_payload.get("rating")
        if not isinstance(rating, dict):
            continue
        if "error" in rating:
            continue

        for k in ("coverage_rating", "content_quality_rating"):
            v = rating.get(k)
            if isinstance(v, (int, float)) and v <= threshold:
                return True

    return False


def extract_paths_from_report(report_path: Path, threshold: float, apis_filter: set[str] | None) -> set[str]:
    try:
        data = json.loads(report_path.read_text(encoding="utf-8"))
    except Exception:
        return set()

    topics = data.get("topics") if isinstance(data, dict) else None
    out = set()

    for topic in iter_topics(topics):
        if not isinstance(topic, dict):
            continue
        topic_path = topic.get("topic_path")
        if not isinstance(topic_path, str) or not topic_path.strip():
            continue
        if is_low_rated_topic(topic, threshold, apis_filter):
            out.add(topic_path)

    return out


def main():
    parser = argparse.ArgumentParser(
        description="Extract full topic paths where topic-level rating is <= threshold from reports JSON files."
    )
    parser.add_argument(
        "--reports-dir",
        default="reports",
        help="Directory containing ratings JSON reports (default: reports)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=5,
        help="Include topics with coverage/content quality <= threshold (default: 5)",
    )
    parser.add_argument(
        "--api",
        choices=["all", "minimax", "chutes"],
        default="all",
        help="Filter by API. 'all' checks any available API result (default: all)",
    )
    parser.add_argument(
        "--output",
        help=(
            "Output .txt path. Defaults to <reports-dir>/low_rated_topic_paths_"
            "<api>_le_<threshold>_<timestamp>.txt"
        ),
    )
    args = parser.parse_args()

    reports_dir = Path(args.reports_dir).expanduser().resolve()
    if not reports_dir.is_dir():
        raise SystemExit(f"Reports directory not found: {reports_dir}")

    apis_filter = None if args.api == "all" else {args.api}

    report_files = sorted(
        [p for p in reports_dir.glob("*.json") if "_ratings_" in p.name],
        key=lambda p: p.name,
    )

    if not report_files:
        raise SystemExit(f"No ratings JSON files found in: {reports_dir}")

    all_paths = set()
    per_file_counts = []

    for rp in report_files:
        paths = extract_paths_from_report(rp, args.threshold, apis_filter)
        per_file_counts.append((rp.name, len(paths)))
        all_paths.update(paths)

    threshold_label = str(int(args.threshold)) if float(args.threshold).is_integer() else str(args.threshold)
    if args.output:
        output_path = Path(args.output).expanduser().resolve()
    else:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = reports_dir / f"low_rated_topic_paths_{args.api}_le_{threshold_label}_{ts}.txt"

    sorted_paths = sorted(all_paths)
    output_path.write_text("\n".join(sorted_paths) + ("\n" if sorted_paths else ""), encoding="utf-8")

    print(f"Reports dir: {reports_dir}")
    print(f"Report files scanned: {len(report_files)}")
    print(f"API filter: {args.api}")
    print(f"Threshold: <= {args.threshold}")
    print(f"Unique low-rated topic paths: {len(sorted_paths)}")
    print(f"Output: {output_path}")
    print("Per-report matches:")
    for name, count in per_file_counts:
        print(f"  - {name}: {count}")


if __name__ == "__main__":
    main()
