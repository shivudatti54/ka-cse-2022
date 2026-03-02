# Binary Relations and Equivalence - Summary

## Key Definitions and Concepts

- **Binary Relation**: A subset R of A × B where (a,b) ∈ R denotes aRb
- **Relation on Set A**: A subset of A × A
- **Equivalence Relation**: A relation that is reflexive, symmetric, and transitive simultaneously
- **Equivalence Class**: [a] = {x ∈ A | xRa} — all elements related to a
- **Partition**: A collection of disjoint non-empty subsets whose union is the entire set

## Important Formulas and Theorems

- **Composition**: S ∘ R = {(a,c) | ∃b: (a,b) ∈ R ∧ (b,c) ∈ S}
- **Inverse**: R⁻¹ = {(b,a) | (a,b) ∈ R}
- **Reflexive Closure**: R ∪ I_A (add diagonal elements)
- **Symmetric Closure**: R ∪ R⁻¹
- **Transitive Closure**: R⁺ = R ∪ R² ∪ R³ ∪ ... (using Boolean matrix multiplication)
- **Theorem**: Equivalence relations ↔ Partitions (one-to-one correspondence)

## Key Points

- Reflexive: ∀a ∈ A, (a,a) ∈ R; Symmetric: aRb implies bRa; Transitive: aRb and bRc imply aRc
- Antisymmetric: aRb and bRa imply a = b (used in partial orders)
- Congruence modulo n (a ≡ b mod n) is the standard equivalence relation example
- Equivalence classes are either identical or completely disjoint (never overlap)
- For n-element set, there are 2^(n²) possible relations
- Identity relation I_A = {(a,a) | a ∈ A} is always an equivalence relation
- A relation can be both symmetric and antisymmetric only if it is a subset of the identity relation

## Common Mistakes to Avoid

- Forgetting to check all three properties when determining if a relation is an equivalence relation
- Confusing symmetric with antisymmetric — they are NOT opposites
- Assuming a relation is transitive if (a,b) and (b,c) exist but (a,c) doesn't — this violates transitivity
- In matrix representation, confusing rows and columns — row i, column j gives (i,j)
- Forgetting that the empty set is reflexive on the empty set (trivially true)

## Revision Tips

1. Practice identifying properties from both set and matrix representations
2. Memorize the "congruence modulo n" example thoroughly — it appears in almost every exam
3. Draw digraphs for relations to visually check properties (loops = reflexive, two-way edges = symmetric, paths = transitive)
4. For transitive closure, remember the Warshall's algorithm approach for efficient computation
5. Solve at least 5-10 problems on finding equivalence classes from different types of relations