# Eulerian and Hamiltonian Paths

## Introduction

Graph theory, a fundamental branch of discrete mathematics, provides powerful tools for modeling and solving real-world problems ranging from network design to route optimization. Among the most fascinating and practically significant concepts in graph theory are Eulerian and Hamiltonian paths, named after two of the most celebrated mathematicians in history—Leonhard Euler and William Rowan Hamilton. These concepts, while superficially similar in naming, address fundamentally different problems and have distinct theoretical foundations and applications.

An Eulerian path concerns itself with traversing edges of a graph exactly once, while a Hamiltonian path focuses on visiting vertices exactly once. Understanding the distinction between these two problems is crucial for any computer science student, as they form the backbone of numerous algorithms and real-world applications. The Eulerian path problem was solved elegantly by Euler in 1736 through his famous theorem on the bridges of Königsberg, making it one of the earliest problems in graph theory and indeed one of the first problems to establish graph theory as a distinct mathematical discipline. The Hamiltonian path problem, despite its apparent similarity, proved to be fundamentally more challenging—indeed, it is one of the classic NP-complete problems, meaning there is no known efficient (polynomial-time) algorithm to solve it for arbitrary graphs.

In this chapter, we will explore the theoretical foundations of both Eulerian and Hamiltonian paths, learn algorithms for finding Eulerian paths, study important theorems related to Hamiltonian paths, and examine practical applications in fields such as computer networking, route planning, and DNA sequencing.

## Key Concepts

### Eulerian Paths and Circuits

An **Eulerian path** in a graph is a path that traverses each edge exactly once. If such a path starts and ends at the same vertex, it is called an **Eulerian circuit** or **Eulerian cycle**. A graph that possesses an Eulerian circuit is called an **Eulerian graph** or **Euler graph**.

**Theorem (Euler's Theorem):** A connected graph has an Eulerian circuit if and only if every vertex has even degree. A connected graph has an Eulerian path (but not a circuit) if and only if exactly two vertices have odd degree.

The proof of this theorem relies on the fact that whenever we enter a vertex via an edge, we must leave it via another edge (except for the starting and ending vertices in a path). Therefore, vertices in an Eulerian circuit must have an even number of edges incident to them—the degree must be even. For an Eulerian path, the two vertices with odd degree serve as the start and end points.

A **semi-Eulerian graph** is a connected graph that has an Eulerian path but not an Eulerian circuit. This occurs precisely when exactly two vertices have odd degree.

### Finding Eulerian Paths: Fleury's Algorithm

Fleury's algorithm provides a practical method for finding Eulerian paths in graphs that have them. The algorithm proceeds as follows:

1. Choose a starting vertex: If finding an Eulerian circuit, start at any vertex. If finding an Eulerian path (but not circuit), start at one of the odd-degree vertices.
2. At each step, traverse an edge that is not a bridge in the remaining graph, unless there is no alternative.
3. Remove the traversed edge from the graph.
4. Continue until all edges have been traversed.

The key insight is to avoid bridges (edges whose removal would disconnect the graph) unless absolutely necessary, as using a bridge prematurely would prevent completing the Eulerian path.

### Hierholzer's Algorithm

For finding Eulerian circuits efficiently, Hierholzer's algorithm is more practical than Fleury's algorithm. It works in O(V + E) time:

1. Start at any vertex and follow edges arbitrarily until returning to the starting vertex, forming a circuit.
2. If there are remaining edges in the graph, find a vertex in the current circuit that has unused incident edges.
3. From that vertex, follow unused edges to form a new circuit, then splice it into the existing circuit.
4. Repeat until all edges are used.

### Hamiltonian Paths and Cycles

A **Hamiltonian path** is a path in a graph that visits each vertex exactly once. If such a path returns to its starting vertex (forming a cycle), it is called a **Hamiltonian cycle**. A graph containing a Hamiltonian cycle is called a **Hamiltonian graph**.

Unlike the Eulerian case, there is no simple characterization of Hamiltonian graphs. This is one of the most famous unsolved problems in graph theory. However, several sufficient conditions have been discovered.

**Dirac's Theorem (1952):** If a simple graph with n vertices (n ≥ 3) has minimum degree δ(G) ≥ n/2, then the graph is Hamiltonian.

**Ore's Theorem (1960):** If a simple graph with n vertices (n ≥ 3) has the property that for every pair of non-adjacent vertices u and v, deg(u) + deg(v) ≥ n, then the graph is Hamiltonian.

These theorems provide sufficient conditions but not necessary ones—graphs can be Hamiltonian without satisfying these conditions.

A **semi-Hamiltonian graph** is a graph that has a Hamiltonian path but no Hamiltonian cycle.

### Differences Between Eulerian and Hamiltonian Problems

It is crucial to understand that despite the similarity in naming, these are fundamentally different problems:

| Aspect | Eulerian | Hamiltonian |
|--------|----------|-------------|
| What is traversed? | Edges | Vertices |
| Requirement | Every edge exactly once | Every vertex exactly once |
| Characterization | Simple (even/odd degrees) | Unknown (NP-complete) |
| Easy to find? | Yes, O(V + E) algorithms | No, exponential in worst case |
| Decision problem | P (polynomial time) | NP-complete |

## Examples

### Example 1: Determining Eulerian Nature

Consider the graph G with vertices {A, B, C, D, E} and edges: AB, AC, AD, BC, BD, CD, DE.

First, let's compute the degree of each vertex:
- deg(A) = 3 (connected to B, C, D)
- deg(B) = 3 (connected to A, C, D)
- deg(C) = 3 (connected to A, B, D)
- deg(D) = 4 (connected to A, B, C, E)
- deg(E) = 1 (connected to D)

Vertices A, B, C have odd degree (3), vertex D has even degree (4), and vertex E has odd degree (1). We have three vertices with odd degree (A, B, C, E—but wait, E has odd degree too).

Actually, let me recalculate: A has degree 3 (odd), B has degree 3 (odd), C has degree 3 (odd), D has degree 4 (even), E has degree 1 (odd). So we have four vertices with odd degree: A, B, C, and E.

Since the graph is connected and has exactly 0 vertices with odd degree, it has an Eulerian circuit. If it had exactly 2 odd-degree vertices, it would have an Eulerian path (but not circuit).

### Example 2: Finding an Eulerian Path Using Fleury's Algorithm

Consider the graph with vertices {1, 2, 3, 4, 5, 6} and edges: (1,2), (1,3), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5), (4,6), (5,6).

Degrees: deg(1)=2, deg(2)=4, deg(3)=4, deg(4)=4, deg(5)=4, deg(6)=2.

All vertices have even degree, and the graph is connected. Therefore, an Eulerian circuit exists. Using Fleury's algorithm starting from vertex 1:

1. From vertex 1, we can choose edge (1,2) or (1,3). Neither is a bridge initially. Let's choose (1,2).
2. At vertex 2, edges available: (2,3), (2,4), (2,5). Edge (2,3) is not a bridge. Choose (2,3).
3. At vertex 3, available: (1,3), (3,4), (3,5). Edge (1,3) is not a bridge. Choose (1,3).
4. Back at vertex 1, only edge (1,3) is already used, so we return... Wait, we used (1,3) just now. Let me reconsider.

Actually, starting fresh: 1 → 2 → 3 → 4 → 5 → 6 → 2 → 5 → 4 → 3 → 1 forms an Eulerian circuit.

### Example 3: Applying Dirac's Theorem

Consider a complete graph K₅ (5 vertices, each connected to every other). The minimum degree is 4, and n/2 = 2.5. Since 4 ≥ 2.5, Dirac's theorem guarantees K₅ is Hamiltonian—which we know is true since any complete graph with n ≥ 3 is Hamiltonian.

Consider a different graph: a cycle C₅ (5 vertices in a ring). The minimum degree is 2, and n/2 = 2.5. Since 2 < 2.5, Dirac's theorem does not apply. However, C₅ is indeed Hamiltonian (the cycle itself is a Hamiltonian cycle). This illustrates that Dirac's condition is sufficient but not necessary.

## Exam Tips

For DU semester examinations, keep the following points in mind:

1. **Memorize Euler's theorem precisely**: A connected graph has an Eulerian circuit iff all vertices have even degree. It has an Eulerian path (not circuit) iff exactly two vertices have odd degree.

2. **Always check connectivity first**: The degree conditions apply only to connected graphs. A disconnected graph can never have an Eulerian path or circuit.

3. **Understand when to use which algorithm**: For exams, Fleury's algorithm is more commonly tested as it's easier to explain step-by-step. Know both but focus on Fleury's for problem-solving.

4. **Dirac's and Ore's theorems are sufficient conditions**: Remember these are sufficient but not necessary conditions. A graph may be Hamiltonian even if these conditions fail.

5. **Know the practical differences**: Eulerian is about edges (P-problem, polynomial), Hamiltonian is about vertices (NP-complete). This distinction is frequently tested.

6. **For Hamiltonian problems in exams**: If asked to show a graph is Hamiltonian, either provide an explicit Hamiltonian cycle or apply Dirac's/Ore's theorem if applicable.

7. **Drawing matters**: In internal assessments and exams, practice drawing graphs and identifying Eulerian/Hamiltonian properties visually. Many questions ask you to determine these properties from a given graph.

8. **Application-based questions**: Be prepared for application questions like "A postman needs to deliver mail on every street"—this is Eulerian. "A salesman needs to visit every city once"—this is Hamiltonian.