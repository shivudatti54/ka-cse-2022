**Topic 6: Develop a Program to Find the Shortest Path between Vertices using Bellman-Ford and Path Vector Routing Algorithm**

**Introduction**

In computer networks, finding the shortest path between vertices is a crucial task in many applications such as network routing, traffic optimization, and resource allocation. This topic will focus on two algorithms to solve this problem: Bellman-Ford and path vector routing algorithm.

**What is Shortest Path Problem?**

The shortest path problem is a classic problem in graph theory and computer science. Given a weighted graph, it is asked to find the path between two vertices that has the minimum total weight.

**Bellman-Ford Algorithm**

Bellman-Ford algorithm is a dynamic programming algorithm used to find the shortest path from a source vertex to all other vertices in a weighted graph. It is an improvement over Dijkstra's algorithm as it can handle negative weight edges.

**How Bellman-Ford Algorithm Works**

The steps involved in Bellman-Ford algorithm are:

- Initialize the distance of the source vertex to 0 and all other vertices to infinity.
- Relax all edges repeatedly.
- Check for negative cycles.

**Example**

Suppose we have the following graph:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

We want to find the shortest path from A to all other vertices. The weights of the edges are:

|     | A   | B   | C   | D   | E   | F   |
| --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 5   | 3   | inf | inf | inf |
| B   | inf | 0   | 2   | 1   | inf | inf |
| C   | inf | inf | 0   | inf | 4   | inf |
| D   | inf | 1   | inf | 0   | 2   | 1   |
| E   | inf | inf | 4   | 2   | 0   | 3   |
| F   | inf | inf | inf | 1   | 3   | 0   |

We can use Bellman-Ford algorithm to find the shortest path from A to all other vertices.

```
Vertex  | Distance
--------|---------
A       | 0
B       | 5
C       | 3
D       | 6
E       | 5
F       | 4
```

**Path Vector Routing Algorithm**

Path vector routing algorithm is a routing algorithm used in computer networks to find the shortest path between two vertices. It is an extension of Bellman-Ford algorithm.

**How Path Vector Routing Algorithm Works**

The steps involved in path vector routing algorithm are:

- Initialize the distance of the source vertex to 0 and all other vertices to infinity.
- Relax all edges repeatedly.
- Check for negative cycles.
- If a negative cycle is found, the algorithm terminates.

**Example**

Suppose we have the following graph:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

We want to find the shortest path from A to all other vertices. The weights of the edges are:

|     | A   | B   | C   | D   | E   | F   |
| --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 5   | 3   | inf | inf | inf |
| B   | inf | 0   | 2   | 1   | inf | inf |
| C   | inf | inf | 0   | inf | 4   | inf |
| D   | inf | 1   | inf | 0   | 2   | 1   |
| E   | inf | inf | 4   | 2   | 0   | 3   |
| F   | inf | inf | inf | 1   | 3   | 0   |

We can use path vector routing algorithm to find the shortest path from A to all other vertices.

```
Vertex  | Distance
--------|---------
A       | 0
B       | 5
C       | 3
D       | 6
E       | 5
F       | 4
```

**Implementation**

Here is a Python implementation of both algorithms:

```python
import sys
import heapq

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))

    def bellman_ford(self, source):
        distances = [sys.maxsize] * self.num_vertices
        distances[source] = 0

        for _ in range(self.num_vertices - 1):
            for u in range(self.num_vertices):
                for v, weight in self.adj_list[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        for u in range(self.num_vertices):
            for v, weight in self.adj_list[u]:
                if distances[u] + weight < distances[v]:
                    print("Negative cycle detected")
                    return None

        return distances

    def path_vector_routing(self, source):
        distances = [sys.maxsize] * self.num_vertices
        distances[source] = 0

        for _ in range(self.num_vertices - 1):
            for u in range(self.num_vertices):
                for v, weight in self.adj_list[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        # Check for negative cycles
        for u in range(self.num_vertices):
            for v, weight in self.adj_list[u]:
                if distances[u] + weight < distances[v]:
                    print("Negative cycle detected")
                    return None

        return distances

# Example usage
graph = Graph(6)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 2)
graph.add_edge(2, 4, 4)
graph.add_edge(3, 5, 3)
graph.add_edge(3, 5, 1)
graph.add_edge(4, 5, 2)

print("Bellman-Ford distances:")
print(graph.bellman_ford(0))

print("\nPath Vector Routing distances:")
print(graph.path_vector_routing(0))
```

This code creates a graph with 6 vertices and adds edges with weights. It then uses both Bellman-Ford and path vector routing algorithms to find the shortest path from vertex 0 to all other vertices.
