# Linked Stacks and Queues

## Introduction

Data structures form the backbone of efficient algorithm design, and among the most fundamental linear data structures are stacks and queues. While array-based implementations provide straightforward approaches, they suffer from inherent limitations such as fixed size constraints and inefficient memory utilization. Linked implementations using dynamic memory allocation offer elegant solutions to these problems, providing flexibility, efficient memory usage, and unbounded growth potential.

Linked stacks and queues represent the application of linked list principles to these classic data structures. In a linked implementation, elements are stored in nodes that contain both data and pointers to subsequent nodes, enabling dynamic memory allocation where memory is allocated only when needed. This approach eliminates the capacity restrictions of array-based implementations and provides O(1) time complexity for all fundamental operations. For students preparing for DU semester examinations, understanding the implementation details, algorithmic complexity, and practical applications of linked stacks and queues is essential for scoring well in both internal assessments and end semester examinations.

This topic builds upon the foundational concepts of linked lists while introducing the specialized constraints that stack (LIFO) and queue (FIFO) access patterns impose on linked implementations. The knowledge gained here directly applies to problem-solving in algorithm design, expression evaluation, breadth-first search traversals, and numerous real-world applications.

## Key Concepts

### Linked Stack Implementation

A linked stack implements the stack abstract data type using a singly linked list where insertions and deletions occur at one end, traditionally called the top. The linked representation consists of nodes, each containing a data field and a pointer field linking to the next node. The top pointer maintains reference to the first node in the chain, enabling O(1) access to the most recently inserted element.

The node structure for a linked stack typically includes two components: an element field to store the data and a link field containing the memory address of the next node. When implementing in C, this translates to a structure with a data element and a pointer to the same structure type, creating a self-referential data structure. The stack itself requires only a pointer to the top node, with NULL indicating an empty stack.

The push operation in a linked stack involves creating a new node, populating its data field with the new element, setting its link field to point to the current top node, and updating the top pointer to reference the new node. This operation requires only constant time regardless of stack size because it performs a fixed number of pointer manipulations. The pop operation reverses this process by saving the data from the top node, moving the top pointer to the next node, freeing the memory of the old top node, and returning the saved data. Memory allocation for new nodes typically uses dynamic memory allocation functions like malloc in C.

### Linked Queue Implementation

A linked queue implements the queue abstract data type using a singly linked list where insertion occurs at the rear and deletion occurs at the front. This design maintains the FIFO (First-In-First-Out) property essential to queue behavior. Unlike array-based queues that require circular logic to efficiently use available space, linked implementations naturally handle both ends without special considerations.

The linked queue structure requires two pointers: a front pointer referencing the first node (where deletions occur) and a rear pointer referencing the last node (where insertions occur). When the queue is empty, both pointers are NULL. As elements are enqueued, new nodes are linked to the rear of the chain, and the rear pointer is updated. During dequeue, the front node is removed, and the front pointer advances to the next node.

The critical aspect of linked queue implementation is maintaining both pointers correctly, especially when transitioning from empty to non-empty queue and vice versa. When the first element is enqueued, both front and rear pointers must be set to point to the newly created node. When the last element is dequeued, both pointers must be reset to NULL to indicate an empty queue. Failure to handle these boundary conditions correctly leads to pointer errors and memory leaks.

### Dynamic Memory Management

The primary advantage of linked implementations lies in dynamic memory allocation. Unlike arrays where memory must be reserved in advance, linked structures allocate memory for each element individually as needed. This approach provides several benefits: no memory is wasted on pre-allocated unused space, the data structure can grow arbitrarily large (bounded only by available system memory), and memory is returned to the system when elements are removed.

However, this dynamic approach introduces new considerations for programmers. Memory must be explicitly allocated using functions like malloc (or new in C++) and deallocated using free (or delete) to prevent memory leaks. In languages without automatic garbage collection, failing to deallocate removed nodes results in memory that remains allocated but inaccessible, gradually exhausting available memory. Additionally, linked implementations have higher overhead per element due to the pointer storage requirement, and they lack the cache-friendly contiguous memory layout of arrays.

### Time and Space Complexity Analysis

Understanding the computational complexity of linked stack and queue operations is crucial for algorithm selection and analysis. For linked stacks, push, pop, top, and isEmpty operations all execute in O(1) constant time because each operation involves only a fixed number of pointer manipulations regardless of the number of elements stored. This makes linked stacks highly efficient for scenarios requiring rapid insertions and deletions.

Linked queues similarly achieve O(1) time complexity for enqueue, dequeue, front, rear, and isEmpty operations when properly implemented. The key requirement is maintaining both front and rear pointers; implementations that only track the front pointer would require O(n) traversal for enqueue operations, defeating the purpose of queue efficiency.

The space complexity for both structures is O(n) where n represents the number of elements, with a constant overhead factor due to pointer storage. Each node requires memory for the data element plus the pointer field, meaning linked implementations use more memory than equivalent array implementations for the same data.

## Examples

### Example 1: Linked Stack Operations

Consider implementing a linked stack of integers and performing a sequence of operations to demonstrate the dynamic nature of linked implementation.

```
Initial state: top = NULL (empty stack)

Operation: push(25)
1. Create new node with data = 25
2. Set node->link = top (NULL)
3. Update top = node
Stack: top → [25|NULL]

Operation: push(50)
1. Create new node with data = 50
2. Set node->link = top (points to [25|NULL])
3. Update top = node
Stack: top → [50|→] [25|NULL]

Operation: push(75)
1. Create new node with data = 75
2. Set node->link = top (points to [50|→])
3. Update top = node
Stack: top → [75|→] [50|→] [25|NULL]

Operation: pop()
1. Save data from top node: data = 75
2. Set top = top->link (now points to [50|→])
3. Free memory of removed node
4. Return 75
Stack: top → [50|→] [25|NULL]
```

This example illustrates how linked stacks grow and shrink dynamically without requiring预先 allocation of fixed capacity. Each push allocates exactly the memory needed for one element, and each pop returns that memory to the system.

### Example 2: Linked Queue Operations

Consider a linked queue of strings and trace the behavior through various operations:

```
Initial state: front = NULL, rear = NULL (empty queue)

Operation: enqueue("Apple")
1. Create new node with data = "Apple"
2. Set node->link = NULL
3. Set front = node, rear = node
Queue: front → [Apple|NULL] ← rear

Operation: enqueue("Banana")
1. Create new node with data = "Banana"
2. Set rear->link = node (link Apple to Banana)
3. Set rear = node
Queue: front → [Apple|→] [Banana|NULL] ← rear

Operation: enqueue("Cherry")
1. Create new node with data = "Cherry"
2. Set rear->link = node
3. Set rear = node
Queue: front → [Apple|→] [Banana|→] [Cherry|NULL] ← rear

Operation: dequeue()
1. Save data from front node: data = "Apple"
2. Set front = front->link (now points to [Banana|→])
3. If front becomes NULL, set rear = NULL (but not here)
4. Free memory of old front node
5. Return "Apple"
Queue: front → [Banana|→] [Cherry|NULL] ← rear
```

This trace demonstrates proper pointer management in linked queues, particularly the relationship between front and rear pointers as elements are added and removed.

### Example 3: Application - Checking Balanced Parentheses

A practical application of linked stacks is checking whether parentheses, brackets, and braces are balanced in an expression. This problem appears frequently in compiler design and expression evaluation.

```
Expression: {(a + b) * [c - d]}

Algorithm using linked stack:
1. Scan each character left to right
2. For opening brackets: push onto stack
3. For closing brackets: pop from stack and check matching
4. At end: stack should be empty for balanced expression

Step-by-step:
'{' → push: Stack: { '(' → push: Stack: {( 
'[' → push: Stack: {( [ 
'a' → ignore
'+' → ignore
'b' → ignore
')' → pop matches '(': Stack: { [ 
'c' → ignore
'-' → ignore
'd' → ignore
']' → pop matches '[': Stack: { 
'}' → pop matches '{': Stack: empty

Result: Balanced ✓
```

This application showcases the LIFO property of stacks being essential for solving problems where matching requires remembering the order of opening symbols.

## Exam Tips

For DU semester examinations, several key points require special attention when studying linked stacks and queues.

First, MEMORY LEAKS represent a critical concern in linked implementations. When implementing pop or dequeue operations, always ensure that the removed node's memory is properly freed using the free() function in C. Examiners frequently test understanding of proper memory management, and failing to deallocate memory results in losing marks even if the algorithmic logic is correct.

Second, BOUNDARY CONDITION HANDLING separates correct implementations from flawed ones. Always handle the transitions between empty and non-empty states carefully: when pushing onto an empty stack, the top pointer changes from NULL to the new node; when popping the last element, the top pointer changes to NULL. In queues, ensure both front and rear pointers are properly initialized and reset during enqueue and dequeue operations.

Third, UNDERSTAND THE POINTER MECHANICS clearly. Many exam questions ask students to trace through operations or identify errors in given code. Practice drawing node diagrams and tracing pointer changes step-by-step, as this develops the spatial understanding necessary for debugging linked implementations.

Fourth, TIME COMPLEXITY analysis is frequently tested. Remember that all fundamental operations on properly implemented linked stacks and queues are O(1). However, be prepared to identify when a poorly designed implementation might degrade to O(n), such as a queue implementation that only maintains a front pointer.

Fifth, COMPARISON WITH ARRAY-BASED IMPLEMENTATIONS is a common examination theme. Understand the trade-offs: linked implementations offer dynamic size and O(1) worst-case operations, while array implementations offer O(1) random access and better cache performance but face capacity limitations.

Sixth, in C PROGRAMMING QUESTIONS, ensure correct use of structure pointers, malloc and free, and arrow operator (->) for accessing structure members through pointers. Common mistakes include using dot notation instead of arrow notation, forgetting to allocate memory before dereferencing, and not checking for NULL after malloc.

Seventh, APPLICATIONS of linked stacks and queues are important. Understand how stacks enable expression evaluation, function call management, and backtracking algorithms, while queues enable breadth-first search, scheduling algorithms, and buffering in IO systems.