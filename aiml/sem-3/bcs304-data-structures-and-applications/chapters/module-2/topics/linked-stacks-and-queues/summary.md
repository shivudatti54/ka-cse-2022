# Linked Stacks and Queues - Summary

## Key Definitions and Concepts

- LINKED STACK: Stack implementation using singly linked list where all operations (push/pop) occur at the top; requires only a top pointer pointing to the first node.
- LINKED QUEUE: Queue implementation using singly linked list where enqueue occurs at rear and dequeue occurs at front; requires both front and rear pointers.
- NODE: Basic unit of linked structure containing a data field and a link field (pointer to next node).
- DYNAMIC MEMORY ALLOCATION: Memory allocated at runtime using malloc() and deallocated using free() to prevent memory leaks.
- LIFO: Last-In-First-Out access pattern used by stacks.
- FIFO: First-In-First-Out access pattern used by queues.

## Important Formulas and Theorems

- Stack push: top = newNode; newNode->link = oldTop
- Stack pop: temp = top; top = top->link; free(temp)
- Queue enqueue: rear->link = newNode; rear = newNode
- Queue dequeue: temp = front; front = front->link; free(temp)
- Time complexity: O(1) for all fundamental operations (push, pop, enqueue, dequeue)
- Space complexity: O(n) where n is number of elements (overhead of pointer per node)

## Key Points

- Linked implementations provide dynamic size capability unlike fixed-size array implementations.
- Stack operations require only a top pointer; queue operations require both front and rear pointers.
- Proper memory management through malloc() and free() is essential to prevent memory leaks.
- Boundary condition handling is critical when queue transitions between empty and non-empty states.
- Linked implementations have O(1) constant time complexity for all basic operations.
- Each node has overhead of pointer storage compared to array elements.
- Stack applications include expression evaluation, function call management, and balanced parentheses checking.
- Queue applications include breadth-first search, CPU scheduling, and IO buffer management.
- Linked queues avoid the "creeping forward" problem that plagues array-based circular queues.
- NULL pointer indicates empty stack or queue in linked implementations.

## Common Mistakes to Avoid

- Forgetting to set rear->link = NULL when enqueuing in linked queue implementation.
- Not checking if queue is empty before dequeue operation, leading to NULL pointer dereference.
- Failing to free memory of removed nodes, causing memory leaks that accumulate over time.
- Using dot operator (.) instead of arrow operator (->) when accessing members through pointers.
- Not handling the case when dequeuing the last element (both front and rear should become NULL).
- Forgetting to check if malloc() returns NULL (allocation failure).

## Revision Tips

- Practice drawing node diagrams for stack and queue operations to visualize pointer changes.
- Memorize the four key operations for each data structure and their pointer manipulations.
- Compare linked vs array implementations by creating a comparison table covering size, memory, complexity, and access patterns.
- Solve at least three problems involving tracing operations through linked stacks and queues.
- Review C programming fundamentals: structures, pointers, malloc/free, and dynamic memory management.