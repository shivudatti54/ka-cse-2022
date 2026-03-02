# Maps and Comparators in Java Collections Framework

## Introduction to Maps

While the `Collection` interface represents groups of objects, the Java Collections Framework also includes the `Map` interface for storing key-value pairs. Maps are fundamental data structures that allow efficient retrieval of values based on unique keys.

### What is a Map?

A `Map` is an object that maps keys to values. It cannot contain duplicate keys, and each key can map to at most one value. The Map interface provides three collection views:

- Set of keys
- Collection of values
- Set of key-value mappings

```
+-----------------------+
|        Map<K,V>       |
+-----------------------+
| key1 -> value1        |
| key2 -> value2        |
| key3 -> value3        |
| ...                   |
+-----------------------+
```

### Core Map Interface Methods

```java
// Basic operations
V put(K key, V value);
V get(Object key);
V remove(Object key);
boolean containsKey(Object key);
boolean containsValue(Object value);
int size();
boolean isEmpty();

// Bulk operations
void putAll(Map<? extends K, ? extends V> m);
void clear();

// Collection views
Set<K> keySet();
Collection<V> values();
Set<Map.Entry<K, V>> entrySet();
```

## Map Implementations

### HashMap

The most commonly used Map implementation that uses a hash table for storage.

**Characteristics:**

- Allows null values and one null key
- No ordering guarantees
- Constant-time performance for basic operations (get and put)
- Not synchronized

```java
Map<String, Integer> studentGrades = new HashMap<>();
studentGrades.put("Alice", 85);
studentGrades.put("Bob", 92);
studentGrades.put("Charlie", 78);

int aliceGrade = studentGrades.get("Alice"); // Returns 85
```

### LinkedHashMap

Maintains insertion order or access order.

**Characteristics:**

- Predictable iteration order
- Slightly slower than HashMap
- Maintains a doubly-linked list running through all entries

```java
Map<String, Integer> orderedMap = new LinkedHashMap<>();
orderedMap.put("Zebra", 1);
orderedMap.put("Apple", 2);
orderedMap.put("Banana", 3);
// Iteration order: Zebra, Apple, Banana
```

### TreeMap

Implements NavigableMap and stores entries in sorted order.

**Characteristics:**

- Sorted according to the natural ordering of keys or by a Comparator
- Guaranteed log(n) time cost for containsKey, get, put, and remove operations
- Implements SortedMap and NavigableMap interfaces

```java
Map<String, Integer> sortedMap = new TreeMap<>();
sortedMap.put("Zebra", 1);
sortedMap.put("Apple", 2);
sortedMap.put("Banana", 3);
// Iteration order: Apple, Banana, Zebra
```

### Hashtable

Legacy synchronized implementation.

**Characteristics:**

- Synchronized (thread-safe)
- Doesn't allow null keys or values
- Largely replaced by HashMap and ConcurrentHashMap

## Map Implementation Comparison

| Implementation | Ordering         | Null Keys/Values | Synchronized | Performance | Use Case                 |
| -------------- | ---------------- | ---------------- | ------------ | ----------- | ------------------------ |
| HashMap        | None             | Yes/Yes          | No           | O(1)        | General purpose          |
| LinkedHashMap  | Insertion/access | Yes/Yes          | No           | O(1)        | Maintain insertion order |
| TreeMap        | Sorted           | No/Yes           | No           | O(log n)    | Sorted data              |
| Hashtable      | None             | No/No            | Yes          | O(1)        | Legacy, thread-safe      |

## The Map.Entry Interface

The `Map.Entry` interface represents a key-value pair in a Map. It's useful for iterating through map entries:

```java
for (Map.Entry<String, Integer> entry : studentGrades.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

Key methods:

- `K getKey()` - returns the key
- `V getValue()` - returns the value
- `V setValue(V value)` - replaces the value

## Introduction to Comparators

### Natural Ordering vs Custom Ordering

Many collection classes can be sorted either by their **natural ordering** (if they implement Comparable) or by using a **Comparator** for custom ordering.

```java
// Natural ordering (String implements Comparable)
List<String> names = Arrays.asList("Charlie", "Alice", "Bob");
Collections.sort(names); // [Alice, Bob, Charlie]

// Custom ordering using Comparator
Collections.sort(names, Comparator.reverseOrder()); // [Charlie, Bob, Alice]
```

### The Comparator Interface

The `Comparator<T>` interface defines a single method:

```java
int compare(T o1, T o2);
```

Returns:

- Negative integer if o1 < o2
- Zero if o1 == o2
- Positive integer if o1 > o2

### Creating Custom Comparators

**Method 1: Traditional anonymous class**

```java
Comparator<String> lengthComparator = new Comparator<String>() {
    @Override
    public int compare(String s1, String s2) {
        return Integer.compare(s1.length(), s2.length());
    }
};
```

**Method 2: Lambda expression (Java 8+)**

```java
Comparator<String> lengthComparator = (s1, s2) ->
    Integer.compare(s1.length(), s2.length());
```

**Method 3: Using Comparator utility methods**

```java
// Sort by length then alphabetically
Comparator<String> complexComparator = Comparator
    .comparingInt(String::length)
    .thenComparing(Comparator.naturalOrder());
```

## Practical Examples with Maps and Comparators

### Example 1: Sorting Map by Values

```java
Map<String, Integer> scores = new HashMap<>();
scores.put("Alice", 85);
scores.put("Bob", 92);
scores.put("Charlie", 78);

// Convert to list of entries
List<Map.Entry<String, Integer>> entries = new ArrayList<>(scores.entrySet());

// Sort by value
entries.sort(Map.Entry.comparingByValue());

// Create new LinkedHashMap to maintain order
Map<String, Integer> sortedByValue = new LinkedHashMap<>();
for (Map.Entry<String, Integer> entry : entries) {
    sortedByValue.put(entry.getKey(), entry.getValue());
}
```

### Example 2: Using Comparator with TreeMap

```java
// Sort by key length
Comparator<String> keyLengthComparator = (s1, s2) ->
    Integer.compare(s1.length(), s2.length());

Map<String, Integer> customSortedMap = new TreeMap<>(keyLengthComparator);
customSortedMap.put("ZZ", 1);
customSortedMap.put("A", 2);
customSortedMap.put("BBB", 3);
// Order: A (length 1), ZZ (length 2), BBB (length 3)
```

### Example 3: Complex Comparator Chaining

```java
class Student {
    String name;
    int grade;
    int age;

    // Constructor, getters omitted
}

List<Student> students = Arrays.asList(
    new Student("Alice", 85, 20),
    new Student("Bob", 92, 19),
    new Student("Charlie", 85, 21)
);

// Sort by grade descending, then by age ascending
Comparator<Student> studentComparator = Comparator
    .comparingInt(Student::getGrade).reversed()
    .thenComparingInt(Student::getAge);

students.sort(studentComparator);
```

## Advanced Comparator Techniques

### Null-Friendly Comparators

```java
Comparator<String> nullsFirstComparator = Comparator.nullsFirst(Comparator.naturalOrder());
Comparator<String> nullsLastComparator = Comparator.nullsLast(Comparator.naturalOrder());
```

### Reversed Comparators

```java
Comparator<String> reverseComparator = Comparator.reverseOrder();
Comparator<String> specificReverse = Comparator.comparingInt(String::length).reversed();
```

### Method References in Comparators

```java
Comparator<Student> byName = Comparator.comparing(Student::getName);
Comparator<Student> byGrade = Comparator.comparingInt(Student::getGrade);
```

## Common Pitfalls and Best Practices

1. **HashMap keys must implement hashCode() and equals() properly**
   - Inconsistent implementations can cause lost entries
   - Mutable keys can cause entries to become unreachable

2. **TreeMap keys must be Comparable or use Comparator**
   - Otherwise, ClassCastException will be thrown

3. **Comparator should be consistent with equals()**
   - `compare(a, b) == 0` should imply `a.equals(b) == true`

4. **Use appropriate Map implementation for your needs**
   - HashMap for general use
   - TreeMap when sorted order is needed
   - LinkedHashMap when insertion order matters

## Performance Considerations

| Operation     | HashMap | LinkedHashMap | TreeMap  |
| ------------- | ------- | ------------- | -------- |
| put()         | O(1)    | O(1)          | O(log n) |
| get()         | O(1)    | O(1)          | O(log n) |
| containsKey() | O(1)    | O(1)          | O(log n) |
| remove()      | O(1)    | O(1)          | O(log n) |
| iteration     | O(n)    | O(n)          | O(n)     |

## Exam Tips

1. **Remember that Map is not a Collection** but part of Collections Framework
2. **HashMap allows one null key**, TreeMap allows no null keys if using natural ordering
3. **TreeMap maintains sorted order** either by natural ordering or comparator
4. **Comparator.compare() returns negative, zero, or positive** - memorize what each means
5. **For thread-safe scenarios**, use ConcurrentHashMap instead of synchronizing HashMap
6. **LinkedHashMap can be configured** for access-order instead of insertion-order
7. **Practice writing comparators** using both traditional and lambda approaches
8. **Understand the contract** between hashCode(), equals(), and compare() methods
