# Java Collection Interfaces

## Introduction to the Java Collections Framework

The Java Collections Framework (JCF) represents a unified architecture for representing and manipulating collections of objects. Introduced in Java 2 (JDK 1.2), the framework provides a set of interfaces and classes that implement reusable data structures, eliminating the need for programmers to write collection implementations from scratch. The framework is built around a hierarchical interface structure with `Collection` as the root interface from which `List`, `Set`, `Queue`, and `Deque` extend. Additionally, `Map` represents a separate hierarchy for key-value pair storage.

## The Collection Interface

The `Collection<E>` interface serves as the root of the entire collection hierarchy. It defines the fundamental operations that all collections must implement:

```java
public interface Collection<E> extends Iterable<E> {
 boolean add(E e);
 boolean remove(Object o);
 int size();
 boolean isEmpty();
 boolean contains(Object o);
 void clear();
 Iterator<E> iterator();
}
```

The `add(E e)` method ensures the collection contains the specified element, returning true if the collection was modified. The `remove(Object o)` method removes a single instance of the specified element. The contract specifies that the collection should throw `UnsupportedOperationException` if it does not permit duplicate elements or modification.

## The List Interface

The `List<E>` interface extends `Collection` and represents an ordered collection (sequence) that allows duplicate elements. Lists maintain insertion order and provide positional access through zero-based indexing.

```java
List<String> studentNames = new ArrayList<>();
studentNames.add("Alice"); // Index 0
studentNames.add("Bob"); // Index 1
studentNames.add("Alice"); // Duplicate allowed at Index 2

System.out.println(studentNames.get(1)); // Output: Bob
System.out.println(studentNames.indexOf("Alice")); // Output: 0
```

Key methods include:

- `E get(int index)` - returns element at specified position
- `E set(int index, E element)` - replaces element at index
- `void add(int index, E element)` - inserts at specified position
- `E remove(int index)` - removes element at index
- `ListIterator<E> listIterator()` - bidirectional traversal

## The Set Interface

The `Set<E>` interface models the mathematical concept of a set—a collection containing no duplicate elements. The contract requires that no two elements `e1` and `e2` satisfy `e1.equals(e2)`. Implementations include `HashSet` (unordered), `LinkedHashSet` (insertion-ordered), and `TreeSet` (sorted).

## The Queue and Deque Interfaces

The `Queue<E>` interface extends `Collection` to support FIFO (First-In-First-Out) operations:

- `boolean offer(E e)` - inserts element, returns false if full
- `E poll()` - removes and returns head, null if empty
- `E peek()` - returns head without removal, null if empty

The `Deque<E>` interface (Double-Ended Queue) extends `Queue` to support insertion and removal at both ends:

- `void addFirst(E e)` / `void addLast(E e)`
- `E removeFirst()` / `E removeLast()`
- `E getFirst()` / `E getLast()`

## Important Contracts and Behaviors

**Fail-Fast Iterators**: Iterators returned by collection implementations are fail-fast, meaning they throw `ConcurrentModificationException` if the collection is structurally modified during iteration (except through the iterator's own remove method).

**Modifiability**: Collections may be unmodifiable (read-only) or modifiable. Creating an unmodifiable collection through `Collections.unmodifiableList()` enforces immutability at the collection level.

**Null Handling**: Most implementations do not permit null elements; `HashMap`, `Hashtable`, and `ArrayList` historically allowed null, but modern best practices discourage null elements in collections.

## Time Complexity Considerations

| Operation  | ArrayList | LinkedList | HashSet | TreeSet  |
| ---------- | --------- | ---------- | ------- | -------- |
| add()      | O(1)\*    | O(1)       | O(1)    | O(log n) |
| remove()   | O(n)      | O(n)       | O(1)    | O(log n) |
| contains() | O(n)      | O(n)       | O(1)    | O(log n) |
| get()      | O(1)      | O(n)       | N/A     | N/A      |

\*Amortized complexity

## Interface Hierarchy Summary

```
Iterable<T>
 └── Collection<E>
 ├── List<E>
 ├── Set<E>
 │ └── SortedSet<E>
 └── Queue<E>
 └── Deque<E>

Map<K,V>
 └── SortedMap<K,V>
```

The Map interface, while not extending Collection, is part of the Java Collections Framework and provides key-value pair storage with operations like `put()`, `get()`, `containsKey()`, and `containsValue()`.
