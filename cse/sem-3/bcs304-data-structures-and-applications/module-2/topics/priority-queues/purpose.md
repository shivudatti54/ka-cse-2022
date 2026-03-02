# Learning Objectives

After studying this topic, you should be able to:

1. **Define** a priority queue and **identify** the two main types (ascending/min-priority queue and descending/max-priority queue) with their respective deletion operations.
2. **List** the core operations of the priority queue ADT (insert, deleteMin, deleteMax, peek, isEmpty, size, changePriority) and **describe** their purposes.
3. **Explain** the fundamental difference between a regular FIFO queue and a priority queue in terms of element ordering.
4. **Compare** and **contrast** the time complexities of different priority queue implementations (unsorted array, sorted array, sorted linked list, binary heap) for insert, delete, and peek operations.
5. **Analyze** the trade-offs between unsorted and sorted implementations and **determine** when to use each based on the frequency of insertions versus deletions.
6. **Implement** the insert and deleteMin operations for a sorted linked list priority queue in C, including proper memory allocation and traversal logic.
7. **Apply** the sorted array trick (storing elements in descending priority order for a min-PQ) to achieve O(1) deleteMin complexity and **evaluate** its impact on performance.
8. **Justify** why binary heap is the preferred implementation for general-purpose priority queues by **analyzing** its O(log n) performance for both insert and delete operations.
9. **Design** a solution using priority queues for a real-world problem, such as CPU scheduling or event-driven simulation, and **assess** its efficiency.
