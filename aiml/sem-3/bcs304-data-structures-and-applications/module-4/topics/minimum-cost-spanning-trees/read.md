# Minimum Cost Spanning Trees


## Table of Contents

- [Minimum Cost Spanning Trees](#minimum-cost-spanning-trees)
- [Introduction](#introduction)
- [Formal Definition](#formal-definition)
  - [Fundamental Properties of MST](#fundamental-properties-of-mst)
  - [Illustrative Example](#illustrative-example)
- [Theoretical Foundations](#theoretical-foundations)
  - [Proof of Cut Property](#proof-of-cut-property)
  - [Proof of Cycle Property](#proof-of-cycle-property)
- [Kruskal's Algorithm](#kruskals-algorithm)
  - [Algorithm Concept](#algorithm-concept)
  - [Algorithm Pseudocode](#algorithm-pseudocode)
  - [Step-by-Step Execution Trace](#step-by-step-execution-trace)
  - [Time Complexity Analysis](#time-complexity-analysis)
  - [Union-Find Data Structure](#union-find-data-structure)
- [Prim's Algorithm](#prims-algorithm)
  - [Algorithm Concept](#algorithm-concept)
  - [Algorithm Pseudocode](#algorithm-pseudocode)
  - [Step-by-Step Execution Trace](#step-by-step-execution-trace)
  - [Time Complexity Analysis](#time-complexity-analysis)
  - [Comparison: Kruskal's vs Prim's](#comparison-kruskals-vs-prims)
- [Correctness Proof of Greedy Algorithms](#correctness-proof-of-greedy-algorithms)
  - [Kruskal's Algorithm Correctness](#kruskals-algorithm-correctness)
  - [Prim's Algorithm Correctness](#prims-algorithm-correctness)
- [Hard-Level Multiple Choice Questions](#hard-level-multiple-choice-questions)
- [Answer Key with Explanations](#answer-key-with-explanations)

## Introduction

A **Minimum Cost Spanning Tree (MST)** of a weighted, connected, undirected graph is a spanning tree whose total edge weight is the smallest among all possible spanning trees. The spanning tree is a subgraph that includes all vertices and is acyclic (a tree). MSTs are fundamental in network design problems such as telephone network layout, electrical grid installation, road construction, and computer network topology, where the objective is to connect all nodes at minimum total cost.

## Formal Definition

Given a weighted connected undirected graph $G = (V, E, w)$ where $w: E \rightarrow \mathbb{R}^+$ is the weight function, a minimum spanning tree $T$ is a spanning tree such that:

$$w(T) = \sum_{e \in E(T)} w(e)$$

is minimized, where $E(T)$ denotes the edge set of the tree $T$.

### Fundamental Properties of MST

| Property           | Description                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------ |
| **Edge Count**     | Contains exactly $\|V\| - 1$ edges                                                         |
| **Connected**      | Includes all vertices, forms a connected subgraph                                          |
| **Acyclic**        | Contains no cycles                                                                         |
| **Minimum Weight** | Total weight is minimum among all spanning trees                                           |
| **Uniqueness**     | MST is unique if all edge weights are distinct                                             |
| **Cut Property**   | For any cut of the graph, the minimum weight edge crossing the cut belongs to every MST    |
| **Cycle Property** | For any cycle in the graph, the maximum weight edge in that cycle cannot belong to any MST |

### Illustrative Example

Consider the weighted graph:

```
 0 ---4--- 1
 | \   / |
 8  2  6
 |   \ |
 2 ---3--- 3
```

Edges: (0,1,4), (0,2,8), (1,2,2), (1,3,6), (2,3,3)

**MST Edges:** {(1,2,2), (2,3,3), (0,1,4)}  
**Total Weight:** 2 + 3 + 4 = 9

---

## Theoretical Foundations

### Proof of Cut Property

**Theorem:** Let $C$ be any cut of graph $G$ (a partition of $V$ into two non-empty sets). If $e$ is the minimum weight edge crossing $C$, then $e$ belongs to some MST.

_Proof:_ Consider an arbitrary MST $T$. There are two cases:

1. If $e \in T$, the theorem holds trivially.
2. If $e \notin T$, then adding $e$ to $T$ creates a cycle. Since $e$ crosses cut $C$, at least one other edge $f$ in this cycle must also cross $C$ (otherwise the cycle would be entirely on one side). Since $e$ is the minimum weight edge crossing $C$, we have $w(e) \leq w(f)$. Removing $f$ and adding $e$ yields a new spanning tree $T' = T - \{f\} + \{e\}$ with weight $w(T') = w(T) - w(f) + w(e) \leq w(T)$. Since $T$ is an MST, $T'$ is also an MST containing $e$. $\square$

### Proof of Cycle Property

**Theorem:** For any cycle $C$ in graph $G$, if $e$ is the maximum weight edge in $C$, then $e$ does not belong to any MST.

_Proof:_ Let $T$ be an MST. Consider two cases:

1. If $e \notin T$, the theorem holds.
2. If $e \in T$, removing $e$ from $T$ disconnects the tree into two components forming a cut $C'$. Edge $e$ lies on cycle $C$, so there exists another edge $f \in C$ crossing the same cut $C'$. Since $e$ is the maximum weight edge in $C$, $w(e) \geq w(f)$. Replacing $e$ with $f$ yields $T' = T - \{e\} + \{f\}$ with weight $w(T') = w(T) - w(e) + w(f) \leq w(T)$. Since $T$ is optimal, $T'$ is also an MST but does not contain $e$. $\square$

---

## Kruskal's Algorithm

### Algorithm Concept

Kruskal's algorithm employs a greedy strategy, processing edges in ascending order of weight and adding an edge if it does not form a cycle with already selected edges. The algorithm uses the **Union-Find** (Disjoint Set Union) data structure to efficiently detect cycles.

### Algorithm Pseudocode

```
Kruskal(Graph G = (V, E, w)):
    Sort all edges in E by weight in non-decreasing order
    Initialize MST T = ∅
    Initialize Union-Find with V singleton sets

    for each edge (u, v, w) in sorted order:
        if Find(u) ≠ Find(v):           // u and v in different components
            Add edge (u, v, w) to T
            Union(u, v)                  // merge the two components
        if |T| = V - 1:
            break

    return T
```

### Step-by-Step Execution Trace

Using the example graph:

**Sorted Edges:** (1,2,2), (2,3,3), (0,1,4), (1,3,6), (0,2,8)

| Step | Edge   | Weight | Find(u) | Find(v) | Action                       | MST                   |
| ---- | ------ | ------ | ------- | ------- | ---------------------------- | --------------------- |
| 1    | (1, 2) | 2      | {1}     | {2}     | Add, Union(1,2)              | {(1,2)}               |
| 2    | (2, 3) | 3      | {1,2}   | {3}     | Add, Union                   | {(1,2), (2,3)}        |
| 3    | (0, 1) | 4      | {0}     | {1,2,3} | Add, Union                   | {(1,2), (2,3), (0,1)} |
| 4    | —      | —      | —       | —       | V-1 edges reached, terminate | —                     |

**Total MST Weight:** 2 + 3 + 4 = 9

### Time Complexity Analysis

- **Sorting edges:** $O(E \log E)$
- **Union-Find operations:** $O(E \cdot \alpha(V)) \approx O(E)$ (using path compression and union by rank)
- **Overall:** $O(E \log E) = O(E \log V)$ since $E \leq V^2$

### Union-Find Data Structure

```c
typedef struct {
    int parent[MAX];
    int rank[MAX];
} UnionFind;

void makeSet(UnionFind* uf, int n) {
    for (int i = 0; i < n; i++) {
        uf->parent[i] = i;
        uf->rank[i] = 0;
    }
}

int find(UnionFind* uf, int x) {
    if (uf->parent[x] != x)
        uf->parent[x] = find(uf, uf->parent[x]);  // Path compression
    return uf->parent[x];
}

void unionSets(UnionFind* uf, int x, int y) {
    int rootX = find(uf, x);
    int rootY = find(uf, y);
    if (rootX == rootY) return;

    // Union by rank
    if (uf->rank[rootX] < uf->rank[rootY])
        uf->parent[rootX] = rootY;
    else if (uf->rank[rootX] > uf->rank[rootY])
        uf->parent[rootY] = rootX;
    else {
        uf->parent[rootY] = rootX;
        uf->rank[rootX]++;
    }
}
```

---

## Prim's Algorithm

### Algorithm Concept

Prim's algorithm grows the MST from an arbitrary starting vertex. At each step, it adds the minimum weight edge that connects a vertex in the current MST to a vertex outside it. Unlike Kruskal's (which grows forests), Prim's maintains a single connected tree throughout execution.

### Algorithm Pseudocode

```
Prim(Graph G, start vertex s):
    for each vertex v in V:
        key[v] = ∞
        parent[v] = -1
        inMST[v] = false

    key[s] = 0

    Repeat V times:
        u = vertex with minimum key[v] where inMST[v] = false
        inMST[u] = true

        for each neighbor v of u with edge weight w(u,v):
            if not inMST[v] and w(u,v) < key[v]:
                key[v] = w(u,v)
                parent[v] = u

    Return edges (parent[v], v) for all v ≠ s
```

### Step-by-Step Execution Trace

Starting from vertex 0:

| Iteration | u   | key[0] | key[1] | key[2] | key[3] | Added Edge |
| --------- | --- | ------ | ------ | ------ | ------ | ---------- |
| Initial   | —   | 0      | ∞      | ∞      | ∞      | —          |
| 1         | 0   | 0      | 4(0)   | 8(0)   | ∞(0)   | —          |
| 2         | 1   | 0      | 4(0)   | 2(1)   | 6(1)   | (0,1,4)    |
| 3         | 2   | 0      | 4(0)   | 2(1)   | 3(2)   | (1,2,2)    |
| 4         | 3   | 0      | 4(0)   | 2(1)   | 3(2)   | (2,3,3)    |

**MST Edges:** (0,1,4), (1,2,2), (2,3,3)  
**Total Weight:** 9

### Time Complexity Analysis

- **Using Adjacency Matrix:** $O(V^2)$ — simple implementation
- **Using Binary Heap + Adjacency List:** $O(E \log V)$
- **Using Fibonacci Heap:** $O(E + V \log V)$

### Comparison: Kruskal's vs Prim's

| Aspect             | Kruskal's                            | Prim's                                   |
| ------------------ | ------------------------------------ | ---------------------------------------- |
| **Approach**       | Edge-centric, processes sorted edges | Vertex-centric, grows from start vertex  |
| **Data Structure** | Union-Find                           | Priority Queue (Min-Heap/Fibonacci Heap) |
| **Best For**       | Sparse graphs (E ≈ V)                | Dense graphs (E ≈ V²)                    |
| **Time (Basic)**   | $O(E \log E)$                        | $O(V^2)$                                 |
| **Space**          | O(E) for sorted edges                | O(V + E)                                 |

---

## Correctness Proof of Greedy Algorithms

### Kruskal's Algorithm Correctness

**Theorem:** Kruskal's algorithm always produces an MST.

_Proof by Cut Property:_ Consider edges processed in non-decreasing order. When Kruskal considers an edge $e$, let $C$ be the cut separating vertices in the current forest $F$ (connected components). Edge $e$ is the minimum weight edge crossing $C$ among all edges not yet processed (since all lighter edges have been considered). By the cut property, $e$ belongs to every MST. Adding $e$ preserves optimality. By induction, the final tree is an MST. $\square$

### Prim's Algorithm Correctness

**Theorem:** Prim's algorithm always produces an MST.

_Proof by Cut Property:_ At each iteration, let $S$ be the set of vertices already in the MST, and let $e = (u, v)$ be the minimum weight edge with $u \in S$ and $v \notin S$. The cut $(S, V-S)$ has $e$ as its minimum weight edge crossing. By the cut property, $e$ belongs to every MST. Adding $e$ preserves optimality. By induction, the final tree is an MST. $\square$

---

## Hard-Level Multiple Choice Questions

1. **Consider a graph with vertices {1,2,3,4,5} and edges with weights: (1-2:3), (1-3:4), (1-4:2), (1-5:5), (2-3:1), (2-4:6), (2-5:7), (3-4:8), (3-5:3), (4-5:9). What is the total weight of the MST using Prim's algorithm starting from vertex 1?**

   a) 7  
   b) 8  
   c) 9  
   d) 10

2. **Which of the following statements is FALSE about MST algorithms?**

   a) Both Kruskal's and Prim's algorithms use the greedy approach  
   b) Kruskal's algorithm always produces the same MST regardless of edge sorting stability  
   c) Prim's algorithm can be implemented using a priority queue  
   d) The cut property guarantees correctness of both algorithms

3. **In a graph with 7 vertices and 15 edges, what is the time complexity of Kruskal's algorithm using Union-Find with path compression and union by rank?**

   a) O(7 log 7)  
   b) O(15 log 15)  
   c) O(15 log 7)  
   d) O(7²)

4. **Given a complete graph with n vertices (every pair connected), which algorithm is more efficient for finding MST?**

   a) Kruskal's  
   b) Prim's  
   c) Both equal  
   d) Neither works

5. **If all edges in a graph have distinct weights, how many MSTs can the graph have?**

   a) 0  
   b) 1  
   c) n  
   d) Depends on structure

---

## Answer Key with Explanations

1. **Answer: (c) 9**  
   Sorted edges from 1: (2-3:1), (1-4:2), (1-2:3), (1-3:4), (1-5:3), (3-5:3), (1-2:3), (1-3:4), (1-5:5), (2-4:6)... Tracing Prim's from vertex 1: keys become {0,3,4,2,3}, select 1→4(2), then 1→2(3), then 1→5(3), then 2→3(1). Total = 2+3+3+1 = 9.

2. **Answer: (b)**  
   FALSE statement. Kruskal's can produce different MSTs if edges have equal weights. With distinct weights, MST is unique.

3. **Answer: (b)**  
   Time = O(E log E) = O(15 log 15). Using properties of logs, this equals O(15 log 15).

4. **Answer: (b) Prim's**  
   For dense graphs (E ≈ V²), Prim's with adjacency matrix gives O(V²), while Kruskal's requires O(E log E) ≈ O(V² log V).

5. **Answer: (b) 1**  
   With distinct edge weights, the MST is unique by definition.
