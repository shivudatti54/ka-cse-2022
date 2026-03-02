# Dijkstra's Algorithm

## Table of Contents

- [Dijkstra's Algorithm](#dijkstras-algorithm)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Algorithm Overview](#algorithm-overview)
  - [Formal Description](#formal-description)
  - [Correctness Proof Sketch](#correctness-proof-sketch)
  - [Time Complexity Analysis](#time-complexity-analysis)
  - [Limitations](#limitations)
- [Examples](#examples)
  - [Worked Example 1: Step-by-Step Execution](#worked-example-1-step-by-step-execution)
  - [Worked Example 2: Practical Application](#worked-example-2-practical-application)
  - [Pseudocode Implementation](#pseudocode-implementation)
- [Exam Tips](#exam-tips)

## Introduction

Dijkstra's Algorithm, developed by computer scientist Edsger W. Dijkstra in 1956, is a fundamental greedy algorithm for finding the shortest paths from a single source vertex to all other vertices in a weighted graph with non-negative edge weights. This algorithm finds extensive applications in network routing protocols (such as OSPF and IS-IS), GPS navigation systems, flight scheduling, and road network analysis. The algorithm exemplifies the greedy approach, where making locally optimal choices at each step leads to a globally optimal solution, provided certain conditions (non-negative weights) are satisfied.

The problem addressed by Dijkstra's Algorithm can be formally stated as follows: Given a weighted graph G = (V, E) with a weight function w: E → ℝ⁺ (non-negative weights), and a source vertex s ∈ V, find the shortest path distance from s to every other vertex v ∈ V. The algorithm maintains a set S of vertices whose shortest distance from the source has been finalized, and iteratively selects the vertex with the minimum tentative distance from the priority queue to add to S.

## Key Concepts

### Algorithm Overview

Dijkstra's Algorithm operates by maintaining a priority queue (min-heap) containing vertices with their current tentative distances. At each iteration, the vertex with the minimum distance is extracted from the priority queue, and its distance is finalized. Then, for each adjacent vertex, the algorithm attempts to improve its distance through the recently finalized vertex—a process called relaxation.

### Formal Description

Let dist[v] represent the current shortest distance from source s to vertex v, and let π[v] represent the predecessor of v on the shortest path. The algorithm initializes dist[s] = 0 and dist[v] = ∞ for all v ≠ s. It proceeds by extracting the minimum distance vertex u from the priority queue, and for each neighbor v of u, performs relaxation:

**Relaxation Operation:**

```
if dist[u] + w(u, v) < dist[v]:
 dist[v] = dist[u] + w(u, v)
 π[v] = u
 update priority queue with new dist[v]
```

### Correctness Proof Sketch

The correctness of Dijkstra's Algorithm rests on a key invariant and proof by contradiction.

**Lemma (Invariant):** When a vertex u is removed from the priority queue (i.e., added to set S), dist[u] equals the length of the shortest path from source s to u.

**Proof by Induction:**

_Base Case:_ For the source vertex s, dist[s] = 0, which is clearly the shortest distance to itself.

_Inductive Step:_ Assume the invariant holds for all vertices already in S. Let u be the next vertex extracted from the priority queue with minimum dist[u]. Consider any alternative path from s to u that ends with edge (x, u) where x ∉ S. Since u has minimum dist[u] among all vertices in the priority queue, and all edges have non-negative weights, we have:

dist[u] ≤ dist[x] + w(x, u)

By the inductive hypothesis, dist[x] is the true shortest distance to x. Therefore, any path through x to u is at least as long as dist[u]. Hence, no shorter path to u exists, and dist[u] is optimal when u is extracted.

### Time Complexity Analysis

The time complexity depends on the data structure used for the priority queue:

| Data Structure | Extract-Min | Decrease-Key   | Overall Complexity |
| -------------- | ----------- | -------------- | ------------------ |
| Array          | O(V)        | O(1)           | O(V² + E)          |
| Binary Heap    | O(log V)    | O(log V)       | O((V + E) log V)   |
| Fibonacci Heap | O(log V)\*  | O(1) amortized | O(V log V + E)     |

\*where V = |V| and E = |E|

For sparse graphs (E ≈ V), the binary heap implementation yields O(V log V), while for dense graphs (E ≈ V²), the array implementation performs better at O(V²).

### Limitations

Dijkstra's Algorithm fails when edge weights are negative. Consider a graph with negative weights: the algorithm may finalize a vertex before discovering a shorter path through an unreached vertex. The Bellman-Ford algorithm handles negative weights but runs in O(VE) time.

## Examples

### Worked Example 1: Step-by-Step Execution

Consider the following graph with source vertex A:

```
 4
 A ------- B
 | │
 9 | | 1
 | ▼
 D ------- C
 2 3
```

Edge list: A→B(4), A→D(9), B→C(1), D→C(2), C→E(6), B→E(5)

**Step 0:** Initialize

- dist[A] = 0, dist[others] = ∞
- Priority Queue: [(A,0)]

**Step 1:** Extract A (distance 0 finalized)

- Relax neighbors: B→4, D→9
- PQ: [(B,4), (D,9)]

**Step 2:** Extract B (distance 4 finalized)

- Relax neighbors: C→4+1=5, E→4+5=9
- PQ: [(C,5), (D,9), (E,9)]

**Step 3:** Extract C (distance 5 finalized)

- Relax: E→min(9, 5+6=11)=9 (no change)
- PQ: [(D,9), (E,9)]

**Step 4:** Extract D (distance 9 finalized)

- Relax: C→min(5, 9+2=11)=5 (no change)
- PQ: [(E,9)]

**Step 5:** Extract E (distance 9 finalized)

Final distances from A: A=0, B=4, C=5, D=9, E=9

### Worked Example 2: Practical Application

In network routing, Dijkstra's Algorithm computes the optimal routing table. For a network of 5 routers (nodes A-E) with bandwidth-latency costs as edge weights, the algorithm determines the minimum-cost path from a source router to all others, enabling efficient packet forwarding.

### Pseudocode Implementation

```
DIJKSTRA(G, w, s):
 for each vertex v in G.V:
 dist[v] = ∞
 π[v] = NIL
 dist[s] = 0
 S = ∅
 Q = priority queue containing all vertices

 while Q ≠ ∅:
 u = EXTRACT-MIN(Q)
 S = S ∪ {u}
 for each vertex v in G.Adj[u]:
 if dist[u] + w(u,v) < dist[v]:
 dist[v] = dist[u] + w(u,v)
 π[v] = u
 DECREASE-KEY(Q, v, dist[v])

 return dist, π
```

## Exam Tips

1. **Algorithm Classification:** Remember Dijkstra's is a GREEDY algorithm, not dynamic programming, though both aim for optimality.

2. **Non-Negative Weights Requirement:** Always verify edge weights are non-negative before applying Dijkstra; state this assumption explicitly in solutions.

3. **Priority Queue Choice:** For exam questions, specify your data structure choice and justify the complexity analysis accordingly.

4. **Proof Understanding:** Be able to prove why the vertex with minimum tentative distance, when extracted, has its final distance determined.

5. **Edge Cases:** Handle disconnected graphs (vertices remain at ∞), single vertex graphs, and the source vertex case explicitly.

6. **Reconstruction of Paths:** Use the predecessor array π[] to reconstruct shortest paths by backtracking from destination to source.

7. **Comparison with Other Algorithms:** Know when to use Bellman-Ford (negative weights), Floyd-Warshall (all-pairs), or Dijkstra based on problem constraints.
