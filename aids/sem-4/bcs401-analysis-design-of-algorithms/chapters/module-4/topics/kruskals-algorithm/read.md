# Kruskal's Algorithm

## Introduction

Kruskal's Algorithm is a fundamental greedy algorithm in graph theory used to find the Minimum Spanning Tree (MST) of a weighted undirected graph. A spanning tree is a subgraph that includes all vertices of the original graph without forming any cycles, and a minimum spanning tree is the spanning tree with the minimum possible total edge weight. This algorithm holds significant importance in network design problems, such as designing telephone networks, electrical grids, transportation networks, and computer networks, where the goal is to connect all nodes with minimum cost.

The algorithm was developed by Joseph Kruskal in 1956 and is based on the greedy method approach, where at each step, it selects the edge with the minimum weight that does not form a cycle with the already selected edges. This greedy choice property makes it efficient and conceptually straightforward. Unlike Prim's Algorithm, which grows the MST from a single vertex, Kruskal's Algorithm builds the MST by considering individual edges in increasing order of their weights, effectively treating each vertex as a separate component initially and gradually merging them.

Understanding Kruskal's Algorithm is essential for computer science students because it demonstrates the practical application of the greedy method, introduces the concept of disjoint set data structures (Union-Find), and provides a foundation for solving various optimization problems. The algorithm's elegance lies in its simplicity and its guaranteed optimality, as it always produces the minimum spanning tree for any weighted undirected graph.

## Key Concepts

### Minimum Spanning Tree (MST)

A spanning tree of a connected undirected graph is a subgraph that is a tree and contains all vertices of the graph. A minimum spanning tree is the spanning tree with the minimum total edge weight among all possible spanning trees. For a graph with V vertices, any spanning tree contains exactly V-1 edges. The MST problem is a classic optimization problem with numerous real-world applications in network design, clustering, and approximation algorithms for NP-hard problems.

### Greedy Method Approach

Kruskal's Algorithm follows the greedy method paradigm, which makes locally optimal choices at each step with the hope of finding a global optimum. The greedy choice in Kruskal's Algorithm is to always pick the minimum weight edge that does not create a cycle. This approach works because adding a minimum weight edge that doesn't form a cycle is always part of some minimum spanning tree—a property known as the cut property of MSTs.

### Disjoint Set Union (DSU) / Union-Find

The efficiency of Kruskal's Algorithm relies heavily on the Disjoint Set Union (DSU) data structure, also known as Union-Find. This data structure maintains a collection of disjoint sets and supports two primary operations: FIND and UNION. The FIND operation determines which set a particular element belongs to, typically implemented using path compression for efficiency. The UNION operation merges two sets together, typically implemented using union by rank. These operations allow the algorithm to efficiently detect cycles by checking whether two vertices belong to the same set.

### Cycle Detection

A fundamental aspect of Kruskal's Algorithm is preventing the formation of cycles in the growing spanning tree. When considering adding an edge between two vertices, the algorithm checks if these vertices are already connected through the edges selected so far. If they are in the same connected component, adding the edge would create a cycle, and the edge is rejected. If they are in different components, adding the edge merges these components without creating a cycle, and the edge is included in the MST.

### Edge Sorting

The algorithm begins by sorting all edges of the graph in non-decreasing order of their weights. This sorting step has a time complexity of O(E log E), where E is the number of edges. After sorting, the algorithm processes edges one by one, adding them to the MST if they don't form a cycle. The total time complexity, including the sorting step and DSU operations, is O(E log E) or equivalently O(E log V) since E ≤ V².

## Examples

### Example 1: Simple Graph with 4 Vertices

Consider a graph with 4 vertices (A, B, C, D) and the following edges with weights:
- AB: 10
- AC: 15
- AD: 20
- BC: 25
- BD: 30
- CD: 35

Step-by-step execution of Kruskal's Algorithm:

Step 1: Sort edges by weight: AB(10), AC(15), AD(20), BC(25), BD(30), CD(35)

Step 2: Process AB(10) - A and B are in different sets. Include edge. Sets: {A,B}, {C}, {D}

Step 3: Process AC(15) - A and C are in different sets. Include edge. Sets: {A,B,C}, {D}

Step 4: Process AD(20) - A and D are in different sets. Include edge. Sets: {A,B,C,D}

Step 5: Process BC(25) - B and C are already in the same set. REJECT (would form cycle)

Step 6: Process BD(30) - B and D are already in the same set. REJECT (would form cycle)

Step 7: Process CD(35) - C and D are already in the same set. REJECT (would form cycle)

MST Edges: AB, AC, AD
Total Weight: 10 + 15 + 20 = 45
Number of edges in MST: V-1 = 3 ✓

### Example 2: Graph with Multiple Components Initially

Consider a graph with vertices {1, 2, 3, 4, 5} and edges:
- 1-2: 2
- 1-3: 3
- 2-3: 1
- 2-4: 4
- 3-4: 5
- 4-5: 6

Step 1: Sort edges: 2-3(1), 1-2(2), 1-3(3), 2-4(4), 3-4(5), 4-5(6)

Step 2: Process 2-3(1) - Different sets. Include. Sets: {2,3}, {1}, {4}, {5}

Step 3: Process 1-2(2) - Different sets (1 and {2,3}). Include. Sets: {1,2,3}, {4}, {5}

Step 4: Process 1-3(3) - Same set (both in {1,2,3}). REJECT

Step 5: Process 2-4(4) - Different sets ({1,2,3} and {4}). Include. Sets: {1,2,3,4}, {5}

Step 6: Process 3-4(5) - Same set. REJECT

Step 7: Process 4-5(6) - Different sets ({1,2,3,4} and {5}). Include. Sets: {1,2,3,4,5}

MST Edges: 2-3, 1-2, 2-4, 4-5
Total Weight: 1 + 2 + 4 + 6 = 13
Number of edges: 5-1 = 4 ✓

### Example 3: Practical Network Design

Suppose we need to connect 5 cities (Delhi, Mumbai, Chennai, Kolkata, Bangalore) with minimum cost fiber optic cables. The cost (in crores) to connect each pair of cities is given:

- Delhi-Mumbai: 12
- Delhi-Kolkata: 10
- Delhi-Bangalore: 15
- Mumbai-Chennai: 8
- Mumbai-Kolkata: 20
- Chennai-Kolkata: 25
- Chennai-Bangalore: 18
- Kolkata-Bangalore: 22
- Mumbai-Bangalore: 30

Sorted edges: Mumbai-Chennai(8), Delhi-Kolkata(10), Delhi-Mumbai(12), Delhi-Bangalore(15), Chennai-Bangalore(18), Mumbai-Kolkata(20), Kolkata-Bangalore(22), Chennai-Kolkata(25), Mumbai-Bangalore(30)

Processing edges:
1. Mumbai-Chennai(8) - Include. Components: {Mumbai, Chennai}, {Delhi}, {Kolkata}, {Bangalore}
2. Delhi-Kolkata(10) - Include. Components: {Mumbai, Chennai}, {Delhi, Kolkata}, {Bangalore}
3. Delhi-Mumbai(12) - Different sets (Delhi in {Delhi, Kolkata}, Mumbai in {Mumbai, Chennai}). Include. Components: {Delhi, Kolkata, Mumbai, Chennai}, {Bangalore}
4. Delhi-Bangalore(15) - Different sets. Include. All cities connected.

MST: Mumbai-Chennai, Delhi-Kolkata, Delhi-Mumbai, Delhi-Bangalore
Total Cost: 8 + 10 + 12 + 15 = 45 crores
Number of edges: 5-1 = 4 ✓

## Exam Tips

For DU semester examinations, keep the following points in mind when answering questions on Kruskal's Algorithm:

ALWAYS STATE THE INITIAL STEP of sorting all edges in non-decreasing order of weights before processing. This is a critical first step that examiners look for.

WHEN ASKED TO TRACE THE ALGORITHM, maintain a clear record of which vertices are in which set after each edge selection. This demonstrates your understanding of the Union-Find process.

IF QUESTION ASKS FOR MINIMUM SPANNING TREE WEIGHT, verify that you have exactly V-1 edges in your MST, where V is the number of vertices. Having more or fewer edges indicates an error.

UNDERSTAND THE CYCLE DETECTION LOGIC: An edge is included only if its endpoints belong to different connected components. Use the concept that including an edge between vertices in the same component creates a cycle.

KNOW THE TIME COMPLEXITY: O(E log E) or O(E log V), where E is edges and V is vertices. Be prepared to explain why this complexity arises from sorting and DSU operations.

DISTINGUISH BETWEEN KRUSKAL'S AND PRIM'S ALGORITHM: Kruskal's starts with V single-vertex components and merges them, while Prim's starts from one vertex and grows a single tree. This is a common exam question.

REMEMBER THAT KRUSKAL'S WORKS WELL FOR SPARSE GRAPHS (fewer edges) while Prim's is often preferred for dense graphs. This is a useful comparative analysis point.

THE CUT PROPERTY: If asked to prove correctness, remember that the greedy choice is justified by the cut property—any minimum weight edge crossing a cut belongs to some MST.