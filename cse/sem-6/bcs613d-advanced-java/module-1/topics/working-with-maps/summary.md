# Working with Maps - Summary

## Overview

The Map interface provides a key-value pair storage mechanism where each unique key maps to exactly one value. Unlike sequential collections, Maps enable O(1) average-case lookup, making them essential for efficient data access patterns. The interface offers three collection views: keySet() returns a Set of all keys, values() returns a Collection of all values, and entrySet() returns a Set of Map.Entry objects representing key-value pairs.

## Implementation Comparison

| Implementation | Internal Structure | Time Complexity | Ordering | Null Keys | Null Values |
|----------------|---------------------|-----------------|----------|-----------|-------------|
| HashMap | Hash table with buckets | O(1) average | Unordered | One allowed | Multiple allowed |
| LinkedHashMap | Hash table + doubly-linked list | O(1) average | Insertion or Access | One allowed | Multiple allowed |
| TreeMap | Red-Black tree | O(log n) | Sorted (ascending) | Not allowed* | Allowed |
| Hashtable | Hash table (synchronized) | O(1) average | Unordered | Not allowed | Not allowed |

*TreeMap allows null if Comparator accepts null

## Key Operations and Time Complexities

- **put(key, value)**: O(1) average for HashMap/LinkedHashMap, O(log n) for TreeMap
- **get(key)**: O(1) average for HashMap/LinkedHashMap, O(log n) for TreeMap  
- **containsKey(key)**: Same complexity as get() 
- **containsValue(value)**: O(n) for all implementations - requires full traversal
- **remove(key)**: O(1) average for HashMap/LinkedHashMap, O(log n) for TreeMap
- **size()**: O(1) for all implementations

## HashMap Internal Mechanics

The internal capacity starts at 16 with a default load factor of 0.75, creating a threshold of 12 entries before resizing occurs. When collisions happen (multiple keys hash to the same bucket), Java 8+ converts链表 to balanced trees after 8 entries in a single bucket, improving worst-case performance. The hashCode() and equals() methods must be consistently overridden for custom key types to ensure correct storage and retrieval behavior.

## Selection Guidelines

Choose **HashMap** for general-purpose key-value storage with fast operations. Choose **LinkedHashMap** when insertion order must be preserved or for LRU cache implementation. Choose **TreeMap** when sorted key order or range operations (subMap, headMap, tailMap) are required. Avoid Hashtable in new code; use ConcurrentHashMap for thread-safe operations instead.

## Important Exam Points

- All Map implementations except TreeMap maintain a separate internal array structure; TreeMap uses tree nodes
- The entrySet() provides the most efficient iteration when both keys and values are needed
- Structural modifications that trigger rehashing include adding new entries beyond threshold
- The fail-fast iterator throws ConcurrentModificationException if the map is modified during iteration
- HashMap allows one null key; Hashtable and TreeMap (natural ordering) do not allow null keys
- For custom keys, always override equals() and hashCode() together; hashCode() affects bucket placement while equals() resolves collisions within buckets