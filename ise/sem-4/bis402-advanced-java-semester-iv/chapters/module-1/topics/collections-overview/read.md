# Collections Framework: Overview and Interfaces

## Introduction to Collections Framework

The Collections Framework in Java provides a unified architecture for representing and manipulating collections of objects. Before JDK 1.2, Java offered limited collection support through classes like Vector, Hashtable, and arrays, but these implementations lacked a standardized interface hierarchy.

The Collections Framework, introduced in Java 2, provides:

- **Interfaces**: Abstract data types representing collections
- **Implementations**: Concrete classes implementing these interfaces
- **Algorithms**: Methods that perform useful operations on collections

This framework reduces programming effort, increases performance, provides interoperability between unrelated APIs, and fosters software reuse.

## Core Collection Interfaces

The Collections Framework is built around a set of core interfaces that define the fundamental collection types. These interfaces form a hierarchy that provides increasing specificity.

### The Collection Interface

The `Collection` interface is the root of the collection hierarchy. It defines the most general methods that all collections will have:

```java
public interface Collection<E> extends Iterable<E> {
    // Basic operations
    int size();
    boolean isEmpty();
    boolean contains(Object element);
    boolean add(E element);
    boolean remove(Object element);
    Iterator<E> iterator();

    // Bulk operations
    boolean containsAll(Collection<?> c);
    boolean addAll(Collection<? extends E> c);
    boolean removeAll(Collection<?> c);
    boolean retainAll(Collection<?> c);
    void clear();

    // Array operations
    Object[] toArray();
    <T> T[] toArray(T[] a);
}
```

### The Iterable Interface

The `Iterable` interface enables collections to be used with the enhanced for-loop (for-each loop):

```java
public interface Iterable<T> {
    Iterator<T> iterator();
}
```

Example usage:

```java
Collection<String> names = new ArrayList<>();
// Add elements...
for (String name : names) {
    System.out.println(name);
}
```

## Specialized Collection Interfaces

### List Interface

The `List` interface extends `Collection` and represents an ordered collection (sequence). Lists allow duplicate elements and positional access.

```java
public interface List<E> extends Collection<E> {
    // Positional access
    E get(int index);
    E set(int index, E element);
    void add(int index, E element);
    E remove(int index);

    // Search
    int indexOf(Object o);
    int lastIndexOf(Object o);

    // List-specific operations
    ListIterator<E> listIterator();
    ListIterator<E> listIterator(int index);
    List<E> subList(int fromIndex, int toIndex);
}
```

### Set Interface

The `Set` interface extends `Collection` and represents a collection that contains no duplicate elements. It models the mathematical set abstraction.

```java
public interface Set<E> extends Collection<E> {
    // Same methods as Collection, but with additional constraints
    // No duplicate elements allowed
}
```

### Queue Interface

The `Queue` interface extends `Collection` and represents a collection designed for holding elements prior to processing, typically in a FIFO (first-in-first-out) manner.

```java
public interface Queue<E> extends Collection<E> {
    // Insertion
    boolean offer(E e);  // Add if possible
    boolean add(E e);    // Add or throw exception

    // Removal
    E poll();           // Remove and return head, or null
    E remove();         // Remove and return head, or throw exception

    // Examination
    E peek();           // Return head without removing, or null
    E element();        // Return head without removing, or throw exception
}
```

### Deque Interface

The `Deque` interface (double-ended queue) extends `Queue` and supports element insertion and removal at both ends.

```java
public interface Deque<E> extends Queue<E> {
    // First element operations
    void addFirst(E e);
    void offerFirst(E e);
    E removeFirst();
    E pollFirst();
    E getFirst();
    E peekFirst();

    // Last element operations
    void addLast(E e);
    void offerLast(E e);
    E removeLast();
    E pollLast();
    E getLast();
    E peekLast();

    // Stack operations
    void push(E e);
    E pop();
}
```

## Collection Interface Hierarchy

The following diagram shows the relationship between the core collection interfaces:

```
                    Iterable<E>
                        |
                    Collection<E>
            _____________|______________
           |            |              |
         List<E>      Set<E>         Queue<E>
                                    |
                                  Deque<E>
```

## Key Methods and Their Contracts

### The equals() and hashCode() Methods

When storing objects in collections, proper implementation of `equals()` and `hashCode()` is crucial:

```java
public class Person {
    private String name;
    private int age;

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Person person = (Person) obj;
        return age == person.age && Objects.equals(name, person.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }
}
```

**Contract requirements:**

- If `a.equals(b)` is true, then `a.hashCode() == b.hashCode()` must be true
- `hashCode()` should return the same value for equal objects
- `equals()` method should be reflexive, symmetric, transitive, and consistent

### The Comparable Interface

The `Comparable` interface allows objects to define their natural ordering:

```java
public interface Comparable<T> {
    int compareTo(T o);
}
```

Example:

```java
public class Student implements Comparable<Student> {
    private String name;
    private int grade;

    @Override
    public int compareTo(Student other) {
        return Integer.compare(this.grade, other.grade);
    }
}
```

## Collection Framework Design Principles

### Generics and Type Safety

The Collections Framework uses generics to ensure type safety:

```java
// Without generics (pre-Java 5)
List list = new ArrayList();
list.add("hello");
String s = (String) list.get(0);  // Cast required

// With generics
List<String> list = new ArrayList<>();
list.add("hello");
String s = list.get(0);  // No cast needed
```

### Fail-Fast Iterators

Most collection implementations provide fail-fast iterators that throw `ConcurrentModificationException` if the collection is modified during iteration:

```java
List<String> list = new ArrayList<>();
list.add("A");
list.add("B");
list.add("C");

Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    String element = iterator.next();
    if (element.equals("B")) {
        list.remove(element);  // Throws ConcurrentModificationException
    }
}
```

To safely remove during iteration, use the iterator's remove method:

```java
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    String element = iterator.next();
    if (element.equals("B")) {
        iterator.remove();  // Safe removal
    }
}
```

## Interface Comparison Table

| Interface | Ordered | Allows Duplicates | Allows Null | Thread-Safe | Primary Implementations               |
| --------- | ------- | ----------------- | ----------- | ----------- | ------------------------------------- |
| List      | Yes     | Yes               | Yes         | No\*        | ArrayList, LinkedList, Vector\*       |
| Set       | Depends | No                | Depends     | No\*        | HashSet, LinkedHashSet, TreeSet       |
| Queue     | Yes     | Yes               | Depends     | No\*        | LinkedList, PriorityQueue, ArrayDeque |
| Deque     | Yes     | Yes               | Depends     | No\*        | ArrayDeque, LinkedList                |

\*Note: Most implementations are not thread-safe by default. Thread-safe variants are available in `java.util.concurrent` package.

## Practical Examples

### Working with Lists

```java
List<String> arrayList = new ArrayList<>();
arrayList.add("Apple");
arrayList.add("Banana");
arrayList.add(1, "Orange");  // Insert at specific position

List<String> linkedList = new LinkedList<>();
linkedList.add("First");
linkedList.addFirst("New First");  // Add to beginning
```

### Working with Sets

```java
Set<String> hashSet = new HashSet<>();
hashSet.add("Red");
hashSet.add("Green");
hashSet.add("Red");  // Duplicate, won't be added

Set<String> treeSet = new TreeSet<>();
treeSet.add("Zebra");
treeSet.add("Apple");
treeSet.add("Monkey");
// Elements are sorted: Apple, Monkey, Zebra
```

### Working with Queues

```java
Queue<String> queue = new LinkedList<>();
queue.offer("Task1");
queue.offer("Task2");
String nextTask = queue.poll();  // Returns "Task1"

Deque<String> deque = new ArrayDeque<>();
deque.offerFirst("Urgent");
deque.offerLast("Normal");
String urgent = deque.pollFirst();  // Returns "Urgent"
```

## Exam Tips

1. **Understand the contract**: Know the specific behaviors and contracts of each interface (e.g., Set doesn't allow duplicates)

2. **Method differences**: Remember subtle differences between similar methods:
   - `add()` vs `offer()`: Both add elements, but `offer()` returns false if capacity constrained
   - `remove()` vs `poll()`: Both remove elements, but `poll()` returns null if empty

3. **Iterator behavior**: Understand fail-fast iterators and how to properly modify collections during iteration

4. **Equals and hashCode**: Always override both methods together when storing custom objects in Hash-based collections

5. **Interface vs Implementation**: Differentiate between the interface contract and specific implementation behaviors

6. **Generics**: Use generics for type safety and to avoid ClassCastException

7. **Performance characteristics**: Know when to use which implementation based on required operations:
   - ArrayList for frequent random access
   - LinkedList for frequent insertions/deletions
   - HashSet for fast lookup without ordering
   - TreeSet for sorted elements with log(n) operations
