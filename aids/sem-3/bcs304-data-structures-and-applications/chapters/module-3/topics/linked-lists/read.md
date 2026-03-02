# Linked Lists

## Introduction

Linked lists represent one of the most fundamental and versatile data structures in computer science, forming the backbone of dynamic data management in countless applications. Unlike static arrays that require contiguous memory allocation and fixed size specification at declaration, linked lists provide a dynamic approach to storing collections of elements where the memory is allocated as needed during program execution. This fundamental difference makes linked lists indispensable in scenarios where the number of elements is unknown beforehand or changes frequently during program execution.

In the context of the University of Delhi's Computer Science curriculum, linked lists serve as a prerequisite understanding for more complex data structures such as stacks, queues, trees, and graphs. The concept of node allocation and pointer manipulation developed through linked lists directly applies to these advanced structures. Moreover, linked lists are extensively used in operating system memory management, file allocation systems, and implementatin of abstract data types like lists, stacks, and queues. Understanding linked lists thoroughly is essential for algorithmic problem-solving and efficiently managing memory in resource-constrained environments.

This chapter explores the fundamental characteristics of linked lists, their various types, implementation details, and the operations that can be performed on them. We examine both the theoretical aspects and practical implementation considerations, providing numerous examples to illustrate key concepts and prepare students for examination success.

## Key Concepts

### Definition and Structure

A linked list is a linear data structure where elements (called nodes) are stored in memory in a non-contiguous manner. Each node contains two components: the actual data (or payload) and a pointer (or reference) to the next node in the sequence. This pointer-based connection between nodes gives linked lists their name and distinguishes them from array-based storage.

The fundamental building block of a linked list is the NODE, typically implemented as a structure or class containing:

- **Data Field**: Stores the actual element value (can be primitive data types or complex objects)
- **Next Pointer**: Stores the memory address of the next node in the list

The first node is called the HEAD or START node, while the last node in the list points to NULL (or nullptr in C++) to indicate the end of the list. This NULL pointer serves as a sentinel value that marks the termination of the list.

### Types of Linked Lists

**Singly Linked List (SLL)**: The simplest form where each node contains a data field and a single pointer to the next node. Navigation is strictly forward—from the head to the tail. This structure requires minimal memory overhead but limits traversal to one direction only.

**Doubly Linked List (DLL)**: Each node contains three fields—data, a pointer to the next node, and a pointer to the previous node. This bidirectional navigation allows traversal in both forward and backward directions, facilitating operations like reverse traversal and easier deletion when given a pointer to the node to be deleted. However, this comes at the cost of extra memory for the previous pointer.

**Circular Linked List**: In this variant, the last node points back to the first node (head), forming a circle. Both singly and doubly linked lists can be circular. Circular linked lists eliminate the NULL termination condition and are particularly useful in round-robin scheduling, repeated iteration over data, and certain gaming applications where continuous cycling through elements is required.

### Memory Representation

In array-based storage, elements occupy contiguous memory locations, enabling constant-time random access through index calculation. However, this requires预先 knowing the size and leads to either wasted space (if over-allocated) or overflow (if more elements are needed).

Linked lists solve this through dynamic memory allocation. Each node is typically allocated from the heap using functions like malloc() in C or new in C++/Java. The nodes can be scattered throughout memory, connected only through pointers. This flexible allocation means:

- No memory wasted on potential future growth
- Lists can grow to the limits of available heap memory
- No need for initial size estimation
- Insertions and deletions do not require shifting elements

The trade-off is that linked lists do not support direct random access. To access the i-th element, we must traverse all i nodes from the beginning, resulting in O(i) time complexity.

### Basic Operations

**Traversal**: Visiting each node in the list exactly once to process or display its data. Starting from the head, we follow next pointers until we reach NULL. This operation takes O(n) time where n is the number of nodes.

**Insertion**: Adding a new node to the list. Depending on position, insertion can occur:
- At the beginning: Create new node, point it to current head, update head to new node—O(1) time
- At the end: Traverse to last node, create new node, set last node's next to new node—O(n) time
- At a specific position: Traverse to position-1, adjust pointers to insert new node—O(n) time

**Deletion**: Removing a node from the list. Similar to insertion, deletion can occur:
- At the beginning: Update head to point to second node, free memory of old head—O(1) time
- At the end: Traverse to second-last node, set its next to NULL, free memory of old tail—O(n) time
- At a specific position: Traverse to node before target, adjust pointers, free target node—O(n) time

**Search**: Finding whether a particular element exists in the list. Requires linear traversal in the worst case—O(n) time complexity.

### Implementation Considerations

When implementing linked lists in practical scenarios, several factors require careful attention:

**Memory Management**: In languages like C and C++, proper allocation and deallocation are critical. Forgetting to free memory leads to memory leaks, while accessing freed memory causes undefined behavior. In languages with garbage collection (Java, Python), this concern is mitigated but understanding the underlying mechanism remains important.

**Edge Cases**: Proper handling of edge cases ensures correctness:
- Empty list (head = NULL)
- Single-node list
- Insertion/deletion at head or tail
- Overflow conditions (when heap memory is exhausted)

**Pointer Handling**: Careful pointer manipulation is essential. A common error is dereferencing a NULL pointer or losing the reference to the next node before updating pointers, which results in orphaned sublists.

## Examples

### Example 1: Insertion at Beginning in Singly Linked List

Consider an existing linked list: 10 → 20 → 30 → NULL, where head points to node containing 10.

We want to insert a new node with value 5 at the beginning.

**Step-by-Step Procedure:**

1. **Create new node**: Allocate memory for a new node and store value 5:
   ```
   newNode = (Node*)malloc(sizeof(Node))
   newNode->data = 5
   ```

2. **Point new node to current head**: The next pointer of newNode should reference the first node (containing 10):
   ```
   newNode->next = head
   ```

   After this step: 5 → 10 → 20 → 30 → NULL

3. **Update head pointer**: Move head to point to the new node:
   ```
   head = newNode
   ```

   Final list: head → 5 → 10 → 20 → 30 → NULL

**Time Complexity**: O(1) constant time, regardless of list size. This makes linked lists superior to arrays for frequent insertions at the beginning.

### Example 2: Deletion of a Node from Singly Linked List

Given the list: head → 10 → 20 → 30 → 40 → NULL, delete the node containing 30.

**Step-by-Step Procedure:**

1. **Initialize pointers**: Set a pointer 'temp' to head and 'prev' to NULL:
   ```
   temp = head
   prev = NULL
   ```

2. **Traverse to find target node**: Move both pointers until temp points to the node with value 30:
   ```
   Iteration 1: temp = 10 (data ≠ 30), prev = NULL
                 prev = temp, temp = temp->next
   
   Iteration 2: temp = 20 (data ≠ 30), prev = node(10)
                 prev = temp, temp = temp->next
   
   Iteration 3: temp = 30 (found!), prev = node(20)
   ```

3. **Adjust pointers**: Skip the node to be deleted by connecting prev->next to temp->next:
   ```
   prev->next = temp->next
   ```

   After adjustment: 10 → 20 → 40 → NULL

4. **Free memory**: Release the deleted node:
   ```
   free(temp)
   ```

**Time Complexity**: O(n) in worst case (when deleting last element or element not found), as traversal to find the node is required.

### Example 3: Creating a Linked List from Array Elements

Given an array arr = {5, 15, 25, 35}, create a linked list and display all elements.

**Algorithm:**

```
1. Initialize head = NULL, tail = NULL
2. For each element x in array:
   a. Create new node with data = x
   b. If list is empty:
        head = newNode
        tail = newNode
   c. Else:
        tail->next = newNode
        tail = newNode
3. Set tail->next = NULL
```

**Execution Trace:**

- After element 5: head → 5 → NULL
- After element 15: head → 5 → 15 → NULL
- After element 25: head → 5 → 15 → 25 → NULL
- After element 35: head → 5 → 15 → 25 → 35 → NULL

**Display Function** (traversal and printing):
```
void display(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        printf("%d → ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
```

Output: 5 → 15 → 25 → 35 → NULL

## Exam Tips

1. **Understand pointer manipulation**: Most exam questions test your understanding of how pointers connect nodes. Always draw diagrams when solving problems involving insertions and deletions.

2. **Time complexity is crucial**: Remember that traversal, search, insertion at end end all, and deletion at require O(n) time, while insertion and deletion at the beginning are O(1). Arrays provide O(1) random access but O(n) insertions/deletions.

3. **NULL pointer handling**: Always check for NULL before accessing node->next in traversal. Forgetting this causes segmentation faults. The termination condition in while loops should be (temp != NULL).

4. **Distinguish between node and pointer names**: In implementations, clearly distinguish between the head pointer (external pointer to list) and the next pointers (internal links between nodes).

5. **Edge case scenarios**: Practice handling empty lists, single-node lists, and operations at boundaries (first and last positions). Many exam questions specifically test these conditions.

6. **Doubly vs Singly linked lists**: Remember that doubly linked lists require updating two pointers during insertion/deletion (previous and next), but provide O(1) deletion if given the node pointer directly.

7. **Space-time trade-off**: Linked lists use more memory than arrays (extra pointer per node) but provide better performance for dynamic size changes. This trade-off is a common examination topic.