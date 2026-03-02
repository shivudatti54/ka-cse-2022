# Implementation of Stacks and Queues Using Linked Lists

## Overview

Stacks and queues can be implemented using linked lists to overcome the fixed-size limitation of array-based implementations. Linked list implementations provide dynamic sizing, eliminating overflow concerns while maintaining O(1) operations.

## Key Points

- **Stack using Linked List**: Push and pop both at head for O(1) LIFO operations
- **Queue using Linked List**: Enqueue at tail, dequeue at head for O(1) FIFO operations
- **Dynamic Size**: No overflow condition, grows until system memory exhausted
- **Stack Push**: Insert at beginning, new node becomes head
- **Stack Pop**: Delete from beginning, update head to next node
- **Queue Enqueue**: Insert at end using tail pointer
- **Queue Dequeue**: Delete from beginning using head pointer

## Important Concepts

- Stack top corresponds to linked list head for efficient operations
- Queue requires both head (front) and tail (rear) pointers
- Push/pop use same linked list insert/delete at beginning
- Enqueue inserts at tail, dequeue removes from head
- No isFull check needed, only isEmpty check
- Memory allocated dynamically as needed, freed when elements removed
- Linked list implementation more flexible than array implementation

## Notes

- Practice implementing stack with head-only operations
- Practice implementing queue with head and tail pointers
- Understand advantage: no overflow, only system memory limit
- Know disadvantage: extra memory for pointers, not cache-friendly
- Be able to write complete code for both stack and queue
