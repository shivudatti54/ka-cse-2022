#!/usr/bin/env python3
"""
Remove the intermediate 'chapters' folder from CSE content structure.
Transforms: subject/chapters/module-X/topics/ → subject/module-X/topics/
"""
import os
import shutil
from pathlib import Path

BASE_PATH = Path("/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse")

def restructure_subject(subject_path):
    """Restructure a single subject folder by removing chapters/ intermediate level"""
    chapters_dir = subject_path / "chapters"

    if not chapters_dir.exists():
        return False, "No chapters folder"

    # Step 1: Move chapters/_index.json to subject/_index.json
    chapters_index = chapters_dir / "_index.json"
    if chapters_index.exists():
        target_index = subject_path / "_index.json"
        if target_index.exists():
            return False, f"Target _index.json already exists at {target_index}"
        shutil.move(str(chapters_index), str(target_index))
        print(f"    ✓ Moved _index.json to subject level")
    else:
        print(f"    ⚠ No _index.json in chapters folder")

    # Step 2: Move all module-X folders up one level
    module_count = 0
    for item in chapters_dir.iterdir():
        if item.is_dir() and item.name.startswith("module-"):
            target_path = subject_path / item.name
            if target_path.exists():
                return False, f"Target module folder already exists: {target_path}"
            shutil.move(str(item), str(target_path))
            module_count += 1
            print(f"    ✓ Moved {item.name}")

    # Step 3: Delete empty chapters folder
    remaining = list(chapters_dir.iterdir())
    if remaining:
        return False, f"Chapters folder not empty after move: {remaining}"

    chapters_dir.rmdir()
    print(f"    ✓ Deleted empty chapters folder")

    return True, f"Restructured ({module_count} modules moved)"

def main():
    print("=" * 70)
    print("RESTRUCTURING CSE CONTENT - Removing 'chapters' folder")
    print("=" * 70)

    total_subjects = 0
    restructured = 0
    skipped = 0
    errors = 0

    # Process each semester
    for sem_dir in sorted(BASE_PATH.glob("sem-*")):
        if not sem_dir.is_dir():
            continue

        print(f"\n{'='*70}")
        print(f"Processing {sem_dir.name}")
        print(f"{'='*70}")

        # Process each subject
        for subject_dir in sorted(sem_dir.iterdir()):
            if not subject_dir.is_dir() or subject_dir.name.startswith('.'):
                continue

            total_subjects += 1
            print(f"\n  Subject: {subject_dir.name}")

            success, message = restructure_subject(subject_dir)

            if success:
                restructured += 1
                print(f"    ✅ {message}")
            else:
                if "No chapters folder" in message:
                    skipped += 1
                    print(f"    ⏭️  {message}")
                else:
                    errors += 1
                    print(f"    ❌ {message}")

    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"Total subjects processed: {total_subjects}")
    print(f"  ✅ Restructured: {restructured}")
    print(f"  ⏭️  Skipped: {skipped}")
    print(f"  ❌ Errors: {errors}")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
