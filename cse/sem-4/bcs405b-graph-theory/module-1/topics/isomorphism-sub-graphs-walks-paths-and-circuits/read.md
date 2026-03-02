# Isomorphism, Subgraphs, Walks, Paths and Circuits

## Introduction

Graph theory is a fundamental branch of discrete mathematics that studies relationships between objects through the abstraction of vertices (or nodes) and edges (or arcs). While the geometric representation of a graph helps visualize its structure, the actual layout is not essential—what matters is the underlying abstract relationship. This distinction leads to the critical concept of **graph isomorphism**, which determines when two apparently different-looking graphs are structurally identical. Understanding isomorphism is essential for recognizing equivalent structures and avoiding redundant analysis.

Beyond isomorphism, the study of subgraphs allows us to extract meaningful components from larger graphs, enabling analysis of specific structural features. The concepts of **walks**, **paths**, and **circuits** form the backbone of graph traversal theory, with extensive applications in network analysis, route optimization, and solving various computational problems. These concepts are not merely theoretical constructs but provide the foundation for understanding connectivity, finding shortest routes, and identifying cycles in systems ranging from transportation networks to molecular structures.

This module explores these interconnected concepts systematically, establishing rigorous definitions and demonstrating their practical utility through carefully chosen examples. The material presented here forms an essential prerequisite for advanced topics such as Eulerian and Hamiltonian graphs, planarity testing, and graph coloring.

## Key Concepts

### 1. Graph Isomorphism

Two graphs G₁ = (V₁, E₁) and G₂ = (V₂, E₂) are said to be **isomorphic** if there exists a bijective function f: V₁ → V₂ such that for any two vertices u, v ∈ V₁, the edge {u, v} ∈ E₁ if and only if {f(u), f(v)} ∈ E₂. Such a function f is called an **isomorphism** between the graphs. When G₁ is isomorphic to G₂, we write G₁ ≅ G₂.

The bijective correspondence preserves the adjacency relationship exactly—if vertices are adjacent in one graph, their images must be adjacent in the other, and vice versa. Graph isomorphism is an equivalence relation, satisfying reflexivity (every graph is isomorphic to itself), symmetry (if G₁ ≅ G₂ then G₂ ≅ G₁), and transitivity (if G₁ ≅ G₂ and G₂ ≅ G₃ then G₁ ≅ G₃).

**Properties preserved under isomorphism:**
- Number of vertices and edges
- Degree sequence (multiset of vertex degrees)
- Number of connected components
- Presence of cycles of particular lengths
- Whether the graph is bipartite, regular, or complete

**Theorem (Isomorphism Invariants):** If two graphs are isomorphic, they must have identical values for: (i) number of vertices, (ii) number of edges, (iii) degree sequence, and (iv) number of connected components. However, these conditions are necessary but not sufficient—graphs can share all invariants without being isomorphic.

### 2. Subgraphs

A graph H = (V(H), E(H)) is a **subgraph** of a graph G = (V(G), E(G)) if V(H) ⊆ V(G) and E(H) ⊆ E(G). We write H ⊆ G to indicate that H is a subgraph of G. Several important special types of subgraphs merit specific attention.

A **spanning subgraph** (or spanning subgraph) of G is a subgraph that contains all vertices of G—that is, V(H) = V(G) but E(H) ⊆ E(G). Spanning subgraphs are particularly useful for studying properties that depend on vertex coverage. An **induced subgraph** is obtained by taking a subset of vertices and all edges between them that exist in the original graph. If S ⊆ V(G), the induced subgraph G[S] has vertex set S and edge set consisting of all edges of G whose both endpoints lie in S.

A **vertex-induced subgraph** on a set S ⊆ V(G) is G[S] = (S, E ∩ (S × S)). An **edge-induced subgraph** on a set F ⊆ E(G) is (V(F), F) where V(F) consists of all vertices incident to edges in F. The **complement** of a subgraph H in G, denoted G − H, is the subgraph containing all vertices of G and all edges of G not in H.

### 3. Walks, Trails, Paths, and Circuits

A **walk** in a graph G is a finite sequence of vertices and edges alternatingly, beginning and ending with vertices, where each edge connects its preceding and following vertices. Formally, a walk of length k is a sequence v₀, e₁, v₁, e₂, v₂, ..., e_k, v_k where for each i, e_i = {v_{i-1}, v_i} ∈ E(G). The vertices v₀ and v_k are called the **initial** and **terminal** vertices, respectively, and we say the walk connects v₀ to v_k. The **length** of a walk equals the number of edges it contains.

A walk in which all edges are distinct is called a **trail**. If additionally all vertices are distinct (except possibly the initial and terminal vertices), the trail becomes a **path**. More formally, a **path** of length k (k ≥ 0) is a sequence of distinct vertices v₀, v₁, ..., v_k such that v_i is adjacent to v_{i+1} for 0 ≤ i < k. A path of length k has k+1 vertices and k edges. The special case of a path of length 1 is simply an edge.

A **closed walk** is a walk where the initial and terminal vertices coincide (v₀ = v_k). A closed trail (all edges distinct) of length at least 3 is called a **circuit**. A **cycle** is a circuit in which all vertices except the initial/terminal vertex are distinct—a simple closed path. A cycle of length k is often denoted C_k. The smallest cycle possible in a simple graph is a triangle (C₃), as cycles of length 1 or 2 are not possible in simple graphs.

**Key Relationships:**
- Every path is a trail, and every trail is a walk
- Every cycle is a circuit, but not every circuit is a cycle
- The length of a walk/trail/path/circuit is the number of edges it contains

### 4. Distance in Graphs

The **distance** between two vertices u and v in a graph G, denoted d(u, v), is the length of the shortest path connecting them. If no path exists between u and v, we define d(u, v) = ∞. The distance function satisfies the **metric properties**: (i) d(u, v) ≥ 0 with equality iff u = v, (ii) d(u, v) = d(v, u) (symmetry), and (iii) d(u, v) ≤ d(u, w) + d(w, v) (triangle inequality).

The **eccentricity** of a vertex v, denoted ecc(v), is the maximum distance from v to any other vertex in the same connected component. The **radius** of a graph is the minimum eccentricity among all vertices, while the **diameter** is the maximum eccentricity. A vertex with minimum eccentricity is called a **center**, and a vertex pair with maximum distance defines the diameter.

## Examples

### Example 1: Graph Isomorphism

Consider graphs G₁ and G₂ both having 4 vertices and 4 edges, forming square shapes with diagonals:

G₁: vertices {a, b, c, d} with edges {ab, bc, cd, da, ac}
G₂: vertices {w, x, y, z} with edges {wx, xy, yz, zw, wy}

To check isomorphism, we attempt to find a bijection f. Observing that both graphs have: one vertex of degree 3 (the diagonal endpoint), two vertices of degree 2, and one vertex of degree 3. Mapping the degree-3 vertices correspondingly and preserving adjacency of edges and diagonals, we find G₁ ≅ G₂. However, if G₂ had the diagonal as {wx, yz} instead of {wy}, the graphs would not be isomorphic despite having the same degree sequence, as the diagonal positions differ.

### Example 2: Identifying Subgraphs

Given G with vertices {1, 2, 3, 4, 5} and edges {{1,2}, {1,3}, {2,3}, {2,4}, {3,4}, {4,5}}:

- Spanning subgraph H₁: Take all vertices, edges {{1,2}, {2,4}, {4,5}}—this is a path of length 3
- Induced subgraph G[{1,2,3,4}]: Contains vertices 1,2,3,4 and all edges between them—forming a K₄ minus one edge
- Edge-induced subgraph on {{1,2}, {2,3}, {3,1}}: This is the triangle on vertices {1,2,3}

### Example 3: Walks, Paths, and Circuits

In the graph with vertices {a, b, c, d, e} and edges {ab, bc, cd, de, ea, ac}:

- Walk: a → b → c → a → e → d (length 5, edges: ab, bc, ca, ae, ed)—not a trail (ca repeated)
- Trail: a → b → c → d → e (length 4, edges: ab, bc, cd, de)—all distinct
- Path: a → c → d → e (length 3, vertices a,c,d,e are distinct)
- Circuit: a → b → c → a (length 3, returns to start, edges ab, bc, ca)—also a cycle
- Cycle: a → c → d → e → a (length 4, vertices a,c,d,e distinct)

## Exam Tips

1. **Isomorphism Verification**: When proving two graphs are isomorphic, explicitly construct the bijection and verify adjacency preservation. When proving non-isomorphism, find a graph invariant that differs between them (most commonly: degree sequence or number of cycles of a specific length).

2. **Subgraph Recognition**: Carefully distinguish between induced and non-induced subgraphs. Remember that an induced subgraph contains all edges between selected vertices that exist in the original graph, while a non-induced subgraph may omit some edges.

3. **Path vs. Circuit vs. Cycle**: A path has distinct vertices; a circuit is a closed trail (may repeat vertices); a cycle is a simple closed path (only the start/end vertex repeats). These are distinct categories—memorize the inclusions: Path ⊂ Trail ⊂ Walk.

4. **Distance Properties**: Remember that distance is defined only within a connected component. The diameter represents the worst-case shortest path; computing it requires finding all pairwise distances.

5. **Edge Cases**: Consider isolated vertices and single-edge paths when analyzing graph properties. A single vertex constitutes a path of length 0. The empty graph (no vertices) requires careful handling in various definitions.

6. **Structural Arguments**: For isomorphism problems with larger graphs, consider using complement graphs or removing vertices of particular degrees to simplify the comparison. Look for unique degree sequences as quick non-isomorphism checks.

7. **Proof Techniques**: When proving statements about walks, paths, and circuits, use induction on the length of the walk. The fundamental approach involves considering whether a vertex repeats in the walk.