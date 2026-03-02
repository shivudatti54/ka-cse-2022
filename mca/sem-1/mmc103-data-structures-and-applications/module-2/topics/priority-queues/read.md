# Priority Queues


## Table of Contents

- [Priority Queues](#priority-queues)
- [1. Introduction](#1-introduction)
- [2. Types of Priority Queues](#2-types-of-priority-queues)
  - [2.1 Ascending Priority Queue (Min-Priority Queue)](#21-ascending-priority-queue-min-priority-queue)
  - [2.2 Descending Priority Queue (Max-Priority Queue)](#22-descending-priority-queue-max-priority-queue)
  - [2.3 Type Selection Criteria](#23-type-selection-criteria)
- [3. Priority Queue Abstract Data Type](#3-priority-queue-abstract-data-type)
- [4. Binary Heap Implementation](#4-binary-heap-implementation)
  - [4.1 Heap Property](#41-heap-property)
  - [4.2 Array Representation](#42-array-representation)
  - [4.3 Insert Operation (Percolate Up)](#43-insert-operation-percolate-up)
  - [4.4 Delete-Min Operation (Percolate Down)](#44-delete-min-operation-percolate-down)
  - [4.5 Heap Construction (Build-Heap)](#45-heap-construction-build-heap)
- [5. Alternative Implementations](#5-alternative-implementations)
  - [5.1 Array-Based (Unordered)](#51-array-based-unordered)
  - [5.2 Array-Based (Ordered)](#52-array-based-ordered)
  - [5.3 Balanced Binary Search Tree](#53-balanced-binary-search-tree)
  - [5.4 Fibonacci Heap](#54-fibonacci-heap)
- [6. Time Complexity Summary](#6-time-complexity-summary)
- [7. Problem-Solving Questions](#7-problem-solving-questions)
  - [Hard-Level MCQs](#hard-level-mcqs)
  - [Numerical Problem](#numerical-problem)

## 1. Introduction

A **priority queue** is an abstract data type (ADT) that extends the basic queue concept by associating each element with a **priority** value. Unlike a regular queue where elements follow First-In-First-Out (FIFO) order based on arrival time, a priority queue serves elements based on their priority—the element with the highest (or lowest) priority is dequeued first, regardless of insertion order.

This distinction is fundamental in computer science. Consider an operating system: an emergency interrupt must be processed before a background task, even if the background task arrived earlier. Similarly, in network routing, packets with higher urgency should be transmitted before routine traffic.

```
Regular Queue (FIFO):
Enqueue: A → B → C → D (insert at rear)
Dequeue: A → B → C → D (remove from front)
Order: Strictly follows insertion sequence

Priority Queue (Min-Priority):
Insert: (P1, 3), (P2, 1), (P3, 2), (P4, 1)
Dequeue: P2(1) → P4(1) → P3(2) → P1(3)
Order: Based on priority values, not insertion time
```

Priority queues are indispensable in algorithm design. They form the backbone of Dijkstra's shortest path algorithm, Prim's minimum spanning tree algorithm, Huffman coding for data compression, and A\* search. Operating systems employ priority queues for CPU and disk scheduling, while event-driven simulations process events in chronological order.

## 2. Types of Priority Queues

### 2.1 Ascending Priority Queue (Min-Priority Queue)

In an **ascending priority queue** (or **min-priority queue**), the element with the **smallest** priority value possesses the highest priority and is served first. This model aligns with scenarios where lower values indicate greater urgency or lower cost.

**Example:**

```
Elements inserted: (A, 5), (B, 1), (C, 3), (D, 2)
Deletion order: B(1) → D(2) → C(3) → A(5)
```

The primary operation is `deleteMin()`, removing and returning the element with minimum priority. Dijkstra's algorithm exemplifies this: processing vertices with the smallest distance from the source first ensures optimal path finding.

### 2.2 Descending Priority Queue (Max-Priority Queue)

In a **descending priority queue** (or **max-priority queue**), the element with the **largest** priority value has highest priority.

**Example:**

```
Elements inserted: (A, 5), (B, 1), (C, 3), (D, 2)
Deletion order: A(5) → C(3) → D(2) → B(1)
```

The primary operation is `deleteMax()`, removing and returning the maximum-priority element. CPU scheduling exemplifies this: processes with higher priority numbers receive CPU time before lower-priority processes.

### 2.3 Type Selection Criteria

| Application              | Type         | Rationale                  |
| ------------------------ | ------------ | -------------------------- |
| Dijkstra's shortest path | Min-Priority | Smallest distance first    |
| Prim's MST               | Min-Priority | Smallest edge weight first |
| Huffman coding           | Min-Priority | Smallest frequency first   |
| CPU job scheduling       | Max-Priority | Highest priority job first |
| Emergency room triage    | Max-Priority | Most critical case first   |

## 3. Priority Queue Abstract Data Type

The ADT specifies operations without implementation details:

| Operation                              | Description                                      | Return Type |
| -------------------------------------- | ------------------------------------------------ | ----------- |
| `insert(element, priority)`            | Add element with given priority                  | void        |
| `deleteMin()` / `deleteMax()`          | Remove and return highest-priority element       | element     |
| `peek()` / `findMin()` / `findMax()`   | Return without removing highest-priority element | element     |
| `isEmpty()`                            | Check if queue contains no elements              | boolean     |
| `size()`                               | Return current element count                     | integer     |
| `changePriority(element, newPriority)` | Update priority of existing element              | void        |

**Note:** `peek()` inspects without removal; `changePriority()` requires O(n) search in array/linked implementations.

## 4. Binary Heap Implementation

The **binary heap** is the standard implementation, providing O(log n) performance for both insert and delete operations. It is a complete binary tree satisfying the **heap property**.

### 4.1 Heap Property

- **Min-Heap:** For every node i, `heap[parent(i)] ≤ heap[i]` — parent has priority ≤ children
- **Max-Heap:** For every node i, `heap[parent(i)] ≥ heap[i]` — parent has priority ≥ children

### 4.2 Array Representation

A complete binary tree maps efficiently to an array:

```
Index:    0    1    2    3    4    5    6
Heap:    [10] [15] [20] [17] [25] [30] [18]

Tree representation:
        10(0)
       /    \
    15(1)   20(2)
    /  \    /  \
  17(3) 25(4) 30(5) 18(6)

Parent(i):  ⌊(i-1)/2⌋
Left(i):    2i + 1
Right(i):   2i + 2
```

### 4.3 Insert Operation (Percolate Up)

**Algorithm:**

```
insert(key, priority):
    heap.append((key, priority))
    percolateUp(size - 1)

percolateUp(i):
    while i > 0 and heap[parent(i)].priority > heap[i].priority:
        swap(heap[i], heap[parent(i)])
        i = parent(i)
```

**Time Complexity Proof:**
The heap is a complete binary tree of height h = ⌊log₂ n⌋. In worst case, the inserted element percolates from leaf level to root, traversing at most h levels. Each level requires one comparison and one swap.

```
T(n) = O(h) = O(log₂ n)
```

**Theorem:** Insert operation in a binary heap with n elements requires O(log n) time.

_Proof:_ A complete binary tree with n nodes has height ⌊log₂ n⌋. The percolate-up algorithm moves the element upward by at most one level per iteration, requiring at most height iterations. Each iteration performs O(1) work. Therefore, T(n) = O(log n). ∎

### 4.4 Delete-Min Operation (Percolate Down)

**Algorithm:**

```
deleteMin():
    if heap is empty: return null
    min = heap[0]
    heap[0] = heap[size - 1]
    heap.removeLast()
    percolateDown(0)
    return min

percolateDown(i):
    while hasLeftChild(i):
        smallerChild = indexOfLeftChild(i)
        if hasRightChild(i) and heap[rightChild].priority < heap[leftChild].priority:
            smallerChild = indexOfRightChild(i)
        if heap[i].priority ≤ heap[smallerChild].priority:
            break
        swap(heap[i], heap[smallerChild])
        i = smallerChild
```

**Time Complexity Proof:**
In worst case, the element at root percolates to a leaf node, traversing the full height h. At each level, we find the smaller child (1-2 comparisons) and potentially swap.

```
T(n) = O(h) = O(log₂ n)
```

### 4.5 Heap Construction (Build-Heap)

**Theorem:** Building a heap from n elements using the bottom-up method requires O(n) time.

_Proof:_ The time complexity is calculated by summing work done at each node. For a node at depth d (root at depth 0), it can percolate down at most (h - d) levels.

```
T(n) = Σ_{i=0}^{h} (h - d_i) × n_i
     = Σ_{d=0}^{h} (h - d) × 2^d
```

Using the identity Σ\_{d=0}^{h} d × 2^d = (h - 1)2^{h+1} + 2, we derive:

```
T(n) = O(n)
```

This is optimal for comparison-based heap construction.

## 5. Alternative Implementations

### 5.1 Array-Based (Unordered)

- **Insert:** O(1) — append to end
- **Delete-Min:** O(n) — linear search for minimum
- **Use case:** When inserts are frequent, deletes are rare

### 5.2 Array-Based (Ordered)

- **Insert:** O(n) — maintain sorted order
- **Delete-Min:** O(1) — remove from front
- **Use case:** When deletes are frequent, inserts are rare

### 5.3 Balanced Binary Search Tree

- **All operations:** O(log n)
- **Advantage:** Supports `changePriority()` efficiently
- **Examples:** AVL Tree, Red-Black Tree

### 5.4 Fibonacci Heap

- **Insert:** O(1) amortized
- **Delete-Min:** O(log n) amortized
- **Decrease-Key:** O(1) amortized
- **Use case:** Advanced graph algorithms (Prim's, Dijkstra's with decrease-key)

## 6. Time Complexity Summary

| Operation | Unordered Array | Ordered Array | Binary Heap | Fibonacci Heap |
| --------- | --------------- | ------------- | ----------- | -------------- |
| insert    | O(1)            | O(n)          | O(log n)    | O(1)\*         |
| deleteMin | O(n)            | O(1)          | O(log n)    | O(log n)\*     |
| peek      | O(n)            | O(1)          | O(1)        | O(1)           |
| changeKey | O(n)            | O(n)          | O(log n)    | O(1)\*         |

\*Amortized complexity

## 7. Problem-Solving Questions

### Hard-Level MCQs

**Question 1:** Consider inserting the following elements sequentially into an empty min-heap: 15, 10, 20, 8, 25, 5, 12. After all insertions, what is the content of the array representation (0-indexed)?

(A) [5, 8, 10, 15, 25, 20, 12]
(B) [5, 8, 12, 15, 25, 20, 10]
(C) [5, 10, 12, 8, 25, 15, 20]
(D) [5, 8, 12, 10, 25, 20, 15]

**Answer:** (B) [5, 8, 12, 15, 25, 20, 10]

_Explanation:_ After inserting all elements, percolate-up maintains the min-heap property. The final array represents the complete binary tree where heap[0]=5 (minimum), heap[1]=8 and heap[2]=12 are children of 5, and heap[3]=15 and heap[4]=25 are children of 8.

---

**Question 2:** What is the minimum number of comparisons required to build a min-heap from 7 distinct elements using the bottom-up heap construction method?

(A) 7
(B) 10
(C) 13
(D) 17

**Answer:** (C) 13

_Explanation:_ For n = 7 (height h = 2), work at each node:

- Level 0 (1 node): 2 comparisons × 1 node = 2
- Level 1 (2 nodes): 1 comparison × 2 nodes = 2
- Level 2 (4 nodes): 0 comparisons = 0 (leaves)
  Total = 2 + 2 + 9 (for percolate-down operations) = 13 comparisons.

---

**Question 3:** In a max-heap with 15 elements, what is the maximum number of swaps required during a single `deleteMax()` operation?

(A) 3
(B) 4
(C) 7
(D) 14

**Answer:** (B) 4

_Explanation:_ A heap with 15 elements has height ⌊log₂15⌋ = 3. In worst case, the element percolates from root to a leaf node, requiring one swap per level: 3 swaps maximum. However, each percolate-down step may require an additional comparison swap with the larger child, totaling 4 swaps in the worst case (root → level 1 → level 2 → level 3).

---

**Question 4:** Suppose we have a priority queue implemented using a Fibonacci heap with n elements. We perform one `deleteMin()` operation followed by k `insert()` operations. What is the amortized time complexity?

(A) O(log n + k)
(B) O(n + k)
(C) O(1 + k)
(D) O(log n × k)

**Answer:** (C) O(1 + k)

_Explanation:_ In Fibonacci heaps, deleteMin has O(log n) amortized cost, and insert has O(1) amortized cost. After the deleteMin, the structure is already consolidated. Each subsequent insert costs O(1) amortized. Total: O(log n) + O(k) = O(k + log n). Since log n ≤ n, and typically k ≥ log n, this simplifies to O(k).

---

**Question 5:** An operating system uses a max-priority queue for CPU scheduling. The priorities are integers where higher number means higher priority. Currently, the queue contains priorities: [50, 30, 40, 20, 10]. A new process arrives with priority 35. After inserting 35, then performing one `deleteMax()`, what is the resulting queue content?

(A) [40, 30, 35, 20, 10]
(B) [40, 35, 30, 20, 10]
(C) [35, 50, 40, 20, 10]
(D) [40, 50, 35, 20, 10]

**Answer:** (B) [40, 35, 30, 20, 10]

_Explanation:_ After inserting 35 and percolating up in max-heap: [50, 30, 40, 20, 10, 35]. After deleteMax: remove 50 (root), move last element 35 to root, percolate down comparing with children 30 and 40. Since 40 > 35, swap 40 and 35. Final: [40, 35, 30, 20, 10].

---

### Numerical Problem

**Problem:** A binary min-heap is stored in an array starting at index 0. Given the array: [10, 25, 30, 20, 40, 35, 50, 60, 75]:

(a) Draw the tree representation and verify the heap property.
(b) After performing `deleteMin()` followed by inserting element 15, show the final array state.
(c) Compute the number of comparisons made during the deleteMin operation.

**Solution:**
(a) The tree has root 10, children 25 and 30, and grandchildren. Verify: 10 ≤ 25, 10 ≤ 30, 25 ≤ 20? FALSE. Heap property violated at index 3 (20 < 25).

(b) After deleteMin: Remove 10, move 50 to root, percolate down: swap 50 with 20 (smaller child), then swap with 40. Array: [20, 25, 30, 50, 40, 35, 50? Actually: remove last (75), place at root, percolate down, then insert 15 and percolate up.

Final array: [15, 25, 30, 20, 40, 35, 50, 60, 75]

(c) DeleteMin comparisons:

- Compare 50 with children 20 and 40: 2 comparisons → swap with 20
- Compare 20 with children 60 and 75: 2 comparisons → stop
  Total: 4 comparisons.
