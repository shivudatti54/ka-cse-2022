# Linked Lists

## Introduction

Linked Lists represent one of the most fundamental and versatile data structures in computer science, forming the backbone of dynamic memory management and linear data organization. Unlike static arrays that require contiguous memory allocation and fixed size declaration, linked lists provide a dynamic approach to storing elements where memory is allocated as needed during program execution. This fundamental distinction makes linked lists indispensable in scenarios where the number of elements is unknown beforehand or changes frequently during program execution.

The concept of linked lists becomes particularly significant in the context of the University of Delhi's Computer Science curriculum, where students must understand not only the theoretical underpinnings but also the practical implementation details that differentiate linked lists from other linear data structures. In modern computing applications, linked lists serve as the foundation for implementing complex data structures like stacks, queues, graphs (adjacency lists), and dynamic memory allocation systems. Understanding linked lists is essential for grasping more advanced topics such as trees, hash tables, and memory management algorithms that students will encounter in subsequent courses.

This chapter explores the various types of linked lists, their operations, implementation details, and practical applications. We will examine how linked lists overcome the limitations of static arrays and why they remain a critical topic in computer science education despite being among the oldest data structure concepts. The chapter provides comprehensive coverage suitable for preparing students for both internal assessments and end semester examinations.

## Key Concepts

### Self-Referential Structures

The foundation of linked lists lies in a special type of structure called a self-referential structure. In C programming, a self-referential structure contains a pointer member that points to a structure of the same type. This recursive definition enables structures to "refer to" or "contain" references to other structures of the identical type, creating the chain-like arrangement essential for linked lists.

Consider the fundamental structure definition for a node in a singly linked list:

```c
struct Node {
    int data;
    struct Node *next;
};
```

The structure contains two components: a data field to store the actual information (which can be of any data type including integers, floats, characters, or even complex structures), and a pointer field called 'next' that stores the memory address of the next node in the sequence. The 'next' pointer of the last node in the list is set to NULL, serving as a sentinel value that indicates the end of the list. This design allows each node to know only about its successor, making the list traversal unidirectional from the head to the tail.

Self-referential structures are not limited to singly linked lists; they form the basis for implementing binary trees, linked stacks, linked queues, and various other dynamic data structures. The key principle is that the structure must be complete before it can reference itself, which is why structures in C are typically defined before declaring pointers to them.

### Singly Linked List Operations

The operations on singly linked lists form the core practical knowledge that students must master. These operations include traversal, insertion, deletion, searching, and various utility functions like finding the length and displaying all elements.

**Traversal** is the fundamental operation of visiting each node in the list exactly once to process its data. Starting from the head pointer, we navigate through the list by following the 'next' pointers until we reach NULL. The time complexity of traversal is O(n) where n is the number of nodes, as we must potentially visit every node.

**Insertion** in a singly linked list can occur at three different positions: at the beginning, at the end, or at a specific position in the middle. Insertion at the beginning requires updating the head pointer to point to the new node while making the new node point to the previously first node. Insertion at the end requires traversing to the last node (or maintaining a tail pointer) and appending the new node after it. Middle insertions require locating the position and adjusting pointers of the preceding node to point to the new node and the new node to point to the subsequent node.

**Deletion** operations mirror insertion but in reverse order. Deleting the first node simply moves the head pointer to the second node. Deleting the last node requires traversing to find the second-last node and setting its 'next' pointer to NULL. Deleting a node from the middle requires adjusting the 'next' pointer of the predecessor to skip over the node being deleted.

### Circular Singly Linked List

A circular singly linked list represents a variation where the last node's 'next' pointer points back to the first node (the head) instead of NULL. This circular arrangement eliminates the NULL termination condition and creates a closed loop. The primary advantage of circular linked lists is that every node has a successor, making certain operations more efficient—particularly those that require traversing to the end and returning to the beginning.

 circular linked lists, the conceptIn of a "tail" pointer becomes particularly useful as it enables constant-time insertion at both ends. The implementation must carefully handle edge cases to avoid infinite loops during traversal, typically by maintaining a reference point and stopping when that reference is encountered again.

Circular linked lists find practical applications in operating system task scheduling (round-robin algorithms), browser history navigation (where you can cycle through pages), and multiplayer game turn management.

### Implementation of Stacks and Queues using Linked Lists

Linked lists provide an elegant solution for implementing stacks and queues dynamically. Unlike array-based implementations that require fixed capacity or complex resizing logic, linked list implementations naturally accommodate growing and shrinking data structures.

**Linked Stack Implementation**: A stack implemented using a linked list uses the head of the list as the top of the stack. Push operation involves creating a new node, setting its next pointer to the current top, and updating the top pointer. Pop operation removes the node at the top by moving the top pointer to the next node. Both operations execute in O(1) constant time, making linked stacks highly efficient.

**Linked Queue Implementation**: A queue requires insertion at one end (rear) and deletion from the other end (front). While a singly linked list can implement a queue, the efficiency depends on which end we maintain access to. Maintaining both head and tail pointers enables O(1) time for both enqueue and dequeue operations. The enqueue operation adds a new node after the tail, while dequeue removes the node at the head.

### Concatenating Two Lists

List concatenation refers to joining two separate linked lists where all nodes from the second list are attached after the last node of the first list. This operation is particularly useful in scenarios where we need to combine sorted lists or merge data from different sources.

The implementation requires locating the last node of the first list (traversing from head until next is NULL), then setting its 'next' pointer to point to the head of the second list. If the first list is maintained with a tail pointer, concatenation becomes an O(1) operation; otherwise, it requires O(n) time to find the last node.

### Reversing a List Without Creating New Nodes

Reversing a linked list in-place without allocating additional nodes is a classic problem that tests understanding of pointer manipulation. The algorithm uses three pointers: one pointing to the current node, one to its previous node, and one to its next node. By iterating through the list and reversing each pointer's direction, we transform the list in-place with O(n) time complexity and O(1) space complexity.

The algorithm proceeds by saving the next node before modifying the current node's pointer, then advancing all three pointers forward. After complete traversal, the previous pointer will be pointing to the new head (formerly the last node), which becomes the new head of the reversed list.

### Static Allocation versus Linked Allocation

Understanding the difference between static (array-based) and dynamic (linked) allocation is fundamental to choosing appropriate data structures for specific applications.

| Aspect | Static Allocation (Arrays) | Linked Allocation |
|--------|---------------------------|-------------------|
| Memory | Contiguous block | Scattered locations |
| Size | Fixed at declaration | Dynamic, grows/shrinks |
| Insertion/Deletion | O(n) potentially | O(1) at known positions |
| Access Time | O(1) random access | O(n) sequential only |
| Memory Waste | Possible unused space | No pre-allocation waste |
| Implementation | Simpler | More complex |

Static allocation offers advantages of simplicity, cache-friendly memory access due to contiguity, and O(1) random access to elements. Linked allocation provides flexibility, efficient insertions and deletions, and optimal memory utilization as nodes are created only when needed.

## Examples

### Example 1: Insertion in Singly Linked List at Specific Position

**Problem**: Create a function to insert a new node with value 25 after the node containing value 15 in a singly linked list.

**Step-by-Step Solution**:

Consider a list: 10 → 15 → 20 → 30 → NULL

Step 1: Create the new node with the value 25
```c
struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = 25;
newNode->next = NULL;
```

Step 2: Traverse to find the node after which insertion must occur (node with value 15)
```c
struct Node *temp = head;
while (temp != NULL && temp->data != 15) {
    temp = temp->next;
}
```

Step 3: After loop, temp points to node containing 15
- Current: temp->next points to node containing 20
- We need: newNode->next = temp->next (to connect to 20)
- Then: temp->next = newNode (to connect from 15 to 25)

Step 4: Final list becomes: 10 → 15 → 25 → 20 → 30 → NULL

**Explanation**: The key is to first establish the link from the new node to the succeeding node before breaking the link from the current node. Reversing this order would cause us to lose reference to the rest of the list.

### Example 2: Implementing Stack using Linked List

**Problem**: Implement push and pop operations for a stack using a linked list.

**Solution**:

```c
struct StackNode {
    int data;
    struct StackNode *next;
};

struct StackNode *top = NULL;

void push(int value) {
    struct StackNode *newNode = (struct StackNode*)malloc(sizeof(struct StackNode));
    newNode->data = value;
    newNode->next = top;  // Point new node to current top
    top = newNode;        // Update top to new node
}

int pop() {
    if (top == NULL) {
        printf("Stack Underflow\n");
        return -1;
    }
    struct StackNode *temp = top;
    int poppedValue = temp->data;
    top = top->next;      // Move top to next node
    free(temp);           // Free memory of popped node
    return poppedValue;
}
```

**Trace Example**: Push operations 10, 20, 30
- After push(10): top → [10|NULL]
- After push(20): top → [20]→[10|NULL]
- After push(30): top → [30]→[20]→[10|NULL]

Pop operation returns 30, then 20, then 10 (LIFO order maintained)

### Example 3: Reversing a Linked List In-Place

**Problem**: Reverse a linked list without creating new nodes.

**Solution**:

```c
struct Node* reverseList(struct Node *head) {
    struct Node *prev = NULL;
    struct Node *current = head;
    struct Node *next = NULL;
    
    while (current != NULL) {
        next = current->next;  // Save next node
        current->next = prev;   // Reverse the link
        prev = current;        // Move prev forward
        current = next;        // Move current forward
    }
    return prev;  // prev is now the new head
}
```

**Step-by-Step Trace** for list: 1 → 2 → 3 → NULL

Initial: prev=NULL, current=1, next=undefined

Iteration 1: next=2, 1→NULL, prev=1, current=2
Iteration 2: next=3, 2→1, prev=2, current=3
Iteration 3: next=NULL, 3→2, prev=3, current=NULL

Final: prev=3, list is now 3 → 2 → 1 → NULL

## Exam Tips

1. **Pointer Manipulation is Key**: In linked list operations, always save the next pointer before modifying the current node's next pointer to avoid losing the rest of the list.

2. **Edge Cases Matter**: Always consider and handle edge cases including empty list, single node list, insertion at beginning/end, and deletion of first/last node.

3. **Time Complexities**: Remember that array access is O(1) while linked list traversal is O(n); insertion/deletion at beginning is O(1) for linked lists but O(n) for arrays.

4. **Memory Allocation**: Always check if malloc returns NULL (memory allocation failure), especially in examination scenarios where memory constraints might be relevant.

5. **Drawing Helps**: Practice drawing node diagrams to visualize pointer changes during operations—this is crucial for understanding and debugging.

6. **Circular List Traversal**: When traversing circular lists, use a counter or compare pointers to the head to avoid infinite loops.

7. **Stack vs Queue Implementation**: Remember that linked stack uses only head pointer while linked queue needs both head and tail pointers for efficiency.

8. **In-place Reversal**: The three-pointer technique (previous, current, next) is the standard approach for reversing without allocation—practice this thoroughly.

9. **NULL Pointer Checks**: Always verify pointers are not NULL before dereferencing them to avoid segmentation faults.

10. **Free Memory**: When implementing delete operations, always free the memory of the deleted node to prevent memory leaks, though in exam scenarios this may be omitted for simplicity.