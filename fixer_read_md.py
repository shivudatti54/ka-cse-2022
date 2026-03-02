import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent.parent / "docs" / "scripts"
NVIDIA_ENHANCE = SCRIPT_DIR / "nvidia-enhance.sh"

def main():
    path_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("read_md_list.txt")

    with path_file.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # SVG path -> topic dir: .../topics/foo/assets/foo.svg -> .../topics/foo
            topic_dir = str(Path(line).parent.parent)
            read_md = Path(topic_dir) / "read.md"
            if not read_md.is_file():
                print(f"Skipping (no read.md): {topic_dir}")
                continue

            print(f"\n{'='*60}")
            print(f"Running: nvidia-enhance.sh {Path(topic_dir).name} read")
            print(f"{'='*60}")
            result = subprocess.run(["bash", str(NVIDIA_ENHANCE), topic_dir, "read"])

            if result.returncode != 0:
                print(f"FAILED for {topic_dir} (exit {result.returncode})")
                break

if __name__ == "__main__":
    main()
