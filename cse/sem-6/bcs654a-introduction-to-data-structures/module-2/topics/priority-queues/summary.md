# Priority Queues

## Overview

A priority queue is a special queue where elements are processed based on priority rather than FIFO order. Each element has an associated priority, and higher priority elements are dequeued before lower priority ones regardless of insertion order.

## Key Points

- **Priority-Based Ordering**: Elements dequeued by priority, not insertion order
- **Priority Assignment**: Each element has associated priority value
- **Higher Priority First**: Element with highest priority removed first
- **Implementation Methods**: Can use arrays, linked lists, or heaps
- **Heap Implementation**: Most efficient using binary heap with O(log n) operations
- **Types**: Min-priority queue (smallest first) or max-priority queue (largest first)
- **Applications**: OS task scheduling, Dijkstra's algorithm, Huffman coding, event simulation

## Important Concepts

- FIFO property replaced by priority-based ordering
- Multiple elements can have same priority
- Insertion considers priority to maintain ordering
- Array implementation simple but inefficient for large datasets
- Heap provides optimal balance between insertion and deletion
- Common in operating systems for process scheduling

## Notes

- Understand difference between FIFO queue and priority queue
- Know real-world applications like hospital emergency rooms
- Be able to explain heap-based implementation advantages
- Practice inserting elements with different priorities
- Remember applications in graph algorithms and compression
