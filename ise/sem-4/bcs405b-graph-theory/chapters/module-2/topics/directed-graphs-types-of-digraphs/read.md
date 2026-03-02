# **Directed Graphs – Types of Digraphs**

## **Introduction**

A directed graph, also known as a digraph, is a type of graph that has directed edges between its vertices. Each edge in a digraph has a direction and can be thought of as a one-way path between two vertices. In this topic, we will explore the different types of digraphs and their characteristics.

## **Definition**

A digraph is a pair G = (V, E), where:

- V is the set of vertices (or nodes)
- E is the set of edges, and each edge (u, v) is an ordered pair of vertices

## **Types of Digraphs**

### 1. Directed Acyclic Graphs (DAGs)

A directed acyclic graph (DAG) is a digraph that has no cycles. A cycle in a digraph is a path that starts and ends at the same vertex, and passes through at least one edge.

**Example:** A DAG representing a workflow process is a digraph where each vertex represents a task, and each edge represents the dependency between tasks.

**Key Characteristics:**

- No cycles
- No multiple paths between any two vertices
- Can be represented using topological sort

### 2. Directed Cyclic Graphs (DCCs)

A directed cyclic graph (DCG) is a digraph that has cycles. A cycle in a digraph is a path that starts and ends at the same vertex, and passes through at least one edge.

**Example:** A DCG representing a voting process is a digraph where each vertex represents a voter, and each edge represents the voting preference of one voter for another.

**Key Characteristics:**

- Cycles
- Multiple paths between any two vertices
- Can be represented using depth-first search (DFS) or breadth-first search (BFS)

### 3. Bicyclic Graphs

A bicyclic graph is a digraph that has exactly two cycles. A bicycle is a cycle that contains only two edges.

**Example:** A bicyclic graph representing a social network is a digraph where each vertex represents a person, and each edge represents the friendship between two people.

**Key Characteristics:**

- Exactly two cycles
- Only two edges in each cycle
- Can be represented using DFS or BFS

### 4. Strongly Connected Graphs

A strongly connected graph is a digraph where there is a path from every vertex to every other vertex.

**Example:** A strongly connected graph representing a communication network is a digraph where each vertex represents a node, and each edge represents the communication channel between two nodes.

**Key Characteristics:**

- Path from every vertex to every other vertex
- Can be represented using DFS or BFS

### 5. Tournaments

A tournament is a digraph where every pair of vertices is connected by a directed edge.

**Example:** A tournament representing a sports league is a digraph where each vertex represents a team, and each edge represents the win or loss between two teams.

**Key Characteristics:**

- Every pair of vertices is connected
- Can be represented using adjacency matrix or adjacency list

## **Conclusion**

In this topic, we have explored the different types of digraphs, including DAGs, DCCs, bicyclic graphs, strongly connected graphs, and tournaments. Each type of digraph has its unique characteristics and applications in real-world scenarios. Understanding the properties of digraphs is essential for solving problems in graph theory and computer science.
