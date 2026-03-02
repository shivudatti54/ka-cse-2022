# Linked Lists: Singly, Doubly, and Circular

## A Comprehensive Study Material for BSc Physical Science (CS) - Delhi University (NEP 2024)

---

## 1. Introduction

### 1.1 What is a Linked List?

A **linked list** is a fundamental linear data structure in computer science where elements (called **nodes**) are stored in a sequence, with each node containing two main components:

1. **Data**: The actual information or value stored in the node
2. **Pointer (or Reference)**: A link to the next node (and in some cases, the previous node)

Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, each node points to its successor, creating a dynamic chain of elements that can grow or shrink during program execution.

### 1.2 Real-World Relevance

Linked lists have numerous practical applications:

- **Music Players**: Playlist management uses circular linked lists to seamlessly transition from the last song back to the first
- **Browser History**: The back/forward navigation in web browsers is implemented using doubly linked lists
- **Image Viewers**: Next/previous image navigation in gallery apps
- **Operating Systems**: Process scheduling queues
- **Undo/Redo Functionality**: Text editors use doubly linked lists to maintain edit history
- **Polynomial Representation**: Mathematical polynomials are often stored using linked lists for efficient arithmetic operations

### 1.3 Why Linked Lists Over Arrays?

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory Allocation | Static (fixed size) | Dynamic (grows/shrinks) |
| Insertion/Deletion | O(n) - requires shifting | O(1) - if node reference available |
| Random Access | O(1) - direct index access | O(n) - must traverse |
| Memory Usage | May have unused space | Overhead of storing pointers |
| Cache Performance | Better (contiguous memory) | Poor (scattered memory) |

---

## 2. Singly Linked List

### 2.1 Definition and Structure

A **singly linked list** is the simplest form of linked list where each node contains:
- Data field
- A pointer (or reference) to the next node in the sequence
- The last node points to `NULL` (or `None`)

```
┌─────┬──────┐     ┌─────┬──────┐     ┌─────┬──────┐     ┌─────┬──────┐
│ 10  │ next │ ──► │ 20  │ next │ ──► │ 30  │ next │ ──► │ 40  │ NULL │
└─────┴──────┘     └─────┴──────┘     └─────┴──────┘     └─────┴──────┘
   HEAD
```

### 2.2 Node Representation

**In C:**
```c
struct Node {
    int data;
    struct Node* next;
};
```

**In Python:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### 2.3 Basic Operations

#### (a) Traversal
```python
def traverse(head):
    """Traverse and print all elements in the linked list"""
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("NULL")
```

#### (b) Insertion at Beginning
```python
def insert_at_beginning(head, data):
    """Insert a new node at the beginning of the list"""
    new_node = Node(data)
    new_node.next = head
    return new_node  # New node becomes the new head
```

#### (c) Insertion at End
```python
def insert_at_end(head, data):
    """Insert a new node at the end of the list"""
    new_node = Node(data)
    
    # If list is empty
    if head is None:
        return new_node
    
    # Traverse to the last node
    current = head
    while current.next is not None:
        current = current.next
    
    current.next = new_node
    return head
```

#### (d) Deletion from Beginning
```python
def delete_from_beginning(head):
    """Delete the first node and return new head"""
    if head is None:
        return None
    temp = head
    head = head.next
    temp = None  # Free memory
    return head
```

#### (e) Search Operation
```python
def search(head, key):
    """Search for a key in the list, return True if found"""
    current = head
    position = 0
    while current is not None:
        if current.data == key:
            return True, position
        current = current.next
        position += 1
    return False, -1
```

### 2.4 Time and Space Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Insertion at Beginning | O(1) | O(1) |
| Insertion at End | O(n) | O(1) |
| Deletion at Beginning | O(1) | O(1) |
| Deletion at End | O(n) | O(1) |
| Search | O(n) | O(1) |
| Traversal | O(n) | O(1) |

**Space Complexity**: O(n) for storing n elements, plus O(n) overhead for pointers

---

## 3. Doubly Linked List

### 3.1 Definition and Structure

A **doubly linked list** extends the singly linked list by adding a **previous pointer** to each node. This allows traversal in both directions (forward and backward). Each node contains:

- Data field
- Pointer to the next node
- Pointer to the previous node

```
NULL  ◄──┌─────┬──────┬─────┐     ┌─────┬──────┬─────┐     ┌─────┬──────┬─────┐──► NULL
       │prev │  10  │next │ ◄──► │prev │  20  │next │ ◄──► │prev │  30  │next │
       └─────┴──────┴─────┘     └─────┴──────┬─────┘     └─────┴──────┴─────┘
                                             HEAD
```

### 3.2 Node Representation

**In C:**
```c
struct DNode {
    int data;
    struct DNode* prev;
    struct DNode* next;
};
```

**In Python:**
```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

### 3.3 Why Doubly Linked Lists?

- **Bidirectional Traversal**: Can move forward and backward
- **Efficient Deletion**: Can delete a node given only its reference (no need to search from head)
- **Browser Navigation**: Perfect for back/forward buttons
- **Music Player Playlists**: Easy navigation to previous/next song

### 3.4 Basic Operations

#### (a) Insertion at Beginning
```python
def insert_at_beginning_dll(head, data):
    """Insert a new node at the beginning of doubly linked list"""
    new_node = DNode(data)
    new_node.next = head
    
    if head is not None:
        head.prev = new_node
    
    return new_node  # New node becomes the new head
```

#### (b) Insertion at End
```python
def insert_at_end_dll(head, data):
    """Insert a new node at the end of doubly linked list"""
    new_node = DNode(data)
    
    if head is None:
        return new_node
    
    # Traverse to the last node
    current = head
    while current.next is not None:
        current = current.next
    
    current.next = new_node
    new_node.prev = current
    return head
```

#### (c) Deletion of a Specific Node
```python
def delete_node_dll(head, node_to_delete):
    """Delete a specific node (given reference)"""
    if head is None or node_to_delete is None:
        return head
    
    # If deleting head node
    if node_to_delete == head:
        head = head.next
        if head:
            head.prev = None
    
    # Update previous node's next pointer
    if node_to_delete.prev:
        node_to_delete.prev.next = node_to_delete.next
    
    # Update next node's prev pointer
    if node_to_delete.next:
        node_to_delete.next.prev = node_to_delete.prev
    
    return head
```

#### (d) Traversal in Both Directions
```python
def traverse_forward(head):
    """Traverse forward and print elements"""
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("NULL")

def traverse_backward(head):
    """Traverse backward from end and print elements"""
    # Go to the last node
    if head is None:
        return
    current = head
    while current.next:
        current = current.next
    
    # Traverse backward
    while current:
        print(current.data, end=" <-> ")
        current = current.prev
    print("NULL")
```

### 3.5 Time and Space Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Insertion at Beginning | O(1) | O(1) |
| Insertion at End | O(n) | O(1) |
| Deletion at Beginning | O(1) | O(1) |
| Deletion at End | O(n) | O(1) |
| Deletion (given node ref) | O(1) | O(1) |
| Search | O(n) | O(1) |
| Traversal | O(n) | O(1) |

**Space Complexity**: O(n) for storing n elements, but requires extra O(n) for both forward and backward pointers (slightly more than singly)

---

## 4. Circular Linked List

### 4.1 Definition and Structure

A **circular linked list** is a variation where the last node points back to the first node (head), forming a circle. There are two types:

1. **Singly Circular Linked List**: Last node points to first node (only next pointer)
2. **Doubly Circular Linked List**: Last node points to first, and first node's prev points to last

```
SINGLY CIRCULAR:                    DOUBLY CIRCULAR:
                                    
┌─────┬──────┐     ┌─────┬──────┐    NULL ◄──┌─────┬──────┬─────┐►──► NULL
│ 10  │ next │ ──► │ 20  │ next │    ▲      │prev │  10  │next │      │
└─────┴──────┘     └─────┴──────┘    │      └─────┴──────┬─────┘      │
    ▲                 │              │                 │            │
    │                 └──────────────┘                 ▼            │
    └───────────────────────────────────────────────────────────────┘
```

### 4.2 Real-World Applications

- **Round-Robin CPU Scheduling**: Processes are organized in a circular manner
- **Multiplayer Games**: Turn-based games use circular lists to track player turns
- **Circular Buffers**: Used in producer-consumer problems
- **Repeated Looping**: Music playlists that repeat infinitely

### 4.3 Singly Circular Linked List Implementation

**Node Structure:**
```python
class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None
```

#### (a) Insertion in Singly Circular Linked List

```python
def insert_at_beginning_circular(head, data):
    """Insert at beginning of circular singly linked list"""
    new_node = CNode(data)
    
    if head is None:
        new_node.next = new_node  # Points to itself
        return new_node
    
    # Find the last node
    current = head
    while current.next != head:
        current = current.next
    
    # Insert new node
    new_node.next = head
    current.next = new_node
    return new_node  # New node becomes head

def insert_at_end_circular(head, data):
    """Insert at end of circular singly linked list"""
    new_node = CNode(data)
    
    if head is None:
        new_node.next = new_node
        return new_node
    
    # Find the last node
    current = head
    while current.next != head:
        current = current.next
    
    current.next = new_node
    new_node.next = head
    return head
```

#### (b) Traversal of Singly Circular Linked List
```python
def traverse_circular(head):
    """Traverse and print circular linked list"""
    if head is None:
        print("List is empty")
        return
    
    current = head
    while True:
        print(current.data, end=" -> ")
        current = current.next
        if current == head:
            break
    print("(back to head)")
```

### 4.4 Doubly Circular Linked List Implementation

**Node Structure:**
```python
class DCNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

#### (a) Insertion at Beginning (Doubly Circular)
```python
def insert_at_beginning_dc(head, data):
    """Insert at beginning of doubly circular linked list"""
    new_node = DCNode(data)
    
    if head is None:
        new_node.next = new_node
        new_node.prev = new_node
        return new_node
    
    # Find last node
    last = head.prev
    
    # Insert new node
    new_node.next = head
    new_node.prev = last
    last.next = head.prev = new_node
    return new_node
```

#### (b) Deletion from Doubly Circular Linked List
```python
def delete_from_dc(head, key):
    """Delete node with given key from doubly circular list"""
    if head is None:
        return None
    
    current = head
    
    # Search for the node
    while True:
        if current.data == key:
            # Adjust pointers
            current.prev.next = current.next
            current.next.prev = current.prev
            
            # If deleting the only node
            if current == current.next:
                return None
            
            # If deleting head
            if current == head:
                return current.next
            
            return head
        
        current = current.next
        if current == head:
            break
    
    return head
```

### 4.5 Time and Space Complexity

| Operation | Singly Circular | Doubly Circular |
|-----------|-----------------|------------------|
| Insertion at Beginning | O(n) | O(1) |
| Insertion at End | O(n) | O(1) |
| Deletion at Beginning | O(n) | O(1) |
| Deletion at End | O(n) | O(1) |
| Search | O(n) | O(n) |
| Traversal | O(n) | O(n) |

**Note**: In circular lists, we typically maintain a tail pointer to make end operations O(1).

---

## 5. Comprehensive Comparison

### 5.1 Comparison Table

| Feature | Singly Linked | Doubly Linked | Singly Circular | Doubly Circular |
|---------|---------------|---------------|-----------------|-----------------|
| Memory Usage | Low | High | Low | Highest |
| Traversal Direction | Forward only | Both | Forward (cyclic) | Both (cyclic) |
| Insertion at End | O(n) | O(n) | O(n) | O(1)* |
| Deletion from End | O(n) | O(n) | O(n) | O(1)* |
| No NULL issues | No | No | Yes | Yes |
| Implementation | Simple | Moderate | Moderate | Complex |

*With tail pointer

### 5.2 When to Use Which?

- **Singly Linked List**: When memory is limited and only forward traversal is needed
- **Doubly Linked List**: When bidirectional traversal is required (browsers, editors)
- **Circular Linked List**: When you need continuous looping (playlists, round-robin)

---

## 6. Multiple Choice Questions (Difficulty Progression)

### Level 1: Basic Understanding

**Q1. In a singly linked list, each node contains:**
- (a) Data and one pointer
- (b) Data and two pointers
- (c) Only data
- (d) Only pointers

**Answer: (a)**

---

**Q2. The last node in a singly linked list points to:**
- (a) First node
- (b) NULL
- (c) Itself
- (d) None of these

**Answer: (b)**

---

### Level 2: Intermediate Concepts

**Q3. What is the time complexity of inserting a node at the beginning of a singly linked list?**
- (a) O(n)
- (b) O(log n)
- (c) O(1)
- (d) O(n²)

**Answer: (c)**

---

**Q4. In a doubly linked list, if we have a reference to a node, we can delete it in:**
- (a) O(n) time
- (b) O(1) time
- (c) O(log n) time
- (d) O(n²) time

**Answer: (b)**

---

### Level 3: Advanced Application

**Q5. Which data structure is most suitable for implementing a "round-robin" CPU scheduling algorithm?**
- (a) Singly linked list
- (b) Doubly linked list
- (c) Singly circular linked list
- (d) Doubly circular linked list

**Answer: (c)**

---

**Q6. In a doubly circular linked list with 5 nodes, if you start from node 3 and follow next pointers, how many steps will you take to return to node 3?**
- (a) 3
- (b) 4
- (c) 5
- (d) 6

**Answer: (c)**

---

**Q7. The main advantage of linked lists over arrays is:**
- (a) Faster search
- (b) Random access
- (c) Dynamic size and efficient insertion/deletion
- (d) Better cache performance

**Answer: (c)**

---

### Level 4: Critical Thinking

**Q8. You need to implement an "Undo" feature in a text editor. Which data structure would be most efficient?**
- (a) Singly linked list
- (b) Array
- (c) Doubly linked list
- (d) Stack

**Answer: (c)** — Doubly linked list allows moving back and forth through edit history

---

**Q9. What is the space complexity of storing n elements in a singly linked list?**
- (a) O(1)
- (b) O(n)
- (c) O(n²)
- (d) O(log n)

**Answer: (b)** — We need O(n) space for data + O(n) overhead for pointers

---

**Q10. In a circular linked list, the problem of NULL pointer checking is eliminated because:**
- (a) There are no pointers
- (b) Every node points to another node
- (c) It uses arrays instead
- (d) The compiler handles it automatically

**Answer: (b)** — In circular lists, there's no NULL at the end; the last node points back to the first

---

## 7. Flashcards for Quick Review

### Flashcard Set

| # | Term/Concept | Definition/Key Point |
|---|--------------|---------------------|
| 1 | **Linked List** | A linear data structure where elements (nodes) are stored in non-contiguous memory locations, connected via pointers |
| 2 | **Singly Linked List** | Each node has data and a single pointer (next) pointing to the successor node |
| 3 | **Doubly Linked List** | Each node has data, a next pointer (to successor), and a prev pointer (to predecessor) |
| 4 | **Circular Linked List** | Last node points back to the first node, forming a cycle |
| 5 | **Head** | The first node in a linked list; entry point for traversal |
| 6 | **Tail** | The last node in a linked list; points to NULL (or head in circular) |
| 7 | **Node** | A fundamental unit containing data and pointer(s) |
| 8 | **Traversal** | The process of visiting each node in the list exactly once |
| 9 | **Dynamic Memory** | Memory allocated at runtime; linked lists use dynamic allocation |
| 10 | **O(1) Insertion** | Insertion at beginning of linked list (no shifting required) |
| 11 | **O(n) Search** | Linear search required to find an element (no random access) |
| 12 | **NULL Pointer** | A pointer that points to nothing; marks end of singly/doubly linked list |
| 13 | **Memory Overhead** | Extra memory needed for storing pointers in linked lists vs arrays |
| 14 | **Round-Robin Scheduling** | CPU scheduling algorithm using circular linked lists |
| 15 | **Playlist (Circular)** | Music player implementation using circular linked list for repeat functionality |

---

## 8. Delhi University Syllabus Context

This study material aligns with the **BSc Physical Science (Computer Science)** curriculum under **NEP 2024** for the course **Ge4A Data Structures**. The content covers:

- ✅ Understanding of fundamental data structures
- ✅ Implementation of linked list variations
- ✅ Time and space complexity analysis
- ✅ Practical applications (as required by industry-oriented learning)
- ✅ Problem-solving skills through MCQs and code examples

**Reference Topics from Typical DU Syllabus:**
- Linked List as a dynamic data structure
- Singly Linked List: Creation, Insertion, Deletion, Traversal
- Doubly Linked List: Operations and bidirectional traversal
- Circular Linked List: Applications and implementation
- Comparison with other data structures

---

## 9. Key Takeaways

1. **Linked Lists are Dynamic**: Unlike arrays, linked lists can grow and shrink during execution, making them ideal for scenarios where the size is unknown or changes frequently.

2. **Singly vs Doubly vs Circular**:
   - **Singly**: Simple, memory-efficient, forward-only traversal
   - **Doubly**: Allows bidirectional traversal, easier deletion with node reference
   - **Circular**: Enables continuous looping, eliminates NULL checks, perfect for round-robin processes

3. **Time Complexity Matters**:
   - Insertion/Deletion at beginning: **O(1)** for all linked list types
   - Insertion/Deletion at end: **O(n)** singly; **O(1)** with tail pointer or doubly circular
   - Search: Always **O(n)** (linear search required)

4. **Space Trade-off**: Linked lists use extra memory for pointers (~8 bytes per pointer in 64-bit systems), but this overhead enables flexibility.

5. **Real-World Applications**:
   - Browsers use doubly linked lists for history navigation
   - Music players use circular linked lists for playlist looping
   - Operating systems use circular lists for scheduling

6. **Choose Wisely**: Select the appropriate linked list type based on requirements:
   - Need backward traversal? → Doubly
   - Need continuous looping? → Circular
   - Memory constrained? → Singly

7. **Practice is Essential**: Implementation of these data structures builds strong foundation for understanding trees and graphs, which are advanced topics in data structures.

---

*Study Material prepared for BSc Physical Science (CS) - Delhi University, NEP 2024*