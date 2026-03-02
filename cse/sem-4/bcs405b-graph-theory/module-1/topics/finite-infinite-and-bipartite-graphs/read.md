# Finite, Infinite, and Bipartite Graphs

## Introduction

Graph theory is a fundamental branch of discrete mathematics that deals with objects called graphs, which consist of vertices (or nodes) connected by edges. Understanding the classification of graphs is essential for solving real-world problems in computer science, networking, and optimization. This topic explores two important classifications: finite and infinite graphs, and a special type of graph called bipartite graphs.

Finite graphs, where the number of vertices and edges is finite, form the foundation of most practical applications. Infinite graphs, while more theoretical, are crucial in understanding infinite sequences, networks with unbounded growth, and certain computational models. Bipartite graphs represent a class of graphs where vertices can be divided into two disjoint sets such that every edge connects a vertex from one set to a vertex from the other set. This property makes bipartite graphs invaluable in matching problems, assignment problems, and relationship modeling.

The study of these graph types is particularly important for the university's Graph Theory course as they form the building blocks for more advanced topics like planar graphs, graph coloring, and network flows. Students must master these concepts to excel in both theoretical examinations and practical applications.

## Key Concepts

### Finite Graphs

A **finite graph** is a graph containing a finite number of vertices and a finite number of edges. In other words, both the vertex set V(G) and the edge set E(G) are finite sets. Most graphs encountered in practical applications and undergraduate studies are finite graphs.

**Properties of Finite Graphs:**

- The number of vertices is denoted as |V| or n
- The number of edges is denoted as |E| or m
- For a simple graph (no loops or multiple edges), the maximum number of edges is n(n-1)/2
- The sum of degrees of all vertices equals 2m (Handshaking Lemma)

**Examples of Finite Graphs:**

- A social network with 1000 users and 5000 friendship connections
- A computer network with 50 computers and 100 physical links
- A flowchart representing a finite algorithm

### Infinite Graphs

An **infinite graph** contains infinitely many vertices or edges. While they may seem purely theoretical, infinite graphs are important in various advanced applications.

**Types of Infinite Graphs:**

1. **Countably Infinite Graphs**: Graphs with countably infinite vertices (can be put in one-to-one correspondence with natural numbers). Example: The integer graph where vertices represent integers and edges connect consecutive integers.

2. **Uncountably Infinite Graphs**: Graphs with uncountably infinite vertices, such as continuous graphs used in topology.

3. **Locally Finite Graphs**: Infinite graphs where each vertex has finite degree.

4. **Infinite Paths and Rays**: An infinite path extends indefinitely in one direction (a ray) or both directions (a two-way infinite path).

**Applications of Infinite Graphs:**

- Modeling infinite data streams
- Theoretical computer science for modeling unbounded computation
- Telecommunication networks with potential for unlimited growth

### Bipartite Graphs

A **bipartite graph** is a graph whose vertex set can be partitioned into two disjoint sets U and V (called partite sets) such that every edge of the graph connects a vertex in U to a vertex in V. No edge connects two vertices within the same partite set.

**Formal Definition:**
A graph G = (V, E) is bipartite if and only if V can be partitioned into two subsets V₁ and V₂ such that:

- V₁ ∪ V₂ = V
- V₁ ∩ V₂ = ∅
- For every edge (u, v) ∈ E, either u ∈ V₁ and v ∈ V₂, or u ∈ V₂ and v ∈ V₁

**Characterization of Bipartite Graphs:**
A graph is bipartite if and only if it contains no odd cycles (cycles of odd length). This is a fundamental theorem in graph theory known as the bipartite graph characterization theorem.

**Proof Sketch:**

- (**If**) Suppose G is bipartite with partition (V₁, V₂). Starting from any vertex, edges alternate between V₁ and V₂. Therefore, any cycle must have even length (return to the starting set after an even number of edges).
- (**Only If**) If G has no odd cycles, we can perform a proper 2-coloring: start from any vertex and color it red, color all neighbors blue, continue alternating. Since there are no odd cycles, this process will not lead to contradictions.

### Complete Bipartite Graphs

A **complete bipartite graph** K(m,n) is a bipartite graph where:

- The first partite set has m vertices
- The second partite set has n vertices
- Every vertex in the first set is connected to every vertex in the second set
- There are no edges within each partite set

**Properties of K(m,n):**

- Number of vertices: m + n
- Number of edges: m × n
- It is a regular graph only when m = n
- K(m,n) is bipartite but not complete in the general graph sense

**Special Cases:**

- K(1,n) is called a star graph Sₙ
- K(n,n) is a regular bipartite graph with degree n

### Bipartite Graph Matching

A **matching** in a graph is a set of edges where no two edges share a vertex. In bipartite graphs, maximum matching has important applications.

**Key Definitions:**

- **Maximum Matching**: A matching containing the maximum possible number of edges
- **Perfect Matching**: A matching that covers all vertices (every vertex is incident to exactly one edge in the matching)
- For a bipartite graph to have a perfect matching, both partite sets must have equal size

## Examples

### Example 1: Identifying Bipartite Graphs

**Problem:** Determine whether the following graphs are bipartite:

a) A square (cycle of length 4)
b) A triangle (cycle of length 3)
c) A path of length 3

**Solution:**

a) **Square (C₄):** Yes, it is bipartite.

- Label vertices as v₁, v₂, v₃, v₄ in order
- Partition: V₁ = {v₁, v₃}, V₂ = {v₂, v₄}
- All edges connect vertices from different partitions
- C₄ contains only even cycles (length 4)

b) **Triangle (C₃):** No, it is not bipartite.

- Try to partition: start with vertex v₁ in V₁
- v₂ must be in V₂, v₃ must be in V₁ (adjacent to v₂)
- But v₁ and v₃ are adjacent and both in V₁ - contradiction!
- Contains odd cycle (length 3)

c) **Path of length 3 (P₄):** Yes, it is bipartite.

- Vertices: v₁ -- v₂ -- v₃ -- v₄
- Partition: V₁ = {v₁, v₃}, V₂ = {v₂, v₄}
- All edges connect different partitions

### Example 2: Complete Bipartite Graph Properties

**Problem:** For the complete bipartite graph K(3,4):
a) Find the number of vertices
b) Find the number of edges
c) Find the degree of each vertex
d) Determine if it has a perfect matching

**Solution:**

Given: m = 3, n = 4

a) **Number of vertices:** m + n = 3 + 4 = 7 vertices

b) **Number of edges:** m × n = 3 × 4 = 12 edges

c) **Degree of vertices:**

- Vertices in the first set (size 3): each has degree n = 4
- Vertices in the second set (size 4): each has degree m = 3
- Therefore: degrees are {4, 4, 4, 3, 3, 3, 3}

d) **Perfect matching:**

- For a perfect matching, both partitions must have equal size
- Here, |V₁| = 3 and |V₂| = 4
- Since 3 ≠ 4, K(3,4) does NOT have a perfect matching
- Maximum matching can have at most min(3,4) = 3 edges

### Example 3: Practical Application - Job Assignment

**Problem:** Consider a company with 3 jobs (J₁, J₂, J₃) and 3 candidates (C₁, C₂, C₃). The compatibility graph shows which candidates are qualified for which jobs:

- C₁ can do J₁ and J₂
- C₂ can do J₂ and J₃
- C₃ can do J₁ and J₃

Represent this as a bipartite graph and determine if a perfect matching exists.

**Solution:**

**Step 1: Construct the bipartite graph**

- Partite set U (Candidates): {C₁, C₂, C₃}
- Partite set V (Jobs): {J₁, J₂, J₃}
- Edges: (C₁,J₁), (C₁,J₂), (C₂,J₂), (C₂,J₃), (C₃,J₁), (C₃,J₃)

**Step 2: Find a matching**
We need to match each candidate to a unique job they are qualified for.

Attempt 1: Assign C₁ → J₁

- Then C₃ cannot use J₁ (already taken)
- C₃ can use J₃
- C₂ can use J₂
- Result: {C₁-J₁, C₂-J₂, C₃-J₃} - SUCCESS!

**Step 3: Conclusion**
A perfect matching exists. All 3 candidates can be assigned to distinct jobs they are qualified for. This is an example of Hall's Marriage Theorem application.

## Exam Tips

1. **Know the definitions clearly**: For university exams, memorize the precise definitions of finite, infinite, and bipartite graphs. Understand that finite/infinite refers to the cardinality of vertex and edge sets.

2. **Bipartite graph test**: Remember the key characterization theorem - a graph is bipartite if and only if it contains no odd cycles. This is frequently tested in examinations.

3. **Complete bipartite graph formula**: For K(m,n), remember:

- Vertices = m + n
- Edges = m × n
- This is a common numerical problem

4. **2-coloring approach**: When asked to show a graph is bipartite, demonstrate a proper 2-coloring by partitioning vertices into two sets with no edges within each set.

5. **Star graphs**: Remember that K(1,n) is called a star graph Sₙ - this special case frequently appears in exam questions.

6. **Perfect matching condition**: For a bipartite graph to have a perfect matching, both partite sets must have equal cardinality. This is necessary but not sufficient.

7. **Handshaking Lemma**: For any finite graph, the sum of all vertex degrees equals twice the number of edges. This is crucial for solving many numerical problems.

8. **Common examples**: Know that cycles of even length (C₄, C₆, etc.) are bipartite, while cycles of odd length (C₃, C₅, etc.) are not bipartite.
