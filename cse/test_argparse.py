#!/usr/bin/env python3
"""Test argparse with start-from-topic argument."""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("paths_file")
parser.add_argument("--start-from-topic", type=int, default=1, dest="start_from_topic")
parser.add_argument("--dry-run", action="store_true")

args = parser.parse_args()

print(f"paths_file: {args.paths_file}")
print(f"start_from_topic: {args.start_from_topic}")
print(f"start_from_topic (getattr): {getattr(args, 'start_from_topic', 'NOT FOUND')}")
print(f"dry_run: {args.dry_run}")
print(f"\nAll args: {vars(args)}")
