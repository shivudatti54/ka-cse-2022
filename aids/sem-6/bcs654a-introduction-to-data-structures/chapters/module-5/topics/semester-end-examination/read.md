# Module 5: Semester-End Examination Guide for Introduction to Data Structures

## Introduction

As you approach the end of your "Introduction to Data Structures" course, Module 5 focuses on preparing you for the semester-end examination. This exam is designed to evaluate your comprehensive understanding of the fundamental data structures, their properties, operations, and appropriate use-cases. Success hinges on your ability to not just recall definitions but to apply concepts to solve problems efficiently. This guide outlines the core concepts you must master, their typical representation in exam questions, and strategies for effective revision.

## Core Concepts & Exam Focus

The examination will test your knowledge across the spectrum of data structures covered in the course. Key areas include:

### 1. Analysis of Algorithms
This is the foundational concept for comparing data structures.
*   **Big-O Notation:** You must be able to express the worst-case time and space complexity of operations (insertion, deletion, search, traversal) for each data structure. Understand what O(1), O(log n), O(n), O(n log n), and O(n²) mean practically.
*   **Exam Question Example:** "Compare the time complexity of searching for an element in a sorted array versus a binary search tree. Justify your answer."

### 2. Linear Data Structures
Understand the implementation, usage, and differences between these structures.
*   **Arrays vs. Linked Lists:** Be prepared to discuss the trade-offs. Arrays allow O(1) random access but have fixed size and costly insertions/deletions. Linked Lists have dynamic size and efficient insertions/deletions at known positions but require O(n) for access.
*   **Stacks (LIFO) & Queues (FIFO):** Know their core operations (push/pop, enqueue/dequeue). Understand their applications (e.g., stack for function call management/undo operations, queue for task scheduling).
*   **Exam Question Example:** "Show the state of a stack after the following operations: push(A), push(B), pop(), push(C)." or "Implement a queue using two stacks and analyze the complexity of enqueue and dequeue operations."

### 3. Non-Linear Data Structures
These are often a major focus of the exam due to their complexity.
*   **Trees:** Key terminology (root, leaf, parent, child, height, depth).
*   **Binary Trees & Binary Search Trees (BST):** Understand the BST property (left subtree < root < right subtree). Be able to perform and code traversals (Inorder, Preorder, Postorder). Know the worst-case (O(n)) and average-case (O(log n)) search complexities.
*   **Graphs:** Differentiate between concepts like directed/undirected, weighted/unweighted graphs. Know the difference between adjacency matrix and adjacency list representations and their space/time trade-offs. Understand traversal algorithms:
    *   **Breadth-First Search (BFS):** Implemented using a queue. Finds shortest path in unweighted graphs.
    *   **Depth-First Search (DFS):** Implemented using a stack (or recursion). Useful for cycle detection, topological sorting.
*   **Exam Question Example:** "Insert the following elements into an initially empty BST: 50, 30, 70, 20, 40. Draw the resulting tree." or "Perform BFS and DFS on a given graph starting from node A."

### 4. Hashing
*   **Concept:** Understand how a hash function maps keys to array indices.
*   **Collision Resolution:** Be able to explain and differentiate between open hashing (chaining) and closed hashing (probaining, e.g., linear probing). Discuss the advantages and disadvantages of each.
*   **Exam Question Example:** "Insert keys into a hash table of a given size using linear probing. Show the final table state."

## Key Points & Summary

*   **Time & Space Complexity:** The "why" behind every data structure. Always justify your choice of data structure by referring to the complexity of the required operations.
*   **Trade-offs are Crucial:** There is no "best" data structure. The choice depends on the most frequent operation (e.g., search vs. insertion). Be ready to compare and contrast (e.g., Array vs. LinkedList, BST vs. Hash Table).
*   **Traversals:** Ensure you can write pseudocode or code for tree (inorder, preorder, postorder) and graph (BFS, DFS) traversals.
*   **Practice Applied Problems:** Exams test application. Practice problems that involve building, modifying, and tracing algorithms on these data structures.
*   **Standard Applications:** Remember standard use-cases: stacks for recursion/parsing, queues for scheduling, graphs for networks, trees for hierarchical data, hash tables for O(1) lookups.

**Final Tip:** Your ability to trace algorithms manually and visualize the state of a data structure after a series of operations is paramount. Practice drawing trees, graphs, hash tables, and stacks/queues extensively.