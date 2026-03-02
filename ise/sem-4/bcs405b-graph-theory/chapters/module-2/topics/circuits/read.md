# **Circuits**

## **Introduction**

In graph theory, a circuit is a path in a graph that starts and ends at the same vertex, and passes through at least one edge more than once. Circuits are also known as cycles or loops. In this section, we will explore the concept of circuits in graph theory, including definitions, types of circuits, and examples.

## **Definition**

A circuit is a path in a graph that satisfies the following conditions:

- The path starts and ends at the same vertex.
- The path passes through at least one edge more than once.
- The path does not form a loop that only contains one edge.

## **Types of Circuits**

There are two main types of circuits:

- **Simple Circuit**: A simple circuit is a circuit that passes through at least two edges.
- **Multiple Circuit**: A multiple circuit is a circuit that passes through all the edges of a graph.

## **Eulerian Circuit**

An Eulerian circuit is a circuit in a graph that visits every edge exactly once. An Eulerian circuit is also known as a Eulerian path if it has an odd number of edges.

**Characteristics of Eulerian Circuit**

- The graph must be connected.
- The graph must have at least two vertices with even degree.
- The graph must have an Eulerian circuit if and only if it has at most two vertices with odd degree.

## **Hamiltonian Circuit**

A Hamiltonian circuit is a circuit in a graph that visits every vertex exactly once.

**Characteristics of Hamiltonian Circuit**

- The graph must be connected.
- The graph must have at least three vertices.
- The graph must have a Hamiltonian circuit if and only if it is a tree or a forest.

## **Operations on Graphs**

Graphs can be manipulated using various operations, including:

- **Union of graphs**: The union of two graphs is a graph that contains all the vertices and edges of both graphs.
- **Intersection of graphs**: The intersection of two graphs is a graph that contains only the vertices and edges that are common to both graphs.
- **Complement of a graph**: The complement of a graph is a graph that contains all the vertices and edges of the original graph, but with the opposite edge relationship.

## **Key Concepts**

- **Vertex**: A vertex is a point in a graph.
- **Edge**: An edge is a line that connects two vertices in a graph.
- **Degree**: The degree of a vertex is the number of edges that connect to it.
- **Path**: A path is a sequence of edges and vertices in a graph.
- **Circuit**: A circuit is a path that starts and ends at the same vertex, and passes through at least one edge more than once.

## **Examples**

- Consider a graph with four vertices {A, B, C, D} and four edges {AB, BC, CD, DA}.
  - The graph is connected and has a circuit {A -> B -> C -> D -> A}.
  - The graph is not Eulerian because it has an odd number of edges at vertex A.
- Consider a graph with three vertices {A, B, C} and three edges {AB, BC, CA}.
  - The graph is connected and has a Hamiltonian circuit {A -> B -> C -> A}.

## **Practice Problems**

- Find a circuit in the graph with five vertices {A, B, C, D, E} and five edges {AB, BC, CD, DE, EA}.
- Determine if the graph with four vertices {A, B, C, D} and four edges {AB, BC, CD, DA} is Eulerian or not.

## **Conclusion**

In this section, we have explored the concept of circuits in graph theory, including definitions, types of circuits, and examples. We have also discussed operations on graphs and key concepts such as vertex, edge, degree, path, and circuit. With this knowledge, you should be able to analyze and solve problems involving circuits in graph theory.
