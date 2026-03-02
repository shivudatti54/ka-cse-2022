Of course. Here is comprehensive educational content on the specified topics for  Engineering students.

# Module 2: Travelling Salesman Problem & Directed Graphs

## 1. Introduction

Graph Theory provides powerful tools to model and solve complex real-world problems in computer networks, logistics, circuit design, and operations research. This module focuses on two crucial concepts: the **Travelling Salesman Problem (TSP)**, a famous optimization problem, and **Directed Graphs (Digraphs)**, which extend the concept of graphs to model relationships with inherent direction.

---

## 2. Core Concepts & Explanation

### A. Travelling Salesman Problem (TSP)

The Travelling Salesman Problem is one of the most well-known and intensely studied problems in computational mathematics and graph theory.

- **Problem Statement:** Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city **exactly once** and returns to the origin city?
- **Graph Model:** The problem is modeled using a **weighted complete graph**. The cities are represented as vertices, the connections between them are edges, and the distance (or cost) between two cities is the weight assigned to the edge connecting them.
- **The Challenge:** The primary challenge with TSP is its computational complexity. For `n` cities, there are `(n-1)! / 2` possible Hamiltonian cycles (for a symmetric TSP). This number grows factorially, making a brute-force approach infeasible for even a modest number of cities (e.g., 20 cities have over 60 quadrillion possible routes). Therefore, TSP is classified as an **NP-Hard** problem.
- **Solution Approaches:**
  - **Exact Algorithms:** Algorithms like **Branch and Bound** or using **Integer Linear Programming** can find the optimal solution for small instances but become impractical for large `n`.
  - **Approximation Algorithms:** These algorithms do not guarantee the optimal solution but provide a "good enough" solution in polynomial time. Examples include the **Nearest Neighbor** heuristic and the **Christofides Algorithm**.
  - **Metaheuristics:** For large problems, techniques like **Genetic Algorithms**, **Simulated Annealing**, and **Ant Colony Optimization** are often used to find high-quality solutions.

**Example:** Consider a salesman who must visit cities A, B, C, and D. The distance matrix is:

|       | A   | B   | C   | D   |
| :---- | :-- | :-- | :-- | :-- |
| **A** | 0   | 10  | 15  | 20  |
| **B** | 10  | 0   | 35  | 25  |
| **C** | 15  | 35  | 0   | 30  |
| **D** | 20  | 25  | 30  | 0   |

A possible Hamiltonian cycle is `A -> B -> D -> C -> A` with a total cost of `10 + 25 + 30 + 15 = 80`. The goal is to find the cycle with the minimum possible cost.

### B. Directed Graphs (Digraphs)

A Directed Graph or **Digraph** `D` consists of a set of vertices `V` and a set of **ordered pairs** of vertices called **arcs** or **directed edges**. The key difference from an ordinary graph is that the edge `(u, v)` is distinct from the edge `(v, u)`; it has a direction from `u` (the tail) to `v` (the head).

- **Basic Terminology:**
  - **Out-degree:** The number of arcs directed **from** a vertex.
  - **In-degree:** The number of arcs directed **towards** a vertex.
  - **Adjacency:** If there is an arc `(u, v)`, then `v` is **adjacent from** `u`, and `u` is **adjacent to** `v`.

#### Types of Digraphs

1.  **Simple Directed Graph:** A digraph with no self-loops (arcs from a vertex to itself) and no multiple arcs in the same direction between the same pair of vertices.
2.  **Directed Multigraph:** A digraph that allows **multiple arcs** between the same pair of vertices in the same direction. This is useful for modeling multiple relationships, like multiple flights between the same two airports.
3.  **Oriented Graph (Tournament):** A directed graph obtained by assigning a direction to each edge of a simple undirected graph. A **complete oriented graph** (where every pair of distinct vertices is connected by a single directed edge) is called a **tournament**.
4.  **Symmetric Digraph:** A digraph where for every arc `(u, v)`, the reverse arc `(v, u)` is also present. This essentially mimics an undirected graph.
5.  **Rooted Tree:** A directed tree where one vertex, the **root**, has an in-degree of 0, and all other vertices have an in-degree of 1. This is the standard model for hierarchical structures like file systems or organizational charts.
6.  **Directed Acyclic Graph (DAG):** A digraph with **no directed cycles**. This is a profoundly important structure in computer science for representing dependencies (e.g., task scheduling, dataflow graphs, version history).

**Example:** A simple social network digraph where vertices represent people and an arc `(A, B)` means "Person A follows Person B". Here, the in-degree of B is their number of followers, and the out-degree of A is the number of people they follow.

---

## 3. Key Points / Summary

| Concept      | Key Takeaways                                                                                                                                                                                                                                                                                                                                             |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TSP**      | - An **NP-Hard** optimization problem to find the shortest **Hamiltonian cycle** in a weighted graph. <br> - Characterized by **factorial growth** in possible solutions. <br> - Solved using exact methods (for small `n`), approximation algorithms, or metaheuristics.                                                                                 |
| **Digraphs** | - Graphs where edges have **direction** (arcs). <br> - Defined by **in-degree** and **out-degree** of vertices. <br> - **Types** include Simple, Multigraphs, Oriented Graphs (Tournaments), Symmetric Digraphs, Rooted Trees, and **DAGs**. <br> - Essential for modeling asymmetric relationships like web links, task dependencies, and traffic flows. |

**Connection:** TSP is typically defined on a complete undirected graph, but a variant, the **Asymmetric TSP**, operates on a digraph where the cost from `u` to `v` may not equal the cost from `v` to `u` (e.g., one-way roads with different travel times).
