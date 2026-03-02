# Semester-End Examination Guide: Data Structures and Applications (Module 5)

## Introduction

The Semester-End Examination is the comprehensive assessment of your understanding of the entire course on Data Structures and Applications. Module 5, often covering advanced non-linear data structures like Graphs and their algorithms, is a critical component that frequently appears in the exam. This guide will help you understand the core concepts from this module, explain how they are typically examined, and provide strategies for effective preparation.

## Core Concepts & Their Examination

Questions from Module 5 are designed to test your conceptual understanding, analytical skills, and ability to apply algorithms to solve problems.

### 1. Graphs: Representation and Terminology
This is foundational. You must be able to define and illustrate key terms:
*   **Graph (G = {V, E})**: A set of vertices (V) and edges (E).
*   **Directed vs. Undirected Graphs**: Know the difference. An edge (u, v) in a directed graph is not the same as (v, u).
*   **Path, Cycle, Connected Components**: Be prepared to identify these in a given graph.

**Exam Focus:** You might be asked to represent a given graph using an **Adjacency Matrix** or an **Adjacency List**. Understand the trade-offs: the matrix offers O(1) lookups but consumes O(V²) space, while the list is space-efficient (O(V+E)) but lookups are slower.

**Example:**
*   *Question:* "Represent the following graph using an adjacency list."
    *(A graph with vertices {0,1,2} and edges: 0->1, 0->2, 1->2)*
*   *Answer:*
    *   0 -> 1 -> 2
    *   1 -> 2
    *   2 -> [ ]

### 2. Graph Traversal Algorithms
A major part of the exam involves applying Breadth-First Search (BFS) and Depth-First Search (DFS).

*   **BFS:** Uses a queue. Explores level-by-level. Ideal for finding the **shortest path** in an unweighted graph.
*   **DFS:** Uses a stack (recursion). Explores as far as possible along a branch before backtracking. Useful for cycle detection, topological sorting, and exploring connected components.

**Exam Focus:** You will almost certainly be asked to **execute BFS or DFS** on a given graph, providing the order of vertex visitation. Remember to track the `visited` state to avoid loops.

**Example:**
*   *Question:* "Perform BFS starting from vertex A." (A graph will be provided).
*   *Answer:* You must show the queue's state at each step and the final visitation order (e.g., A, B, C, D).

### 3. Applications of Graph Algorithms
You need to understand *why* and *how* these algorithms are used.

*   **Topological Sort:** A linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge (u -> v), u comes before v. **Implementation:** Uses DFS with a stack.
*   **Minimum Spanning Tree (MST):** For a connected, undirected, weighted graph, an MST is a subset of edges that connects all vertices with the minimum total edge weight.
    *   **Prim's Algorithm:** Starts from a single vertex and grows the MST by adding the cheapest connecting edge.
    *   **Kruskal's Algorithm:** Sorts all edges and adds them to the MST if they don't form a cycle (using Union-Find data structure).
*   **Shortest Path Algorithms:**
    *   **Dijkstra's Algorithm:** Finds the shortest path from a source node to all other nodes in a weighted graph **with non-negative weights**. It uses a priority queue.

**Exam Focus:** You may be asked to **step through** Prim's, Kruskal's, or Dijkstra's algorithm on a small graph, showing the state of the solution (e.g., the MST or the distance array) after each iteration.

## Key Points & Summary

*   **Understand, Don't Memorize:** Focus on the underlying principles of each algorithm. Why does BFS use a queue? Why can't Dijkstra's handle negative weights?
*   **Practice Diagrammatically:** Draw the graphs and walk through the algorithms by hand. This is exactly what you'll do in the exam.
*   **Time/Space Complexity:** Be prepared to state and compare the time and space complexity of each algorithm (e.g., BFS/DFS: O(V+E), Dijkstra with min-heap: O((V+E) log V)).
*   **Identify the Right Tool:** Exam problems often present a scenario (e.g., "find the shortest network cable layout" or "find the fastest path"). You must identify that this requires MST or Dijkstra's algorithm, respectively.
*   **Exam Strategy:**
    1.  **Read the question carefully.** Note the starting vertex and the graph type (directed/undirected, weighted/unweighted).
    2.  **Show your work clearly.** For traversal or algorithm steps, draw tables to track the queue, visited nodes, distances, or the MST set.
    3.  **Write legibly.** A well-presented answer is easier to mark.

Mastering these concepts and their practical application is key to performing well in the Semester-End Examination. Consistent practice with problem-solving is the most effective method of preparation.