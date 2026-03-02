# Graph Representations, BFS, and DFS

## Introduction
Graphs are fundamental data structures used to model pairwise relationships between objects. With applications ranging from social network analysis to GPS navigation systems, understanding graph representations and traversal algorithms is essential for solving complex real-world problems.

Two primary representations exist: adjacency matrices (ideal for dense graphs) and adjacency lists (efficient for sparse graphs). Breadth-First Search (BFS) and Depth-First Search (DFS) form the foundation for more advanced algorithms like shortest path finding and topological sorting.

In modern systems, BFS powers web crawlers that index internet pages level-by-level, while DFS enables backtracking in maze-solving robots. The choice between these representations and algorithms significantly impacts time and space complexity in applications like recommendation systems and network analysis.

## Key Concepts

**Adjacency Matrix**
- 2D array where matrix[i][j] = 1 indicates edge between vertex i and j
- Space complexity: O(V²)
- Edge lookup: O(1)
- Best for dense graphs with V² ≈ E

**Adjacency List**
- Array of linked lists where each list stores neighbors of a vertex
- Space complexity: O(V + E)
- Edge lookup: O(degree(V))
- Ideal for sparse graphs

**BFS Algorithm**
1. Uses queue data structure
2. Explores nodes level-by-level
3. Guarantees shortest path in unweighted graphs
4. Time complexity: O(V + E)

**DFS Algorithm**
1. Uses stack (implicit via recursion)
2. Explores deepest node first
3. Useful for cycle detection and topological sorting
4. Time complexity: O(V + E)

**BFS vs DFS**
- BFS requires more memory (queue size up to O(V))
- DFS better for deep graphs with limited memory
- BFS gives shortest path, DFS helps find connected components

## Examples

**Example 1: Adjacency Representation**
Construct adjacency matrix and list for graph:
```
0 connected to 1, 2
1 connected to 2
2 connected to 0, 3
3 connected to 3
```

*Solution:*
Adjacency Matrix:
```
[[0,1,1,0],
 [1,0,1,0],
 [1,1,0,1],
 [0,0,1,1]]
```

Adjacency List:
```
0: [1, 2]
1: [0, 2]
2: [0, 1, 3]
3: [2, 3]
```

**Example 2: BFS Traversal**
Perform BFS starting at node 2 for the above graph:

*Solution:*
1. Queue: [2], Visited: {2}
2. Dequeue 2 → visit 0,1,3 → Queue: [0,1,3]
3. Dequeue 0 → visit 1 (already visited) → Queue: [1,3]
4. Dequeue 1 → no new nodes → Queue: [3]
5. Dequeue 3 → visit 3 (self-loop) → Queue: []
Traversal order: 2 → 0 → 1 → 3

**Example 3: DFS Application**
Detect cycle in directed graph using DFS recursion stack:

```python
def has_cycle(graph):
    visited = [False] * len(graph)
    rec_stack = [False] * len(graph)
    
    def dfs(v):
        visited[v] = True
        rec_stack[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[v] = False
        return False
    
    return any(not visited[i] and dfs(i) for i in range(len(graph)))
```

## Exam Tips
1. Always mention time/space complexity when comparing representations
2. For BFS, remember to mark nodes as visited when enqueuing, not dequeuing
3. In DFS, specify if using recursive or iterative implementation
4. When asked about real-world applications:
   - BFS: Social network degrees of separation
   - DFS: Solving Sudoku puzzles
5. For cycle detection, DFS is generally preferred
6. Adjacency matrices enable O(1) edge existence checks
7. Practice writing both representations from adjacency diagrams