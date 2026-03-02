# Partial Orders and Hasse Diagrams - Summary

## Key Definitions and Concepts

- **Partial Order (≼):** A relation on set A that is reflexive, antisymmetric, and transitive. The pair (A, ≼) is called a **poset** (partially ordered set).

- **Comparable/Incomparable:** Elements a and b are comparable if a ≼ b or b ≼ a; otherwise they are incomparable (denoted a || b).

- **Hasse Diagram:** A graph representing a finite poset where vertices are elements, edges show covering relations (immediate predecessors), and transitive edges are omitted.

- **Covering Relation:** a covers b if a ≼ b, a ≠ b, and no element c exists such that a ≼ c ≼ b.

- **Maximal Element:** No other element is strictly greater. Minimal Element: No other element is strictly smaller.

- **Greatest Element (Top):** Comparable with all elements (a ≼ g for all a). Least Element (Bottom): All elements comparable to it (l ≼ a for all a).

- **Upper/Lower Bound:** For subset B, u is upper bound if b ≼ u for all b ∈ B; l is lower bound if l ≼ b for all b ∈ B.

- **Lattice:** A poset where every pair of elements has both least upper bound (join, ∨) and greatest lower bound (meet, ∧).

- **Topological Sort:** Linear ordering of elements consistent with the partial order (if a ≼ b, then a appears before b).

## Important Formulas and Theorems

- A poset can have multiple maximal/minimal elements but at most one greatest/least element.
- A finite poset always has at least one maximal and one minimal element.
- A poset has a topological ordering if and only if it is acyclic (no cycles).
- For n-element set, power set P(S) has 2^n elements and forms a Boolean lattice under ⊆.

## Key Points

- Partial order must satisfy: Reflexivity (a ≼ a), Antisymmetry (a ≼ b and b ≼ a implies a = b), Transitivity (a ≼ b and b ≼ c implies a ≼ c).

- Hasse diagrams omit transitive edges for clarity; only covering relations are shown.

- In divisibility poset on {1, 2, ..., n}, 1 is always least element and n is always greatest (when n is in the set).

- Subset relation (P(S), ⊆) is the most common example of a lattice—the Boolean lattice.

- Topological sorting has applications in task scheduling, course prerequisite planning, and build systems.

## Common Mistakes to Avoid

- Confusing antisymmetric (if a ≼ b and b ≼ a, then a = b) with asymmetric (if a ≼ b, then b ⊀ a).

- Drawing transitive edges in Hasse diagrams—only covering relations should be shown.

- Assuming a greatest element exists; many posets (like ℤ under ≤) have none.

- Mixing up maximal (local maximum) with greatest (global maximum) elements.

## Revision Tips

- Practice drawing Hasse diagrams for divisibility on small sets like {1, 2, 3, 6, 12}.

- Memorize the properties of partial orders: R-A-T (Reflexive, Antisymmetric, Transitive).

- For topological sort, always identify minimal elements first and remove them iteratively.

- Remember: In Hasse diagrams, "smaller" elements go at the bottom, "larger" at the top.

- Solve previous year university questions on this topic to understand exam patterns.
