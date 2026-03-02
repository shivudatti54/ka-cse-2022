# Linked Lists

## Introduction

Linked lists represent one of the most fundamental and versatile data structures in computer science, serving as the building block for more complex data structures like stacks, queues, and trees. Unlike arrays, linked lists provide dynamic memory allocation, allowing us to allocate memory as needed during program execution rather than at compile time. This characteristic makes linked lists particularly valuable when the size of data is unknown beforehand or when frequent insertions and deletions are required.

In the context of the University of Delhi's Computer Science curriculum, linked lists form an essential topic that bridges theoretical understanding with practical implementation. The concept of linked allocation, where each element points to its successor, introduces students to the fundamental principle of dynamic data structures. This topic appears frequently in university examinations, with typically one full question (8-10 marks) dedicated to linked list operations, and concepts like traversal, insertion, and deletion appearing in various problem-solving contexts.

The importance of linked lists extends beyond academic requirements. They are extensively used in operating systems for memory management, in file systems for directory structures, and in implementing graphs through adjacency lists. Understanding linked lists deeply prepares students for advanced data structures and algorithms courses, making it a critical skill for any aspiring software developer.

## Key Concepts

### Definition and Structure

A linked list is a linear data structure where elements are stored in nodes, and each node contains two components: the data and a pointer (or reference) to the next node in the sequence. This pointer-based connection eliminates the need for contiguous memory allocation, solving many limitations of static arrays.

The basic node structure in C can be defined as:

```c
struct Node {
    int data;
    struct Node* next;
};
```

The first node is called the head, and the last node's pointer is set to NULL to indicate the end of the list. This NULL pointer serves as a sentinel value that helps in detecting the end of the list during traversal.

### Types of Linked Lists

**Singly Linked List:** Each node contains data and a pointer to the next node. Navigation is possible only in one direction—from head to tail. This is the simplest form of linked list and serves as the foundation for understanding more complex variants.

**Doubly Linked List:** Each node contains three components: a pointer to the previous node, the data, and a pointer to the next node. This bidirectional navigation allows traversal in both directions but requires additional memory for storing the previous pointer.

**Circular Linked List:** In this variant, the last node points back to the first node (head), forming a circle. Circular linked lists can be either singly or doubly linked and are particularly useful in applications requiring cyclic processing, such as round-robin scheduling.

### Memory Allocation

Linked lists utilize dynamic memory allocation using functions like malloc() in C or new operator in C++. Each node is allocated individually from the heap, allowing the list to grow and shrink as needed. This is fundamentally different from arrays, where memory is allocated contiguously at declaration time.

When creating a new node, memory is allocated using:

```c
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
```

Proper memory management is crucial—each malloc() should have a corresponding free() to prevent memory leaks. In C++, smart pointers can be used to automate memory management.

### Basic Operations

**Traversal:** Visiting each node exactly once to process its data. Starting from the head, we follow the next pointers until we reach NULL. The time complexity is O(n) where n is the number of nodes.

**Insertion:** Can be performed at three positions:
- At the beginning: O(1) time complexity
- At the end: O(n) time complexity (unless tail pointer is maintained)
- At a specific position: O(n) time complexity

**Deletion:** Can remove a node from:
- The beginning: O(1) time complexity
- The end: O(n) time complexity
- A specific position: O(n) time complexity

**Search:** Linear search requiring O(n) time in the worst case, similar to unsorted arrays.

### Comparison with Arrays

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory Allocation | Static/Contiguous | Dynamic/Scattered |
| Access Time | O(1) for random access | O(n) for sequential access |
| Insertion/Deletion | O(n) | O(1) at beginning, O(n) otherwise |
| Memory Efficiency | Fixed size, may waste space | Variable size, overhead for pointers |
| Cache Performance | Better (contiguous) | Poor (scattered) |

## Examples

### Example 1: Insertion at Beginning

Given a linked list with nodes containing values 10->20->30 and a new node with value 5, insertion at the beginning requires the following steps:

**Step 1:** Create a new node and assign the data
```c
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = 5;
```

**Step 2:** Make the new node point to the current head
```c
newNode->next = head;
```

**Step 3:** Update head to point to the new node
```c
head = newNode;
```

**Result:** The list becomes 5->10->20->30

This operation takes constant time O(1) because we only need to modify two pointers regardless of the list size. This makes linked lists ideal for implementing stacks.

### Example 2: Deletion at a Specific Position

Consider deleting the node at position 3 (0-indexed) from the list: 5->10->20->30->NULL

**Step 1:** Traverse to the node just before the position to delete
```c
struct Node* temp = head;
for (int i = 0; i < position - 1; i++) {
    temp = temp->next;
}
```

After the loop, temp points to the node containing 10.

**Step 2:** Store the node to be deleted
```c
struct Node* nodeToDelete = temp->next;  // Points to 20
```

**Step 3:** Update the pointer to skip the deleted node
```c
temp->next = nodeToDelete->next;  // Now points to 30
```

**Step 4:** Free the memory
```c
free(nodeToDelete);
```

**Result:** The list becomes 5->10->30->NULL

The time complexity is O(n) because we must traverse to the position, though the actual deletion and memory deallocation are O(1).

### Example 3: Reversing a Linked List

Reversing a linked list is a classic problem that tests understanding of pointer manipulation. Given 1->2->3->4->5, we need to produce 5->4->3->2->1.

**Algorithm:**
1. Initialize three pointers: prev = NULL, current = head, next = NULL
2. Iterate through the list
3. In each iteration:
   - Save next node: next = current->next
   - Reverse the pointer: current->next = prev
   - Move prev and current forward: prev = current, current = next
4. When loop ends, prev points to the new head

```c
struct Node* reverse(struct Node* head) {
    struct Node* prev = NULL;
    struct Node* current = head;
    struct Node* next = NULL;
    
    while (current != NULL) {
        next = current->next;  // Save next
        current->next = prev;  // Reverse link
        prev = current;        // Move prev forward
        current = next;        // Move current forward
    }
    // New return prev;  head
}
```

**Result:** The reversed list is 5->4->3->2->1

This operation requires O(n) time and O(1) auxiliary space, making it an efficient in-place reversal technique.

## Exam Tips

1. **Drawing diagrams is essential:** For linked list problems, always draw the initial list, show pointer modifications step-by-step, and verify the final state. Examiners award marks for correct pointer handling shown visually.

2. **Understand NULL handling:** Many students lose marks due to improper NULL pointer handling. Always check if head is NULL before operations, and ensure the last node points to NULL (or appropriate value for circular lists).

3. **Time complexity is frequently tested:** Memorize the time complexities for all operations—insertion at beginning is O(1), traversal is O(n), search is O(n), and deletion at end is O(n) without a tail pointer.

4. **Edge cases matter:** Always consider empty lists, single-node lists, and operations at boundaries (first and last positions). Write code that handles these gracefully.

5. **Distinguish between singly and doubly linked lists:** Understand when to use each type. Doubly linked lists allow reverse traversal but require additional memory and pointer updates for both next and previous.

6. **Practice dry running code:** Examiners often ask to predict output or find errors in given linked list code. Practice tracing through code with sample inputs to build this skill.

7. **Know the difference between malloc and free:** In C programs, remember to free allocated memory, and in questions about memory leaks, identify where free() statements are missing.