# **Computer Networks Revision Notes: Shortest Path Algorithms**

### Introduction

- The Bellman-Ford and Path Vector Routing algorithms are used to find the shortest path between vertices in a weighted graph.
- These algorithms are essential in computer networks for routing data efficiently.

### Bellman-Ford Algorithm

- **Definition:** The Bellman-Ford algorithm is a dynamic programming algorithm that finds the shortest path from a source vertex to all other vertices in a weighted graph.
- **Formulas:**
  - f[v] = min{f[v] + w(e, u) | e is an edge from u to v, for all vertices u}
  - distance[v] = min{d[v] + w(e, u) | e is an edge from u to v, for all vertices u}

- **Theorems:**
  - The shortest path from a source vertex to a vertex u is unique if the graph does not contain negative-weight cycles.

- **Step-by-Step Procedure:**
  1.  Initialize distance[v] = infinity, for all vertices v, except the source vertex which is set to 0.
  2.  Relax all edges repeatedly.
  3.  If there is a negative-weight cycle, the algorithm will not terminate.

- **Example:**

  Given graph:

      0----1----2----3
      |    /     \    /
      |   /       \  /
      |  /         \/
      |/           >/

  Source vertex: 0
  Destination vertices: 1, 2, 3

  Shortest path distances:
  - 0->1: 1
  - 0->2: 3
  - 0->3: 5

### Path Vector Routing Algorithm

- **Definition:** The Path Vector Routing algorithm is a shortest path algorithm that uses a path vector to find the shortest path from a source vertex to all other vertices in a weighted graph.
- **Formulas:** The same as Bellman-Ford algorithm.
- **Theorems:** The same as Bellman-Ford algorithm.
- **Step-by-Step Procedure:**
  1.  Initialize distance[v] = infinity, for all vertices v, except the source vertex which is set to 0.
  2.  Initialize path vector [v] = [], for all vertices v.
  3.  Relax all edges repeatedly.
  4.  If there is a negative-weight cycle, the algorithm will not terminate.

- **Example:**

  Given graph:

      0----1----2----3
      |    /     \    /
      |   /       \  /
      |  /         \/
      |/           >/

  Source vertex: 0
  Destination vertices: 1, 2, 3

  Shortest path distances:
  - 0->1: 1
  - 0->2: 3
  - 0->3: 5

  Shortest path vectors:
  - [1] = [0, 1]
  - [2] = [0, 1, 2]
  - [3] = [0, 1, 2, 3]
