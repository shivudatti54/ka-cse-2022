# Graph Traversals and Topological Sort

## Comprehensive Study Material for Ge7A: Design and Analysis of Algorithms

**BSc Physical Science (CS) - Delhi University, NEP 2024**

---

## 1. Introduction

Graphs are fundamental data structures in computer science that model relationships between objects. Whether it's finding the shortest path in a navigation system, determining the order of tasks in a project, or analyzing social network connections, graph algorithms form the backbone of many real-world applications.

In this study material, we will explore **Graph Traversals** (specifically Depth-First Search and Breadth-First Search) and **Topological Sort** — two essential techniques covered under Unit 3 of the Delhi University syllabus for Design and Analysis of Algorithms (Ge7A). These concepts are not only crucial for understanding advanced graph algorithms but also have direct applications in scheduling, dependency resolution, and network analysis.

---

## 2. Graph Fundamentals Review

Before diving into traversals, let's establish key terminology:

- **Vertex (V)**: A node in the graph
- **Edge (E)**: A connection between two vertices
- **Directed Graph**: Edges have a specific direction
- **Undirected Graph**: Edges have no direction
- **Weighted Graph**: Edges have associated weights/costs
- **Adjacency List**: Array of lists storing neighbors for each vertex
- **Adjacency Matrix**: 2D matrix where matrix[i][j] indicates edge existence

---

## 3. Depth First Search (DFS)

### 3.1 Concept and Overview

**Depth First Search** is a graph traversal algorithm that explores as deep as possible along each branch before backtracking. It uses a **stack** (either explicitly or via recursion) to keep track of vertices to visit.

### 3.2 Algorithm Explanation

The DFS algorithm works as follows:

1. Start at a chosen source vertex
2. Mark the current vertex as **visited**
3. Process the current vertex (e.g., print it)
4. For each adjacent (unvisited) vertex, recursively perform DFS

### 3.3 Pseudocode

```
DFS(graph G, vertex v):
    mark v as visited
    process(v)  // e.g., print v
    
    for each adjacent vertex u of v:
        if u is not visited:
            DFS(G, u)

// For traversing entire graph (if disconnected)
DFS_Complete(graph G):
    for each vertex v in G:
        if v is not visited:
            DFS(G, v)
```

### 3.4 Step-by-Step Execution Example

Consider this directed graph:

```
    A → B → C
    ↓   ↓   ↓
    D → E → F
```

**Execution Steps:**

| Step | Current Vertex | Action | Visited Set |
|------|---------------|--------|-------------|
| 1 | A | Visit A, push neighbors | {A} |
| 2 | B | Visit B (neighbor of A) | {A, B} |
| 3 | C | Visit C (neighbor of B) | {A, B, C} |
| 4 | Backtrack | No unvisited neighbors of C | {A, B, C} |
| 5 | E | Visit E (neighbor of B) | {A, B, C, E} |
| 6 | F | Visit F (neighbor of E) | {A, B, C, E, F} |
| 7 | D | Visit D (neighbor of A) | {A, B, C, E, F, D} |

**DFS Traversal Order**: A → B → C → E → F → D

### 3.5 Implementation in Python

```python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' → ')
        
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)
    
    def dfs(self, start):
        visited = set()
        print("DFS Traversal:", end=" ")
        self.dfs_util(start, visited)
        print("END")

# Example usage
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'D')
g.add_edge('B', 'C')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('D', 'E')
g.add_edge('E', 'F')

g.dfs('A')
```

**Output**: `DFS Traversal: A → B → C → F → E → D → END`

### 3.6 Time and Space Complexity

- **Time Complexity**: O(V + E) — each vertex and edge is visited once
- **Space Complexity**: O(V) — for visited set and recursion stack

### 3.7 Applications of DFS

1. **Detecting cycles** in graphs
2. **Path finding** between two vertices
3. **Topological sorting**
4. **Solving puzzles** with only one solution (e.g., maze solving)
5. **Finding strongly connected components**
6. **Web crawling** by search engines

---

## 4. Breadth First Search (BFS)

### 4.1 Concept and Overview

**Breadth First Search** explores all vertices at the present depth before moving to vertices at the next depth level. It uses a **queue** data structure to ensure FIFO (First In, First Out) processing.

### 4.2 Algorithm Explanation

1. Start at a chosen source vertex
2. Mark the source as visited and enqueue it
3. While the queue is not empty:
   - Dequeue a vertex
   - Process the vertex
   - Enqueue all unvisited adjacent vertices

### 4.3 Pseudocode

```
BFS(graph G, vertex s):
    mark s as visited
    enqueue s into queue Q
    
    while Q is not empty:
        v = dequeue from Q
        process(v)
        
        for each adjacent vertex u of v:
            if u is not visited:
                mark u as visited
                enqueue u into Q
```

### 4.4 Step-by-Step Execution Example

Using the same graph as DFS:

```
    A → B → C
    ↓   ↓   ↓
    D → E → F
```

**Execution Steps:**

| Step | Queue (Front → Rear) | Dequeued | Visited After |
|------|---------------------|----------|---------------|
| 1 | [A] | - | {A} |
| 2 | [B, D] | A | {A, B, D} |
| 3 | [D, C, E] | B | {A, B, D, C, E} |
| 4 | [C, E, F] | D | {A, B, D, C, E, F} |
| 5 | [E, F] | C | {A, B, D, C, E, F} |
| 6 | [F, E] | E | {A, B, D, C, E, F} |
| 7 | [E] | F | {A, B, D, C, E, F} |
| 8 | [] | E | Complete |

**BFS Traversal Order**: A → B → D → C → E → F

### 4.5 Implementation in Python

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        print("BFS Traversal:", " → ".join(result))

# Example usage
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'D')
g.add_edge('B', 'C')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('D', 'E')
g.add_edge('E', 'F')

g.bfs('A')
```

**Output**: `BFS Traversal: A → B → D → C → E → F`

### 4.6 Time and Space Complexity

- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V) — for visited set and queue

### 4.7 Applications of BFS

1. **Finding shortest path** in unweighted graphs
2. **Level-order traversal** in trees
3. **Finding connected components**
4. **Social network friend suggestions** (degree of separation)
5. **GPS navigation systems** (shortest distance)
6. **Broadcasting in networks**

---

## 5. BFS vs DFS: A Comprehensive Comparison

| Aspect | BFS | DFS |
|--------|-----|-----|
| **Data Structure** | Queue | Stack (or Recursion) |
| **Exploration Pattern** | Level by level | Depth first |
| **Time Complexity** | O(V + E) | O(V + E) |
| **Space Complexity** | O(V) | O(V) |
| **Path Found** | Shortest (unweighted) | Any path |
| **Memory Usage** | Higher for wide graphs | Higher for deep graphs |
| **Optimal For** | Shortest path, level-order | Cycle detection, topological sort |

---

## 6. Topological Sort

### 6.1 Introduction and Importance

**Topological Sort** is a linear ordering of vertices in a **directed acyclic graph (DAG)** such that for every directed edge (u, v), vertex u comes before vertex v in the ordering.

**Why is this important?**

Consider these real-world scenarios:
- **Course prerequisites**: You must complete prerequisites before advanced courses
- **Build systems**: Compile dependencies in correct order
- **Task scheduling**: Order tasks that depend on each other
- **Instruction scheduling**: CPU pipeline optimization

### 6.2 Key Property

A topological sort is **only possible** if the graph is a **DAG** (Directed Acyclic Graph — contains no cycles). This makes cycle detection essential before performing topological sort.

### 6.3 Topological Sort using DFS

**Algorithm:**

1. Perform DFS on the graph
2. Push vertices to a stack **after** all their neighbors are visited (post-order)
3. Pop elements from stack to get topological order

**Pseudocode:**

```
TopologicalSort_DFS(graph G):
    visited = set()
    stack = []
    
    for each vertex v in G:
        if v not in visited:
            topological_sort_util(v, visited, stack)
    
    while stack is not empty:
        print(stack.pop())

topological_sort_util(v, visited, stack):
    visited.add(v)
    
    for each adjacent vertex u of v:
        if u not in visited:
            topological_sort_util(u, visited, stack)
    
    stack.push(v)
```

### 6.4 Topological Sort using BFS (Kahn's Algorithm)

This algorithm uses the concept of **in-degree** (number of incoming edges).

**Algorithm:**

1. Calculate in-degree for all vertices
2. Add all vertices with in-degree 0 to queue
3. While queue is not empty:
   - Remove vertex from queue, add to result
   - Reduce in-degree of all neighbors
   - If any neighbor's in-degree becomes 0, add to queue

**Pseudocode:**

```
TopologicalSort_Kahn(graph G):
    in_degree = array of size V, initialized to 0
    
    for each vertex u in G:
        for each vertex v in G.adj[u]:
            in_degree[v] += 1
    
    queue = []
    for each vertex v in G:
        if in_degree[v] == 0:
            queue.enqueue(v)
    
    result = []
    while queue is not empty:
        u = queue.dequeue()
        result.append(u)
        
        for each vertex v in G.adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.enqueue(v)
    
    if result.length != V:
        print("Graph has a cycle!")
        return empty
    
    return result
```

### 6.5 Step-by-Step Example

Consider this course prerequisite graph:

```
    CS101 → CS201 → CS301
      ↓        ↓
    MATH    DBMS
```

**Vertices**: CS101, CS201, CS301, MATH, DBMS
**Edges**: (CS101→CS201), (CS101→MATH), (CS201→CS301), (CS201→DBMS)

**Using Kahn's Algorithm:**

| Step | Queue | In-degrees | Result |
|------|-------|-----------|--------|
| Initial | [CS101, MATH] | CS201:1, CS301:1, DBMS:1, others:0 | [] |
| 1 | [MATH] | CS101 removed, no changes | [CS101] |
| 2 | [] | MATH removed, no changes | [CS101, MATH] |
| 3 | [CS201] | DBMS:0 now (in-degree reduced) | [CS101, MATH, CS201] |
| 4 | [DBMS] | CS301:0 now | [CS101, MATH, CS201, DBMS] |
| 5 | [CS301] | All processed | [CS101, MATH, CS201, DBMS, CS301] |

**Topological Order**: CS101 → MATH → CS201 → DBMS → CS301

### 6.6 Implementation in Python (Kahn's Algorithm)

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def topological_sort(self):
        in_degree = [0] * self.V
        
        # Calculate in-degrees
        for u in range(self.V):
            for v in self.graph[u]:
                in_degree[v] += 1
        
        # Queue for vertices with in-degree 0
        queue = deque()
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        count = 0
        
        while queue:
            u = queue.popleft()
            result.append(u)
            count += 1
            
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        if count != self.V:
            print("Error: Graph contains a cycle!")
            return []
        
        return result

# Example usage (using vertex indices)
g = Graph(6)
g.add_edge(0, 1)  # CS101 → CS201
g.add_edge(0, 3)  # CS101 → MATH
g.add_edge(1, 2)  # CS201 → CS301
g.add_edge(1, 4)  # CS201 → DBMS
g.add_edge(3, 4)  # MATH → DBMS

result = g.topological_sort()
print("Topological Sort:", result)
# Output: [0, 3, 1, 4, 2]
```

### 6.7 Cycle Detection Connection

An important property of topological sort is that **if the graph contains a cycle, topological sorting is impossible**. Kahn's algorithm inherently detects cycles:

- If the result contains fewer vertices than the graph has, a cycle exists
- This is because vertices in a cycle have non-zero in-degrees at all times

**Cycle Detection Applications:**
- **Deadlock detection** in operating systems
- **Dependency validation** in build systems
- **Prerequisite conflict detection** in course registration

---

## 7. Real-World Applications Summary

| Algorithm | Applications |
|-----------|--------------|
| **DFS** | Maze solving, path finding, cycle detection, topological sort, tree inorder/preorder/postorder traversal |
| **BFS** | Shortest path (unweighted), social network analysis, web crawling, level-order traversal, broadcasting |
| **Topological Sort** | Course scheduling, build systems (make), task ordering, package dependency resolution, instruction scheduling |

---

## 8. Key Takeaways

1. **Graph Traversals** are fundamental techniques for systematically visiting all vertices in a graph.

2. **DFS** explores deeply before backtracking, using a stack (recursion). It's ideal for path finding, cycle detection, and topological sorting.

3. **BFS** explores level by level, using a queue. It finds the shortest path in unweighted graphs.

4. **Topological Sort** orders vertices in a DAG such that all dependencies come before the dependent tasks.

5. **Cycle Detection** is intrinsically linked to topological sort — a valid ordering exists only if the graph is acyclic.

6. Both traversals have **O(V + E)** time complexity, making them efficient for large graphs.

7. **Kahn's Algorithm** (BFS-based) is often preferred for topological sorting due to its cycle detection capability.

---

## 9. Practice Questions: Multiple Choice

### Section A: Basic Concepts

1. **Which data structure does BFS use internally?**
   - (a) Stack
   - (b) Queue
   - (c) Heap
   - (d) Tree
   
   **Answer**: (b) Queue

2. **What is the time complexity of DFS and BFS?**
   - (a) O(V)
   - (b) O(E)
   - (c) O(V × E)
   - (d) O(V + E)
   
   **Answer**: (d) O(V + E)

3. **Which traversal guarantees the shortest path in an unweighted graph?**
   - (a) DFS
   - (b) BFS
   - (c) Both
   - (d) Neither
   
   **Answer**: (b) BFS

4. **A topological sort is possible only for:**
   - (a) Connected graphs
   - (b) Directed graphs
   - (c) DAGs
   - (d) Weighted graphs
   
   **Answer**: (c) DAGs

### Section B: Intermediate Questions

5. **In DFS, when is a vertex added to the output in topological sort?**
   - (a) When first discovered
   - (b) After visiting all neighbors (post-order)
   - (c) Before exploring neighbors
   - (d) Depends on the implementation
   
   **Answer**: (b) After visiting all neighbors

6. **Kahn's Algorithm uses which concept to determine ordering?**
   - (a) Out-degree
   - (b) In-degree
   - (c) Edge weights
   - (d) Connected components
   
   **Answer**: (b) In-degree

7. **How does Kahn's Algorithm detect cycles?**
   - (a) By checking for back edges
   - (b) If result contains fewer vertices than expected
   - (c) By using timestamps
   - (d) Cannot detect cycles
   
   **Answer**: (b) If result contains fewer vertices than expected

8. **Which algorithm is better for finding if two vertices are connected?**
   - (a) BFS only
   - (b) DFS only
   - (c) Either BFS or DFS
   - (d) Topological Sort only
   
   **Answer**: (c) Either BFS or DFS

### Section C: Advanced Application Questions

9. **Which of the following problems can be solved using DFS?**
   - (i) Detecting cycle in a graph
   - (ii) Finding shortest path
   - (iii) Topological sort
   - (iv) Finding connected components
   
   - (a) (i) and (ii) only
   - (b) (i), (iii), and (iv)
   - (c) (ii) and (iv) only
   - (d) All of the above
   
   **Answer**: (b) (i), (iii), and (iv)

10. **In a graph with V vertices and E edges represented using adjacency list, BFS requires how much extra space?**
    - (a) O(V)
    - (b) O(E)
    - (c) O(V + E)
    - (d) O(1)
    
    **Answer**: (a) O(V)

11. **Which traversal would you use to find the shortest path in a weighted graph with positive weights?**
    - (a) DFS
    - (b) BFS
    - (c) Dijkstra's Algorithm
    - (d) Topological Sort
    
    **Answer**: (c) Dijkstra's Algorithm

12. **What is the maximum recursion depth for DFS on a graph with V vertices?**
    - (a) O(log V)
    - (b) O(V)
    - (c) O(E)
    - (d) O(V + E)
    
    **Answer**: (b) O(V)

---

## 10. Flashcards for Quick Revision

| # | Term | Definition |
|---|------|------------|
| 1 | **Graph Traversal** | The process of visiting all vertices in a graph systematically |
| 2 | **DFS (Depth First Search)** | A traversal that explores as deep as possible before backtracking; uses stack |
| 3 | **BFS (Breadth First Search)** | A traversal that explores all neighbors at current depth before moving deeper; uses queue |
| 4 | **Topological Sort** | Linear ordering of vertices in a DAG where for every edge (u,v), u comes before v |
| 5 | **DAG** | Directed Acyclic Graph — a directed graph with no cycles |
| 6 | **In-degree** | Number of edges coming INTO a vertex |
| 7 | **Out-degree** | Number of edges going OUT from a vertex |
| 8 | **Kahn's Algorithm** | BFS-based topological sort using in-degree calculation |
| 9 | **Cycle Detection** | Finding whether a graph contains a directed cycle |
| 10 | **Adjacency List** | Graph representation using an array of lists (space-efficient for sparse graphs) |
| 11 | **Adjacency Matrix** | Graph representation using 2D matrix (O(1) edge lookup) |
| 12 | **Backtracking** | Returning to previous vertex in DFS when no unvisited neighbors remain |

---

## References

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. *Introduction to Algorithms* (CLRS)
- Delhi University B.Sc. (Hons.) Computer Science Syllabus, NEP 2024
- GeeksforGeeks — Graph Algorithms Tutorial

---

*End of Study Material*