# Graph Representations: Matrix Representation of Graphs

### Overview

Matrix representation of graphs is a way to represent a graph using matrices. This provides a compact and efficient way to store and manipulate graph data.

### Key Points

- **Adjacency Matrix**
  - A matrix where each entry `a_ij` represents the edge between vertex `i` and vertex `j`.
  - If `a_ij = 1`, there is an edge between `i` and `j`.
  - If `a_ij = 0`, there is no edge between `i` and `j`.
  - **Formula:** `A = (a_{ij})` where `a_{ij} = 1 if (i, j) is an edge, 0 otherwise`
- **Incidence Matrix**
  - A matrix where each row represents a vertex and each column represents an edge.
  - A 1 in the matrix indicates that the vertex is incident to the edge.
  - **Formula:** `I = (b_{ij})` where `b_{ij} = 1 if vertex j is incident to edge i, 0 otherwise`
- **Circuit Matrix**
  - A matrix where each row represents a vertex and each column represents a vertex.
  - If the entry is 1, then the vertex is connected to the vertex in the row.
  - If the entry is -1, then the vertex is connected to the vertex in the row, but in the opposite direction.
  - **Formula:** `C = (c_{ij})` where `c_{ij} = 1 if vertex i is connected to vertex j, -1 otherwise`
- **Path Matrix**
  - A matrix where each row represents a vertex and each column represents a vertex.
  - If the entry is 1, then there is a path between the vertex in the row and the vertex in the column.
  - If the entry is 0, then there is no path between the vertex in the row and the vertex in the column.
  - **Formula:** `P = (p_{ij})` where `p_{ij} = 1 if there is a path between vertices i and j, 0 otherwise`

### Important Formulas and Definitions

- **Graph**: A set of vertices and edges that satisfy the following properties: (1) there are no multiple edges between any two vertices, and (2) there are no self-loops.
- **Adjacency**: Two vertices are said to be adjacent if they are connected by an edge.
- **Incidence**: A vertex is said to be incident to an edge if it is either the starting vertex or the ending vertex of the edge.
