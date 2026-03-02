# **Bellman-Ford and Path Vector Routing Algorithm**

## **Key Points**

- **Bellman-Ford Algorithm**
  - Used to find the shortest path from a single source vertex to all other vertices in a graph.
  - Can handle negative weight edges.
  - Iterative approach with a maximum of |V| - 1 iterations.
  - Formula: `d[v] = min(d[v], d[u] + w(e, u, v))` for all edges (u, v) and for all vertices v.
- **Path Vector Routing Algorithm**
  - Used to find the shortest path between two vertices in a graph.
  - Uses a vector to store the shortest distance from the source vertex to all other vertices.
  - Formula: `d[v] = min(d[v], d[u] + w(e, u, v))` for all edges (u, v) and for all vertices v.
- **Important Formulas**
  - Bellman-Ford: `d[v] = min(cost(v, u) + d[u])` for all edges (u, v) and for all vertices v.
  - Path Vector Routing: `d[v] = min(cost(v, u) + d[u])` for all edges (u, v) and for all vertices v.
- **Definitions**
  - **Vertex**: A node in a graph.
  - **Edge**: A connection between two vertices.
  - **Weight**: The cost or distance associated with an edge.
- **Theorems**
  - **Bellman-Ford Theorem**: The Bellman-Ford algorithm can find the shortest path from a single source vertex to all other vertices in a graph with negative weight edges.

## **Revision Notes**

- Focus on the differences between the Bellman-Ford and Path Vector Routing algorithms.
- Practice implementing the algorithms using sample graphs.
- Review the formulas, definitions, and theorems to ensure a solid understanding of the concepts.
