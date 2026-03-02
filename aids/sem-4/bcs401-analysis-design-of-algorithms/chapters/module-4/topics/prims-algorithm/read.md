# Prim’s Algorithm

## Introduction

Prim's Algorithm is a fundamental greedy algorithm in graph theory used to find the Minimum Spanning Tree (MST) of a connected, weighted, and undirected graph. A spanning tree is a subgraph that includes all vertices of the original graph without forming any cycles, and a minimum spanning tree is the spanning tree with the minimum possible total edge weight. This algorithm holds significant importance in network design problems, including telephone network layouts, electrical grid planning, and road construction, where the goal is to connect all nodes with minimum total cost.

The algorithm was originally discovered in 1930 by Czech mathematician Vojtěch Jarník, later rediscovered by Robert Prim in 1957, and independently by Edsger Dijkstra in 1959. This is why it is sometimes known as the Jarník-Prim algorithm. In the context of the University of Delhi's Computer Science curriculum, Prim's Algorithm forms a critical component of the "Greedy Method" module, where it is studied alongside Kruskal's Algorithm and Dijkstra's Algorithm. Understanding Prim's Algorithm demonstrates the power of greedy choice—making locally optimal decisions to achieve globally optimal solutions—and provides essential problem-solving skills for algorithm design questions in semester examinations.

## Key Concepts

### Minimum Spanning Tree (MST)

A Minimum Spanning Tree of a connected, weighted graph G = (V, E) is a spanning tree T ⊆ E that connects all vertices in V with minimum total weight. The MST has exactly (|V| - 1) edges and satisfies three fundamental properties: it is acyclic, it connects all vertices, and its total edge weight is minimum among all possible spanning trees. These properties are essential for understanding why Prim's Algorithm produces correct results.

### Greedy Approach in Prim's Algorithm

Prim's Algorithm follows the greedy method paradigm by always selecting the minimum weight edge that connects a vertex already in the MST to a vertex outside the MST. This locally optimal choice, when applied repeatedly, guarantees finding the globally optimal MST. The algorithm builds the MST incrementally, starting from an arbitrary source vertex and growing the tree until all vertices are included.

### Algorithm Working

The algorithm maintains two sets of vertices: vertices already included in the MST (let's call this set MST) and vertices not yet included (called V-MST). At each step, it selects the minimum weight edge (u, v) where u ∈ MST and v ∈ (V - MST), adds this edge and vertex v to the MST, and updates the key values for all adjacent vertices. This process continues until all vertices are included in the MST.

### Data Structures for Implementation

The efficiency of Prim's Algorithm depends significantly on the data structure used to select the minimum weight edge. Using a simple array leads to O(V²) time complexity, which is suitable for dense graphs. However, using a binary min-heap or Fibonacci heap reduces the time complexity to O(E log V) or O(E + V log V) respectively, making the algorithm more efficient for sparse graphs. The choice of data structure is often examined in practical and theoretical questions in DU exams.

### Correctness Proof Outline

The correctness of Prim's Algorithm rests on the CUT PROPERTY: for any cut in the graph (a partition of vertices into two sets), the minimum weight edge crossing the cut belongs to some MST. In Prim's Algorithm, at each step, we consider the cut between vertices already in MST and vertices not in MST. The algorithm always chooses the minimum weight edge crossing this cut. Since this edge is guaranteed to be part of some MST by the cut property, adding it never destroys the possibility of completing to a full MST. By induction, when the algorithm terminates, the selected edges form a complete spanning tree that is minimum.

## Examples

### Example 1: Simple Graph with 4 Vertices

Consider the following weighted graph with vertices {A, B, C, D} and the given edge weights:

```
    4
  A---B
  |   |
 2|   |3
  |   |
  C---D
    1
```

Edges: AB=4, AC=2, BD=3, CD=1, BC=∞ (no edge), AD=∞ (no edge)

Step-by-step execution of Prim's Algorithm:

**Step 1:** Start from vertex A. Add A to MST.
Key values: B=4, C=2, D=∞

**Step 2:** Select minimum key vertex from V-MST. Minimum is C with key 2.
Add edge AC to MST. Add C to MST.
Update keys: B remains 4, D remains ∞ (C has no edges to D with smaller weight)

**Step 3:** Select minimum key vertex from V-MST. Minimum is B with key 4.
Add edge AB to MST. Add B to MST.
Update keys: D's key becomes 3 through edge BD

**Step 4:** Select minimum key vertex from V-MST. Minimum is D with key 3.
Add edge BD to MST. Add D to MST.

MST edges: AC(2), AB(4), BD(3) with total weight = 9

### Example 2: Graph with 5 Vertices

Consider a graph with vertices {1, 2, 3, 4, 5} and edges with weights:
Edges: (1,2)=2, (1,3)=3, (2,3)=1, (2,4)=4, (3,4)=5, (3,5)=6, (4,5)=2

**Step 1:** Start from vertex 1. MST = {1}
Keys: 2=2, 3=3, 4=∞, 5=∞

**Step 2:** Select minimum = vertex 2 with key 2. Add edge (1,2) to MST.
MST = {1, 2}
Update: 3 remains 3 (via edge 1-3), 4 becomes 4 (via edge 2-4)

**Step 3:** Select minimum = vertex 3 with key 3. Add edge (1,3) to MST.
MST = {1, 2, 3}
Update: 4 becomes 4 (via edge 2-4), 5 becomes 6 (via edge 3-5)

**Step 4:** Select minimum = vertex 4 with key 4. Add edge (2,4) to MST.
MST = {1, 2, 3, 4}
Update: 5 becomes 2 (via edge 4-5)

**Step 5:** Select minimum = vertex 5 with key 2. Add edge (4,5) to MST.
MST = {1, 2, 3, 4, 5}

Total MST weight = 2 + 3 + 4 + 2 = 11

### Example 3: Comparing with Kruskal's Algorithm

For the same graph in Example 2, let's verify using Kruskal's Algorithm:
Edges sorted by weight: (2,3)=1, (1,2)=2, (4,5)=2, (1,3)=3, (2,4)=4, (3,5)=6, (3,4)=5

Kruskal picks: (2,3), (1,2), (4,5), (1,3), (2,4) = Total 11

Both algorithms produce MST with the same total weight, confirming correctness. This example is important for exam questions comparing greedy algorithms.

## Exam Tips

1. UNDERSTAND THE CUT PROPERTY: The cut property is fundamental to Prim's Algorithm's correctness. In exams, questions frequently ask to explain why Prim's Algorithm works, and mentioning the cut property demonstrates deep understanding.

2. DISTINGUISH BETWEEN PRIM'S AND KRUSKAL'S: Prim's Algorithm grows a single tree from a starting vertex (like Dijkstra's), while Kruskal's Algorithm grows multiple trees and merges them (like a forest). Know when to apply each.

3. TIME COMPLEXITY MATTERS: For array implementation, Prim's runs in O(V²). With binary heap, it becomes O(E log V). With Fibonacci heap, it is O(E + V log V). Know these complexities and their implications for dense versus sparse graphs.

4. STARTING VERTEX IS ARBITRARY: Unlike Dijkstra's Algorithm where source matters, any starting vertex in Prim's Algorithm produces the same MST weight (though edge composition may differ in case of equal weights).

5. HANDLING DISCONNECTED GRAPHS: Prim's Algorithm cannot produce an MST for disconnected graphs. Always check graph connectivity first. If the graph is disconnected, Prim's will only find MST for the connected component containing the start vertex.

6. SIMILARITY WITH DIJKSTRA'S: Prim's Algorithm looks almost identical to Dijkstra's Algorithm. The key difference is: Dijkstra's uses distance from source and minimizes total path distance, while Prim's uses the minimum edge weight connecting to MST and minimizes spanning tree weight.

7. TRACING ALGORITHM STEP-BY-STEP: Most exam questions require tracing the algorithm manually. Practice tracing with different starting vertices and be comfortable showing each iteration's MST set and key values.

8. PROOF BY CONTRADICTION QUESTIONS: Be prepared to prove correctness using the cut property or exchange argument. The standard approach involves assuming a different MST exists and showing that replacing an edge leads to contradiction.