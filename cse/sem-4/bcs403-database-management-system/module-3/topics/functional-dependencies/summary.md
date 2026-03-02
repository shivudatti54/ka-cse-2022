# Functional Dependencies - Summary

## Key Definitions and Concepts

- **Functional Dependency (X → Y):** A constraint where for any two tuples with same X values, they must have same Y values. X is the determinant/determinant, Y is the dependent.
- **Trivial FD:** X → Y where Y ⊆ X (always true, no new information)
- **Non-Trivial FD:** X → Y where Y ⊄ X (provides meaningful constraints)
- **Armstrong's Axioms:** Reflexivity (if Y ⊆ X, then X → Y), Augmentation (if X → Y, then XZ → YZ), Transitivity (if X → Y and Y → Z, then X → Z)
- **Attribute Closure (X⁺):** Set of all attributes functionally determined by X using Armstrong's axioms

## Important Formulas and Theorems

- **Algorithm for X⁺:** Start with X, repeatedly add RHS of FDs whose LHS is contained in current closure until no change
- **Minimal Cover Properties:** F_c must be equivalent to F, have single attribute on RHS, no extraneous LHS attributes, and no redundant FDs

## Key Points

- Functional dependencies eliminate data redundancy and prevent insertion, deletion, and update anomalies
- Trivial FDs (Y ⊆ X) always hold in any relation
- Armstrong's axioms are sound and complete - they generate all valid FDs
- Attribute closure computation is fundamental to finding keys and solving FD problems
- A candidate key is a minimal super key - no proper subset can determine all attributes
- Minimal cover is used before decomposition in normalization

## Common Mistakes to Avoid

- Confusing the direction of functional dependency (X → Y ≠ Y → X)
- Forgetting that trivial FDs always hold and don't add constraints
- Not checking all FDs when computing attribute closure (may miss some)
- Assuming a single attribute FD is always non-trivial without checking subset relationship

## Revision Tips

1. Practice attribute closure computation for at least 5 different problems
2. Memorize Armstrong's axioms and all derived rules
3. Understand the relationship between candidate keys and FDs - if X⁺ = R, then X is a key
4. Practice minimal cover problems using the three-step approach
5. Review previous year questions on functional dependencies for exam pattern
