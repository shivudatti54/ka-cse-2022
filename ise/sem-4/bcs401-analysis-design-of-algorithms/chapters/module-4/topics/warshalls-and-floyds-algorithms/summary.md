# **Warshall's and Floyd's Algorithms**

## **Overview**

- Warshall's algorithm: finds the shortest path between all pairs of nodes in a weighted graph
- Floyd's algorithm: finds the shortest path between all pairs of nodes in a weighted graph with negative weight edges

## **Warshall's Algorithm**

- **Definition**: Warshall's algorithm is a dynamic programming algorithm to find the shortest path between all pairs of nodes in a weighted graph.
- **Formula**: Warshall's algorithm uses the following formula to update the distance matrix:
  ```
  d[i][j] = min(d[i][j], d[i][k] + d[k][j])
  ```
- **Steps**:
  1. Initialize the distance matrix with the given weights
  2. Iterate over all intermediate nodes (k)
  3. Update the distance matrix for each pair of nodes (i, j)
- **Time Complexity**: O(n^3)
- **Space Complexity**: O(n^2)

## **Floyd's Algorithm**

- **Definition**: Floyd's algorithm is a dynamic programming algorithm to find the shortest path between all pairs of nodes in a weighted graph with negative weight edges.
- **Theorem**: If the graph contains a negative cycle, then there is no algorithm that can guarantee the shortest path between all pairs of nodes.
- **Formula**: Floyd's algorithm uses the following formula to update the distance matrix:
  ```
  d[i][j] = min(d[i][j], d[i][k] + d[k][j])
  ```
- **Steps**:
  1. Initialize the distance matrix with the given weights
  2. Iterate over all pairs of nodes (i, j)
  3. Check if the distance matrix contains a negative cycle
  4. If it does, then the algorithm terminates
- **Time Complexity**: O(n^3)
- **Space Complexity**: O(n^2)

## **Key Points**

- Both algorithms are used to find the shortest path between all pairs of nodes in a weighted graph
- Warshall's algorithm can handle graphs with both positive and negative weights
- Floyd's algorithm can only handle graphs with negative weight edges
- Both algorithms have a time complexity of O(n^3)
