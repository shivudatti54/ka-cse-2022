# **Developing Shortest Path Algorithms: Bellman-Ford and Path Vector Routing**

### Introduction

---

In computer networks, finding the shortest path between vertices is crucial for efficient data transfer and communication. Two popular algorithms for this purpose are the Bellman-Ford and path vector routing algorithms. In this study material, we will explore these algorithms, their working principles, and implement them in a program.

### What is the Bellman-Ford Algorithm?

---

The Bellman-Ford algorithm is a graph search algorithm that can find the shortest path from a source vertex to all other vertices in a weighted graph. It was designed by Robert Bellman and is an extension of Dijkstra's algorithm.

### How the Bellman-Ford Algorithm Works

---

Here are the steps involved in the Bellman-Ford algorithm:

- Initialize the distance to the source vertex as 0 and all other vertices as infinity.
- Relax the edges repeatedly.
- If the distance to a vertex can be improved, update its distance.
- Repeat steps 2-3 until the distance to all vertices is updated or the graph becomes negative-weight.

### Example of the Bellman-Ford Algorithm

---

Suppose we have a graph with vertices A, B, C, and D, and edges with weights as follows:

|     | A -> B | A -> C | B -> C | C -> D |
| --- | ------ | ------ | ------ | ------ |
|     | 2      | 4      | 1      | 3      |
|     | 0      | 0      | 0      | 0      |

We want to find the shortest path from vertex A to all other vertices.

|     | A -> B | A -> C | B -> C | C -> D |
| --- | ------ | ------ | ------ | ------ | --------------------------- |
|     | 0      | 0      | 0      | 0      | (distances to all vertices) |

We relax the edges repeatedly:

1.  Relax edge A -> B: 0 + 2 = 2 (update distance to B)
2.  Relax edge A -> C: 0 + 4 = 4 (update distance to C)
3.  Relax edge B -> C: 2 + 1 = 3 (update distance to C)
4.  Relax edge C -> D: 4 + 3 = 7 (update distance to D)

|     | A -> B | A -> C | B -> C | C -> D |
| --- | ------ | ------ | ------ | ------ | --- |
|     | 0      | 0      | 0      | 0      | 7   |

### How to Implement the Bellman-Ford Algorithm

---

Here is a simple implementation of the Bellman-Ford algorithm in Python:

```python
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative-weight cycle")
                return

        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

# Example usage:
g = Graph(4)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)

g.bellman_ford(0)
```

### What is Path Vector Routing?

---

Path vector routing is a routing algorithm used in packet switching networks to find the shortest path between a sender and a receiver. It is similar to the Bellman-Ford algorithm but is specifically designed for packet switching networks.

### How Path Vector Routing Works

---

Path vector routing works by maintaining a list of packets and their corresponding routes. When a packet is sent, the network checks the route of each packet to determine the next hop.

### Example of Path Vector Routing

---

Suppose we have a network with three routers R1, R2, and R3, and three packets P1, P2, and P3. The packets have the following routes:

|     | P1 -> R1 | P1 -> R2 | P1 -> R3 |
| --- | -------- | -------- | -------- |
|     | 2        | 3        | 1        |
|     | 0        | 0        | 0        |

To find the shortest path for packet P1, we evaluate the routes of each packet:

|     | P1 -> R1 | P1 -> R2 | P1 -> R3 |
| --- | -------- | -------- | -------- | --------------- |
|     | 0        | 0        | 0        | (shortest path) |

### How to Implement Path Vector Routing

---

Here is a simple implementation of path vector routing in Python:

```python
class PathVectorRouting:
    def __init__(self, routers):
        self.routers = routers

    def find_shortest_path(self, packet):
        shortest_path = None
        min_distance = float("Inf")

        for router in self.routers:
            distance = router.get_distance(packet)

            if distance < min_distance:
                min_distance = distance
                shortest_path = router.get_route(packet)

        return shortest_path

# Example usage:
class Router:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, packet, distance):
        self.routes[packet] = distance

    def get_distance(self, packet):
        return self.routes[packet]

    def get_route(self, packet):
        return self.routes[packet]

routers = [Router("R1"), Router("R2"), Router("R3")]
routers[0].add_route("P1", 2)
routers[0].add_route("P1", 3)
routers[1].add_route("P1", 3)
routers[1].add_route("P1", 0)
routers[2].add_route("P1", 1)

routing = PathVectorRouting(routers)
shortest_path = routing.find_shortest_path("P1")
print(shortest_path)
```

### Conclusion

---

In this study material, we have explored the Bellman-Ford and path vector routing algorithms, their working principles, and implemented them in a program. We have also discussed the differences between these algorithms and their applications in computer networks.
