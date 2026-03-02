# Matchings in Graph Theory

## Table of Contents

- [Matchings in Graph Theory](#matchings-in-graph-theory)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Definitions](#basic-definitions)
  - [Hall's Marriage Theorem](#halls-marriage-theorem)
  - [König's Theorem and Vertex Covers](#knigs-theorem-and-vertex-covers)
  - [Augmenting Paths](#augmenting-paths)
  - [Tutte's Theorem](#tuttes-theorem)
  - [Maximum Matching in Bipartite Graphs](#maximum-matching-in-bipartite-graphs)
- [Examples](#examples)
  - [Example 1: Applying Hall's Theorem](#example-1-applying-halls-theorem)
  - [Example 2: Finding a Maximum Matching](#example-2-finding-a-maximum-matching)
  - [Example 3: Applying König's Theorem](#example-3-applying-knigs-theorem)
- [Exam Tips](#exam-tips)

## Introduction

Matchings represent one of the most fundamental and practically significant concepts in graph theory. A matching in a graph is a set of edges where no two edges share a common vertex—essentially, we are pairing up vertices in such a way that each vertex belongs to at most one pair. This concept emerges naturally in numerous real-world applications, including job assignments where workers must be matched to jobs, college admissions where students apply to institutions, resource allocation problems, and even in scheduling scenarios where tasks must be assigned to time slots without conflicts.

The study of matchings forms a cornerstone of combinatorial optimization and has deep theoretical connections to other areas of graph theory, particularly vertex covers, independent sets, and flows. In the the syllabus for BCS405B - Graph Theory, this module carries substantial weightage, and students are expected to understand both the theoretical foundations (theorems and their proofs) and algorithmic aspects (finding maximum matchings). The material in this module builds upon concepts from earlier modules, particularly paths, cycles, and connectivity, making it essential to have a firm grasp of these prerequisites before studying matchings.

This module introduces several critical theorems including Hall's Marriage Theorem, König's Theorem, and Tutte's Theorem, each providing necessary and sufficient conditions for the existence of certain types of matchings. These theorems not only help in determining whether perfect matchings exist but also provide the theoretical foundation for algorithms used to find maximum matchings in practice.

## Key Concepts

### Basic Definitions

A **matching** M in a graph G = (V, E) is a subset of edges such that no two edges in M share a common vertex. If an edge e ∈ M is incident to a vertex v, we say that v is **matched** (or **covered**) by M; otherwise, v is **unmatched** (or **free**). The **size** of a matching is the number of edges it contains, denoted as |M|.

A **maximum matching** is a matching of maximum possible size in the graph. Every maximum matching is also maximal (meaning no additional edge can be added to the matching), but the converse is not necessarily true. A **perfect matching** (or **complete matching**) is a matching that covers every vertex in the graph—every vertex is incident to exactly one edge in the matching. A perfect matching exists only in graphs with an even number of vertices, and it is necessarily a maximum matching.

In **bipartite graphs** (graphs whose vertex set can be partitioned into two independent sets X and Y such that every edge connects a vertex in X to a vertex in Y), matchings take on special importance. We often denote a bipartite graph as G = (X, Y, E) where X and Y are the two partite sets.

### Hall's Marriage Theorem

The Hall's Marriage Theorem (also known as Hall's Theorem) provides a necessary and sufficient condition for the existence of a perfect matching in a bipartite graph. This theorem is fundamental and is frequently tested in university examinations.

**Theorem (Hall, 1935):** Let G = (X, Y, E) be a bipartite graph with partite sets X and Y. There exists a matching that covers every vertex in X (called an X-perfect matching) if and only if for every subset S ⊆ X, the number of neighbors of S (denoted N(S)) satisfies |N(S)| ≥ |S|.

**Proof Sketch:** The necessity is straightforward—if a matching covering X exists, then each subset S of X must have at least |S| distinct neighbors in Y (one for each vertex in S). For sufficiency, we use induction on |X|. The base case is trivial. For the inductive step, consider two cases: either every proper nonempty subset S ⊂ X has |N(S)| > |S|, or there exists a proper subset S ⊂ X with |N(S)| = |S|. In the first case, we can match any vertex x ∈ X with one of its neighbors and apply the inductive hypothesis to the remaining graph. In the second case, we apply the inductive hypothesis to S and to X \ S separately, using the fact that N(S) provides enough vertices to match S.

**Corollary:** If |X| = |Y| and |N(S)| ≥ |S| for all S ⊆ X, then G has a perfect matching.

### König's Theorem and Vertex Covers

König's Theorem establishes a beautiful relationship between matchings and vertex covers in bipartite graphs, which is why it's considered one of the most elegant results in graph theory.

**Theorem (König, 1931):** In any bipartite graph G, the size of a minimum vertex cover equals the size of a maximum matching.

This theorem has profound implications: it shows that the optimization problems of finding a maximum matching and finding a minimum vertex cover are equivalent in bipartite graphs. The theorem also provides an algorithmic approach—finding a maximum matching gives us the size of a minimum vertex cover.

A **vertex cover** is a set of vertices such that every edge in the graph has at least one endpoint in the set. The **minimum vertex cover** is the vertex cover of smallest possible size. König's Theorem tells us that in bipartite graphs, α'(G) = τ(G), where α'(G) is the size of a maximum matching and τ(G) is the size of a minimum vertex cover.

### Augmenting Paths

The concept of an **augmenting path** is crucial for understanding algorithms that find maximum matchings. An augmenting path with respect to a matching M is a path in the graph that alternates between edges not in M and edges in M, starts and ends at unmatched vertices.

If we can find an augmenting path, we can increase the size of the matching by one: simply toggle the status of edges on the path (edges not in M become part of the matching, and edges in M are removed). This operation is called **augmenting** along the path.

**Berge's Theorem:** A matching M in a graph is maximum if and only if there is no augmenting path with respect to M.

This theorem provides the theoretical foundation for the augmenting path algorithm (similar to the Ford-Fulkerson method for flows) used to find maximum matchings in bipartite graphs.

### Tutte's Theorem

For general (non-bipartite) graphs, Tutte's Theorem provides the characterization of when a perfect matching exists. This is more complex than the bipartite case due to the possibility of odd cycles.

**Theorem (Tutte, 1947):** A graph G has a perfect matching if and only if for every subset S ⊆ V(G), the number of odd components in G - S (denoted as o(G - S)) satisfies o(G - S) ≤ |S|.

This theorem generalizes Hall's Theorem—Hall's Theorem can be derived from Tutte's Theorem for the special case of bipartite graphs. The condition essentially states that removing any set of vertices should not create too many odd-sized components that would be impossible to pair up perfectly.

### Maximum Matching in Bipartite Graphs

The algorithm for finding a maximum matching in a bipartite graph G = (X, Y, E) proceeds as follows:

1. Start with an arbitrary matching M (often empty)
2. Find an augmenting path with respect to M
3. If an augmenting path exists, augment M along the path and repeat
4. If no augmenting path exists, M is maximum (by Berge's Theorem)

The key algorithmic challenge is efficiently finding augmenting paths. This can be done using BFS/DFS-based approaches, leading to algorithms with O(VE) time complexity. More sophisticated algorithms can achieve O(√V E) time complexity.

## Examples

### Example 1: Applying Hall's Theorem

Consider a bipartite graph with X = {x₁, x₂, x₃} and Y = {y₁, y₂, y₃, y₄}. The edges are: x₁ connected to y₁, y₂; x₂ connected to y₂, y₃; x₃ connected to y₃, y₄. Determine if an X-perfect matching exists.

**Solution:**

We need to check Hall's condition for all subsets S ⊆ X.

- For S = {x₁}: N(S) = {y₁, y₂}, so |N(S)| = 2 ≥ |S| = 1 ✓
- For S = {x₂}: N(S) = {y₂, y₃}, so |N(S)| = 2 ≥ |S| = 1 ✓
- For S = {x₃}: N(S) = {y₃, y₄}, so |N(S)| = 2 ≥ |S| = 1 ✓
- For S = {x₁, x₂}: N(S) = {y₁, y₂, y₃}, so |N(S)| = 3 ≥ |S| = 2 ✓
- For S = {x₁, x₃}: N(S) = {y₁, y₂, y₃, y₄}, so |N(S)| = 4 ≥ |S| = 2 ✓
- For S = {x₂, x₃}: N(S) = {y₂, y₃, y₄}, so |N(S)| = 3 ≥ |S| = 2 ✓
- For S = {x₁, x₂, x₃}: N(S) = {y₁, y₂, y₃, y₄}, so |N(S)| = 4 ≥ |S| = 3 ✓

Since Hall's condition holds for all subsets, an X-perfect matching exists. One such matching is: {x₁-y₁, x₂-y₂, x₃-y₃}.

### Example 2: Finding a Maximum Matching

Find a maximum matching in the bipartite graph with X = {a, b, c, d}, Y = {1, 2, 3, 4, 5} and edges: a-1, a-2, b-2, b-3, c-3, c-4, d-4, d-5.

**Solution:**

Starting with empty matching M = ∅:

Search for augmenting path starting from unmatched vertices in X:

- From a: Path a-2-b-3-c-4-d-5 ends at unmatched vertex 5 in Y
- Augment: M = {a-2, b-3, c-4, d-5}

Now check for more augmenting paths:

- From c: can reach 1 through c-4-d-5 (matched) and there's no path to 1
- From d: already matched, no augmenting path starting from d
- From a: can reach 1 through a-1, but 1 is unmatched

Actually, we can find augmenting path a-1: start at unmatched a, go to unmatched 1
Augment: M = {a-1, a-2, b-3, c-4, d-5} but this is invalid since a appears twice

Let's restart properly using alternating path concept:

**Iteration 1:** Start with M = ∅
Find augmenting path from unmatched a: a-1 (both unmatched)
Augment: M = {a-1}

**Iteration 2:** Unmatched vertices: b, c, d in X
Find augmenting path from b: b-2 (2 unmatched)
Augment: M = {a-1, b-2}

**Iteration 3:** Unmatched vertices: c, d in X
Find augmenting path from c: c-3 (3 unmatched)
Augment: M = {a-1, b-2, c-3}

**Iteration 4:** Unmatched vertices: d in X
Find augmenting path from d: d-4 (4 unmatched)
Augment: M = {a-1, b-2, c-3, d-4}

Now all vertices in X are matched. Check if we can find augmenting path from any Y vertex to increase matching:

- Vertex 5 is unmatched in Y. Can we reach it from some matched vertex?
- d-4 is matched, and d connects to 5. But d-4 is in matching, and d-5 is not.
- Path: 5-d-4-c... This path is d-5-c-4 which alternates but starts at unmatched 5 and goes to matched d, then to matched c via 4.

Actually, this is an alternating path from unmatched 5 to unmatched c, so it is an augmenting path!

**Iteration 5:** Augment along path 5-d-4-c-3-b-2-a-1:
Toggle edges: remove d-4, c-3, b-2, a-1 from M; add d-5, c-4, b-3, a-2 to M
New M = {a-2, b-3, c-4, d-5}

Now all X vertices are matched, and all Y vertices except 1 are matched. No more augmenting paths exist. Maximum matching size = 4.

### Example 3: Applying König's Theorem

In a bipartite graph, a maximum matching has size 5. Find the size of a minimum vertex cover and verify using König's Theorem.

**Solution:**

By König's Theorem, in any bipartite graph, the size of a minimum vertex cover equals the size of a maximum matching.

Therefore, minimum vertex cover size = maximum matching size = 5.

This is a direct application—the theorem guarantees this relationship without needing to construct either the matching or the vertex cover explicitly.

## Exam Tips

1. **Memorize Hall's Theorem statement precisely**: The condition |N(S)| ≥ |S| for all S ⊆ X is frequently tested. Be able to both state and apply it.

2. **Understand the difference between maximum and perfect matchings**: A perfect matching is a special case of maximum matching where all vertices are covered. Every perfect matching is maximum, but not vice versa.

3. **Know the relationship between matching and vertex cover**: König's Theorem states that in bipartite graphs, α'(G) = τ(G). This is a favorite examination topic.

4. **Berge's Theorem is fundamental**: Remember that a matching is maximum if and only if no augmenting path exists. This is the key to understanding matching algorithms.

5. **Tutte's Theorem for general graphs**: Although more complex, you should know its statement: A graph has a perfect matching if and only if o(G-S) ≤ |S| for all S ⊆ V.

6. **Practice checking Hall's condition**: Many questions ask you to determine whether a perfect matching exists by verifying Hall's condition for all subsets. Start with singletons and work upward.

7. **Algorithm for finding maximum matching**: Understand the augmenting path approach conceptually—you don't need to code it, but you should understand how it works.

8. **Graphs with odd number of vertices cannot have perfect matchings**: This obvious fact is often overlooked. Remember that |V| must be even for a perfect matching to exist.

9. **Hall's Theorem as a characterization**: Know that Hall's Theorem provides necessary and sufficient conditions—it's not just a sufficient condition.

10. **Realize the equivalence of different viewpoints**: Maximum matching, minimum vertex cover, and the existence of perfect matching are all interrelated through the theorems studied in this module.
