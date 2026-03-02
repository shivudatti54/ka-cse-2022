# Greedy Algorithms: Minimum Spanning Tree & Shortest Path

## Comprehensive Study Material for GE7A - Design and Analysis of Algorithms

---

## 1. Introduction to Greedy Algorithms

### 1.1 What is a Greedy Algorithm?

A **Greedy Algorithm** is a problem-solving paradigm that builds a solution incrementally by making the most optimal choice at each step, hoping that these local optimal choices lead to a globally optimal solution. Unlike Dynamic Programming (which explores all possibilities and stores intermediate results), Greedy algorithms make irrevocable decisions based on the current state without considering future consequences.

### 1.2 Characteristics of Greedy Algorithms

- **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to subproblems
- **Greedy Choice Property**: A global optimal solution can be obtained by making locally optimal choices

### 1.3 When to Use Greedy Approach

Greedy algorithms are ideal when:
- The problem exhibits the greedy choice property
- Local optimum leads to global optimum
- No backtracking is required
- Efficiency is paramount

### 1.4 Greedy vs Dynamic Programming

| Aspect | Greedy | Dynamic Programming |
|--------|--------|---------------------|
| Approach | Makes choice then solves subproblems | Solves subproblems first, then makes choice |
| Memory | Usually less memory | Requires table storage |
| Optimality | May not always give optimal solution | Always gives optimal solution |
| Time Complexity | Often faster | Generally slower |

---

## 2. Minimum Spanning Tree (MST)

### 2.1 Introduction

A **Minimum Spanning Tree (MST)** is a subset of edges in a weighted, undirected graph that connects all vertices with the minimum possible total edge weight, without forming any cycles. A spanning tree has exactly V-1 edges (where V is the number of vertices).

### 2.2 Real-World Applications of MST

- **Network Design**: Telephone, electrical, or computer network布线
- **Transportation Networks**: Road and rail connectivity
- **Cluster Analysis**: Grouping similar data points
- **Image Segmentation**: Boundary detection in computer vision

### 2.3 Kruskal's Algorithm

Kruskal's Algorithm is a **greedy** algorithm that finds MST by sorting all edges in ascending order of weight and adding them one by one, skipping edges that would create cycles.

#### Algorithm Steps:
1. Sort all edges by weight (ascending order)
2. Initialize a Disjoint Set Union (DSU) for all vertices
3. For each edge (u, v) in sorted order:
   - If u and v are in different components, add edge to MST
   - Union the two components

#### Detailed Example:

Consider the following graph with 6 vertices:

```
        10
    A -------- B
    |  \      /|
   6|   5\  /15|
    |     \/   |4
    |     /\   |
    |   4/  \  |
    | /       \|
    C -------- D
        2
```

**Edge List (sorted by weight):**
| Edge | Weight |
|------|--------|
| C-D  | 2      |
| A-C  | 6      |
| B-D  | 4      |
| A-B  | 10     |
| B-C  | 5      |
| A-D  | 15     |

**Step-by-step construction:**

| Step | Edge Added | Weight | Reason |
|------|------------|--------|--------|
| 1 | C-D | 2 | Different components |
| 2 | B-D | 4 | Different components |
| 3 | A-C | 6 | Different components |
| 4 | Skip A-B (10) | - | Would create cycle (A-C-D-B) |
| 5 | Skip B-C (5) | - | Would create cycle |
| 6 | Skip A-D (15) | - | Would create cycle |

**Total MST Weight: 2 + 4 + 6 = 12**

#### C++ Implementation:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Edge {
    int src, dest, weight;
    bool operator<(Edge const& other) {
        return weight < other.weight;
    }
};

struct DSU {
    vector<int> parent, rank;
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return false;
        if (rank[x] < rank[y]) swap(x, y);
        parent[y] = x;
        if (rank[x] == rank[y]) rank[x]++;
        return true;
    }
};

int main() {
    int V = 6, E = 8;
    vector<Edge> edges = {
        {0, 1, 10}, {0, 2, 6}, {0, 3, 15},
        {1, 3, 4}, {2, 3, 5}, {2, 4, 2},
        {3, 4, 2}, {3, 5, 3}, {4, 5, 4}
    };
    
    sort(edges.begin(), edges.end());
    DSU dsu(V);
    int mstWeight = 0;
    vector<Edge> mst;
    
    for (Edge e : edges) {
        if (dsu.unite(e.src, e.dest)) {
            mst.push_back(e);
            mstWeight += e.weight;
        }
        if (mst.size() == V - 1) break;
    }
    
    cout << "MST Weight: " << mstWeight << endl;
    return 0;
}
```

#### Time Complexity:
- **Sorting edges**: O(E log E) = O(E log V)
- **DSU operations**: O(E α(V)) ≈ O(E)
- **Total**: **O(E log V)**

---

### 2.4 Prim's Algorithm

Prim's Algorithm grows the MST by starting from an arbitrary vertex and gradually adding the minimum weight edge that connects a vertex in the MST to a vertex outside it.

#### Algorithm Steps:
1. Start with an arbitrary vertex (usually vertex 0)
2. Maintain a min-priority queue of edges connecting MST to non-MST vertices
3. Repeatedly extract the minimum weight edge that doesn't form a cycle
4. Add the connected vertex to MST

#### Detailed Example:

Using the same graph:

```
        10
    A -------- B
    |  \      /|
   6|   5\  /15|
    |     \/   |4
    |     /\   |
    |   4/  \  |
    | /       \|
    C -------- D
        2
```

**Starting from vertex A:**

| Step | Vertex Added | Edge | Weight | Total |
|------|--------------|------|--------|-------|
| 1 | A | - | 0 | 0 |
| 2 | C | A-C | 6 | 6 |
| 3 | D | C-D | 2 | 8 |
| 4 | B | B-D | 4 | 12 |

**MST: A-C (6) + C-D (2) + B-D (4) = 12**

#### C++ Implementation:

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

int main() {
    int V = 5;
    vector<vector<pair<int, int>>> graph(V);
    
    // Sample graph: (neighbor, weight)
    graph[0] = {{1, 10}, {2, 6}, {3, 15}};
    graph[1] = {{0, 10}, {3, 4}};
    graph[2] = {{0, 6}, {3, 5}};
    graph[3] = {{0, 15}, {1, 4}, {2, 5}};
    
    vector<int> key(V, INT_MAX);
    vector<bool> inMST(V, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    key[0] = 0;
    pq.push({0, 0});
    
    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();
        
        if (inMST[u]) continue;
        inMST[u] = true;
        
        for (auto [v, weight] : graph[u]) {
            if (!inMST[v] && weight < key[v]) {
                key[v] = weight;
                pq.push({weight, v});
            }
        }
    }
    
    int mstWeight = 0;
    for (int i = 0; i < V; i++) mstWeight += key[i];
    cout << "MST Weight: " << mstWeight << endl;
    
    return 0;
}
```

#### Time Complexity:
- **Using Binary Heap**: O(E log V)
- **Using Fibonacci Heap**: O(E + V log V)

---

### 2.5 Comparison: Kruskal's vs Prim's

| Aspect | Kruskal's | Prim's |
|--------|-----------|--------|
| Approach | Edge-based | Vertex-based |
| Data Structure | Disjoint Set | Priority Queue |
| Best For | Sparse graphs | Dense graphs |
| Initial State | No starting vertex | Arbitrary start vertex |
| Sorting Required | Yes | No |

---

## 3. Shortest Path Algorithms

### 3.1 Introduction

The **Shortest Path Problem** asks for the minimum distance (or cost) between a source vertex and one or all other vertices in a weighted graph. This is fundamental in navigation, routing, and network optimization.

---

### 3.2 Dijkstra's Algorithm

Dijkstra's Algorithm finds the shortest path from a source vertex to all other vertices in a graph with **non-negative** edge weights.

#### Algorithm Steps:
1. Initialize distances: source = 0, others = ∞
2. Mark all vertices as unvisited
3. Select unvisited vertex with minimum distance (source initially)
4. For the selected vertex, update distances to all neighbors
5. Mark current vertex as visited
6. Repeat until all vertices visited or destination reached

#### Key Properties:
- **Greedy approach**: Always picks the vertex with minimum distance
- **Works only with non-negative weights**
- **Guarantees optimal solution**

#### Detailed Example:

```
        4
    A -------- B
    | \        |
   2|  \1     |3
    |   \     |
    |    \    |
    C ---- D
        5
```

**Starting from A:**

| Step | Current | A | B | C | D |
|------|---------|---|---|---|---|
| Initial | - | 0 | ∞ | ∞ | ∞ |
| 1 | A | 0 | 4 (A→B) | 2 (A→C) | 1 (A→D) |
| 2 | D | 0 | 4 | 2 | 1 |
| 3 | C | 0 | 4 | 2 | 3 (C→D) |
| 4 | B | 0 | 4 | 2 | 3 |

**Shortest Paths from A:**
- A → B: 4
- A → C: 2
- A → D: 1

#### C++ Implementation:

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

int main() {
    int V = 5, src = 0;
    vector<vector<pair<int, int>>> graph(V);
    
    graph[0] = {{1, 4}, {2, 2}, {3, 1}};
    graph[1] = {{3, 3}, {4, 5}};
    graph[2] = {{3, 3}, {4, 1}};
    graph[3] = {{4, 2}};
    graph[4] = {};
    
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});
    
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        
        if (d > dist[u]) continue;
        
        for (auto [v, weight] : graph[u]) {
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    
    cout << "Shortest distances from " << src << ":\n";
    for (int i = 0; i < V; i++) 
        cout << i << ": " << dist[i] << endl;
    
    return 0;
}
```

#### Time Complexity:
- **Using Binary Heap**: O((V + E) log V)
- **Using Fibonacci Heap**: O(E + V log V)

---

### 3.3 Bellman-Ford Algorithm

Bellman-Ford algorithm finds shortest paths from a source to all vertices, **even with negative edge weights**. It can also detect negative weight cycles.

#### Algorithm Steps:
1. Initialize distances: source = 0, others = ∞
2. Relax all edges V-1 times (V = number of vertices)
3. Optionally, check for negative weight cycles by one more relaxation

#### Key Properties:
- **Handles negative weights** (unlike Dijkstra)
- **Can detect negative weight cycles**
- **Time complexity**: O(VE)

#### Detailed Example:

```
        4
    A -------- B
    | \       /|
   -2\     /-3|
    |   \ /   |
    |    X    |
    |   / \   |
   5/     \-1 |
    |       \ |
    C -------- D
        2
```

**Starting from A:**

| Iteration | A | B | C | D |
|-----------|---|---|---|---|
| Initial | 0 | ∞ | ∞ | ∞ |
| 1 | 0 | 4 | -2 (A→C) | 1 (A→D) |
| 2 | 0 | 4 | -2 | 0 (C→D) |
| 3 | 0 | 4 | -2 | 0 |
| 4 | 0 | 4 | -2 | 0 |

**Final Shortest Paths:**
- A → B: 4
- A → C: -2
- A → D: 0

#### C++ Implementation:

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Edge {
    int src, dest, weight;
};

int main() {
    int V = 5, E = 8, src = 0;
    vector<Edge> edges = {
        {0, 1, 4}, {0, 2, -2}, {0, 3, 1},
        {1, 3, 3}, {2, 1, -1}, {2, 3, 2},
        {3, 4, 5}, {2, 4, 1}
    };
    
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;
    
    // Relax all edges V-1 times
    for (int i = 0; i < V - 1; i++) {
        for (auto e : edges) {
            if (dist[e.src] != INT_MAX && dist[e.src] + e.weight < dist[e.dest]) {
                dist[e.dest] = dist[e.src] + e.weight;
            }
        }
    }
    
    // Check for negative weight cycles
    bool hasNegativeCycle = false;
    for (auto e : edges) {
        if (dist[e.src] != INT_MAX && dist[e.src] + e.weight < dist[e.dest]) {
            hasNegativeCycle = true;
            break;
        }
    }
    
    cout << "Shortest distances from " << src << ":\n";
    for (int i = 0; i < V; i++) 
        cout << i << ": " << dist[i] << endl;
    cout << "Negative cycle: " << (hasNegativeCycle ? "Yes" : "No") << endl;
    
    return 0;
}
```

#### Comparison: Dijkstra vs Bellman-Ford

| Aspect | Dijkstra | Bellman-Ford |
|--------|----------|--------------|
| Time Complexity | O(E log V) | O(VE) |
| Negative Weights | Not supported | Supported |
| Negative Cycles | Not detected | Detected |
| Greedy | Yes | No (dynamic programming) |

---

## 4. Real-World Applications

### 4.1 MST Applications
- **Road Network Design**: Minimum cost to connect all cities
- **Telecommunication Networks**: Cable TV, telephone networks
- **Electrical Grids**: Power distribution
- **Cluster Analysis**: Data mining

### 4.2 Shortest Path Applications
- **GPS Navigation**: Route planning
- **Network Routing**: Internet packet routing
- **Flight Schedules**: Airline route optimization
- **Game Development**: Pathfinding

---

## 5. Key Takeaways

1. **Greedy Algorithms** make locally optimal choices hoping for global optimality
2. **MST** connects all vertices with minimum total edge weight
3. **Kruskal's Algorithm**: Sort edges, add non-cyclic edges (O(E log V))
4. **Prim's Algorithm**: Grow tree from arbitrary vertex (O(E log V))
5. **Dijkstra's Algorithm**: Non-negative shortest paths (O(E log V))
6. **Bellman-Ford Algorithm**: Handles negative weights, detects negative cycles (O(VE))
7. Greedy doesn't always work - check optimal substructure property
8. Dijkstra fails with negative weights; use Bellman-Ford instead

---

## 6. Assessment Section

### 6.1 Multiple Choice Questions

**Q1.** In Kruskal's algorithm, the edges are processed in:
- a) Descending order of weight
- b) Random order
- c) Ascending order of weight ✓
- d) Graph traversal order

**Q2.** Which algorithm is used to find MST in dense graphs?
- a) Kruskal's
- b) Prim's ✓
- c) Dijkstra's
- d) Bellman-Ford

**Q3.** Dijkstra's algorithm fails when:
- a) Graph has cycles
- b) Graph has negative edge weights ✓
- c) Graph is disconnected
- d) Source vertex is isolated

**Q4.** The time complexity of Bellman-Ford algorithm is:
- a) O(V log E)
- b) O(E log V)
- c) O(VE) ✓
- d) O(V²)

**Q5.** A spanning tree has exactly how many edges (for V vertices)?
- a) V
- b) V + 1
- c) V - 1 ✓
- d) V²

**Q6.** Which data structure is commonly used in Prim's algorithm?
- a) Stack
- b) Queue
- c) Priority Queue ✓
- d) Linked List

**Q7.** Bellman-Ford can detect:
- a) Positive weight cycles only
- b) Zero weight cycles only
- c) Negative weight cycles ✓
- d) No cycles

**Q8.** The greedy choice property means:
- a) Making random choices
- b) Making locally optimal choices leads to global optimum ✓
- c) Always choosing the maximum
- d) Backtracking after failure

**Q9.** Which algorithm is not greedy?
- a) Kruskal's
- b) Prim's
- c) Bellman-Ford ✓
- d) Dijkstra's

**Q10.** In Dijkstra's algorithm, once a vertex is marked as visited:
- a) It can be visited again
- b) Its distance is final ✓
- c) It is removed permanently
- d) Both b and c

### 6.2 Flashcards

| Term | Definition |
|------|------------|
| **Greedy Algorithm** | A problem-solving approach that makes locally optimal choices at each step |
| **MST** | Minimum Spanning Tree - connects all vertices with minimum total edge weight |
| **Kruskal's Algorithm** | MST algorithm that sorts edges and adds non-cyclic edges |
| **Prim's Algorithm** | MST algorithm that grows tree from arbitrary vertex using priority queue |
| **Dijkstra's Algorithm** | Shortest path algorithm for non-negative weights using greedy approach |
| **Bellman-Ford Algorithm** | Shortest path algorithm that handles negative weights and detects negative cycles |
| **Optimal Substructure** | Property where optimal solution contains optimal solutions to subproblems |
| **Cycle** | A path that starts and ends at the same vertex without repeating edges |
| **Disjoint Set Union (DSU)** | Data structure for tracking set membership, used in Kruskal's algorithm |
| **Relaxation** | Process of updating distance values when a shorter path is found |

### 6.3 Short Answer Questions

**Q1.** Explain why Dijkstra's algorithm fails with negative edge weights.
> Dijkstra's algorithm assumes that once a vertex is visited with minimum distance, it cannot be improved. However, with negative weights, a later path through an unvisited vertex might provide a shorter route to already-visited vertices.

**Q2.** Compare Kruskal's and Prim's algorithms with respect to data structures used.
> Kruskal's uses Disjoint Set Union (DSU) to track connected components, while Prim's uses Priority Queue to efficiently select minimum weight edge connecting MST to non-MST vertices.

**Q3.** Why does Bellman-Ford run V-1 iterations to find shortest paths?
> In a graph without negative cycles, the shortest path between any two vertices can have at most V-1 edges. Each iteration relaxes all edges, progressively finding paths with more edges.

### 6.4 Application-Based Questions

**Q1.** Design a network topology for connecting 5 offices with minimum cable cost. Which algorithm would you use and why?
> For 5 offices with given cable costs between each pair, I would use Prim's algorithm if the graph is dense (many possible connections), or Kruskal's if sparse. Prim's is preferred for dense graphs as it builds the tree vertex by vertex, which is intuitive for network design.

**Q2.** In a GPS navigation system, why might Dijkstra's algorithm be preferred over Bellman-Ford?
> GPS navigation typically deals with road networks that have non-negative weights (distances/costs). Dijkstra's algorithm is faster O(E log V) compared to Bellman-Ford's O(VE), making it more suitable for real-time navigation.

**Q3.** How would you modify Dijkstra's algorithm to find the shortest path to a specific destination rather than all vertices?
> Terminate the algorithm once the destination vertex is extracted from the priority queue. At that point, we have found the shortest path to the destination.

---

## 7. Delhi University NEP 2024 Context

This topic aligns with **GE7A: Design and Analysis of Algorithms** under the NEP 2024 curriculum for BSc Physical Science (CS). Students should focus on:

- Understanding greedy approach fundamentals
- Implementing MST algorithms (Kruskal's and Prim's)
- Mastering shortest path algorithms (Dijkstra and Bellman-Ford)
- Analyzing time and space complexities
- Solving problems with proper algorithmic thinking

**Recommended Practice Problems:**
1. Implement MST using both Kruskal's and Prim's
2. Solve shortest path problems on various graph types
3. Compare algorithm performance on different input sizes

---

*End of Study Material*