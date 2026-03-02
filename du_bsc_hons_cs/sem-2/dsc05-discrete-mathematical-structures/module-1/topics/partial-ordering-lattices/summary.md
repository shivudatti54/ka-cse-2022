# Partial Ordering and Lattices - Summary

## Key Definitions and Concepts

- **Poset (Partially Ordered Set)**: A set P with a binary relation ≤ satisfying reflexivity, antisymmetry, and transitivity
- **Comparable Elements**: a and b are comparable if a ≤ b or b ≤ a; otherwise they are incomparable (a || b)
- **Hasse Diagram**: Graphical representation showing covering relations with minimal elements at bottom
- **Maximal Element**: No element greater than it; Minimal Element: No element less than it
- **Greatest Element (⊤)**: Every element ≤ it; Least Element (⊥): Every element ≥ it
- **Upper Bound**: Element ≥ all elements in subset; Lower Bound: Element ≤ all elements in subset
- **Supremum (lub)**: Least upper bound; Infimum (glb): Greatest lower bound
- **Lattice**: Poset where every pair has both supremum and infimum (join ∨ and meet ∧)
- **Complete Lattice**: Every subset has supremum and infimum
- **Distributive Lattice**: Satisfies distributive laws; non-distributive lattices include M₃ (diamond) and N₅ (pentagon)
- **Complemented Lattice**: Every element has a complement where a ∨ a' = ⊤ and a ∧ a' = ⊥

## Important Formulas and Theorems

- **Lattice Properties**: a ≤ b iff a = a ∧ b iff b = a ∨ b
- **Distributive Laws**: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) and a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)
- **Key Theorem**: Every finite poset has maximal and minimal elements
- **Key Theorem**: Every finite lattice is complete
- **Key Theorem**: In a distributive lattice, if complements exist, they are unique

## Key Points

- Partial orders allow incomparability unlike total orders
- Hasse diagrams show covering relations, not all order relations
- Greatest/least elements must compare with ALL elements; maximal/minimal need only be incomparable with anything above/below
- A poset can have multiple maximal/minimal elements but at most one greatest and one least element
- A lattice combines two operations (join and meet) that are dual to each other
- The power set of any set forms a distributive lattice under union/intersection
- M₃ and N₅ are the two smallest non-distributive lattices

## Common Mistakes to Avoid

- Confusing maximal with greatest element—every greatest element is maximal, but not vice versa
- Forgetting that antisymmetry requires distinct elements to not mutually relate
- Not checking all pairs when proving a poset is a lattice
- Assuming infinite lattices are complete without proof
- In Hasse diagrams, forgetting that transitive edges are implied

## Revision Tips

- Practice drawing Hasse diagrams from relation descriptions and vice versa
- Memorize the structures of M₃ (diamond) and N₅ (pentagon) lattices
- Solve problems identifying bounds and extremal elements
- Review the duality principle: swapping ≤ with ≥, ∧ with ∨, sup with inf
- Solve at least 5-10 problems from previous year question papers