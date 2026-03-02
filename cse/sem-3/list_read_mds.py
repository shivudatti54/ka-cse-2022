import os

base_path = r"c:\codeRepo\codeRepo2\studyApp\content-packs\vtu-2022-scheme\cse\sem-3"
subjects = [
    "bcs304-data-structures-and-applications",
    "bcs306a-object-oriented-programming-with-java",
    "bcs306b-object-oriented-programming-with-c"
]

output_file = "read_md_paths.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for subject in subjects:
        subject_path = os.path.join(base_path, subject)
        if not os.path.exists(subject_path):
            f.write(f"Directory not found: {subject_path}\n")
            continue
            
        for root, dirs, files in os.walk(subject_path):
            if "read.md" in files:
                full_path = os.path.join(root, "read.md")
                f.write(f"{full_path}\n")

print(f"Paths written to {output_file}")
