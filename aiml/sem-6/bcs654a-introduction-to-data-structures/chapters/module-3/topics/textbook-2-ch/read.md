# Textbook 2: Ch

## Introduction to Linked Lists

### What are Linked Lists?

A linked list is a linear collection of data elements, where each element is a separate object and each object points to the next element in the sequence. This structure allows for efficient insertion and deletion of elements, making it a popular data structure in computer science.

### Advantages of Linked Lists

- Efficient use of memory: Linked lists only allocate memory for the actual data, rather than for a contiguous block of memory.
- Efficient insertion and deletion: Insertion and deletion operations can be performed in O(1) time, making linked lists suitable for applications where these operations are frequent.
- Dynamic size: Linked lists can grow or shrink dynamically, making them suitable for applications where the size of the data is unknown or changing.

### Disadvantages of Linked Lists

- Slow search: Searching for a specific element in a linked list can be slow, with a time complexity of O(n).
- Higher memory usage: Although linked lists use memory efficiently, they can still require more memory than arrays or other data structures.

### Types of Linked Lists

#### Singly Linked List

A singly linked list is a linked list where each element only points to the next element in the sequence. This is the most common type of linked list.

#### Doubly Linked List

A doubly linked list is a linked list where each element points to both the next and previous elements in the sequence. This allows for efficient traversal in both directions.

#### Self-Referential Structures

A self-referential structure is a linked list where each element points to a different node in the list. This allows for efficient insertion and deletion of elements.

### Operations on Linked Lists

#### Insertion

- Insertion at the beginning: O(1) time complexity, where a new node is created and inserted at the beginning of the list.
- Insertion at the end: O(1) time complexity, where a new node is created and inserted at the end of the list.
- Insertion at a specific position: O(n) time complexity, where the list needs to be traversed to find the insertion point.

#### Deletion

- Deletion at the beginning: O(1) time complexity, where the first element is removed.
- Deletion at the end: O(1) time complexity, where the last element is removed.
- Deletion at a specific position: O(n) time complexity, where the list needs to be traversed to find the deletion point.

#### Search

- Search for a specific element: O(n) time complexity, where the list needs to be traversed to find the element.

#### Traversal

- Traversal from the beginning: O(n) time complexity, where the list needs to be traversed from the beginning.
- Traversal from the end: O(n) time complexity, where the list needs to be traversed from the end.

### Example Use Cases

- Dynamic memory allocation: Linked lists can be used to manage a pool of dynamically allocated memory.
- Database query results: Linked lists can be used to represent the results of a database query, where each element represents a row in the result set.
- Browser history: Linked lists can be used to implement a browser's history feature, where each element represents a webpage.
