# Equivalence and Partial Order Relations - Summary

## Key Definitions and Concepts

- **Equivalence Relation**: A relation that is reflexive, symmetric, and transitive on set A. Denoted by ∼ or ≡.

- **Equivalence Class**: For a ∈ A, [a] = {x ∈ A | xRa}. Partition of A into disjoint classes.

- **Partial Order**: A relation that is reflexive, antisymmetric, and transitive. A set with a partial order is called a **poset** (P, ≤).

- **Total Order**: A partial order where every pair of distinct elements is comparable.

- **Hasse Diagram**: Graphical representation of finite poset showing covering relations.

- **Lattice**: A poset where every two-element subset has a join (least upper bound) and meet (greatest lower bound).

- **Topological Sort**: Linear ordering consistent with the partial order.

## Important Formulas and Theorems

- **Fundamental Theorem of Equivalence Relations**: One-to-one correspondence between equivalence relations on A and partitions of A.

- **Equivalence Class Properties**: For equivalence relation R on A:
  - a ∈ [a] (representative)
  - aRb ⇔ [a] = [b]
  - [a] ∩ [b] = ∅ or [a] = [b]

## Key Points

- Equivalence relations partition sets into disjoint equivalence classes.

- Partial orders generalize total orders by allowing incomparability.

- In Hasse diagrams, edges represent covering relations only (not transitive closure).

- A poset can have multiple minimal/maximal elements but at most one least/greatest element.

- Topological sorting always exists for finite posets.

- Every finite poset has at least one minimal element and at least one maximal element.

- Chains are subsets where all elements are comparable; antichains have no comparable pairs.

## Common Mistakes to Avoid

- Confusing symmetry with antisymmetry—they are opposite properties.

- Drawing transitive edges in Hasse diagrams (only covering relations should appear).

- Assuming minimal implies least; they are different concepts.

- Forgetting that partial orders must be reflexive by definition.

## Revision Tips

- Practice identifying relation properties with various examples (equality, divisibility, ≤ on numbers).

- Draw Hasse diagrams for divisor sets (6, 12, 24, 30) to master diagram construction.

- Memorize the algorithm for topological sorting: find minimal → output → remove → repeat.

- Create your own examples of posets and identify all special elements.