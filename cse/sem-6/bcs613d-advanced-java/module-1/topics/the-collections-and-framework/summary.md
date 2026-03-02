# Collections and Framework

## Overview

The Java Collections Framework provides a unified architecture for representing and manipulating collections of objects. It includes interfaces (List, Set, Map, Queue), concrete implementations (ArrayList, HashSet, HashMap), and algorithms that operate on collections, reducing programming effort while increasing performance.

## Key Points

- **Unified Architecture**: Standard way to store and manipulate groups of objects introduced in Java 1.2
- **Core Interfaces**: Collection, List, Set, Queue, Deque, and Map form the hierarchy
- **ArrayList Implementation**: Dynamic array with O(1) random access, amortized O(1) add, O(n) insert/delete
- **Generic Support**: Type-safe collections using generics to avoid ClassCastException
- **Algorithms**: Static methods in Collections class for sorting, searching, shuffling
- **Performance Benefits**: Optimized implementations for different use cases (random access vs sequential)

## Important Concepts

- List allows duplicates and maintains insertion order
- Set stores unique elements only
- Map stores key-value pairs with unique keys
- Queue supports FIFO processing
- Fail-fast iterators detect concurrent modifications
- ArrayList capacity grows by ~50% when exceeded

## Notes

- Understand the difference between interface and implementation when choosing collections
- Know performance characteristics: ArrayList O(1) access, LinkedList O(1) insertion/deletion in middle
- Remember that Map is not part of Collection interface hierarchy
- Use synchronized wrappers for thread-safe operations