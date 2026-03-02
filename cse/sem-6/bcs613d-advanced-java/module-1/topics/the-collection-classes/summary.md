# Collection Classes

## Overview

Collection classes are concrete implementations of collection interfaces that provide specific data structures for storing elements. Each implementation offers different performance characteristics optimized for particular use cases like random access, frequent insertions, or sorted ordering.

## Key Points

- **ArrayList**: Resizable array with O(1) random access, grows by 50%, not synchronized
- **LinkedList**: Doubly-linked list with O(1) insertion/deletion at ends, O(n) access
- **HashSet**: Hash table implementation with O(1) operations, no ordering guarantees
- **LinkedHashSet**: Maintains insertion order with O(1) operations
- **TreeSet**: Red-Black tree with O(log n) operations, maintains sorted order
- **HashMap**: Hash table for key-value pairs, O(1) operations, allows one null key
- **TreeMap**: Red-Black tree for sorted key-value pairs, O(log n) operations
- **PriorityQueue**: Heap-based priority queue with O(log n) enqueue/dequeue

## Important Concepts

- RandomAccess marker: ArrayList has it, LinkedList doesn't
- Thread-safety: Vector and Hashtable synchronized (legacy), modern classes are not
- Ordering: HashSet (none), LinkedHashSet (insertion), TreeSet (sorted)
- Null handling: HashMap allows nulls, Hashtable doesn't, TreeSet doesn't allow null
- Performance tradeoffs: ArrayList vs LinkedList depends on access patterns

## Notes

- Choose ArrayList for frequent access, LinkedList for frequent modifications
- Use HashSet for fast lookup, TreeSet when sorted order needed
- Remember to override equals() and hashCode() for custom objects in hash-based collections
