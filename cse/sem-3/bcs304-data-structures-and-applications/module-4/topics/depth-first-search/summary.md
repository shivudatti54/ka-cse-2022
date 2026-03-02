# Depth First Search

## Overview

Depth First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It uses a stack (either explicitly or via recursion) to keep track of vertices to visit and a visited array to avoid revisiting vertices. DFS is suitable for finding connected components, detecting cycles, and topological sorting.

## Key Points

- DFS explores a graph by visiting a node and then visiting all of its neighbors before backtracking.
- It uses a stack data structure to keep track of nodes to visit.
- The algorithm marks each visited node to avoid revisiting it.
- DFS can be implemented recursively or iteratively.
- Time complexity: O(V + E) for adjacency list, O(V^2) for adjacency matrix.
- Space complexity: O(V) due to the visited array and recursion stack.

## Important Definitions

- **DFS Tree**: A tree formed by the edges used to traverse the graph.
- **Back Edge**: An edge that connects a node to its ancestor in the DFS tree, indicating a cycle.
- **Tree Edge**: An edge that is part of the DFS tree.
- **Forward Edge**: An edge that connects a node to its descendant in the DFS tree but is not a tree edge.
- **Cross Edge**: An edge that connects two nodes in different subtrees.

## Key Formulas / Syntax

```c
// Recursive DFS
void DFS(Graph* g, int v) {
    g->visited[v] = 1;
    printf("%d ", v);
    Node* temp = g->adjList[v];
    while (temp != NULL) {
        if (!g->visited[temp->vertex]) {
            DFS(g, temp->vertex);
        }
        temp = temp->next;
    }
}
```

## Comparisons

| Representation   | Time Complexity | Space Complexity |
| ---------------- | --------------- | ---------------- |
| Adjacency List   | O(V + E)        | O(V)             |
| Adjacency Matrix | O(V^2)          | O(V)             |

## Exam Tips

- Practice tracing DFS by hand on various graphs.
- Know both recursive and iterative DFS implementations.
- Understand time complexity for different graph representations.
- Be able to classify edges in a graph (tree, back, forward, cross).
- Familiarize yourself with DFS applications (cycle detection, topological sort, connected components).
- Remember to handle disconnected graphs by calling DFS on each unvisited vertex.
