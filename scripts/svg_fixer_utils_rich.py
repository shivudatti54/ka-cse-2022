import subprocess
import sys
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRIPT_DIR = Path(__file__).resolve().parent
MINIMAX_SCRIPT = SCRIPT_DIR / "minimax-fix-svg-rich.sh"

def resolve_svg(svg_input):
    """Resolve topic dir and SVG filename from flexible input (SVG path, topic dir, or assets dir)."""
    p = Path(svg_input)
    if p.suffix == ".svg":
        svg_file = p
        topic_dir = p.parent.parent
    elif (p / "assets").is_dir():
        topic_dir = p
        svg_file = next((p / "assets").glob("*.svg"), None)
    elif p.is_dir() and p.name == "assets":
        topic_dir = p.parent
        svg_file = next(p.glob("*.svg"), None)
    else:
        topic_dir = p
        svg_file = next((p / "assets").glob("*.svg"), None)

    if svg_file is None or not svg_file.is_file():
        return None, None
    return str(topic_dir), svg_file.name

def update_visual_json_for_topic(topic_dir):
    """Update visual.json in topic directory to include -rich.svg entries. Returns count of added entries."""
    topic_path = Path(topic_dir)
    visual_json_path = topic_path / "visual.json"

    if not visual_json_path.is_file():
        return 0

    try:
        # Read existing visual.json
        with visual_json_path.open('r', encoding='utf-8') as f:
            data = json.load(f)

        updated_count = 0

        # Process 'visuals' array if it exists
        if 'visuals' in data and isinstance(data['visuals'], list):
            new_entries = []

            for visual in data['visuals']:
                if visual.get('type') == 'animated-svg' and 'file' in visual:
                    svg_file = visual['file']  # e.g., "assets/topic-name.svg"

                    # Generate -rich.svg filename
                    svg_path = Path(svg_file)
                    rich_svg_name = f"{svg_path.stem}-rich.svg"
                    rich_svg_file = str(svg_path.parent / rich_svg_name)

                    # Check if -rich.svg exists
                    rich_svg_path = topic_path / rich_svg_file
                    if rich_svg_path.is_file():
                        # Check if this -rich entry already exists
                        rich_id = f"{visual['id']}-rich"
                        already_exists = any(
                            v.get('id') == rich_id for v in data['visuals']
                        )

                        if not already_exists:
                            # Create new entry for -rich.svg
                            rich_entry = {
                                "id": rich_id,
                                "title": f"{visual['title']} (Rich)",
                                "description": f"{visual['description']} - Enhanced with CSS animations",
                                "type": "animated-svg",
                                "file": rich_svg_file,
                                "animated": True
                            }
                            new_entries.append(rich_entry)
                            updated_count += 1

            # Add new entries to visuals array
            if new_entries:
                data['visuals'].extend(new_entries)

        # Save updated visual.json if changes were made
        if updated_count > 0:
            with visual_json_path.open('w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write('\n')  # Add trailing newline

        return updated_count

    except Exception as e:
        print(f"  Warning: Failed to update visual.json in {topic_dir}: {e}")
        return 0


def run_one(svg_input):
    """Run minimax-fix-svg-rich.sh for a single SVG. Returns (svg_input, success, message, stderr, topic_dir)."""
    topic_dir, svg_name = resolve_svg(svg_input)
    if not topic_dir:
        return svg_input, False, "No SVG found", "", None

    result = subprocess.run(
        ["bash", str(MINIMAX_SCRIPT), topic_dir, svg_name],
        capture_output=True, text=True,
    )

    if result.returncode != 0:
        # Extract error summary from stderr/stdout
        error_lines = (result.stderr + result.stdout).split('\n')
        error_msg = "Script failed"

        # Look for specific error patterns
        for line in error_lines:
            if "ERROR:" in line or "❌" in line:
                error_msg = line.strip()
                break
            elif "HTTP" in line and any(code in line for code in ["401", "429", "500", "502", "503"]):
                error_msg = f"API error: {line.strip()}"
                break

        return svg_input, False, error_msg, result.stderr, None

    # Success - return topic_dir so we can update visual.json
    return svg_input, True, "ok", "", topic_dir

def find_all_svgs_in_topic(topic_path):
    """Find all SVG files in a topic directory's assets folder."""
    p = Path(topic_path)

    # Handle both topic dir and assets dir paths
    if p.name == "assets" and p.is_dir():
        # Path already points to assets directory
        assets_dir = p
    else:
        # Path points to topic directory
        assets_dir = p / "assets"

    if not assets_dir.is_dir():
        return []

    # Find all SVG files in assets directory (excluding -rich.svg files)
    svg_files = []
    for svg_file in assets_dir.glob("*.svg"):
        # Skip already-generated rich SVGs
        if not svg_file.stem.endswith("-rich"):
            svg_files.append(str(svg_file))

    return svg_files

def load_tasks(path_file):
    """Read paths from file and expand topic directories into all their SVG files."""
    tasks = []
    with path_file.open() as f:
        for line in f:
            path_input = line.strip()
            if not path_input or path_input.startswith("#"):
                continue

            # Fix common path issues: remove /chapters/ if it doesn't exist
            path_input_fixed = path_input.replace("/chapters/module-", "/module-")

            # Remove trailing /assets/ if present (we'll add it back in find_all_svgs_in_topic)
            path_input_fixed = path_input_fixed.rstrip("/")
            if path_input_fixed.endswith("/assets"):
                path_input_fixed = path_input_fixed[:-7]  # Remove /assets

            p = Path(path_input_fixed)

            # If it's already an SVG file, add it directly
            if p.suffix == ".svg":
                tasks.append(path_input_fixed)
            # If it's a directory, find all SVGs in it
            elif p.is_dir():
                svg_files = find_all_svgs_in_topic(path_input_fixed)
                tasks.extend(svg_files)
            else:
                # Try to treat as topic directory anyway
                svg_files = find_all_svgs_in_topic(path_input_fixed)
                if svg_files:
                    tasks.extend(svg_files)

    return tasks

def main():
    # Parse args: svg_fixers_rich.py [path_file] [workers]
    # If first arg is a digit, treat as worker count (path_file defaults to svg_path.txt)
    path_file = Path("svg_path.txt")
    workers = 1

    for arg in sys.argv[1:]:
        if arg.isdigit():
            workers = int(arg)
        else:
            path_file = Path(arg)

    if not path_file.is_file():
        print(f"Path file not found: {path_file}")
        return

    if not MINIMAX_SCRIPT.is_file():
        print(f"MiniMax script not found: {MINIMAX_SCRIPT}")
        return

    tasks = load_tasks(path_file)
    if not tasks:
        print("No SVG files found to process.")
        return

    total = len(tasks)
    print(f"Found {total} SVG file(s) to enhance with RICH ANIMATIONS")
    print(f"Using {workers} worker(s)\n")

    if workers <= 1:
        # Sequential mode (original behavior, stops on first failure)
        for i, svg_input in enumerate(tasks, 1):
            topic_dir, svg_name = resolve_svg(svg_input)
            if not topic_dir:
                print(f"[{i}/{total}] No SVG found for: {svg_input}")
                continue

            print(f"[{i}/{total}] {svg_name} → rich version")
            result = subprocess.run(["bash", str(MINIMAX_SCRIPT), topic_dir, svg_name])

            if result.returncode != 0:
                print(f"Command failed for {svg_input} with exit code {result.returncode}")
                break
    else:
        # Parallel mode
        done = 0
        failed = 0
        errors = []
        topics_to_update = set()  # Track unique topic directories

        print(f"{'━' * 60}")
        print(f"  Processing {total} SVGs in parallel...")
        print(f"{'━' * 60}\n")

        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(run_one, t): t for t in tasks}
            for future in as_completed(futures):
                svg_input, success, msg, stderr, topic_dir = future.result()
                done += 1
                name = Path(svg_input).stem
                progress_pct = int((done / total) * 100)

                if success:
                    print(f"[{done}/{total} {progress_pct}%] ✅ {name}-rich")
                    if topic_dir:
                        topics_to_update.add(topic_dir)
                else:
                    failed += 1
                    print(f"[{done}/{total} {progress_pct}%] ❌ {name} — {msg}")
                    errors.append((name, msg, stderr))

        # Update visual.json files for all successfully processed topics
        if topics_to_update:
            print(f"\n{'━' * 60}")
            print(f"  Updating visual.json files...")
            print(f"{'━' * 60}\n")
            total_visual_updates = 0
            for topic_dir in topics_to_update:
                count = update_visual_json_for_topic(topic_dir)
                if count > 0:
                    topic_name = Path(topic_dir).name
                    print(f"  ✓ {topic_name} - Added {count} rich SVG entry(ies)")
                    total_visual_updates += count
            print(f"\nUpdated {len(topics_to_update)} visual.json file(s), added {total_visual_updates} rich SVG entries")

        print(f"\n{'━' * 60}")
        print(f"  SUMMARY")
        print(f"{'━' * 60}")
        print(f"  ✅ Succeeded: {done - failed}/{total}")
        print(f"  ❌ Failed: {failed}/{total}")

        if errors and failed <= 10:  # Show detailed errors if not too many
            print(f"\n{'━' * 60}")
            print(f"  FAILED ITEMS")
            print(f"{'━' * 60}")
            for name, msg, _ in errors[:10]:
                print(f"  • {name}: {msg}")

        if failed == 0:
            print(f"\n🎉 All SVGs enhanced successfully with CSS animations!")
        print()

if __name__ == "__main__":
    main()
