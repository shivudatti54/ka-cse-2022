# Connected Graphs, Disconnected Graphs and Components - Summary

## Key Definitions and Concepts

- **Graph**: A mathematical structure G = (V, E) consisting of vertices V and edges E connecting pairs of vertices.

- **Connected Graph**: An undirected graph where a path exists between every pair of vertices.

- **Disconnected Graph**: A graph that is not connected; contains at least two vertices with no path between them.

- **Connected Component**: A maximal connected subgraph of a graph. The number of components is denoted ω(G).

- **Walk**: A sequence of vertices where consecutive vertices are adjacent; length equals number of edges.

- **Path**: A walk with no repeated vertices.

- **Cycle**: A closed path where the first and last vertices are the same.

- **Strongly Connected (Directed)**: A directed graph where a directed path exists from every vertex to every other vertex.

- **Weakly Connected (Directed)**: A directed graph where the underlying undirected graph is connected.

- **Strongly Connected Component (SCC)**: A maximal strongly connected subgraph of a directed graph.

- **Cut Vertex**: A vertex whose removal increases the number of components.

- **Cut Edge (Bridge)**: An edge whose removal disconnects the graph.

## Important Formulas and Theorems

- A graph G is connected if and only if ω(G) = 1
- Every vertex belongs to exactly one component
- A graph with n vertices and fewer than n-1 edges is necessarily disconnected
- A tree with n vertices has exactly n-1 edges and is connected

## Key Points

1. Connectivity is a fundamental property that determines whether a graph represents a single connected system.

2. Components can be found using BFS or DFS traversal algorithms starting from any unvisited vertex.

3. In directed graphs, strong connectivity is stricter than weak connectivity.

4. Strongly connected components of a directed graph form a DAG when contracted.

5. Cut vertices and cut edges are critical for analyzing network robustness.

6. A single vertex graph is always connected by definition.

7. The complement of a disconnected graph is always connected.

## Common Mistakes to Avoid

1. Confusing weak connectivity with strong connectivity in directed graphs—always check both directions for strong connectivity.

2. Forgetting that isolated vertices (vertices with no edges) each form their own component.

3. Incorrectly assuming that a graph with n vertices and exactly n-1 edges is always a tree (must also be acyclic).

4. Assuming a graph is connected just because it has many edges—always verify path existence between all vertex pairs.

## Revision Tips

1. Practice identifying components by hand using BFS/DFS on various graph examples.

2. For directed graphs, always construct the reachability matrix to verify strong connectivity.

3. Remember: A graph is connected iff there is a path from any vertex to any other vertex.

4. Draw various graphs (connected and disconnected) to visualize the concepts clearly.

5. Review the relationship between bridges, cut vertices, and connectivity.
