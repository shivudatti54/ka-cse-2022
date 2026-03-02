#!/usr/bin/env python3
"""
Estimate completion time for SVG regeneration
"""

import re
from datetime import datetime, timedelta
from pathlib import Path

LOG_FILE = "/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/svg_regeneration.log"

def parse_log():
    if not Path(LOG_FILE).exists():
        return None

    with open(LOG_FILE, 'r') as f:
        content = f.read()

    # Extract total
    total_match = re.search(r'Need regeneration: (\d+)', content)
    total = int(total_match.group(1)) if total_match else 0

    # Count completed
    regenerated = content.count('✓ Regenerated')
    failed = content.count('✗')
    completed = regenerated + failed

    # Get start time (approximate from first generation line)
    lines = content.split('\n')
    start_time = None
    current_time = datetime.now()

    # Estimate based on log
    # Each SVG takes ~1-3 seconds with rate limiting
    if completed > 5:
        # Calculate rate
        rate = completed / max(1, (current_time - (current_time - timedelta(minutes=5))).total_seconds())
        remaining = total - completed
        seconds_left = remaining / rate if rate > 0 else 0
        eta = current_time + timedelta(seconds=seconds_left)
    else:
        # Not enough data
        eta = None
        rate = 0

    return {
        'total': total,
        'completed': completed,
        'regenerated': regenerated,
        'failed': failed,
        'remaining': total - completed,
        'eta': eta,
        'rate': rate
    }

def main():
    stats = parse_log()
    if not stats:
        print("No log data available")
        return

    print("="*80)
    print("SVG REGENERATION - ETA CALCULATOR")
    print("="*80)
    print()
    print(f"Total to regenerate: {stats['total']}")
    print(f"Completed: {stats['completed']}")
    print(f"  ✓ Success: {stats['regenerated']}")
    print(f"  ✗ Failed: {stats['failed']}")
    print(f"Remaining: {stats['remaining']}")
    print()
    print(f"Progress: {100*stats['completed']/stats['total']:.2f}%")
    print()

    if stats['eta']:
        print(f"Estimated completion: {stats['eta'].strftime('%Y-%m-%d %H:%M:%S')}")
        time_left = stats['eta'] - datetime.now()
        hours = int(time_left.total_seconds() // 3600)
        minutes = int((time_left.total_seconds() % 3600) // 60)
        print(f"Time remaining: ~{hours}h {minutes}m")
    else:
        # Use average of 2s per SVG as estimate
        avg_seconds = 2
        total_seconds = stats['remaining'] * avg_seconds
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        eta = datetime.now() + timedelta(seconds=total_seconds)
        print(f"Estimated completion: {eta.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Time remaining: ~{hours}h {minutes}m (estimated)")

    print()
    print("Note: ETA is approximate and may vary based on API performance")
    print("="*80)

if __name__ == '__main__':
    main()
