# Kuratowski's Theorem - Summary

## Key Definitions and Concepts

- **Planar Graph:** A graph that can be drawn on a plane without edge crossings. A plane graph is a specific embedding of a planar graph.
- **Subdivision:** Replacing an edge (u,v) with edges (u,w) and (w,v) by inserting a new vertex w.
- **Homeomorphic Graphs:** Two graphs are homeomorphic if one can be obtained from the other through a sequence of edge subdivisions.
- **K5:** Complete graph on 5 vertices with 10 edges—non-planar.
- **K3,3:** Complete bipartite graph with 3 vertices in each partition, 9 edges—non-planar.

## Important Formulas and Theorems

- **Euler's Formula:** For any connected planar graph: n - m + f = 2
- **Edge Bound:** For simple planar graphs with n ≥ 3: m ≤ 3n - 6
- **Kuratowski's Theorem:** A graph is planar if and only if it contains no subgraph homeomorphic to K5 or K3,3 (equivalently, no minor of K5 or K3,3).

## Key Points

- K5 and K3,3 are the only fundamental non-planar graphs—every non-planar graph contains one of these as a subdivision or minor.
- A graph containing K5 or K3,3 as a subgraph is definitely non-planar.
- A graph may appear non-planar in one drawing but still be planar if an alternative drawing exists without crossings.
- The inequality m > 3n - 6 provides a quick non-planarity test for simple graphs.
- K5 and K3,3 are not homeomorphic to each other—they represent two distinct families of non-planarity.

## Common Mistakes to Avoid

- Assuming a graph is non-planar because one particular drawing shows crossings; planarity requires checking ALL possible drawings.
- Confusing subdivision with edge contraction—subdivision adds vertices while contraction removes edges.
- Forgetting that the edge bound m ≤ 3n - 6 only applies to simple graphs (no loops or multiple edges).

## Revision Tips

- Practice drawing K5 and K3,3 repeatedly until you can recognize their structures instantly in larger graphs.
- When analyzing planarity, first check the quick m > 3n - 6 test; if it fails, then search for K5/K3,3 subdivisions.
- Remember: if a graph contains either K5 or K3,3 as a subgraph (or homeomorphic to one), it is non-planar; otherwise, it is planar.
