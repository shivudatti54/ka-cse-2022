# Directed Acyclic Graphs (DAGs) and Topological Ordering - Summary

## Key Definitions and Concepts

- **DAG (Directed Acyclic Graph):** A directed graph with no directed cycles; every DAG has at least one vertex with in-degree 0 and at least one with out-degree 0.

- **Topological Sort:** A linear ordering of vertices in a DAG such that for every directed edge (u, v), vertex u appears before vertex v in the ordering.

- **In-degree:** The number of incoming edges to a vertex; out-degree is the number of outgoing edges.

- **Kahn's Algorithm:** A BFS-based topological sorting algorithm that uses in-degree counts and processes vertices with zero in-degree first.

- **DFS-based Topological Sort:** Uses depth-first search, adding vertices to the result after exploring all their descendants.

## Important Formulas and Theorems

- **Time Complexity:** O(V + E) for both Kahn's and DFS-based approaches
- **Space Complexity:** O(V) for both algorithms
- **Cycle Detection:** A directed graph is acyclic if and only if topological sort processes all vertices

## Key Points

- Topological ordering exists ONLY for DAGs—if a graph has cycles, topological sort is impossible.

- Any DAG has at least one topological ordering, and many DAGs have multiple valid orderings.

- Kahn's algorithm uses a queue of vertices with in-degree 0; process each vertex and reduce neighbors' in-degrees.

- DFS-based approach adds vertices to the result list when their DFS call finishes, then reverses the list.

- In Kahn's algorithm, if processed vertices < total vertices, the graph contains a cycle.

- A vertex with in-degree 0 always comes first in any topological ordering; a vertex with out-degree 0 can come last.

- DAGs model partial orders and are used in course scheduling, build systems, task planning, and dependency resolution.

## Common Mistakes to Avoid

- Attempting topological sort on graphs with cycles (always check for cycles first).

- Forgetting to reduce neighbor in-degrees after processing a vertex in Kahn's algorithm.

- Not checking if in-degree becomes 0 before adding vertices to the queue.

- Forgetting to reverse the result in DFS-based topological sort.

- Confusing in-degree with out-degree; only in-degree 0 vertices start the process.

## Revision Tips

1. Practice Kahn's algorithm on 5-6 different graphs until you can do it without mistakes.

2. Remember the cycle detection rule: processed vertices must equal total vertices for a valid DAG.

3. For verification, always check that for every edge (u, v), position(u) < position(v).

4. Know the time and space complexities by heart—they're frequently tested.

5. Draw the graph first before applying any algorithm; visual understanding prevents errors.