# Cartesian Products and Relations - Summary

## Key Definitions and Concepts

- **Cartesian Product**: A × B = {(a, b) : a ∈ A and b ∈ B} — the set of all ordered pairs from A and B.

- **Relation**: A relation R from set A to set B is a subset of A × B. If (a, b) ∈ R, we denote aRb.

- **Domain**: dom(R) = {a ∈ A : ∃b ∈ B such that (a, b) ∈ R}

- **Range**: ran(R) = {b ∈ B : ∃a ∈ A such that (a, b) ∈ R}

- **Inverse Relation**: R⁻¹ = {(b, a) : (a, b) ∈ R}

- **Composition**: S ∘ R = {(a, c) : ∃b ∈ B such that (a, b) ∈ R and (b, c) ∈ S}

## Important Formulas and Theorems

- **Cardinality**: |A × B| = |A| × |B|
- **Number of relations**: If |A| = n, there are 2^(n²) relations on A
- **Equivalence Relation**: Reflexive + Symmetric + Transitive
- **Partial Order**: Reflexive + Anti-symmetric + Transitive

## Key Points

1. Cartesian product produces ordered pairs; order matters: A × B ≠ B × A generally.
2. The empty relation ∅ and universal relation A × A are extreme cases of relations on A.
3. The identity relation Iₐ = {(a, a) : a ∈ A} is reflexive, symmetric, and transitive.
4. An equivalence relation partitions a set into disjoint equivalence classes.
5. A poset (partially ordered set) uses ≤ notation and has a Hasse diagram representation.
6. Every function is a relation, but a relation is a function only if each domain element maps to exactly one range element.
7. Composition of relations is associative: (R ∘ S) ∘ T = R ∘ (S ∘ T)

## Common Mistakes to Avoid

1. Confusing "anti-symmetric" with "asymmetric" — anti-symmetric allows (a, b) when a = b.
2. Forgetting that Cartesian product is not commutative; always check the order of sets.
3. In transitive property tests, assuming the relation must contain (a, c) if (a, b) and (b, c) exist separately — both pairs must exist.
4. Confusing domain with codomain — domain is the set of first components that actually appear.

## Revision Tips

1. Practice identifying relation properties with multiple examples from different contexts (numbers, sets, people).
2. Draw Hasse diagrams for partial orders to visualize the structure of posets.
3. Remember that equivalence classes form a partition — they are mutually disjoint and their union is the original set.
4. For exams, memorize the property definitions and practice with previous year questions on relation classification.
