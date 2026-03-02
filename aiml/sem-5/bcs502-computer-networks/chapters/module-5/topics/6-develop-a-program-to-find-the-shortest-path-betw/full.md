# **Developing a Program to Find the Shortest Path Between Vertices Using Bellman-Ford and Path Vector Routing Algorithm**

## **Introduction**

This paper provides a comprehensive guide to developing a program to find the shortest path between vertices using the Bellman-Ford and path vector routing algorithm. The Bellman-Ford algorithm is a graph search algorithm that finds the shortest path from a source vertex to all other vertices in a weighted graph. The path vector routing algorithm is a more general algorithm that can be used to find the shortest path between two vertices in a weighted graph.

## **Historical Context**

The Bellman-Ford algorithm was first introduced by Richard Bellman in 1958 as part of his Ph.D. thesis. The algorithm was later popularized by Robert Ford and Donald Fulkerson in 1958. The path vector routing algorithm has its roots in the work of Leonard Kleinrock, who developed the concept of routing algorithms in the 1960s.

## **Bellman-Ford Algorithm**

The Bellman-Ford algorithm is a graph search algorithm that finds the shortest path from a source vertex to all other vertices in a weighted graph. The algorithm works by maintaining a distance array that stores the shortest distance from the source vertex to each vertex in the graph.

### Algorithm Steps

1.  Initialize the distance array with infinity for all vertices except the source vertex, which is set to 0.
2.  Relax the edges of the graph by updating the distance array based on the edge weights.
3.  Repeat step 2 until the distance array no longer changes.
4.  If a negative weight cycle is detected, the algorithm terminates.

### Example

---

Suppose we have a weighted graph with vertices A, B, C, D, and E, and edges with weights as follows:

|     | A   | B   | C   | D   | E   |
| --- | --- | --- | --- | --- | --- |
| A   | 0   | 5   | ∞   | ∞   | ∞   |
| B   | ∞   | 0   | 3   | ∞   | ∞   |
| C   | ∞   | ∞   | 0   | 2   | ∞   |
| D   | ∞   | ∞   | ∞   | 0   | 1   |
| E   | ∞   | ∞   | ∞   | ∞   | 0   |

Suppose we want to find the shortest path from vertex A to all other vertices. We can initialize the distance array as follows:

|     | A   | B   | C   | D   | E   |
| --- | --- | --- | --- | --- | --- |
| A   | 0   | ∞   | ∞   | ∞   | ∞   |
| B   | ∞   | 0   | 3   | ∞   | ∞   |
| C   | ∞   | ∞   | 0   | 2   | ∞   |
| D   | ∞   | ∞   | ∞   | 0   | 1   |
| E   | ∞   | ∞   | ∞   | ∞   | 0   |

We can then relax the edges of the graph as follows:

|     | A   | B   | C   | D   | E   |
| --- | --- | --- | --- | --- | --- |
| A   | 0   | 5   | 7   | 8   | 9   |
| B   | ∞   | 0   | 3   | ∞   | ∞   |
| C   | ∞   | ∞   | 0   | 2   | ∞   |
| D   | ∞   | ∞   | ∞   | 0   | 1   |
| E   | ∞   | ∞   | ∞   | ∞   | 0   |

We can continue relaxing the edges until the distance array no longer changes. The final distance array will be:

|     | A   | B   | C   | D   | E   |
| --- | --- | --- | --- | --- | --- |
| A   | 0   | 5   | 7   | 8   | 9   |
| B   | ∞   | 0   | 3   | ∞   | ∞   |
| C   | ∞   | ∞   | 0   | 2   | ∞   |
| D   | ∞   | ∞   | ∞   | 0   | 1   |
| E   | ∞   | ∞   | ∞   | ∞   | 0   |

### Code Implementation

---

Here is an example implementation of the Bellman-Ford algorithm in Python:

```python
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def bellman_ford(self, source):
        distance = [float('inf')] * self.vertices
        distance[source] = 0

        for _ in range(self.vertices - 1):
            for u in range(self.vertices):
                for v in range(self.vertices):
                    if self.graph[u][v] != 0:
                        distance[v] = min(distance[v], distance[u] + self.graph[u][v])

        for u in range(self.vertices):
            for v in range(self.vertices):
                if self.graph[u][v] != 0:
                    if distance[v] > distance[u] + self.graph[u][v]:
                        print("Negative weight cycle detected")
                        return

        return distance

# Example usage
graph = Graph(5)
graph.graph = [[0, 5, 0, 0, 0],
              [0, 0, 3, 0, 0],
              [0, 0, 0, 2, 0],
              [0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0]]

distance = graph.bellman_ford(0)
print(distance)
```

## **Path Vector Routing Algorithm**

The path vector routing algorithm is a more general algorithm that can be used to find the shortest path between two vertices in a weighted graph. The algorithm works by maintaining a vector of paths from the source vertex to the destination vertex.

### Algorithm Steps

1.  Initialize the vector of paths with an empty path.
2.  Add the source vertex to the path.
3.  Relax the edges of the graph by adding the destination vertex to the path if the updated path is shorter than the current shortest path.
4.  Repeat step 3 until the destination vertex is reached.
5.  If a shorter path is found, update the vector of paths.

### Example

---

Suppose we have a weighted graph with vertices A, B, C, and D, and edges with weights as follows:

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| A   | 0   | 5   | ∞   | ∞   |
| B   | ∞   | 0   | 3   | ∞   |
| C   | ∞   | ∞   | 0   | 2   |
| D   | ∞   | ∞   | ∞   | 0   |

Suppose we want to find the shortest path from vertex A to vertex D. We can initialize the vector of paths as follows:

|     | A   | B   | C      | D         |
| --- | --- | --- | ------ | --------- |
| A   | []  | [A] | []     | []        |
| B   | []  | []  | [A, B] | []        |
| C   | []  | []  | []     | [A, B, C] |
| D   | []  | []  | []     | []        |

We can then relax the edges of the graph as follows:

|     | A   | B   | C      | D         |
| --- | --- | --- | ------ | --------- |
| A   | []  | [A] | []     | []        |
| B   | []  | []  | [A, B] | []        |
| C   | []  | []  | []     | [A, B, C] |
| D   | []  | []  | []     | []        |

We can continue relaxing the edges until the destination vertex D is reached. The final vector of paths will be:

|     | A   | B   | C      | D            |
| --- | --- | --- | ------ | ------------ |
| A   | []  | [A] | []     | [A, B, C, D] |
| B   | []  | []  | [A, B] | [A, B, C, D] |
| C   | []  | []  | []     | [A, B, C, D] |
| D   | []  | []  | []     | []           |

### Code Implementation

---

Here is an example implementation of the path vector routing algorithm in Python:

```python
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def path_vector_routing(self, source, destination):
        paths = [[] for _ in range(self.vertices)]
        paths[source] = [source]

        while len(paths[destination]) == 0:
            for u in range(self.vertices):
                for v in range(self.vertices):
                    if self.graph[u][v] != 0 and len(paths[u]) + 1 < len(paths[v]):
                        paths[v] = paths[u] + [v]

        return paths[destination]

# Example usage
graph = Graph(4)
graph.graph = [[0, 5, 0, 0],
              [0, 0, 3, 0],
              [0, 0, 0, 2],
              [0, 0, 0, 0]]

path = graph.path_vector_routing(0, 3)
print(path)
```

## **Comparison of Bellman-Ford and Path Vector Routing Algorithm**

Both the Bellman-Ford algorithm and the path vector routing algorithm can be used to find the shortest path between vertices in a weighted graph. However, there are some key differences between the two algorithms:

- **Complexity:** The Bellman-Ford algorithm has a higher complexity than the path vector routing algorithm. The Bellman-Ford algorithm has a time complexity of O(|E| \* |V|), while the path vector routing algorithm has a time complexity of O(|E| \* |V|) in the worst case, but it can be faster in practice.
- **Handling Negative Weight Edges:** The Bellman-Ford algorithm can handle negative weight edges, while the path vector routing algorithm cannot.
- **Handling Negative Weight Cycles:** The Bellman-Ford algorithm can detect negative weight cycles, while the path vector routing algorithm cannot.

## **Applications**

Both the Bellman-Ford algorithm and the path vector routing algorithm have a wide range of applications in computer networks, including:

- **Routing Protocols:** Both algorithms can be used to find the shortest path between two vertices in a weighted graph, which is useful in routing protocols such as OSPF and IS-IS.
- **Network Optimization:** Both algorithms can be used to optimize network performance by finding the shortest path between two vertices in a weighted graph.
- **Traffic Engineering:** Both algorithms can be used to optimize traffic flow in networks by finding the shortest path between two vertices in a weighted graph.

## **Further Reading**

- **"Algorithms" by Robert Sedgewick and Kevin Wayne:** This book provides a comprehensive introduction to algorithms, including the Bellman-Ford algorithm and the path vector routing algorithm.
- **"Computer Networks" by Andrew S. Tanenbaum and David J. Wetherall:** This book provides a comprehensive introduction to computer networks, including routing protocols and network optimization.
- **"Traffic Engineering" by Harald König and Anna Touati:** This book provides a comprehensive introduction to traffic engineering, including traffic flow optimization using the Bellman-Ford algorithm and the path vector routing algorithm.
