# Iterator Pattern in Java Collections

## Theoretical Background

The Iterator design pattern is a behavioral pattern that provides a standardized mechanism for traversing elements of a collection sequentially without exposing the underlying representation. In Java, this pattern is implemented through the `Iterator<E>` interface, which was introduced in Java 1.2 as part of the Collections Framework, replacing the legacy `Enumeration` interface.

## Interface Definition

The `Iterator<E>` interface declares three fundamental methods:

```java
public interface Iterator<E> {
 boolean hasNext(); // Returns true if iteration has more elements
 E next(); // Returns next element and advances cursor
 void remove(); // Removes last element returned by next()
}
```

Note: The `remove()` method is optional and throws `UnsupportedOperationException` if the collection does not support removal.

## Complete Implementation Example

```java
import java.util.*;

public class IteratorDemo {
 public static void main(String[] args) {
 // Create and populate an ArrayList
 List<String> fruits = new ArrayList<>();
 fruits.add("Apple");
 fruits.add("Banana");
 fruits.add("Cherry");
 fruits.add("Date");

 // Obtain iterator from collection
 Iterator<String> iterator = fruits.iterator();

 // Traverse collection using iterator pattern
 while (iterator.hasNext()) {
 String element = iterator.next();
 System.out.println("Element: " + element);

 // Safe removal: Remove "Banana" during iteration
 if (element.equals("Banana")) {
 iterator.remove(); // Removes last element returned by next()
 }
 }

 System.out.println("After removal: " + fruits);
 }
}
```

**Output:**

```
Element: Apple
Element: Banana
Element: Cherry
Element: Date
After removal: [Apple, Cherry, Date]
```

## Internal Working Mechanism

When `iterator()` is called, the collection returns an object implementing the `Iterator` interface. This iterator maintains an internal cursor position (initially pointing before the first element). The `hasNext()` method checks if any elements remain ahead of the cursor, while `next()` advances the cursor and returns the element it passes.

## Fail-Fast Iterator Behavior

Java's standard iterators are **fail-fast**: they throw `ConcurrentModificationException` if the collection is structurally modified during iteration via any method other than the iterator's own `remove()` method. This detects concurrent modifications that may cause unpredictable behavior:

```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C"));
for (String s : list) {
 list.remove(s); // Throws ConcurrentModificationException
}
```

This behavior is implemented by maintaining a `modCount` (modification count) in the collection and comparing it with the expected count stored at iterator creation time.

## Comparison with Legacy Enumeration

The `Enumeration` interface (legacy, JDK 1.0) has been superseded by `Iterator`:

| Feature           | Enumeration                          | Iterator              |
| ----------------- | ------------------------------------ | --------------------- |
| Method names      | `hasMoreElements()`, `nextElement()` | `hasNext()`, `next()` |
| Remove capability | No                                   | Yes (`remove()`)      |
| Legacy            | Yes                                  | No (modern)           |

## Enhanced For-Loop (For-Each)

The enhanced for-loop is syntactic sugar that internally uses iterators for collections:

```java
// This is equivalent to using an iterator
for (String fruit : fruits) {
 System.out.println(fruit);
}
```

However, the enhanced for-loop cannot modify the collection during iteration (it uses an internal iterator without exposing the `remove()` method).

## ListIterator: Bidirectional Traversal

For `List` implementations, `ListIterator` provides additional capabilities:

```java
ListIterator<String> listItr = fruits.listIterator();
while (listItr.hasNext()) {
 int index = listItr.nextIndex();
 String element = listItr.next();
 // Can also traverse backwards using hasPrevious() and previous()
}
```

`ListIterator` supports: `add()`, `set()`, `hasPrevious()`, `previous()`, `nextIndex()`, `previousIndex()`.

## Best Practices

1. **Use iterator.remove()** instead of `collection.remove()` during iteration
2. **Prefer enhanced for-loop** when modification is not needed
3. **Handle NoSuchElementException** when using `next()` without checking `hasNext()`
4. **Use ListIterator** when bidirectional traversal or element modification is required
5. **Be aware of fail-fast behavior** when working with shared data structures
