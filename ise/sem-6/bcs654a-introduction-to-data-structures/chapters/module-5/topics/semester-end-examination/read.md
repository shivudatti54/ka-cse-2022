# Module 5: Semester-End Examination - Introduction to Data Structures ()

## Introduction

The Semester-End Examination in "Introduction to Data Structures" is designed to evaluate your comprehensive understanding of the fundamental concepts, their applications, and your ability to analyze the efficiency of various data structures. This module (often Module 5 in the  syllabus) consolidates your learning from the entire course, testing not just rote memory but your analytical and problem-solving skills. Success hinges on a clear grasp of core principles and the ability to apply them to different scenarios.

## Core Concepts for Examination

The exam typically focuses on several key areas. A thorough preparation requires proficiency in each.

### 1. Analysis of Algorithms (Big-O Notation)

This is the bedrock for comparing data structures. You must understand:
*   **Why it's used:** To analyze the time and space complexity of algorithms independently of machine-specific constants.
*   **The Notation:** Big-O (`O`) describes the **upper bound** (worst-case) growth rate of a function.
*   **Common Complexities:** Be able to recognize and rank them:
    *   `O(1)` - Constant Time (best)
    *   `O(log n)` - Logarithmic Time (e.g., binary search)
    *   `O(n)` - Linear Time (e.g., linear search)
    *   `O(n log n)` - Linearithmic Time (e.g., efficient sorting algorithms)
    *   `O(n²)` - Quadratic Time (e.g., bubble sort, nested loops)
    *   `O(2ⁿ)` - Exponential Time (worst)

**Example:** If an algorithm for searching a list is `O(n)`, it means in the worst case, the time taken grows linearly with the number of elements `n`.

### 2. Advanced Tree Structures

Move beyond basic binary trees to more complex, efficient variants.
*   **AVL Trees:** Self-balancing Binary Search Trees (BSTs) where the height difference (balance factor) between left and right subtrees of any node is at most 1. Understand the **rotation operations (LL, RR, LR, RL)** used to maintain balance after insertion/deletion.
*   **B-Trees:** Multi-way search trees designed for systems that read and write large blocks of data (like databases). Understand the properties: a tree of order `m` has a maximum of `m` children and `m-1` keys per node. Know the splitting and merging processes during insertion and deletion.
*   **Splay Trees:** Self-adjusting BSTs where recently accessed elements are moved to the root through a process called **splaying**, improving access time for frequently used items.

### 3. Graph Representations and Algorithms

Graphs are crucial for modeling networks. You must know how to represent them and traverse them.
*   **Representations:**
    *   **Adjacency Matrix:** A 2D array where `matrix[i][j]` indicates an edge between node `i` and `j`. Efficient for dense graphs but consumes `O(V²)` space.
    *   **Adjacency List:** An array of lists, where each list stores the neighbors of a vertex. Space-efficient for sparse graphs (`O(V+E)`).
*   **Traversal Algorithms:**
    *   **Breadth-First Search (BFS):** Explores level-by-level using a queue. Used for shortest path in unweighted graphs.
    *   **Depth-First Search (DFS):** Explores as far as possible along a branch before backtracking, using a stack (or recursion). Used for cycle detection, topological sorting.

**Example:** For a social network (a graph), an adjacency list is efficient because each person (vertex) has a limited number of friends (edges).

### 4. Hashing and Collision Resolution

Hashing provides average-case `O(1)` time for search, insert, and delete operations.
*   **Hash Functions:** A function that maps a key to an array index. Goals: uniform distribution, quick computation.
*   **Collision:** When two different keys hash to the same index.
*   **Resolution Techniques:**
    *   **Chaining:** Store colliding elements in a linked list at the array index. Simple but requires extra memory.
    *   **Open Addressing:** Find another slot within the table itself. Methods include:
        *   **Linear Probing:** Check the next sequential slot.
        *   **Quadratic Probing:** Check slots using a quadratic function.
        *   **Double Hashing:** Use a second hash function to determine the probe step.

## Key Points & Summary

*   **Big-O is Fundamental:** You *must* be able to derive and compare time/space complexities for algorithms.
*   **Trees are Hierarchical:** Understand the properties, operations, and use-cases of different trees (BST, AVL, B-Tree). Balance is key for efficiency.
*   **Graphs are Relational:** Know how to represent a graph (Matrix vs. List) and traverse it (BFS for shortest unweighted path, DFS for connectivity).
*   **Hashing for Speed:** The goal is average `O(1)` access. Master the concepts of hash functions and, crucially, how to handle collisions.
*   **Practice Application:** Don't just memorize definitions. Practice writing algorithms for insertion, deletion, and traversal for each data structure. Solve previous years'  question papers to understand the exam pattern and question style.