# Singly, Doubly & Circular Linked Lists
## Data Structures - BSc (Hons) Computer Science (NEP 2024 UGCF)
### Delhi University

---

## Learning Objectives

After studying this chapter, students will be able to:
- Understand the limitations of arrays and the need for linked lists
- Implement Singly Linked List with all operations (insertion, deletion, traversal, search)
- Implement Doubly Linked List with forward and backward traversal
- Understand Circular Linked Lists and their applications
- Analyze time and space complexity of all operations
- Identify edge cases and handle them appropriately
- Apply linked lists in real-world scenarios

---

## 1. Introduction

### 1.1 The Problem with Arrays

Arrays are the simplest linear data structure, but they suffer from significant limitations:

- **Fixed Size**: Arrays require contiguous memory allocation at declaration time
- **Inefficient Insertion/Deletion**: Inserting or deleting an element requires shifting all subsequent elements
- **Wasted Memory**: Pre-allocating large arrays leads to memory waste when not all slots are used

### 1.2 Enter Linked Lists

A **linked list** is a linear data structure where elements (called **nodes**) are stored in random memory locations. Each node contains:
1. **Data** - The actual information
2. **Pointer/Link** - Address of the next (and/or previous) node

### 1.3 Real-World Relevance

Linked lists are everywhere in computing:
- **Music Players**: Playlists use circular linked lists to repeat songs seamlessly
- **Browser History**: Back/Forward navigation uses doubly linked lists
- **Operating Systems**: Process scheduling, memory management
- **Undo/Redo Features**: Text editors use doubly linked lists
- **File Systems**: Directory structures

---

## 2. Singly Linked List (SLL)

### 2.1 Structure

Each node contains:
- **Data field**: Stores the value
- **Next pointer**: Stores address of the next node

```
┌─────────┬────────────┐
│  Data   │   Next     │
│   10    │  ──────►   │
└─────────┴────────────┘
```

### 2.2 Node Definition (C)

```c
struct Node {
    int data;
    struct Node* next;
};
```

### 2.3 Basic Operations

#### a) Traversal
```c
void traverse(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}
```

#### b) Insertion at Beginning
```c
struct Node* insertAtBeginning(struct Node* head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = head;
    return newNode;  // New node becomes new head
}
```

#### c) Insertion at End
```c
struct Node* insertAtEnd(struct Node* head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    
    if (head == NULL) {
        return newNode;
    }
    
    struct Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    return head;
}
```

#### d) Deletion at Beginning
```c
struct Node* deleteAtBeginning(struct Node* head) {
    if (head == NULL) return NULL;
    struct Node* temp = head;
    head = head->next;
    free(temp);
    return head;
}
```

#### e) Deletion at End
```c
struct Node* deleteAtEnd(struct Node* head) {
    if (head == NULL) return NULL;
    if (head->next == NULL) {
        free(head);
        return NULL;
    }
    
    struct Node* current = head;
    while (current->next->next != NULL) {
        current = current->next;
    }
    free(current->next);
    current->next = NULL;
    return head;
}
```

#### f) Search
```c
int search(struct Node* head, int key) {
    struct Node* current = head;
    int position = 1;
    while (current != NULL) {
        if (current->data == key) {
            return position;
        }
        current = current->next;
        position++;
    }
    return -1;  // Not found
}
```

### 2.4 Example: Managing a Queue

```c
// Simple queue implementation using SLL
struct Queue {
    struct Node *front, *rear;
};

void enqueue(struct Queue* q, int value) {
    struct Node* newNode = createNode(value);
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
        return;
    }
    q->rear->next = newNode;
    q->rear = newNode;
}

int dequeue(struct Queue* q) {
    if (q->front == NULL) return -1;
    struct Node* temp = q->front;
    int data = temp->data;
    q->front = q->front->next;
    if (q->front == NULL) q->rear = NULL;
    free(temp);
    return data;
}
```

---

## 3. Doubly Linked List (DLL)

### 3.1 Why Doubly Linked Lists?

Singly linked lists allow traversal in only one direction. Doubly linked lists provide:
- **Bi-directional traversal**
- **Efficient deletion** (no need to find previous node)
- **Undo operations** in applications

### 3.2 Structure

Each node contains:
- **Previous pointer**: Address of the previous node
- **Data field**: The actual information
- **Next pointer**: Address of the next node

```
┌──────────┬─────────┬──────────┐
│  Prev    │  Data   │  Next    │
│  ◄────── │   20    │ ──────►  │
└──────────┴─────────┴──────────┘
```

### 3.3 Node Definition (C)

```c
struct DNode {
    struct DNode* prev;
    int data;
    struct DNode* next;
};
```

### 3.4 Basic Operations

#### a) Insertion at Beginning
```c
struct DNode* insertAtBeginning(struct DNode* head, int value) {
    struct DNode* newNode = (struct DNode*)malloc(sizeof(struct DNode));
    newNode->data = value;
    newNode->prev = NULL;
    newNode->next = head;
    
    if (head != NULL) {
        head->prev = newNode;
    }
    return newNode;
}
```

#### b) Insertion at End
```c
struct DNode* insertAtEnd(struct DNode* head, int value) {
    struct DNode* newNode = (struct DNode*)malloc(sizeof(struct DNode));
    newNode->data = value;
    newNode->next = NULL;
    
    if (head == NULL) {
        newNode->prev = NULL;
        return newNode;
    }
    
    struct DNode* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    newNode->prev = current;
    return head;
}
```

#### c) Deletion at Position
```c
struct DNode* deleteNode(struct DNode* head, struct DNode* del) {
    if (head == NULL || del == NULL) return head;
    
    if (head == del) {
        head = del->next;
    }
    
    if (del->next != NULL) {
        del->next->prev = del->prev;
    }
    
    if (del->prev != NULL) {
        del->prev->next = del->next;
    }
    
    free(del);
    return head;
}
```

#### d) Traversal Forward
```c
void traverseForward(struct DNode* head) {
    struct DNode* current = head;
    while (current != NULL) {
        printf("%d <-> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}
```

#### e) Traversal Backward
```c
void traverseBackward(struct DNode* head) {
    if (head == NULL) return;
    
    // Go to last node
    struct DNode* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    // Traverse backward
    while (current != NULL) {
        printf("%d <-> ", current->data);
        current = current->prev;
    }
    printf("NULL\n");
}
```

### 3.5 Example: Browser History

```c
// Browser Back/Forward simulation
struct BrowserHistory {
    struct DNode* current;  // Current page
    struct DNode* tail;     // Most recent page
};

void visit(struct BrowserHistory* history, char* url) {
    struct DNode* newNode = (struct DNode*)malloc(sizeof(struct DNode));
    newNode->data = url;
    newNode->next = NULL;
    
    if (history->current != NULL) {
        history->current->next = newNode;
        newNode->prev = history->current;
    }
    
    history->current = newNode;
    history->tail = newNode;
}

char* back(struct BrowserHistory* history, int steps) {
    for (int i = 0; i < steps && history->current->prev != NULL; i++) {
        history->current = history->current->prev;
    }
    return history->current->data;
}

char* forward(struct BrowserHistory* history, int steps) {
    for (int i = 0; i < steps && history->current->next != NULL; i++) {
        history->current = history->current->next;
    }
    return history->current->data;
}
```

---

## 4. Circular Linked Lists

### 4.1 What is a Circular Linked List?

In a circular linked list, the last node points back to the first node (head), forming a circle. This can be:

- **Circular Singly Linked List**: Last node's next points to head
- **Circular Doubly Linked List**: Last node's next points to head, first node's prev points to tail

### 4.2 Visual Representation

```
Circular Singly:
    ┌──┐     ┌──┐     ┌──┐
    │10│────►│20│────►│30│────┐
    └──┘     └──┘     └──┘    │
         ▲─────────────────────┘

Circular Doubly:
       ┌──────────────────────┐
       │                      │
    ┌──┴──┐  ┌──┴──┐  ┌──┴──┐
    │ 10  │◄─│ 20  │◄─│ 30  │
    └──┬──┘  └──┬──┘  └──┬──┘
       │       │       │
       └───────┴───────┘
```

### 4.3 Node Definition

```c
// Circular Singly
struct CSNode {
    int data;
    struct CSNode* next;
};

// Circular Douly
struct CDNode {
    struct CDNode* prev;
    int data;
    struct CDNode* next;
};
```

### 4.4 Operations on Circular Linked List

#### a) Insertion in Circular Singly Linked List (at end)
```c
struct CSNode* insertAtEnd(struct CSNode* head, int value) {
    struct CSNode* newNode = (struct CSNode*)malloc(sizeof(struct CSNode));
    newNode->data = value;
    
    if (head == NULL) {
        newNode->next = newNode;  // Points to itself
        return newNode;
    }
    
    struct CSNode* current = head;
    while (current->next != head) {
        current = current->next;
    }
    current->next = newNode;
    newNode->next = head;
    return head;
}
```

#### b) Deletion in Circular Singly Linked List
```c
struct CSNode* deleteNode(struct CSNode* head, int key) {
    if (head == NULL) return NULL;
    
    struct CSNode* current = head;
    struct CSNode* prev = NULL;
    
    // Find the node to delete
    while (current->data != key) {
        if (current->next == head) {
            printf("Node not found\n");
            return head;
        }
        prev = current;
        current = current->next;
    }
    
    // Single node case
    if (current->next == head && prev == NULL) {
        free(current);
        return NULL;
    }
    
    // Delete head
    if (current == head) {
        prev = head;
        while (prev->next != head) {
            prev = prev->next;
        }
        head = head->next;
        prev->next = head;
    } else {
        prev->next = current->next;
    }
    
    free(current);
    return head;
}
```

### 4.5 Applications of Circular Linked Lists

| Application | Use Case |
|-------------|----------|
| **Round Robin Scheduling** | Process scheduling in OS |
| **Music Players** | Playlist looping |
| **Circular Buffers** | Producer-consumer problems |
| **Fibonacci Heap** | Advanced data structures |
| **Multiplayer Games** | Turn-based games |

### 4.6 Example: Round Robin CPU Scheduling

```c
struct Process {
    int pid;
    int burstTime;
    struct Process* next;
};

struct Process* addProcess(struct Process* head, int pid, int burst) {
    struct Process* newProcess = (struct Process*)malloc(sizeof(struct Process));
    newProcess->pid = pid;
    newProcess->burstTime = burst;
    
    if (head == NULL) {
        newProcess->next = newProcess;
        return newProcess;
    }
    
    struct Process* current = head;
    while (current->next != head) {
        current = current->next;
    }
    current->next = newProcess;
    newProcess->next = head;
    return head;
}

void executeRoundRobin(struct Process* head, int quantum) {
    if (head == NULL) return;
    
    struct Process* current = head;
    while (current != NULL) {
        printf("Executing Process %d for %d units\n", 
               current->pid, 
               (current->burstTime < quantum) ? current->burstTime : quantum);
        
        current->burstTime -= quantum;
        
        if (current->burstTime <= 0) {
            printf("Process %d completed\n", current->pid);
            // Remove completed process from circular list
            // (deletion code would go here)
        }
        
        current = current->next;
        if (current == head && current->burstTime <= 0) break;
    }
}
```

---

## 5. Complexity Analysis

### 5.1 Time Complexity

| Operation | Singly LL | Doubly LL | Circular Singly |
|-----------|-----------|-----------|-----------------|
| Insert at Beginning | O(1) | O(1) | O(n) |
| Insert at End | O(n) | O(n)* | O(1) |
| Delete at Beginning | O(1) | O(1) | O(n) |
| Delete at End | O(n) | O(1)** | O(n) |
| Search | O(n) | O(n) | O(n) |
| Traversal | O(n) | O(n) | O(n) |

*With tail pointer: O(1)
**Without tail pointer: O(n)

### 5.2 Space Complexity

- **All Linked Lists**: O(n) where n is number of nodes
- **Additional Memory**: Each node requires extra space for pointer(s)

### 5.3 Comparison with Arrays

| Criteria | Array | Linked List |
|----------|-------|-------------|
| Random Access | O(1) | O(n) |
| Insertion at Beginning | O(n) | O(1) |
| Deletion at Beginning | O(n) | O(1) |
| Insertion at End | O(1)* | O(n) |
| Memory Efficiency | Fixed size | Dynamic |
| Cache Performance | Better | Worse |

*With pre-allocation

---

## 6. Edge Cases and Practical Considerations

### 6.1 Common Edge Cases

1. **Empty List**: All operations must handle NULL head gracefully
2. **Single Node**: Deletion should handle both prev and next being NULL
3. **First/Last Node Operations**: Special handling for boundary conditions
4. **Memory Leaks**: Always free deleted nodes
5. **Circular List Infinite Loop**: Ensure termination conditions in traversal

### 6.2 Handling Edge Cases in Code

```c
// Safe deletion with edge case handling
struct Node* safeDelete(struct Node* head, int key) {
    // Edge case 1: Empty list
    if (head == NULL) {
        printf("List is empty\n");
        return NULL;
    }
    
    // Edge case 2: Single node
    if (head->data == key && head->next == head) {
        free(head);
        return NULL;
    }
    
    // Normal deletion logic...
    return head;
}
```

### 6.3 Memory Management Best Practices

- Always initialize pointers to NULL
- Check for NULL before dereferencing
- Free memory after deletion
- Handle allocation failures with NULL checks

---

## 7. Delhi University Examination Tips

### Important Topics for Exams:
1. Difference between array and linked list
2. All insertion/deletion operations (with diagrams)
3. Time complexity comparisons
4. Circular linked list advantages
5. Applications of different linked list types

---

## 8. Multiple Choice Questions

1. **Which linked list allows traversal in both directions?**
   - [a] Singly Linked List
   - [b] Doubly Linked List
   - [c] Circular Linked List
   - [d] None of the above
   
   **Answer: (b) Doubly Linked List**

2. **What is the time complexity of inserting at the beginning of a Singly Linked List?**
   - [a] O(n)
   - [b] O(1)
   - [c] O(n²)
   - [d] O(log n)
   
   **Answer: (b) O(1)**

3. **In a circular linked list, the last node points to:**
   - [a] NULL
   - [b] First node (head)
   - [c] Last node
   - [d] None
   
   **Answer: (b) First node (head)**

4. **Which data structure is best for implementing "Undo" functionality?**
   - [a] Singly Linked List
   - [b] Doubly Linked List
   - [c] Array
   - [d] Stack
   
   **Answer: (b) Doubly Linked List**

5. **What is the space complexity of a linked list with n nodes?**
   - [a] O(1)
   - [b] O(n)
   - [c] O(log n)
   - [d] O(n²)
   
   **Answer: (b) O(n)**

6. **Which operation is NOT efficient in a singly linked list?**
   - [a] Insertion at beginning
   - [b] Deletion at beginning
   - [c] Deletion at end
   - [d] Traversal
   
   **Answer: (c) Deletion at end**

7. **The main advantage of circular linked lists is:**
   - [a] No NULL pointer issues
   - [b] Can be traversed infinitely
   - [c] Memory efficiency for round-robin
   - [d] All of the above
   
   **Answer: (c) Memory efficiency for round-robin**

8. **In a doubly linked list, each node contains:**
   - [a] One pointer
   - [b] Two pointers
   - [c] Three pointers
   - [d] No pointers
   
   **Answer: (b) Two pointers**

9. **What happens when you delete the only node in a singly linked list?**
   - [a] Nothing happens
   - [b] Head becomes NULL
   - [c] Memory leak occurs
   - [d] Program crashes
   
   **Answer: (b) Head becomes NULL**

10. **Which is NOT an application of linked lists?**
    - [a] Polynomial representation
    - [b] Hash tables (chaining)
    - [c] Binary search trees
    - [d] Random access memory
    
    **Answer: (d) Random access memory**

---

## 9. Flashcards

| Term | Definition |
|------|------------|
| **Node** | Basic unit of a linked list containing data and pointer(s) |
| **Head** | First node in a linked list |
| **Tail** | Last node in a linked list (points to NULL) |
| **Singly Linked List** | Each node has only a next pointer |
| **Doubly Linked List** | Each node has prev and next pointers |
| **Circular Linked List** | Last node points back to head |
| **Traversal** | Visiting each node exactly once |
| **Dynamic Memory** | Memory allocated at runtime using malloc |
| **NULL Pointer** | Pointer that doesn't point to any valid memory location |
| **Time Complexity** | Measure of execution time as function of input size |
| **Space Complexity** | Measure of memory usage as function of input size |
| **Round Robin** | CPU scheduling using circular linked list |
| **Random Access** | Direct access to any element (O(1)) |
| **Sequential Access** | Accessing elements one by one in order |

---

## Key Takeaways

1. **Linked Lists vs Arrays**: Linked lists provide dynamic memory allocation, efficient insertions/deletions at the beginning, but lack random access capability.

2. **Singly Linked Lists** are optimal when:
   - Memory is limited (only one pointer per node)
   - Unidirectional traversal is sufficient
   - Stack implementation is needed

3. **Doubly Linked Lists** are optimal when:
   - Bidirectional traversal is required
   - Frequent deletions from the middle
   - Implementing undo/redo features
   - Browser history management

4. **Circular Linked Lists** are essential for:
   - Round-robin scheduling
   - Continuous looping (music players)
   - Applications requiring cyclic behavior
   - Avoiding NULL checks at the end

5. **Time Complexity Matters**: Always choose the data structure based on the most frequent operations your application will perform.

6. **Memory Trade-off**: Linked lists use more memory than arrays due to pointer storage, but provide flexibility that arrays cannot match.

7. **Practical Applications**: From operating systems to web browsers, linked lists form the backbone of many real-world software systems.

---

*Prepared for BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)*