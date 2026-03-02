# Introduction to Data Structures

## What are Data Structures?

A **data structure** is a specialized format for organizing, processing, retrieving, and storing data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently. Data structures serve as the basis for abstract data types (ADT) and provide a means to manage large amounts of data efficiently.

**Definition:** A data structure is a particular way of organizing data in a computer so that it can be used effectively.

## Why Study Data Structures?

1. **Efficiency**: Different data structures have different strengths and weaknesses. Choosing the right data structure can dramatically improve program performance.

2. **Organization**: Data structures help organize data in a meaningful way for efficient access and modification.

3. **Reusability**: Well-designed data structures can be reused across different applications.

4. **Abstraction**: Data structures provide a level of abstraction that separates the logical view from the physical implementation.

5. **Foundation for Algorithms**: Algorithms and data structures go hand-in-hand. Many algorithms are designed specifically for certain data structures.

## Classification of Data Structures

Data structures can be classified in two main ways:

### 1. Based on Organization

```
Data Structures
 |
 |-- Primitive Data Structures
 | |-- Integer
 | |-- Float
 | |-- Character
 | |-- Boolean
 |
 |-- Non-Primitive Data Structures
 |
 |-- Linear Data Structures
 | |-- Static: Arrays
 | |-- Dynamic: Linked List, Stack, Queue
 |
 |-- Non-Linear Data Structures
 |-- Trees
 |-- Graphs
 |-- Tables (Hash Tables)
```

### 2. Based on Memory Allocation

**Static Data Structures:**

- Size is fixed at compile time
- Memory is allocated at compile time
- Example: Arrays
- Advantages: Fast access, simple implementation
- Disadvantages: Waste of memory if not fully used, cannot grow

**Dynamic Data Structures:**

- Size can change during execution
- Memory is allocated at runtime
- Examples: Linked Lists, Trees, Graphs
- Advantages: Efficient memory usage, can grow and shrink
- Disadvantages: Slower access, more complex implementation

## Primitive vs Non-Primitive Data Structures

### Primitive Data Structures

- Basic data types provided by programming languages
- Directly operated upon by machine instructions
- Examples: int, float, char, boolean
- Store single values

### Non-Primitive Data Structures

- Derived from primitive data structures
- More sophisticated structures
- Can store multiple values
- Examples: arrays, structures, linked lists, trees, graphs

## Linear vs Non-Linear Data Structures

### Linear Data Structures

- Elements are arranged in a sequential manner
- Each element has a unique predecessor and successor (except first and last)
- Can be traversed in a single run
- Examples:
- **Arrays**: Fixed-size, contiguous memory
- **Linked Lists**: Dynamic size, non-contiguous memory
- **Stacks**: LIFO (Last In First Out) - add/remove from one end
- **Queues**: FIFO (First In First Out) - add at one end, remove from other

**Characteristics:**

- Simple to implement
- Memory may not be utilized efficiently
- Traversal is straightforward

### Non-Linear Data Structures

- Elements are not arranged sequentially
- One element can be connected to multiple elements
- Represent hierarchical relationships
- Examples:
- **Trees**: Hierarchical structure with root node
- **Graphs**: Network of nodes connected by edges
- **Hash Tables**: Key-value pairs with hash function

**Characteristics:**

- Complex to implement
- Better memory utilization
- Efficient for complex operations
- Multiple levels of data

## Operations on Data Structures

Common operations performed on data structures include:

1. **Traversing**: Accessing each element exactly once
2. **Searching**: Finding the location of an element
3. **Insertion**: Adding a new element
4. **Deletion**: Removing an element
5. **Sorting**: Arranging elements in order
6. **Merging**: Combining elements from multiple data structures
7. **Updating**: Modifying an existing element

## Selection Criteria for Data Structures

When choosing a data structure, consider:

1. **Type of data** to be stored
2. **Operations** to be performed frequently
3. **Memory constraints**
4. **Time complexity** requirements
5. **Ease of implementation**
6. **Dynamic vs static** requirements

## Abstract Data Types (ADT)

An **Abstract Data Type** is a data type that is defined by its behavior (operations) rather than its implementation.

**Components of ADT:**

1. **Data**: What information is stored
2. **Operations**: What operations can be performed
3. **Implementation**: Hidden from the user

**Examples:**

- Stack ADT: Operations - push(), pop(), peek()
- Queue ADT: Operations - enqueue(), dequeue(), front()
- List ADT: Operations - insert(), delete(), search()

## Time and Space Complexity

### Time Complexity

Measures the amount of time an algorithm takes as a function of input size.

**Common Time Complexities:**

- O(1) - Constant time
- O(log n) - Logarithmic time
- O(n) - Linear time
- O(n log n) - Linearithmic time
- O(n²) - Quadratic time
- O(2ⁿ) - Exponential time

### Space Complexity

Measures the amount of memory an algorithm uses as a function of input size.

## Overview of Data Structures Covered

### Arrays

- Fixed-size collection of similar elements
- Random access using index
- Memory efficient for known size

### Linked Lists

- Dynamic size collection
- Sequential access
- Efficient insertion/deletion

### Stacks

- LIFO principle
- Used in function calls, expression evaluation, backtracking

### Queues

- FIFO principle
- Used in scheduling, buffering, BFS

### Trees

- Hierarchical structure
- Binary trees, BST, AVL trees
- Used in databases, file systems, compilers

### Graphs

- Network of nodes and edges
- Used in social networks, maps, resource allocation

### Hash Tables

- Key-value pairs
- Fast lookup, insertion, deletion
- Used in caching, databases, symbol tables

## Applications of Data Structures

1. **Operating Systems**: Process scheduling (queues), file system (trees)
2. **Databases**: Indexing (B-trees), hashing
3. **Compilers**: Symbol tables (hash tables), syntax trees
4. **Artificial Intelligence**: Search algorithms (graphs, trees)
5. **Networks**: Routing algorithms (graphs)
6. **Graphics**: Scene graphs (trees)

## Exam Tips

1. Understand the classification of data structures clearly
2. Know the differences between linear and non-linear structures
3. Be able to compare static vs dynamic data structures
4. Understand time and space complexity basics
5. Know which data structure to use for specific scenarios
6. Memorize common operations and their complexities for each data structure
7. Practice drawing diagrams for different data structures
