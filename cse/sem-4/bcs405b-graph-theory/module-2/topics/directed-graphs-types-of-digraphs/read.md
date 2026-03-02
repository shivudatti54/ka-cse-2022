# Directed Graphs - Types of Digraphs

## Table of Contents

- [Directed Graphs - Types of Digraphs](#directed-graphs---types-of-digraphs)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Definition of Digraph](#basic-definition-of-digraph)
  - [Types of Digraphs](#types-of-digraphs)
  - [Operations on Digraphs](#operations-on-digraphs)
  - [Indegree and Outdegree](#indegree-and-outdegree)
- [Examples](#examples)
  - [Example 1: Identifying Types of Digraphs](#example-1-identifying-types-of-digraphs)
  - [Example 2: Finding Shortest Path in DAG using Topological Sort](#example-2-finding-shortest-path-in-dag-using-topological-sort)
  - [Example 3: Proving a Property of Tournaments](#example-3-proving-a-property-of-tournaments)
- [Exam Tips](#exam-tips)

## Introduction

Directed graphs, commonly known as digraphs, are fundamental structures in graph theory where edges have a specific direction. Unlike undirected graphs where edges connect vertices without any orientation, directed graphs assign a precise direction to each edge, making them essential for modeling asymmetric relationships in various real-world applications. In computer science, digraphs are extensively used to represent dependencies in project scheduling, control flow in programs, web page linkages, transportation networks with one-way routes, and database relationships.

The study of directed graphs forms a crucial part of the the syllabus for Graph Theory (BCS405B), and understanding their properties, types, and operations is essential for solving complex problems in algorithms, data structures, and discrete mathematics. This module explores the classification of digraphs into various types based on their structural properties, connectivity patterns, and edge configurations.

## Key Concepts

### Basic Definition of Digraph

A directed graph (digraph) G = (V, E) consists of a finite set V of vertices (or nodes) and a finite set E of directed edges (or arcs). Each directed edge is an ordered pair of vertices (u, v) where u is called the tail and v is called the head of the edge. We denote a directed edge from u to v as uv or (u → v). The direction indicates that we can travel from u to v but not necessarily in the reverse direction.

For example, consider a digraph G = (V, E) where V = {v1, v2, v3, v4} and E = {(v1, v2), (v2, v3), (v3, v1), (v2, v4)}. This digraph has 4 vertices and 4 directed edges.

### Types of Digraphs

#### 1. Simple Digraph

A simple digraph (or strict digraph) is a digraph that has no loops and no multiple directed edges between the same pair of vertices. In other words, it contains at most one directed edge from one vertex to another.

**Example:** G = (V, E) where V = {a, b, c} and E = {(a, b), (b, c), (c, a)} is a simple digraph. However, if we add another edge (a, b), it becomes a multigraph, not a simple digraph.

#### 2. Complete Digraph

A complete digraph (or tournament of order n) is a directed graph in which every pair of distinct vertices is connected by a pair of opposite directed edges—that is, both (u, v) and (v, u) exist for all u ≠ v.

For a complete digraph with n vertices, the number of edges is n(n-1). This is because each of the n vertices has directed edges to all other (n-1) vertices.

**Example:** A complete digraph with 3 vertices has edges: (v1, v2), (v2, v1), (v2, v3), (v3, v2), (v1, v3), (v3, v1)—totaling 6 edges.

#### 3. Complete Asymmetric Digraph

A complete asymmetric digraph is a directed graph where for every pair of distinct vertices, exactly one directed edge exists between them. This is equivalent to a tournament—a complete oriented graph.

#### 4. Acyclic Digraph (DAG)

A directed acyclic graph (DAG) is a digraph that contains no directed cycles. This is one of the most important types of digraphs in computer science, used extensively in task scheduling, dependency resolution, and topological sorting.

**Properties:**

- Every DAG has at least one vertex with no incoming edges (source) and at least one vertex with no outgoing edges (sink).
- Topological sorting is possible for DAGs.
- If a digraph has n vertices and is a DAG, it can have at most n(n-1)/2 edges.

**Example:** Consider a course prerequisite structure where courses have dependencies—this naturally forms a DAG.

#### 5. Strongly Connected Digraph

A digraph is strongly connected if there is a directed path from every vertex to every other vertex. In other words, for any two distinct vertices u and v, there exists a directed path from u to v and also from v to u.

**Example:** A directed cycle graph (v1 → v2 → v3 → ... → vn → v1) is strongly connected because you can travel in any direction along the cycle to reach any vertex.

**Testing Strong Connectivity:** A digraph is strongly connected if and only if a depth-first search from any vertex can reach all other vertices.

#### 6. Weakly Connected Digraph

A digraph is weakly connected if its underlying undirected graph (obtained by ignoring edge directions) is connected. This is a weaker condition than strong connectivity.

**Example:** Consider a digraph with vertices {a, b, c, d} and edges {(a, b), (b, c), (c, d)}. The underlying undirected graph is connected (a—b—c—d), so this digraph is weakly connected. However, there is no directed path from d to a, so it is not strongly connected.

#### 7. Tournament

A tournament is a directed graph obtained by assigning a direction to each edge in an undirected complete graph. For every pair of distinct vertices, exactly one directed edge connects them.

**Properties of Tournaments:**

- A tournament always contains a Hamiltonian path (a path that visits all vertices exactly once).
- A tournament is strongly connected if and only if it has a directed cycle of length 3.
- The score sequence of a tournament (outdegrees of vertices) satisfies certain conditions.

**Example:** With vertices {1, 2, 3}, edges could be {(1, 2), (3, 1), (2, 3)}—this is a tournament.

#### 8. Regular Digraph

A k-regular digraph is a digraph where each vertex has exactly k incoming edges and k outgoing edges. Regular digraphs are important in network design and distributed systems.

**Example:** A 1-regular digraph on n vertices consists of disjoint directed cycles that cover all vertices.

#### 9. Transitive Digraph

A digraph is transitive if whenever edges (u, v) and (v, w) exist, the edge (u, w) also exists. Transitive digraphs represent transitive relations in mathematics.

**Example:** If we have edges (a, b) and (b, c) in a transitive digraph, we must also have (a, c).

### Operations on Digraphs

#### 1. Union of Digraphs

The union of two digraphs G1 = (V1, E1) and G2 = (V2, E2) is a digraph G = (V1 ∪ V2, E1 ∪ E2).

#### 2. Intersection of Digraphs

The intersection is G = (V1 ∩ V2, E1 ∩ E2).

#### 3. Complement of a Digraph

The complement of a digraph G = (V, E) is another digraph with the same vertex set but with all directed edges that are not in E.

#### 4. Reversal of a Digraph

The reverse (or transpose) of a digraph G = (V, E) is a digraph G^T = (V, E^T) where E^T contains the reversal of each edge in E. If (u, v) ∈ E, then (v, u) ∈ E^T.

### Indegree and Outdegree

For any vertex v in a digraph:

- **Outdegree** od(v): Number of edges leaving v (edges of the form (v, u))
- **Indegree** id(v): Number of edges entering v (edges of the form (u, v))

The sum of all outdegrees equals the sum of all indegrees, both equal to the total number of edges in the digraph.

## Examples

### Example 1: Identifying Types of Digraphs

Consider the digraph G with vertices {A, B, C, D} and edges:
E = {(A, B), (B, C), (C, A), (C, D)}

**Solution:**

1. **Simple Digraph?** Yes - no loops and no multiple edges between same vertex pairs.

2. **Weakly Connected?** Yes - ignoring directions gives a connected graph (A-B-C-D).

3. **Strongly Connected?** Yes - we can reach any vertex from any other:

- A → B → C → D (A to D)
- A → B → C → A (A to A, cycle)
- D has no outgoing edges, so we cannot reach others from D!

Actually, this is NOT strongly connected because D has outdegree 0. Let me reconsider: D cannot reach A, B, or C. So it's weakly connected but not strongly connected.

4. **DAG?** No - contains directed cycle A → B → C → A.

5. **Complete?** No - not all vertex pairs have edges in both directions.

### Example 2: Finding Shortest Path in DAG using Topological Sort

Given a DAG with vertices representing tasks and edge weights representing time, find the minimum time to complete all tasks.

Consider tasks with dependencies:

- Vertex 1 (start): no prerequisites
- Vertex 2 depends on 1
- Vertex 3 depends on 1
- Vertex 4 depends on 2 and 3
- Vertex 5 depends on 4

Using topological sort: 1 → 2 → 3 → 4 → 5

The longest path (critical path) determines minimum completion time.

### Example 3: Proving a Property of Tournaments

**Prove that every tournament contains a Hamiltonian path.**

**Solution:**
We prove this by induction on the number of vertices n.

**Base case:** For n = 1, the single vertex is trivially a Hamiltonian path.

**Inductive step:** Assume every tournament with n vertices has a Hamiltonian path. Consider a tournament T with n+1 vertices.

Remove vertex v to get tournament T' with n vertices. By induction, T' has a Hamiltonian path: v1 → v2 → ... → vn.

Now we need to insert vertex v into this path. Consider the edges from v to the vertices in the path:

1. If there exists an edge from v to v1, then v → v1 → ... → vn is a Hamiltonian path.

2. If there exists an edge from vn to v, then v1 → ... → vn → v is a Hamiltonian path.

3. Otherwise, there must be some vertex vi such that there is an edge from vi to v and from v to vi+1 (by the nature of tournaments). Then the path v1 → ... → vi → v → vi+1 → ... → vn is a Hamiltonian path.

Thus, by induction, every tournament has a Hamiltonian path.

## Exam Tips

1. **Know the difference between strongly connected and weakly connected digraphs**: Strongly connected requires directed paths in both directions between any two vertices, while weakly connected only requires the underlying undirected graph to be connected.

2. **Remember that every DAG has a source and sink**: In any directed acyclic graph, there exists at least one vertex with indegree 0 (source) and at least one vertex with outdegree 0 (sink).

3. **Key property of tournaments**: Every tournament has a Hamiltonian path—this is a frequently tested theorem in university exams.

4. **Understanding regular digraphs**: A k-regular digraph has exactly k edges entering and k edges leaving each vertex. For n vertices, total edges = n × k.

5. **Complement of a digraph**: When finding the complement, ensure all possible edges (except loops) that don't exist in the original are added.

6. **Topological sort applies only to DAGs**: Remember that topological ordering exists if and only if the digraph is acyclic.

7. **Counting edges in complete digraph**: A complete digraph with n vertices has n(n-1) directed edges (not n(n-1)/2 like undirected).

8. **Transitive closure**: If a digraph represents a relation and is not transitive, its transitive closure adds edges to make it transitive (u → w if u → v and v → w exist).
