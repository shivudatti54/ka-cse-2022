# Textbook 2: Ch - Introduction to Data Structures

=============================================

### Overview

---

- Data structures are fundamental concepts in computer science that provide efficient storage and retrieval of data.
- Introduction to data structures is crucial for building efficient algorithms and solving complex problems.

### Key Concepts

---

### Arrays

---

- Definition: A collection of elements of the same data type stored in contiguous memory locations.
- Important Formulas:
  - Elements are accessed using an index (i.e., array[i])
  - Array operations (e.g., insertion, deletion, search) have a time complexity of O(1)
- Important Definitions:
  - Homogeneous (elements of the same data type)
  - Heterogeneous (elements of different data types)
- Important Theorems:
  - The Arrays' search algorithm has a worst-case time complexity of O(n)

### Linked Lists

---

- Definition: A dynamic collection of elements, where each element points to the next element.
- Important Formulas:
  - Insertion and deletion operations have a time complexity of O(1) at the beginning and end of the list, respectively
  - Search operation has a time complexity of O(n)
- Important Definitions:
  - Singly linked list (each node has a reference to the next node)
  - Doubly linked list (each node has references to both the next and previous nodes)
- Important Theorems:
  - The LinkedList's merge sort algorithm has a time complexity of O(n log n)

### Stacks and Queues

---

- Definition:
  - Stack: Last In First Out (LIFO) data structure
  - Queue: First In First Out (FIFO) data structure
- Important Formulas:
  - Stack operations (e.g., push, pop) have a time complexity of O(1)
  - Queue operations (e.g., enqueue, dequeue) have a time complexity of O(1)
- Important Definitions:
  - Last In First Out (LIFO)
  - First In First Out (FIFO)
- Important Theorems:
  - The Stack's implementation using an array has a time complexity of O(n)

### Trees

---

- Definition: A hierarchical data structure composed of nodes with a value and child nodes.
- Important Formulas:
  - Insertion and deletion operations have a time complexity of O(log n)
  - Search operation has a time complexity of O(log n)
- Important Definitions:
  - Binary tree (each node has at most two child nodes)
  - Balanced tree (each node has roughly the same number of left and right child nodes)
- Important Theorems:
  - The Binary Search Tree's insert operation has a time complexity of O(log n)

### Graphs

---

- Definition: A non-linear data structure consisting of nodes and edges.
- Important Formulas:
  - Graph traversal algorithms (e.g., DFS, BFS) have a time complexity of O(V + E)
  - Shortest path algorithm (e.g., Dijkstra's) has a time complexity of O((V + E) log V)
- Important Definitions:
  - Undirected graph (edges have no direction)
  - Directed graph (edges have a direction)
- Important Theorems:
  - The Graph's connectivity has a time complexity of O(V + E)

### Hash Tables

---

- Definition: A data structure that maps keys to values using a hash function.
- Important Formulas:
  - Insertion and deletion operations have a time complexity of O(1)
  - Search operation has a time complexity of O(1)
- Important Definitions:
  - Hash function (maps keys to indices)
  - Collision resolution (handles multiple keys mapping to the same index)
- Important Theorems:
  - The Hash Table's implementation using a separate chaining has a time complexity of O(1)

### Important Formulas and Definitions

---

| Formula/Definition     | Description | Time Complexity |
| ---------------------- | ----------- | --------------- |
| Array Indexing         | array[i]    | O(1)            |
| Linked List Insertion  | O(1)        | O(1)            |
| Stack/Queue Operations | push, pop   | O(1)            |
| Tree Insertion         | O(log n)    | O(log n)        |
| Graph Traversal        | DFS, BFS    | O(V + E)        |
| Hash Table Search      | O(1)        | O(1)            |

### Important Theorems

---

| Theorem                  | Description                        | Time Complexity |
| ------------------------ | ---------------------------------- | --------------- |
| Arrays' Search Algorithm | worst-case time complexity of O(n) | O(n)            |
| LinkedList's Merge Sort  | time complexity of O(n log n)      | O(n log n)      |
| Stack's Implementation   | time complexity of O(n)            | O(n)            |
