# **Bellman-Ford and Path Vector Routing Algorithm Revision Notes**

## **Introduction**

- The Bellman-Ford algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph.
- The path vector routing algorithm is used to find the shortest path between two vertices in a network.

## **Bellman-Ford Algorithm**

- **Definition:** The Bellman-Ford algorithm is a dynamic programming algorithm that finds the shortest path from a source vertex to all other vertices in a weighted graph.
- **Theorem:** The Bellman-Ford algorithm can handle negative weight edges, but it may not always find the optimal solution.
- **Formula:**
  - `d[v] = min(d[v], d[u] + w(u, v))` for all vertices `v` and `u` in the graph
- **Steps:**
  1.  Initialize `d[v] = ∞` for all vertices `v` except the source vertex `s`, which is set to `0`.
  2.  Relax all edges `w(u, v)` for `i = 1` to `V-1`, where `V` is the number of vertices.
  3.  Check for negative weight cycles.

## **Path Vector Routing Algorithm**

- **Definition:** The path vector routing algorithm is a routing algorithm that finds the shortest path between two vertices in a network by maintaining a path vector.
- **Theorem:** The path vector routing algorithm is an efficient algorithm for finding the shortest path in a network.
- **Formula:** `path[v] = [v] for the source vertex, and path[v] = [v, u] if the edge (u, v) is in the shortest path`
- **Steps:**
  1.  Initialize the path vector for the source vertex.
  2.  For each vertex `v`, check if the edge `(s, v)` is in the shortest path.
  3.  If it is, update the path vector for `v`.

## **Key Points**

- The Bellman-Ford algorithm can handle negative weight edges, but it may not always find the optimal solution.
- The path vector routing algorithm is an efficient algorithm for finding the shortest path in a network.
- The algorithm uses dynamic programming to find the shortest path from a source vertex to all other vertices in a weighted graph.
- The algorithm can handle negative weight edges, but it may not always find the optimal solution.

## **Example Use Cases**

- Finding the shortest path between two vertices in a network.
- Finding the shortest path from a source vertex to all other vertices in a weighted graph.
- Handling negative weight edges in a weighted graph.
