# **Warshall's and Floyd's Algorithms**

## **Introduction**

Dynamic programming is a method for solving complex problems by breaking them down into smaller sub-problems, solving each sub-problem only once, and storing the solutions to sub-problems to avoid redundant computation. Two important algorithms in the field of dynamic programming are Warshall's algorithm and Floyd's algorithm.

## **Warshall's Algorithm**

Warshall's algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. It is particularly useful for finding the shortest path in a directed acyclic graph (DAG).

### Definition:

Warshall's algorithm is a dynamic programming algorithm that finds the shortest path between all pairs of vertices in a weighted graph. It is based on the principle of transitivity, which states that if there is a path from vertex A to vertex B and a path from vertex B to vertex C, then there is a path from vertex A to vertex C.

### Key Concepts:

- **Weighted graph:** A graph where each edge has a weight or label associated with it.
- **Shortest path:** The path with the minimum total weight between two vertices.
- **Transitivity:** The property that if there is a path from vertex A to vertex B and a path from vertex B to vertex C, then there is a path from vertex A to vertex C.

### Example:

Suppose we have a weighted graph with vertices A, B, C, and D, and edges with weights as follows:

| From | To  | Weight |
| ---- | --- | ------ |
| A    | B   | 2      |
| A    | C   | 3      |
| B    | C   | 1      |
| B    | D   | 4      |
| C    | D   | 2      |

We can use Warshall's algorithm to find the shortest path between all pairs of vertices. The algorithm will produce a matrix where the entry at row i and column j represents the shortest path from vertex i to vertex j.

### Implementation:

Here is a Python implementation of Warshall's algorithm:

```python
def warshall(W):
    n = len(W)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = min(W[i][j], W[i][k] + W[k][j])

# Define the weighted graph
W = [[0, 2, 3, 0],
     [0, 0, 1, 4],
     [0, 0, 0, 2],
     [0, 0, 0, 0]]

# Run Warshall's algorithm
warshall(W)

# Print the shortest path matrix
for row in W:
    print(row)
```

## **Floyd's Algorithm**

Floyd's algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. It is particularly useful for finding the shortest path in a weighted graph with negative weights.

### Definition:

Floyd's algorithm is a dynamic programming algorithm that finds the shortest path between all pairs of vertices in a weighted graph. It is based on the principle of transitivity, which states that if there is a path from vertex A to vertex B and a path from vertex B to vertex C, then there is a path from vertex A to vertex C.

### Key Concepts:

- **Weighted graph:** A graph where each edge has a weight or label associated with it.
- **Shortest path:** The path with the minimum total weight between two vertices.
- **Negative weights:** Weights that can be negative, which can result in a negative shortest path.

### Example:

Suppose we have a weighted graph with vertices A, B, C, and D, and edges with weights as follows:

| From | To  | Weight |
| ---- | --- | ------ |
| A    | B   | 2      |
| A    | C   | 3      |
| B    | C   | 1      |
| B    | D   | 4      |
| C    | D   | 2      |

We can use Floyd's algorithm to find the shortest path between all pairs of vertices. The algorithm will produce a matrix where the entry at row i and column j represents the shortest path from vertex i to vertex j.

### Implementation:

Here is a Python implementation of Floyd's algorithm:

```python
def floyd(W):
    n = len(W)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = min(W[i][j], W[i][k] + W[k][j])

# Define the weighted graph
W = [[0, 2, 3, 0],
     [0, 0, 1, 4],
     [0, 0, 0, 2],
     [0, 0, 0, 0]]

# Run Floyd's algorithm
floyd(W)

# Print the shortest path matrix
for row in W:
    print(row)
```

## **Comparison of Warshall's and Floyd's Algorithm**

|                       | Warshall's Algorithm                                  | Floyd's Algorithm                                             |
| --------------------- | ----------------------------------------------------- | ------------------------------------------------------------- |
| **Time Complexity:**  | O(n^3)                                                | O(n^3)                                                        |
| **Space Complexity:** | O(n^2)                                                | O(n^2)                                                        |
| **Weighted Graph:**   | Can handle negative weights                           | Can handle negative weights                                   |
| **Shortest Path:**    | Finds shortest path in a directed acyclic graph (DAG) | Finds shortest path in a weighted graph with negative weights |

In conclusion, Warshall's algorithm and Floyd's algorithm are both used to find the shortest path between all pairs of vertices in a weighted graph. While they share some similarities, they also have some key differences. Warshall's algorithm is particularly useful for finding the shortest path in a DAG, while Floyd's algorithm is useful for finding the shortest path in a weighted graph with negative weights.
