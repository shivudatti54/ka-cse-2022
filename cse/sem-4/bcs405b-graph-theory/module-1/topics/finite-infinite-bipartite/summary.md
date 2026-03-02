# Finite, Infinite, and Bipartite Graphs - Summary

## Key Definitions and Concepts

- **Finite Graph**: A graph containing a finite (limited) number of vertices and edges. Most practical applications use finite graphs.

- **Infinite Graph**: A graph containing infinitely many vertices or edges. Types include countably infinite, uncountably infinite, and locally finite graphs.

- **Bipartite Graph**: A graph whose vertex set can be partitioned into two disjoint sets (V₁, V₂) such that every edge connects a vertex from V₁ to a vertex from V₂. No edge exists within the same set.

- **Complete Bipartite Graph K(m,n)**: A bipartite graph with m vertices in one set, n vertices in the other set, and every possible edge between the sets.

## Important Formulas and Theorems

- **Complete Bipartite Graph K(m,n)**:
- Number of vertices: m + n
- Number of edges: m × n
- Degree of vertices in set of size m: n
- Degree of vertices in set of size n: m

- **Handshaking Lemma**: Sum of degrees of all vertices = 2 × (number of edges)

- **Bipartite Characterization**: A graph is bipartite if and only if it contains no odd cycles (odd-length cycles).

- **Perfect Matching Condition**: For a bipartite graph to have a perfect matching, both partite sets must have equal size.

## Key Points

1. Finite graphs have bounded number of vertices and edges, while infinite graphs have unbounded (infinite) vertices or edges.

2. A cycle graph Cₙ is bipartite if and only if n is even (no odd cycles).

3. Star graph K(1,n) is a special case of complete bipartite graphs.

4. Trees are always bipartite graphs (they contain no cycles).

5. Complete bipartite graphs K(m,n) are not complete graphs unless m = n = 1.

6. The two-coloring algorithm can determine if a graph is bipartite: if proper 2-coloring is possible, the graph is bipartite.

7. Paths are always bipartite regardless of their length.

## Common Mistakes to Avoid

1. Confusing complete graphs with complete bipartite graphs - they are different concepts.

2. Forgetting that bipartite graphs can have isolated vertices in either partition.

3. Assuming that a graph without odd cycles is automatically bipartite - must verify the partition condition.

4. Incorrectly stating that all infinite graphs are theoretical with no practical use.

## Revision Tips

1. Practice identifying bipartite graphs by looking for odd cycles - this is the quickest test.

2. Memorize the formulas for K(m,n) vertices and edges - these frequently appear in exam problems.

3. Draw examples of bipartite graphs (C₄, C₆, K₂₃, paths) to build visual understanding.

4. Remember: trees, paths, cycles of even length, and complete bipartite graphs are always bipartite.
