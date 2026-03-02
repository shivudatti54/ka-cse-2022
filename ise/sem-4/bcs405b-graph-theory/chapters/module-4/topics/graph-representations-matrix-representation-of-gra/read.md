# **Graph Representations: Matrix Representation of Graphs**

## **Introduction**

In graph theory, a graph is a non-linear data structure consisting of nodes or vertices connected by edges. Representing graphs in a matrix format is a powerful tool for analyzing and manipulating graph properties. In this section, we will explore four common matrix representations of graphs:

- Adjacency Matrix
- Incidence Matrix
- Circuit Matrix
- Path Matrix

## **Adjacency Matrix**

An adjacency matrix is a matrix where the entry at row i and column j is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.

### Properties of Adjacency Matrix

- The matrix is square, with the same number of rows and columns as the number of vertices in the graph.
- The diagonal elements are always 0, since there is no edge between a vertex and itself.
- The matrix can be used to represent the graph in a matrix format.

### Example of Adjacency Matrix

Suppose we have a graph with 4 vertices (A, B, C, D) and the following edges:

- A -> B
- B -> C
- C -> D
- D -> A

The adjacency matrix for this graph would be:

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| A   | 0   | 1   | 0   | 1   |
| B   | 1   | 0   | 1   | 0   |
| C   | 0   | 1   | 0   | 1   |
| D   | 1   | 0   | 1   | 0   |

## **Incidence Matrix**

An incidence matrix is a matrix where the entry at row i and column j is 1 if vertex i is incident to edge j, and 0 otherwise.

### Properties of Incidence Matrix

- The matrix is square, with the same number of rows and columns as the number of vertices and edges in the graph.
- The diagonal elements are always 0, since a vertex is not incident to an edge.
- The matrix can be used to represent the graph in a matrix format.

### Example of Incidence Matrix

Suppose we have a graph with 4 vertices (A, B, C, D) and the following edges:

- A -> B
- B -> C
- C -> D
- D -> A

The incidence matrix for this graph would be:

|     | Edge 1 | Edge 2 | Edge 3 | Edge 4 |
| --- | ------ | ------ | ------ | ------ |
| A   | 1      | 0      | 0      | 1      |
| B   | 0      | 1      | 0      | 0      |
| C   | 0      | 0      | 1      | 0      |
| D   | 1      | 0      | 0      | 1      |

## **Circuit Matrix**

A circuit matrix is a matrix where the entry at row i and column j is 1 if vertex i is part of a circuit (a path that starts and ends at the same vertex), and 0 otherwise.

### Properties of Circuit Matrix

- The matrix is square, with the same number of rows and columns as the number of vertices in the graph.
- The diagonal elements are always 0, since a vertex is not part of a circuit.
- The matrix can be used to represent the graph in a matrix format.

### Example of Circuit Matrix

Suppose we have a graph with 4 vertices (A, B, C, D) and the following edges:

- A -> B -> C -> D -> A

The circuit matrix for this graph would be:

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| A   | 1   | 0   | 0   | 0   |
| B   | 0   | 1   | 1   | 0   |
| C   | 0   | 1   | 1   | 1   |
| D   | 0   | 0   | 1   | 1   |

## **Path Matrix**

A path matrix is a matrix where the entry at row i and column j is 1 if there is a path from vertex i to vertex j, and 0 otherwise.

### Properties of Path Matrix

- The matrix is square, with the same number of rows and columns as the number of vertices in the graph.
- The diagonal elements are always 0, since there is no path from a vertex to itself.
- The matrix can be used to represent the graph in a matrix format.

### Example of Path Matrix

Suppose we have a graph with 4 vertices (A, B, C, D) and the following edges:

- A -> B
- B -> C
- C -> D
- D -> A

The path matrix for this graph would be:

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| A   | 0   | 1   | 0   | 0   |
| B   | 0   | 0   | 1   | 0   |
| C   | 0   | 0   | 0   | 1   |
| D   | 1   | 0   | 0   | 0   |

## **Conclusion**

In this section, we have explored four common matrix representations of graphs: Adjacency Matrix, Incidence Matrix, Circuit Matrix, and Path Matrix. Each matrix has its own properties and can be used to represent the graph in a different way. Understanding these matrix representations is essential for analyzing and manipulating graph properties.
