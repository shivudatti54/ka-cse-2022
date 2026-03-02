# Heaps and Heap Operations

## Introduction

A **heap** is a specialized tree-based data structure that satisfies the **heap property**. It is one of the most important data structures in computer science, serving as the foundation for efficient priority queue implementations and sorting algorithms like Heap Sort. Heaps are particularly valuable in scenarios requiring repeated access to the maximum or minimum element, such as task scheduling, graph algorithms (Dijkstra's shortest path), and event-driven simulations.

In the context of the University of Delhi's Data Structures curriculum, heaps represent a crucial topic that connects theoretical concepts with practical applications. The binary heap, specifically, is the most commonly used implementation due to its simplicity and efficiency. Understanding heaps is essential because they provide **O(log n)** time complexity for insertion and deletion operations, making them superior to simple array-based implementations for priority queue operations. This topic appears frequently in internal assessments and end-semester examinations, with questions ranging from conceptual explanations to complex algorithm implementations.

## Key Concepts

### Definition and Properties of a Heap

A **heap** is a complete binary tree (or nearly complete) that satisfies the heap property. There are two types of heaps:

1. **Max-Heap**: For every node (except the root), the value of the node is less than or equal to the value of its parent. The maximum element is at the root.
2. **Min-Heap**: For every node (except the root), the value of the node is greater than or equal to the value of its parent. The minimum element is at the root.

The **complete binary tree** property means all levels are completely filled except possibly the last level, which is filled from left to right. This property is crucial because it allows heaps to be represented efficiently using an array.

### Array Representation of Heaps

One of the most elegant aspects of heaps is their array representation. For a heap stored in an array `arr[]` of size `n`:

- **Root element**: `arr[0]`
- **Parent of node at index i**: `arr[(i-1)/2]`
- **Left child of node at index i**: `arr[2*i + 1]`
- **Right child of node at index i**: `arr[2*i + 2]`

This representation eliminates the need for explicit pointers, saving memory and enabling cache-friendly operations. For a heap with `n` nodes, the indices of internal nodes range from `0` to `(n/2 - 1)`.

### Heap Operations

#### 1. Heapify (Sift Down / Trickle Down)

**Heapify** is the process of maintaining the heap property by moving an element down the tree until it satisfies the heap property. This operation is fundamental to heap algorithms.

```
Heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        swap arr[i] and arr[largest]
        Heapify(arr, n, largest)
```

**Time Complexity**: O(log n) in worst case, O(1) in best case

#### 2. Insertion into Heap

To insert a new element into a heap:
1. **Add the element** at the end of the array (maintaining complete binary tree property)
2. **Sift up** (heapify from bottom to top) to restore heap property

```
Insert(arr, n, key):
    n = n + 1
    arr[n-1] = key
    i = n - 1
    
    while i > 0 and arr[parent(i)] < arr[i]:
        swap arr[i] and arr[parent(i)]
        i = parent(i)
```

**Time Complexity**: O(log n)

#### 3. Deletion from Heap (Extract Max/Min)

To remove the root element (maximum in max-heap, minimum in min-heap):
1. **Replace root** with the last element
2. **Remove last element** (effectively removing the root)
3. **Heapify from root** to restore heap property

```
ExtractMax(arr, n):
    if n == 0:
        return NULL (or error)
    
    max = arr[0]
    arr[0] = arr[n-1]
    n = n - 1
    Heapify(arr, n, 0)
    
    return max
```

**Time Complexity**: O(log n)

#### 4. Build Heap

Given an unsorted array, we can convert it into a heap using the **Build Heap** operation. We start from the last non-leaf node and heapify each node going upward.

```
BuildHeap(arr, n):
    for i = (n/2 - 1) to 0:
        Heapify(arr, n, i)
```

**Time Complexity**: O(n) — this is a surprising but important result

### Heap Sort

Heap Sort is an efficient comparison-based sorting algorithm that uses a heap as the core data structure:

1. Build a max-heap from the unsorted array
2. Repeatedly extract the maximum element and place it at the end
3. Reduce heap size and heapify the root

```
HeapSort(arr, n):
    BuildMaxHeap(arr, n)
    
    for i = n-1 to 1:
        swap arr[0] and arr[i]
        Heapify(arr, i, 0)
```

**Time Complexity**: O(n log n) in all cases
**Space Complexity**: O(1) (in-place sorting)
**Stability**: Unstable

## Examples

### Example 1: Building a Max-Heap

**Problem**: Build a max-heap from the following array: [4, 10, 3, 5, 1]

**Solution**:

**Step 1**: Start from the last non-leaf node.
- n = 5, so last non-leaf node is at index (5/2 - 1) = 1
- Indices to heapify: 1, 0

**Step 2**: Heapify at index 1 (value 10)
- Tree structure at this stage:
```
        4
       / \
     10    3
    /  \
   5    1
```
- Children of 10: left=5 (index 3), right=1 (index 4)
- 10 > 5 and 10 > 1, so heap property satisfied
- Array remains: [4, 10, 3, 5, 1]

**Step 3**: Heapify at index 0 (value 4)
- Children of 4: left=10 (index 1), right=3 (index 2)
- Largest is 10 at index 1
- Swap arr[0] and arr[1]:
```
        10
       /  \
      4    3
     / \
    5   1
```
- Now heapify at index 1 (value 4)
- Children of 4: left=5 (index 3), right=1 (index 4)
- Largest is 5 at index 3
- Swap arr[1] and arr[3]:
```
        10
       /  \
      5    3
     / \
    4   1
```
- Final heap: [10, 5, 3, 4, 1]

### Example 2: Insertion into a Min-Heap

**Problem**: Insert element 2 into the following min-heap: [3, 5, 8, 7, 9, 10]

**Solution**:

**Step 1**: Insert 2 at the end
- New array: [3, 5, 8, 7, 9, 10, 2]
- New element at index 6

**Step 2**: Sift up
- Parent of index 6: (6-1)/2 = 2, value = 8
- 2 < 8, so swap:
- Array: [3, 5, 2, 7, 9, 10, 8]
- New position: index 2

- Parent of index 2: (2-1)/2 = 0, value = 3
- 2 < 3, so swap:
- Array: [2, 5, 3, 7, 9, 10, 8]
- New position: index 0

- Now at root, stop
- Final min-heap: [2, 5, 3, 7, 9, 10, 8]

### Example 3: Heap Sort Demonstration

**Problem**: Sort the array [12, 11, 13, 5, 6, 7] using Heap Sort

**Solution**:

**Step 1**: Build max-heap
- Build heap from array: [12, 11, 13, 5, 6, 7]
- After building: [13, 11, 12, 5, 6, 7]

**Step 2**: Extract elements
- Swap arr[0] and arr[5]: [7, 11, 12, 5, 6, 13]
- Heapify root (0) with heap size 5: [12, 11, 7, 5, 6, 13]
- Swap arr[0] and arr[4]: [6, 11, 7, 5, 12, 13]
- Heapify root with heap size 4: [11, 6, 7, 5, 12, 13]
- Swap arr[0] and arr[3]: [5, 6, 7, 11, 12, 13]
- Heapify root with heap size 3: [7, 6, 5, 11, 12, 13]
- Swap arr[0] and arr[2]: [5, 6, 7, 11, 12, 13]
- Heapify root with heap size 2: [6, 5, 7, 11, 12, 13]
- Swap arr[0] and arr[1]: [5, 6, 7, 11, 12, 13]

**Sorted Array**: [5, 6, 7, 11, 12, 13]

## Exam Tips

1. **Remember the heap property**: For max-heap, parent ≥ children; for min-heap, parent ≤ children. This is frequently tested in conceptual questions.

2. **Array representation formulas**: Memorize the parent, left child, and right child index formulas: parent(i) = (i-1)/2, left(i) = 2*i + 1, right(i) = 2*i + 2.

3. **Time complexities**: Insertion - O(log n), Deletion (Extract Max/Min) - O(log n), Heapify - O(log n), Build Heap - O(n), Heap Sort - O(n log n).

4. **Build Heap complexity**: Remember that Build Heap runs in O(n) time, not O(n log n), despite appearing to require n heapify operations.

5. **Heap is not fully sorted**: The heap property only guarantees that the root is the maximum/minimum, not that the array is sorted in order.

6. **Complete binary tree property**: This ensures the heap can be stored efficiently in an array with no gaps, which is why heap operations are so efficient.

7. **Heap Sort is in-place**: It requires only O(1) auxiliary space, making it suitable for memory-constrained environments.

8. **Applications**: Be familiar with real-world applications like priority queues, job scheduling, and graph algorithms (Dijkstra's, Prim's).