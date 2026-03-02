# **Depth First Search**

### Definition

- A graph traversal algorithm that explores a graph or tree by visiting a node and then visiting all of its neighbors before backtracking.
- It uses a stack data structure to keep track of the nodes to visit.

### Important Concepts

- **Node**: A single element in the graph or tree.
- **Neighbor**: A node that is directly connected to the current node.
- **Stack**: A data structure that stores nodes to visit in the order they are visited.

### Key Formulas and Theorems

- **Depth First Search Algorithm**:
  ```markdown

  ```

1. Choose a starting node (also known as the root node)
2. Mark the starting node as visited
3. Explore the neighbors of the starting node
4. For each unvisited neighbor, mark it as visited and repeat steps 3-4
5. Backtrack to the previous node when all its neighbors have been visited

````

* **Time Complexity**: O(|V| + |E|), where |V| is the number of nodes and |E| is the number of edges.

### Important Theorems

* **Depth First Search Theorem**: If a graph has a cycle, then the depth-first search will either find a cycle or visit all nodes in the graph.
* **No Cycle Property**: If the depth-first search does not find a cycle, then the graph is acyclic.

### Example Use Cases

* Finding strongly connected components in a graph
* Testing whether a graph contains a cycle
* Topological sorting of a directed acyclic graph (DAG)

### Example Code (in Python)
```python
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return visited
````

Note: This is a basic implementation of DFS.
