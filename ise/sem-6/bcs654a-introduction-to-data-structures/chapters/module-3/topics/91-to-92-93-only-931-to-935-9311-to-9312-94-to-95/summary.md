**Linked Lists: Introduction, Singly Linked List, Self-Referential Structures**

### 9.1 to 9.2

- **Definition of Linked List:**
  - A linear collection of data elements whose order is not given by their physical placement in memory.
  - Each element points to the next element in the sequence.
- **Types of Linked Lists:**
  - Singly Linked List
  - Doubly Linked List
  - Circularly Linked List
- **Operations on Linked Lists:**
  - Insertion
  - Deletion
  - Traversal
  - Search

### 9.3

- **Singly Linked List:**
  - Only forward pointers are used to link elements.
  - Each node contains a value and a pointer to the next node.
- **9.3.1: Node Structure**
  - Node: value and pointer to next node
- **9.3.2: Operations**
  - Insertion: Insert a new node at a specific position
  - Deletion: Delete a node at a specific position
  - Traversal: Visit each node in the list
- **9.3.3: Time Complexity**
  - Insertion: O(1) at the end, O(n) at other positions
  - Deletion: O(1) at the end, O(n) at other positions
  - Traversal: O(n)
- **9.3.4: Space Complexity**
  - O(n) for storage of nodes
- **9.3.5: Example Use Case**
  - Implementing a stack or queue data structure
- **9.3.11: Node Cloning**
  - Create a new node with the same value and pointer to next node
- **9.3.12: Node Deletion**
  - Update pointers of adjacent nodes

### 9.4 to 9.5

- **Self-Referential Structures:**
  - A node contains a pointer to its own memory location.
  - Allows for efficient insertion and deletion of nodes.
- **9.4: Node Cloning and Deletion**
  - Methods for cloning and deleting nodes
- **9.5: Applications of Self-Referential Structures**
  - Implementing efficient data structures, such as hash tables and binary search trees
