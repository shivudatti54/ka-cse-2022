# Introduction to Hashing and Priority Queues - Summary

## Key Definitions and Concepts

- HASH TABLE: A data structure that implements an associative array, using a hash function to compute storage locations from keys
- HASH FUNCTION: A mathematical function that maps keys to array indices; should be uniform and efficient
- COLLISION: When two different keys hash to the same bucket location; requires resolution strategy
- LOAD FACTOR (α): Ratio of stored elements to bucket count (n/m); critical for performance
- PRIORITY QUEUE: Abstract data type where elements have associated priorities; highest priority element retrieved first
- HEAP: Complete binary tree satisfying heap property (max-heap or min-heap)
- DOUBLE-ENDED PRIORITY QUEUE (DEPQ): Supports access to both maximum and minimum elements

## Important Formulas and Theorems

- Hash function (division): h(k) = k mod m, where m is table size
- Hash function (multiplication): h(k) = floor(m × (kA mod 1)), where A is constant
- Load factor: α = n/m, where n is number of elements, m is number of buckets
- Heap insert: O(log n) time complexity
- Extract max/min from heap: O(log n) time complexity
- Building heap from n elements: O(n) time using bottom-up approach

## Key Points

- Hashing achieves O(1) average-case lookup time, making it ideal for dictionary operations
- Static hashing uses fixed bucket count; dynamic hashing adapts to dataset size
- Collision resolution via chaining maintains O(1 + α) average search time
- Open addressing requires load factor below 0.5 for good performance
- Heaps provide efficient priority queue implementation with O(log n) operations
- Max-heap root contains maximum; min-heap root contains minimum
- DEPQ implementations typically use two heaps for simultaneous access to extremes
- Priority queues are essential in Dijkstra's algorithm, Prim's algorithm, and OS scheduling

## Common Mistakes to Avoid

- Confusing max-heap and min-heap properties; always verify root contains the extreme value
- Using non-prime table sizes in division method; leads to poor distribution
- Ignoring load factor thresholds; causes significant performance degradation
- Forgetting that heap is a complete binary tree, enabling array representation

## Revision Tips

- Practice implementing hash functions and tracing collision resolution with concrete examples
- Draw heap structures from array representations and verify heap property
- Memorize the time complexities of all operations for both data structures
- Review Dijkstra's and Prim's algorithms to understand priority queue applications
- Solve previous year DU questions on hashing and priority queues for pattern familiarity