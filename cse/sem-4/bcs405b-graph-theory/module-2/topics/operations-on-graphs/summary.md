# Operations on Graphs - Summary

## Key Definitions and Concepts

- **Union (G₁ ∪ G₂)**: Combines all vertices and edges from both graphs
- **Intersection (G₁ ∩ G₂)**: Retains only common vertices and edges present in both graphs
- **Join (G₁ + G₂)**: Adds all possible edges between vertices of G₁ and G₂
- **Complement (G̅)**: Contains edges between vertices that are NOT adjacent in G
- **Cartesian Product (G₁ × G₂)**: Grid-like connection where vertices are adjacent if same in one coordinate and adjacent in other
- **Strong Product**: Combines Cartesian product with join-like connectivity
- **Composition (G₁[G₂])**: Replaces each vertex of G₁ with a copy of G₂

## Important Formulas and Theorems

- |V(G₁ ∪ G₂)| = |V(G₁)| + |V(G₂)| - |V(G₁ ∩ G₂)|
- For join: |V(G₁ + G₂)| = |V(G₁)| + |V(G₂)|; |E(G₁ + G₂)| = |E(G₁)| + |E(G₂)| + |V(G₁)|×|V(G₂)|
- For complement: |E(G̅)| = C(n,2) - |E(G)|, where n = |V(G)|
- Cartesian product: |V(G₁ × G₂)| = |V(G₁)| × |V(G₂)|

## Key Points

- Union of disjoint graphs is called disjoint union (or sum)
- A graph is self-complementary if G ≅ G̅ (examples: P₄, C₅)
- K₂ × K₂ = C₄ (cycle of 4 vertices)
- Pₘ × Pₙ creates an m×n grid graph
- Induced subgraph includes ALL edges between selected vertices
- Spanning subgraph must include all original vertices but can have fewer edges
- Removing a vertex removes all incident edges; removing an edge preserves vertices

## Common Mistakes to Avoid

1. Confusing join with disjoint union — they are different operations
2. Forgetting that complement preserves the vertex set but changes all edges
3. In Cartesian product, not all pairs are adjacent — only those meeting the adjacency condition
4. Mixing up induced subgraph (vertex-based) with spanning subgraph (vertex coverage)
5. Assuming intersection is always defined — it requires common vertices

## Revision Tips

1. Practice drawing each operation with small examples (2-3 vertex graphs)
2. Remember that Cartesian product forms grids — visualize the structure
3. Know at least one example of self-complementary graphs (P₄, C₅)
4. For complement problems, always start by listing all missing edges from the original graph
5. Focus on understanding when each operation is applicable and what properties the result has
