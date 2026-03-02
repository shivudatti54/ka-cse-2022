# Topological Sorting

## Table of Contents

- [Topological Sorting](#topological-sorting)
- [Introduction](#introduction)
- [Theoretical Foundations](#theoretical-foundations)
  - [Directed Acyclic Graph (DAG)](#directed-acyclic-graph-dag)
  - [Topological Order](#topological-order)
  - [Indegree and Outdegree](#indegree-and-outdegree)
  - [Theorem: Characterization of Topological Sortability](#theorem-characterization-of-topological-sortability)
- [Algorithms for Topological Sorting](#algorithms-for-topological-sorting)
  - [Kahn's Algorithm (BFS-based)](#kahns-algorithm-bfs-based)
  - [DFS-based Topological Sort](#dfs-based-topological-sort)
- [Worked Examples](#worked-examples)
  - [Example 1: Applying Kahn's Algorithm](#example-1-applying-kahns-algorithm)
  - [Example 2: Applying DFS-based Algorithm](#example-2-applying-dfs-based-algorithm)
  - [Example 3: Detecting Cycles](#example-3-detecting-cycles)
- [Summary](#summary)

## Introduction

Topological sorting is a fundamental graph algorithm that arranges the vertices of a directed acyclic graph (DAG) in a linear order such that for every directed edge (u, v), vertex u appears before vertex v in the ordering. This ordering is called a **topological order** or **topological ordering**. The problem has significant practical importance in scenarios where tasks have precedence constraints—certain tasks must be completed before others can commence.

In computer science and operations research, topological sorting addresses the fundamental problem of finding a valid execution sequence when activities have directed dependencies. The algorithm ensures that all prerequisite relationships are satisfied, making it indispensable in various applications including build systems (determining compilation order), task scheduling in project management, resolving package dependencies in package managers, course prerequisite planning in academic systems, and instruction scheduling in compilers.

A fundamental property governing topological sorting is that a topological ordering exists **if and only if** the directed graph is acyclic (contains no cycles). This equivalence is formally stated: a directed graph G has a topological ordering if and only if G is a Directed Acyclic Graph (DAG). The proof of this theorem is presented in the subsequent sections.

## Theoretical Foundations

### Directed Acyclic Graph (DAG)

A **directed acyclic graph (DAG)** is a directed graph that contains no directed cycles. Formally, a graph G = (V, E) is a DAG if there exists no sequence of vertices v₁, v₂, ..., vₖ (where k ≥ 1) such that there are directed edges (v₁, v₂), (v₂, v₃), ..., (vₖ₋₁, vₖ), and additionally (vₖ, v₁) exists in E. The absence of directed cycles is both necessary and sufficient for topological sorting to be possible.

**Lemma 1**: Every DAG has at least one vertex with indegree zero (a source) and at least one vertex with outdegree zero (a sink).

_Proof_: Assume a DAG G has no vertex with indegree zero. Then start from any vertex and follow incoming edges backward. Since the graph is finite and acyclic, this process must eventually terminate at a vertex with no incoming edges—a contradiction. The sink argument follows symmetrically by considering outgoing edges. ∎

### Topological Order

A **topological order** (or topological ordering) of a DAG G = (V, E) is a linear ordering of all vertices in V such that for every directed edge (u, v) ∈ E, u precedes v in the ordering. A DAG may have multiple valid topological orderings; in fact, the number of topological orderings can be exponential in the number of vertices for certain DAG structures.

### Indegree and Outdegree

For a vertex v in a directed graph:

- **Indegree** (deg⁻(v)): the number of edges entering v, denoted |{u ∈ V : (u, v) ∈ E}|
- **Outdegree** (deg⁺(v)): the number of edges leaving v, denoted |{w ∈ V : (v, w) ∈ E}|

In Kahn's algorithm, vertices with indegree zero serve as initial sources—tasks with no prerequisites.

### Theorem: Characterization of Topological Sortability

**Theorem**: A directed graph G has a topological ordering if and only if G is acyclic.

_Proof (necessity)_: Suppose G has a topological ordering. If G contained a directed cycle v₁ → v₂ → ... → vₖ → v₁, then by the definition of topological ordering, v₁ must precede v₂, v₂ must precede v₃, ..., vₖ must precede v₁. This implies v₁ ≺ v₁, a contradiction. Hence G must be acyclic.

_Proof (sufficiency)_: If G is acyclic (a DAG), Lemma 1 guarantees the existence of a source vertex (indegree zero). Remove this vertex and its outgoing edges to obtain G'. By induction on |V|, G' has a topological ordering. Prepending the removed source vertex to this ordering yields a topological ordering for G. ∎

## Algorithms for Topological Sorting

### Kahn's Algorithm (BFS-based)

Kahn's algorithm employs a modified breadth-first search (BFS) approach using a queue. The algorithm leverages the observation that vertices with indegree zero can be placed first in any topological order.

**Algorithm (Pseudocode)**:

```
TOPOLOGICAL-SORT-KAHN(G):
 1. Compute indegree[v] for each vertex v ∈ G.V
 2. Initialize queue Q with all vertices having indegree = 0
 3. Initialize empty list result
 4. while Q is not empty:
 5. u ← Q.dequeue()
 6. append u to result
 7. for each vertex v ∈ G.Adj[u]:
 8. indegree[v] ← indegree[v] - 1
 9. if indegree[v] == 0:
 10. Q.enqueue(v)
 11. if |result| ≠ |G.V|:
 12. return ERROR: Graph contains a cycle
 13. return result
```

**Time Complexity Analysis**: Computing indegrees requires O(V + E) time (visiting all vertices and edges). The while loop processes each vertex exactly once and examines each edge exactly once during indegree decrementation. Therefore, total time complexity is **O(V + E)**.

**Space Complexity Analysis**: The algorithm stores:

- Indegree array: O(V)
- Queue: O(V) in worst case
- Result list: O(V)
  Thus, space complexity is **O(V)**.

**Correctness Proof**: We prove that Kahn's algorithm returns a topological ordering when the graph is a DAG. The algorithm maintains the invariant that every vertex enqueued has indegree zero with respect to the remaining unprocessed vertices. When a vertex u is dequeued and added to result, all its outgoing edges are removed, ensuring that no vertex appearing after u in result has an incoming edge from a later vertex. If the algorithm processes all vertices (|result| = |V|), the ordering satisfies the topological property. Conversely, if a cycle exists, eventually all remaining vertices have indegree ≥ 1, the queue empties prematurely, and |result| < |V|.

### DFS-based Topological Sort

The depth-first search (DFS) based approach exploits the recursive nature of DFS traversal. The key insight is that vertices are added to the result when their exploration completes—after all descendants have been processed.

**Algorithm (Pseudocode)**:

```
TOPOLOGICAL-SORT-DFS(G):
 1. Initialize visited[v] = false for all v ∈ G.V
 2. Initialize empty list result
 3. for each vertex v ∈ G.V:
 4. if not visited[v]:
 5. DFS(v)
 6. reverse result
 7. return result

DFS(u):
 1. visited[u] ← true
 2. for each v ∈ G.Adj[u]:
 3. if not visited[v]:
 4. DFS(v)
 5. append u to result // Post-order: after all descendants processed
```

**Time Complexity Analysis**: The DFS procedure visits each vertex once and examines each edge once. The final reversal operation costs O(V). Hence, total time complexity is **O(V + E)**.

**Space Complexity Analysis**:

- Visited array: O(V)
- Result list: O(V)
- Recursion stack: O(V) in worst case
  Total space complexity is **O(V)**.

**Cycle Detection**: During DFS, if we encounter a vertex currently in the recursion stack (visiting state), a cycle exists. This is detected by maintaining three color states: white (unvisited), gray (visiting), and black (fully processed).

## Worked Examples

### Example 1: Applying Kahn's Algorithm

Consider a DAG with vertices V = {1, 2, 3, 4, 5} and edges E = {(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)}.

**Step 1: Compute indegrees**

- indegree(1) = 0
- indegree(2) = 1 (from 1)
- indegree(3) = 1 (from 1)
- indegree(4) = 2 (from 2, 3)
- indegree(5) = 1 (from 4)

**Step 2: Initialize queue Q = {1}** (vertices with indegree 0)

**Step 3-7: Process vertices**

- Dequeue 1: result = [1]; remove (1,2) → indegree(2)=0 → enqueue 2; remove (1,3) → indegree(3)=0 → enqueue 3; Q = {2, 3}
- Dequeue 2: result = [1, 2]; remove (2,4) → indegree(4)=1; Q = {3}
- Dequeue 3: result = [1, 2, 3]; remove (3,4) → indegree(4)=0 → enqueue 4; Q = {4}
- Dequeue 4: result = [1, 2, 3, 4]; remove (4,5) → indegree(5)=0 → enqueue 5; Q = {5}
- Dequeue 5: result = [1, 2, 3, 4, 5]

**Final Topological Order**: 1 → 2 → 3 → 4 → 5

### Example 2: Applying DFS-based Algorithm

Using the same graph:

**DFS Traversal**:

- DFS(1): visit 1 → DFS(2) → DFS(4) → DFS(5): no unvisited neighbors → add 5 to result → backtrack → add 4 → backtrack to 2 → add 2
- Return to 1 → DFS(3) → DFS(4) already visited → add 3
- Add 1

**Intermediate result**: [5, 4, 2, 3, 1]
**After reversal**: [1, 3, 2, 4, 5]

This is also a valid topological ordering, demonstrating that multiple valid orderings exist.

### Example 3: Detecting Cycles

If edges included (5, 1), forming a cycle 1→2→4→5→1:

- Kahn's algorithm would process vertices until Q becomes empty with |result| < |V|, signaling cycle detection
- DFS-based approach would encounter vertex 1 in recursion stack during traversal, indicating a cycle

---

## Summary

Topological sorting arranges vertices of a DAG such that all directed edges point forward in the ordering. This is possible if and only if the graph is acyclic. Two primary algorithms exist:

1. **Kahn's Algorithm (BFS-based)**: Uses indegree tracking with a queue; O(V + E) time and O(V) space; naturally detects cycles when queue empties prematurely.

2. **DFS-based Algorithm**: Exploits post-order traversal with reversal; O(V + E) time and O(V) space; detects cycles through recursion stack examination.

Both algorithms have identical asymptotic complexities, differing in approach: Kahn's is iterative and builds the order forward, while DFS-based is recursive and constructs the order backward. The choice depends on implementation preferences and specific requirements such as cycle detection methodology.
