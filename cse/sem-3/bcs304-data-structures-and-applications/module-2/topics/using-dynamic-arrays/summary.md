# Using Dynamic Arrays for Queues

## Overview

A dynamic array-based queue is a linear data structure that follows the FIFO principle, automatically growing its capacity when needed. It combines the efficiency of array-based storage with the flexibility of unbounded capacity. This approach overcomes the limitations of fixed-size queues, including overflow and wasted space.

## Key Points

- Dynamic arrays are used to implement queues that can grow automatically when they run out of space.
- The queue is treated as a circular array, with the last element connected to the first element.
- A **doubling strategy** is used to resize the queue when it becomes full.
- The `size` field keeps track of the number of elements currently in the queue.
- The `capacity` field represents the current allocated capacity of the queue.
- Enqueue and dequeue operations are performed using circular indexing.
- The queue can be shrunk when the size drops below one-quarter of the capacity.

## Important Definitions

- **FIFO (First In, First Out)**: A principle where the first element added to the queue is the first one to be removed.
- **Doubling strategy**: A technique used to resize the queue by doubling its capacity when it becomes full.
- **Circular indexing**: A method used to treat the array as a circular structure, where the last element is connected to the first element.

## Key Formulas / Syntax

- **Next position**: `(index + 1) % capacity`
- **Queue size**: `(rear - front + capacity) % capacity`
- **Full condition**: `(rear + 1) % capacity == front`
- **Empty condition**: `front == rear`

## Comparisons

| Feature           | Fixed-Size Queue    | Dynamic Queue                      |
| ----------------- | ------------------- | ---------------------------------- |
| Maximum capacity  | Decided at creation | Grows as needed                    |
| Overflow possible | Yes                 | No (limited only by system memory) |
| Memory usage      | Fixed allocation    | Grows/shrinks with demand          |

## Exam Tips

- Always mention the **doubling strategy** when explaining how the queue is resized.
- Be ready to explain why enqueue is **amortized O(1)** despite occasional O(n) resizes.
- Remember the **circular indexing formula**: `(index + 1) % capacity`.
- Emphasize the difference between `size` and `capacity`.
- Be prepared to compare fixed-size and dynamic queues, highlighting the trade-offs between resize cost and overflow guarantee.
