# Edge-Connectivity in Graph Theory

## Table of Contents

- [Edge-Connectivity in Graph Theory](#edge-connectivity-in-graph-theory)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Definitions](#basic-definitions)
  - [Important Properties](#important-properties)
  - [Bridges and Their Properties](#bridges-and-their-properties)
  - [Menger's Theorem (Edge Version)](#mengers-theorem-edge-version)
  - [Max-Flow Min-Cut Theorem](#max-flow-min-cut-theorem)
  - [Local Edge-Connectivity](#local-edge-connectivity)
  - [Edge-Connectivity and Network Reliability](#edge-connectivity-and-network-reliability)
- [Examples](#examples)
  - [Example 1: Finding Edge-Connectivity of a Cycle Graph](#example-1-finding-edge-connectivity-of-a-cycle-graph)
  - [Example 2: Edge-Connectivity of a Wheel Graph](#example-2-edge-connectivity-of-a-wheel-graph)
  - [Example 3: Using Max-Flow Min-Cut to Find Edge-Connectivity](#example-3-using-max-flow-min-cut-to-find-edge-connectivity)
- [Exam Tips](#exam-tips)

## Introduction

Edge-connectivity is a fundamental concept in graph theory that measures the resilience of a graph against edge failures. While vertex connectivity deals with the removal of vertices, edge-connectivity focuses on how many edges must be removed to disconnect a graph. This concept is crucial in network design, telecommunications, transportation systems, and reliability engineering. In real-world applications, understanding edge-connectivity helps engineers design robust networks that can withstand link failures without complete system breakdown.

The study of edge-connectivity connects deeply with many important theorems in graph theory, including Menger's Theorem and the Max-Flow Min-Cut Theorem. These connections make it a pivotal topic in both theoretical and applied graph theory. For computer science students, edge-connectivity concepts are essential for understanding network reliability algorithms, distributed systems, and data structures.

## Key Concepts

### Basic Definitions

**Edge Cut:** An edge cut in a graph G is a set of edges whose removal disconnects the graph. More formally, a set S ⊆ E(G) is an edge cut if G - S (the graph obtained by removing edges in S) is disconnected. The simplest edge cuts are bridges—individual edges whose removal disconnects the graph.

**Edge-Connectivity (λ(G)):** The edge-connectivity of a graph G, denoted λ(G), is the minimum number of edges whose removal disconnects the graph. It represents the "strength" of the graph's connectivity. Formally:

λ(G) = min{|S| : S ⊆ E(G) and G - S is disconnected}

**Minimum Edge Cut:** A minimum edge cut is an edge cut with the smallest possible cardinality. The size of a minimum edge cut equals λ(G).

**k-edge-connected Graph:** A graph is k-edge-connected if its edge-connectivity is at least k. That is, λ(G) ≥ k. A 1-edge-connected graph is simply a connected graph, while a 2-edge-connected graph cannot be disconnected by removing a single edge.

### Important Properties

**Relationship with Vertex Connectivity:** For any simple graph G with n vertices, we have:
κ(G) ≤ λ(G) ≤ δ(G)

Where κ(G) is the vertex-connectivity and δ(G) is the minimum degree of G. This inequality shows that edge-connectivity is bounded between vertex-connectivity and minimum degree.

**Edge-Connectivity of Complete Graphs:** For a complete graph Kₙ with n vertices:
λ(Kₙ) = n - 1

This is because removing all (n-1) edges incident to any vertex disconnects the graph.

**Edge-Connectivity of Complete Bipartite Graphs:** For Kₘ,ₙ (where m, n ≥ 2):
λ(Kₘ,ₙ) = min(m, n)

This follows from the fact that removing all edges incident to all vertices on the smaller partition side disconnects the graph.

### Bridges and Their Properties

An edge e in a graph G is called a **bridge** (or cut-edge) if its removal increases the number of connected components. Bridges are edges with λ(G) = 1. A graph with no bridges is called **2-edge-connected**.

**Theorem:** An edge e is a bridge in G if and only if e does not lie on any cycle of G.

This theorem provides a practical way to identify bridges—by checking whether an edge belongs to any cycle.

### Menger's Theorem (Edge Version)

Menger's Theorem is one of the most fundamental results in graph connectivity. The edge-version states:

**Edge Menger's Theorem:** For any two non-adjacent vertices s and t in a graph G, the minimum number of edges whose removal disconnects s from t equals the maximum number of edge-disjoint s-t paths.

This theorem has profound implications for network reliability and is closely related to the Max-Flow Min-Cut Theorem.

### Max-Flow Min-Cut Theorem

The Max-Flow Min-Cut Theorem is essentially a special case of Menger's Theorem applied to flow networks:

**Theorem:** In any flow network, the maximum value of a flow from source s to sink t equals the minimum capacity of an s-t cut.

This theorem provides an algorithmic approach to computing edge-connectivity. By constructing a flow network where each edge has unit capacity, the maximum flow equals the edge-connectivity between the source and sink.

### Local Edge-Connectivity

For specific vertex pairs, we define **local edge-connectivity** λ(s, t) as the minimum number of edges whose removal disconnects s from t. For any graph:

λ(G) = min{λ(s, t) : s, t ∈ V(G), s ≠ t}

### Edge-Connectivity and Network Reliability

In practical applications, edge-connectivity helps measure network reliability:

- **Telecommunication Networks:** Higher edge-connectivity means more redundant paths between nodes
- **Transportation Networks:** Edge-connectivity indicates robustness against route closures
- **Power Grids:** Edge-connectivity helps assess vulnerability to transmission line failures

## Examples

### Example 1: Finding Edge-Connectivity of a Cycle Graph

Consider the cycle graph C₆ (6 vertices):

**Solution:**
Step 1: Identify minimum degree: δ(C₆) = 2

Step 2: Check if any edge is a bridge:

- In a cycle, every edge lies on a cycle
- Therefore, no edge is a bridge

Step 3: Determine minimum edge cut:

- Removing 1 edge: Graph remains connected (becomes a path)
- Removing 2 edges: Graph becomes disconnected
- Therefore, λ(C₆) = 2

**Verification:** Using the property λ(G) ≤ δ(G), we have λ(C₆) ≤ 2. Since C₆ is not a tree, λ(C₆) ≥ 2. Hence λ(C₆) = 2.

### Example 2: Edge-Connectivity of a Wheel Graph

Consider the wheel graph W₆ (6 vertices: one hub + 5 rim vertices):

**Solution:**
Step 1: Identify structure:

- One central vertex connected to all rim vertices
- Rim vertices form a cycle C₅

Step 2: Find minimum degree:

- Hub has degree 5 (connected to all rim vertices)
- Each rim vertex has degree 3 (2 rim neighbors + hub)
- Therefore, δ(W₆) = 3

Step 3: Find minimum edge cut:

- Remove all 5 edges incident to hub: This disconnects all rim vertices from hub
- Graph becomes disconnected
- So λ(W₆) ≤ 5

Step 4: Check smaller cuts:

- Can we disconnect with fewer than 5 edges?
- If we remove 4 edges from hub, at least one rim vertex still connects to hub
- Cannot disconnect with fewer than 5 edges
- Therefore, λ(W₆) = 5

### Example 3: Using Max-Flow Min-Cut to Find Edge-Connectivity

Find edge-connectivity between vertices a and d in the following graph:

```
 b
 /|\
 1 | 1
 / | \
a---+---c
|\ | /|
| 1 | 1 |
d---+---e
```

**Solution:**
Step 1: Assign unit capacity to all edges

Step 2: Find maximum flow from a to d:

**Path 1:** a-b-c-d (using edges a-b, b-c, c-d): Flow = 1
**Path 2:** a-c-e-d (using edges a-c, c-e, e-d): Flow = 1
**Path 3:** a-b-d (using edges a-b, b-d): Flow = 0 (a-b already used)

Maximum flow = 2

Step 3: By Max-Flow Min-Cut, minimum cut also equals 2

Step 4: Verify by identifying cut:

- Cut separating {a, b, c} from {d, e} has edges: b-d and c-d = 2 edges
- λ(a, d) = 2

## Exam Tips

1. **Remember the inequality chain:** κ(G) ≤ λ(G) ≤ δ(G) — this is frequently tested in university exams.

2. **Bridge identification shortcut:** An edge is a bridge if and only if it does not belong to any cycle. Use this to quickly identify when λ(G) = 1.

3. **Complete graph edge-connectivity:** λ(Kₙ) = n - 1 — this is a standard result that appears in many problems.

4. **Complete bipartite graph:** λ(Kₘ,ₙ) = min(m, n) — remember to identify the smaller partition.

5. **Application of Max-Flow Min-Cut:** For computing edge-connectivity between specific vertices, construct a flow network with unit capacities and find the maximum flow.

6. **Cycle graphs:** For any cycle Cₙ (n ≥ 3), λ(Cₙ) = 2 — cycles have no bridges.

7. **Tree graphs:** For any tree with n vertices, λ(T) = 1 — trees have no cycles, so every edge is a bridge.

8. **Difference from vertex connectivity:** Remember that edge-connectivity is always at least vertex-connectivity, and they are equal for many common graph families.
