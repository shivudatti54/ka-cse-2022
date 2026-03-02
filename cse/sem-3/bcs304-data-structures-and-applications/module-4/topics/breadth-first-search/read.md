# Breadth First Search

## Introduction

**Breadth First Search (BFS)** is a fundamental graph traversal algorithm that explores vertices in increasing order of their distance from the source vertex. The algorithm systematically visits all vertices at distance k from the source before proceeding to vertices at distance k+1, thereby discovering vertices in non-decreasing order of their path length from the source. This level-by-level exploration pattern resembles ripples propagating outward from a stone dropped in water—the exploration radiates from the starting vertex in concentric layers of increasing distance.

BFS possesses several fundamental properties that make it indispensable in graph theory: it always discovers vertices in order of their shortest path distance from the source, it computes the shortest path in unweighted graphs, and it partitions the vertex set into disjoint levels corresponding to distances from the source.

## Theoretical Foundation

### Algorithm Description

BFS employs a **FIFO (First-In-First-Out) queue** data structure to manage the frontier of exploration. The algorithm maintains a visited set to prevent revisiting vertices and ensures each vertex is processed exactly once. The fundamental invariant maintained throughout BFS execution is that vertices are dequeued in non-decreasing order of their discovery time, which corresponds to their distance from the source vertex.

### Formal Algorithm Specification

```
BFS(Graph G, Vertex s):
    for each vertex v in G.V:
        color[v] ← WHITE          // Unvisited state
        distance[v] ← ∞           // Unknown distance
        predecessor[v] ← NIL     // No predecessor known

    color[s] ← GRAY               // Discovered but not fully processed
    distance[s] ← 0
    predecessor[s] ← NIL

    Create empty queue Q
    Enqueue(Q, s)

    while Q is not empty:
        u ← Dequeue(Q)
        for each neighbor v of u:
            if color[v] = WHITE:
                color[v] ← GRAY
                distance[v] ← distance[u] + 1
                predecessor[v] ← u
                Enqueue(Q, v)
        color[u] ← BLACK          // Fully processed
```

### Correctness Proof: Shortest Path Property

**Theorem**: For an unweighted graph G = (V, E) and source vertex s, BFS assigns to each vertex v discovered during the search a distance value distance[v] equal to the length of the shortest path (minimum number of edges) from s to v.

_Proof_: We prove this theorem by induction on the order in which vertices are discovered by BFS.

_Base Case_: The source vertex s is discovered first with distance[s] = 0, which is clearly the shortest path length from s to itself.

_Inductive Hypothesis_: Assume that when a vertex u is dequeued from the queue, distance[u] equals the length of the shortest path from s to u.

_Inductive Step_: When exploring neighbors of u, any undiscovered vertex v receives distance[v] = distance[u] + 1. By the inductive hypothesis, there exists a path from s to u of length distance[u]; appending edge (u, v) yields a path from s to v of length distance[u] + 1 = distance[v].

We must show no shorter path to v exists. Suppose a shorter path P' to v existed with length L < distance[v]. Let w be the predecessor of v on this shorter path. When w was processed (dequeued), v would have been discovered with distance[w] + 1 ≤ L < distance[v], contradicting the fact that v was first discovered with distance[v]. Therefore, distance[v] represents the shortest path length.

_Queue Order Invariant_: BFS processes vertices in non-decreasing distance order because vertices are enqueued only when discovered, and the FIFO property ensures all vertices at distance d are dequeued before any vertex at distance d+1. ∎

### Time and Space Complexity Analysis

**Theorem**: The time complexity of BFS on a graph G = (V, E) represented using an adjacency list is O(|V| + |E|).

_Proof_: We analyze each component of the algorithm:

- Initialization loop iterates over all |V| vertices: O(|V|)
- Each vertex is enqueued exactly once and dequeued exactly once: O(|V|)
- For each vertex dequeued, we examine all its adjacent edges. Since each edge in an undirected graph appears in adjacency lists of both endpoints, it is examined exactly twice. In a directed graph, each edge is examined exactly once. Thus, total edge examinations: O(|E|)

Summing all components: O(|V|) + O(|V|) + O(|E|) = O(|V| + |E|). ∎

**Space Complexity**: The algorithm requires O(|V|) space for:

- The visited/colour array: O(|V|)
- The distance array: O(|V|)
- The predecessor array: O(|V|)
- The queue: O(|V|) in worst case

For adjacency matrix representation, time complexity becomes O(|V|²) because exploring neighbors of a vertex requires scanning all |V| possible vertices regardless of actual adjacency.

## Step-by-Step Execution Trace

Consider the undirected graph G with vertices {0, 1, 2, 3, 4, 5} and edges: {0-1, 0-2, 1-3, 1-5, 2-3, 2-4}.

### Adjacency List Representation

```
Vertex 0: → 1 → 2
Vertex 1: → 0 → 3 → 5
Vertex 2: → 0 → 3 → 4
Vertex 3: → 1 → 2
Vertex 4: → 2
Vertex 5: → 1
```

### Detailed Execution Trace Starting from Vertex 0

| Step | Operation                     | Queue State (Front→Rear) | Distance Array   | Visited Vertices |
| ---- | ----------------------------- | ------------------------ | ---------------- | ---------------- |
| 1    | Initialize, Enqueue(0)        | [0]                      | d[0]=0, others=∞ | {0}              |
| 2    | Dequeue(0), Explore neighbors | [1, 2]                   | d[1]=1, d[2]=1   | {0,1,2}          |
| 3    | Dequeue(1), Explore neighbors | [2, 3, 5]                | d[3]=2, d[5]=2   | {0,1,2,3,5}      |
| 4    | Dequeue(2), Explore neighbors | [3, 5, 4]                | d[4]=2           | {0,1,2,3,5,4}    |
| 5    | Dequeue(3), No new neighbors  | [5, 4]                   | Unchanged        | {0,1,2,3,5,4}    |
| 6    | Dequeue(5), No new neighbors  | [4]                      | Unchanged        | {0,1,2,3,5,4}    |
| 7    | Dequeue(4), No new neighbors  | []                       | Unchanged        | {0,1,2,3,5,4}    |

**BFS Traversal Order**: 0 → 1 → 2 → 3 → 5 → 4

### Level Partitioning

```
Level 0 (Distance 0): {0}        — Source vertex
Level 1 (Distance 1): {1, 2}      — Adjacent to source
Level 2 (Distance 2): {3, 5, 4}  — Two edges from source
```

### BFS Tree Structure

```
         0          ← Level 0 (root)
        / \
       1   2        ← Level 1 (children of 0)
      /|   |\
     3 5   4        ← Level 2 (children of 1 and 2)
```

The BFS tree rooted at vertex 0 contains edges representing the predecessor relationship: {(0,1), (0,2), (1,3), (1,5), (2,4)}. This tree encodes the shortest path from vertex 0 to every reachable vertex.

## Implementation in C (Adjacency List)

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_VERTICES 100

/*---------------- Data Structures ----------------*/

typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

typedef struct {
    int numVertices;
    Node* adjacencyList[MAX_VERTICES];
} Graph;

typedef struct {
    int items[MAX_VERTICES];
    int front;
    int rear;
} Queue;

/*---------------- Queue Operations ----------------*/

void initializeQueue(Queue* q) {
    q->front = -1;
    q->rear = -1;
}

int isQueueEmpty(Queue* q) {
    return q->front == -1;
}

void enqueue(Queue* q, int value) {
    if (q->front == -1)
        q->front = 0;
    q->items[++q->rear] = value;
}

int dequeue(Queue* q) {
    return q->items[q->front++];
}

/*---------------- Graph Operations ----------------*/

Node* createNode(int v) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

void initializeGraph(Graph* g, int n) {
    g->numVertices = n;
    for (int i = 0; i < n; i++)
        g->adjacencyList[i] = NULL;
}

void addEdge(Graph* g, int u, int v) {
    // Add v to adjacency list of u
    Node* newNode = createNode(v);
    newNode->next = g->adjacencyList[u];
    g->adjacencyList[u] = newNode;

    // Add u to adjacency list of v (undirected graph)
    newNode = createNode(u);
    newNode->next = g->adjacencyList[v];
    g->adjacencyList[v] = newNode;
}

/*---------------- BFS Implementation ----------------*/

void BFS(Graph* g, int startVertex) {
    int visited[MAX_VERTICES] = {0};
    int distance[MAX_VERTICES];
    int predecessor[MAX_VERTICES];
    Queue q;
    initializeQueue(&q);

    // Initialize distance and predecessor arrays
    for (int i = 0; i < g->numVertices; i++) {
        distance[i] = INT_MAX;
        predecessor[i] = -1;
    }

    // Start BFS from source vertex
    visited[startVertex] = 1;
    distance[startVertex] = 0;
    enqueue(&q, startVertex);

    printf("BFS Traversal starting from vertex %d:\n", startVertex);

    while (!isQueueEmpty(&q)) {
        int currentVertex = dequeue(&q);
        printf("Dequeued: %d (distance: %d)\n", currentVertex, distance[currentVertex]);

        // Explore all adjacent vertices
        Node* temp = g->adjacencyList[currentVertex];
        while (temp != NULL) {
            int adjacentVertex = temp->vertex;
            if (!visited[adjacentVertex]) {
                visited[adjacentVertex] = 1;
                distance[adjacentVertex] = distance[currentVertex] + 1;
                predecessor[adjacentVertex] = currentVertex;
                enqueue(&q, adjacentVertex);
                printf("  → Enqueued: %d (from %d, distance: %d)\n",
                       adjacentVertex, currentVertex, distance[adjacentVertex]);
            }
            temp = temp->next;
        }
    }

    // Print shortest distances
    printf("\nShortest Distances from vertex %d:\n", startVertex);
    for (int i = 0; i < g->numVertices; i++) {
        if (distance[i] != INT_MAX)
            printf("  Vertex %d: %d\n", i, distance[i]);
        else
            printf("  Vertex %d: Unreachable\n", i);
    }
}

/*---------------- Path Reconstruction ----------------*/

void printPath(int predecessor[], int start, int target) {
    if (target == start) {
        printf("%d", start);
        return;
    }
    if (predecessor[target] == -1) {
        printf("No path exists");
        return;
    }
    printPath(predecessor, start, predecessor[target]);
    printf(" → %d", target);
}

/*---------------- Main Function ----------------*/

int main() {
    Graph graph;
    initializeGraph(&graph, 6);

    // Construct the graph
    addEdge(&graph, 0, 1);
    addEdge(&graph, 0, 2);
    addEdge(&graph, 1, 3);
    addEdge(&graph, 1, 5);
    addEdge(&graph, 2, 3);
    addEdge(&graph, 2, 4);

    BFS(&graph, 0);

    return 0;
}
```

## Applications of BFS

### 1. Shortest Path in Unweighted Graphs

As proven in the correctness theorem, BFS inherently computes the shortest path (minimum number of edges) from the source to all reachable vertices. The distance array stores these values, and the predecessor array enables path reconstruction.

### 2. Cycle Detection in Undirected Graphs

A cycle exists in an undirected graph if and only if BFS encounters a visited vertex that is not the immediate predecessor of the current vertex.

```c
int detectCycle(Graph* g, int start) {
    int visited[MAX_VERTICES] = {0};
    Queue q;
    initializeQueue(&q);

    visited[start] = 1;
    enqueue(&q, start);

    while (!isQueueEmpty(&q)) {
        int current = dequeue(&q);
        Node* temp = g->adjacencyList[current];

        while (temp != NULL) {
            int neighbor = temp->vertex;
            if (!visited[neighbor]) {
                visited[neighbor] = 1;
                enqueue(&q, neighbor);
            } else if (neighbor != current) {
                // Visit to already-visited node that isn't parent
                return 1; // Cycle detected
            }
            temp = temp->next;
        }
    }
    return 0; // No cycle
}
```

### 3. Bipartite Graph Checking

A graph is bipartite if its vertices can be partitioned into two disjoint sets such that no edge connects vertices within the same set. BFS can verify bipartiteness using a two-coloring approach:

```c
int isBipartite(Graph* g) {
    int color[MAX_VERTICES];
    for (int i = 0; i < g->numVertices; i++)
        color[i] = -1; // Uncolored

    Queue q;
    initializeQueue(&q);

    // Handle disconnected components
    for (int start = 0; start < g->numVertices; start++) {
        if (color[start] == -1) {
            color[start] = 0;
            enqueue(&q, start);

            while (!isQueueEmpty(&q)) {
                int u = dequeue(&q);
                Node* temp = g->adjacencyList[u];

                while (temp != NULL) {
                    int v = temp->vertex;
                    if (color[v] == -1) {
                        color[v] = 1 - color[u]; // Assign opposite color
                        enqueue(&q, v);
                    } else if (color[v] == color[u]) {
                        return 0; // Not bipartite
                    }
                    temp = temp->next;
                }
            }
        }
    }
    return 1; // Graph is bipartite
}
```

## BFS vs DFS: Comparative Analysis

| Aspect               | Breadth First Search                                     | Depth First Search                                 |
| -------------------- | -------------------------------------------------------- | -------------------------------------------------- |
| **Data Structure**   | Queue                                                    | Stack (or recursion)                               |
| **Traversal Order**  | Level by level                                           | Depth-first (backtracking)                         |
| **Memory Usage**     | O(width of graph)                                        | O(depth of graph)                                  |
| **Shortest Path**    | Finds shortest path in unweighted graphs                 | Does not guarantee shortest path                   |
| **Applications**     | Shortest path, level-order traversal, bipartite checking | Topological sorting, cycle detection, maze solving |
| **Space Complexity** | O(V)                                                     | O(V)                                               |
| **Time Complexity**  | O(V + E)                                                 | O(V + E)                                           |

## Handling Disconnected Graphs

When BFS is executed on a disconnected graph, only the component containing the source vertex is explored. To traverse all components, BFS must be initiated from every unvisited vertex:

```c
void BFSAllComponents(Graph* g) {
    int visited[MAX_VERTICES] = {0};

    for (int v = 0; v < g->numVertices; v++) {
        if (!visited[v]) {
            printf("\nStarting new component from vertex %d:\n", v);
            BFSComponent(g, v, visited);
        }
    }
}
```

## Complexity Summary

| Graph Representation | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| Adjacency List       | O(V + E)        | O(V)             |
| Adjacency Matrix     | O(V²)           | O(V)             |

Where V represents the number of vertices and E represents the number of edges in the graph.
