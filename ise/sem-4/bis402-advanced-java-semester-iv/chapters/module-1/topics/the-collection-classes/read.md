# Collection Classes and Implementations

## Introduction to Collection Classes

The Java Collections Framework provides a comprehensive architecture to store and manipulate groups of objects. Collection classes are concrete implementations of the collection interfaces that provide the data structures for storing elements. These implementations offer different performance characteristics and are optimized for various use cases.

The core collection interfaces include: Collection, List, Set, Queue, and Map. Each interface has multiple implementations with different characteristics.

## List Implementations

### ArrayList

ArrayList is a resizable array implementation of the List interface. It provides fast random access and is ideal when frequent access by index is required.

```java
List<String> arrayList = new ArrayList<>();
arrayList.add("Java");
arrayList.add("Python");
arrayList.add("C++");
```

**Characteristics:**

- Dynamic resizing (grows by 50% when capacity exceeded)
- Implements RandomAccess interface (fast index-based access)
- Not synchronized (not thread-safe)
- O(1) for get/set operations
- O(n) for add/remove operations at beginning/middle

### LinkedList

LinkedList is a doubly-linked list implementation of both List and Deque interfaces. It provides efficient insertion and deletion operations.

```java
List<String> linkedList = new LinkedList<>();
linkedList.add("First");
linkedList.add("Second");
linkedList.addFirst("New First");
```

**Characteristics:**

- Efficient insertion/deletion (O(1) at ends, O(n) in middle)
- Implements both List and Deque interfaces
- Poor random access performance (O(n))
- Extra memory overhead for node references

### Vector

Vector is a legacy synchronized implementation similar to ArrayList. It's thread-safe but has performance overhead due to synchronization.

```java
Vector<String> vector = new Vector<>();
vector.add("Element");
vector.addElement("Another");
```

**Characteristics:**

- Synchronized (thread-safe)
- Grows by doubling size when capacity exceeded
- Legacy class, largely replaced by ArrayList

## Set Implementations

### HashSet

HashSet implements the Set interface using a hash table (actually a HashMap instance). It provides constant-time performance for basic operations.

```java
Set<String> hashSet = new HashSet<>();
hashSet.add("Apple");
hashSet.add("Banana");
hashSet.add("Apple"); // Duplicate, won't be added
```

**Characteristics:**

- Stores elements using hashCode()
- No ordering guarantees
- O(1) for add, remove, contains operations
- Performance depends on hash function quality

### LinkedHashSet

LinkedHashSet maintains a doubly-linked list running through all entries, preserving insertion order.

```java
Set<String> linkedHashSet = new LinkedHashSet<>();
linkedHashSet.add("Zebra");
linkedHashSet.add("Apple");
// Iteration order: Zebra, Apple (insertion order)
```

**Characteristics:**

- Predictable iteration order (insertion order)
- Slightly slower than HashSet due to linked list maintenance
- O(1) for basic operations

### TreeSet

TreeSet implements the NavigableSet interface using a Red-Black tree structure. Elements are stored in sorted order.

```java
Set<String> treeSet = new TreeSet<>();
treeSet.add("Orange");
treeSet.add("Apple");
treeSet.add("Banana");
// Sorted order: Apple, Banana, Orange
```

**Characteristics:**

- Elements stored in sorted order (natural ordering or Comparator)
- O(log n) for basic operations
- Implements NavigableSet interface for navigation methods

## Queue Implementations

### PriorityQueue

PriorityQueue is an unbounded priority queue based on a priority heap. Elements are ordered according to their natural ordering or by a Comparator.

```java
Queue<Integer> priorityQueue = new PriorityQueue<>();
priorityQueue.add(30);
priorityQueue.add(10);
priorityQueue.add(20);
// Poll order: 10, 20, 30 (natural ordering)
```

**Characteristics:**

- No capacity constraints (grows automatically)
- O(log n) time for enqueuing and dequeuing methods
- Not synchronized
- Head is the least element according to ordering

### ArrayDeque

ArrayDeque is a resizable-array implementation of the Deque interface. It's more efficient than Stack when used as a stack and faster than LinkedList when used as a queue.

```java
Deque<String> arrayDeque = new ArrayDeque<>();
arrayDeque.addFirst("Front");
arrayDeque.addLast("Back");
arrayDeque.offer("End");
```

**Characteristics:**

- No capacity restrictions
- Faster than Stack and LinkedList for stack/queue operations
- Not thread-safe
- O(1) for add/remove at both ends

## Map Implementations

### HashMap

HashMap is a hash table based implementation of the Map interface. It provides constant-time performance for basic operations.

```java
Map<String, Integer> hashMap = new HashMap<>();
hashMap.put("John", 25);
hashMap.put("Alice", 30);
hashMap.put("Bob", 28);
```

**Characteristics:**

- Allows one null key and multiple null values
- No ordering guarantees
- O(1) for get and put operations (assuming good hash distribution)
- Capacity and load factor affect performance

### LinkedHashMap

LinkedHashMap maintains a doubly-linked list running through all entries, preserving insertion order or access order.

```java
Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
linkedHashMap.put("First", 1);
linkedHashMap.put("Second", 2);
// Iteration order: First, Second
```

**Characteristics:**

- Predictable iteration order
- Can be configured for access-order (for LRU cache implementation)
- Slightly slower than HashMap

### TreeMap

TreeMap is a Red-Black tree based implementation of the NavigableMap interface. Keys are stored in sorted order.

```java
Map<String, Integer> treeMap = new TreeMap<>();
treeMap.put("Orange", 3);
treeMap.put("Apple", 1);
treeMap.put("Banana", 2);
// Key order: Apple, Banana, Orange
```

**Characteristics:**

- Keys are sorted (natural ordering or Comparator)
- O(log n) for containsKey, get, put, remove
- Implements NavigableMap for navigation methods

### Hashtable

Hashtable is a legacy synchronized implementation similar to HashMap. It doesn't allow null keys or values.

```java
Hashtable<String, Integer> hashtable = new Hashtable<>();
hashtable.put("Key", 100);
```

**Characteristics:**

- Synchronized (thread-safe)
- Doesn't allow null keys or values
- Legacy class, largely replaced by HashMap

## Performance Comparison Table

| Implementation | Ordering  | Null Elements | Duplicates | Get/Contains | Add/Remove | Thread-Safe |
| -------------- | --------- | ------------- | ---------- | ------------ | ---------- | ----------- |
| ArrayList      | Insertion | Yes           | Yes        | O(1)         | O(n)       | No          |
| LinkedList     | Insertion | Yes           | Yes        | O(n)         | O(1)       | No          |
| HashSet        | None      | Yes           | No         | O(1)         | O(1)       | No          |
| LinkedHashSet  | Insertion | Yes           | No         | O(1)         | O(1)       | No          |
| TreeSet        | Sorted    | No            | No         | O(log n)     | O(log n)   | No          |
| HashMap        | None      | 1 null key    | Keys: No   | O(1)         | O(1)       | No          |
| LinkedHashMap  | Insertion | 1 null key    | Keys: No   | O(1)         | O(1)       | No          |
| TreeMap        | Sorted    | No null keys  | Keys: No   | O(log n)     | O(log n)   | No          |
| Vector         | Insertion | Yes           | Yes        | O(1)         | O(n)       | Yes         |
| Hashtable      | None      | No            | Keys: No   | O(1)         | O(1)       | Yes         |

## Choosing the Right Collection

**When to use ArrayList:**

- Frequent access by index
- Mostly add/remove at end of list
- Don't need thread safety

**When to use LinkedList:**

- Frequent add/remove at beginning/middle
- Need Deque functionality
- Don't need random access

**When to use HashSet:**

- Need fast lookup
- Don't care about order
- Need to avoid duplicates

**When to use TreeSet:**

- Need sorted elements
- Need range operations
- Willing to accept O(log n) performance

**When to use HashMap:**

- Key-value storage with fast access
- Don't care about order
- Need O(1) performance

**When to use TreeMap:**

- Need sorted keys
- Need range operations on keys
- Willing to accept O(log n) performance

## Iterators and Fail-Fast Behavior

Most collection implementations provide fail-fast iterators that throw ConcurrentModificationException if the collection is modified during iteration (except through iterator's own methods).

```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C"));
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    String element = iterator.next();
    if (element.equals("B")) {
        list.remove("B"); // Throws ConcurrentModificationException
    }
}
```

## Storing User-Defined Classes

When storing custom objects in hash-based collections (HashSet, HashMap), you must properly override hashCode() and equals() methods.

```java
class Student {
    private String id;
    private String name;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return Objects.equals(id, student.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
```

## Collection Algorithms

The Collections class provides utility methods for common operations:

- Sorting: Collections.sort(list)
- Searching: Collections.binarySearch(list, key)
- Shuffling: Collections.shuffle(list)
- Synchronization wrappers: Collections.synchronizedList(list)

## Exam Tips

1. **Remember performance characteristics**: ArrayList for random access, LinkedList for frequent modifications
2. **Understand ordering**: HashSet (none), LinkedHashSet (insertion), TreeSet (sorted)
3. **Know thread-safe alternatives**: Use CopyOnWriteArrayList instead of Vector, ConcurrentHashMap instead of Hashtable
4. **HashCode/Equals contract**: Critical for proper functioning of hash-based collections
5. **Fail-fast iterators**: Understand ConcurrentModificationException and how to avoid it
6. **Legacy classes**: Know that Vector and Hashtable are synchronized but largely replaced by newer implementations
