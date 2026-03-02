# Warshall's and Floyd's Algorithms

## Table of Contents

- [Introduction](#introduction)
- [Warshall's Algorithm](#warshalls-algorithm)
  - [Definition](#definition)
  - [Explanation](#explanation)
  - [Example](#example)
- [Floyd's Algorithm](#floyds-algorithm)
  - [Definition](#definition-1)
  - [Explanation](#explanation-1)
  - [Example](#example-1)
- [Key Concepts](#key-concepts)
- [Implementation](#implementation)
- [Applications](#applications)

## Introduction

Warshall's and Floyd's algorithms are two fundamental algorithms in graph theory and computer science. They are used to find the shortest path between all pairs of vertices in a weighted graph.

## Warshall's Algorithm

### Definition

Warshall's algorithm is an algorithm in graph theory that finds the shortest path between all pairs of vertices in a weighted graph. It is a dynamic programming algorithm that works by scanning the graph and updating the distance matrix.

### Explanation

The algorithm starts by initializing a distance matrix, where the entry `d[i][j]` represents the shortest distance from vertex `i` to vertex `j`. The algorithm then scans the graph and updates the distance matrix. For each vertex `k`, it checks if the path from vertex `i` to vertex `j` through vertex `k` is shorter than the current shortest distance. If it is, it updates the distance matrix.

### Example

Suppose we have the following weighted graph:

```
  A --1--> B --2--> C --3--> D
  |    / |     |    / |
  |   /  |     |   /  |
  0  /   |     |  0  /   |
  | /    |     | /    |
  |/     |     |/     |
  --        --        --
  E        F        G
```

The distance matrix for this graph is:

|     | A   | B   | C   | D   | E   | F   | G   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 1   | 2   | 3   | inf | inf | inf |
| B   | inf | 0   | 1   | 2   | inf | inf | inf |
| C   | inf | inf | 0   | 1   | inf | inf | inf |
| D   | inf | inf | inf | 0   | inf | inf | inf |
| E   | inf | inf | inf | inf | 0   | 1   | 2   |
| F   | inf | inf | inf | inf | 1   | 0   | 1   |
| G   | inf | inf | inf | inf | 2   | 1   | 0   |

The algorithm updates the distance matrix as follows:

|     | A   | B   | C   | D   | E   | F   | G   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 1   | 2   | 3   | inf | inf | inf |
| B   | inf | 0   | 1   | 2   | inf | inf | inf |
| C   | inf | inf | 0   | 1   | inf | inf | inf |
| D   | inf | inf | inf | 0   | inf | inf | inf |
| E   | inf | inf | inf | inf | 0   | 1   | 2   |
| F   | inf | inf | inf | inf | 1   | 0   | 1   |
| G   | inf | inf | inf | inf | 2   | 1   | 0   |

After the algorithm finishes, the distance matrix is:

|     | A   | B   | C   | D   | E   | F   | G   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 1   | 2   | 3   | 4   | 5   | 6   |
| B   | inf | 0   | 1   | 2   | 3   | 4   | 5   |
| C   | inf | inf | 0   | 1   | 2   | 3   | 4   |
| D   | inf | inf | inf | 0   | 1   | 2   | 3   |
| E   | inf | inf | inf | inf | 0   | 1   | 2   |
| F   | inf | inf | inf | inf | 1   | 0   | 1   |
| G   | inf | inf | inf | inf | 2   | 1   | 0   |

## Floyd's Algorithm

### Definition

Floyd's algorithm is an algorithm in graph theory that finds the shortest path between all pairs of vertices in a weighted graph. It is a dynamic programming algorithm that works by maintaining a matrix of shortest paths.

### Explanation

The algorithm starts by initializing a matrix of shortest paths, where the entry `d[i][j]` represents the shortest distance from vertex `i` to vertex `j`. The algorithm then scans the graph and updates the matrix of shortest paths. For each vertex `k`, it checks if the path from vertex `i` to vertex `j` through vertex `k` is shorter than the current shortest distance. If it is, it updates the matrix of shortest paths.

### Example

Suppose we have the following weighted graph:

```
  A --1--> B --2--> C --3--> D
  |    / |     |    / |
  |   /  |     |   /  |
  0  /   |     |  0  /   |
  | /    |     | /    |
  |/     |     |/     |
  --        --        --
  E        F        G
```

The matrix of shortest paths for this graph is:

|     | A   | B   | C   | D   | E   | F   | G   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 1   | 2   | 3   | inf | inf | inf |
| B   | inf | 0   | 1   | 2   | inf | inf | inf |
| C   | inf | inf | 0   | 1   | inf | inf | inf |
| D   | inf | inf | inf | 0   | inf | inf | inf |
| E   | inf | inf | inf | inf | 0   | 1   | 2   |
| F   | inf | inf | inf | inf | 1   | 0   | 1   |
| G   | inf | inf | inf | inf | 2   | 1   | 0   |

The algorithm updates the matrix of shortest paths as follows:

|     | A   | B   | C   | D   | E   | F   | G   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 1   | 2   | 3   | inf | inf | inf |
| B   | inf | 0   | 1   | 2   | inf | inf | inf |
| C   | inf | inf | 0   | 1   | inf | inf | inf |
| D   | inf | inf | inf | 0   | inf | inf | inf |
| E   | inf | inf | inf | inf | 0   | 1   | 2   |
| F   | inf | inf | inf | inf | 1   | 0   | 1   |
| G   | inf | inf | inf | inf | 2   | 1   | 0   |

After the algorithm finishes, the matrix of shortest paths is:

|     | A   | B   | C   | D   | E   | F   | G   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 1   | 2   | 3   | 4   | 5   | 6   |
| B   | inf | 0   | 1   | 2   | 3   | 4   | 5   |
| C   | inf | inf | 0   | 1   | 2   | 3   | 4   |
| D   | inf | inf | inf | 0   | 1   | 2   | 3   |
| E   | inf | inf | inf | inf | 0   | 1   | 2   |
| F   | inf | inf | inf | inf | 1   | 0   | 1   |
| G   | inf | inf | inf | inf | 2   | 1   | 0   |

## Key Concepts

- **Dynamic Programming**: Warshall's and Floyd's algorithms are examples of dynamic programming, which involves breaking down a problem into smaller subproblems and solving each subproblem only once.
- **Shortest Path**: The algorithms find the shortest path between all pairs of vertices in a weighted graph.
- **Distance Matrix**: The algorithms use a matrix of shortest paths to keep track of the shortest distances between vertices.

## Implementation

Here is an example implementation of Warshall's and Floyd's algorithms in Python:

```python
def warshall(W):
    n = len(W)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][k] + W[k][j] < W[i][j]:
                    W[i][j] = W[i][k] + W[k][j]

def floyd(W):
    n = len(W)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][k] + W[k][j] < W[i][j]:
                    W[i][j] = W[i][k] + W[k][j]

# Example usage:
W = [[0, 1, 2, 3], [float('inf'), 0, 1, 2], [float('inf'), float('inf'), 0, 1], [float('inf'), float('inf'), float('inf'), 0]]
warshall(W)
print("Warshall's algorithm:")
for row in W:
    print(row)

W = [[0, 1, 2, 3], [float('inf'), 0, 1, 2], [float('inf'), float('inf'), 0, 1], [float('inf'), float('inf'), float('inf'), 0]]
floyd(W)
print("Floyd's algorithm:")
for row in W:
    print(row)
```

## Applications

- **Network Routing**: Warshall's and Floyd's algorithms can be used to find the shortest path between all pairs of nodes in a network, which is useful for routing data packets.
- **GPS Navigation**: The algorithms can be used to find the shortest path between two points on a map, taking into account road distances and traffic conditions.
- **Database Query Optimization**: The algorithms can be used to optimize database queries by finding the shortest path between two tables in a database schema.

Note: This is a basic example of Warshall's and Floyd's algorithms. In real-world applications, you may need to consider additional factors such as traffic patterns, road closures, and other constraints.
