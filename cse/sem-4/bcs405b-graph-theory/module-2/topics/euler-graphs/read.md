# Euler Graphs

## Table of Contents

- [Euler Graphs](#euler-graphs)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definitions](#definitions)
  - [Euler's Theorems](#eulers-theorems)
  - [Fleury's Algorithm](#fleurys-algorithm)
  - [Hierholzer's Algorithm](#hierholzers-algorithm)
  - [Graph Connectivity](#graph-connectivity)
  - [Relationship Between Eulerian and Hamiltonian Concepts](#relationship-between-eulerian-and-hamiltonian-concepts)
- [Examples](#examples)
  - [Example 1: Determining Eulerian Nature](#example-1-determining-eulerian-nature)
  - [Example 2: Finding Eulerian Circuit Using Fleury's Algorithm](#example-2-finding-eulerian-circuit-using-fleurys-algorithm)
  - [Example 3: Hierholzer's Algorithm](#example-3-hierholzers-algorithm)
- [Exam Tips](#exam-tips)

## Introduction

Euler graphs represent one of the most celebrated topics in graph theory, originating from the famous problem of the Seven Bridges of Königsberg. In 1736, Leonhard Euler solved this problem by proving that it was impossible to walk through the city of Königsberg crossing each of its seven bridges exactly once. This solution gave birth to graph theory as a mathematical discipline and introduced the fundamental concepts of Eulerian paths and circuits that we study today.

An Euler graph is a graph that contains a closed trail (a trail is a walk with no repeated edges) passing through every edge of the graph exactly once. If such a trail exists but is not closed (i.e., it starts and ends at different vertices), the graph is called a semi-Eulerian graph. These concepts have significant practical applications in route planning, network design, DNA sequencing, and solving various optimization problems where we need to traverse every edge exactly once.

Understanding Euler graphs requires a firm grasp of fundamental graph theory terminology including vertices, edges, degree of vertices, paths, circuits, connected graphs, and subgraph concepts. This module explores the necessary and sufficient conditions for Eulerian behavior, algorithms to find Eulerian trails, and numerous examples to solidify understanding.

## Key Concepts

### Definitions

**Eulerian Circuit**: An Eulerian circuit (or Eulerian cycle) is a closed trail that contains every edge of a graph exactly once. The trail starts and ends at the same vertex.

**Eulerian Path**: An Eulerian path (or Eulerian trail) is a trail that contains every edge of a graph exactly once but does not necessarily return to the starting vertex. It starts and ends at different vertices.

**Euler Graph**: A connected graph that possesses an Eulerian circuit is called an Euler graph (or Eulerian graph).

**Semi-Eulerian Graph**: A connected graph that has an Eulerian path but not an Eulerian circuit is called a semi-Eulerian graph (or semi-Eulerian graph).

### Euler's Theorems

**Theorem 1 (Euler's Circuit Theorem)**: A connected graph is an Euler graph if and only if every vertex has even degree.

_Proof_:

- (**Necessity**) If an Eulerian circuit exists, it must traverse each edge exactly once and return to the starting vertex. Each time the circuit enters a vertex, it must also leave it (except for the starting/ending vertex which are the same). Therefore, each vertex is visited an even number of times, meaning the degree of each vertex must be even.
- (**Sufficiency**) If every vertex has even degree in a connected graph, we can construct an Eulerian circuit. Start from any vertex and follow edges arbitrarily, ensuring we never traverse an edge that would leave us stranded (i.e., a bridge that hasn't been used yet). This process continues until all edges are exhausted, and since all degrees are even, we return to the starting vertex.

**Theorem 2 (Euler's Path Theorem)**: A connected graph has an Eulerian path but not an Eulerian circuit if and only if it has exactly two vertices of odd degree.

_Proof_:

- If an Eulerian path exists from vertex u to vertex v (where u ≠ v), then u and v must have odd degree (the path starts at u and ends at v, so these vertices have one more entry than exit or vice versa). All other vertices, being entered and exited equal numbers of times, have even degree.
- Conversely, if a connected graph has exactly two vertices of odd degree, we can add a hypothetical edge between these two vertices to make all vertices even. The resulting graph has an Eulerian circuit. Removing this added edge gives us an Eulerian path between the two odd-degree vertices.

### Fleury's Algorithm

Fleury's Algorithm provides a systematic method to find an Eulerian path or circuit in a graph:

1. **Start at appropriate vertex**:

- If finding an Eulerian circuit, start at any vertex
- If finding an Eulerian path (semi-Eulerian case), start at one of the odd-degree vertices

2. **At each step, choose an edge**:

- Never choose a bridge (cut edge) unless no alternative exists
- A bridge is an edge whose removal would disconnect the graph

3. **Continue** until all edges have been traversed

**Why avoid bridges?** Choosing a bridge prematurely could disconnect the graph before all edges are visited, making it impossible to complete the trail.

### Hierholzer's Algorithm

Hierholzer's Algorithm is more efficient than Fleury's Algorithm for finding Eulerian circuits:

1. **Start** at any vertex and construct a circuit by traversing unused edges until returning to the starting vertex

2. **If there are unexplored edges** in the graph:

- Find a vertex in the current circuit that has unused incident edges
- From that vertex, construct a new circuit
- Splice this new circuit into the existing one

3. **Repeat** until all edges are included in a single circuit

This algorithm runs in O(E) time complexity, making it highly efficient for large graphs.

### Graph Connectivity

For a graph to be Eulerian or semi-Eulerian, it must be connected (except isolated vertices). If a graph has isolated vertices, they don't affect Eulerian properties since edges cannot be traversed to or from them. Such vertices can simply be ignored when determining Eulerian nature.

### Relationship Between Eulerian and Hamiltonian Concepts

| Aspect     | Eulerian                                                            | Hamiltonian                                  |
| ---------- | ------------------------------------------------------------------- | -------------------------------------------- |
| Traverses  | Every edge exactly once                                             | Every vertex exactly once                    |
| Condition  | All vertices even degree (circuit) or exactly two odd degree (path) | No simple necessary and sufficient condition |
| Complexity | Polynomial time (O(E))                                              | NP-complete                                  |

## Examples

### Example 1: Determining Eulerian Nature

Consider a graph with vertices A, B, C, D and edges: AB, AC, AD, BC, BD, CD (complete graph K4).

**Solution**:

- Degree of A = 3 (odd)
- Degree of B = 3 (odd)
- Degree of C = 3 (odd)
- Degree of D = 3 (odd)

The graph has 4 vertices of odd degree, which is neither 0 nor 2. Therefore, K4 is neither Eulerian nor semi-Eulerian.

### Example 2: Finding Eulerian Circuit Using Fleury's Algorithm

Consider a graph with vertices P, Q, R, S and edges: PQ, QR, RS, SP, PS, QS

Degrees:

- P: 3 (edges PQ, PS, SP) - Wait, let me recalculate properly
- Using edges: PQ, QR, RS, SP, PS, QS
- P connects to Q, S, S → degree 3
- Q connects to P, R, S → degree 3
- R connects to Q, S → degree 2
- S connects to R, P, P, Q → degree 4

All vertices have even degree (P:3 is odd - let me reconsider)

Let's use a clearer example: A graph with vertices A, B, C, D and edges: AB, BC, CD, DA, AC

Degrees:

- A: 3 (AB, DA, AC) - odd
- B: 2 (AB, BC) - even
- C: 3 (BC, CD, AC) - odd
- D: 2 (CD, DA) - even

Exactly two vertices (A and C) have odd degree. This is a semi-Eulerian graph with an Eulerian path from A to C or C to A.

Finding the Eulerian path using Fleury's Algorithm starting at A:

- From A, we can choose AB or AC (neither is a bridge initially)
- Let's choose AB: A→B
- From B, only BC is available: B→C
- From C, we can choose CD or AC. Neither is a bridge currently.
- Choose CD: C→D
- From D, we can go to A via DA: D→A
- Now we have edges AB, BC, CD, DA used. Remaining: AC
- From A, go to C: A→C
- Path: A → B → C → D → A → C

All 5 edges are traversed exactly once. This is a valid Eulerian path.

### Example 3: Hierholzer's Algorithm

Consider a graph with vertices 1, 2, 3, 4 and edges: 1-2, 2-3, 3-1, 1-4, 4-2

**Step 1**: Start at vertex 1 and build a circuit: 1→2→3→1 (uses edges 1-2, 2-3, 3-1)

**Step 2**: Find a vertex in this circuit with unused edges. Vertex 1 has unused edge 1-4. From 1, build new circuit: 1→4→2→1 (uses edges 1-4, 4-2, 2-1)

**Step 3**: Splice this circuit into the original:

- Original: 1→2→3→1
- Replace 1→2 with 1→4→2→1→2
- Result: 1→4→2→1→2→3→1

All edges used: 1-2, 2-3, 3-1, 1-4, 4-2. This is the Eulerian circuit.

## Exam Tips

1. **Remember the key theorem**: For a connected graph - Eulerian circuit exists if and only if all vertices have even degree; Eulerian path exists if and only if exactly two vertices have odd degree.

2. **Always check connectivity first**: Before applying Euler's theorems, ensure the graph is connected (ignoring isolated vertices). A disconnected graph cannot be Eulerian.

3. **Distinguish between circuit and path**: If all vertices have even degree → Eulerian circuit. If exactly two vertices have odd degree → Eulerian path (not circuit). Any other case → Not Eulerian or semi-Eulerian.

4. **Fleury's Algorithm - avoid bridges**: When applying Fleury's algorithm, never choose a bridge unless you have no alternative. Test if removing an edge disconnects the graph to identify bridges.

5. **Hierholzer's for efficiency**: In exam questions requiring construction of Eulerian trail, Hierholzer's algorithm is often faster and less error-prone than Fleury's algorithm.

6. **Handshaking Lemma verification**: The sum of all vertex degrees equals 2E. Use this to quickly verify your degree calculations.

7. **Semi-Eulerian start point**: For semi-Eulerian graphs, the Eulerian path must start at one odd-degree vertex and end at the other.

8. **Consider multiple components**: If the graph has multiple components with edges, it's not Eulerian. Isolated vertices (no edges) can be ignored.
