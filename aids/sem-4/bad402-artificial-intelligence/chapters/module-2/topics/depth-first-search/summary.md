# Depth First Search (DFS)

### Definitions and Formulas

- **Depth-First Search (DFS)**: a graph traversal algorithm that explores a graph or tree by visiting a node and then visiting all of its neighbors before backtracking.
- **Depth**: the number of edges from the starting node to the current node.

### Key Points

- **Algorithm:**
  - Choose a starting node (also called the root node)
  - Explore the node and visit its unvisited neighbors
  - Recursively repeat the process for each unvisited neighbor
  - Backtrack when all neighbors have been visited
- **Types of DFS:**
  - **Unweighted Graph DFS**: no weights are considered
  - **Weighted Graph DFS**: weights are considered during the traversal
  - **Directed Graph DFS**: the graph has a direction
  - **Undirected Graph DFS**: the graph does not have a direction
- **Terminology:**
  - **Stack**: a data structure used to store nodes during the traversal
  - **Node**: a vertex in the graph
  - **Neighbor**: a node that is directly connected to the current node
  - **Backtrack**: returning to the previous node to explore other branches

### Important Theorems

- **Depth-First Search Theorem**: given a graph or tree, DFS traverses all nodes exactly once.
- **Wright's Theorem**: for an unweighted graph, DFS has a time complexity of O(V + E), where V is the number of nodes and E is the number of edges.

### Applications

- **Finding connected components**
- **Testing whether a graph is connected**
- **Topological sorting**
- **Finding strongly connected components**

### Important Formulas

- **Time complexity:** O(V + E)
- **Space complexity:** O(V)
