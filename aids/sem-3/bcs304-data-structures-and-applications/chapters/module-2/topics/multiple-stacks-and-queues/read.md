# Multiple Stacks and Queues

## Introduction

In Module 1, you learned about fundamental linear data structures: the stack and the queue. However, a single stack or queue in an application is often insufficient. Real-world systems like memory management in operating systems or job scheduling in a print spooler require managing *multiple* instances of these structures efficiently. This module explores the implementation and application of multiple stacks and queues, focusing on a memory-efficient technique for managing two stacks within a single array.

## Core Concepts

### The Need for Multiple Stacks and Queues

Imagine a scenario where an application requires two different types of FIFO (First-In-First-Out) processing. A single queue cannot handle this. Similarly, an algorithm might need to use two separate stacks for different temporary storage tasks. Implementing these as separate arrays is straightforward but can be inefficient in its memory usage. If we allocate fixed sizes for each, one stack might overflow while the other has plenty of free space, leading to wasted memory and premature failure.

### Implementing Two Stacks in a Single Array

A classic and efficient solution is to implement two stacks at opposite ends of a single array. This approach allows the stacks to grow and shrink dynamically towards each other, utilizing the entire available space.

*   **Initialization:** We create an array of size `n`. We initialize one stack (`stack1`) from the leftmost index (usually `0`) and the other stack (`stack2`) from the rightmost index (`n-1`).
*   **Stack1 Operations:**
    *   **Push:** The `top1` pointer starts at `-1`. To push an element, we increment `top1` and place the element at `arr[top1]`.
    *   **Pop:** We retrieve the element at `arr[top1]` and then decrement `top1`.
*   **Stack2 Operations:**
    *   **Push:** The `top2` pointer starts at `n`. To push an element, we decrement `top2` and place the element at `arr[top2]`.
    *   **Pop:** We retrieve the element at `arr[top2]` and then increment `top2`.
*   **Stack Overflow Condition:** The stacks share the same space. An overflow for the entire array occurs only when the two stack pointers meet, i.e., when `top1 + 1 == top2`. This means there is no free cell left between them to accommodate a new element for either stack.

**Example: Push Operations**
Let `n = 6`. The array is `arr[0..5]`.
1.  Push `10` to Stack1: `top1 = 0`, `arr[0] = 10`
2.  Push `20` to Stack2: `top2 = 5`, `arr[5] = 20`
3.  Push `30` to Stack1: `top1 = 1`, `arr[1] = 30`
4.  Push `40` to Stack2: `top2 = 4`, `arr[4] = 40`

The array now looks like this:
`Index: 0   1   2   3   4   5`
`Value: 10, 30, __, __, 40, 20`
`       ^top1=1   ^top2=4^`

### Multiple Queues

The concept of multiple queues is also common, especially in systems programming. For example, an operating system might maintain:
*   **Multiple Ready Queues:** Each with a different priority level for processes waiting to use the CPU.
*   **Multiple I/O Wait Queues:** Separate queues for different hardware devices (e.g., disk, printer, network).

Unlike the two-stacks-in-one-array technique, multiple queues are typically implemented as distinct, separate linked lists or arrays. This is because the flexible nature of a linked list avoids the fixed-size constraint problem from the outset. Each queue has its own `front` and `rear` pointers.

**Application Example: A Print Spooler**
A print server manages jobs from multiple users. It's inefficient to have a single queue, as a large job from one user could block dozens of small jobs from others. A better solution is to implement **multiple queues**, perhaps one per user or one per priority level. The scheduler can then allocate printer time in a round-robin or priority-based fashion between these queues.

## Key Points / Summary

| Key Point | Description |
| :--- | :--- |
| **Purpose** | To manage more than one stack or queue efficiently within an application, optimizing memory usage and organizing data with different processing rules. |
| **Two-Stacks-in-One-Array** | A memory-efficient technique where two stacks start at opposite ends of an array and grow towards the center. |
| **Overflow Condition** | Overflow occurs not when a stack reaches the end of the array, but when the two stack pointers are adjacent (`top1 + 1 == top2`). This maximizes space utilization. |
| **Multiple Queues** | Commonly implemented using separate linked lists for flexibility. Crucial for systems like OS schedulers that need to manage different categories of tasks (e.g., by priority or resource type). |
| **Real-World Applications** | Memory management (stacks), process scheduling (queues), print spoolers (queues), and evaluating complex expressions (stacks). |