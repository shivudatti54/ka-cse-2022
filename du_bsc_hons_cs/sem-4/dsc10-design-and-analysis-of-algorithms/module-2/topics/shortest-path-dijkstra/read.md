# Shortest Path: Dijkstra's Algorithm

## Introduction

The single-source shortest path problem is one of the most fundamental problems in graph theory and computer science. Given a weighted graph (with non-negative edge weights), the task is to find the shortest path from a designated source vertex to all other vertices in the graph. This problem appears in numerous real-world applications including road networks (GPS navigation), computer networks (routing protocols like OSPF), airline flight connections, and game pathfinding.

Dijkstra's algorithm, developed by Dutch computer scientist Edsger W. Dijkstra in 1956, solves this problem elegantly using a greedy approach. The algorithm maintains a set of vertices whose shortest distance from the source is already finalized and repeatedly selects the vertex with the minimum tentative distance from this set. This greedy choice proves to be globally optimal due to the non-negative edge weight constraint, making Dijkstra's algorithm both simple and efficient.

In the context of the University of Delhi's Computer Science curriculum, Dijkstra's algorithm serves as a cornerstone topic that demonstrates the power of greedy algorithms, introduces priority queue data structures, and provides insight into algorithm analysis. Understanding this algorithm is essential for students preparing for competitive examinations and technical interviews at top companies.

## Key Concepts

### Problem Definition

Given a weighted graph G = (V, E) with non-negative edge weights w(u, v) ≥ 0 and a source vertex s, find the shortest path distance from s to every other vertex v ∈ V. The shortest path distance d(s, v) is defined as the minimum total weight of any path from s to v.

### Algorithm Overview

Dijkstra's algorithm maintains two key data structures:
1. **Distance array dist[]**: Stores the currently known shortest distance from source to each vertex
2. **Priority queue (min-heap)**: Extracts the vertex with minimum distance efficiently

The algorithm proceeds in iterations, at each step selecting the unvisited vertex with smallest tentative distance and "finalizing" it.

### Relaxation Operation

The core operation in Dijkstra's algorithm is relaxation. For an edge (u, v) with weight w:
```
if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w
    parent[v] = u
```

This operation checks whether going through vertex u provides a shorter path to vertex v than the current known path.

### Algorithm Steps

1. Initialize dist[s] = 0 and dist[v] = ∞ for all other vertices
2. Insert all vertices into a priority queue with their dist values
3. While priority queue is not empty:
   - Extract vertex u with minimum dist[u]
   - For each neighbor v of u:
     - Perform relaxation operation
     - If relaxation succeeds, update v's distance in priority queue

### Correctness Proof Sketch

The correctness of Dijkstra's algorithm rests on a key invariant: when a vertex u is extracted from the priority queue, dist[u] equals the true shortest path distance from the source to u.

**Proof by contradiction**: Assume the first extracted vertex whose dist is not optimal is u. Since all vertices extracted before u have optimal distances, consider the shortest path P from source s to u. Let x be the first vertex on P that is not yet extracted, and let y be its predecessor on P. Since edge weights are non-negative, the path to y has already been discovered and y was extracted before x (otherwise y would have smaller distance). Through relaxation, when y was processed, the path to x via y was considered, establishing dist[x] = d(s, x). Since u is chosen with minimum dist, we have dist[u] ≤ dist[x] = d(s, u), contradicting the assumption that dist[u] > d(s, u).

### Time Complexity Analysis

Using different priority queue implementations:
- **Array/Linear scan**: O(V²) time, O(V) space
- **Binary Min-Heap**: O((V + E) log V) time, O(V) space
- **Fibonacci Heap**: O(E + V log V) time, O(V) space

For dense graphs (E ≈ V²), array implementation is often fastest due to lower constant factors. For sparse graphs, binary heap is preferred.

### Limitations

1. **Negative edge weights**: The algorithm fails with negative weights because the greedy choice may no longer be optimal
2. **Negative weight cycles**: Can cause infinite relaxation, making shortest path undefined

## Examples

### Example 1: Basic Dijkstra's Algorithm

Consider the following graph with source vertex A:

```
        4
    A-------B
   /|       |\
  2| |7     | 1
 /  |  \   |
C   |   \  D
 \  |    \ |
  5|     6\|
   |       E
    -------F
        3
```

**Step-by-step execution:**

**Initialization:**
dist[A]=0, dist[others]=∞

**Iteration 1:** Extract A (distance 0)
- Relax A→B: dist[B] = 0 + 4 = 4
- Relax A→C: dist[C] = 0 + 2 = 2

**Iteration 2:** Extract C (distance 2)
- Relax C→F: dist[F] = 2 + 5 = 7

**Iteration 3:** Extract B (distance 4)
- Relax B→D: dist[D] = 4 + 1 = 5
- Relax B→E: dist[E] = 4 + 6 = 10

**Iteration 4:** Extract D (distance 5)
- Relax D→E: dist[E] = min(10, 5 + 6) = 10 (no change)

**Iteration 5:** Extract E (distance 10)
- No outgoing edges to relax

**Iteration 6:** Extract F (distance 7)
- Relax F→E: dist[E] = min(10, 7 + 3) = 10 (no change)

**Final distances:** A=0, B=4, C=2, D=5, E=10, F=7

### Example 2: Implementation with Binary Heap

```python
import heapq

def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    parent = {v: None for v in graph}
    pq = [(0, source)]  # (distance, vertex)
    visited = set()
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    return dist, parent

# Example usage
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 1), ('E', 6)],
    'C': [('F', 5)],
    'D': [('E', 6)],
    'E': [],
    'F': [('E', 3)]
}

distances, parents = dijkstra(graph, 'A')
print("Shortest distances:", distances)
# Output: {'A': 0, 'B': 4, 'C': 2, 'D': 5, 'E': 10, 'F': 7}
```

### Example 3: Trace Table

For a graph with vertices {S, A, B, C, D} and edges:
- S→A: 5, S→B: 2
- A→C: 3, A→D: 9
- B→A: 1, B→C: 6
- C→D: 2

| Step | Extracted | dist[A] | dist[B] | dist[C] | dist[D] |
|------|-----------|---------|---------|---------|---------|
| Init | -         | ∞       | 2       | ∞       | ∞       |
| 1    | B(2)      | 3       | 2       | 8       | ∞       |
| 2    | A(3)      | 3       | 2       | 6       | 12      |
| 3    | C(6)      | 3       | 2       | 6       | 8       |
| 4    | D(8)      | 3       | 2       | 6       | 8       |

Final shortest paths from S: A=3, B=2, C=6, D=8

## Exam Tips

1. **Always check edge weights first**: Dijkstra's algorithm ONLY works for non-negative weights. Mention this as a prerequisite in exams.

2. **Greedy choice property**: The algorithm makes a locally optimal choice (minimum distance vertex) that leads to global optimum due to non-negative weights.

3. **Time complexity matters**: Be prepared to analyze and compare implementations. Binary heap implementation is most commonly asked.

4. **Draw complete trace tables**: Show each iteration with current distances, extracted vertex, and relaxation operations. This demonstrates understanding.

5. **Comparison with Bellman-Ford**: Know that Bellman-Ford handles negative weights but runs in O(VE), while Dijkstra is O(E + V log V) but fails with negative weights.

6. **Space complexity**: Always mention O(V) auxiliary space for the distance array and priority queue.

7. **Applications knowledge**: Be ready to mention real-world applications like GPS navigation, network routing, and flight bookings to score marks in "write short notes" questions.

8. **Handling ties**: When multiple vertices have equal minimum distance, any can be chosen. This doesn't affect final distances but may change the order of extraction.

9. **Reconstruction of paths**: Remember to maintain a parent array to reconstruct the actual shortest path, not just the distance.

10. **Optimization tip**: Use adjacency list representation for sparse graphs and adjacency matrix for dense graphs.