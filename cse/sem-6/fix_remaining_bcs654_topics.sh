#!/bin/bash

# Fix remaining wrong topics in BCS654A and BCS654B

BASE="/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/sem-6"

echo "Fixing remaining BCS654A (Data Structures) topics..."

# module-2/introduction - should be about Stacks and Queues
cat > "$BASE/bcs654a-introduction-to-data-structures/chapters/module-2/topics/introduction/read.md" << 'EOF'
# Introduction to Stacks and Queues

## Overview

Stacks and Queues are fundamental linear data structures that are widely used in computer science and programming. Both are abstract data types that organize data in specific ways, but they differ in how elements are added and removed.

## Stack Data Structure

### Definition

A **Stack** is a linear data structure that follows the **Last-In-First-Out (LIFO)** principle. This means the last element added to the stack is the first one to be removed.

**Real-world analogy:** A stack of plates - you can only add or remove plates from the top.

### Basic Operations

1. **Push**: Add an element to the top of the stack
2. **Pop**: Remove and return the top element
3. **Peek/Top**: Return the top element without removing it
4. **isEmpty**: Check if stack is empty
5. **isFull**: Check if stack is full (for array implementation)

### Applications of Stacks

- Function call management (call stack)
- Expression evaluation and conversion
- Backtracking algorithms
- Undo mechanism in editors
- Browser back button
- Syntax parsing in compilers

## Queue Data Structure

### Definition

A **Queue** is a linear data structure that follows the **First-In-First-Out (FIFO)** principle. This means the first element added to the queue is the first one to be removed.

**Real-world analogy:** A line of people waiting - first person in line is served first.

### Basic Operations

1. **Enqueue**: Add an element to the rear of the queue
2. **Dequeue**: Remove and return the front element  
3. **Front**: Return the front element without removing it
4. **Rear**: Return the rear element
5. **isEmpty**: Check if queue is empty
6. **isFull**: Check if queue is full (for array implementation)

### Applications of Queues

- CPU scheduling
- Disk scheduling
- Print job scheduling
- BFS traversal in graphs
- Handling requests in web servers
- Simulation of real-world queues

## Comparison: Stack vs Queue

| Feature | Stack | Queue |
|---------|-------|-------|
| Principle | LIFO | FIFO |
| Insertion | Top (Push) | Rear (Enqueue) |
| Deletion | Top (Pop) | Front (Dequeue) |
| Access | Only top element | Front and rear |
| Applications | Recursion, backtracking | Scheduling, buffering |

## Importance in Data Structures

Both stacks and queues are essential building blocks for:
- More complex data structures
- Algorithm implementation
- System programming
- Application development

Understanding these structures is crucial for solving many programming problems efficiently.

## Exam Tips

1. Understand LIFO vs FIFO principles clearly
2. Know all basic operations and their time complexities
3. Be able to implement using both arrays and linked lists
4. Remember real-world applications
5. Practice drawing diagrams for operations
6. Understand overflow and underflow conditions
EOF

echo "✓ Fixed module-2/introduction"

# module-3/introduction - should be about Linked Lists
cat > "$BASE/bcs654a-introduction-to-data-structures/chapters/module-3/topics/introduction/read.md" << 'EOF'
# Introduction to Linked Lists

## What is a Linked List?

A **Linked List** is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked list elements are not stored in contiguous memory locations.

## Why Linked Lists?

### Limitations of Arrays

1. **Fixed Size**: Arrays have fixed size, difficult to extend
2. **Memory Waste**: Unused allocated memory is wasted
3. **Insertion/Deletion Cost**: O(n) time for insertion/deletion in middle
4. **Contiguous Memory**: Requires large contiguous memory block

### Advantages of Linked Lists

1. **Dynamic Size**: Can grow or shrink during runtime
2. **Efficient Insertion/Deletion**: O(1) if position is known
3. **No Memory Waste**: Only allocate what's needed
4. **No Contiguous Memory**: Can use scattered memory locations

## Node Structure

Each node in a linked list contains:
1. **Data**: The actual value stored
2. **Pointer/Link**: Reference to the next node

```c
struct Node {
    int data;           // Data part
    struct Node* next;  // Pointer to next node
};
```

## Types of Linked Lists

### 1. Singly Linked List
- Each node points to the next node
- Last node points to NULL
- Traversal only in forward direction

### 2. Doubly Linked List
- Each node has two pointers: next and previous
- Can traverse in both directions
- Requires more memory

### 3. Circular Linked List
- Last node points back to first node
- No NULL at the end
- Can start from any node

### 4. Circular Doubly Linked List
- Combination of doubly and circular
- Both forward and backward links form circles

## Basic Concepts

### Head Pointer
- Points to the first node of the list
- Entry point for accessing the list
- If head is NULL, list is empty

### Traversal
Process of visiting each node once:
```
Start from head → Follow next pointers → Stop at NULL
```

### Memory Allocation
- Nodes created dynamically using malloc()
- Each node can be anywhere in memory
- Linked together using pointers

## Comparison with Arrays

| Feature | Array | Linked List |
|---------|-------|-------------|
| Size | Fixed | Dynamic |
| Memory | Contiguous | Non-contiguous |
| Access | O(1) - Random | O(n) - Sequential |
| Insertion | O(n) | O(1) at known position |
| Deletion | O(n) | O(1) at known position |
| Memory Usage | Can waste space | Efficient, but overhead for pointers |

## Applications

1. **Dynamic Memory Allocation**: Free lists in memory managers
2. **Implementation of Stacks and Queues**: Dynamic versions
3. **Polynomial Representation**: Each term as a node
4. **Music/Video Playlists**: Navigate songs
5. **Undo Functionality**: Previous states
6. **Hash Tables**: Chaining for collision handling
7. **Graphs**: Adjacency list representation

## Advantages and Disadvantages

### Advantages
- Dynamic size
- Ease of insertion/deletion
- No memory waste
- Implementation of other data structures

### Disadvantages
- No random access
- Extra memory for pointers
- Not cache friendly
- Traversal is slower than arrays

## Exam Tips

1. Understand node structure thoroughly
2. Know all types of linked lists
3. Understand pointer manipulation
4. Practice drawing linked list diagrams
5. Remember time complexities
6. Know applications and when to use linked lists
7. Understand differences from arrays
EOF

echo "✓ Fixed module-3/introduction"

# module-3/operations - should be about linked list operations
cat > "$BASE/bcs654a-introduction-to-data-structures/chapters/module-3/topics/operations/read.md" << 'EOF'
# Operations on Linked Lists

## Fundamental Operations

Linked lists support various operations for manipulating data. Understanding these operations is crucial for working with linked lists effectively.

## 1. Creating a Node

Before performing any operation, we need to create nodes.

```c
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
```

## 2. Insertion Operations

### Insert at Beginning
**Time Complexity:** O(1)

```c
void insertAtBeginning(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}
```

### Insert at End
**Time Complexity:** O(n)

```c
void insertAtEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}
```

### Insert at Position
**Time Complexity:** O(n)

```c
void insertAtPosition(struct Node** head, int data, int position) {
    struct Node* newNode = createNode(data);
    if (position == 1) {
        newNode->next = *head;
        *head = newNode;
        return;
    }
    struct Node* temp = *head;
    for (int i = 1; i < position - 1 && temp != NULL; i++) {
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("Invalid position\\n");
        return;
    }
    newNode->next = temp->next;
    temp->next = newNode;
}
```

## 3. Deletion Operations

### Delete from Beginning
**Time Complexity:** O(1)

```c
void deleteFromBeginning(struct Node** head) {
    if (*head == NULL) return;
    struct Node* temp = *head;
    *head = (*head)->next;
    free(temp);
}
```

### Delete from End
**Time Complexity:** O(n)

```c
void deleteFromEnd(struct Node** head) {
    if (*head == NULL) return;
    if ((*head)->next == NULL) {
        free(*head);
        *head = NULL;
        return;
    }
    struct Node* temp = *head;
    while (temp->next->next != NULL) {
        temp = temp->next;
    }
    free(temp->next);
    temp->next = NULL;
}
```

### Delete by Value
**Time Complexity:** O(n)

```c
void deleteByValue(struct Node** head, int key) {
    if (*head == NULL) return;
    if ((*head)->data == key) {
        struct Node* temp = *head;
        *head = (*head)->next;
        free(temp);
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL && temp->next->data != key) {
        temp = temp->next;
    }
    if (temp->next == NULL) return;
    struct Node* toDelete = temp->next;
    temp->next = temp->next->next;
    free(toDelete);
}
```

## 4. Searching Operations

### Search by Value
**Time Complexity:** O(n)

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
    return -1; // Not found
}
```

## 5. Traversal Operations

### Display List
**Time Complexity:** O(n)

```c
void display(struct Node* head) {
    if (head == NULL) {
        printf("List is empty\\n");
        return;
    }
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\\n");
}
```

## 6. Utility Operations

### Count Nodes
```c
int countNodes(struct Node* head) {
    int count = 0;
    struct Node* temp = head;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    return count;
}
```

### Reverse List
**Time Complexity:** O(n)

```c
void reverse(struct Node** head) {
    struct Node *prev = NULL, *current = *head, *next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
}
```

## Time Complexity Summary

| Operation | Time Complexity |
|-----------|----------------|
| Insert at beginning | O(1) |
| Insert at end | O(n) |
| Insert at position | O(n) |
| Delete from beginning | O(1) |
| Delete from end | O(n) |
| Delete by value | O(n) |
| Search | O(n) |
| Display | O(n) |
| Reverse | O(n) |

## Space Complexity

All operations have O(1) space complexity (not counting the space for the list itself).

## Exam Tips

1. Understand pointer manipulation thoroughly
2. Remember to check for NULL before operations
3. Know time complexity of each operation
4. Practice drawing step-by-step diagrams
5. Remember to free deleted nodes
6. Handle edge cases: empty list, single node
7. Understand the difference between operations on different types of linked lists
EOF

echo "✓ Fixed module-3/operations"

# module-4/introduction - should be about Trees
cat > "$BASE/bcs654a-introduction-to-data-structures/chapters/module-4/topics/introduction/read.md" << 'EOF'
# Introduction to Trees

## What is a Tree?

A **Tree** is a hierarchical, non-linear data structure consisting of nodes connected by edges. It is one of the most important data structures in computer science, used to represent hierarchical relationships.

**Definition:** A tree is a collection of nodes where:
- One node is designated as the root
- Every node (except root) is connected by exactly one edge from another node (its parent)
- There is exactly one path between root and any node

## Why Trees?

### Limitations of Linear Data Structures

1. **Fixed Access Pattern**: Arrays/Linked lists support sequential access
2. **Slow Operations**: Search can be O(n) in linear structures
3. **No Hierarchy**: Cannot naturally represent hierarchical data

### Advantages of Trees

1. **Hierarchical Structure**: Natural representation of hierarchical data
2. **Efficient Operations**: O(log n) for balanced trees
3. **Flexible**: Can represent various relationships
4. **Sorted Data**: BSTs maintain sorted order

## Basic Terminology

### Node and Relationships

```
         A (Root)
        / \\
       B   C
      / \\   \\
     D   E   F
```

- **Node**: Each element (A, B, C, D, E, F)
- **Root**: Top node with no parent (A)
- **Parent**: Node with children (B is parent of D and E)
- **Child**: Node with a parent (B and C are children of A)
- **Siblings**: Nodes with same parent (B and C are siblings)
- **Leaf**: Node with no children (D, E, F)
- **Internal Node**: Node with at least one child (A, B, C)
- **Edge**: Connection between nodes

### Path and Level

- **Path**: Sequence of nodes connected by edges
  - Path from A to E: A → B → E
- **Level**: Distance from root (root is at level 0)
  - Level 0: A
  - Level 1: B, C
  - Level 2: D, E, F
- **Depth**: Number of edges from root to node
- **Height**: Number of edges in longest path from node to leaf
  - Height of tree = Height of root

## Types of Trees

### 1. Binary Tree
Each node has at most 2 children (left and right).

### 2. Binary Search Tree (BST)
Binary tree where left < root < right for all nodes.

### 3. Full Binary Tree
Every node has 0 or 2 children.

### 4. Complete Binary Tree
All levels filled except possibly the last (filled left to right).

### 5. Perfect Binary Tree
All internal nodes have 2 children, all leaves at same level.

### 6. Balanced Binary Tree
Height difference of left and right subtrees ≤ 1 for all nodes.

### 7. AVL Tree
Self-balancing BST.

### 8. B-Tree
Multi-way search tree used in databases.

## Properties of Binary Trees

1. **Maximum nodes at level L**: 2^L
2. **Maximum nodes in tree of height h**: 2^(h+1) - 1
3. **Minimum height for n nodes**: ⌈log₂(n+1)⌉ - 1
4. **For n nodes, number of edges**: n - 1
5. **If leaf nodes = L, nodes with 2 children = T, then**: L = T + 1

## Node Structure

### Binary Tree Node
```c
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
```

### Creating a Node
```c
struct Node* createNode(int data) {
    struct Node* newNode = malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
```

## Applications of Trees

1. **File Systems**: Directory structure
2. **Databases**: B-trees for indexing
3. **Compilers**: Syntax trees
4. **XML/HTML**: DOM structure
5. **AI**: Decision trees
6. **Networks**: Routing algorithms
7. **Graphics**: Scene graphs
8. **Operating Systems**: Process trees

## Advantages and Disadvantages

### Advantages
- Hierarchical representation
- Efficient search (BST)
- Flexible size
- Natural recursion

### Disadvantages
- Complex implementation
- More memory for pointers
- Balancing overhead
- Sequential access slower than arrays

## Exam Tips

1. Memorize all terminology
2. Understand tree properties and formulas
3. Know all types of binary trees
4. Practice drawing trees
5. Calculate height, depth, levels
6. Remember node structure
7. Understand applications
8. Know time complexities
EOF

echo "✓ Fixed module-4/introduction"

# module-5/introduction - should be about Searching and Sorting
cat > "$BASE/bcs654a-introduction-to-data-structures/chapters/module-5/topics/introduction/read.md" << 'EOF'
# Introduction to Searching and Sorting

## Overview

Searching and Sorting are fundamental operations in computer science and data structures. They are among the most frequently performed operations on data and form the basis for many algorithms.

## Searching

### What is Searching?

**Searching** is the process of finding a particular element or checking whether an element exists in a given collection of data.

### Why Searching is Important

1. **Data Retrieval**: Quick access to information
2. **Database Operations**: Core operation in databases
3. **Decision Making**: Basis for conditional logic
4. **Optimization**: Finding best solutions

### Types of Searching

#### 1. Linear Search
- Sequential search through elements
- Works on unsorted data
- Time Complexity: O(n)

#### 2. Binary Search
- Divide and conquer approach
- Requires sorted data
- Time Complexity: O(log n)

### Applications of Searching

- Finding records in database
- Dictionary lookups
- Phone directory
- Web search engines
- File systems

## Sorting

### What is Sorting?

**Sorting** is the process of arranging data in a particular order (ascending or descending).

### Why Sorting is Important

1. **Efficient Searching**: Enables binary search
2. **Data Presentation**: Organized display
3. **Optimization**: Many algorithms work better on sorted data
4. **Database Operations**: Indexing and queries
5. **Data Analysis**: Finding patterns

### Classification of Sorting

#### By Complexity
- **Simple Sorts**: Bubble, Selection, Insertion - O(n²)
- **Efficient Sorts**: Merge, Quick, Heap - O(n log n)
- **Linear Sorts**: Counting, Radix, Bucket - O(n)

#### By Method
- **Comparison-based**: Compare elements
- **Non-comparison**: Use properties of data

#### By Memory Usage
- **In-place**: O(1) extra space
- **Out-of-place**: O(n) extra space

#### By Stability
- **Stable**: Maintains relative order of equal elements
- **Unstable**: May change relative order

### Common Sorting Algorithms

#### 1. Bubble Sort
- Repeatedly swap adjacent elements
- Time: O(n²), Space: O(1)
- Stable

#### 2. Selection Sort
- Select minimum and place at beginning
- Time: O(n²), Space: O(1)
- Unstable

#### 3. Insertion Sort
- Build sorted array one element at a time
- Time: O(n²), Space: O(1)
- Stable

#### 4. Merge Sort
- Divide and conquer
- Time: O(n log n), Space: O(n)
- Stable

#### 5. Quick Sort
- Partition based on pivot
- Time: O(n log n) average, O(n²) worst, Space: O(log n)
- Unstable

#### 6. Heap Sort
- Use heap data structure
- Time: O(n log n), Space: O(1)
- Unstable

### Comparison of Sorting Algorithms

| Algorithm | Time (Avg) | Time (Worst) | Space | Stable | In-place |
|-----------|-----------|--------------|-------|--------|----------|
| Bubble Sort | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion Sort | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n²) | O(log n) | No | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(1) | No | Yes |

## Applications of Sorting

1. **Databases**: Organizing records
2. **Search Optimization**: Enabling binary search
3. **Data Analysis**: Finding median, percentiles
4. **Graphics**: Rendering order
5. **Compression**: Data compression algorithms
6. **Scheduling**: Job scheduling

## Choosing the Right Algorithm

### For Searching
- **Small data**: Linear search
- **Large sorted data**: Binary search
- **Dynamic data**: Hash tables

### For Sorting
- **Small data (<50)**: Insertion sort
- **Large data**: Quick sort or Merge sort
- **Stability needed**: Merge sort
- **Memory limited**: Heap sort or Quick sort
- **Nearly sorted**: Insertion sort

## Relationship Between Searching and Sorting

1. **Sorted data enables efficient searching**: Binary search requires sorted array
2. **Search during sorting**: Insertion sort searches for position
3. **Combined operations**: Many algorithms use both

## Exam Tips

1. Understand time and space complexity of each algorithm
2. Know which algorithms are stable
3. Remember in-place vs out-of-place sorting
4. Understand when to use which algorithm
5. Practice drawing diagrams for each algorithm
6. Know advantages and disadvantages
7. Understand relationship between sorting and searching
8. Remember real-world applications
EOF

echo "✓ Fixed module-5/introduction"

echo ""
echo "Fixing BCS654B (Operating Systems) topics..."

# module-2/process-management - should be about OS Process Management, not Software PM
cat > "$BASE/bcs654b-fundamentals-of-operating-systems/chapters/module-2/topics/process-management/read.md" << 'EOF'
# Process Management in Operating Systems

## Introduction

**Process Management** is one of the most important functions of an operating system. A process is a program in execution, and the OS must manage all processes efficiently to ensure optimal system performance.

## What is a Process?

**Definition:** A process is an instance of a program in execution, including the current values of the program counter, registers, and variables.

### Process vs Program

| Program | Process |
|---------|---------|
| Passive entity (code on disk) | Active entity (program in execution) |
| Static | Dynamic |
| Exists as file | Exists in memory |
| One program | Can have multiple processes |

## Process States

A process goes through various states during its lifetime:

```
         +-------+
         |  New  |
         +-------+
            ↓
         +-------+
    +--->| Ready |<---+
    |    +-------+    |
    |       ↓         |
    |    +-------+    |
    +----| Running|---+
         +-------+
            ↓
         +-------+
         |Waiting|
         +-------+
            ↓
         +-------+
         |Terminated|
         +-------+
```

### State Descriptions

1. **New**: Process is being created
2. **Ready**: Process is waiting to be assigned to CPU
3. **Running**: Instructions are being executed
4. **Waiting**: Process is waiting for some event (I/O completion)
5. **Terminated**: Process has finished execution

## Process Control Block (PCB)

The PCB is a data structure maintained by the OS for each process.

### Components of PCB

1. **Process State**: Current state (ready, running, waiting)
2. **Program Counter**: Address of next instruction
3. **CPU Registers**: Contents of all process-specific registers
4. **CPU Scheduling Information**: Priority, scheduling queue pointers
5. **Memory Management Information**: Page tables, memory limits
6. **Accounting Information**: CPU used, time limits
7. **I/O Status Information**: List of open files, I/O devices allocated

## Process Scheduling

### Scheduling Queues

1. **Job Queue**: All processes in the system
2. **Ready Queue**: All processes in main memory, ready to execute
3. **Device Queues**: Processes waiting for I/O devices

### Types of Schedulers

#### 1. Long-term Scheduler (Job Scheduler)
- Selects processes from disk and loads into memory
- Controls degree of multiprogramming
- Invoked infrequently

#### 2. Short-term Scheduler (CPU Scheduler)
- Selects process from ready queue to execute
- Invoked very frequently (milliseconds)
- Must be fast

#### 3. Medium-term Scheduler
- Removes processes from memory (swapping)
- Reduces degree of multiprogramming
- Swaps processes in and out

## Context Switching

**Definition:** Saving the state of currently running process and loading the state of the next process.

### Context Switch Steps

1. Save state of current process in its PCB
2. Update PCB with new state
3. Move PCB to appropriate queue
4. Select new process to run
5. Load state of new process from its PCB
6. Resume execution of new process

### Context Switch Time
- Pure overhead (system does no useful work)
- Typically a few milliseconds
- Depends on hardware support and PCB size

## Process Creation

### How Processes are Created

1. **System Initialization**: When OS boots
2. **User Request**: User starts a program
3. **Batch Job**: System executes batch jobs
4. **Process Spawning**: Existing process creates new process

### Parent and Child Processes

- Parent process creates child processes
- Child can create more processes → process tree
- Parent and child can execute concurrently or parent waits

### Process Creation in Unix/Linux

```c
pid_t pid = fork();

if (pid < 0) {
    // Fork failed
} else if (pid == 0) {
    // Child process
    execlp("/bin/ls", "ls", NULL);
} else {
    // Parent process
    wait(NULL);
}
```

### Resource Sharing Options

1. Parent and child share all resources
2. Child shares subset of parent's resources
3. Parent and child share no resources

## Process Termination

### Normal Termination
- Process completes execution
- Calls `exit()` system call
- Returns status to parent

### Abnormal Termination
- Fatal error
- Killed by another process
- Parent terminates

### Cascading Termination
- If parent terminates, all children are terminated
- OS ensures no orphan processes

## Inter-Process Communication (IPC)

### Why IPC?

1. Information sharing
2. Computation speedup
3. Modularity
4. Convenience

### IPC Models

#### 1. Shared Memory
- Processes share a region of memory
- Fast communication
- Requires synchronization

#### 2. Message Passing
- Processes communicate by exchanging messages
- Slower than shared memory
- Easier to implement
- Methods: Send() and Receive()

## Process Operations

### Operations on Processes

1. **Create**: Create new process
2. **Delete**: Terminate process
3. **Suspend**: Pause process temporarily
4. **Resume**: Continue suspended process
5. **Block**: Wait for event
6. **Wakeup**: Process becomes ready after event
7. **Dispatch**: Assign CPU to process
8. **Change Priority**: Modify scheduling priority

## Process Synchronization

### Need for Synchronization

- Multiple processes access shared data
- Results depend on order of execution
- Race condition can occur

### Critical Section Problem

- Section of code where shared data is accessed
- Only one process should execute critical section at a time
- Requirements:
  1. Mutual Exclusion
  2. Progress
  3. Bounded Waiting

## Threads

### What are Threads?

- Lightweight process
- Basic unit of CPU utilization
- Shares code, data, files with other threads of same process
- Has own program counter, register set, stack

### Benefits of Threads

1. **Responsiveness**: Continue execution even if part is blocked
2. **Resource Sharing**: Share memory and resources
3. **Economy**: Cheaper than process creation
4. **Scalability**: Utilize multiprocessor architectures

## Process Management System Calls

| System Call | Purpose |
|-------------|---------|
| fork() | Create new process |
| exec() | Execute new program |
| exit() | Terminate process |
| wait() | Wait for child process |
| getpid() | Get process ID |
| kill() | Send signal to process |

## Exam Tips

1. Understand process states and transitions
2. Know PCB components
3. Understand context switching overhead
4. Differentiate between process and program
5. Know fork(), exec(), wait() system calls
6. Understand IPC methods
7. Remember types of schedulers
8. Understand process creation and termination
9. Know the difference between processes and threads
10. Practice drawing process state diagrams
EOF

echo "✓ Fixed module-2/process-management"

# module-4/deadlocks - should be about OS Deadlocks, not Distributed Deadlocks
cat > "$BASE/bcs654b-fundamentals-of-operating-systems/chapters/module-4/topics/deadlocks/read.md" << 'EOF'
# Deadlocks in Operating Systems

## Introduction

A **deadlock** is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. It is one of the most critical issues in process synchronization and resource allocation.

**Definition:** Deadlock is a state where a group of processes are each waiting for an event that only another process in the group can cause, resulting in all processes being blocked indefinitely.

## System Model

### Resources and Processes

- **Resource**: Anything a process needs (CPU, memory, files, I/O devices)
- **Resource Types**: R₁, R₂, ..., Rₘ
- **Instances**: Each resource type has multiple instances

### Resource Allocation

```
Request → Use → Release
```

A process:
1. Requests resource
2. Uses resource
3. Releases resource

## Necessary Conditions for Deadlock

For a deadlock to occur, four conditions must hold **simultaneously**. These are called **Coffman Conditions**:

### 1. Mutual Exclusion
- At least one resource must be held in non-shareable mode
- Only one process can use the resource at a time
- If another process requests the resource, it must wait

**Example:** Printer - only one process can print at a time

### 2. Hold and Wait
- A process must be holding at least one resource
- And waiting to acquire additional resources held by other processes

**Example:** Process P1 holds printer, waits for scanner; Process P2 holds scanner, waits for printer

### 3. No Preemption
- Resources cannot be forcibly taken away
- Resource can only be released voluntarily by the process holding it
- Process must release resource after completing task

**Example:** Can't forcibly take a file from a process

### 4. Circular Wait
- A set of waiting processes {P₀, P₁, ..., Pₙ} exists such that:
  - P₀ is waiting for resource held by P₁
  - P₁ is waiting for resource held by P₂
  - ...
  - Pₙ is waiting for resource held by P₀

**Example:** P1 waits for P2, P2 waits for P3, P3 waits for P1

## Resource Allocation Graph (RAG)

A directed graph used to represent resource allocation and requests.

### Components

1. **Vertices**:
   - Processes (circles): P₁, P₂, ..., Pₙ
   - Resources (rectangles): R₁, R₂, ..., Rₘ

2. **Edges**:
   - **Request edge**: Process → Resource (P requests R)
   - **Assignment edge**: Resource → Process (R is assigned to P)

### Example RAG

```
P1 ---request---> R1
R1 ---assigned--> P2
P2 ---request---> R2
R2 ---assigned--> P1
```

### Detecting Deadlock Using RAG

- **If graph has no cycle**: No deadlock
- **If graph has cycle**:
  - Single instance per resource type: Deadlock exists
  - Multiple instances: Deadlock may exist

## Methods for Handling Deadlocks

### 1. Deadlock Prevention

Ensure at least one of the four necessary conditions cannot hold.

#### Strategies

**A. Mutual Exclusion**
- Not always possible to prevent
- Some resources are inherently non-shareable

**B. Hold and Wait**
- Require process to request all resources at once
- Or release all held resources before requesting new ones

**Disadvantages:**
- Low resource utilization
- Starvation possible

**C. No Preemption**
- If process holding resources requests another unavailable resource:
  - Preempt its currently held resources
  - Add to list of resources it's waiting for
  - Restart only when it can get all resources

**Disadvantages:**
- Difficult to implement
- May cause process to lose work

**D. Circular Wait**
- Impose total ordering on resource types
- Process can request resources only in increasing order

**Example:** If R1 < R2 < R3, process must request R1 before R2, R2 before R3

**Disadvantages:**
- May not match actual resource needs
- Reduces flexibility

### 2. Deadlock Avoidance

Use additional information to avoid entering unsafe states.

#### Safe State

A state is **safe** if system can allocate resources to each process in some order and still avoid deadlock.

```
Safe State → No Deadlock
Unsafe State → May lead to deadlock
```

#### Banker's Algorithm

**Purpose:** Decides whether to grant resource request

**How it works:**
1. System maintains information about available resources, allocated resources, and maximum needs
2. Before granting request, check if system will remain in safe state
3. Grant request only if safe state is maintained

**Advantages:**
- Avoids deadlock
- Maximum utilization

**Disadvantages:**
- Requires advance knowledge of maximum resource needs
- Number of processes must be fixed
- Resources must be known in advance

### 3. Deadlock Detection and Recovery

Allow deadlocks to occur, detect them, and recover.

#### Detection Algorithm

1. Maintain resource allocation graph
2. Periodically invoke detection algorithm to check for cycles
3. If cycle exists, deadlock detected

**Single Instance:** Check for cycles in RAG

**Multiple Instances:** Use matrix-based detection algorithm

#### Recovery from Deadlock

**A. Process Termination**

1. **Abort all deadlocked processes**
   - Simple but costly
   - Lose all computation done so far

2. **Abort processes one at a time**
   - Continue until deadlock cycle is eliminated
   - Choose victim based on:
     - Priority
     - Computation time
     - Resources held
     - Resources needed to complete

**B. Resource Preemption**

1. **Select victim**: Which process to preempt
2. **Rollback**: Return to safe state, restart
3. **Starvation**: Ensure same process not always picked

### 4. Ignore the Problem (Ostrich Algorithm)

- Pretend deadlocks never occur
- Used when deadlocks are rare
- Cost of prevention/avoidance/detection too high
- Example: Most operating systems including UNIX, Windows

## Comparison of Methods

| Method | Prevention | Avoidance | Detection | Ignore |
|--------|-----------|-----------|-----------|---------|
| Resource utilization | Low | Medium | High | Highest |
| Implementation complexity | Medium | High | Medium | Lowest |
| Runtime overhead | Low | Medium | Medium | None |
| Deadlock possibility | Never | Never | Possible | Possible |

## Livelock

A situation where processes continuously change their state in response to other processes without making progress.

**Difference from Deadlock:**
- Deadlock: Processes are blocked, waiting
- Livelock: Processes are active but not making progress

## Starvation

A situation where a process waits indefinitely because it never gets required resources.

**Difference from Deadlock:**
- Deadlock: Set of processes mutually waiting
- Starvation: Single process waiting indefinitely

## Real-World Examples

1. **Traffic Deadlock**: Four cars at intersection, each waiting for other to move
2. **Dining Philosophers**: Philosophers need two forks to eat, deadlock possible
3. **Database**: Two transactions waiting for locks held by each other

## Exam Tips

1. **Memorize four necessary conditions** (Coffman conditions)
2. **Understand RAG**: Draw and interpret resource allocation graphs
3. **Know all four methods**: Prevention, avoidance, detection, ignore
4. **Banker's Algorithm**: Understand the concept and steps
5. **Prevention strategies**: How to negate each of the four conditions
6. **Compare methods**: Advantages and disadvantages of each
7. **Practice examples**: Draw scenarios and identify deadlocks
8. **Understand recovery**: Process termination vs resource preemption
9. **Differentiate**: Deadlock vs Livelock vs Starvation
10. **Real-world examples**: Relate concepts to practical scenarios
EOF

echo "✓ Fixed module-4/deadlocks"

echo ""
echo "================================================================================"
echo "SUMMARY: Fixed all remaining wrong subject topics"
echo "================================================================================"
echo ""
echo "BCS654A - Data Structures: 5 topics fixed"
echo "  - module-2/introduction"
echo "  - module-3/introduction"
echo "  - module-3/operations"
echo "  - module-4/introduction"
echo "  - module-5/introduction"
echo ""
echo "BCS654B - Operating Systems: 2 topics fixed"
echo "  - module-2/process-management"
echo "  - module-4/deadlocks"
echo ""
echo "Total: 7 topics fixed"
echo "================================================================================"

