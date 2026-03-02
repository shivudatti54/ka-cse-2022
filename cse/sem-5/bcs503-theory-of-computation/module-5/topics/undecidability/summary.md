# Undecidability - Summary

## Key Definitions and Concepts

- **Decidable Problem**: A problem for which there exists an algorithm that always halts and produces the correct yes/no answer for all inputs.

- **Undecidable Problem**: A problem for which no such algorithm exists; cannot be solved by any computer program.

- **Recursive Language**: A language L such that there exists a Turing machine that accepts every string in L and rejects every string not in L, always halting.

- **Recursively Enumerable (r.e.) Language**: A language L such that there exists a Turing machine that accepts all strings in L and may either reject or loop on strings not in L.

- **Halting Problem**: The decision problem that asks whether a given Turing machine M halts on a given input w.

- **Rice's Theorem**: Any non-trivial property of the language recognized by a Turing machine is undecidable.

## Important Formulas and Theorems

- **Turing's Halting Problem Theorem**: No algorithm exists that can decide, for all possible program-input pairs, whether the program halts on the input.

- **Post Correspondence Problem (PCP)**: Given two lists of strings, determining if there exists a concatenation sequence that produces equal strings from both lists is undecidable.

- **Language Properties**: The following are undecidable for arbitrary TMs: emptiness of L(M), finiteness of L(M), whether L(M) = Σ\*, regularity of L(M), whether a specific string is in L(M).

## Key Points

- Undecidability establishes theoretical limits on what algorithms can accomplish; not all problems have algorithmic solutions.

- The halting problem is the canonical undecidable problem; most other undecidability results are proven by reducing the halting problem to them.

- Rice's Theorem provides a quick way to prove undecidability: if a problem concerns a non-trivial property of a language recognized by a TM, it is undecidable.

- Reduction is the primary technique for proving undecidability: if P ≤ Q and P is undecidable, then Q is undecidable.

- Recursively enumerable languages are those accepted by TMs that may loop on non-members; recursive languages are those for which TMs always halt.

- The Post Correspondence Problem is undecidable and serves as a useful intermediate problem for reductions.

## Common Mistakes to Avoid

- Confusing "undecidable" with "impossible to solve"—undecidable means no algorithm exists, not that humans cannot solve specific instances.

- Applying Rice's Theorem to trivial properties (properties true for all languages or false for all languages), which are actually decidable.

- Forgetting that a TM can loop forever on some inputs—this is crucial for understanding r.e. languages versus recursive languages.

- Incorrectly assuming that a problem being undecidable means we cannot check any instances of it; we can still check specific instances, just not all.

## Revision Tips

1. Practice proving at least three problems undecidable using both Rice's Theorem and reduction from the halting problem.

2. Memorize the statement of Rice's Theorem and be able to identify non-trivial properties quickly.

3. Understand the diagonalization proof of the halting problem—it frequently appears in exams.

4. Create a table of common undecidable problems and their reduction relationships for quick reference.

5. Focus on understanding the difference between recursive and recursively enumerable languages as this is a common exam question.
