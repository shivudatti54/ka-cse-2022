# Semester-End Examination Guide: Data Structures & Applications (Module 5)

## Introduction

Congratulations on reaching the culmination of your studies in Module 5 of Data Structures and Applications! The semester-end examination is designed to evaluate your comprehensive understanding of the core concepts, your ability to apply them to solve problems, and your skill in analyzing the efficiency of different data structures. This guide will help you structure your revision, understand what is expected, and approach the exam with confidence.

## Core Concepts & Exam Focus Areas

Module 5 primarily deals with non-linear data structures, specifically **Graphs** and their algorithms. Your exam will likely test you on the following core areas:

### 1. Graph Fundamentals
*   **Definition:** A graph `G` is a set of vertices (`V`) and edges (`E`) connecting them. `G = (V, E)`.
*   **Terminology:** You must be thorough with terms like directed/undirected graphs, weighted/unweighted edges, path, cycle, degree, in-degree, out-degree, connected components, and complete graphs.
*   **Representation:** A fundamental question often asks you to represent a graph or compare representation methods.
    *   **Adjacency Matrix:** A 2D array of size `V x V`. `matrix[i][j] = 1` (or weight) if there is an edge from vertex `i` to vertex `j`.
        *   *Example:* For an undirected graph, the matrix will be symmetric.
    *   **Adjacency List:** An array of lists (or linked lists). Each index `i` stores a list of all vertices adjacent to vertex `i`.
        *   *Example:* For a graph with vertices `0, 1, 2` and edges `(0,1)` and `(0,2)`, the list at index `0` would be `[1, 2]`.

### 2. Graph Traversal Algorithms
These are cornerstone algorithms for exploring nodes and edges in a graph.

*   **Breadth-First Search (BFS):**
    *   **Concept:** Explores a graph level-by-level, starting from a source vertex. It uses a **queue**.
    *   **Applications:** Finding the shortest path in an unweighted graph, finding connected components, peer-to-peer networks.
    *   **Key Point:** It guarantees the shortest path in terms of the number of edges.

*   **Depth-First Search (DFS):**
    *   **Concept:** Explores as far as possible along a branch before backtracking. It uses a **stack** (often via recursion).
    *   **Applications:** Topological sorting, detecting cycles, solving puzzles with multiple moves (e.g., mazes).
    *   **Key Point:** Useful for exploring the entire structure of a graph.

### 3. Topological Sort
*   **Concept:** A linear ordering of the vertices of a **Directed Acyclic Graph (DAG)** such that for every directed edge `(u, v)`, vertex `u` comes before `v` in the ordering.
*   **Method:** Commonly performed using a modified DFS (by order of finishing time) or by using the in-degree of nodes (Kahn's Algorithm).
*   *Example:* Prerequisite tasks for a university course. You must complete CS101 (u) before taking DS202 (v). The topological sort will always list CS101 before DS202.

### 4. Minimum Spanning Tree (MST)
*   **Concept:** For a connected, undirected, weighted graph, an MST is a subset of edges that connects all vertices together without any cycles and with the minimum possible total edge weight.
*   **Prim's Algorithm:** Grows the MST one vertex at a time. It starts from an arbitrary vertex and always adds the cheapest edge that connects the current MST to a new vertex. Uses a **priority queue** for efficiency.
*   **Kruskal's Algorithm:** Adds the next cheapest edge that does not form a cycle. It uses a **union-find (disjoint set)** data structure to efficiently check for cycles.

### 5. Shortest Path Algorithms
*   **Dijkstra's Algorithm:** Finds the shortest path from a single source to all other vertices in a graph with **non-negative** edge weights. It uses a greedy strategy with a priority queue.
*   **Bellman-Ford Algorithm:** Also finds single-source shortest paths but can handle graphs **with negative weight edges**. It can also detect negative weight cycles. It is slower than Dijkstra's as it relaxes all edges `|V|-1` times.

## Exam Strategy & Summary

**Key Points to Remember:**
*   **Understand, Don't Memorize:** The exam will test your application skills. Focus on understanding *why* an algorithm works and *when* to use it.
*   **Time and Space Complexity:** Be prepared to state and compare the time complexity (`O(...)`) of all algorithms. This is a frequent question.
*   **Trace Algorithms:** You may be asked to manually trace an algorithm (e.g., "Perform Dijkstra's algorithm on the following graph..."). Practice this step-by-step.
*   **Differentiate:** Know the key differences between similar algorithms (e.g., Prim's vs. Kruskal's, Dijkstra's vs. Bellman-Ford, BFS vs. DFS).
*   **Pseudocode:** While you may not need to write full code, understanding the algorithm's steps in pseudocode is crucial for tracing and application questions.

**Summary of Core Algorithms:**
| Algorithm | Key Use Case | Data Structure Used | Note |
| :--- | :--- | :--- | :--- |
| **BFS** | Shortest path (unweighted graphs) | Queue | Level-order traversal |
| **DFS** | Cycle detection, topological sort | Stack (Recursion) | Explores depth-first |
| **Prim's / Kruskal's**| Finding MST | Priority Queue / Union-Find | For weighted, undirected graphs |
| **Dijkstra's** | Shortest path (non-negative weights) | Priority Queue | Greedy algorithm |
| **Bellman-Ford** | Shortest path (can handle negatives) | - | Can detect negative cycles |

Approach the exam systematically. Read questions carefully, draw diagrams to visualize problems, and clearly present your solutions. Good luck