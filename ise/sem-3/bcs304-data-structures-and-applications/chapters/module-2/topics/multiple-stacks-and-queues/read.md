Of course. Here is a comprehensive educational module on Multiple Stacks and Queues, tailored for  engineering students.

# Module 2: Multiple Stacks and Queues

## 1. Introduction

In our previous modules, we implemented a single stack or a single queue using an array. A significant limitation of this approach is that the memory allocated to the structure is fixed and used only for that one structure. In real-world systems, we often need to manage multiple lists (stacks or queues) simultaneously. Allocating separate arrays for each is inefficient and can lead to memory wastage, as one stack might overflow while another has free space.

**Multiple stacks and queues** address this problem by utilizing a single large array to efficiently manage two or more stacks or queues. This approach allows for flexible memory usage, where the total memory is shared dynamically between the structures.

## 2. Core Concepts

### 2.1. Two Stacks in a Single Array

The simplest form of multiple stacks is implementing two stacks at opposite ends of a single array.

- **Concept:** Stack 1 grows from the leftmost cell (index `0`) towards the right. Stack 2 grows from the rightmost cell (index `n-1`) towards the left. The stacks utilize the entire array space, and they "meet" in the middle when the total number of elements in both stacks equals the array size.
- **Implementation:**
  - Initialize `top1 = -1` and `top2 = n` (where `n` is the size of the array).
  - For **Push operation on Stack 1**: Check if there is space (`top1 < top2 - 1`). If yes, increment `top1` and insert the element.
  - For **Push operation on Stack 2**: Check if there is space (`top1 < top2 - 1`). If yes, decrement `top2` and insert the element.
  - For **Pop operations**, simply decrement `top1` for Stack 1 or increment `top2` for Stack 2.

**Example:**
Let `n = 6`. The array `arr[6]` is initially empty.

- Push `A` to Stack 1: `top1 = 0`, `arr[0] = A`
- Push `X` to Stack 2: `top2 = 5`, `arr[5] = X`
- Push `B` to Stack 1: `top1 = 1`, `arr[1] = B`
- Push `Y` to Stack 2: `top2 = 4`, `arr[4] = Y`
  The array now looks like: `[A, B, _, _, Y, X]`.

### 2.2. More Than Two Stacks (k Stacks)

The concept can be generalized to `k` number of stacks in a single array of size `n`. This requires more complex management to track the tops and available space.

- **Data Structures Required:**
  1.  `arr[n]`: The single large array that holds all the elements.
  2.  `top[k]`: An array of size `k` that stores the index of the top element for each stack. Initialize all to `-1`.
  3.  `next[n]`: An array of size `n` that serves two purposes:
      - For a used cell `i`, `next[i]` points to the next element in the same stack (like a linked list).
      - For a free cell, `next[i]` points to the next free cell in the array.
  4.  `freeTop`: An integer that always holds the index of the first free cell in the array. Initialize to `0`. Initially, `next[i] = i+1` for all `i` and `next[n-1] = -1`.

- **Push Operation (to stack `sn`):**
  1.  Check for overflow (`freeTop == -1`).
  2.  `i = freeTop;` // `i` is the index where we will store the new item.
  3.  `freeTop = next[i];` // Update `freeTop` to the next free slot.
  4.  `next[i] = top[sn];` // The new element's `next` points to the old top of its stack.
  5.  `top[sn] = i;` // Update the top of stack `sn` to `i`.
  6.  `arr[i] = new_item;` // Store the data.

- **Pop Operation (from stack `sn`):**
  1.  Check for underflow (`top[sn] == -1`).
  2.  `i = top[sn];` // `i` is the index of the top item to be removed.
  3.  `top[sn] = next[i];` // Update the top to the previous element in the stack.
  4.  `next[i] = freeTop;` // The freed cell now points to the current list of free cells.
  5.  `freeTop = i;` // This freed cell becomes the new first free cell.
  6.  Return `arr[i]`.

### 2.3. Multiple Queues in a Single Array

The concept for multiple queues is similar to that of multiple stacks. A common approach is to implement two queues, but the same `k`-stack method using `next` and `freeTop` arrays can be adapted for queues as well. For two queues:

- **Concept:** Initialize an array `arr[n]`.
- For **Queue 1**, use the front (`front1`) and rear (`rear1`) pointers. It grows from left to right.
- For **Queue 2**, use the front (`front2`) and rear (`rear2`) pointers. It grows from right to left.
- Enqueue operations must check if `rear1 < rear2 - 1` to avoid the two queues overlapping.

## 3. Key Points and Summary

| Aspect                  | Description                                                                                                                                                     |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Motivation**  | Efficient memory utilization by sharing a common array space between multiple stacks or queues. Prevents individual stack overflow when others have free space. |
| **Two-Stack Technique** | Simple and efficient. Stacks grow from opposite ends towards the middle.                                                                                        |
| **k-Stack Technique**   | More complex. Uses `top[k]`, `next[n]`, and `freeTop` to manage both the stacks and the free space in a linked-list fashion.                                    |
| **Memory Efficiency**   | Dramatically improves memory usage compared to allocating separate fixed arrays for each stack.                                                                 |
| **Time Complexity**     | All operations (Push, Pop, Enqueue, Dequeue) remain **O(1)**, i.e., constant time.                                                                              |
| **Applications**        | Used in memory management, graph algorithms (e.g., managing multiple adjacency lists), and operating systems for handling multiple process queues efficiently.  |

**In summary,** multiple stacks and queues are a crucial data structure technique for optimizing memory usage. They demonstrate how a single, large block of memory can be managed dynamically to service multiple independent lists, a common requirement in complex software systems.
