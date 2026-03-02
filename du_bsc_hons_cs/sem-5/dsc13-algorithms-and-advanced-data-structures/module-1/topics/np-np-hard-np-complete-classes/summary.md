# NP, NP-Hard, and NP-Complete Classes - Summary

## Key Definitions and Concepts

- **P (Polynomial Time)**: Problems solvable in O(n^k) time for constant k. Examples: sorting, shortest path, primality testing.

- **NP (Nondeterministic Polynomial Time)**: Problems where "yes" answers have polynomial-time verifiable certificates. Examples: SAT, Hamiltonian Path, Vertex Cover.

- **NP-Complete**: Problems in NP that are as hard as any problem in NP. If one can be solved in P, all NP problems can be solved in P (P = NP).

- **NP-Hard**: Problems at least as hard as NP-complete problems. Does not require being in NP. Includes optimization versions and undecidable problems.

## Important Formulas and Theorems

- **Cook-Levin Theorem (1971)**: SAT is NP-complete. This is the foundation—all other NP-complete proofs reduce from SAT.

- **Polynomial Reduction**: Problem A ≤_p B if there exists polynomial-time computable f such that x is "yes" for A iff f(x) is "yes" for B.

- **NP-Complete Proof Steps**: (1) Show problem X ∈ NP, (2) Reduce known NP-complete problem Y to X in polynomial time.

## Key Points

- P ⊆ NP (if P = NP, all three classes collapse together)
- NP-Complete ⊂ NP ⊂ PSPACE (strict inclusions if P ≠ NP)
- Common NP-complete problems: SAT, 3-SAT, Vertex Cover, Clique, Hamiltonian Path, TSP (decision version), Subset Sum, Partition
- Optimization versions of NP-complete problems are NP-hard (not in NP)
- If P ≠ NP, NP splits into P, NP-complete, and NP-intermediate
- Graph Isomorphism and Integer Factorization are believed to be NP-intermediate
- Complement of NP-complete is in co-NP (unknown if equals NP)

## Common Mistakes to Avoid

- Confusing NP-hard with NP-complete: NP-complete requires membership in NP, NP-hard does not.
- Treating optimization problems as NP-complete: They are NP-hard, not in NP.
- Forgetting that "verification" is key to NP: Problems in NP need polynomial-time verifiable certificates, not polynomial-time solutions.
- Using exponential-time reductions: Reductions must be polynomial-time to preserve NP-completeness.

## Revision Tips

1. Memorize the standard reduction chain: SAT → 3-SAT → Vertex Cover → Clique → Independent Set → Vertex Cover (complement).

2. Practice proving membership in NP: Always describe the certificate and verification algorithm.

3. Know at least one complete reduction proof (e.g., 3-SAT to Vertex Cover) in detail.

4. Understand the complement relationships: Independent Set ≤_p Vertex Cover via graph complement.

5. Remember that all NP-complete problems are polynomially equivalent—solving one in P solves all.