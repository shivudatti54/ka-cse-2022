# **Warshall's and Floyd's Algorithms**

## **Introduction**

In graph theory, Warshall's and Floyd's algorithms are used to find the shortest path between all pairs of vertices in a weighted graph. These algorithms are essential in solving problems related to connectivity and shortest paths in networks.

## **Warshall's Algorithm**

### Definition

Warshall's algorithm is a dynamic programming algorithm that finds the shortest path between all pairs of vertices in a weighted graph. It was first proposed by Robert C. Warshall in 1960.

### How it Works

The algorithm works by considering all possible paths between all pairs of vertices. It starts by considering the direct edges between all pairs of vertices. Then, it iterates over all vertices and updates the shortest path between all pairs of vertices by considering the paths through the current vertex.

### Example

Consider a weighted graph G = (V, E) with 3 vertices and 4 edges:

|     | A   | B   | C   |
| --- | --- | --- | --- | --- |
| A   | 0   | 3   | 7   | 0   |
| B   | 3   | 0   | 2   | 5   |
| C   | 7   | 2   | 0   | 9   |
| D   | 0   | 5   | 9   | 0   |

We want to find the shortest path between all pairs of vertices. We can use Warshall's algorithm to find the shortest paths as follows:

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| A   | 0   | 3   | 7   | 0   |
| B   | 3   | 0   | 2   | 5   |
| C   | 7   | 2   | 0   | 9   |
| D   | 0   | 5   | 9   | 0   |

**Key Concepts**

- The algorithm works by considering all possible paths between all pairs of vertices.
- The algorithm iterates over all vertices and updates the shortest path between all pairs of vertices by considering the paths through the current vertex.
- The algorithm uses dynamic programming to store the shortest paths between all pairs of vertices.

### Code

Here is an example implementation of Warshall's algorithm in Python:

```python
def warshall(graph):
    num_vertices = len(graph)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph

# Example usage:
graph = [[0, 3, 7, 0],
         [3, 0, 2, 5],
         [7, 2, 0, 9],
         [0, 5, 9, 0]]

warshall(graph)

# Print the shortest paths
for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j], end=" ")
    print()
```

## **Floyd's Algorithm**

### Definition

Floyd's algorithm is an efficient algorithm for finding the shortest path between all pairs of vertices in a weighted graph. It was first proposed by Robert W. Floyd in 1962.

### How it Works

The algorithm works by considering all possible paths between all pairs of vertices. It uses a matrix `dist` to store the shortest distances between all pairs of vertices. It iterates over all vertices and updates the shortest distances by considering the paths through the current vertex.

### Example

Consider a weighted graph G = (V, E) with 3 vertices and 4 edges:

|     | A   | B   | C   |
| --- | --- | --- | --- | --- |
| A   | 0   | 3   | 7   | 0   |
| B   | 3   | 0   | 2   | 5   |
| C   | 7   | 2   | 0   | 9   |
| D   | 0   | 5   | 9   | 0   |

We want to find the shortest path between all pairs of vertices. We can use Floyd's algorithm to find the shortest paths as follows:

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| A   | 0   | 3   | 7   | 0   |
| B   | 3   | 0   | 2   | 5   |
| C   | 7   | 2   | 0   | 9   |
| D   | 0   | 5   | 9   | 0   |

**Key Concepts**

- The algorithm works by considering all possible paths between all pairs of vertices.
- The algorithm uses a matrix `dist` to store the shortest distances between all pairs of vertices.
- The algorithm iterates over all vertices and updates the shortest distances by considering the paths through the current vertex.

### Code

Here is an example implementation of Floyd's algorithm in Python:

```python
def floyd(graph):
    num_vertices = len(graph)
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Initialize the distance matrix
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # Update the distance matrix
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage:
graph = [[0, 3, 7, 0],
         [3, 0, 2, 5],
         [7, 2, 0, 9],
         [0, 5, 9, 0]]

floyd(graph)

# Print the shortest paths
for i in range(len(graph)):
    for j in range(len(graph)):
        print(floyd(graph)[i][j], end=" ")
    print()
```

## **Comparison of Warshall's and Floyd's Algorithms**

|                      | Warshall's Algorithm                         | Floyd's Algorithm                               |
| -------------------- | -------------------------------------------- | ----------------------------------------------- |
| **Time Complexity**  | O(n^3)                                       | O(n^2)                                          |
| **Space Complexity** | O(n^2)                                       | O(n^2)                                          |
| **Implementation**   | Dynamic programming                          | Iterative approach                              |
| **Use Cases**        | Finding shortest paths in graphs with cycles | Finding shortest paths in graphs without cycles |

## **Conclusion**

Warshall's and Floyd's algorithms are two popular algorithms for finding the shortest path between all pairs of vertices in a weighted graph. While Warshall's algorithm has a higher time complexity, Floyd's algorithm is more efficient for graphs without cycles. The choice of algorithm depends on the specific use case and the properties of the graph.
