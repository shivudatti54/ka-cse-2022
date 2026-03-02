# Minimum Spanning Tree

## Introduction
A Minimum Spanning Tree (MST) is a fundamental concept in graph theory with critical applications in network design, clustering, and approximation algorithms. It represents the minimum-cost subgraph connecting all vertices in a weighted undirected graph without cycles. MSTs are particularly valuable in scenarios like designing efficient telecommunications networks, power grids, and transportation systems where cost optimization is paramount.

The importance of MSTs stems from their ability to solve real-world optimization problems efficiently. With algorithms like Kruskal's and Prim's operating in O(E log V) time, they provide practical solutions for large-scale problems. Modern applications include IoT network design, circuit board routing, and even in machine learning for hierarchical clustering.

## Key Concepts
1. **Spanning Tree**: A subgraph that includes all vertices with minimum possible edges (|V|-1 edges) and no cycles
2. **Greedy Approach**: Both Kruskal's and Prim's algorithms use greedy strategies
3. **Cut Property**: Basis for Prim's algorithm - lightest edge crossing a cut belongs to MST
4. **Cycle Property**: Foundation for Kruskal's algorithm - heaviest edge in any cycle not in MST
5. **Union-Find Data Structure**: Critical for efficient cycle detection in Kruskal's algorithm
6. **Priority Queue**: Used in Prim's algorithm for efficient edge selection
7. **Edge vs Vertex-Centric**: Kruskal's processes edges, Prim's grows from a vertex

**Kruskal's Algorithm**:
1. Sort all edges in non-decreasing order
2. Add edges one by one from lightest to heaviest
3. Use Union-Find to avoid cycles
4. Stop when |V|-1 edges are added

**Prim's Algorithm**:
1. Start with arbitrary root node
2. Maintain a min-heap of edges connecting to MST
3. Always add the smallest edge from the heap
4. Update heap with new adjacent edges

## Examples

**Example 1: Basic MST Construction**
```
Graph:
A-B: 3
A-C: 1
B-C: 4
B-D: 2
C-D: 5

Kruskal's Steps:
1. Sort edges: AC(1), BD(2), AB(3), BC(4), CD(5)
2. Add AC (MST edges: 1)
3. Add BD (MST edges: 2)
4. Add AB (Total edges: 3, stop)
Total weight: 1+2+3 = 6

Prim's Steps (Start at A):
1. Adjacent edges: AB(3), AC(1) → choose AC
2. Adjacent to {A,C}: AB(3), CD(5) → choose AB
3. Adjacent to {A,B,C}: BD(2) → choose BD
Final MST same as Kruskal's
```

**Example 2: Real-world Network Design**
Problem: Connect 5 offices with fiber optics. Costs between locations:
```
NY-CHI: $50k
NY-LON: $120k
CHI-LON: $80k
NY-SF: $30k
CHI-SF: $40k
SF-LON: $70k

Solution using Kruskal's:
1. Sort edges: NY-SF(30), CHI-SF(40), NY-CHI(50), SF-LON(70), CHI-LON(80), NY-LON(120)
2. Add NY-SF
3. Add CHI-SF
4. Add NY-CHI (creates cycle NY-CHI-SF-NY? No)
5. Add SF-LON (total edges: 4)
Total cost: 30+40+50+70 = $190k
```

## Exam Tips
1. Always mention whether the graph is connected before applying MST algorithms
2. For time complexity questions, specify graph representation (adjacency matrix vs list)
3. Remember Kruskal's works better for sparse graphs, Prim's for dense graphs
4. Practice edge case: Multiple edges with same weight (MST not unique)
5. Be prepared to prove MST properties using contradiction
6. Implement Union-Find with path compression and union by rank for optimal complexity
7. In written solutions, clearly show edge selection order and rejection reasons