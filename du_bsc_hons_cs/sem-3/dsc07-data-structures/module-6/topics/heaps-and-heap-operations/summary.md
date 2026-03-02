# Heaps and Heap Operations - Summary

## Key Definitions and Concepts

- **Heap**: A specialized tree-based data structure satisfying the heap property
- **Max-Heap**: Parent node value ≥ children node values; maximum at root
- **Min-Heap**: Parent node value ≤ children node values; minimum at root
- **Complete Binary Tree**: All levels filled except possibly last, filled left to right
- **Heapify**: Process of restoring heap property by moving an element down the tree
- **Sift Up**: Insertion operation that moves element upward to restore heap property

## Important Formulas and Theorems

- **Parent index**: `parent(i) = (i - 1) / 2`
- **Left child index**: `left(i) = 2 * i + 1`
- **Right child index**: `right(i) = 2 * i + 2`
- **Last non-leaf node**: `(n/2 - 1)` where n is number of elements
- **Time Complexity - Insertion**: O(log n)
- **Time Complexity - Extract Max/Min**: O(log n)
- **Time Complexity - Heapify**: O(log n)
- **Time Complexity - Build Heap**: O(n)
- **Time Complexity - Heap Sort**: O(n log n)
- **Space Complexity - Heap Sort**: O(1)

## Key Points

- Heaps are complete binary trees, allowing efficient array representation
- Heap property distinguishes max-heap (parent ≥ children) from min-heap (parent ≤ children)
- The root element in a max-heap is always the maximum; in min-heap, it's the minimum
- Build Heap processes nodes from last non-leaf to root, achieving O(n) complexity
- Heap Sort combines build heap and extract operations for in-place sorting
- Heap operations maintain O(log n) time due to tree height being O(log n)
- Heaps provide efficient priority queue implementation compared to sorted arrays

## Common Mistakes to Avoid

- Confusing heap property with binary search tree property (left < root < right)
- Forgetting that heapify is a recursive operation that may continue after one swap
- Assuming Build Heap takes O(n log n) when it's actually O(n)
- Confusing heap index calculations, especially for parent and child relationships
- Thinking heap sort produces a sorted array in ascending order directly (it builds max-heap first)

## Revision Tips

- Practice drawing heap trees from array representations and vice versa
- Trace through insertion and deletion operations step-by-step by hand
- Memorize the time complexities of all heap operations
- Implement heap operations in code to understand the recursive nature of heapify
- Solve previous year DU exam questions on heaps to understand question patterns
- Remember that heap sort is the only O(n log n) sorting algorithm with O(1) space