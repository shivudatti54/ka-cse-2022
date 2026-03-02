# **Warshall's and Floyd's Algorithms**

## **Introduction**

- Warshall's and Floyd's algorithms are used for solving all-pairs shortest paths problems in a weighted graph.
- They are two of the most important algorithms in graph theory and computer science.

## **Warshall's Algorithm**

- **Definition**: Warshall's algorithm is used to find the transitive closure of a directed graph, i.e., the shortest path between every pair of vertices.
- **Formula**: `w[i][j] = min(w[i][k] + w[k][j])` for `1 <= i <= n` and `1 <= j <= n`
- **Time complexity**: O(n^3)
- **Space complexity**: O(n^2)

## **Floyd's Algorithm**

- **Definition**: Floyd's algorithm is used to find the shortest path between every pair of vertices in a weighted graph.
- **Formula**: `d[i][j] = min(d[i][k] + w[k][j])` for `1 <= i <= n` and `1 <= j <= n`
- **Time complexity**: O(n^2 \* m)
- **Space complexity**: O(n^2)

## **Important Theorems and Definitions**

- **Bellman-Ford Theorem**: A single source shortest paths problem in a weighted graph with non-negative weights has a unique shortest path if and only if the graph does not contain negative cycles.
- **Floyd-Warshall Theorem**: The all-pairs shortest path problem in a weighted graph has a unique solution if and only if the graph does not contain negative cycles.

## **Key Points**

- Warshall's algorithm is used for transitive closure, while Floyd's algorithm is used for shortest paths.
- Both algorithms have a time complexity of O(n^3) and O(n^2 \* m) respectively.
- The Bellman-Ford and Floyd-Warshall theorems are used to determine the existence of negative cycles in a graph.
