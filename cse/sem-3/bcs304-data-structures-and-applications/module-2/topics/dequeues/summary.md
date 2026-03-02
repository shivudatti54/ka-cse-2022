# Deques (Double-Ended Queues)

## Overview

A deque (Double-Ended Queue) is a linear data structure allowing insertion and deletion at both front and rear ends. It generalizes both stack (LIFO) and queue (FIFO), making it highly flexible. Implementation is typically done using circular arrays or doubly linked lists.

## Key Points

- Four main operations: insertFront, insertRear, deleteFront, deleteRear — all O(1)
- Input-restricted deque: Insert only at rear; delete from both ends allowed
- Output-restricted deque: Insert at both ends; delete only from front
- Simulates stack: insertFront + deleteFront (or insertRear + deleteRear)
- Simulates queue: insertRear + deleteFront
- insertFront moves front backward first; deleteFront moves front forward
- Rear pointer always points to next free slot, not the last element

## Important Concepts

- Deque: Linear structure allowing operations at both front and rear ends
- Input-Restricted Deque: Insert only at rear, delete from both ends
- Output-Restricted Deque: Insert at both ends, delete only from front
- Circular Array: Array with wrap-around indices using modulo operator
- Overflow: Attempt to insert into a full deque
- Underflow: Attempt to delete from an empty deque

## Notes

- Exam Tip: Memorize the operation table for restricted deque types (5-mark question)
- Critical formula: getRear returns element at index (rear - 1 + MAX) % MAX
- Common mistake: insertFront decrements front BEFORE storing (not after)
- For O(1) deleteRear, use doubly linked list — singly linked list requires O(n)
- Applications to mention in long answers: palindrome checking, sliding window maximum (O(n)), undo/redo systems
