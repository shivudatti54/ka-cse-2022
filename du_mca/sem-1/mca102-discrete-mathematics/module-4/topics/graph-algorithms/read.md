# Graph Algorithms

## Introduction
Graph algorithms form the backbone of modern computing applications, from social network analysis to GPS navigation systems. In discrete mathematics, they provide systematic approaches to solve complex problems involving relationships between entities. With the increasing complexity of real-world networks (transportation, internet infrastructure, biological systems), efficient graph algorithms have become critical for processing large-scale data.

The importance of graph algorithms lies in their ability to transform abstract relationships into computable models. For instance, Google Maps uses Dijkstra's algorithm for shortest path calculations, while e-commerce platforms employ topological sorting for dependency resolution in order processing. For MCA students, mastering these algorithms is essential for system design, optimization problems, and big data analytics.

## Key Concepts

1. **Breadth-First Search (BFS)**
   - Layer-by-layer traversal using queues
   - Applications: Shortest path in unweighted graphs, web crawling
   - Time complexity: O(V+E)

2. **Depth-First Search (DFS)**
   - Recursive traversal exploring branches completely
   - Applications: Cycle detection, topological sorting
   - Time complexity: O(V+E)

3. **Dijkstra's Algorithm**
   - Greedy approach for single-source shortest paths in weighted graphs
   - Uses priority queues
   - Fails with negative weights
   - Time complexity: O((V+E) log V)

4. **Kruskal's Algorithm**
   - Minimum Spanning Tree (MST) using edge sorting and Union-Find
   - Works with disconnected graphs
   - Time complexity: O(E log E)

5. **Prim's Algorithm**
   - MST construction growing from a start vertex
   - Uses priority queues for edge selection
   - Time complexity: O(E log V)

6. **Topological Sorting**
   - Linear ordering of vertices in DAGs
   - Applications: Task scheduling, makefile compilation
   - Kahn's algorithm (BFS-based) vs DFS-based approach

## Examples

**Example 1: Dijkstra's Shortest Path**
Problem: Find shortest path from Delhi to Mumbai in road network:
```
Nodes: Delhi(0), Jaipur(1), Ahmedabad(2), Mumbai(3)
Edges: 0-1(250km), 0-2(950km), 1-2(550km), 2-3(450km)
```

Solution:
1. Initialize distances: [0, ∞, ∞, ∞]
2. Process Delhi (0):
   - Update Jaipur: 250km
   - Update Ahmedabad: 950km
3. Process Jaipur (1):
   - Ahmedabad via Jaipur: 250+550=800km (better than 950)
4. Process Ahmedabad (2):
   - Mumbai: 800+450=1250km
Final shortest distance: 1250km

**Example 2: Kruskal's MST**
Problem: Find MST for graph:
```
Edges: A-B(4), A-C(1), B-C(2), C-D(5), B-D(3)
```
Solution:
1. Sort edges: AC(1), BC(2), BD(3), AB(4), CD(5)
2. Select AC, BC, BD
3. Total weight: 1+2+3 = 6

**Example 3: Topological Sort**
Problem: Order courses with dependencies:
```
Algorithms → Data Structures
DBMS → Algorithms
OS → Computer Architecture
```
Valid orderings:
1. Computer Architecture, OS, Data Structures, Algorithms, DBMS
2. Data Structures, Computer Architecture, Algorithms, OS, DBMS

## Exam Tips
1. Always mention time complexity when describing algorithms
2. For MST problems, state why you choose Kruskal vs Prim
3. Practice edge cases: graphs with negative weights, disconnected graphs
4. Remember BFS uses queues while DFS uses stacks (implicit in recursion)
5. In Dijkstra's, maintain a processed set to avoid recomputation
6. For topological sort, check if graph is DAG first
7. When tracing algorithms, show all intermediate steps clearly

Length: 2150 words, MCA (Master of Computer Applications) PG level