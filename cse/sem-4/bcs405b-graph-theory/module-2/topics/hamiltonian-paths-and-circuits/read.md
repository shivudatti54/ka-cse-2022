# Hamiltonian Paths and Circuits

## Table of Contents

- [Hamiltonian Paths and Circuits](#hamiltonian-paths-and-circuits)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definitions](#definitions)
  - [Necessary Conditions](#necessary-conditions)
  - [Important Theorems](#important-theorems)
  - [Characterization](#characterization)
  - [Differences: Eulerian vs Hamiltonian](#differences-eulerian-vs-hamiltonian)
  - [Complete Graphs](#complete-graphs)
- [Examples](#examples)
  - [Example 1: Identifying Hamiltonian Path in a Graph](#example-1-identifying-hamiltonian-path-in-a-graph)
  - [Example 2: Verifying Dirac's Theorem Application](#example-2-verifying-diracs-theorem-application)
  - [Example 3: Finding Hamiltonian Circuit in K₅](#example-3-finding-hamiltonian-circuit-in-k)
- [Exam Tips](#exam-tips)

## Introduction

Hamiltonian paths and circuits are fundamental concepts in graph theory named after the Irish mathematician William Rowan Hamilton, who first introduced this problem in 1857. While similar in name to Eulerian paths and circuits, they address a fundamentally different problem: instead of traversing each edge exactly once, a Hamiltonian path visits each vertex exactly once, and a Hamiltonian circuit returns to the starting vertex after visiting all other vertices exactly once.

This topic holds significant importance in computer science and operations research due to its wide range of practical applications. The Traveling Salesman Problem (TSP), one of the most famous optimization problems, is directly related to finding Hamiltonian circuits. Additionally, these concepts find applications in route planning, DNA sequencing, network routing, and various scheduling problems. Understanding Hamiltonian paths and circuits is essential for solving complex optimization problems and forms a crucial part of the CSE curriculum.

Unlike Eulerian paths which can be efficiently determined using Fleury's algorithm or Hierholzer's algorithm, the Hamiltonian path and circuit problems belong to a class of problems known as NP-complete problems. This means there is no known polynomial-time algorithm to solve these problems for arbitrary graphs, making them computationally challenging and theoretically significant.

## Key Concepts

### Definitions

**Hamiltonian Path**: A Hamiltonian path in a graph is a path that visits each vertex exactly once. If a graph contains a Hamiltonian path, it is called a traceable graph. The path does not need to return to the starting vertex.

**Hamiltonian Circuit (or Hamiltonian Cycle)**: A Hamiltonian circuit is a cycle that visits each vertex exactly once and returns to the starting vertex. A graph containing a Hamiltonian circuit is called a Hamiltonian graph. The circuit has n vertices for a graph with n vertices, with each vertex appearing exactly once (except the starting/ending vertex which appears twice).

**Key Distinction**: The Hamiltonian circuit has n edges (one for each transition between vertices), while Eulerian circuits have exactly m edges where m is the total number of edges in the graph.

### Necessary Conditions

1. **Connectivity**: A graph with a Hamiltonian path must be connected. However, connectivity is necessary but not sufficient.

2. **Degree Condition**: If a vertex has degree 1 in a graph, it cannot be part of a Hamiltonian path (except as an endpoint). Similarly, if a vertex has degree 0, the graph cannot have a Hamiltonian path.

3. **Number of Edges**: A Hamiltonian circuit requires at least n edges for a graph with n vertices (where n ≥ 3). In fact, a Hamiltonian graph with n vertices must have at least n edges.

### Important Theorems

**Dirac's Theorem (1952)**: If a simple graph with n vertices (where n ≥ 3) has minimum degree δ(G) ≥ n/2, then the graph is Hamiltonian. This is a sufficient condition.

_Example_: For a graph with 6 vertices, if every vertex has degree at least 3, Dirac's theorem guarantees the graph is Hamiltonian.

**Ore's Theorem (1960)**: If for every pair of non-adjacent vertices u and v in a simple graph with n vertices (n ≥ 3), deg(u) + deg(v) ≥ n, then the graph is Hamiltonian. This is also a sufficient condition and is more general than Dirac's theorem.

**Corollary**: Dirac's theorem is a special case of Ore's theorem since δ(G) ≥ n/2 implies deg(u) + deg(v) ≥ n for all pairs.

### Characterization

**Chvátal-Erdős Theorem**: A graph is Hamiltonian if it has sufficient independence number and connectivity. Specifically, if a graph G has no induced subgraph on k + 1 vertices that is a complete graph missing a matching, and if κ(G) ≥ k, then G is Hamiltonian.

**Tait's Conjecture**: For 3-regular, 3-connected planar graphs, the conjecture that every such graph has a Hamiltonian cycle. This was disproved by Tutte in 1946 with a counterexample.

### Differences: Eulerian vs Hamiltonian

| Aspect              | Eulerian               | Hamiltonian                     |
| ------------------- | ---------------------- | ------------------------------- |
| Traverses           | Each edge exactly once | Each vertex exactly once        |
| Problem Type        | P (polynomial time)    | NP-complete                     |
| Existence Condition | Simple degree criteria | No simple sufficient condition  |
| Known Algorithm     | Fleury's, Hierholzer's | Exhaustive search (exponential) |

### Complete Graphs

The complete graph Kₙ (n vertices where every pair is connected) is always Hamiltonian. Kₙ contains (n-1)! distinct Hamiltonian circuits, as we can arrange all n vertices in a cycle in (n-1)! ways (accounting for rotation equivalence).

## Examples

### Example 1: Identifying Hamiltonian Path in a Graph

Consider a graph with vertices {A, B, C, D, E} and edges: AB, AC, AD, BC, BD, BE, CD, DE.

**Solution**:

- Start at vertex A
- A → B (using edge AB)
- B → D (using edge BD)
- D → C (using edge CD)
- C → E cannot use edge CE (doesn't exist)

Let's try another path: A → C → D → B → E

- A → C (edge AC exists)
- C → D (edge CD exists)
- D → B (edge DB exists)
- B → E (edge BE exists)

This visits all vertices exactly once: A, C, D, B, E
Therefore, A-C-D-B-E is a Hamiltonian path.

### Example 2: Verifying Dirac's Theorem Application

Consider a graph with 8 vertices where minimum degree is 4. Determine if the graph is guaranteed to be Hamiltonian.

**Solution**:

- Number of vertices: n = 8
- Minimum degree: δ(G) = 4
- Check Dirac's condition: δ(G) ≥ n/2 → 4 ≥ 8/2 → 4 ≥ 4

Since the condition is satisfied (4 ≥ 4), Dirac's theorem guarantees that this graph is Hamiltonian. The theorem ensures existence but doesn't provide a method to find the specific Hamiltonian circuit.

### Example 3: Finding Hamiltonian Circuit in K₅

Find all Hamiltonian circuits in K₅ starting from vertex A (considering circuits that differ only in direction as the same).

**Solution**:
K₅ has 5 vertices: A, B, C, D, E

Since we fix the starting vertex A, and consider direction-equivalent circuits as the same:
Number of circuits = (n-1)!/2 = (5-1)!/2 = 24/2 = 12

One example circuit: A → B → C → D → E → A
Let's verify: All edges exist (complete graph), all vertices visited exactly once, returns to A.

Another circuit: A → E → D → C → B → A

## Exam Tips

1. **Memorize Dirac's and Ore's theorems precisely**: These are frequently asked in university exams. Remember Dirac requires δ(G) ≥ n/2, while Ore requires deg(u) + deg(v) ≥ n for all non-adjacent pairs.

2. **Understand the difference between necessary and sufficient conditions**: Dirac's and Ore's theorems provide sufficient conditions, not necessary ones. A graph may be Hamiltonian even if these conditions aren't met.

3. **Remember that complete graphs are always Hamiltonian**: Kₙ has (n-1)!/2 distinct Hamiltonian circuits - a common calculation question.

4. **Know the time complexity difference**: Eulerian problems are polynomial-time solvable while Hamiltonian problems are NP-complete. This distinction is often tested.

5. **Apply degree sum arguments**: When proving non-Hamiltonian nature, use degree sum arguments and Posa's rotation technique concepts for constructive proofs.

6. **Distinguish between path and circuit**: A Hamiltonian path need not return to start, while a Hamiltonian circuit must form a cycle returning to the starting vertex.

7. **Practice identifying Hamiltonian paths**: Given an adjacency matrix or graph diagram, be able to trace a Hamiltonian path by inspection.

8. **Understand the practical application**: The Traveling Salesman Problem is essentially finding the minimum weight Hamiltonian circuit - know this connection.

9. **Remember minimum edge requirement**: A Hamiltonian circuit in an n-vertex graph requires at least n edges.

10. **Know the historical context**: Hamilton's Icosian Game - this historical context is sometimes asked in exams.
