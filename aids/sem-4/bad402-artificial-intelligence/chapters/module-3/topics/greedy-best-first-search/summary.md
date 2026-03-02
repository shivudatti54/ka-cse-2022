# Greedy Best First Search

### Definition

Greedy Best First Search (GBFS) is a pathfinding algorithm used to find the shortest path between two points in a weighted graph or network.

### Key Points

- **Goal**: Find the shortest path between two nodes in a weighted graph.
- **Algorithm**:
  - Explore the node with the lowest cost (or heuristic value) at each step.
  - Choose the next node to visit based on the lowest cost.
- **Heuristic**: A function that estimates the cost from a node to the goal node.
- **Greedy Choice**: At each step, choose the next node that minimizes the total cost (heuristic + cost of reaching the node).

### Important Formulas and Definitions

- **Heuristic Function**: $h(n) = \text{estimated cost from node } n \text{ to the goal node}$
- **Cost Function**: $c(n) = \text{actual cost of reaching node } n$
- **Total Cost**: $f(n) = c(n) + h(n)$
- **A\* Algorithm**: A variant of GBFS that uses an admissible heuristic function.

### Theorem

- **Optimality**: GBFS is not guaranteed to find the optimal solution, but it is guaranteed to find a suboptimal solution.

### Time Complexity

- The time complexity of GBFS is O(b^d), where b is the branching factor and d is the depth of the search tree.

### Space Complexity

- The space complexity of GBFS is O(b^d), where b is the branching factor and d is the depth of the search tree.

### Advantages

- GBFS is fast and efficient, especially in situations where the graph is sparse.
- GBFS is easy to implement and understand.

### Disadvantages

- GBFS is not guaranteed to find the optimal solution.
- GBFS can get stuck in local optima.
