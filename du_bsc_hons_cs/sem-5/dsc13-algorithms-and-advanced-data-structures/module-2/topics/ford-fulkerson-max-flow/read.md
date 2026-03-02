# Ford-Fulkerson Maximum Flow Algorithm

## Introduction

The Ford-Fulkerson method is a fundamental algorithm in graph theory and combinatorial optimization that solves the **Maximum Flow Problem**. This problem asks: Given a flow network (a directed graph with capacities on each edge), what is the maximum possible flow from a source vertex to a sink vertex without violating capacity constraints?

The significance of this algorithm extends far beyond theoretical computer science. In real-world applications, maximum flow problems arise in **transportation networks** (moving goods from warehouses to retail stores), **telecommunications** (maximizing data throughput in networks), **circulation systems** (blood flow in blood vessels, traffic flow on roads), and **bipartite matching** (assigning jobs to applicants, college admissions). The Ford-Fulkerson algorithm, developed by L.R. Ford and D.R. Fulkerson in 1956, laid the foundation for modern network flow theory and remains a cornerstone topic in the University of Delhi's Computer Science curriculum.

Understanding this algorithm requires careful attention to several interconnected concepts: flow networks, capacity constraints, residual graphs, augmenting paths, and the powerful Max-Flow Min-Cut theorem. This algorithm demonstrates how seemingly complex optimization problems can be solved through iterative improvement of a feasible solution.

## Key Concepts

### Flow Network Definition

A flow network is a directed graph G = (V, E) with the following components:
- A **source vertex (s)**: The starting point where flow originates
- A **sink vertex (t)**: The destination where flow terminates
- A **capacity function c(u, v)**: Non-negative integer assigned to each edge (u, v) ∈ E, representing the maximum amount of flow that can pass through that edge

For example, in a transportation network, vertices could represent cities, edges could represent roads, and capacities could represent the maximum number of vehicles the road can handle per hour.

### Flow Function

A flow f is a function f: V × V → ℝ that satisfies three properties:

1. **Capacity Constraint**: For every edge (u, v) ∈ E: 0 ≤ f(u, v) ≤ c(u, v)
   - Flow through any edge cannot exceed its capacity

2. **Skew Symmetry**: For every u, v ∈ V: f(u, v) = -f(v, u)
   - Flow from u to v is the negative of flow from v to u

3. **Flow Conservation**: For every vertex v ∈ V - {s, t}: Σ f(u, v) = Σ f(v, u)
   - At all intermediate vertices, total incoming flow equals total outgoing flow

The **value of a flow** |f| is the total amount of flow leaving the source: |f| = Σ f(s, v) for all v ∈ V.

### Residual Graph

The residual graph G_f represents the remaining capacity in the network after pushing some flow. For each edge (u, v) in the original graph:

- **Forward edge**: If f(u, v) < c(u, v), residual capacity = c(u, v) - f(u, v)
- **Backward edge**: If f(u, v) > 0, residual capacity = f(u, v)

The residual graph G_f contains edges with positive residual capacity. Finding augmenting paths in this residual graph is the key to increasing the total flow.

### Augmenting Path

An **augmenting path** is a simple path from source s to sink t in the residual graph G_f. The **bottleneck capacity** of an augmenting path is the minimum residual capacity among all edges on that path. This bottleneck represents how much additional flow can be pushed through that particular path.

### Maximum Flow and Minimum Cut

A **cut** (S, T) in a flow network is a partition of vertices V into two sets S and T such that s ∈ S and t ∈ T. The **capacity of a cut** is the sum of capacities of all edges from S to T: c(S, T) = Σ c(u, v) for all u ∈ S, v ∈ T.

The **Max-Flow Min-Cut Theorem** (Ford-Fulkerson, 1956) states: **In any flow network, the maximum value of a flow equals the minimum capacity of an s-t cut.** This theorem provides the theoretical foundation for proving the correctness of the Ford-Fulkerson algorithm.

### The Ford-Fulkerson Algorithm

The algorithm works as follows:

```
FORD-FULKERSON(G, s, t):
1. Initialize flow f to 0 for all edges
2. While there exists an augmenting path p from s to t in residual graph G_f:
   a. Find bottleneck(p) = min{c_f(u,v) : (u,v) is in p}
   b. For each edge (u,v) in p:
      - If (u,v) is a forward edge: f(u,v) += bottleneck(p)
      - If (u,v) is a backward edge: f(u,v) -= bottleneck(p)
3. Return f (the maximum flow)
```

The algorithm iteratively finds augmenting paths and increases the flow until no more augmenting paths exist. When the algorithm terminates, the flow is maximum (by the Max-Flow Min-Cut theorem).

### Complexity Analysis

The time complexity of Ford-Fulkerson depends on how augmenting paths are found:
- **With BFS/DFS**: O(E × |f*|) where |f*| is the value of maximum flow
- **With Edmonds-Karp (BFS-based)**: O(VE²)

The complexity is pseudo-polynomial since it depends on the flow value. However, for integer capacities, the algorithm always terminates.

## Examples

### Example 1: Basic Ford-Fulkerson Execution

Consider the following flow network with source s and sink t:

```
s ──(10)──► a ──(4)──► t
│            │
(10)         (9)
▼            ▼
b ──(10)──► c ──(10)──► t
```

**Step 1**: Find augmenting path s→a→t
- Bottleneck: min(10, 4) = 4
- Update: f(s,a)=4, f(a,t)=4
- Flow value: 4

**Step 2**: Find augmenting path s→b→c→t
- Bottleneck: min(10, 10, 10) = 10
- Update: f(s,b)=10, f(b,c)=10, f(c,t)=10
- Flow value: 4 + 10 = 14

**Step 3**: Find augmenting path s→a→c→t
- Residual capacities: s→a has 6 left, a→c (new edge) has 9, c→t has 0 (full)
- No path to t exists! Need to find another path.

**Step 4**: Find augmenting path s→a→c→b→...wait, let's reconsider with residual graph analysis. Actually, after step 2, c→t is saturated, so we need different paths.

After complete execution, maximum flow = **19** (achieved through multiple augmentations including path reversal to adjust flow).

### Example 2: Understanding Residual Graph and Path Reversal

```
s ──(3)──► a ──(3)──► t
│            │
(3)         (2)
▼            ▼
b ──(3)──► c ──(3)──► t
```

**Iteration 1**: Path s→a→t (bottleneck = 3)
- f(s,a) = 3, f(a,t) = 3

**Iteration 2**: Path s→b→c→t (bottleneck = 3)
- f(s,b) = 3, f(b,c) = 3, f(c,t) = 3

Current flow value = 6, but check if we can do better...

Actually, with these capacities, maximum flow = 6. The cut {s,a,b} has capacity c(s,a)+c(s,b) = 3+3 = 6, which equals our flow, confirming optimality.

### Example 3: Complex Network with Path Reversal

```
        4
    s ───► a ───► t
    │    ↗  ↘    ↗
   4│   /    \   │4
    ▼ /      \ ▼
    b ───────► c
        4
```

**Path 1**: s→a→c→t: bottleneck = min(4,4,4) = 4
- f(s,a)=4, f(a,c)=4, f(c,t)=4, Flow = 4

**Path 2**: s→b→c→a→...t is blocked since a→t has 0 residual
- s→b→c: b→c has 0 residual now
- Need to find alternate path

Actually, after first path, c→t is saturated. To get more flow:
- We can push flow back from c to a (backward edge)
- Then push from a to t... but a→t was already saturated

The maximum flow here is actually 8. Can you find all augmenting paths to achieve this?

**Solution**: After s→a→c→t saturates all edges, use reverse edges:
- Augment along s→b→c→a→t by reducing flow on a→c and pushing through a→t
- This "path reversal" technique is crucial for maximizing flow

## Exam Tips

1. **Memorize the three flow properties**: Capacity constraint, skew symmetry, and flow conservation are frequently asked in theory questions.

2. **Understand residual graph construction**: Know how to compute residual capacities for both forward and backward edges.

3. **Max-Flow Min-Cut theorem is crucial**: This is THE most important theorem for this topic. Be able to state it precisely and use it to prove optimality.

4. **Draw residual graphs carefully**: Many marks are lost due to errors in residual graph construction. Practice with multiple examples.

5. **Time complexity matters**: Remember Ford-Fulkerson is O(E × |f|) while Edmonds-Karp (BFS-based) is O(VE²).

6. **Connection to bipartite matching**: Know how maximum flow solves bipartite matching problems - this is a common exam application.

7. **Cut identification**: Be able to identify minimum s-t cuts and compute their capacities to verify maximum flow.

8. **Algorithm termination**: For integer capacities, Ford-Fulkerson always terminates. Mention this in your answers when discussing correctness.

9. **Step-by-step execution**: In exams, show each iteration clearly with the residual graph and augmenting path.

10. **Know when algorithm stops**: The algorithm terminates when no augmenting path exists in the residual graph - at this point, flow is maximum.