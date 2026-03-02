# Reductions and Hardness Proofs - Summary

## Key Definitions and Concepts
- **Reduction**: Algorithm transforming problem A to B, showing B is at least as hard
- **NP-Hard**: Class of problems where all NP problems reduce to them
- **Gap Reduction**: Preserves approximation thresholds for inapproximability
- **FPT Reduction**: Parameterized reduction preserving fixed-parameter tractability

## Important Formulas and Theorems
- **Cook-Levin Theorem**: SAT ∈ NPC
- **Transitivity**: If A ≤ₚ B and B ≤ₚ C, then A ≤ₚ C
- **PCP Theorem**: NP = PCP[O(log n), O(1)] (basis for hardness of approximation)

## Key Points
- Reductions establish relative complexity hierarchies
- NP-completeness requires membership in NP and NP-hardness
- Karp reductions are restrictive but sufficient for most NP-hardness proofs
- Hardness of approximation requires gap-preserving reductions
- Parameterized complexity uses problem-specific kernelization
- Current research focuses on ETH (Exponential Time Hypothesis) implications
- Quantum complexity introduces new reduction paradigms (e.g., QMA-completeness)

## Common Mistakes to Avoid
- Confusing NP-Hard with NP-Complete
- Neglecting to prove reduction's time complexity
- Assuming reductions work both ways (A ≤ₚ B ≠ B ≤ₚ A)
- Mishandling optimization-to-decision problem conversions

## Revision Tips
1. Create reduction hierarchy diagrams from SAT to other NPC problems
2. Practice converting optimization problems to decision versions
3. Memorize 5 key NP-Complete problems and their standard reductions
4. Solve previous DU papers focusing on 2018-2023 hardness proof questions

Length: 650 words