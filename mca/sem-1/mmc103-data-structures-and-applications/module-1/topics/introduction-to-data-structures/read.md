# Introduction to Data Structures


## Table of Contents

- [Introduction to Data Structures](#introduction-to-data-structures)
- [What is a Data Structure?](#what-is-a-data-structure)
- [Why Do Data Structures Matter?](#why-do-data-structures-matter)
  - [Key Reasons to Study Data Structures](#key-reasons-to-study-data-structures)
- [Abstract Data Types (ADTs)](#abstract-data-types-adts)
  - [Example: Stack ADT](#example-stack-adt)
  - [ADT vs Data Structure](#adt-vs-data-structure)
- [Classification of Data Structures](#classification-of-data-structures)
  - [Primitive Data Structures](#primitive-data-structures)
  - [Non-Primitive Data Structures](#non-primitive-data-structures)
- [Overview of Common Data Structures](#overview-of-common-data-structures)
  - [Arrays](#arrays)
  - [Linked Lists](#linked-lists)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Trees](#trees)
  - [Graphs](#graphs)
- [Role of Data Structures in Algorithm Design](#role-of-data-structures-in-algorithm-design)
- [Efficiency Considerations](#efficiency-considerations)
  - [Example Trade-off](#example-trade-off)
- [A Simple C Program Demonstrating Data Structure Choice](#a-simple-c-program-demonstrating-data-structure-choice)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## What is a Data Structure?

A **data structure** is a particular way of organizing, storing, and managing data in a computer so that it can be accessed and modified efficiently. It is not just about storing data -- it is about storing data in a way that supports efficient operations on that data.

Formally:

> A data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data.

Every program deals with data. The way we choose to organize that data fundamentally determines how fast our program runs and how much memory it uses.

## Why Do Data Structures Matter?

Consider a simple example: you need to search for a student's name in a list of 10,000 students.

- If the names are stored in an **unsorted array**, you may need to check all 10,000 entries (linear search) -- O(n).
- If the names are stored in a **sorted array**, you can use binary search and find the name in about 14 comparisons -- O(log n).
- If the names are stored in a **hash table**, you can find the name in approximately 1 step -- O(1) average.

The underlying algorithm is important, but the **choice of data structure** is what makes certain algorithms possible in the first place.

### Key Reasons to Study Data Structures

- **Efficiency**: Proper data structures reduce time and space complexity of programs.
- **Reusability**: Standard data structures (stacks, queues, trees) can be reused across many applications.
- **Abstraction**: They allow programmers to think at a higher level without worrying about low-level memory details.
- **Foundation for Algorithms**: Most algorithms are designed around specific data structures (e.g., Dijkstra's algorithm uses a priority queue).

## Abstract Data Types (ADTs)

An **Abstract Data Type (ADT)** is a mathematical model for data types, defined by its behavior (operations) from the user's point of view, not by its implementation.

An ADT specifies:

1. **Data**: What kind of data is stored.
2. **Operations**: What operations can be performed on that data.
3. **Error conditions**: What happens when an operation is applied incorrectly.

### Example: Stack ADT

| Component      | Description                                    |
| -------------- | ---------------------------------------------- |
| **Data**       | A collection of elements with LIFO ordering    |
| **Operations** | push(item), pop(), peek(), isEmpty(), isFull() |
| **Error**      | pop() on empty stack causes underflow          |

The ADT does **not** specify whether the stack is implemented using an array or a linked list. That is an implementation detail.

### ADT vs Data Structure

| Aspect             | ADT                           | Data Structure                     |
| ------------------ | ----------------------------- | ---------------------------------- |
| Level              | Logical / Conceptual          | Physical / Implementation          |
| Focus              | What operations are supported | How those operations are performed |
| Example            | List ADT                      | Array, Linked List                 |
| Language-dependent | No                            | Yes                                |

## Classification of Data Structures

Data structures are broadly classified as follows:

```
Data Structures
|
|-- Primitive
| |-- int
| |-- float
| |-- char
| |-- double
|-- Non-Primitive
| |-- Linear
| | |-- Arrays
| | |-- Linked Lists
| | |-- Stacks
| | |-- Queues
| |-- Non-Linear
| | |-- Trees
| | |-- Graphs
```

### Primitive Data Structures

These are the basic data types provided directly by the programming language: `int`, `float`, `char`, `double`. They hold a single value and have predefined operations (+, -, \*, /, comparisons).

### Non-Primitive Data Structures

These are derived from primitive types and can hold collections of values.

**Linear Data Structures** -- elements are arranged in a sequential manner:

- **Array**: Fixed-size, contiguous memory, index-based access.
- **Linked List**: Dynamic size, non-contiguous memory, pointer-based access.
- **Stack**: LIFO (Last In, First Out) access pattern.
- **Queue**: FIFO (First In, First Out) access pattern.

**Non-Linear Data Structures** -- elements are not arranged sequentially:

- **Tree**: Hierarchical structure with a root node and child nodes.
- **Graph**: A set of nodes (vertices) connected by edges; can be directed or undirected.

## Overview of Common Data Structures

### Arrays

An array stores elements of the same type in contiguous memory locations.

```c
int marks[5] = {90, 85, 78, 92, 88};
// marks[0] = 90, marks[1] = 85, ...
```

| Operation         | Time Complexity |
| ----------------- | --------------- |
| Access by index   | O(1)            |
| Search (unsorted) | O(n)            |
| Insertion at end  | O(1)            |
| Insertion at pos  | O(n)            |
| Deletion          | O(n)            |

### Linked Lists

A linked list stores elements in nodes, where each node contains data and a pointer to the next node.

```c
struct Node {
 int data;
 struct Node *next;
};
```

| Operation          | Time Complexity |
| ------------------ | --------------- |
| Access by position | O(n)            |
| Insertion at front | O(1)            |
| Insertion at end   | O(n)            |
| Deletion at front  | O(1)            |
| Search             | O(n)            |

### Stacks

A stack follows the **LIFO** principle. Think of a stack of plates -- you add and remove from the top only.

Key operations: `push()`, `pop()`, `peek()`, `isEmpty()`

### Queues

A queue follows the **FIFO** principle. Think of a queue at a ticket counter -- first person in line is served first.

Key operations: `enqueue()`, `dequeue()`, `front()`, `isEmpty()`

### Trees

A tree is a hierarchical data structure with a root node and subtrees of children.

The most important variant is the **Binary Search Tree (BST)**, where for every node, the left subtree has smaller values and the right subtree has larger values.

### Graphs

A graph G = (V, E) consists of a set of vertices V and a set of edges E.

Graphs can model networks, maps, social connections, and many other real-world relationships.

## Role of Data Structures in Algorithm Design

The relationship between data structures and algorithms is inseparable:

- **Sorting algorithms** operate on arrays and linked lists.
- **Graph algorithms** (BFS, DFS, Dijkstra) require adjacency lists or matrices.
- **Tree traversals** (inorder, preorder, postorder) are algorithms specific to tree structures.
- **Hashing** requires hash tables with collision resolution strategies.

The choice of data structure often determines:

1. Which algorithms are applicable.
2. The time complexity of those algorithms.
3. The space complexity of the solution.

## Efficiency Considerations

When choosing a data structure, consider:

| Factor          | Question to Ask                             |
| --------------- | ------------------------------------------- |
| **Time**        | How fast are the required operations?       |
| **Space**       | How much memory does it consume?            |
| **Simplicity**  | Is the implementation straightforward?      |
| **Scalability** | Does it perform well as data grows?         |
| **Operations**  | What operations are needed most frequently? |

### Example Trade-off

If you need frequent **random access**, use an **array** (O(1) access).

If you need frequent **insertions/deletions**, use a **linked list** (O(1) at known positions).

There is no single "best" data structure -- the best choice depends on the specific problem and its constraints.

## A Simple C Program Demonstrating Data Structure Choice

```c
#include <stdio.h>
#define MAX 100

// Using an array to store and retrieve student marks
int main() {
 int marks[MAX], n, i, roll;
 printf("Enter number of students: ");
 scanf("%d", &n);
 for (i = 0; i < n; i++) {
 printf("Enter marks for student %d: ", i + 1);
 scanf("%d", &marks[i]);
 }
 printf("Enter roll number to search (1 to %d): ", n);
 scanf("%d", &roll);
 if (roll >= 1 && roll <= n)
 printf("Marks of student %d: %d\n", roll, marks[roll - 1]); // O(1) access
 else
 printf("Invalid roll number.\n");
 return 0;
}
```

Here the array provides O(1) direct access by roll number -- a clear advantage of choosing the right data structure for the problem.

## Summary

| Concept               | Key Point                                                        |
| --------------------- | ---------------------------------------------------------------- |
| Data Structure        | A way to organize data for efficient access and modification     |
| ADT                   | Logical description of data and operations (implementation-free) |
| Primitive types       | int, float, char, double                                         |
| Linear structures     | Array, Linked List, Stack, Queue                                 |
| Non-linear structures | Tree, Graph                                                      |
| Choice depends on     | Required operations, time/space constraints, data size           |

## Exam Tips

- **Definition questions** are common: Be ready to define "data structure," "ADT," and distinguish between primitive and non-primitive types.
- **Classification diagram**: Practice drawing the classification tree (Primitive vs Non-Primitive, Linear vs Non-Linear). This is a frequently asked 5-mark question.
- **ADT vs Data Structure**: Understand and be able to explain the difference with an example (e.g., List ADT can be implemented as an array or linked list).
- **Comparison questions**: Be prepared to compare arrays vs linked lists, or stacks vs queues, in terms of operations and time complexity.
- **Real-world examples**: Mentioning practical applications (browser back button for stack, printer queue for queue, file system for tree) earns extra marks.
- **Time complexity**: Always mention Big-O complexity when discussing operations on any data structure.
