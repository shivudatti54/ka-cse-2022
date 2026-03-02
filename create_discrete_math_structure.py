#!/usr/bin/env python3
"""
Create folder structure and dummy files for Discrete Mathematical Structures
"""
import os
import json
from pathlib import Path

# Base path
BASE_PATH = Path("/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-3")
SUBJECT_FOLDER = "bcs305-discrete-mathematical-structures"

# Module definitions with topics
MODULES = {
    "module-1": {
        "title": "Fundamentals of Logic",
        "topics": [
            "basic-connectives-and-truth-tables",
            "logic-equivalence-the-laws-of-logic",
            "logical-implication-rules-of-inference",
            "the-use-of-quantifiers",
            "quantifiers-definitions-and-proofs-of-theorems"
        ]
    },
    "module-2": {
        "title": "Properties of the Integers and Counting Principles",
        "topics": [
            "mathematical-induction",
            "the-well-ordering-principle-mathematical-induction",
            "recursive-definitions",
            "fundamental-principles-of-counting-rules-of-sum-and-product",
            "permutations",
            "combinations-the-binomial-theorem",
            "combinations-with-repetition"
        ]
    },
    "module-3": {
        "title": "Relations and Functions",
        "topics": [
            "cartesian-products-and-relations",
            "functions-plain-and-one-to-one",
            "onto-functions",
            "the-pigeon-hole-principle",
            "function-composition-and-inverse-functions",
            "properties-of-relations",
            "computer-recognition-zero-one-matrices-and-directed-graphs",
            "partial-orders-hasse-diagrams",
            "equivalence-relations-and-partitions"
        ]
    },
    "module-4": {
        "title": "Inclusion-Exclusion and Recurrence Relations",
        "topics": [
            "the-principle-of-inclusion-and-exclusion",
            "generalizations-of-the-principle",
            "derangements-nothing-is-in-its-right-place",
            "rook-polynomials",
            "first-order-linear-recurrence-relation",
            "second-order-linear-homogeneous-recurrence-relation-with-constant-coefficients"
        ]
    },
    "module-5": {
        "title": "Introduction to Group Theory",
        "topics": [
            "definitions-and-examples-of-particular-groups",
            "klein-4-group",
            "additive-group-of-integers-modulo-n",
            "multiplicative-group-of-integers-modulo-p-and-permutation-groups",
            "properties-of-groups",
            "subgroups",
            "cyclic-groups",
            "cosets",
            "lagranges-theorem"
        ]
    }
}

# Dummy file templates
DUMMY_FILES = {
    "read.md": "# {topic_title}\n\n*Content to be generated*\n",
    "mcqs.json": json.dumps({"mcqs": []}, indent=2),
    "flashcards.json": json.dumps({"flashcards": []}, indent=2),
    "questions.json": json.dumps({"questions": []}, indent=2),
    "visual.json": json.dumps({"visual": {"svg": "", "narration": []}}, indent=2),
    "memory.json": json.dumps({"memoryTechniques": []}, indent=2),
    "purpose.md": "# Purpose\n\n*To be filled*\n",
    "code.json": json.dumps({"codeExamples": []}, indent=2)
}

def slugify(text):
    """Convert text to URL-friendly slug"""
    return text.lower().replace(" ", "-").replace("–", "-").replace(":", "").replace(",", "").replace(".", "")

def create_structure():
    """Create complete folder structure with dummy files"""

    subject_path = BASE_PATH / SUBJECT_FOLDER
    topic_paths = []

    # Create subject folder
    subject_path.mkdir(parents=True, exist_ok=True)
    print(f"Created subject folder: {subject_path}")

    # Create _meta.json
    meta_json = {
        "id": "discrete-mathematical-structures",
        "name": "DISCRETE MATHEMATICAL STRUCTURES",
        "code": "BCS305",
        "description": "Discrete Mathematical Structures study material",
        "icon": "math-compass",
        "color": "#8b5cf6"
    }
    with open(subject_path / "_meta.json", "w") as f:
        json.dump(meta_json, f, indent=2)
    print(f"Created _meta.json")

    # Create modules
    chapters_list = []

    for module_id, module_data in MODULES.items():
        module_path = subject_path / module_id
        module_path.mkdir(exist_ok=True)

        # Create module _index.json
        module_index = {
            "id": module_id,
            "title": module_data["title"],
            "order": int(module_id.split("-")[1]),
            "topicCount": len(module_data["topics"])
        }

        with open(module_path / "_index.json", "w") as f:
            json.dump(module_index, f, indent=2)

        chapters_list.append(module_index)
        print(f"Created module: {module_id}")

        # Create topics folder
        topics_path = module_path / "topics"
        topics_path.mkdir(exist_ok=True)

        # Create each topic folder with dummy files
        for topic in module_data["topics"]:
            topic_path = topics_path / topic
            topic_path.mkdir(exist_ok=True)

            # Create dummy files
            topic_title = topic.replace("-", " ").title()
            for filename, content in DUMMY_FILES.items():
                file_path = topic_path / filename

                # Only format markdown files, write JSON as-is
                if filename.endswith(".md"):
                    file_content = content.format(topic_title=topic_title)
                else:
                    file_content = content

                with open(file_path, "w") as f:
                    f.write(file_content)

            # Track topic path for the text file
            relative_path = f"sem-3/{SUBJECT_FOLDER}/{module_id}/topics/{topic}"
            topic_paths.append(relative_path)

            print(f"  Created topic: {topic}")

    # Create subject-level _index.json
    subject_index = {
        "chapters": chapters_list
    }

    with open(subject_path / "_index.json", "w") as f:
        json.dump(subject_index, f, indent=2)
    print(f"Created subject _index.json")

    # Create topic paths text file
    topic_paths_file = BASE_PATH.parent / "discrete-math-topic-paths.txt"
    with open(topic_paths_file, "w") as f:
        f.write("\n".join(topic_paths))

    print(f"\n✅ Created topic paths file: {topic_paths_file}")
    print(f"✅ Total topics: {len(topic_paths)}")
    print(f"✅ Total modules: {len(MODULES)}")

    return topic_paths

if __name__ == "__main__":
    print("=" * 70)
    print("Creating Discrete Mathematical Structures folder structure")
    print("=" * 70)
    topic_paths = create_structure()
    print("\n" + "=" * 70)
    print("COMPLETED SUCCESSFULLY")
    print("=" * 70)
