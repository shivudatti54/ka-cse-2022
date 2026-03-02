# Collection Interfaces - Summary

## Overview

The Java Collections Framework provides a standardized architecture for representing and manipulating groups of objects. The framework centers on interface hierarchies with `Collection<E>` as the root interface, supplemented by the separate `Map<K,V>` hierarchy for key-value associations.

## Interface Hierarchy

- **Iterable<T>**: Root interface enabling enhanced for-loops via `iterator()` method
- **Collection<E>**: Base interface defining fundamental operations
- **List<E>**: Ordered sequence allowing duplicates; supports index-based access
- **Set<E>**: Unordered collection with no duplicates; models mathematical sets
- **Queue<E>**: FIFO structure with offer/poll/peek semantics
- **Deque<E>**: Double-ended queue supporting both FIFO and LIFO operations
- **Map<K,V>**: Key-value association (not a subtype of Collection)

## Key Method Contracts

| Interface | Unique Methods | Ordering | Duplicates |
|-----------|---------------|----------|------------|
| List | get(index), set(index), listIterator() | Insertion order | Allowed |
| Set | Inherited from Collection | Depends on implementation | Not allowed |
| Queue | offer(), poll(), peek() | FIFO | Depends on implementation |
| Deque | addFirst(), addLast(), removeFirst() | Both ends | Depends on implementation |

## Critical Implementation Details

- **Fail-Fast Iterators**: Throw `ConcurrentModificationException` on concurrent modification
- **Null Elements**: Most modern implementations reject null; avoid null where possible
- **Time Complexity**: HashSet/HashMap provide O(1) operations; TreeSet/TreeMap provide O(log n)
- **equals() and hashCode()**: Must be properly overridden for custom objects in Set/Map operations

## Interface Contracts to Remember

- Set.add() returns false for duplicates (not throwing exception)
- Queue.poll() returns null for empty queues; offer() returns false for full bounded queues
- List maintains insertion order and allows positional duplicates
- Map is separate from Collection hierarchy but part of the framework