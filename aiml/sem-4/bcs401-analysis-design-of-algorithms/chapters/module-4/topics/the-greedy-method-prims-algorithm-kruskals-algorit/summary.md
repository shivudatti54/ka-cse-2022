# **THE GREEDY METHOD: Prim’s Algorithm, Kruskal’s Algorithm, Dijkstra’s Algorithm, Huffman Trees and Codes**

## **Key Points**

### Introduction

- The Greedy Method: a heuristic approach to solving optimization problems
- Focus on finding the optimal solution by making locally optimal choices

### Prim’s Algorithm

---

- Minimum Spanning Tree (MST) problem
- greedy choice of the minimum edge that connects a new vertex to the tree
- **Theorem:** If there is a cycle in the MST, then the cycle must contain at least one edge with positive weight

### Kruskal’s Algorithm

---

- MST problem
- greedy choice of the minimum edge that does not form a cycle with the existing MST
- **Theorem:** If there is a cycle in the MST, then the cycle must contain at least one edge with zero weight

### Dijkstra’s Algorithm

---

- Shortest Path problem
- greedy choice of the minimum edge that reaches a new vertex
- **Theorem:** The shortest path to a vertex is the path that minimizes the sum of the weights of the edges

### Huffman Trees and Codes

---

- Binary Trees and Codes
- greedy construction of a Huffman tree by combining the two nodes with the lowest frequencies

### Formulas and Definitions

---

- **Weighted Graph:** a graph where each edge has a weight or label
- **Minimum Spanning Tree (MST):** a subgraph that connects all vertices with the minimum total weight
- **Shortest Path:** the path with the minimum total weight between two vertices

### Important Theorems

---

- **Prim’s Theorem:** If there is a cycle in the MST, then the cycle must contain at least one edge with positive weight
- **Kruskal’s Theorem:** If there is a cycle in the MST, then the cycle must contain at least one edge with zero weight
- **Dijkstra’s Theorem:** The shortest path to a vertex is the path that minimizes the sum of the weights of the edges
