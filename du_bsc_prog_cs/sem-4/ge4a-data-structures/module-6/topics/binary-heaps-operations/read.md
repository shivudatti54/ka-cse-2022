# Binary Heaps: Operations and Implementation

## Introduction

A Binary Heap is a fundamental data structure that plays a crucial role in priority queue implementations, heap sort algorithms, and various graph algorithms like Dijkstra's shortest path and Prim's minimum spanning tree. In the context of the University of Delhi's Computer Science curriculum, understanding binary heaps is essential as they form the backbone of efficient scheduling, load balancing, and resource allocation systems.

A binary heap is a complete binary tree that satisfies the heap property. The tree is **complete** meaning all levels except possibly the last are completely filled, and all nodes are as far left as possible. This structural property ensures that the heap can be efficiently represented using an array, making it memory-efficient and cache-friendly. The heap property itself comes in two variants: **Max Heap** (where each parent node is greater than or equal to its children) and **Min Heap** (where each parent node is less than or equal to its children).

In real-world applications, binary heaps are extensively used in operating systems for CPU job scheduling where priority matters, in event-driven simulations, in network bandwidth allocation, and in the implementation of efficient merge operations for external sorting. The elegance of binary heaps lies in their ability to maintain the heap property through efficient O(log n) operations while providing O(1) access to the maximum or minimum element.

## Key Concepts

### Array Representation of Binary Heap

A binary heap is typically implemented using an array rather than a linked tree structure. For any node at index `i`:
- **Parent**: at index `(i-1)/2` (integer division)
- **Left Child**: at index `2i + 1`
- **Right Child**: at index `2i + 2`

This representation is space-efficient and allows for easy traversal. For example, in a heap with 10 elements stored in array `heap[0...9]`:
- Element at index 0 is the root
- Elements at indices 1, 2 form the second level
- Elements at indices 3, 4, 5, 6 form the third level

### Heap Property Maintenance

The two fundamental operations that maintain the heap property are **heapify** (also called percolate down or sift down) and **sift up** (also called percolate up or bubble up).

**Heapify (Percolate Down):** When the heap property is violated at a node (typically after removing the root or replacing it with a smaller value in a max heap), we compare the node with its children and swap with the larger child (for max heap). This process continues downward until the heap property is restored or we reach a leaf node. The time complexity is O(h) where h is the height of the tree, which is O(log n) for a heap.

**Sift Up (Percolate Up):** After inserting a new element at the end of the array, we may need to restore the heap property by comparing the new element with its parent and swapping if necessary. This process continues upward until either the element finds its correct position or reaches the root. This operation also takes O(log n) time.

### Insert Operation

To insert an element into a binary heap:
1. Add the new element at the end of the array (maintaining complete tree property)
2. Compare it with its parent
3. If it violates the heap property (greater in max heap, smaller in min heap), swap with the parent
4. Repeat step 2-3 until the heap property is satisfied or the element reaches the root

The insert operation takes O(log n) time because we traverse at most one path from the leaf to the root, and the height of a complete binary tree with n nodes is ⌊log₂n⌋.

### Extract Max/Min Operation

To extract the maximum element from a max heap (or minimum from a min heap):
1. Store the root element (maximum/minimum) to return later
2. Replace the root with the last element in the array
3. Reduce the heap size by 1
4. Call heapify on the root to restore the heap property
5. Return the stored maximum/minimum

This operation is crucial for implementing priority queues and heap sort. Each extraction takes O(log n) time.

### Build Heap Operation

Given an arbitrary array of n elements, we can build a heap in O(n) time using the **bottom-up heap construction** method:
1. Start from the last non-leaf node (at index ⌊n/2⌋ - 1)
2. Call heapify on each node moving upward to the root
3. This approach is more efficient than inserting elements one by one, which would take O(n log n)

The linear time complexity of build heap is counterintuitive but can be proven mathematically by analyzing the work done at each level of the tree.

### Other Operations

- **Peek**: Return the root element without removing it - O(1)
- **Get Size**: Return the number of elements - O(1)
- **Is Empty**: Check if heap contains any elements - O(1)
- **Decrease Key** (for min heap) / **Increase Key** (for max heap): Change the value of a key and adjust its position - O(log n)
- **Delete**: Remove an arbitrary element - O(log n) by replacing with last element and then performing heapify or sift up as needed

## Examples

### Example 1: Insert Operation in Max Heap

**Problem:** Insert the following elements one by one into a max heap: 15, 10, 20, 8, 25. Show the array representation after each insertion.

**Solution:**

**Insert 15:**
```
Array: [15]
Tree: 15 (root)
```

**Insert 10:**
```
Array: [15, 10]
Tree:    15
        /
       10
```

**Insert 20:**
- Add 20 at end: [15, 10, 20]
- Parent of index 2 is (2-1)/2 = 0
- 20 > 15, so swap
- Array: [20, 10, 15]
```
Tree:    20
        /  \
       10   15
```

**Insert 8:**
- Add 8 at end: [20, 10, 15, 8]
- Parent of index 3 is (3-1)/2 = 1
- 8 < 10, no swap needed
- Array: [20, 10, 15, 8]
```
Tree:       20
           /  \
         10    15
         /
        8
```

**Insert 25:**
- Add 25 at end: [20, 10, 15, 8, 25]
- Parent of index 4 is (4-1)/2 = 1
- 25 > 10, swap: [20, 25, 15, 8, 10]
- Parent of index 1 is (1-1)/2 = 0
- 25 > 20, swap: [25, 20, 15, 8, 10]
- Array: [25, 20, 15, 8, 10]
```
Tree:       25
           /  \
         20    15
         /  \
        8   10
```

### Example 2: Extract Max Operation

**Problem:** Extract the maximum element twice from the max heap: [25, 20, 15, 8, 10]. Show the array after each extraction.

**Solution:**

**Initial Heap:**
```
Array: [25, 20, 15, 8, 10]
Tree:       25
           /  \
         20    15
         /  \
        8   10
```

**First Extraction:**
1. Store max = 25
2. Replace root with last element: [10, 20, 15, 8]
3. Heapify at index 0:
   - Compare 10 with children 20 and 15
   - Largest child = 20 at index 1
   - 20 > 10, swap: [20, 10, 15, 8]
   - Compare 10 with children (indices 3, 4) - only index 3 exists with value 8
   - 10 > 8, no more swapping needed

**After First Extraction:**
```
Array: [20, 10, 15, 8]
Tree:      20
          /  \
        10    15
        /
       8
```
Returned: 25

**Second Extraction:**
1. Store max = 20
2. Replace root with last element: [8, 10, 15]
3. Heapify at index 0:
   - Compare 8 with children 10 and 15
   - Largest child = 15 at index 2
   - 15 > 8, swap: [15, 10, 8]
   - Compare 8 with children - no children at indices 3, 4
   - Done

**After Second Extraction:**
```
Array: [15, 10, 8]
Tree:    15
        /  \
      10    8
```
Returned: 20

### Example 3: Build Heap from Unsorted Array

**Problem:** Build a max heap from the array [4, 10, 3, 5, 1] using the bottom-up approach. Show all steps.

**Solution:**

**Initial Array:** [4, 10, 3, 5, 1]
- n = 5
- Last non-leaf node index = ⌊5/2⌋ - 1 = 1

**Start at index 1 (value 10):**
- Heapify at index 1:
  - Left child: 2×1+1 = 3 → value 5
  - Right child: 2×1+2 = 4 → value 1
  - Largest = 10 (no change)
- Array: [4, 10, 3, 5, 1]

**Move to index 0 (value 4):**
- Heapify at index 0:
  - Left child: 1 → value 10
  - Right child: 2 → value 3
  - Largest = 10 at index 1
  - Swap index 0 and 1: [10, 4, 3, 5, 1]
  - Heapify at new position (index 1):
    - Left child: 3 → value 5
    - Right child: 4 → value 1
    - Largest = 5 at index 3
    - Swap index 1 and 3: [10, 5, 3, 4, 1]
    - No children below index 3

**Final Heap:**
```
Array: [10, 5, 3, 4, 1]
Tree:       10
           /  \
          5    3
         /  \
        4   1
```

## Exam Tips

1. **Remember the array index formulas**: For index i, parent = (i-1)/2, left child = 2i+1, right child = 2i+2. These are frequently tested in DU exams.

2. **Time Complexities**: Insert = O(log n), Extract Max/Min = O(log n), Peek = O(1), Build Heap = O(n). Know these without hesitation.

3. **Max Heap vs Min Heap**: In max heap, parent ≥ children; in min heap, parent ≤ children. Always clarify which type you're working with before solving problems.

4. **Complete Binary Tree Property**: Remember that a heap is always a complete binary tree, which guarantees height = ⌊log₂n⌋, leading to O(log n) operations.

5. **Heap Sort Connection**: Heap sort works by building a max heap and repeatedly extracting the maximum element. Understand this connection as it's often asked in exams.

6. **Priority Queue Implementation**: Binary heaps are the underlying structure for priority queues. Be prepared to explain how heap operations implement priority queue functions.

7. **Common Mistake**: Don't confuse heapify (top-down) with building a heap (bottom-up). Heapify is used after extraction, while building uses bottom-up approach for O(n) complexity.

8. **Visual Representation**: Practice converting between tree and array representations of heaps. This is essential for solving numerical problems in exams.