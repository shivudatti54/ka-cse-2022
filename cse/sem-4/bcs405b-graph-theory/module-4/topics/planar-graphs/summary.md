# Planar Graphs - Summary

## Key Definitions and Concepts

- **Planar Graph:** A graph that can be drawn in a plane without any edges crossing. The drawing is called a planar embedding.
- **Face/Region:** The connected areas bounded by edges in a planar embedding. The unbounded area is the outer face.
- **Maximal Planar Graph:** A planar graph to which no edge can be added without losing planarity; all faces are triangles.
- **Outer Planar Graph:** A graph that can be embedded such that all vertices lie on the outer face.
- **Dual Graph:** A graph constructed from a planar embedding where each face becomes a vertex, and edges correspond to adjacency.
- **Subdivision:** A graph obtained by replacing edges with paths (adding vertices of degree 2).

## Important Formulas and Theorems

- **Euler's Formula (Connected):** v - e + r = 2
- **Euler's Formula (General):** v - e + r = c + 1 (c = components)
- **Maximal Planar Edge Count:** e = 3v - 6 (for v ≥ 3)
- **Outer Planar Edge Count:** e ≤ 2v - 3
- **Kuratowski's Theorem:** A graph is planar iff it contains no subdivision of K5 or K3,3
- **Four Color Theorem:** Every planar graph can be colored with at most 4 colors
- **Planarity Test:** If e > 3v - 6 for v ≥ 3, the graph is non-planar

## Key Points

1. Euler's formula v - e + r = 2 is the fundamental relationship for all connected planar graphs

2. K5 and K3,3 are the two fundamental non-planar graphs; any graph containing their subdivisions is non-planar

3. Complete graph K5 has 5 vertices and 10 edges, exceeding 3(5) - 6 = 9, proving non-planarity

4. Complete bipartite graph K3,3 has 6 vertices and 9 edges, exceeding 3(6) - 6 = 12? Actually 9 ≤ 12, but still non-planar due to structure

5. Maximal planar graphs are triangulations where every face (including outer) is bounded by 3 edges

6. Dual graphs preserve planarity - the dual of a planar graph is also planar

7. The Four Color Theorem (1976) was the first major theorem proven with computer assistance

8. Any graph with v < 5 is automatically planar unless it is K4

9. Planarity can be tested algorithmically using DFS-based methods and PCQ trees

## Common Mistakes to Avoid

1. Forgetting that Euler's formula only applies to connected graphs; use v - e + r = c + 1 for disconnected graphs

2. Applying the inequality e ≤ 3v - 6 to graphs with v < 3; the formula requires v ≥ 3

3. Confusing maximal planar graphs with just planar graphs; maximal planar graphs have exactly 3v - 6 edges

4. Incorrectly identifying subdivisions when applying Kuratowski's theorem

5. Forgetting that the outer face counts as a region in Euler's formula

## Revision Tips

1. Practice drawing K5 and K3,3 to see why they cannot be planar - visualize the edge crossings

2. Memorize Euler's formula and practice deriving other formulas from it

3. Create a table comparing planar, maximal planar, and outer planar graphs with their properties

4. Solve at least 5-10 problems involving Euler's formula to become comfortable with identifying v, e, and r

5. Remember: when in doubt about planarity, try to redraw the graph with different vertex arrangements first
