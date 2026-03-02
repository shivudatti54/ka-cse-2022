# **Greedy Best First Search**

## **Introduction**

Greedy Best First Search (GBFS) is a popular pathfinding algorithm used in artificial intelligence and computer science. It is an optimization of Dijkstra's algorithm, which is used to find the shortest path between two nodes in a weighted graph or network.

## **Definition**

GBFS is an algorithm that selects the next node to visit based on the estimated total cost of reaching the goal node, rather than the estimated cost of reaching the goal node from the current node. It is called "best first" because it always chooses the node that has the lowest estimated total cost.

## **How GBFS Works**

Here is a step-by-step explanation of how GBFS works:

1. **Initialization**: The algorithm starts with the initial node and estimates the cost of reaching each neighbor based on the edge weights.
2. **Expansion**: The algorithm expands the current node by exploring its neighbors and estimating the cost of reaching the goal node from each neighbor.
3. **Selection**: The algorithm selects the next node to visit based on the estimated total cost of reaching the goal node from each neighbor.
4. **Repetition**: Steps 2 and 3 are repeated until the goal node is reached or it is determined that there is no path to the goal.

## **Key Concepts**

- **Heuristic**: A heuristic is a function that estimates the cost of reaching the goal node from a given node. In GBFS, the heuristic is used to estimate the total cost of reaching the goal node from each neighbor.
- **Cost**: The cost of reaching a node is the sum of the edge weights of the path from the initial node to that node.
- **Estimated Total Cost**: The estimated total cost of reaching the goal node from a given node is the sum of the cost of reaching that node and the estimated cost of reaching the goal node from that node.

## **Example**

Suppose we have a weighted graph with the following nodes and edges:

| Node | Edge Weight |
| ---- | ----------- |
| A    | 1           |
| B    | 2           |
| C    | 3           |
| D    | 4           |
| E    | 5           |

We want to find the shortest path from node A to node E using GBFS.

1.  **Initialization**: The algorithm starts with node A and estimates the cost of reaching each neighbor based on the edge weights.
    - Node B: cost = 1 + 2 = 3
    - Node C: cost = 1 + 3 = 4
    - Node D: cost = 1 + 4 = 5
    - Node E: cost = 1 + 5 = 6
2.  **Expansion**: The algorithm expands node B by exploring its neighbors and estimating the cost of reaching the goal node from each neighbor.
    - Node B: cost = 3 + 2 = 5 (estimated total cost = 3 + 2 = 5)
    - Node C: cost = 4 + 3 = 7 (estimated total cost = 3 + 3 = 6)
    - Node D: cost = 5 + 4 = 9 (estimated total cost = 3 + 4 = 7)
    - Node E: cost = 6 + 5 = 11 (estimated total cost = 3 + 5 = 8)
3.  **Selection**: The algorithm selects the next node to visit based on the estimated total cost of reaching the goal node from each neighbor.
    - Node B: selected
4.  **Repetition**: Steps 2 and 3 are repeated until the goal node is reached or it is determined that there is no path to the goal.

## **Pseudocode**

Here is the pseudocode for GBFS:

```
function GBFS(graph, start, goal):
    openSet = {start}
    cameFrom = {}
    gScore = {start: 0}
    fScore = {start: heuristic(start, goal)}

    while openSet != empty():
        current = argmin(fScore, openSet)
        if current == goal:
            break

        openSet.remove(current)

        for neighbor in neighbors(current):
            tentativeGScore = gScore[current] + edgeWeight(current, neighbor)
            if neighbor not in openSet or tentativeGScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentativeGScore
                fScore[neighbor] = tentativeGScore + heuristic(neighbor, goal)
                if neighbor not in openSet:
                    openSet.add(neighbor)

    return cameFrom, gScore, fScore
```

## **Advantages and Disadvantages**

**Advantages:**

- GBFS is an efficient algorithm for finding the shortest path in unweighted graphs.
- It is easy to implement and understand.

**Disadvantages:**

- GBFS assumes that the heuristic function is admissible (never overestimates the cost) and consistent (the estimated cost is always less than or equal to the true cost).
- It may not work well for graphs with a large number of nodes or edges.
- It may not be able to find the optimal solution if the graph has a complex structure.
