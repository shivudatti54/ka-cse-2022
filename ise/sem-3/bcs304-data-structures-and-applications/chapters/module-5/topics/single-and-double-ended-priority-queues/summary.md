# Single and Double Ended Priority Queues - Summary

## Key Definitions and Concepts

- **Priority Queue**: An abstract data type where each element has an associated priority, and elements with higher (or lower) priority are served before others
- **Single-Ended Priority Queue (SEPQ)**: Supports removal of either maximum or minimum priority element efficiently
- **Double-Ended Priority Queue (DEPQ)**: Supports efficient removal of both maximum and minimum priority elements
- **Binary Heap**: A complete binary tree satisfying the heap property—either max-heap (parent ≥ children) or min-heap (parent ≤ children)
- **Heap Property**: The key relationship between parent and child nodes that determines the ordering

## Important Formulas and Theorems

- **Array representation**: For node at index i, parent = (i-1)/2, left child = 2i+1, right child = 2i+2
- **Heap height**: ⌊log₂n⌋ for n elements
- **Time complexity (Binary Heap)**: INSERT O(log n), EXTRACT-MAX/MIN O(log n), GET-MAX/MIN O(1)
- **Heap sort time complexity**: O(n log n)
- **Space complexity**: O(n) for n elements

## Key Points

- Priority queues extend regular queues by associating priority values with elements
- Binary heaps provide efficient O(log n) insertion and extraction
- Heaps are complete binary trees, guaranteeing logarithmic height
- DEPQ can be implemented using dual heaps, balanced BST, interval heaps, or min-max heaps
- Priority queues are essential in Dijkstra's algorithm, Huffman coding, and operating system scheduling
- Min-heap returns smallest element; max-heap returns largest element
- Heapify operation builds a heap in O(n) time using bottom-up approach

## Common Mistakes to Avoid

- Confusing the heap property with binary search tree property—heaps only compare parent with children, not left with right
- Forgetting that heap must remain a complete binary tree after every operation
- Assuming priority queue maintains insertion order—it follows priority order
- Overlooking the need for synchronization in dual-heap DEPQ implementation

## Revision Tips

- Practice drawing binary heaps after each insertion and extraction operation
- Memorize the time complexities for all operations in different implementations
- Understand why complete binary trees are used (guarantees O(log n) operations)
- Review the connection between priority queues and heap sort
- Know the trade-offs between different DEPQ implementation approaches