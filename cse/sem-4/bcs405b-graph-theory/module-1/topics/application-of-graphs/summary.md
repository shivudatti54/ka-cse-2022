# Applications of Graphs - Summary

## Key Definitions and Concepts

- **Graph**: A mathematical structure consisting of vertices (nodes) and edges connecting pairs of vertices
- **Directed Graph (Digraph)**: Graph where edges have a specific direction
- **Weighted Graph**: Graph where edges have associated costs or distances
- **Directed Acyclic Graph (DAG)**: A directed graph with no cycles, essential for dependency resolution
- **PageRank**: Algorithm that ranks web pages based on link structure
- **Topological Sort**: Linear ordering of vertices in a DAG respecting edge directions

## Important Formulas and Theorems

- **Dijkstra's Algorithm**: Finds shortest path in O((V+E) log V) with min-heap, works only with non-negative weights
- **Bellman-Ford Algorithm**: Handles negative edge weights, O(VE) time complexity
- **PageRank Formula**: PR(A) = (1-d)/N + d × Σ(PR(i)/outlinks(i)) where d is damping factor
- **Maximum Flow**: Value of maximum flow equals minimum cut capacity (Max-Flow Min-Cut Theorem)

## Key Points

1. Graphs model relationships in computer networks, social networks, transportation systems, and biological networks
2. Shortest path algorithms are fundamental for GPS navigation and network routing
3. PageRank transformed search engines by using web link structure for ranking
4. Dependency graphs enable efficient task scheduling and build system optimization
5. Topological sorting resolves dependencies in correct execution order
6. Centrality measures identify influential nodes in networks
7. Graph representation choice (matrix vs. list) affects algorithm efficiency
8. DAGs are essential for representing hierarchical dependencies without cycles

## Common Mistakes to Avoid

1. Applying Dijkstra's algorithm when negative edge weights exist (use Bellman-Ford instead)
2. Confusing between directed and undirected graphs when solving problems
3. Forgetting that topological sort only works on DAGs (check for cycles first)
4. Using adjacency matrix for sparse graphs (wastes memory, use adjacency list)
5. Overlooking that PageRank requires damping factor to handle dead ends and spider traps

## Revision Tips

1. Practice converting word problems into graph models—start by identifying vertices and edges
2. Memorize the time complexities of key graph algorithms and know when to apply each
3. Review the PageRank concept with the damping factor and iterative computation process
4. Understand the relationship between graph properties and their applications in real systems
5. Solve previous years' university exam questions on graph applications to familiarize question patterns
