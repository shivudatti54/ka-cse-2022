# Representations of Graphs


## Table of Contents

- [Representations of Graphs](#representations-of-graphs)
- [Introduction](#introduction)
- [1. Adjacency Matrix Representation](#1-adjacency-matrix-representation)
  - [1.1 Formal Definition](#11-formal-definition)
  - [1.2 Theoretical Properties](#12-theoretical-properties)
  - [1.3 Illustrative Examples](#13-illustrative-examples)
  - [1.4 Complexity Analysis](#14-complexity-analysis)
  - [1.5 Implementation in C](#15-implementation-in-c)
  - [1.6 Advantages and Limitations](#16-advantages-and-limitations)
- [2. Adjacency List Representation](#2-adjacency-list-representation)
  - [2.1 Formal Definition](#21-formal-definition)
  - [2.2 Illustrative Examples](#22-illustrative-examples)
  - [2.3 Complexity Analysis](#23-complexity-analysis)
  - [2.4 Implementation in C](#24-implementation-in-c)
- [3. Adjacency Multilist Representation](#3-adjacency-multilist-representation)
  - [3.1 Motivation and Definition](#31-motivation-and-definition)
  - [3.2 Example and Implementation](#32-example-and-implementation)
  - [3.3 Complexity Analysis](#33-complexity-analysis)
- [4. Comparative Analysis](#4-comparative-analysis)
  - [4.1 Selection Criteria](#41-selection-criteria)
  - [4.2 Summary of Key Formulas](#42-summary-of-key-formulas)
- [5. Assessment](#5-assessment)
  - [Multiple Choice Questions](#multiple-choice-questions)
- [Conclusion](#conclusion)

## Introduction

Graphs constitute one of the most versatile and widely employed data structures in computer science, enabling the modeling of pairwise relationships between objects. The efficient implementation of graph algorithms depends critically upon selecting an appropriate representation for the underlying graph structure. The choice of representation directly impacts the time complexity of fundamental operations such as edge insertion, edge deletion, and neighbor retrieval.

This module examines three principal methods for representing graphs in computer memory: the **adjacency matrix**, the **adjacency list**, and the **adjacency multilist**. Each representation possesses distinct characteristics regarding space complexity, operation efficiency, and suitability for specific graph categories. The theoretical analysis presented herein is accompanied by complete implementation examples in C, enabling practical understanding of the abstract concepts.

## 1. Adjacency Matrix Representation

### 1.1 Formal Definition

Let G = (V, E) denote a graph where V represents the finite set of vertices and E ⊆ V × V represents the set of edges. For a graph containing n = |V| vertices, the **adjacency matrix** A of G is defined as an n × n binary matrix:

**Definition 1.1 (Adjacency Matrix for Undirected Graphs):**

```
A[i][j] = 1  if (v_i, v_j) ∈ E
A[i][j] = 0  otherwise
```

For a **weighted graph** G_w = (V, E, w) where w: E → ℝ⁺ assigns positive weights to edges, the adjacency matrix stores weight values:

**Definition 1.2 (Adjacency Matrix for Weighted Graphs):**

```
A[i][j] = w(e)  if e = (v_i, v_j) ∈ E
A[i][j] = ∞     otherwise
```

where ∞ denotes the absence of an edge. In implementations, a sufficiently large constant (e.g., INT_MAX) or zero may serve this purpose.

### 1.2 Theoretical Properties

**Theorem 1.1 (Symmetry Property):**
For any undirected graph G, its adjacency matrix A is symmetric; that is, A[i][j] = A[j][i] for all 0 ≤ i, j < n.

_Proof:_ In an undirected graph, an edge (v_i, v_j) is identical to edge (v_j, v_i). By Definition 1.1, A[i][j] = 1 if and only if (v_i, v_j) ∈ E. Since (v_i, v_j) ∈ E implies (v_j, v_i) ∈ E in undirected graphs, we have A[i][j] = A[j][i] = 1. Similarly, when no edge exists, both entries equal 0. ∎

**Corollary 1.1:** The adjacency matrix of an undirected graph requires only n(n+1)/2 independent entries, though n² positions are allocated in storage.

**Theorem 1.2 (Degree Computation):**
For an undirected graph represented by adjacency matrix A, the degree of vertex v_i equals the sum of the i-th row (or column):

```
deg(v_i) = Σ_{j=0}^{n-1} A[i][j]
```

_Proof:_ Each entry A[i][j] = 1 precisely when an edge connects v_i to v_j. Counting the ones in row i counts every incident edge exactly once, which by definition equals the degree. ∎

### 1.3 Illustrative Examples

**Example 1.1 (Undirected Graph):**
Consider the graph:

```
     0 ----- 1
     | \    /
     |  \  /
     |   \/
     |   /\
     |  /  \
     | /    \
     2 ----- 3
```

The adjacency matrix A is:

```
    0  1  2  3
0 [ 0  1  1  0 ]
1 [ 1  0  1  1 ]
2 [ 1  1  0  1 ]
3 [ 0  1  1  0 ]
```

Verification: The matrix is symmetric, confirming Theorem 1.1. Row 0 sum = 2, indicating vertex 0 has degree 2, consistent with edges (0,1) and (0,2).

**Example 1.2 (Directed Graph):**
Consider the directed graph:

```
       0 -----> 1
       ↑       ↗
       |      /
       |     /
       |    v
       2 <----- 3
```

The adjacency matrix:

```
    0  1  2  3
0 [ 0  1  0  0 ]
1 [ 0  0  1  1 ]
2 [ 1  0  0  0 ]
3 [ 0  0  1  0 ]
```

Note: This matrix is asymmetric, characteristic of directed graphs. The out-degree of vertex i equals the row sum; the in-degree equals the column sum.

### 1.4 Complexity Analysis

**Table 1.1: Time Complexity of Basic Operations**

| Operation               | Time Complexity | Explanation                        |
| ----------------------- | --------------- | ---------------------------------- |
| Edge insertion          | O(1)            | Direct array access: A[u][v] = 1   |
| Edge deletion           | O(1)            | Direct array access: A[u][v] = 0   |
| Edge query              | O(1)            | Direct array access: check A[u][v] |
| Find all neighbors of v | O(n)            | Scan entire row v                  |
| Find in-degree of v     | O(n)            | Scan entire column v               |
| Space complexity        | O(n²)           | Requires n × n matrix storage      |

**Space Optimization Note:** For sparse graphs where |E| = O(n), the adjacency matrix requires O(n²) space while only storing O(n) actual edge data, representing a significant space inefficiency.

### 1.5 Implementation in C

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_VERTICES 100
#define INF INT_MAX

typedef struct {
    int n;                              // Number of vertices
    int adj[MAX_VERTICES][MAX_VERTICES]; // Adjacency matrix
} Graph;

// Create a graph with n vertices
Graph* createGraph(int n) {
    if (n > MAX_VERTICES) {
        fprintf(stderr, "Error: Maximum vertices exceeded\n");
        return NULL;
    }

    Graph* g = (Graph*)malloc(sizeof(Graph));
    if (!g) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }

    g->n = n;

    // Initialize all entries to 0 (or INF for weighted graphs)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            g->adj[i][j] = 0;
        }
    }
    return g;
}

// Insert undirected edge
void insertEdge(Graph* g, int u, int v) {
    if (u < 0 || u >= g->n || v < 0 || v >= g->n) {
        fprintf(stderr, "Invalid vertex indices\n");
        return;
    }
    g->adj[u][v] = 1;
    g->adj[v][u] = 1;  // Symmetric for undirected graph
}

// Insert directed edge
void insertDirectedEdge(Graph* g, int u, int v) {
    if (u < 0 || u >= g->n || v < 0 || v >= g->n) {
        fprintf(stderr, "Invalid vertex indices\n");
        return;
    }
    g->adj[u][v] = 1;
}

// Remove edge
void removeEdge(Graph* g, int u, int v) {
    g->adj[u][v] = 0;
    g->adj[v][u] = 0;
}

// Check if edge exists
int isAdjacent(Graph* g, int u, int v) {
    return g->adj[u][v] == 1;
}

// Compute out-degree
int outDegree(Graph* g, int v) {
    int degree = 0;
    for (int j = 0; j < g->n; j++) {
        if (g->adj[v][j]) degree++;
    }
    return degree;
}

// Compute in-degree (for directed graphs)
int inDegree(Graph* g, int v) {
    int degree = 0;
    for (int i = 0; i < g->n; i++) {
        if (g->adj[i][v]) degree++;
    }
    return degree;
}

// Print adjacency matrix
void printGraph(Graph* g) {
    printf("Adjacency Matrix (%d vertices):\n", g->n);
    printf("    ");
    for (int j = 0; j < g->n; j++) printf("%d ", j);
    printf("\n");
    for (int i = 0; i < g->n; i++) {
        printf("%d [ ", i);
        for (int j = 0; j < g->n; j++) {
            printf("%d ", g->adj[i][j]);
        }
        printf("]\n");
    }
}
```

### 1.6 Advantages and Limitations

**Advantages:**

- O(1) edge lookup and modification operations
- Simple implementation with straightforward semantics
- Efficient for dense graphs where |E| ≈ n²
- Enables rapid verification of edge existence
- Facilitates matrix-based graph algorithms (e.g., transitive closure via matrix multiplication)

**Limitations:**

- Space complexity O(n²) regardless of edge count
- Inefficient for sparse graphs (|E| << n²)
- Finding all neighbors requires O(n) scan
- Scalability issues for large graphs (e.g., n = 10⁶)

## 2. Adjacency List Representation

### 2.1 Formal Definition

An **adjacency list** represents a graph using an array of size n, where each index i corresponds to vertex v_i. At position i, a linked list (or dynamic array) stores all vertices adjacent to v_i, i.e., all v_j such that (v_i, v_j) ∈ E.

**Definition 2.1 (Adjacency List):**
For graph G = (V, E) with V = {v₀, v₁, ..., v\_{n-1}}, the adjacency list L is an array of n linked lists where:

```
L[i] = { j | (v_i, v_j) ∈ E }
```

For weighted graphs, each list element stores a pair (j, w) where w is the weight of edge (v_i, v_j).

### 2.2 Illustrative Examples

**Example 2.1 (Undirected Graph - Same as Example 1.1):**

```
Vertex 0: → [1] → [2]
Vertex 1: → [0] → [2] → [3]
Vertex 2: → [0] → [1] → [3]
Vertex 3: → [1] → [2]
```

**Example 2.2 (Directed Graph - Same as Example 1.2):**

```
Vertex 0: → [1]
Vertex 1: → [2] → [3]
Vertex 2: → [0]
Vertex 3: → [2]
```

Each list contains only out-neighbors (vertices reachable via outgoing edges).

**Example 2.3 (Weighted Graph):**
For a weighted graph with edges:

- (0,1,5), (0,2,3), (1,2,2), (1,3,7), (2,3,4)

```
Vertex 0: → [1, w=5] → [2, w=3]
Vertex 1: → [0, w=5] → [2, w=2] → [3, w=7]
Vertex 2: → [0, w=3] → [1, w=2] → [3, w=4]
Vertex 3: → [1, w=7] → [2, w=4]
```

### 2.3 Complexity Analysis

**Theorem 2.1 (Space Complexity):**
For a graph G = (V, E) represented using adjacency lists, the space complexity is O(|V| + |E|).

_Proof:_ The array requires O(|V|) storage for vertex pointers. Each edge (u, v) ∈ E appears exactly once in the list of u (for directed graphs) or twice—once in each endpoint's list (for undirected graphs). Thus, total list storage is O(|E|) for directed graphs and O(2|E|) = O(|E|) for undirected graphs. Combined with the array, space complexity is O(|V| + |E|). ∎

**Table 2.1: Time Complexity of Basic Operations**

| Operation                | Undirected Graph | Directed Graph |
| ------------------------ | ---------------- | -------------- |
| Edge insertion (at head) | O(1)             | O(1)           |
| Edge deletion            | O(deg(v))        | O(outdeg(v))   |
| Edge query               | O(deg(v))        | O(outdeg(v))   |
| Find all neighbors       | O(deg(v))        | O(outdeg(v))   |
| Space complexity         | O(V + E)         | O(V + E)       |

**Theorem 2.2 (Trade-off Analysis):**
For sparse graphs where |E| = O(|V|), adjacency lists require O(V) space, while adjacency matrices require O(V²) space. Conversely, for dense graphs where |E| = Θ(V²), adjacency matrices provide O(1) edge lookup while adjacency lists require O(V) lookup time.

_Proof:_ Directly follows from the respective complexity formulas. For sparse graphs, |E| = cV yields O(V + cV) = O(V) versus O(V²). For edge query operations, adjacency matrices access A[u][v] in O(1), whereas adjacency lists require traversing up to deg(u) entries. ∎

### 2.4 Implementation in C

```c
#include <stdio.h>
#include <stdlib.h>

// Node structure for adjacency list
typedef struct Node {
    int vertex;              // Adjacent vertex index
    int weight;              // Edge weight (0 for unweighted)
    struct Node* next;       // Pointer to next node
} Node;

// Graph structure
typedef struct {
    int n;                   // Number of vertices
    Node** adjList;          // Array of adjacency list heads
} GraphList;

// Create a new node
Node* createNode(int v, int w) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }
    newNode->vertex = v;
    newNode->weight = w;
    newNode->next = NULL;
    return newNode;
}

// Create graph with n vertices
GraphList* createGraphList(int n) {
    GraphList* g = (GraphList*)malloc(sizeof(GraphList));
    if (!g) return NULL;

    g->n = n;
    g->adjList = (Node**)malloc(n * sizeof(Node*));

    if (!g->adjList) {
        free(g);
        return NULL;
    }

    for (int i = 0; i < n; i++) {
        g->adjList[i] = NULL;
    }
    return g;
}

// Insert undirected edge
void insertEdgeList(GraphList* g, int u, int v, int weight) {
    // Add v to adjacency list of u
    Node* newNode = createNode(v, weight);
    newNode->next = g->adjList[u];
    g->adjList[u] = newNode;

    // Add u to adjacency list of v (for undirected graph)
    newNode = createNode(u, weight);
    newNode->next = g->adjList[v];
    g->adjList[v] = newNode;
}

// Insert directed edge
void insertDirectedEdgeList(GraphList* g, int u, int v, int weight) {
    Node* newNode = createNode(v, weight);
    newNode->next = g->adjList[u];
    g->adjList[u] = newNode;
}

// Check if edge exists
int isAdjacentList(GraphList* g, int u, int v) {
    Node* temp = g->adjList[u];
    while (temp) {
        if (temp->vertex == v) return 1;
        temp = temp->next;
    }
    return 0;
}

// Get out-degree
int outDegreeList(GraphList* g, int v) {
    int count = 0;
    Node* temp = g->adjList[v];
    while (temp) {
        count++;
        temp = temp->next;
    }
    return count;
}

// Get in-degree (requires scanning all vertices)
int inDegreeList(GraphList* g, int v) {
    int count = 0;
    for (int i = 0; i < g->n; i++) {
        Node* temp = g->adjList[i];
        while (temp) {
            if (temp->vertex == v) count++;
            temp = temp->next;
        }
    }
    return count;
}

// Print adjacency list
void printGraphList(GraphList* g) {
    printf("Adjacency List (%d vertices):\n", g->n);
    for (int i = 0; i < g->n; i++) {
        printf("Vertex %d: ", i);
        Node* temp = g->adjList[i];
        if (!temp) {
            printf("(no edges)");
        } else {
            while (temp) {
                printf("→ [%d", temp->vertex);
                if (temp->weight > 0) printf(", w=%d", temp->weight);
                printf("]");
                temp = temp->next;
            }
        }
        printf("\n");
    }
}

// Free graph memory
void freeGraphList(GraphList* g) {
    for (int i = 0; i < g->n; i++) {
        Node* temp = g->adjList[i];
        while (temp) {
            Node* next = temp->next;
            free(temp);
            temp = next;
        }
    }
    free(g->adjList);
    free(g);
}
```

## 3. Adjacency Multilist Representation

### 3.1 Motivation and Definition

In the adjacency list representation of an undirected graph, each edge (u, v) appears twice—once in u's list and once in v's list. When implementing algorithms that require edge deletion or manipulation (such as network flow algorithms), accessing both representations of the same edge becomes necessary but inefficient.

The **adjacency multilist** addresses this limitation by creating explicit edge objects that can be referenced from multiple adjacency lists. Each edge is represented as a node containing two pointers: one to the next edge in the source vertex's list and one to the next edge in the destination vertex's list.

**Definition 3.1 (Adjacency Multilist):**
A multilist representation maintains:

1. An array of vertex headers, each pointing to the first edge incident to that vertex
2. An array of edge nodes, where each edge node contains:
   - Endpoint vertices (u, v)
   - Two pointer fields: `next_u` links edges from u's perspective
   - `next_v` links edges from v's perspective

### 3.2 Example and Implementation

**Example 3.1:**
For the undirected graph with edges: (0,1), (0,2), (1,2), (1,3), (2,3)

The multilist structure maintains unique edge nodes that can be accessed via either endpoint's adjacency list, facilitating O(1) edge deletion from both perspectives.

### 3.3 Complexity Analysis

**Table 3.1: Adjacency Multilist Operations**

| Operation        | Time Complexity                |
| ---------------- | ------------------------------ |
| Edge insertion   | O(1)                           |
| Edge deletion    | O(1) (direct edge node access) |
| Edge query       | O(min(deg(u), deg(v)))         |
| Space complexity | O(V + E)                       |

The multilist combines the space efficiency of adjacency lists with improved edge deletion performance. It finds application in algorithms requiring frequent edge modifications, such as maximum flow computations and graph connectivity algorithms.

## 4. Comparative Analysis

### 4.1 Selection Criteria

**Table 4.1: Representation Selection Guidelines**

| Criterion             | Adjacency Matrix      | Adjacency List     | Adjacency Multilist        |
| --------------------- | --------------------- | ------------------ | -------------------------- |
| Graph density         | Dense (E ≈ V²)        | Sparse (E << V²)   | Sparse, frequent deletions |
| Edge lookup frequency | High                  | Low to Medium      | Medium                     |
| Memory availability   | Abundant              | Limited            | Limited                    |
| Primary operations    | Edge existence checks | Neighbor iteration | Edge deletion              |

**Theorem 4.1 (Optimal Representation):**
For a graph G = (V, E), if |E| < |V| log |V|, the adjacency list representation offers superior space-time trade-off; otherwise, consider the adjacency matrix.

_Proof:_ Compare space complexities:

- Matrix: Θ(|V|²)
- List: Θ(|V| + |E|)

Setting |V| + |E| < |V|² gives |E| < |V|(|V| - 1). For large |V|, this approximates |E| < |V|². The threshold |E| = |V| log |V| represents a practical heuristic where list representation becomes clearly advantageous. ∎

### 4.2 Summary of Key Formulas

| Representation      | Space    | Edge Query  | Neighbor Listing |
| ------------------- | -------- | ----------- | ---------------- |
| Adjacency Matrix    | O(V²)    | O(1)        | O(V)             |
| Adjacency List      | O(V + E) | O(deg(v))   | O(deg(v))        |
| Adjacency Multilist | O(V + E) | O(min(deg)) | O(deg(v))        |

## 5. Assessment

### Multiple Choice Questions

**Question 1:**
For a directed graph with 5,000 vertices and 15,000 edges, which representation provides the most space-efficient storage?

A) Adjacency matrix
B) Adjacency list
C) Adjacency multilist
D) All require equal space

**Answer:** B) Adjacency list

_Explanation:_ For a sparse graph where |E| = 15,000 and |V| = 5,000:

- Adjacency matrix: O(V²) = 25,000,000 entries
- Adjacency list: O(V + E) = 20,000 entries
  The adjacency list requires approximately 1,250 times less memory.

**Question 2:**
In an adjacency matrix representation of an undirected graph with 1,000 vertices, what is the minimum number of memory locations that must be explicitly stored to represent all possible edges?

A) 1,000
B) 500,000
C) 1,000,000
D) 499,500

**Answer:** D) 499,500

_Explanation:_ Due to matrix symmetry (Theorem 1.1), we need only store the upper (or lower) triangular portion: n(n-1)/2 = 1000 × 999 / 2 = 499,500.

**Question 3:**
Which operation is NOT efficiently supported by adjacency lists?

A) Inserting a new edge
B) Finding all neighbors of a vertex
C) Checking if two specific vertices are connected
D) Computing out-degree of a vertex

**Answer:** C) Checking if two specific vertices are connected

_Explanation:_ While adjacency lists support neighbor iteration (B) and out-degree computation (D) in O(deg(v)) time, edge existence queries require scanning through the adjacency list of one vertex, taking O(deg(u)) time. The adjacency matrix provides O(1) edge lookup.

**Question 4:**
A social network has 1 million users with an average of 50 connections per user. What is the approximate space complexity for storing this graph using an adjacency list?

A) O(10¹²)
B) O(10⁸)
C) O(10⁶)
D) O(10⁴)

**Answer:** C) O(10⁶)

_Explanation:_ Using adjacency lists: O(V + E) = O(1,000,000 + 50,000,000) = O(51,000,000) ≈ 10⁸ bytes, which is O(10⁶) in Big-O notation. Using adjacency matrix would require O(10¹²), making lists dramatically more efficient.

**Question 5:**
In a weighted directed graph stored using adjacency lists, what additional data must be stored in each list node?

A) Only the destination vertex index
B) The weight and destination vertex index
C) The weight and source vertex index
D) Both source and destination vertices with weight

**Answer:** B) The weight and destination vertex index

_Explanation:_ In adjacency list representation, each list corresponds to a source vertex. Nodes within the list store the destination vertex and the edge weight. The source is implicit from the list's position in the array.

---

## Conclusion

The representation of graphs constitutes a fundamental consideration in algorithm design and implementation. This module has presented a rigorous theoretical analysis of three principal representations: adjacency matrices, adjacency lists, and adjacency multilists. Each representation offers distinct trade-offs between space complexity and operation efficiency.

The adjacency matrix provides O(1) edge operations at the cost of O(V²) space, making it suitable for dense graphs. The adjacency list offers optimal space O(V + E) for sparse graphs but incurs O(deg(v)) lookup cost. The adjacency multilist combines space efficiency with efficient edge deletion capabilities.

A thorough understanding of these trade-offs, supported by formal complexity analysis and proofs, enables computer scientists and engineers to make informed decisions when designing graph-based algorithms and systems.
