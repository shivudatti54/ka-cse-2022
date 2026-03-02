# Pendant Vertex, Distance and Centres in a Tree - Summary

## Key Definitions and Concepts

- **Pendant Vertex**: A vertex with degree 1 (leaf vertex). Every tree with n ≥ 2 has at least two pendant vertices.
- **Distance d(u,v)**: The number of edges in the unique path connecting vertices u and v in a tree.
- **Eccentricity ecc(v)**: The maximum distance from vertex v to any other vertex in the tree.
- **Radius rad(T)**: Minimum eccentricity among all vertices in tree T.
- **Diameter diam(T)**: Maximum eccentricity; equals the longest shortest path between any two vertices.
- **Center**: The vertex (or two adjacent vertices) with minimum eccentricity.

## Important Formulas and Theorems

- **Tree edge count**: A tree with n vertices has exactly n-1 edges
- **Eccentricity**: ecc(v) = max{d(v,u) : u ∈ V(T)}
- **Radius**: rad(T) = min{ecc(v) : v ∈ V(T)}
- **Diameter**: diam(T) = max{ecc(v) : v ∈ V(T)} = max{d(u,v)}
- **Fundamental inequality**: rad(T) ≤ diam(T) ≤ 2 × rad(T)
- **Center theorem**: A tree has either one center or two adjacent centers

## Key Points

1. Pendant vertices have degree 1 and serve as endpoints in tree structures
2. Distance in a tree is always uniquely defined due to the absence of cycles
3. The center of a tree can be found by repeatedly removing layers of pendant vertices
4. For a path with n vertices, diameter = n-1 and radius = floor((n-1)/2)
5. In a star graph K₁,ₙ, the center is the central vertex with radius = diameter = 1
6. The diameter path (longest shortest path) passes through the center(s)
7. A vertex with minimum eccentricity is called a center vertex
8. If diam(T) = d, the center is located at distance floor(d/2) from any endpoint of a diameter path

## Common Mistakes to Avoid

1. Confusing degree 0 (isolated vertex) with degree 1 (pendant vertex)—trees are connected
2. Computing distance as number of vertices instead of edges in the path
3. Forgetting that eccentricity is the maximum distance, not minimum or average
4. Assuming all trees have exactly one center—some have two adjacent centers
5. Removing pendant vertices one at a time instead of simultaneously (all at once per layer)

## Revision Tips

1. Practice identifying pendant vertices in various tree diagrams
2. Use the pruning algorithm: remove all pendant vertices, repeat until 1-2 vertices remain
3. Remember: diameter always equals the length of the longest path in the tree
4. For exam problems, draw the tree and trace paths explicitly
5. Verify your answers using the radius-diameter inequality relationship
