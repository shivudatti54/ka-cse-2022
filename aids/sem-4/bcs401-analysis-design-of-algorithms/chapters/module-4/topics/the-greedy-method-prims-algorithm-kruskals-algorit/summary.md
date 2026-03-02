# **THE GREEDY METHOD: Prim’s Algorithm, Kruskal’s Algorithm, Dijkstra’s Algorithm, Huffman Trees and Codes**

## **I. Introduction**

- The Greedy Method: an approach to solve optimization problems by making the locally optimal choice at each step, hoping it will lead to a global optimum.

## **II. Prim’s Algorithm**

- **Definition:** finds a minimum spanning tree for a connected, undirected, weighted graph.
- **Formula:** `MST = ∅; v = 1; while v ≠ V: choose edge e = (u, v) with minimum weight and add e to MST and v to MST; end while`
- **Theorem:** if graph is connected, then MST has a minimum total weight.

## **III. Kruskal’s Algorithm**

- **Definition:** finds a minimum spanning tree for a connected, undirected, weighted graph.
- **Formula:** `MST = ∅; Sort edges by weight; for each edge e in sorted order: if MST + e is connected, add e to MST; end for`
- **Theorem:** if graph is connected, then MST has a minimum total weight.

## **IV. Dijkstra’s Algorithm**

- **Definition:** finds the shortest path between two nodes in a weighted graph.
- **Formula:** `dist(v) = 0, dist(v) = ∞ for v ≠ s; for each node v: update dist(v) = min(dist(v), dist(u) + w(u,v)); end for`
- **Theorem:** if graph is connected, then shortest path from s to t can be found.

## **V. Huffman Trees and Codes**

- **Definition:** a binary tree where each leaf node represents a symbol and each internal node represents a bit.
- **Formula:** `H(x) = - ∑ p(x) log2 p(x)`
- **Theorem:** Huffman codes are optimal variable-length prefix codes.

## **VI. Huffman Coding**

- **Definition:** a method of encoding symbols using Huffman Trees.
- **Formula:** `h(x) = 0 if x = root; h(x) = b(h(y)) if x = node y, b ∈ {0,1}`
