# LINKED LISTS

## Introduction

Linked lists represent one of the most fundamental and versatile data structures in computer science, forming the backbone of dynamic memory management and complex data organization. Unlike static arrays that require contiguous memory allocation, linked lists provide a dynamic approach to storing data elements where each element (called a node) contains both the actual data and a reference (or pointer) to the next element in the sequence. This fundamental distinction gives linked lists their distinctive advantage: the ability to grow and shrink dynamically during program execution without requiring expensive memory reallocation operations.

In the context of the University of Delhi's Computer Science curriculum, linked lists serve as a critical building block for understanding more complex data structures like stacks, queues, trees, and graphs. The concept of "chains" - which refers to linked sequences of nodes - is particularly important as it introduces students to the principle of pointer-based data structures. This knowledge becomes essential when studying polynomial representation, sparse matrix operations, and memory management techniques in subsequent courses. Given that approximately 75% of the end-semester examination weightage focuses on conceptual understanding and problem-solving, a thorough grasp of linked list operations, their time complexities, and practical applications is indispensable for achieving academic success.

## Key Concepts

### Node Structure and Memory Allocation

A linked list consists of nodes, where each node contains two components: the data field (which stores the actual information) and the link field (which stores the memory address of the next node). In C programming, this structure is typically defined using structures or self-referential structures. The last node in the list contains a NULL pointer in its link field, indicating the end of the list. Memory allocation for nodes is performed dynamically using functions like malloc() in C, allowing the list to grow and shrink as needed during program execution.

```c
struct Node {
    int data;
    struct Node* next;
};
```

The significance of dynamic memory allocation cannot be overstated. When we create a node using malloc(), the system allocates memory from the heap (rather than the stack), and this memory persists until it is explicitly freed using free(). This contrasts sharply with static arrays where memory must be declared at compile time. For DU students, understanding this distinction is crucial because questions frequently test the difference between stack and heap memory, and the implications for variable lifetime and memory efficiency.

### Types of Linked Lists

SINGLE LINKED LISTS represent the most basic form where each node contains a single pointer to the next node. Traversal is possible only in one direction - from the head (first node) to the tail (last node). This simplicity makes singly linked lists ideal for implementing stacks and for scenarios where only forward traversal is required.

DOUBLY LINKED LISTS enhance the basic structure by adding a previous pointer to each node, enabling traversal in both forward and backward directions. Each node now contains three fields: a previous pointer, the data, and a next pointer. While this requires more memory per node (approximately 50% more storage), it significantly simplifies operations like deletion (since we can easily access the previous node) and makes certain algorithms more efficient.

CIRCULAR LINKED LISTS modify the basic structure by connecting the last node back to the first node, creating a circular topology. In circular singly linked lists, the last node's next pointer points to the head of the list. Circular linked lists are particularly useful in round-robin scheduling, gaming applications (where turn-taking follows a circular pattern), and in implementing circular buffers.

### Operations on Singly Linked Lists

INSERTION OPERATIONS form the backbone of linked list manipulation. There are four primary insertion scenarios: at the beginning (head), at the end (tail), at a specific position, and after a given node. Insertion at the beginning requires updating the head pointer to point to the new node while setting the new node's next pointer to the previous head. This operation has O(1) time complexity, making it highly efficient. Insertion at the end requires traversing the entire list to find the last node (O(n) complexity), unless we maintain a tail pointer. Insertion at a specific position requires both traversal to find the position and careful pointer manipulation to maintain list integrity.

DELETION OPERATIONS similarly require careful pointer management. When deleting the first node, we simply move the head pointer to the second node and free the memory of the deleted node. Deletion from the end or from a specific position requires finding the previous node and updating its next pointer to skip over the node being deleted. A critical point to remember is that failing to free the memory of deleted nodes results in memory leaks - a serious programming error that can cause programs to consume increasing amounts of memory over time.

TRAVERSAL involves visiting each node in the list exactly once, typically to display the data, search for a specific value, or perform some operation on each element. The standard pattern uses a while loop that continues until the current pointer becomes NULL:

```c
struct Node* current = head;
while (current != NULL) {
    printf("%d ", current->data);
    current = current->next;
}
```

This traversal pattern has O(n) time complexity, where n is the number of nodes in the list.

SEARCHING in a linked list follows the same traversal pattern but includes a comparison at each node:

```c
struct Node* search(struct Node* head, int key) {
    struct Node* current = head;
    while (current != NULL) {
        if (current->data == key) {
            return current;
        }
        current = current->next;
    }
    return NULL;
}
```

The time complexity for searching is O(n) in the worst case, as we may need to examine every node. This is less efficient than array search (which can use binary search for O(log n) on sorted data), but the tradeoff is compensated by the dynamic size advantages of linked lists.

### Linked Stacks and Queues

Linked lists provide an elegant implementation for stack and queue data structures. A LINKED STACK uses a singly linked list where insertions and deletions occur only at the head (top) of the list. The push operation corresponds to inserting at the head, while pop corresponds to deleting from the head. This implementation eliminates the fixed-size limitation of array-based stacks and allows the stack to grow and shrink dynamically without overflow (until system memory is exhausted).

Similarly, a LINKED QUEUE can be implemented using a singly linked list with two pointers: front (for deletion/Dequeue) and rear (for insertion/Enqueue). The key consideration here is that we need both pointers because elements are added at one end and removed from the other. Without maintaining the rear pointer, enqueue operations would require O(n) traversal time.

### Polynomial Representation Using Linked Lists

One of the classic applications of linked lists in the DU syllabus is polynomial representation. A polynomial like 5x³ + 3x² + 2x + 7 can be represented as a linked list where each node stores the coefficient and exponent of a term. The terms are typically stored in descending order of exponents, which simplifies operations like polynomial addition. During addition, we traverse both polynomial lists simultaneously, comparing exponents and adding coefficients of matching terms. This application demonstrates the practical utility of linked lists in representing sparse polynomials efficiently (as opposed to using arrays where most coefficients would be zero).

## Examples

### Example 1: Insertion at the End of a Singly Linked List

PROBLEM: Write a C function to insert a new node with data value 25 at the end of a singly linked list.

SOLUTION:

```c
struct Node* insertAtEnd(struct Node* head, int data) {
    // Create new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    
    // If list is empty, new node becomes head
    if (head == NULL) {
        return newNode;
    }
    
    // Traverse to the last node
    struct Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    // Link the last node to new node
    current->next = newNode;
    return head;
}
```

STEP-BY-STEP EXPLANATION: First, we dynamically allocate memory for the new node and initialize its data and next fields. Since we're inserting at the end, the new node's next pointer must be NULL. If the list is empty (head is NULL), we simply return the new node as the head. Otherwise, we traverse the list starting from head until we find the last node (where next is NULL). Finally, we update the last node's next pointer to point to our new node. The time complexity is O(n) where n is the number of nodes.

### Example 2: Deletion of a Node with Specific Value

PROBLEM: Write a C function to delete the first occurrence of a node containing value key from a singly linked list.

SOLUTION:

```c
struct Node* deleteNode(struct Node* head, int key) {
    // Case 1: List is empty
    if (head == NULL) {
        return NULL;
    }
    
    // Case 2: Head node contains the key
    if (head->data == key) {
        struct Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    
    // Case 3: Search for the node to delete
    struct Node* current = head;
    while (current->next != NULL && current->next->data != key) {
        current = current->next;
    }
    
    // If key not found
    if (current->next == NULL) {
        printf("Key not found in the list\n");
        return head;
    }
    
    // Delete the node
    struct Node* temp = current->next;
    current->next = temp->next;
    free(temp);
    return head;
}
```

CRITICAL POINTS: This function handles three distinct cases. First, if the list is empty, we return NULL. Second, if the head itself contains the key, we save the head in a temporary pointer, advance head to the next node, and free the old head. Third, we search for the node containing the key by maintaining a pointer to the current node and checking its next node's data. When found, we bypass the node by updating the current node's next pointer to skip over the node being deleted, then free the deleted node's memory. This prevents memory leaks.

### Example 3: Reversing a Singly Linked List

PROBLEM: Write a C function to reverse a singly linked list without using extra arrays.

SOLUTION:

```c
struct Node* reverseList(struct Node* head) {
    struct Node* prev = NULL;
    struct Node* current = head;
    struct Node* next = NULL;
    
    while (current != NULL) {
        next = current->next;  // Save next node
        current->next = prev;  // Reverse the link
        prev = current;        // Move prev forward
        current = next;        // Move current forward
    }
    return prev;  // prev is now the new head
}
```

STEP-BY-STEP TRACE: We use three pointers: prev (initially NULL), current (initially head), and next (to save the remaining list). In each iteration, we first save the next node, then reverse the current node's pointer to point to prev. Then we move both prev and current one step forward. This process continues until current becomes NULL, at which point prev points to the new head (the original last node). This algorithm has O(n) time complexity and O(1) space complexity, making it highly efficient.

## Exam Tips

1. UNDERSTAND POINTER MANIPULATION: Most exam questions on linked lists test your understanding of pointer operations. Always draw diagrams when solving problems - visual representation helps identify edge cases and verify pointer updates.

2. MEMORY MANAGEMENT IS CRITICAL: In C programming questions, always remember to use malloc() for node creation and free() for node deletion. Failing to free memory leads to memory leaks, and using freed memory causes undefined behavior - both are serious errors that examiners look for.

3. TIME COMPLEXITY MEMORIZATION: Insertion at head is O(1), insertion at tail is O(n), deletion at head is O(1), deletion at tail is O(n), and search is O(n). Understand WHY each operation has its complexity rather than memorizing blindly.

4. HANDLING EDGE CASES: Always consider these boundary conditions: empty list, single node list, insertion/deletion at first position, and insertion/deletion at last position. Many exam marks are earned by explicitly handling these cases in your code.

5. DIFFERENTIATE BETWEEN STACK AND QUEUE IMPLEMENTATIONS: Remember that linked stack operations occur only at the head (O(1)), while linked queue requires both front and rear pointers with enqueue at rear (O(1) if rear maintained) and dequeue at front (O(1)).

6. POLYNOMIAL ADDITION ALGORITHM: Be prepared to write or trace through polynomial addition using linked lists. The key is to traverse both polynomials simultaneously, comparing exponents and handling cases where exponents match, don't match, or one list is exhausted.

7. CHOOSE THE RIGHT DATA STRUCTURE: Understand when to use arrays versus linked lists. Arrays provide O(1) random access but require O(n) for insertion/deletion at arbitrary positions. Linked lists provide O(1) insertion/deletion at known positions but require O(n) for search. This tradeoff is a frequent exam question.

8. PRACTICE C CODE TRACING: Many DU exam questions present C code with linked list operations and ask you to determine the output or identify errors. Practice tracing through code with sample inputs to build proficiency.