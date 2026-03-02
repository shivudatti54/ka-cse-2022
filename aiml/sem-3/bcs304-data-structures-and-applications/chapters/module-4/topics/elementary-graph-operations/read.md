# Elementary Graph Operations

## Introduction

Graphs are fundamental non-linear data structures used extensively in computer science to model relationships between objects. In the previous chapters, we explored the basic definitions and abstract data types of graphs. Now, we turn our attention to elementary graph operations—the essential building blocks that enable us to manipulate and traverse graph structures effectively.

Elementary graph operations form the backbone of any graph-based algorithm. Whether you are finding the shortest path between cities in a navigation system, detecting cycles in a network, or analyzing social media connections, these operations are the primitives that make such computations possible. For students preparing for DU semester examinations, mastering these operations is crucial as they frequently appear in both theory papers and practical exams.

This chapter covers the core operations including graph traversal techniques (Breadth-First Search and Depth-First Search), methods to add and remove vertices and edges, and various utility operations that help us inspect and modify graph properties. Understanding these operations thoroughly will provide a solid foundation for more advanced graph algorithms studied in subsequent modules.

## Key Concepts

### 1. Graph Representation Methods

Before performing any operation, we must understand how graphs are represented in memory. The choice of representation significantly impacts the efficiency of operations.

**Adjacency Matrix:** A 2D array of size V × V where V represents the number of vertices. For a graph G = (V, E), if there is an edge from vertex i to vertex j, then matrix[i][j] = 1 (or weight for weighted graphs); otherwise, it is 0. The adjacency matrix representation offers O(1) edge lookup but requires O(V²) space regardless of the number of edges. This representation is particularly suitable for dense graphs where the number of edges is close to V².

**Adjacency List:** An array of linked lists where each vertex has a list of its neighboring vertices. The space complexity is O(V + E), making it efficient for sparse graphs where E is much smaller than V². Edge insertion and neighbor iteration are efficient, but edge existence checking takes O(degree) time.

### 2. Graph Traversal Operations

Graph traversal is the process of visiting all vertices in a systematic manner. Two primary traversal algorithms form the foundation of numerous graph applications.

**Breadth-First Search (BFS):** BFS explores vertices level by level, starting from a source vertex. It uses a queue data structure to keep track of vertices to be explored. The algorithm marks vertices as visited when enqueued, not when dequeued, ensuring each vertex is visited exactly once. BFS is particularly useful for finding shortest paths in unweighted graphs and for level-order traversal.

The BFS algorithm proceeds as follows: Initialize a queue with the source vertex, mark it as visited. While the queue is not empty, dequeue a vertex, process it, and enqueue all unvisited neighbors. Continue until the queue becomes empty.

**Depth-First Search (DFS):** DFS explores as far as possible along each branch before backtracking. It uses a stack (either explicitly or through recursion) to keep track of vertices. DFS is essential for detecting cycles, topological sorting, and solving maze problems. The algorithm can be implemented recursively or iteratively using an explicit stack.

The recursive DFS works by: Marking the current vertex as visited, processing the vertex, then recursively visiting all unvisited neighbors. The iterative version uses an explicit stack to simulate the recursion.

### 3. Vertex Operations

**Adding a Vertex:** In an adjacency list representation, adding a vertex involves creating a new entry in the array and initializing an empty list for its neighbors. In an adjacency matrix, this requires expanding the matrix to accommodate the new vertex, which is an O(V²) operation. Most implementations use dynamic data structures to handle vertex additions efficiently.

**Removing a Vertex:** Deleting a vertex requires removing all edges connected to it. In adjacency list, this means iterating through all lists and removing references to the deleted vertex, then removing the list itself. In adjacency matrix, we must remove the corresponding row and column, which is computationally expensive.

**Checking Vertex Existence:** Simply verifying whether a vertex exists in the graph, typically by checking if it falls within the valid range of vertex indices or exists in a vertex set.

### 4. Edge Operations

**Adding an Edge:** For an undirected graph, adding an edge between vertices u and v requires adding v to u's adjacency list and u to v's adjacency list. For directed graphs, only the appropriate direction is added. Using adjacency matrices, this is a simple O(1) assignment operation.

**Removing an Edge:** The inverse of adding an edge—removing the neighbor from the adjacency list or setting the matrix entry to 0. In adjacency lists, this requires searching through the linked list, making it O(degree) in the worst case.

**Checking Edge Existence:** Determining whether an edge exists between two vertices. This is O(1) in adjacency matrix but O(degree) in adjacency list.

### 5. Utility Operations

**Graph Size:** Determining the number of vertices (|V|) or edges (|E|). For adjacency matrix, vertices can be counted directly from dimensions. For adjacency list, we iterate through the array to count non-empty lists.

**Degree Calculations:** For undirected graphs, the degree of a vertex is the number of edges incident to it. In adjacency list, this equals the length of the neighbor list. For directed graphs, we distinguish between in-degree (incoming edges) and out-degree (outgoing edges).

**Neighbor Retrieval:** Getting all adjacent vertices of a given vertex. This is a straightforward iteration through the adjacency list or scanning the corresponding row in the adjacency matrix.

**Graph Initialization:** Creating an empty graph with a specified number of vertices or with zero vertices. This involves allocating appropriate data structures based on the chosen representation.

## Examples

### Example 1: BFS Traversal on a Graph

Consider a graph with vertices {0, 1, 2, 3, 4} and edges: {(0,1), (0,2), (1,3), (2,3), (3,4)}. Perform BFS starting from vertex 0.

**Step-by-step solution:**

1. Initialize: visited array = {F, F, F, F, F}, queue = [0]
2. Dequeue 0, mark visited[0] = T, process 0
3. Enqueue unvisited neighbors: neighbors of 0 are 1 and 2. Queue = [1, 2]
4. Dequeue 1, mark visited[1] = T, process 1. Enqueue neighbor 3 (unvisited). Queue = [2, 3]
5. Dequeue 2, mark visited[2] = T, process 2. Neighbor 3 already visited.
6. Dequeue 3, mark visited[3] = T, process 3. Enqueue neighbor 4. Queue = [4]
7. Dequeue 4, mark visited[4] = T, process 4. No unvisited neighbors.

**BFS Order:** 0 → 1 → 2 → 3 → 4

### Example 2: DFS Traversal on the Same Graph

Using the same graph, perform DFS starting from vertex 0.

**Recursive Solution:**

1. Visit 0, mark visited[0] = T
2. Recursively visit unvisited neighbor: 1 (unvisited) → mark visited[1] = T
3. From 1, visit unvisited neighbor: 3 (unvisited) → mark visited[3] = T
4. From 3, visit unvisited neighbor: 4 (unvisited) → mark visited[4] = T
5. Backtrack to 3, no more unvisited neighbors
6. Backtrack to 1, no more unvisited neighbors
7. Backtrack to 0, visit unvisited neighbor: 2 (unvisited) → mark visited[2] = T
8. From 2, no unvisited neighbors

**DFS Order:** 0 → 1 → 3 → 4 → 2

### Example 3: Edge Operations Demonstration

Given an empty adjacency list graph, perform the following operations sequentially:
1. Add vertices 0, 1, 2
2. Add edges (0,1), (1,2), (0,2)
3. Check if edge (0,2) exists
4. Remove edge (0,1)
5. Check degree of vertex 1

**Solution:**

After Step 1: Adjacency list = [[], [], []]

After Step 2: 
- Adding (0,1): 0's list → [1], 1's list → [0]
- Adding (1,2): 1's list → [0, 2], 2's list → [1]
- Adding (0,2): 0's list → [1, 2], 2's list → [1, 0]
- Final: 0: [1, 2], 1: [0, 2], 2: [1, 0]

Step 3: Edge (0,2) exists in 0's list → TRUE

Step 4: Remove 1 from 0's list, remove 0 from 1's list
- 0: [2], 1: [2], 2: [1, 0]

Step 5: Degree of vertex 1 = number of neighbors = 1 (only vertex 2)

## Exam Tips

1. Understand when to use BFS versus DFS: BFS for shortest path in unweighted graphs, level-order traversal; DFS for cycle detection, topological sort, and path finding.

2. Memorize time complexities: Adjacency matrix has O(1) edge operations but O(V²) space. Adjacency list has O(V+E) space but O(degree) edge operations.

3. Remember that BFS uses a queue (FIFO) while DFS uses a stack (LIFO) or recursion.

4. For degree calculations in directed graphs, clearly distinguish between in-degree and out-degree.

5. Practice implementing both BFS and DFS algorithms as they frequently appear in practical exams.

6. When a graph is represented as an adjacency matrix, the sum of any row gives the out-degree of that vertex.

7. The order of neighbors in DFS matters and affects the traversal order—mention this in exam answers when required.

8. Always initialize visited/queue/stack structures properly before starting traversal.

9. For weighted graphs, store both vertex and weight information in adjacency list nodes.