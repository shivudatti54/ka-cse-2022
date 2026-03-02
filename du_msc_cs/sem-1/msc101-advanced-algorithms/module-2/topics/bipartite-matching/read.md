# Comprehensive Study Material: Bipartite Matching

## Advanced Algorithms — MSc CS, Delhi University

---

## 1. Introduction

**Bipartite Matching** is a fundamental problem in graph theory and combinatorial optimization that deals with finding the maximum possible pairing between two disjoint sets of elements under specific constraints. This topic holds significant importance in the Advanced Algorithms syllabus for MSc CS students at Delhi University, particularly in the context of practical applications ranging from job assignments to college admissions, from online dating platforms to resource allocation in distributed systems.

### Real-World Relevance

The applications of bipartite matching are pervasive across multiple domains:

- **Job Placement**: Matching candidates to job openings based on qualifications
- **College Admissions**: Assigning students to courses or colleges based on preferences and seat availability
- **Ride-Sharing**: Matching drivers with passengers
- **Online Dating Platforms**: Pairing users based on mutual preferences
- **Medical Residency**: Assigning medical graduates to hospitals
- **Resource Allocation**: Distributing resources in cloud computing and networking

Understanding bipartite matching equips computer scientists with tools to solve real-world assignment problems efficiently.

---

## 2. Basic Definitions

### 2.1 Bipartite Graph

A **bipartite graph** $G = (V, E)$ is a graph whose vertex set $V$ can be partitioned into two disjoint sets $L$ and $R$ such that every edge $e \in E$ connects a vertex in $L$ to a vertex in $R$. Formally:

$$V = L \cup R \text{ and } L \cap R = \emptyset$$
$$\forall (u, v) \in E: (u \in L \land v \in R) \text{ or } (u \in R \land v \in L)$$

**Example**: Consider a graph with set $L = \{A, B, C\}$ (job seekers) and set $R = \{1, 2, 3\}$ (jobs). An edge exists if a job seeker is qualified for a particular job.

### 2.2 Matching

A **matching** $M \subseteq E$ is a set of edges such that no two edges share a vertex. In other words, each vertex is incident to at most one edge in $M$.

- **Matched Vertex**: A vertex that is incident to an edge in the matching
- **Unmatched Vertex**: A vertex not incident to any edge in the matching

### 2.3 Maximum Matching

A **maximum matching** (or **maximum cardinality matching**) is a matching that contains the maximum possible number of edges. It is denoted by $|M_{max}|$.

### 2.4 Perfect Matching

A **perfect matching** is a matching that matches all vertices in the graph. For a bipartite graph with $|L| = |R| = n$, a perfect matching contains exactly $n$ edges.

### 2.5 Complete Bipartite Graph

A complete bipartite graph $K_{m,n}$ is a bipartite graph where every vertex in set $L$ (of size $m$) is connected to every vertex in set $R$ (of size $n$). The total number of edges is $m \times n$.

---

## 3. Hall's Marriage Theorem

Hall's Marriage Theorem (also known as Hall's Theorem) provides a necessary and sufficient condition for the existence of a perfect matching in a bipartite graph. This theorem is fundamental to understanding the theoretical underpinnings of bipartite matching.

### Theorem Statement

Let $G = (L \cup R, E)$ be a bipartite graph. There exists a perfect matching that matches every vertex in $L$ to a distinct vertex in $R$ **if and only if** for every subset $S \subseteq L$, the number of neighbors of $S$ (denoted $N(S)$) satisfies:

$$|N(S)| \geq |S|$$

This condition is called **Hall's condition**.

### Intuition

For any subset $S$ of job seekers, there must be at least as many available jobs as job seekers in $S$. If this holds for all subsets, a perfect matching exists.

### Corollary: Existence of Maximum Matching

A matching of size $|L|$ exists if and only if Hall's condition holds. More generally, the size of a maximum matching equals $|L| - \max_{S \subseteq L}(|S| - |N(S)|)$.

### Example Application

Consider $L = \{a, b, c\}$ and $R = \{1, 2, 3, 4\}$ with edges:
- $a$ connected to: $\{1, 2\}$
- $b$ connected to: $\{2, 3\}$
- $c$ connected to: $\{3, 4\}$

Check Hall's condition:
- $S = \{a\}: |N(S)| = 2 \geq 1$ ✓
- $S = \{b\}: |N(S)| = 2 \geq 1$ ✓
- $S = \{c\}: |N(S)| = 2 \geq 1$ ✓
- $S = \{a, b\}: |N(S)| = |\{1, 2, 3\}| = 3 \geq 2$ ✓
- $S = \{a, c\}: |N(S)| = |\{1, 2, 3, 4\}| = 4 \geq 2$ ✓
- $S = \{b, c\}: |N(S)| = |\{2, 3, 4\}| = 3 \geq 2$ ✓
- $S = \{a, b, c\}: |N(S)| = |\{1, 2, 3, 4\}| = 4 \geq 3$ ✓

Since Hall's condition holds, a perfect matching exists.

---

## 4. Augmenting Paths

An **augmenting path** is a critical concept in matching algorithms. It is a path that starts at an unmatched vertex in $L$, ends at an unmatched vertex in $R$, and alternates between unmatched and matched edges.

### Definition

Given a matching $M$, an **augmenting path** $P$ is a path in $G$ such that:
1. The starting vertex is unmatched in $L$
2. The ending vertex is unmatched in $R$
3. Edges alternate between being in $M$ and not in $M$

### Key Theorem (Berge's Lemma)

A matching $M$ is maximum if and only if there is no augmenting path with respect to $M$.

### Augmenting the Matching

If an augmenting path exists, we can **augment** the matching by:
- Removing all matched edges from the path
- Adding all unmatched edges from the path

This operation increases the matching size by exactly 1.

---

## 5. Kuhn's Algorithm (Brute Force DFS Approach)

Kuhn's Algorithm (also called the Hungarian Algorithm for bipartite matching in its basic form, though this name is more commonly associated with assignment problems) is a simple depth-first search based algorithm for finding maximum matching in bipartite graphs.

### Algorithm Description

The algorithm repeatedly attempts to find augmenting paths for each vertex in the left set $L$:

1. For each unmatched vertex $u$ in $L$:
   - Run DFS to find an augmenting path starting from $u$
   - If found, augment the matching

### Time Complexity

- **Worst-case**: $O(VE)$ — Each vertex attempts at most $O(V)$ augmentations, each taking $O(E)$ time
- In practice: $O(VE)$ works well for small to medium graphs

### Pseudocode

```
function Kuhn(u):
    if visited[u]:
        return false
    visited[u] = true
    
    for each v in Adj[u]:
        if matchR[v] == -1 or Kuhn(matchR[v]):
            matchR[v] = u
            return true
    
    return false

function findMaximumMatching():
    matchR = array of size |R| initialized to -1
    result = 0
    
    for u in L:
        visited = array of size |L| initialized to false
        if Kuhn(u):
            result += 1
    
    return result
```

### Code Implementation (Python)

```python
from collections import defaultdict

def kuhn_algorithm(adj, n_left, n_right):
    """
    Kuhn's Algorithm for Maximum Bipartite Matching
    
    Args:
        adj: Dictionary mapping left vertices to list of right vertices
        n_left: Number of vertices in left set
        n_right: Number of vertices in right set
    
    Returns:
        Size of maximum matching
    """
    match_right = [-1] * n_right  # Which left vertex is matched to right vertex
    
    def dfs(u, visited):
        if visited[u]:
            return False
        visited[u] = True
        
        for v in adj.get(u, []):
            # If v is unmatched or we can find augmenting path
            if match_right[v] == -1 or dfs(match_right[v], visited):
                match_right[v] = u
                return True
        return False
    
    result = 0
    for u in range(n_left):
        visited = [False] * n_left
        if dfs(u, visited):
            result += 1
    
    return result, match_right

# Example
if __name__ == "__main__":
    # Graph: L = {0, 1, 2}, R = {0, 1, 2, 3}
    # Edges: 0->{0,1}, 1->{1,2}, 2->{2,3}
    adj = {
        0: [0, 1],
        1: [1, 2],
        2: [2, 3]
    }
    
    max_matching, match_right = kuhn_algorithm(adj, 3, 4)
    print(f"Maximum Matching Size: {max_matching}")
    print(f"Matching: {match_right}")
```

**Output:**
```
Maximum Matching Size: 3
Matching: [0, 1, 2, -1]
```

---

## 6. Hopcroft-Karp Algorithm

The Hopcroft-Karp algorithm is an efficient algorithm for finding maximum matching in bipartite graphs. It significantly improves upon Kuhn's algorithm by finding multiple augmenting paths simultaneously using a layered graph approach.

### Key Ideas

1. **BFS Layering**: Build a layered graph to find vertex-disjoint shortest augmenting paths
2. **DFS Phase**: Find all vertex-disjoint shortest augmenting paths in the layered graph
3. **Augment**: Augment along all found paths simultaneously
4. **Repeat** until no augmenting path exists

### Time Complexity

$$O(\sqrt{V} \cdot E)$$

This is significantly better than Kuhn's $O(VE)$ for dense graphs.

### Algorithm Steps

1. **Initialize**: Match = ∅
2. **BFS Phase**: 
   - Start BFS from all free (unmatched) vertices in $L$
   - Build distance labels for vertices in $L$
   - Stop when free vertices in $R$ are reached
   - Create layers: Level 0 = free L vertices, alternating levels
3. **DFS Phase**:
   - Find all vertex-disjoint shortest augmenting paths using DFS
   - Only traverse edges that respect the layer structure (lead to next layer)
4. **Augment**: For each found augmenting path, flip matched/unmatched status
5. **Repeat** BFS and DFS until no augmenting path exists

### Pseudocode

```
function HopcroftKarp(L, R, E):
    matching = ∅
    while true:
        // BFS to build layers
        queue = all free vertices in L
        dist = dict()
        for u in L:
            dist[u] = 0
        dist[NULL] = ∞
        
        while queue not empty:
            u = queue.pop()
            if dist[u] < dist[NULL]:
                for v in Adj[u]:
                    if dist[matchR[v]] == ∞:
                        dist[matchR[v]] = dist[u] + 1
                        queue.push(matchR[v])
        
        if dist[NULL] == ∞:
            break  // No augmenting path exists
        
        // DFS to find augmenting paths
        function dfs(u):
            if u != NULL:
                for v in Adj[u]:
                    if dist[matchR[v]] == dist[u] + 1 and dfs(matchR[v]):
                        matchR[v] = u
                        return True
                dist[u] = ∞
                return False
            return true
        
        for u in L:
            if matching does not include u:
                visited = set()
                if dfs(u):
                    add edge (u, matchR[u]) to matching
    
    return matching
```

### Code Implementation (Python)

```python
from collections import deque, defaultdict

def hopcroft_karp(adj, n_left, n_right):
    """
    Hopcroft-Karp Algorithm for Maximum Bipartite Matching
    
    Args:
        adj: Dictionary mapping left vertices to list of right vertices
        n_left: Number of vertices in left set
        n_right: Number of vertices in right set
    
    Returns:
        Size of maximum matching
    """
    INF = float('inf')
    
    # pairU[u] = matched right vertex for left vertex u, or -1 if unmatched
    # pairV[v] = matched left vertex for right vertex v, or -1 if unmatched
    pair_u = [-1] * n_left
    pair_v = [-1] * n_right
    dist = [0] * n_left
    
    def bfs():
        queue = deque()
        
        # Initialize distances for all free vertices in U
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        
        # Distance to NIL (conceptual node)
        dist_nil = INF
        
        while queue:
            u = queue.popleft()
            
            # If we found a shorter path to NIL, update
            if dist[u] < dist_nil:
                for v in adj.get(u, []):
                    # If v is unmatched, dist_nil = dist[u] + 1
                    if pair_v[v] == -1:
                        dist_nil = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        
        return dist_nil != INF
    
    def dfs(u):
        for v in adj.get(u, []):
            # If v is matched and we can continue the alternating path
            if pair_v[v] == -1 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        
        # Mark u as unreachable for future searches
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        # Try to find augmenting path from each free vertex in U
        for u in range(n_left):
            if pair_u[u] == -1:
                if dfs(u):
                    matching += 1
    
    return matching, pair_u, pair_v

# Example with a more complex graph
if __name__ == "__main__":
    # Larger bipartite graph example
    # Left: 5 vertices {0,1,2,3,4}, Right: 5 vertices {0,1,2,3,4}
    adj = {
        0: [0, 1, 2],
        1: [0, 1],
        2: [1, 2, 3],
        3: [2, 3, 4],
        4: [3, 4]
    }
    
    max_matching, pair_u, pair_v = hopcroft_karp(adj, 5, 5)
    print(f"Maximum Matching Size: {max_matching}")
    print(f"Left-Right Pairs: {[(u, pair_u[u]) for u in range(5) if pair_u[u] != -1]}")
```

**Output:**
```
Maximum Matching Size: 5
Left-Right Pairs: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
```

---

## 7. Minimum Vertex Cover and Kőnig's Theorem

The **Minimum Vertex Cover** problem and its relationship to maximum matching is a crucial topic covered in the Delhi University syllabus.

### Definition

A **vertex cover** of a graph $G = (V, E)$ is a subset $C \subseteq V$ such that every edge $e \in E$ has at least one endpoint in $C$. A **minimum vertex cover** is a vertex cover with the smallest possible size.

### Kőnig's Theorem

For bipartite graphs, the following equality holds:

> **Kőnig's Theorem**: In any bipartite graph, the size of a maximum matching equals the size of a minimum vertex cover.

This is a fundamental result that connects two classic optimization problems.

### Relationship with Maximum Matching

If $M$ is a maximum matching and $C$ is a minimum vertex cover, then:

$$|M| = |C|$$

Furthermore, from any maximum matching, we can construct a minimum vertex cover using the following algorithm:

1. Find all vertices reachable from unmatched vertices in $L$ via alternating paths
2. Let $Z$ be the set of all vertices reachable
3. The minimum vertex cover is: $(L \setminus Z) \cup (R \cap Z)$

### Proof Sketch

- Every edge in $M$ has exactly one endpoint in the vertex cover (by definition)
- No edge in $E \setminus M$ has both endpoints outside the cover
- The constructed cover has exactly $|M|$ vertices

### Example

Consider the bipartite graph with $L = \{a, b, c\}$ and $R = \{1, 2, 3\}$ with edges $a-1, a-2, b-2, b-3, c-3$.

Maximum matching size = 3 (edges: $a-1, b-2, c-3$)

Minimum vertex cover size = 3 (for example: $\{a, b, c\}$ or $\{1, 2, 3\}$)

---

## 8. Applications of Bipartite Matching

### 8.1 Assignment Problem

The classic assignment problem can be reduced to finding a perfect matching in a bipartite graph where each left vertex (worker) is connected to right vertices (jobs) with edge weights representing costs or profits.

### 8.2 Online Dating Platforms

Matching users based on mutual preferences reduces to bipartite matching where edges represent mutual interest.

### 8.3 Network Flow

Bipartite matching can be modeled as a maximum flow problem in a flow network with source connected to all left vertices, all right vertices connected to sink, and capacity 1 on all edges.

### 8.4 Course Allocation

In universities, matching students to courses where each student can select multiple preferred courses and each course has capacity constraints.

---

## 9. Comparison of Algorithms

| Algorithm | Time Complexity | Space Complexity | Best For |
|-----------|-----------------|------------------|----------|
| Kuhn's Algorithm | $O(VE)$ | $O(V)$ | Small graphs, simple implementation |
| Hopcroft-Karp | $O(\sqrt{V}E)$ | $O(V)$ | Large dense graphs |
| Ford-Fulkerson (as flow) | $O(VE)$ | $O(V)$ | When integrated with flow networks |

---

## 10. Multiple Choice Questions

### MCQ 1: Hall's Theorem
For a bipartite graph with left set size 5 and right set size 7, which condition is necessary and sufficient for a matching that matches all 5 vertices in the left set?

A) Every vertex in L has at least one neighbor
B) For every subset S of L, |N(S)| ≥ |S|
C) The graph is complete bipartite
D) |E| ≥ 5

**Answer: B** — Hall's condition states that for every subset S ⊆ L, |N(S)| ≥ |S|.

---

### MCQ 2: Hopcroft-Karp Time Complexity
What is the time complexity of the Hopcroft-Karp algorithm for finding maximum matching in a bipartite graph?

A) O(V²)
B) O(E²)
C) O(√V · E)
D) O(V · log V)

**Answer: C** — Hopcroft-Karp runs in O(√V · E) time.

---

### MCQ 3: Kuhn's Algorithm
In Kuhn's algorithm for maximum bipartite matching, what data structure is primarily used to find augmenting paths?

A) Breadth-First Search
B) Depth-First Search
C) Dijkstra's Algorithm
D) Union-Find

**Answer: B** — Kuhn's algorithm uses DFS to recursively search for augmenting paths.

---

### MCQ 4: Kőnig's Theorem
According to Kőnig's theorem, in a bipartite graph:

A) Maximum matching = Minimum edge cover
B) Maximum matching = Minimum vertex cover
C) Maximum matching = Maximum independent set
D) Maximum matching = Maximum flow

**Answer: B** — Kőnig's theorem states that in bipartite graphs, the size of a maximum matching equals the size of a minimum vertex cover.

---

### MCQ 5: Augmenting Paths
A matching M is maximum if and only if:

A) There exists an augmenting path
B) There is no augmenting path
C) The graph is complete
D) All vertices are matched

**Answer: B** — By Berge's lemma, a matching is maximum if and only if there is no augmenting path with respect to it.

---

### MCQ 6: Perfect Matching
A perfect matching in a bipartite graph with partitions L and R exists only when:

A) |L| = |R| and Hall's condition holds
B) |L| = |R|
C) The graph is connected
D) |E| = |L| × |R|

**Answer: A** — Both equal partition sizes and Hall's condition are necessary for a perfect matching.

---

### MCQ 7: Vertex Cover from Matching
Given a maximum matching M in a bipartite graph, which of the following correctly describes the construction of minimum vertex cover?

A) Take all matched vertices from L
B) Take all vertices in alternating tree from BFS
C) Use (L \ Z) ∪ (R ∩ Z) where Z is set of vertices reachable from unmatched L vertices via alternating paths
D) Take all unmatched vertices

**Answer: C** — This is the standard algorithm to construct minimum vertex cover from maximum matching.

---

## 11. Flashcards

| # | Term | Definition |
|---|------|------------|
| 1 | Bipartite Graph | A graph whose vertices can be partitioned into two disjoint sets L and R such that every edge connects a vertex in L to a vertex in R |
| 2 | Matching | A set of edges with no common vertices |
| 3 | Maximum Matching | A matching containing the maximum possible number of edges |
| 4 | Perfect Matching | A matching that covers all vertices in the graph |
| 5 | Augmenting Path | A path that starts at an unmatched vertex in L, ends at an unmatched vertex in R, and alternates between matched and unmatched edges |
| 6 | Hall's Condition | For every subset S ⊆ L, \|N(S)\| ≥ \|S\| |
| 7 | Kőnig's Theorem | In bipartite graphs, size of maximum matching equals size of minimum vertex cover |
| 8 | Kuhn's Algorithm | DFS-based greedy algorithm for maximum matching with O(VE) time |
| 9 | Hopcroft-Karp | BFS + DFS layered algorithm with O(√V · E) time complexity |
| 10 | Vertex Cover | A set of vertices such that every edge has at least one endpoint in the set |
| 11 | Alternating Path | A path that alternates between edges in M and not in M |
| 12 | Berge's Lemma | A matching is maximum iff there is no augmenting path |

---

## 12. Key Takeaways

1. **Fundamental Concepts**: A bipartite graph has vertices partitioned into two sets L and R, with all edges crossing between sets. A matching is a set of edges without shared vertices.

2. **Hall's Theorem**: Provides necessary and sufficient conditions for perfect matching existence through the condition |N(S)| ≥ |S| for all subsets S of L.

3. **Augmenting Paths**: The key to finding larger matchings. By Berge's lemma, a matching is maximum iff no augmenting path exists.

4. **Kuhn's Algorithm**: A simple O(VE) algorithm using DFS. Good for small graphs and educational purposes. Implement with visited array reset for each iteration.

5. **Hopcroft-Karp Algorithm**: The efficient standard algorithm with O(√V · E) complexity. Uses BFS to build layers and DFS to find multiple vertex-disjoint shortest augmenting paths.

6. **Kőnig's Theorem**: A beautiful connection between matching and vertex cover — in bipartite graphs, maximum matching size equals minimum vertex cover size.

7. **Applications**: Job assignment, college admissions, resource allocation, ride-sharing, and online matching platforms all use bipartite matching algorithms.

8. **Implementation Focus**: Always track matched vertices carefully, reset visited arrays appropriately, and ensure the layered structure is maintained in Hopcroft-Karp.

9. **Exam Preparation**: Understand the theoretical foundations (Hall's theorem, Kőnig's theorem) and be able to trace through algorithms manually for small examples.

10. **Real-World Relevance**: The algorithms studied form the basis for many practical systems and can be extended to weighted matching (Hungarian algorithm) and maximum flow formulations.

---

*This study material is designed for MSc CS students at Delhi University, covering all topics in the Advanced Algorithms syllabus related to Bipartite Matching. For further reading, refer to "Introduction to Algorithms" (Cormen et al.) and "Algorithm Design" (Kleinberg & Tardos).*