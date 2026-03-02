# Depth First Search

## Introduction and Formal Definition

**Depth First Search (DFS)** is a fundamental graph traversal algorithm that systematically explores vertices by venturing as deep as possible along each branch before backtracking. Formally, given a graph G = (V, E) and a source vertex s ∈ V, DFS explores all vertices reachable from s by maintaining a frontier of exploration that prioritizes depth over breadth.

The algorithm exhibits a **LIFO** (Last-In-First-Out) behavior, which can be realized either through explicit stack data structure or through the call stack of recursion. This fundamental characteristic distinguishes DFS from Breadth-First Search (BFS), which employs a FIFO queue.

**Mathematical Definition:** Let G = (V, E) be a directed or undirected graph. DFS defines a discovery time d[v] and finish time f[v] for each vertex v ∈ V, where d[v] represents the time when vertex v is first visited, and f[v] represents the time when all vertices reachable from v have been fully explored. These timestamps form the basis of several important graph algorithms and enable edge classification.

## Correctness Proof

**Theorem:** DFS visits every vertex reachable from the source vertex exactly once.

_Proof:_ We prove by induction on the length of the shortest path from source s to any vertex v.

_Base Case:_ For the source vertex s itself, the shortest path length is 0. DFS starts by marking s as visited and adding it to the exploration stack, so s is visited exactly once.

_Inductive Hypothesis:_ Assume that all vertices at distance k from s are visited exactly once.

_Inductive Step:_ Consider any vertex v at distance k+1 from s. There exists a vertex u at distance k from s such that (u, v) ∈ E. By the inductive hypothesis, u is visited exactly once. When u is processed, DFS examines all outgoing edges (u, v). Since v is unmarked (not yet visited), DFS visits v, marks it, and adds it to the stack. After visiting v, it is never added again because the visited array prevents re-entry. ∎

## Algorithm Specification

### Recursive Implementation

```c
void DFS(Graph* G, int v) {
    visited[v] = TRUE;
    discovery_time[v] = ++time;
    printf("%d ", v);

    for (each neighbor w of v) {
        if (!visited[w]) {
            parent[w] = v;  // Record tree edge
            DFS(G, w);
        }
    }
    finish_time[v] = ++time;
}
```

### Iterative Implementation Using Explicit Stack

```c
void DFS_Iterative(Graph* G, int start) {
    Stack S;
    initStack(&S);
    push(&S, start);

    while (!isEmpty(&S)) {
        int v = pop(&S);
        if (!visited[v]) {
            visited[v] = TRUE;
            discovery_time[v] = ++time;
            printf("%d ", v);

            // Push neighbors in reverse order for correct ordering
            for (int i = getNeighborCount(v)-1; i >= 0; i--) {
                int w = getNeighbor(v, i);
                if (!visited[w]) {
                    parent[w] = v;
                    push(&S, w);
                }
            }
        }
    }
    finish_time[v] = ++time;
}
```

## Time and Space Complexity Analysis

**Theorem:** DFS running on a graph G = (V, E) represented using adjacency lists completes in O(|V| + |E|) time.

_Proof:_ Consider the execution of DFS. Each vertex v ∈ V is marked visited exactly once, contributing O(|V|) operations. For each vertex v, we examine all edges incident to v. Since the sum of degrees over all vertices equals 2|E| for undirected graphs and |E| for directed graphs, the total edge examinations is O(|E|). Therefore, total time complexity is O(|V| + |E|).

For adjacency matrix representation, accessing neighbors of a vertex requires scanning an entire row of the matrix, giving O(V²) complexity regardless of the number of edges.

**Space Complexity:**

- Visited array: O(V)
- Discovery/finish time arrays: O(V)
- Stack (explicit or recursive): O(V) in worst case (when graph is a path)
- Total: O(V)

## Edge Classification in DFS Forest

During DFS execution, each edge (u, v) in the original graph can be classified based on the relationship between discovery and finish times of its endpoints. This classification is fundamental to several graph algorithms.

### Tree Edges

Edge (u, v) where vertex v is first discovered from vertex u during DFS. These edges form the **DFS tree** (or forest for disconnected graphs). Formally: d[u] < d[v] < f[v] < f[u].

### Back Edges

Edge (u, v) where v is an ancestor of u in the DFS tree (d[v] < d[u] < f[u] < f[v]). In undirected graphs, any non-tree edge connecting a vertex to its ancestor is a back edge. **Presence of a back edge guarantees a cycle in the graph.**

### Forward Edges

Edge (u, v) where v is a descendant of u in the DFS tree but not a tree edge (d[u] < d[v] < f[v] < f[u]).

### Cross Edges

Edge (u, v) where neither vertex is an ancestor of the other (d[v] < f[v] < d[u] < f[u]). In DFS of directed graphs, cross edges connect vertices in different subtrees of the DFS forest.

**Important Property:** In DFS of undirected graphs, every edge is either a tree edge or a back edge. Forward and cross edges only occur in directed graphs.

## DFS Properties and Parenthesis Structure

DFS exhibits the **parenthesis property**: for any two vertices u and v, the intervals [d[u], f[u]] and [d[v], f[v]] are either disjoint or one is completely contained within the other. This property enables efficient algorithms for:

1. **Finding LCA (Lowest Common Ancestor)** in trees
2. **Biconnected component decomposition**
3. **Strongly Connected Components (SCC)** via Kosaraju's or Tarjan's algorithm

## Applications of DFS

### 1. Cycle Detection

For undirected graphs: DFS detects a cycle if a non-tree edge (back edge) is found during traversal.

For directed graphs: DFS detects a cycle if a back edge is found (v is ancestor of u).

### 2. Topological Sorting

For directed acyclic graphs (DAGs), vertices can be sorted in reverse finish time order: f[v₁] > f[v₂] > ... > f[vₙ] produces a valid topological ordering.

### 3. Finding Connected Components

For undirected graphs, running DFS from an unvisited vertex discovers all vertices in that connected component. The number of DFS calls required to cover all vertices equals the number of connected components.

### 4. Finding Articulation Points

A vertex v is an articulation point if removing v (and its incident edges) increases the number of connected components. Using DFS with discovery times and low values, articulation points can be identified in O(V + E).

## Step-by-Step Execution Trace

Consider the directed graph:

```
0 → 1 → 3
↓ ↗ ↓
2 → 4
```

Adjacency list: 0:{1,2}, 1:{3}, 2:{0,4}, 3:{}, 4:{}

**DFS from vertex 0 (recursive):**

| Step | Vertex | d[v] | f[v] | Action                  | Stack |
| ---- | ------ | ---- | ---- | ----------------------- | ----- |
| 1    | 0      | 1    | --   | Visit 0, push neighbors | [1,2] |
| 2    | 2      | 2    | --   | Visit 2, push 4         | [1,4] |
| 3    | 4      | 3    | 4    | Visit 4, backtrack      | [1]   |
| 4    | --     | --   | --   | Return to 2, finish 2   | [1]   |
| 5    | 1      | 5    | --   | Visit 1, push 3         | [3]   |
| 6    | 3      | 6    | 7    | Visit 3, finish         | []    |
| 7    | --     | --   | 8    | Return to 1, finish     | []    |
| 8    | --     | --   | 9    | Return to 0, finish     | []    |

**Discovery times:** 0→1, 2→2, 4→3, 1→5, 3→6
**Finish times:** 4→4, 2→9, 3→7, 1→8, 0→9
**Traversal order:** 0, 2, 4, 1, 3

## Comparison: Recursive vs Iterative DFS

| Aspect         | Recursive                      | Iterative                 |
| -------------- | ------------------------------ | ------------------------- |
| Implementation | Simpler, more intuitive        | Requires explicit stack   |
| Stack Space    | O(V) call stack                | O(V) heap-allocated stack |
| Risk           | Stack overflow for deep graphs | No overflow risk          |
| Flexibility    | Limited                        | Can be paused/resumed     |

## Hard Analytical Questions

### Question 1

Consider a directed graph with 6 vertices and the following adjacency list: 0→{1,2}, 1→{3}, 2→{3}, 3→{4}, 4→{5}, 5→{}. If DFS traversal starts from vertex 0, what is the **second vertex to be finished** (i.e., the second vertex whose finish time is recorded)?

### Question 2

In DFS of an undirected graph with 8 vertices, the discovery times are: A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8. Which pair of vertices can definitely NOT have an edge between them?

### Question 3

A DFS performed on a directed graph produces discovery times d[] and finish times f[] as follows: d[A]=1, f[A]=18; d[B]=2, f[B]=17; d[C]=3, f[C]=4; d[D]=5, f[D]=16; d[E]=6, f[E]=15; d[F]=7, f[F]=14; d[G]=8, f[G]=13; d[H]=9, f[H]=12; d[I]=10, f[I]=11. Based on this information, identify all **back edges** in the graph.

### Question 4

What is the time complexity of finding all articulation points in a graph with V vertices and E edges using DFS-based algorithm?

---

**Answers:**

1. Vertex 1 (finish time = 8, after vertex 4 finishes at time 7)
2. Vertices A and H (discovery intervals are disjoint: [1,18] and [9,12])
3. Edges forming cycles: (B,A), (D,B), (E,D), (F,E), (G,F), (H,G), (I,H)
4. O(V + E)
