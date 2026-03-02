# Single and Double Ended Priority Queues - Summary

## Key Definitions

- **Priority Queue**: Abstract data type where elements are accessed based on priority keys rather than insertion order
- **Single-Ended Priority Queue (SEPQ)**: Supports access to either minimum (Min-PQ) or maximum (Max-PQ) element efficiently
- **Double-Ended Priority Queue (DEPQ)**: Supports efficient access to both minimum and maximum elements simultaneously
- **Binary Heap**: Complete binary tree stored in array representation satisfying heap-order property
- **Heap-Order Property**: For Min-PQ, parent key ≤ children's keys; for Max-PQ, parent key ≥ children's keys
- **Min-Max Heap**: DEPQ structure with alternating min/max levels enabling O(1) access to both extremes

## Important Formulas

- Heap array indices: Left child of i = 2i + 1, Right child = 2i + 2, Parent = ⌊(i-1)/2⌋
- Heap height: h = ⌊log₂ n⌋ for n nodes
- Floyd's heap construction: O(n) time complexity
- Binary heap operations: O(log n) worst-case for insert, extract-min/max
- Fibonacci heap amortized costs: O(1) insert, O(log n) extract-min

## Key Points

1. Priority queues serve elements based on priority rather than FIFO order, essential for greedy algorithms
2. Binary heaps provide O(log n) operations with excellent cache locality due to sequential array storage
3. DEPQ structures like min-max heaps enable simultaneous access to minimum and maximum in O(1)
4. The heap property ensures the extreme element is always at the root for efficient access
5. Sift-up maintains heap property during insertion; sift-down maintains it during extraction
6. Min-max heaps organize nodes in alternating min/max levels, searching grandchildren during operations
7. Fibonacci heaps achieve amortized O(1) insertion through lazy consolidation techniques
8. Priority queues are fundamental to Dijkstra's algorithm, Prim's algorithm, and Huffman coding
9. Space complexity for binary heap is O(n); implementation simplicity makes it the default choice

## Common Mistakes

1. Confusing the parent-child relationship indices in 0-based vs 1-based array representations
2. Assuming heap operations are O(1); they are O(log n) in the worst case
3. Forgetting that Fibonacci heap's O(1) insert is amortized, not worst-case
4. Overlooking that min-max heap operations take slightly longer than binary heap due to checking grandchildren
5. Not distinguishing between SEPQ and DEPQ when selecting a data structure for a given problem
