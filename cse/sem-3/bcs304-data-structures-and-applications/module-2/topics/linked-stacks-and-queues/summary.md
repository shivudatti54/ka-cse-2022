# Linked Stacks and Queues

## Overview

Linked stacks and queues use dynamic memory allocation (malloc/free) to implement LIFO and FIFO principles. Unlike arrays, they grow/shrink at runtime with no fixed size limit. Stack operations occur at the head (O(1)); queue uses two pointers—front for deletion and rear for insertion (both O(1)).

## Key Points

- Stack: Add/remove at head for O(1) — `new->next = top; top = new;`
- Queue: Enqueue at rear, dequeue at front — maintains both `front` and `rear` pointers
- All core operations (push, pop, enqueue, dequeue, peek) are O(1)
- Display/traversal is O(n)
- Linked list uses heap memory; arrays use stack with fixed capacity

## Important Concepts

- **Self-referential Structure**: Node containing data and pointer to next node
- **Stack Underflow**: Attempting pop from empty stack — check `top == NULL`
- **Queue Underflow**: Attempting dequeue from empty queue — check `front == NULL`
- **Memory Leak**: Forgetting to `free()` node after pop/dequeue loses heap memory permanently
- **NULL Pointer**: End-of-list marker; new node's next must be set to NULL

## Notes

- Always check `malloc() == NULL` after allocation failure
- In queue dequeue: if `front` becomes NULL, set `rear = NULL` (queue becomes empty)
- Exam tip: Draw diagrams showing pointer updates — examiners reward visual representation
- Common mistake: Updating only one pointer in queue operations (forget rear when front becomes NULL)
- Stack structure: `struct StackNode { int data; struct StackNode* next; }`
- Queue structure: Separate `front` and `rear` pointers; enqueue at rear, dequeue from front
