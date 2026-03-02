# Euler's Theorem and Planar Graphs - Summary

## Key Definitions and Concepts

- **Planar Graph:** A graph that can be drawn in a plane without any edges crossing.
- **Plane Graph:** A specific drawing of a planar graph where no edges intersect.
- **Face:** A region of a plane graph bounded by edges; includes the outer infinite region.
- **Euler's Formula:** For any connected planar graph: V - E + F = 2, where V = vertices, E = edges, F = faces.

## Important Formulas and Theorems

- **Euler's Formula:** V - E + F = 2 (for connected planar graphs)
- **Maximum Edges Corollary:** E ≤ 3V - 6 (for V ≥ 3)
- **Triangle-Free Bound:** E ≤ 2V - 4 (when no 3-cycles exist)
- **Kuratowski's Theorem:** A graph is non-planar if and only if it contains a subdivision of K5 or K3,3

## Key Points

1. Euler's theorem relates vertices, edges, and faces in connected planar graphs through the invariant V - E + F = 2.

2. The outer face must always be counted as one of the faces in Euler's formula.

3. K5 (complete graph on 5 vertices) and K3,3 (complete bipartite graph with 3+3 vertices) are the fundamental non-planar graphs.

4. If E > 3V - 6 for any graph with V ≥ 3, the graph must be non-planar.

5. All trees (connected acyclic graphs) satisfy V - E + 1 = 2 since they have exactly one face.

6. K4 is planar, while K5 is non-planar—this distinction is frequently tested.

7. Subdivisions of K5 or K3,3 make a graph non-planar.

## Common Mistakes to Avoid

1. **Forgetting the outer face:** Many students count only interior faces and get incorrect values.

2. **Applying Euler's formula to disconnected graphs:** The formula V - E + F = 2 applies only to connected graphs.

3. **Confusing planar with plane graph:** A graph may be planar but not yet drawn in the plane without crossings.

4. **Using E > 3V - 6 as conclusive proof:** This is sufficient to prove non-planarity, but E ≤ 3V - 6 doesn't guarantee planarity.

## Revision Tips

1. Practice drawing K5 and K3,3 to understand why edge crossings are unavoidable in these graphs.

2. Memorize the inequalities: E ≤ 3V - 6 (general) and E ≤ 2V - 4 (triangle-free).

3. Solve at least 5 problems involving Euler's formula to build confidence in application.

4. Remember that bipartite graphs (like K3,3) have only even-length cycles, affecting face edge counts.
