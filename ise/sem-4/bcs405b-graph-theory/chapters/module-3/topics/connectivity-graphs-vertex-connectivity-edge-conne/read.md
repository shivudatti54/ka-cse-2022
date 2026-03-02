# **Connectivity Graphs: Vertex Connectivity, Edge Connectivity, Cut set and Cut Vertices, Fundamental circuits**

## **Introduction**

In graph theory, connectivity graphs are studied to understand the connectivity between different parts of a graph. This topic is crucial in various fields such as computer science, networking, and graph theory. In this study material, we will cover the key concepts of connectivity graphs, including vertex connectivity, edge connectivity, cut sets, cut vertices, and fundamental circuits.

## **Vertex Connectivity**

Vertex connectivity is a measure of how connected a graph is, in terms of the removal of vertices. It is defined as:

- **Vertex Connectivity (δ(v))**: The minimum number of vertices that need to be removed from a graph to disconnect it.

### Definition

Given a graph G = (V, E), the vertex connectivity of a vertex v ∈ V is defined as:

δ(v) = min { |A| : v ∈ A, A is a cut set in G }

### Explanation

A cut set is a set of vertices whose removal disconnects the graph. The vertex connectivity of a vertex v is the minimum size of such a cut set.

### Example

Consider a graph G = (V, E) with the following vertices and edges:

V = {u, v, w, x}
E = {uv, vw, vw, vx, wx}

The vertex connectivity of vertex u is 1, since removing either vertex v or w will disconnect the graph.

## **Edge Connectivity**

Edge connectivity is a measure of how connected a graph is, in terms of the removal of edges. It is defined as:

- **Edge Connectivity (δ(e))**: The minimum number of edges that need to be removed from a graph to disconnect it.

### Definition

Given a graph G = (V, E), the edge connectivity of an edge e ∈ E is defined as:

δ(e) = min { |A| : e ∈ A, A is an edge cut in G }

### Explanation

An edge cut is a set of edges whose removal disconnects the graph. The edge connectivity of an edge e is the minimum size of such an edge cut.

### Example

Consider a graph G = (V, E) with the following vertices and edges:

V = {u, v, w, x}
E = {uv, vw, vw, vx, wx}

The edge connectivity of edge uv is 2, since removing either edge vw or wx will disconnect the graph.

## **Cut Set and Cut Vertices**

A cut set and cut vertices are closely related concepts in graph theory.

- **Cut Set**: A set of vertices whose removal disconnects the graph.

### Definition

Given a graph G = (V, E), a cut set in G is:

- A subset S of V such that G - S is not connected.

### Explanation

A cut set is a set of vertices that must be removed to disconnect the graph.

- **Cut Vertex**: A vertex that, when removed, increases the size of a cut set.

### Definition

Given a graph G = (V, E), a cut vertex in G is a vertex v ∈ V such that δ(v) = 1.

### Explanation

A cut vertex is a vertex that is essential for the connectivity of the graph.

### Example

Consider a graph G = (V, E) with the following vertices and edges:

V = {u, v, w, x}
E = {uv, vw, vw, vx, wx}

The cut set of vertex u is {u}, since removing u will disconnect the graph.

## **Fundamental Circuits**

A fundamental circuit is a circuit in a connected graph that is not contained in any other circuit.

- **Fundamental Circuit**: A circuit in a connected graph that is not contained in any other circuit.

### Definition

Given a connected graph G = (V, E), a fundamental circuit in G is a circuit C in G such that there is no other circuit C' in G with C ⊂ C'.

### Explanation

A fundamental circuit is a circuit that is not contained in any other circuit.

### Example

Consider a graph G = (V, E) with the following vertices and edges:

V = {u, v, w, x}
E = {uv, vw, vw, vx, wx}

The fundamental circuit of graph G is {uv, vw, wx}, since it is not contained in any other circuit.

## **Key Concepts**

- Vertex Connectivity (δ(v)): The minimum number of vertices that need to be removed from a graph to disconnect it.
- Edge Connectivity (δ(e)): The minimum number of edges that need to be removed from a graph to disconnect it.
- Cut Set: A set of vertices whose removal disconnects the graph.
- Cut Vertex: A vertex that, when removed, increases the size of a cut set.
- Fundamental Circuit: A circuit in a connected graph that is not contained in any other circuit.
