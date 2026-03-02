# Static Allocation vs Linked Allocation in Data Structures

## Introduction

In the world of data structures, how we allocate memory for storing data is a fundamental design choice that directly impacts a program's efficiency, flexibility, and complexity. For engineering students, understanding the distinction between **Static (Sequential) Allocation** and **Dynamic (Linked) Allocation** is crucial for designing optimal software solutions. This module explores these two core memory management techniques, their characteristics, and their trade-offs.

## Core Concepts Explained

### 1. Static Allocation (Sequential Allocation)

In static allocation, memory for a data structure is allocated at compile-time. The size of the structure is fixed and must be known in advance. A classic example is the **Array**.

- **How it works:** A contiguous block of memory is reserved for the entire data structure. The base address points to the first element, and subsequent elements are accessed using an index and a calculated offset (e.g., `location = base_address + index * size_of_element`).
- **Key Characteristics:**
- **Fixed Size:** The size cannot be altered during program execution (runtime).
- **Contiguous Memory:** Elements are stored next to each other in memory.
- **Efficient Access:** Direct access to any element via its index is possible in constant time, O(1).
- **Memory Usage:** Can lead to memory wastage (if allocated size is too large) or insufficiency (if allocated size is too small).

**Example:**
Declaring an integer array `int arr[100];` reserves a contiguous block of memory for 100 integers. You cannot store the 101st element without recompiling the program with a larger size.

### 2. Linked Allocation (Dynamic Allocation)

In linked allocation, memory is allocated at run-time. The data structure grows and shrinks dynamically as needed. The fundamental building block is a **Node**, which contains both the data and a pointer to the next node. A classic example is the **Linked List**.

- **How it works:** Nodes are created dynamically whenever new data is added. These nodes are not necessarily stored in contiguous memory locations. They are "linked" together using pointers, which store the address of the subsequent node.
- **Key Characteristics:**
- **Dynamic Size:** The size can grow or shrink during program execution, making it highly flexible.
- **Non-Contiguous Memory:** Nodes can be scattered anywhere in the memory heap.
- **Sequential Access:** To access an element, one must traverse the list from the head node, resulting in linear time complexity, O(n), for access by index.
- **Efficient Insertion/Deletion:** Adding or removing elements, especially at the beginning or middle, requires only changing pointers, an O(1) operation if the node is known.

**Example:**
In a singly linked list, each node is defined as:
