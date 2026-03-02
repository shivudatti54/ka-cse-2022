# Multiple Stacks and Queues

## 1. Introduction

In our previous study of stacks and queues, we implemented them using a single array. However, real-world applications often require managing not just one, but several stacks or queues simultaneously. For instance, an operating system might manage multiple process queues (ready, waiting, running), or an application might need several stacks for different purposes. Allocating a fixed-size array for each stack can be highly inefficient, as it's difficult to predict the maximum size each one will need. This leads to either memory wastage (if allocated too much) or stack overflow (if allocated too little). The concept of **Multiple Stacks and Queues** addresses this problem by allowing multiple stacks or queues to coexist efficiently within a single, shared memory array.

## 2. Core Concepts

### Multiple Stacks in a Single Array

The most common approach is to implement two stacks at opposite ends of a single array. These stacks grow towards each other, effectively doubling the available memory utilization before an overflow occurs.

*   **Implementation:**
    *   Declare a single array `arr[MAX]`.
    *   Initialize Stack 1 from the left end. Its `top1` starts at `-1`.
    *   Initialize Stack 2 from the right end. Its `top2` starts at `MAX`.
    *   **Stack 1 Push:** `arr[++top1] = item;` (Check that `top1 < top2 - 1`)
    *   **Stack 2 Push:** `arr[--top2] = item;` (Check that `top2 > top1 + 1`)
    *   **Stack 1 Pop:** `item = arr[top1--];`
    *   **Stack 2 Pop:** `item = arr[top2++];`

*   **Stack Overflow Condition:** The array is full when `top1` and `top2` are adjacent, i.e., `top1 == top2 - 1`. This is a more efficient use of space than having two separate fixed arrays.

### Multiple Queues in a Single Array

Implementing more than two queues in a single array is more complex and is typically done using a **circular array** approach combined with linked list concepts. A common method is to use a single array for data and auxiliary arrays to store the front and rear pointers for each queue.

*   **Implementation (K Queues):**
    1.  Create three arrays:
        *   `arr[MAX]`: The main data array.
        *   `front[K]`: An array to store the front index for each of the `K` queues. Initialize all to `-1`.
        *   `rear[K]`: An array to store the rear index for each of the `K` queues. Initialize all to `-1`.
    2.  Create another array `next[MAX]` which serves two purposes:
        *   It stores the next free slot index (like a linked list of free nodes).
        *   For a used slot, it can store the next element's index in the same queue.
    3.  Maintain a `free` integer pointer that points to the next available free slot in `arr[]`.

*   **Enqueue Operation (for i-th queue):**
    1.  Check if `free == -1` (overflow).
    2.  Find an index `idx = free`.
    3.  Update `free = next[idx]`.
    4.  If the queue is empty (`front[i] == -1`), set both `front[i]` and `rear[i]` to `idx`.
    5.  Else, update `next[rear[i]] = idx` and set `rear[i] = idx`.
    6.  Set `next[idx] = -1` (signifying end of the queue) and store the data in `arr[idx]`.

*   **Dequeue Operation (for i-th queue):**
    1.  Check if `front[i] == -1` (underflow).
    2.  Find `idx = front[i]`.
    3.  Update `front[i] = next[idx]`.
    4.  Set `next[idx] = free` and `free = idx` (return the slot to the free list).
    5.  Return `arr[idx]`.

This approach efficiently manages the free space and allows all `K` queues to dynamically share the entire array.

## 3. Example: Two Stacks

Let's implement two stacks in an array of size 5 (`MAX=5`).

**Initialization:**
*   `arr[5] = { }`
*   `top1 = -1`
*   `top2 = 5`

**Operation Sequence:**
1.  Push(10, Stack1): `top1=0`, `arr[0]=10`
2.  Push(20, Stack2): `top2=4`, `arr[4]=20`
3.  Push(30, Stack1): `top1=1`, `arr[1]=30`
4.  Push(40, Stack2): `top2=3`, `arr[3]=40`
5.  Push(50, Stack1): `top1=2`, `arr[2]=50`

The array now is: `[10, 30, 50, 40, 20]`
Now, `top1=2` and `top2=3`. Since `top1 == top2 - 1` (2 == 3-1), the array is full. The next push operation to either stack would cause an overflow.

## 4. Key Points & Summary

| Key Point | Description |
| :--- | :--- |
| **Problem Solved** | Efficient memory management for multiple stacks/queues without pre-allocating fixed, individual sizes. |
| **Core Idea** | Share a single large array among all stacks or queues. |
| **Two-Stack Method** | Stacks start at opposite ends and grow towards each other. Simple and highly efficient. |
| **K-Queue Method** | More complex. Uses a main data array, `front[]`, `rear[]` arrays, and a `next[]` array to manage both the queues and a linked list of free slots. |
| **Overflow Check** | For two stacks: Check if `top1 == top2 - 1`. For K queues: Check if the `free` pointer is `-1`. |
| **Applications** | Memory management, process scheduling in OS, graph algorithms (e.g., managing multiple adjacency lists), and any system requiring efficient dynamic allocation of multiple linear data structures. |
| **Advantage** | Dramatically reduces memory wastage and provides flexibility as the stacks/queues can grow and shrink dynamically within the shared space. |