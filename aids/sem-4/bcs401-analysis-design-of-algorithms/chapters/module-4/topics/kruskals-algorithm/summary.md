# Kruskal's Algorithm - Summary

## Key Definitions and Concepts

- MINIMUM SPANNING TREE (MST): A spanning tree with minimum total edge weight among all spanning trees of a connected weighted graph. For V vertices, an MST contains exactly V-1 edges.

- KRUSKAL'S ALGORITHM: A greedy algorithm that builds the MST by sorting all edges by weight and adding edges one by one if they don't form cycles, until V-1 edges are selected.

- DISJOINT SET UNION (DSU)/UNION-FIND: A data structure supporting FIND (to determine set membership) and UNION (to merge sets), used for efficient cycle detection in Kruskal's Algorithm.

- CUT PROPERTY: For any cut in the graph, the minimum weight edge crossing the cut belongs to some minimum spanning tree.

## Important Formulas and Theorems

- TIME COMPLEXITY: O(E log E) or equivalently O(E log V), where E is number of edges and V is number of vertices.

- SPACE COMPLEXITY: O(V + E) for storing the graph and DSU structure.

- MST EDGE COUNT: For any graph with V vertices, the MST always contains exactly V-1 edges.

## Key Points

- Kruskal's Algorithm processes edges in increasing order of weight, unlike Prim's which grows from a vertex.

- The algorithm uses the greedy method—it makes locally optimal choices (minimum weight edge) hoping for global optimum.

- Cycle detection is crucial—an edge is rejected if its endpoints are already connected through previously selected edges.

- The DSU data structure with path compression and union by rank provides nearly constant time operations.

- Kruskal's Algorithm is particularly efficient for SPARSE GRAPHS (graphs with fewer edges relative to V²).

- The algorithm terminates when exactly V-1 edges have been added to the MST.

- All edges must have distinct weights for unique MST; with equal weights, multiple MSTs may exist.

## Common Mistakes to Avoid

- FORGETTING TO SORT edges before processing—always sort first in non-decreasing order.

- INCLUDING CYCLES by not properly checking if endpoints belong to the same set before adding an edge.

- STOPPING TOO EARLY—remember the MST must have exactly V-1 edges; stopping with fewer edges means the tree is not spanning.

- CONFUSING with Prim's Algorithm—Kruskal starts with V separate components, Prim starts with one vertex.

## Revision Tips

- Practice tracing Kruskal's Algorithm on at least 3-4 different graphs to master the step-by-step process.

- Remember the two main data structures: sorted edges list and DSU for cycle detection.

- Compare with Prim's Algorithm—know when to use each (Kruskal for sparse graphs, Prim for dense graphs).

- Review the proof of correctness using the cut property—this is a common theoretical question.

- Memorize the time complexity O(E log E) and understand why sorting dominates the complexity.