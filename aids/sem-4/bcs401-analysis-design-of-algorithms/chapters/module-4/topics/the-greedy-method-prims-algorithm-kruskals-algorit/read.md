# **THE GREEDY METHOD: Prim’s Algorithm, Kruskal’s Algorithm, Dijkstra’s Algorithm, Huffman Trees and Codes**

## **Introduction**

The Greedy Method is a simple, intuitive, and efficient approach to solving optimization problems. It involves making the locally optimal choice at each step, hoping that these local choices will lead to a global optimum. In this study material, we will explore four classic problems that can be solved using the Greedy Method: Prim’s Algorithm, Kruskal’s Algorithm, Dijkstra’s Algorithm, and Huffman Coding.

## **Prim’s Algorithm**

**Definition:** Prim’s Algorithm is a Greedy Method used to find the Minimum Spanning Tree (MST) of a graph. It starts with an empty tree and grows it by adding the smallest available edge at each step.

**How it works:**

1.  Choose an arbitrary vertex as the starting point.
2.  Initialize an empty tree.
3.  Find the smallest edge connected to the starting vertex.
4.  Add the edge to the tree and mark both vertices as visited.
5.  Repeat steps 3-4 until all vertices are visited.

**Example:**

Suppose we have a graph with vertices A, B, C, D, and E, and edges with weights 2, 3, 1, 4, and 5, respectively. We choose vertex A as the starting point.

1.  Add edge (A, B) with weight 2 to the tree.
2.  Add edge (A, C) with weight 1 to the tree.
3.  Add edge (B, C) with weight 3 to the tree.
4.  Add edge (B, D) with weight 4 to the tree.
5.  Add edge (C, D) with weight 5 to the tree.

The Minimum Spanning Tree is {(A, B), (A, C), (B, C), (B, D), (C, D)}.

**Key Concepts:**

- **Minimum Spanning Tree (MST):** A subgraph that connects all vertices with the minimum total edge weight.
- **Greedy Choice Property:** The locally optimal choice leads to a global optimum.

## **Kruskal’s Algorithm**

**Definition:** Kruskal’s Algorithm is a Greedy Method used to find the Minimum Spanning Tree (MST) of a graph. It starts with an empty tree and grows it by adding the smallest available edge at each step.

**How it works:**

1.  Sort all edges in non-decreasing order of their weights.
2.  Initialize an empty tree.
3.  Select the smallest edge and add it to the tree if it does not form a cycle.
4.  Repeat step 3 until all edges are selected.

**Example:**

Suppose we have a graph with vertices A, B, C, D, and E, and edges with weights 2, 3, 1, 4, and 5, respectively. We sort the edges in non-decreasing order of their weights.

1.  Select edge (A, C) with weight 1.
2.  Select edge (A, B) with weight 2.
3.  Select edge (B, D) with weight 4.
4.  Select edge (B, C) with weight 3.
5.  Select edge (C, D) with weight 5.

The Minimum Spanning Tree is {(A, C), (A, B), (B, D), (B, C), (C, D)}.

**Key Concepts:**

- **Minimum Spanning Tree (MST):** A subgraph that connects all vertices with the minimum total edge weight.
- **Disjoint Set Data Structure:** A data structure used to keep track of connected components in a graph.

## **Dijkstra’s Algorithm**

**Definition:** Dijkstra’s Algorithm is a Greedy Method used to find the shortest path between two nodes in a weighted graph.

**How it works:**

1.  Create a priority queue with all nodes as initial entries.
2.  Select the node with the minimum distance (i.e., the node with the highest priority).
3.  Update the distances of all adjacent nodes by adding the weight of the selected edge.
4.  Repeat step 2 until the destination node is reached.

**Example:**

Suppose we have a graph with nodes A, B, C, D, and E, and edges with weights 2, 3, 1, 4, and 5, respectively. We want to find the shortest path from node A to node D.

1.  Create a priority queue with all nodes as initial entries: A(0), B(3), C(4), D(6), E(7)
2.  Select node A with distance 0.
3.  Update the distances of adjacent nodes: B(3), C(4), D(6), E(7)
4.  Select node B with distance 3.
5.  Update the distances of adjacent nodes: C(7), D(9), E(10)
6.  Select node C with distance 4.
7.  Update the distances of adjacent nodes: D(12), E(13)
8.  Select node D with distance 6.
9.  No adjacent nodes can be reached.

The shortest path from node A to node D is A -> B -> C -> D.

**Key Concepts:**

- **Shortest Path:** The path with the minimum total edge weight between two nodes.
- **Priority Queue:** A data structure used to keep track of the nodes with the minimum distance.

## **Huffman Coding**

**Definition:** Huffman Coding is a Greedy Method used to compress data by assigning shorter codes to more frequent symbols.

**How it works:**

1.  Create a priority queue with all symbols as initial entries.
2.  Select the two symbols with the lowest frequencies and create a new internal node with these symbols as children.
3.  Add the internal node to the priority queue.
4.  Repeat step 2 until only one node is left.

**Example:**

Suppose we have a dataset with symbols 'A', 'B', 'C', 'D', 'E', and frequencies 5, 3, 2, 2, 1, respectively.

1.  Create a priority queue with all symbols as initial entries: A(5), B(3), C(2), D(2), E(1)
2.  Select symbols 'D' and 'E' and create a new internal node with these symbols as children.
3.  Add the internal node to the priority queue: A(5), B(3), C(2), (D,E)(3)
4.  Select symbols 'B' and 'C' and create a new internal node with these symbols as children.
5.  Add the internal node to the priority queue: A(5), (B,C)(2), (D,E)(3)
6.  Select symbols 'A' and the internal node with 'B' and 'C' as children and create a new internal node with these symbols as children.
7.  Add the internal node to the priority queue: (A,B,C)(3), (D,E)(3)
8.  Select the internal node with 'D' and 'E' as children and create a new internal node with these symbols as children.
9.  Add the internal node to the priority queue: (A,B,C)(3), (D,E)(2)
10. Select the internal node with 'A' and 'B' and 'C' as children and create a new internal node with these symbols as children. 11. Add the internal node to the priority queue: (A,B,C)(1), (D,E)(2)

The Huffman coding is {(A,B,C)(1), (D,E)(2)}.

**Key Concepts:**

- **Huffman Coding:** A method used to compress data by assigning shorter codes to more frequent symbols.
- **Priority Queue:** A data structure used to keep track of the symbols with the minimum frequency.

By understanding the Greedy Method and its applications in Prim’s Algorithm, Kruskal’s Algorithm, Dijkstra’s Algorithm, and Huffman Coding, you can develop effective problem-solving strategies for a wide range of optimization problems.
