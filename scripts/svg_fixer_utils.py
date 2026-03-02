import subprocess
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRIPT_DIR = Path(__file__).resolve().parent
MINIMAX_SCRIPT = SCRIPT_DIR / "minimax-fix-svg.sh"

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

def run_one(svg_input):
    """Run minimax-fix-svg.sh for a single SVG. Returns (svg_input, success, message)."""
    topic_dir, svg_name = resolve_svg(svg_input)
    if not topic_dir:
        return svg_input, False, "No SVG found"

    result = subprocess.run(
        ["bash", str(MINIMAX_SCRIPT), topic_dir, svg_name],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return svg_input, False, f"exit code {result.returncode}"
    return svg_input, True, "ok"

def load_tasks(path_file):
    """Read SVG paths from file, skipping blanks and comments."""
    tasks = []
    with path_file.open() as f:
        for line in f:
            svg_input = line.strip()
            if svg_input and not svg_input.startswith("#"):
                tasks.append(svg_input)
    return tasks

def main():
    # Parse args: svg_fixers.py [path_file] [workers]
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
        print("No SVG paths to process.")
        return

    total = len(tasks)
    print(f"Processing {total} SVGs with {workers} worker(s)\n")

    if workers <= 1:
        # Sequential mode (original behavior, stops on first failure)
        for i, svg_input in enumerate(tasks, 1):
            topic_dir, svg_name = resolve_svg(svg_input)
            if not topic_dir:
                print(f"[{i}/{total}] No SVG found for: {svg_input}")
                continue

            print(f"[{i}/{total}] {svg_name}")
            result = subprocess.run(["bash", str(MINIMAX_SCRIPT), topic_dir, svg_name])

            if result.returncode != 0:
                print(f"Command failed for {svg_input} with exit code {result.returncode}")
                break
    else:
        # Parallel mode
        done = 0
        failed = 0
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(run_one, t): t for t in tasks}
            for future in as_completed(futures):
                svg_input, success, msg = future.result()
                done += 1
                name = Path(svg_input).stem
                if success:
                    print(f"[{done}/{total}] ✓ {name}")
                else:
                    failed += 1
                    print(f"[{done}/{total}] ✗ {name} — {msg}")

        print(f"\nDone: {done - failed} succeeded, {failed} failed out of {total}")

if __name__ == "__main__":
    main()
