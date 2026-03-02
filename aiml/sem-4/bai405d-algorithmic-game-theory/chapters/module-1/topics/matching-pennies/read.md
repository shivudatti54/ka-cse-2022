# Matching and Covering in Graph Theory

## Introduction to Matching and Covering

Matching and covering are fundamental concepts in graph theory with significant applications in computer science, operations research, and combinatorics. These concepts deal with selecting edges or vertices in a graph that satisfy specific conditions without overlapping.

A **matching** is a set of edges without common vertices, while a **covering** is a set of vertices that "cover" all edges in the graph. These complementary concepts are connected through important theorems like Kőnig's theorem, which relates them in bipartite graphs.

## Basic Definitions

### Matching

A **matching** M in a graph G = (V, E) is a set of edges where no two edges share a common vertex. In other words, the edges in M are pairwise non-adjacent.

```
Graph Example:
A -- B
C -- D
E -- F

Matching: {A-B, C-D} is a valid matching
```

**Types of matchings:**

- **Maximum matching**: A matching with the largest possible number of edges
- **Perfect matching**: A matching that covers all vertices of the graph
- **Maximal matching**: A matching that cannot be extended by adding another edge

### Vertex Cover

A **vertex cover** C of a graph G = (V, E) is a set of vertices such that every edge in E has at least one endpoint in C.

```
Graph Example:
A -- B -- C
|    |
D -- E

Vertex cover: {B, D, E} covers all edges
```

### Edge Cover

An **edge cover** L of a graph G = (V, E) is a set of edges such that every vertex in V is incident to at least one edge in L.

```
Graph Example:
A -- B
|    |
C -- D

Edge cover: {A-B, A-C, B-D} covers all vertices
```

## Matching in Bipartite Graphs

Bipartite graphs are particularly important for matching problems. A bipartite graph G = (U, V, E) has its vertex set partitioned into two disjoint sets U and V, with edges only between vertices in different sets.

### Hall's Marriage Theorem

Hall's Theorem provides a necessary and sufficient condition for a bipartite graph to have a matching that covers all vertices in U.

**Theorem**: A bipartite graph G = (U, V, E) has a matching that covers U if and only if for every subset S ⊆ U, the number of neighbors |N(S)| ≥ |S|.

```
Example where Hall's condition fails:
U = {A, B}, V = {1}
Edges: A-1, B-1

For S = {A, B}, |N(S)| = |{1}| = 1 < |S| = 2
No matching covers both A and B
```

### Maximum Matching Algorithm for Bipartite Graphs

The Hopcroft-Karp algorithm finds a maximum matching in bipartite graphs efficiently (O(√n × m)).

**Basic steps:**

1. Start with an empty matching
2. Find augmenting paths using BFS
3. Augment the matching along these paths
4. Repeat until no more augmenting paths exist

```
Bipartite Graph:
U: A, B, C
V: 1, 2, 3
Edges: A-1, A-2, B-2, B-3, C-3

Step 1: Matching = {A-1}
Step 2: Augmenting path: B-2-A-1 (not valid)
         Actually: B-3 (free) is augmenting path
Step 3: Matching = {A-1, B-3}
Step 4: C-3-B-3? Not augmenting
Maximum matching size = 2
```

## Matching in General Graphs

While bipartite matching has elegant solutions, matching in general graphs is more complex. The Blossom algorithm (developed by Jack Edmonds) finds maximum matchings in general graphs.

**Key concept**: A **blossom** is an odd-length cycle that occurs during the matching process. The algorithm contracts blossoms to find augmenting paths.

```
General graph with blossom:
A -- B -- C
|    |    |
D -- E -- F

Blossom: B-C-F-E-D-B (odd cycle)
```

## Relationships Between Matching and Covering

### Kőnig's Theorem

In bipartite graphs, there's a fundamental relationship between matching and vertex covering:

**Kőnig's Theorem**: In any bipartite graph, the size of a maximum matching equals the size of a minimum vertex cover.

```
Bipartite graph:
U: A, B, C
V: 1, 2, 3
Edges: A-1, A-2, B-2, B-3, C-3

Maximum matching: {A-1, B-3} or {A-2, C-3} (size = 2)
Minimum vertex cover: {A, B} or {2, 3} (size = 2)
```

### Gallai's Theorem

For any graph without isolated vertices:
Size of maximum matching + Size of minimum edge cover = Number of vertices

## Algorithms for Matching and Covering

### Hungarian Algorithm for Assignment Problem

The Hungarian algorithm solves the assignment problem, which is essentially a weighted bipartite matching problem.

**Steps:**

1. Subtract row minima from each row
2. Subtract column minima from each column
3. Cover zeros with minimum lines
4. If lines < n, adjust matrix and repeat
5. Find optimal assignment

```
Cost matrix:
[3 1 2]
[2 4 3]
[3 2 1]

Step 1: Subtract row minima
[2 0 1]
[0 2 1]
[2 1 0]

Optimal assignment: Row1-Col2, Row2-Col1, Row3-Col3
Total cost = 1 + 2 + 1 = 4
```

### Greedy Algorithm for Vertex Cover

Although not optimal, a simple greedy algorithm provides a 2-approximation for vertex cover:

```
Algorithm:
1. Initialize cover = ∅
2. While edges remain:
   a. Pick an edge (u,v)
   b. Add both u and v to cover
   c. Remove all edges incident to u or v
```

## Applications of Matching and Covering

### Real-world Applications

1. **Job Assignment**: Matching workers to jobs (bipartite matching)
2. **Network Design**: Finding minimum vertex covers for network monitoring
3. **Scheduling**: Matching tasks to time slots
4. **Image Processing**: Feature matching between images
5. **Chemistry**: Matching molecular structures

### Computational Complexity

| Problem Type         | Graph Class | Best Known Algorithm    | Complexity |
| -------------------- | ----------- | ----------------------- | ---------- |
| Maximum Matching     | Bipartite   | Hopcroft-Karp           | O(√n × m)  |
| Maximum Matching     | General     | Blossom Algorithm       | O(n³)      |
| Minimum Vertex Cover | Bipartite   | Via Maximum Matching    | Polynomial |
| Minimum Vertex Cover | General     | NP-hard (approximation) | -          |
| Minimum Edge Cover   | Any         | Via Maximum Matching    | Polynomial |

## Example Problems with Solutions

### Example 1: Finding a Maximum Matching

```
Graph:
1--2--3
|  |  |
4--5--6

Step 1: Start with matching M = ∅
Step 2: Find augmenting path: 1-2 (add to matching)
Step 3: M = {1-2}
Step 4: Find augmenting path: 3-6 (add to matching)
Step 5: M = {1-2, 3-6}
Step 6: Find augmenting path: 4-5 (add to matching)
Step 7: M = {1-2, 3-6, 4-5} (maximum matching)
```

### Example 2: Finding a Minimum Vertex Cover

```
Using Kőnig's theorem on bipartite graph:
U: A, B, C; V: 1, 2, 3
Edges: A-1, A-2, B-2, B-3, C-3

Maximum matching: {A-1, B-3} (size = 2)
Minimum vertex cover: Also size 2, e.g., {A, B}
```

## Exam Tips

1. **Remember the relationships**: In bipartite graphs, |max matching| = |min vertex cover|
2. **Hall's condition**: Always check if |N(S)| ≥ |S| for all S ⊆ U when determining if a perfect matching exists
3. **Augmenting paths**: Look for alternating paths that start and end at free vertices
4. **Approximation algorithms**: Vertex cover has a 2-approximation algorithm, but exact solution is NP-hard for general graphs
5. **Practice with examples**: Work through multiple examples of finding matchings and covers in different graph types
6. **Understand the proofs**: While not always required, understanding proofs of Kőnig's and Hall's theorems provides deeper insight
