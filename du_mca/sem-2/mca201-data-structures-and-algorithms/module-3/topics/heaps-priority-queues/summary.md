# Heaps and Priority Queues - Summary

## Key Definitions and Concepts
- **Heap**: Complete binary tree satisfying heap property
- **Priority Queue**: ADT where elements have priority
- **Max-Heap**: Parent ≥ children
- **Min-Heap**: Parent ≤ children
- **Heapify**: Process to restore heap property

## Important Formulas and Theorems
- Parent index: floor((i-1)/2)
- Left child: 2i + 1
- Right child: 2i + 2
- Height of heap: ⌊log₂n⌋
- Build-heap time: O(n) (Floyd's method)
- Extract-min/max: O(log n)

## Key Points
- Heaps enable O(1) access to max/min element
- Priority queues are abstract; heaps are concrete implementation
- Array storage uses implicit tree structure
- Heap Sort achieves O(n log n) in-place sorting
- Decrease-key is crucial for Dijkstra's algorithm
- Fibonacci heaps optimize decrease-key to O(1) amortized
- Real-world use cases: OS scheduling, emergency systems

## Common Mistakes to Avoid
- Confusing heap with binary search tree (BST)
- Incorrect index calculations for child/parent nodes
- Assuming heaps maintain complete sorted order
- Forgetting to handle edge cases in percolate operations
- Misapplying time complexity (e.g., thinking build-heap is O(n log n))

## Revision Tips
1. Practice heap operations on paper using array indices
2. Implement priority queue from scratch in code
3. Compare time complexities with alternative implementations
4. Solve previous years' DU questions on Heap Sort
5. Create cheat sheet for index calculations and complexity figures

Length: 400-800 words