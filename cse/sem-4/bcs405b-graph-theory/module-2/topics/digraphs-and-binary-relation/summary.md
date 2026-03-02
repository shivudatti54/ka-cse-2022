# Digraphs and Binary Relations - Summary

## Key Definitions and Concepts

- **Digraph (Directed Graph)**: G = (V, A) where V is a set of vertices and A ⊆ V × V is a set of directed edges called arcs. Each arc (u, v) has a direction from u to v.

- **Binary Relation**: A relation R on set A is a subset of A × A. We write aRb to denote (a, b) ∈ R.

- **In-degree/Out-degree**: d⁻(v) = number of arcs entering v; d⁺(v) = number of arcs leaving v.

- **Strongly Connected**: A digraph where a path exists from every vertex to every other vertex.

- **Weakly Connected**: The underlying undirected graph is connected.

## Important Formulas and Theorems

- **Path Count from Matrix**: M^k[i][j] = number of distinct paths of length k from vertex i to vertex j.

- **Transitive Closure**: R\* = R ∪ R² ∪ R³ ∪ ... ∪ Rⁿ where n = |V|.

- **Composition**: (R₁ ∘ R₂) = {(a,c) | ∃b: (a,b) ∈ R₁ and (b,c) ∈ R₂}

## Key Points

- Binary relations can be represented as digraphs where vertices are set elements and arcs represent ordered pairs.

- Reflexive relations contain all loops (a, a); symmetric relations have arcs in both directions; transitive relations maintain path consistency.

- A relation that is reflexive, symmetric, and transitive is an equivalence relation.

- A relation that is reflexive, antisymmetric, and transitive is a partial order.

- The adjacency matrix of a digraph is not necessarily symmetric (unlike undirected graphs).

- Strong connectivity implies weak connectivity, but not vice versa.

- Matrix powers reveal path information: M gives length-1 paths, M² gives length-2 paths, etc.

## Common Mistakes to Avoid

- Confusing symmetric with antisymmetric: A relation cannot be both unless it contains only diagonal elements.

- Forgetting that partial orders require reflexivity, not just irreflexivity in some definitions.

- Assuming weak connectivity implies strong connectivity—this is a common exam trap.

- Not considering the case when checking transitivity: Need to check ALL pairs where (a,b) and (b,c) exist.

## Revision Tips

1. Practice drawing digraphs from relation definitions and vice versa until the conversion becomes automatic.

2. Create a property checklist: For any relation, systematically check reflexive → symmetric → transitive.

3. Remember that matrix entry M[i][j] = 1 means an arc exists from vertex i to vertex j (note the direction!).

4. For connectivity questions, always check paths in both directions for strong connectivity.
