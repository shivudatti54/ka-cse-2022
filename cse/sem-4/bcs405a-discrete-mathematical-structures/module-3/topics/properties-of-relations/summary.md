# Properties of Relations - Summary

## Key Definitions and Concepts

- **Relation**: A subset of Cartesian product A × B; written aRb if (a,b) ∈ R
- **Domain**: {a ∈ A | ∃b: (a,b) ∈ R}; **Range**: {b ∈ B | ∃a: (a,b) ∈ R}
- **Reflexive**: (a,a) ∈ R for all a ∈ A
- **Irreflexive**: No (a,a) ∈ R for any a ∈ A
- **Symmetric**: aRb implies bRa
- **Asymmetric**: aRb implies bRa is never true
- **Antisymmetric**: aRb and bRa implies a = b
- **Transitive**: aRb and bRc implies aRc
- **Equivalence Relation**: Reflexive + Symmetric + Transitive
- **Partial Order**: Reflexive + Antisymmetric + Transitive

## Important Formulas and Theorems

- **Composite Relation**: S ∘ R = {(a,c) | ∃b: (a,b) ∈ R and (b,c) ∈ S}
- **Inverse Relation**: R^(-1) = {(b,a) | (a,b) ∈ R}
- **Reflexive Closure**: R ∪ I_A where I_A = {(a,a) | a ∈ A}
- **Symmetric Closure**: R ∪ R^(-1)
- **Transitive Closure**: R\* = R ∪ R² ∪ R³ ∪ ... ∪ R^n (for |A| = n)
- **R is transitive** ⟺ R^n ⊆ R for all n ≥ 1

## Key Points

- Relations on finite sets can be represented as directed graphs or matrices
- Equivalence relations partition sets into disjoint equivalence classes
- Partial orders (posets) use Hasse diagrams for visualization
- Warshall's algorithm computes transitive closure in O(n³)
- The identity relation I_A is the smallest reflexive relation
- The empty relation is symmetric, antisymmetric, and transitive but not reflexive
- Universal relation U = A × A is reflexive, symmetric, and transitive
- Symmetric relations have symmetric matrices; antisymmetric have only diagonal when equal

## Common Mistakes to Avoid

- Confusing symmetric with antisymmetric—they are not opposites
- Forgetting to check all pairs when testing properties (especially transitivity)
- Not recognizing that "not symmetric" doesn't mean "antisymmetric"
- Overlooking the empty set case when A is empty
- Assuming transitive closure requires infinite union—finite n suffices

## Revision Tips

1. Practice with 5-6 examples, determining all properties for each
2. Memorize the "checklist": Reflexive → Symmetric → Antisymmetric → Transitive
3. Remember: Equivalence = Reflexive + Symmetric + Transitive; Partial Order = Reflexive + Antisymmetric + Transitive
4. Draw relation as graph—reflexive has self-loops, symmetric has bidirectional edges, transitive shows path consolidation
5. For exam: Start by listing all pairs, then systematically check each property
