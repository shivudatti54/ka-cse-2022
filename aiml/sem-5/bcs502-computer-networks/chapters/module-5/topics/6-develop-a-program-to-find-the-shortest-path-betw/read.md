# **Shortest Path Algorithms in Computer Networks**

## **6. Develop a program to find the shortest path between vertices using the Bellman-Ford and path vector routing algorithm**

## **Introduction**

In computer networks, finding the shortest path between two nodes (vertices) is a common problem in network design, optimization, and fault-tolerant routing. This study material will cover two popular algorithms for solving this problem: the Bellman-Ford algorithm and the path vector routing algorithm.

## **What are Shortest Path Algorithms?**

A shortest path algorithm is a technique used to find the minimum-weight path between two nodes in a weighted graph or network. These algorithms are essential in computer networks, as they help in optimizing network design, traffic routing, and fault-tolerant routing.

## **Bellman-Ford Algorithm**

### Definition

The Bellman-Ford algorithm is a dynamic programming algorithm for finding the shortest path from a source vertex to all other vertices in a weighted graph. It can handle negative-weight edges, making it suitable for finding the shortest path in graphs with negative cycles.

### How it Works

1.  Initialize the distance to the source vertex as 0, and all other vertices as infinity.
2.  Relax the edges repeatedly, updating the distance to each vertex if a shorter path is found.
3.  Repeat step 2 for all vertices (except the source vertex) until no further updates are made.

### Example

Suppose we have a graph with vertices A, B, C, and D, and edges with weights:

- A -> B: 2
- B -> C: 3
- C -> D: -2
- A -> C: 4

If we run the Bellman-Ford algorithm from vertex A, we get:

- Distance from A to A: 0
- Distance from A to B: 2
- Distance from A to C: 4
- Distance from A to D: 6

After relaxing the edges, we get:

- Distance from A to B: 2
- Distance from A to C: 4
- Distance from A to D: 6
- Distance from B to C: 5
- Distance from B to D: 3
- Distance from C to D: -2

Notice that the distance to vertex D is now -2, which is shorter than the initial value of 6.

## **Code Implementation of Bellman-Ford Algorithm**

```python
import sys

def bellman_ford(graph, source):
    # Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Relax edges
    for _ in range(len(graph) - 1):
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative-weight cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Graph contains a negative-weight cycle")
            return

    return distances

# Example usage
graph = [(0, 1, 2), (1, 2, 3), (0, 2, -2), (1, 3, 4)]
source_vertex = 0
distances = bellman_ford(graph, source_vertex)
print(distances)
```

## **Path Vector Routing Algorithm**

### Definition

The path vector routing algorithm is a dynamic programming algorithm for finding the shortest path between two nodes in a network. It uses a path vector to store the shortest path from the source node to all other nodes.

### How it Works

1.  Initialize the path vector with the source node.
2.  For each node, compute the shortest path from the source node to that node using the path vector.
3.  Update the path vector with the shortest path from the current node to all other nodes.

### Example

Suppose we have a network with nodes A, B, C, and D, and edges with weights:

- A -> B: 2
- B -> C: 3
- C -> D: -2
- A -> C: 4

If we run the path vector routing algorithm from node A, we get:

- Path vector: [A] -> [A, B] -> [A, B, C] -> [A, B, C, D]

After updating the path vector, we get:

- Path vector: [A] -> [A, B] -> [A, B, C] -> [A, B, C, D] -> [A, B, C, D]

Notice that the path vector now contains all nodes in the shortest path between nodes A and D.

## **Code Implementation of Path Vector Routing Algorithm**

```python
import sys

def path_vector_routing(graph, source):
    # Initialize path vector
    path_vector = {vertex: [source] for vertex in graph}

    # Compute shortest path to each node
    for _ in range(len(graph)):
        for u, v, weight in graph:
            if len(path_vector[u]) < len(path_vector[v]):
                path_vector[v] = path_vector[u] + [v]

    return path_vector

# Example usage
graph = [(0, 1, 2), (1, 2, 3), (0, 2, -2), (1, 3, 4)]
source_node = 0
path_vector = path_vector_routing(graph, source_node)
print(path_vector)
```

## **Conclusion**

In this study material, we covered two popular shortest path algorithms: the Bellman-Ford algorithm and the path vector routing algorithm. We defined each algorithm, explained how they work, and provided examples to illustrate their usage. We also provided code implementations for each algorithm in Python. These algorithms are essential in computer networks, as they help in optimizing network design, traffic routing, and fault-tolerant routing.
