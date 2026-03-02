# **Warshall's and Floyd's Algorithms**

### Overview

- Dynamic programming algorithms used for finding the shortest paths in weighted graphs.
- Useful in various applications such as social network analysis, traffic routing, and network optimization.

### Warshall's Algorithm

---

### Key Points

- Finds the shortest path between all pairs of vertices in a weighted graph.
- Works by iteratively improving the shortest path between vertices.
- Uses a 2D array to store the shortest distances between vertices.

### Formula

- `w[v][u] = min(w[v][u], w[v][x] + w[x][u])` for all `u, v, x`
- Initialize `w[v][v] = 0`, `w[v][u] = inf` for `u != v`

### Floyd's Algorithm

---

### Key Points

- Finds the shortest path between all pairs of vertices in a weighted graph.
- More efficient than Warshall's algorithm for sparse graphs.
- Uses a 3D array to store the shortest distances between vertices.

### Formula

- `w[v][u] = min(w[v][u], w[v][x] + w[x][u])` for all `u, v, x`
- Initialize `w[v][v] = 0`, `w[v][u] = inf` for `u != v`

### Theorem

- `w[v][u] == w[u][v]` for all `v, u` (symmetry property)

### Time Complexity

- Warshall's algorithm: O(|V|^3)
- Floyd's algorithm: O(|V|^2 \* |E|)

### Space Complexity

- Warshall's algorithm: O(|V|^2)
- Floyd's algorithm: O(|V|^2)
