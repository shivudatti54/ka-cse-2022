# Trees and Spanning Trees

## Introduction
Trees are fundamental discrete structures in computer science that model hierarchical relationships. A tree is an acyclic connected graph with N vertices and (N-1) edges. Spanning trees extend this concept to connected undirected graphs - a spanning tree is a subgraph that includes all vertices of the original graph with the minimum number of edges required to maintain connectivity.

The importance of spanning trees is evident in network design, circuit theory, and clustering algorithms. Minimum Spanning Trees (MSTs) have critical applications in:
- Designing efficient computer networks
- Creating transportation infrastructure
- Cluster analysis in machine learning
- Approximation algorithms for NP-hard problems

Real-world examples include spanning tree protocol in network bridges (IEEE 802.1D) and Kruskal's algorithm for optimizing fiber optic cable layouts in cities.

## Key Concepts
1. **Tree Properties**:
   - Acyclic connected graph
   - Exactly n-1 edges for n vertices
   - Unique path between any two vertices

2. **Spanning Tree**:
   - Subgraph containing all vertices of original graph
   - Minimal connected (exactly n-1 edges for n-vertex graph)
   - Can have multiple spanning trees for a single graph

3. **Minimum Spanning Tree (MST)**:
   - Spanning tree with minimum total edge weight
   - Two main algorithms: Kruskal's and Prim's
   - Cut property: Lightest edge across any partition belongs to MST

4. **Kruskal's Algorithm**:
   - Sort all edges in non-decreasing order
   - Add edges one by one without forming cycles
   - Time complexity: O(E log E) using Union-Find

5. **Prim's Algorithm**:
   - Start with arbitrary vertex
   - Grow tree by adding cheapest edge connecting tree to non-tree vertex
   - Time complexity: O(E + V log V) with Fibonacci heap

6. **Cycle-Cut Duality**:
   - For any cycle in graph, heaviest edge not in MST
   - For any cut in graph, lightest edge is in MST

## Examples

**Example 1: Find All Spanning Trees**
```
Given graph:
A-B
|/|
C-D
```
*Solution:*
1. Original graph has 4 vertices and 5 edges
2. Spanning tree requires 3 edges
3. Possible spanning trees = Total combinations of 3 edges without cycles
4. Calculate using Kirchhoff's theorem or enumeration:
   - Remove 2 edges from original graph without disconnecting
   - Total spanning trees = 8

**Example 2: Kruskal's Algorithm**
```
Weights matrix:
A-B: 3
A-C: 1
B-C: 4
B-D: 2
C-D: 5
```
*Steps:*
1. Sort edges: AC(1), BD(2), AB(3), BC(4), CD(5)
2. Add AC (no cycle)
3. Add BD (no cycle)
4. Add AB (forms A-B-C-A cycle? Check using Union-Find)
   - A and B in different sets: Add AB
5. Total weight: 1+2+3 = 6

**Example 3: Prim's Algorithm**
```
Starting from vertex A:
Weights same as Example 2
```
*Steps:*
1. Initialize: {A}, edges = [A-C(1), A-B(3)]
2. Select A-C(1). Now {A,C}
3. Available edges: C-B(4), C-D(5), A-B(3)
4. Select A-B(3). Now {A,B,C}
5. Available edges: B-D(2), C-D(5)
6. Select B-D(2). MST complete. Total weight: 6

## Exam Tips
1. Always verify acyclic property using DFS/BFS when manually finding spanning trees
2. For MST problems, state which algorithm (Kruskal/Prim) is better based on graph density
3. Remember both algorithms are greedy but use different approaches
4. Practice matrix representation of graphs for Prim's algorithm
5. In proofs, frequently use contradiction with cycle-cut property
6. For weighted graphs, MST is unique if all edge weights are distinct
7. Spanning trees have applications in network reliability - be prepared for scenario-based questions