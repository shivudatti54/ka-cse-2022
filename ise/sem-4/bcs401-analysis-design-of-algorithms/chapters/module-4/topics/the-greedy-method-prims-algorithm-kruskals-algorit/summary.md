# **THE GREEDY METHOD: Prim’s Algorithm, Kruskal’s Algorithm, Dijkstra’s Algorithm, Huffman Trees and Codes**

## **Overview**

- The Greedy Method: a heuristic approach that makes the locally optimal choice at each step with the hope of finding a global optimum solution.
- Four key algorithms:
  - Prim’s Algorithm
  - Kruskal’s Algorithm
  - Dijkstra’s Algorithm
  - Huffman Trees and Codes

## **Key Algorithms**

### Prim’s Algorithm

- Greedy algorithm for finding the minimum spanning tree (MST) of a graph.
- Start with an empty tree and add edges one by one, choosing the edge with the minimum weight that connects a tree vertex to a forest vertex.
- Formula: `MST = ∅ ∪ (edge with min weight connecting tree vertex to forest vertex)`
- Time complexity: O(E log E)

### Kruskal’s Algorithm

- Greedy algorithm for finding the MST of a graph.
- Sort all edges in non-decreasing order of their weights.
- Add edges one by one, choosing the edge with the minimum weight that does not form a cycle.
- Formula: `MST = ∅ ∪ (edge with min weight that does not form cycle)`
- Time complexity: O(E log E)

### Dijkstra’s Algorithm

- Greedy algorithm for finding the shortest path between two nodes in a weighted graph.
- Choose the node with the minimum distance from the source node and update distances of neighboring nodes.
- Formula: `d(u) = min(d(u), d(v) + w(v))`, where `d(u)` is the distance from source node `u` and `w(v)` is the weight of edge `v`
- Time complexity: O((V + E) log V)

### Huffman Trees and Codes

- Greedy algorithm for constructing Huffman codes.
- Combine two nodes with the lowest frequencies and create a new node with a combined frequency.
- Formula: `h(x) = -∑p(x)log2p(x)`
- Time complexity: O(n log n)

## **Important Formulas and Theorems**

- **MST Theorem**: The MST of a graph with `n` vertices has `n-1` edges.
- **Dijkstra’s Theorem**: The shortest path between two nodes in a weighted graph is unique.
- **Huffman’s Theorem**: The Huffman code for a sequence of symbols is unique and optimal.

## **Revision Tips**

- Understand the local optimality of the Greedy Method.
- Practice solving problems using each algorithm.
- Review the formulas and theorems related to each algorithm.
