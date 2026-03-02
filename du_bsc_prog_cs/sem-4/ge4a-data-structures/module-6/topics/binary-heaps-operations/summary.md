# Binary Heaps - Summary

## Key Definitions and Concepts

- **Binary Heap**: A complete binary tree that satisfies the heap property - either max heap (parent ≥ children) or min heap (parent ≤ children)
- **Complete Binary Tree**: A tree where all levels except possibly the last are filled, and all nodes are as far left as possible
- **Heap Property**: For max heap, each node's value ≥ its children's values; for min heap, each node's value ≤ its children's values
- **Heapify (Sift Down)**: Operation to restore heap property by moving an element down the tree, comparing with children and swapping with the larger (for max heap)
- **Sift Up (Bubble Up)**: Operation to restore heap property after insertion by moving an element up the tree, comparing with parent and swapping if needed

## Important Formulas and Theorems

- **Parent Index**: (i - 1) / 2 (integer division)
- **Left Child Index**: 2i + 1
- **Right Child Index**: 2i + 2
- **Height of Heap**: ⌊log₂n⌋ where n is number of nodes
- **Time Complexities**:
  - Insert: O(log n)
  - Extract Max/Min: O(log n)
  - Peek: O(1)
  - Build Heap: O(n)
  - Heapify: O(log n)

## Key Points

- Binary heaps are complete binary trees that can be efficiently stored in arrays
- Max heap provides O(1) access to maximum element; min heap provides O(1) access to minimum
- Insert adds element at end and performs sift-up; Extract removes root and performs heapify
- Bottom-up heap construction achieves O(n) time, more efficient than n insertions at O(n log n)
- Binary heaps are the underlying structure for priority queues and heap sort
- Height of heap with n nodes is always ⌊log₂n⌋, guaranteeing O(log n) for tree operations
- Heap property ensures O(1) peek operation while maintaining O(log n) for insertions and deletions

## Common Mistakes to Avoid

- Confusing parent-child index formulas (remember: left = 2i+1, right = 2i+2)
- Using top-down heapify for building a heap instead of bottom-up approach (results in O(n log n) instead of O(n))
- Forgetting that array indices start at 0 when calculating parent/child relationships
- Mixing up max heap and min heap operations (comparing with wrong child)
- Not reducing heap size after extraction, leading to incorrect behavior

## Revision Tips

1. Practice drawing both tree and array representations of heaps to master conversions
2. Trace through insert and extract operations step-by-step until you can do them without notes
3. Memorize all time complexities - these are frequently tested in DU exams
4. Understand why build heap is O(n) by analyzing work done at each tree level
5. Practice implementing heap sort to solidify understanding of heap operations
6. Solve at least 3-4 previous year DU exam questions on heaps