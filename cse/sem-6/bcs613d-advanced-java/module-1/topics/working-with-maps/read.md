# The Map Interface in Java

## Introduction and Core Contract

The Map interface in the Java Collections Framework represents a mathematical abstraction that stores key-value pairs (also known as an associative array or dictionary). Unlike collections that store individual elements, a Map maintains a set of unique keys where each key is associated with exactly one value. This design enables O(1) average-case lookup operations, making Maps essential for efficient data retrieval, caching, and indexing scenarios.

The core contract of the Map interface establishes several fundamental guarantees:

1. **Key Uniqueness**: Each key can map to at most one value. If an existing key is used in a put() operation, the previous value is replaced.
2. **Null Handling**: Implementations vary in their support for null keys and null values, which is an important consideration when selecting an implementation.
3. **Value Accessibility**: Values can be retrieved using their corresponding keys via the get() method.

The Map interface is not a subtype of Collection, though it shares some conceptual similarities. It provides three distinct collection views:

- `keySet()`: Returns a Set view of all keys
- `values()`: Returns a Collection view of all values
- `entrySet()`: Returns a Set view of all key-value mappings

## HashMap: Implementation and Internal Mechanics

HashMap is the most commonly used Map implementation, providing hash table-based storage with O(1) average-case time complexity for basic operations (put, get, remove). Understanding its internal mechanics is crucial for writing efficient code.

### Data Structure and Hashing

Internally, HashMap maintains an array of buckets (called a table), where each bucket is a linked list (or tree since Java 8) storing entries that hash to the same bucket index. When storing a key-value pair, the following process occurs:

1. The key's hashCode() is computed
2. The hash is transformed using a supplementary hash function to reduce collisions
3. The resulting index determines which bucket will hold the entry

The internal formula for index calculation ensures uniform distribution across all buckets.

### Load Factor and Threshold

HashMap maintains a load factor (default 0.75) that determines when to resize the internal array. When the number of entries exceeds the product of capacity and load factor, the array doubles in size and all entries are rehashed. The threshold is calculated as:

`threshold = capacity × loadFactor`

The default initial capacity is 16, meaning the first resize occurs when the 13th element is added (16 × 0.75 = 12, but resize happens after exceeding).

### Collision Handling

When multiple keys produce the same bucket index, a collision occurs. HashMap handles this through two mechanisms:

1. **Chaining (Java 7 and earlier)**: All entries in the same bucket form a linked list
2. **Treeification (Java 8+)**: When a bucket contains more than 8 entries, the linked list converts to a balanced tree (Red-Black tree), improving worst-case performance from O(n) to O(log n)

This optimization ensures that even with poor hash distribution, performance remains acceptable.

## TreeMap: Sorted Order Implementation

TreeMap implements the NavigableMap interface and uses a Red-Black tree internally, guaranteeing O(log n) time complexity for all operations. Keys are maintained in sorted order according to their natural ordering (using Comparable) or a custom Comparator provided at construction time.

Key characteristics include:

- No null keys allowed (throws NullPointerException)
- Maintains ascending key order
- Supports range operations like subMap(), headMap(), tailMap()
- Suitable when sorted iteration or range queries are required

## LinkedHashMap: Order-Preserving Implementation

LinkedHashMap extends HashMap but additionally maintains a doubly-linked list running through all its entries. This preserves either:

- **Insertion order** (default): The order in which entries were inserted
- **Access order**: The order of most recently accessed entries (useful for LRU caches)

When using access order, each access (get or put) moves the entry to the end of the linked list, making it ideal for implementing Least Recently Used (LRU) caches.

## Hashtable: Legacy Synchronized Implementation

Hashtable is a legacy class (present since Java 1.0) that is functionally similar to HashMap but with key differences:

- Synchronized (thread-safe) but with performance overhead
- Does not allow null keys or null values
- Uses the same internal mechanics as HashMap but without modern optimizations

For new code requiring thread safety, ConcurrentHashMap is preferred over Hashtable.

## Time Complexity Analysis

| Operation                | HashMap | TreeMap  | LinkedHashMap |
| ------------------------ | ------- | -------- | ------------- |
| get/put/remove (average) | O(1)    | O(log n) | O(1)          |
| containsKey              | O(1)    | O(log n) | O(1)          |
| containsValue            | O(n)    | O(n)     | O(n)          |
| First key                | O(1)    | O(log n) | O(1)          |
| Last key                 | O(1)    | O(log n) | O(1)          |

The containsValue() operation in all implementations requires traversing all entries, making it O(n) regardless of the underlying structure.

## Null Key Handling Across Implementations

Different Map implementations have varying policies regarding null keys:

- **HashMap**: Allows exactly one null key and any number of null values
- **LinkedHashMap**: Allows exactly one null key (inherits from HashMap)
- **TreeMap**: Does not allow null keys if using natural ordering; allows null if using Comparator that accepts null
- **Hashtable**: Does not allow null keys or null values (throws NullPointerException)
- **ConcurrentHashMap**: Does not allow null keys or null values

The restriction in TreeMap exists because the comparison mechanism must be able to compare all keys to maintain sorted order.

## Collection Views and Iteration

The three collection views (keySet, values, entrySet) provide dynamic views of the Map. Changes to the Map are reflected in these views, and conversely, changes through these views modify the underlying Map.

The entrySet() view is particularly useful for iteration, as it provides direct access to both keys and values:

```java
for (Map.Entry<K, V> entry : map.entrySet()) {
 K key = entry.getKey();
 V value = entry.getValue();
 // process entry
}
```

HashMap's iterators are fail-fast: if the map is structurally modified after iterator creation (except through the iterator's own remove() method), the iterator throws ConcurrentModificationException.

## Important Implementation Considerations

1. **HashMap Performance**: For optimal performance, pre-size the HashMap when the approximate size is known to avoid rehashing:

```java
new HashMap<>(initialCapacity, loadFactor)
```

2. **Custom Keys**: When using custom objects as keys in HashMap, always override both equals() and hashCode() consistently. Failure to do so results in lost entries since the hash-based lookup mechanism relies on these methods.

3. **TreeMap Range Operations**: TreeMap excels when range queries are needed:

```java
SortedMap<K, V> sub = treeMap.subMap(fromKey, toKey);
```

4. **LinkedHashMap for Caching**: The access-order LinkedHashMap supports efficient LRU cache implementation through its removeEldestEntry() method override.
