# Greedy Best First Search

### Overview

Greedy best first search is a heuristic search algorithm used in artificial intelligence to find the shortest path between a start node and a goal node in an unweighted graph. This algorithm is particularly useful when the graph is large and the start and goal nodes are not adjacent, as it can be more efficient than other search algorithms like depth-first search (DFS) and breadth-first search (BFS).

### Key Concepts

#### Definition

Greedy best first search is a heuristic search algorithm that selects the node with the lowest estimated total cost (heuristic + cost so far) to expand next.

#### Heuristics

Heuristics are estimates of the distance from a node to the goal node. In greedy best first search, the heuristic is used to guide the search towards the goal node.

#### Greedy Algorithm

The greedy algorithm in this algorithm chooses the next node based on the lowest estimated total cost. If the estimated total cost of two nodes is the same, the algorithm chooses the node with the lowest cost so far.

### How it Works

1. Initialize the start node and the goal node.
2. Assign a cost to each node in the graph.
3. Calculate the estimated total cost for each node (heuristic + cost so far).
4. Select the node with the lowest estimated total cost as the next node to expand.
5. Expand the selected node and update the estimated total cost for its neighbors.
6. Repeat steps 4-5 until the goal node is reached or the search space is exhausted.

### Example

Suppose we have a graph with the following nodes and edges:

| Node | Edge | Cost |
| ---- | ---- | ---- |
| A    | B    | 2    |
| A    | C    | 4    |
| B    | D    | 3    |
| B    | E    | 1    |
| C    | F    | 2    |
| C    | G    | 5    |
| D    | H    | 2    |
| E    | H    | 1    |
| F    | H    | 3    |

We want to find the shortest path from node A to node H.

1. Initial node: A
2. Estimated total cost: 0
3. Next node: B (cost 2, heuristic 3 = 5)
4. Expand node B
5. Next node: E (cost 1, heuristic 1 = 2)
6. Expand node E
7. Next node: H (cost 1, heuristic 0 = 1)

The shortest path from node A to node H is A -> B -> E -> H with a total cost of 4.

### Advantages

- Greedy best first search is particularly efficient for large graphs with many nodes.
- It can be used to find approximate solutions when an exact solution is not possible.

### Disadvantages

- Greedy best first search assumes that the heuristic is admissible (never overestimates the distance to the goal node).
- It can get stuck in local optima if the heuristic is not good enough.

### Pseudocode

```
function greedyBestFirstSearch(startNode, goalNode, graph):
    // Initialize the open list and the closed list
    openList = [startNode]
    closedList = []

    // Initialize the estimated total cost and the parent node
    estimatedTotalCost = 0
    parentNode = null

    while openList != empty:
        // Select the node with the lowest estimated total cost
        currentNode = selectNextNode(openList, graph)

        // If the current node is the goal node, return the path
        if currentNode == goalNode:
            return reconstructPath(parentNode, currentNode, graph)

        // Add the current node to the closed list
        closedList.add(currentNode)

        // Expand the current node
        for neighbor in graph[currentNode]:
            // Calculate the estimated total cost for the neighbor
            estimatedTotalCostNeighbor = estimatedTotalCost + graph[currentNode][neighbor] + heuristic(neighbor, goalNode)

            // If the neighbor is in the open list, update its estimated total cost
            if neighbor in openList:
                if estimatedTotalCostNeighbor < openList[neighbor].estimatedTotalCost:
                    openList[neighbor].estimatedTotalCost = estimatedTotalCostNeighbor
                    openList[neighbor].parentNode = currentNode

            // If the neighbor is not in the open list, add it to the open list
            else:
                openList.append(neighbor)
                neighbor.estimatedTotalCost = estimatedTotalCostNeighbor
                neighbor.parentNode = currentNode

        // Remove the current node from the open list
        openList.remove(currentNode)

    // If the goal node is not reachable, return null
    return null
```

### Conclusion

Greedy best first search is a useful heuristic search algorithm for finding the shortest path between a start node and a goal node in an unweighted graph. It is particularly efficient for large graphs and can be used to find approximate solutions when an exact solution is not possible. However, it assumes that the heuristic is admissible and can get stuck in local optima if the heuristic is not good enough.
