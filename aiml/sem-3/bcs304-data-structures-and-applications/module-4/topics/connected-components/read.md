# Connected Components in Graphs


## Table of Contents

- [Connected Components in Graphs](#connected-components-in-graphs)
- [1. Introduction and Theoretical Foundation](#1-introduction-and-theoretical-foundation)
  - [Theorem 1.1: Maximality Property](#theorem-11-maximality-property)
- [2. Fundamental Definitions](#2-fundamental-definitions)
  - [Definition 2.1: Connected Graph](#definition-21-connected-graph)
  - [Definition 2. Graph](#definition-2-graph)
  - [Definition 2.3: Isolated Vertex](#definition-23-isolated-vertex)
- [3. Algorithms for Finding Connected Components](#3-algorithms-for-finding-connected-components)
  - [3.1 Depth-First Search (DFS) Based Method](#31-depth-first-search-dfs-based-method)
  - [3.2 Breadth-First Search (BFS) Based Method](#32-breadth-first-search-bfs-based-method)
  - [3.3 Union-Find (Disjoint Set Union) Method](#33-union-find-disjoint-set-union-method)
- [4. Time and Space Complexity Analysis](#4-time-and-space-complexity-analysis)
  - [Theorem 4.1: Complexity Bounds](#theorem-41-complexity-bounds)
- [5. Strongly Connected Components (Directed Graphs)](#5-strongly-connected-components-directed-graphs)
  - [Definition 5.1: Strongly Connected Component](#definition-51-strongly-connected-component)
  - [Definition 5.2: Condensation Graph](#definition-52-condensation-graph)
- [6. Kosaraju's Algorithm for SCC Detection](#6-kosarajus-algorithm-for-scc-detection)
  - [Algorithm Steps](#algorithm-steps)
  - [Theorem 6.1: Correctness of Kosaraju's Algorithm](#theorem-61-correctness-of-kosarajus-algorithm)
  - [Example Trace](#example-trace)
- [7. Comprehensive Applications](#7-comprehensive-applications)
  - [7.1 Network Connectivity Analysis](#71-network-connectivity-analysis)
  - [7.2 Social Network Analysis](#72-social-network-analysis)
  - [7.3 Image Processing and Computer Vision](#73-image-processing-and-computer-vision)
  - [7.4 Compiler Design](#74-compiler-design)
  - [7.5 Web Graph Analysis](#75-web-graph-analysis)
  - [7.6 Clustering in Data Science](#76-clustering-in-data-science)
- [8. Numerical Problem](#8-numerical-problem)
- [9. Assessment Questions](#9-assessment-questions)
  - [Multiple Choice Questions](#multiple-choice-questions)
- [10. Complete C Implementation](#10-complete-c-implementation)
- [11. Summary](#11-summary)

## 1. Introduction and Theoretical Foundation

A **connected component** (also termed a **component** or **connected subgraph**) of an undirected graph G = (V, E) is defined as a maximal set of vertices C ⊆ V such that for every pair of distinct vertices u, v ∈ C, there exists a path in G connecting u to v. Formally, a connected component is a maximal connected subgraph of G, where a subgraph is connected if it contains a path between every pair of its vertices.

The set of all connected components partitions the vertex set V, meaning:

1. Each vertex belongs to exactly one connected component.
2. Two vertices from different components have no path connecting them.
3. The union of all components equals V, and components are pairwise disjoint.

If |V| = n and the graph contains k connected components, we denote this as k = κ(G), where κ represents the number of components. A graph is **connected** if and only if κ(G) = 1.

### Theorem 1.1: Maximality Property

Let C be a connected component of G. Then no vertex v ∈ V \ C can be added to C while preserving connectivity. Conversely, any maximal connected subgraph of G corresponds to exactly one connected component.

**Proof**: Suppose there exists a vertex v ∉ C such that adding v to C (along with all edges incident to v that connect to vertices in C) yields a larger connected subgraph. Then v must be adjacent to some vertex u there exists a path from any vertex w ∈ C to v via ∈ C, and u. This implies v is reachable from every vertex in C, contradicting the maximality assumption that C is a connected component. ∎

---

## 2. Fundamental Definitions

### Definition 2.1: Connected Graph

An undirected graph G = (V, E) is **connected** if for every pair of distinct vertices u, v ∈ V, there exists a simple path P from u to v consisting entirely of edges from E. Equivalently, G contains exactly one connected component (κ(G) = 1).

### Definition 2. Graph

A graph2: Disconnected G is **disconnected** if there exist at least two vertices u, v ∈ V such that no path exists from u to v. In this case, κ(G) ≥ 2, and G decomposes into multiple connected components.

### Definition 2.3: Isolated Vertex

A vertex v ∈ V with degree deg(v) = 0 forms a connected component of size one, termed an **isolated vertex** or **trivial component**.

```
Figure 1: Connected Graph (κ = 1)
    0 ─── 1
    │    ╲ │
    │     ╲│
    2 ───── 3

All vertices {0,1,2,3} form a single component.
```

```
Figure 2: Disconnected Graph (κ = 3)
    0 ─── 1      4 ─── 5
    │    │      │    │
    2    3      6

Component 1: {0,1,2,3}
Component 2: {4,5,6}
Component 3: ∅ (no isolated vertices shown)
```

---

## 3. Algorithms for Finding Connected Components

### 3.1 Depth-First Search (DFS) Based Method

The fundamental approach exploits the property that performing DFS/BFS from any unvisited vertex discovers exactly one connected component—the set of all vertices reachable from that starting vertex.

**Algorithm 1: DFS-Based Component Detection**

```
procedure FindComponentsDFS(G = (V, E)):
    for each vertex v ∈ V:
        visited[v] ← false

    componentCount ← 0
    for each vertex v ∈ V:
        if not visited[v] then
            componentCount ← componentCount + 1
            DFS(v)          // marks all vertices in this component

    return componentCount

procedure DFS(u):
    visited[u] ← true
    component[u] ← componentCount
    for each neighbor v of u in G:
        if not visited[v] then
            DFS(v)
```

**Theorem 3.1: Correctness of DFS-Based Component Finding**

_Claim_: After executing FindComponentsDFS on graph G, each vertex is labeled with the correct component number, and componentCount equals κ(G).

_Proof_: The algorithm processes vertices in the outer loop. When it encounters an unvisited vertex v, it increments componentCount and invokes DFS(v). By definition of DFS, all vertices reachable from v via paths in G are marked visited during this call. Since no vertex from a different component is reachable from v (by definition of disconnected components), DFS(v) visits precisely the vertices in the component containing v. After returning, v's entire component is marked visited, and the algorithm proceeds to find the next unvisited vertex, which must belong to a different component. By induction on the number of components, all vertices are correctly classified. ∎

### 3.2 Breadth-First Search (BFS) Based Method

BFS yields equivalent results with different traversal characteristics:

```
procedure FindComponentsBFS(G = (V, E)):
    for each vertex v ∈ V:
        visited[v] ← false

    componentCount ← 0
    for each vertex v ∈ V:
        if not visited[v] then
            componentCount ← componentCount + 1
            BFS(v)

    return componentCount

procedure BFS(start):
    Queue ← empty
    visited[start] ← true
    Enqueue(Queue, start)

    while Queue not empty:
        u ← Dequeue(Queue)
        for each neighbor v of u:
            if not visited[v] then
                visited[v] ← true
                Enqueue(Queue, v)
```

### 3.3 Union-Find (Disjoint Set Union) Method

For dynamic graphs where edges are added incrementally, the **Union-Find** data structure provides near-constant time amortized component detection.

**Data Structure Properties**:

- **MakeSet(x)**: Creates a singleton set containing element x
- **Find(x)**: Returns the representative (root) of the set containing x
- **Union(x, y)**: Merges the sets containing x and y

**Algorithm**:

```
procedure FindComponentsUnionFind(G = (V, E)):
    for each vertex v ∈ V:
        MakeSet(v)

    for each edge (u, v) ∈ E:
        if Find(u) ≠ Find(v):
            Union(u, v)

    // Count distinct representatives
    componentCount ← 0
    for each vertex v ∈ V:
        if v is representative:
            componentCount ← componentCount + 1

    return componentCount
```

**Theorem 3.2: Union-Find Amortized Complexity**

With **path compression** and **union by rank**, the amortized time complexity of m MakeSet, Find, and Union operations on n elements is O(m α(n)), where α is the inverse Ackermann function. Since α(n) ≤ 4 for all practical values of n, this is effectively O(m) per operation.

---

## 4. Time and Space Complexity Analysis

### Theorem 4.1: Complexity Bounds

| Algorithm  | Time Complexity | Space Complexity |
| ---------- | --------------- | ---------------- | --- | --- | ---- | --- | --- | ------------------------------------- | --- | --- |
| DFS-based  | O(              | V                | +   | E   | )    | O(  | V   | ) for visited array + recursion stack |
| BFS-based  | O(              | V                | +   | E   | )    | O(  | V   | ) for visited + queue                 |
| Union-Find | O(              | V                | +   | E   | · α( | V   | ))  | O(                                    | V   | )   |

**Proof**: For DFS/BFS, each vertex is visited exactly once, and each edge is examined exactly once in adjacency list representation, yielding O(V + E). The space includes the visited array (O(V)), the queue/stack (O(V)), and the adjacency list storage (O(V + E)). ∎

---

## 5. Strongly Connected Components (Directed Graphs)

### Definition 5.1: Strongly Connected Component

In a directed graph G = (V, A), a **strongly connected component (SCC)** is a maximal set of vertices S ⊆ V such that for every ordered pair (u, v) ∈ S × S, there exists both a directed path from u to v and a directed path from v to u.

### Definition 5.2: Condensation Graph

The **condensation graph** (or **component graph**) G^SCC is obtained by contracting each SCC into a single super-vertex. Edges exist between super-vertices if there is at least one edge between the corresponding SCCs in the original graph.

**Theorem 5.1**: The condensation graph of any directed graph is a **Directed Acyclic Graph (DAG)**.

_Proof_: Suppose G^SCC contains a directed cycle. All vertices in this cycle belong to SCCs that can reach each other via directed paths. By transitivity, any vertex in the cycle can reach any other vertex, contradicting the maximality property of SCCs—all vertices in the cycle would merge into a single SCC. ∎

---

## 6. Kosaraju's Algorithm for SCC Detection

Kosaraju's algorithm computes all SCCs in O(|V| + |E|) time using two graph traversals.

### Algorithm Steps

1. **First DFS Pass**: Perform DFS on the original graph G. Push each vertex onto a stack when its DFS finishes (post-order).
2. **Graph Transpose**: Compute G^T, the transpose of G (reverse all directed edges).
3. **Second DFS Pass**: While the stack is non-empty, pop vertices. On G^T, perform DFS from each unvisited vertex. Each DFS tree corresponds to one SCC.

### Theorem 6.1: Correctness of Kosaraju's Algorithm

_Proof Sketch_: In the first pass, vertices are ordered by finish time. Any vertex that can reach another must finish after the vertex it reaches. When edges are reversed in G^T, this order ensures that starting DFS from the vertex with highest finish time explores exactly one SCC—vertices in the same SCC become reachable in G^T because there are reverse paths. ∎

### Example Trace

```
Figure 3: Directed Graph
    0 → 1 → 2 → 3
              ↓   ↺
              4

Adjacency List:
0: {1}, 1: {2}, 2: {3,4}, 3: {0}, 4: {}

First DFS (starting from 0): Visit order yields stack [3, 4, 2, 1, 0]
Transpose G^T: 0←{3}, 1←{0}, 2←{1}, 3←{2}, 4←{2}

Second DFS on G^T (popping from stack):
- Pop 0: DFS visits {0,3,2,1} → SCC₁ = {0,1,2,3}
- Pop 4: DFS visits {4} → SCC₂ = {4}

Result: Two SCCs
```

---

## 7. Comprehensive Applications

### 7.1 Network Connectivity Analysis

In computer networks, connected components identify network segments. Disconnected components represent isolated subnetworks or failure points. The algorithm aids in network reliability assessment andfault isolation.

### 7.2 Social Network Analysis

Community detection in social networks leverages connected components to identify clusters of individuals who can reach each other through social connections.

### 7.3 Image Processing and Computer Vision

**Connected Component Labeling** in binary images assigns unique labels to foreground pixels, identifying distinct objects. This technique is fundamental to object recognition and medical imaging.

### 7.4 Compiler Design

In call graphs, SCCs identify groups of mutually recursive functions (cycles). Breaking these cycles is essential for effective optimization and static analysis.

### 7.5 Web Graph Analysis

Search engines analyze the web's link structure using SCCs to understand citation patterns and determine page importance (e.g., PageRank initialization).

### 7.6 Clustering in Data Science

Component-based clustering provides a simple yet effective method for discovering natural groupings in spatial datasets.

---

## 8. Numerical Problem

**Problem**: Given an undirected graph with 8 vertices and the following adjacency list, determine the number of connected components:

```
A: B, C
B: A, D
C: A
D: B
E: F
F: E, G
G: F
H: (none)
```

**Solution**:

- Starting from A: DFS reaches {A, B, C, D} → Component 1
- From E: DFS reaches {E, F, G} → Component 2
- H has no neighbors (isolated vertex) → Component 3

**Answer: 3 connected components**

---

## 9. Assessment Questions

### Multiple Choice Questions

**Question 1** (Application Level):
In a connected undirected graph with n vertices, what is the minimum number of edges required to ensure the graph remains connected after the removal of any single edge?

(A) n - 1  
(B) n  
(C) n(n-1)/2  
(D) 2n - 2

**Answer**: (A) n - 1. A tree on n vertices has exactly n - 1 edges and remains connected after removing any edge only if it's a cycle; however, for minimum edges maintaining connectivity, a spanning tree structure is required.

**Question 2** (Analysis Level):
Consider Kosaraju's algorithm applied to a directed graph with n vertices and m edges. If the first DFS completes in O(n + m) time, what is the total time complexity?

(A) O(n)  
(B) O(m)  
(C) O(n + m)  
(D) O(nm)

**Answer**: (C) O(n + m). Both DFS passes take O(n + m) each, and transpose computation also takes O(n + m), yielding O(n + m).

**Question 3** (Numerical Problem):
A graph has 6 vertices and 4 edges. What is the maximum possible number of connected components?

(A) 2  
(B) 3  
(C) 4  
(D) 6

**Answer**: (D) 6. With no edges, each vertex is isolated, giving 6 components.

---

## 10. Complete C Implementation

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

typedef struct {
    int numVertices;
    Node* adjList[MAX_VERTICES];
    int visited[MAX_VERTICES];
    int componentId[MAX_VERTICES];
} Graph;

// Create a new graph with n vertices
Graph* createGraph(int n) {
    Graph* g = (Graph*)malloc(sizeof(Graph));
    g->numVertices = n;
    for (int i = 0; i < n; i++) {
        g->adjList[i] = NULL;
        g->visited[i] = 0;
        g->componentId[i] = -1;
    }
    return g;
}

// Add undirected edge
void addEdge(Graph* g, int src, int dest) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = dest;
    newNode->next = g->adjList[src];
    g->adjList[src] = newNode;

    newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = src;
    newNode->next = g->adjList[dest];
    g->adjList[dest] = newNode;
}

// DFS utility function
void DFS(Graph* g, int vertex, int compNum) {
    g->visited[vertex] = 1;
    g->componentId[vertex] = compNum;

    Node* temp = g->adjList[vertex];
    while (temp) {
        int adjVertex = temp->vertex;
        if (!g->visited[adjVertex]) {
            DFS(g, adjVertex, compNum);
        }
        temp = temp->next;
    }
}

// Find all connected components
int findComponents(Graph* g) {
    int componentCount = 0;

    for (int v = 0; v < g->numVertices; v++) {
        if (!g->visited[v]) {
            componentCount++;
            DFS(g, v, componentCount);
        }
    }
    return componentCount;
}

// Print components
void printComponents(Graph* g) {
    for (int c = 1; c <= g->componentId[0]; c++) {
        printf("Component %d: ", c);
        for (int v = 0; v < g->numVertices; v++) {
            if (g->componentId[v] == c) {
                printf("%d ", v);
            }
        }
        printf("\n");
    }
}

// Free graph memory
void freeGraph(Graph* g) {
    for (int i = 0; i < g->numVertices; i++) {
        Node* temp = g->adjList[i];
        while (temp) {
            Node* prev = temp;
            temp = temp->next;
            free(prev);
        }
    }
    free(g);
}

// Main function for testing
int main() {
    // Build graph from Figure 2
    Graph* g = createGraph(7);

    addEdge(g, 0, 1);
    addEdge(g, 0, 2);
    addEdge(g, 1, 0);
    addEdge(g, 2, 0);
    addEdge(g, 4, 5);
    addEdge(g, 4, 6);
    addEdge(g, 5, 4);
    addEdge(g, 6, 4);
    // Vertex 3 is isolated

    int count = findComponents(g);
    printf("Number of connected components: %d\n", count);
    printComponents(g);

    freeGraph(g);
    return 0;
}
```

---

## 11. Summary

Connected components provide a fundamental decomposition of graphs into maximal connected subgraphs. For undirected graphs, DFS/BFS-based algorithms efficiently identify components in O(V + E) time. The Union-Find data structure offers an alternative approach with near-constant amortized time for dynamic edge insertion. In directed graphs, strongly connected components (SCCs) generalize this concept, and Kosaraju's algorithm computes them efficiently in O(V + E) time. The condensation graph formed by SCCs is always a DAG. These concepts underpin numerous applications across computer networks, social analysis, image processing, and compiler design.
