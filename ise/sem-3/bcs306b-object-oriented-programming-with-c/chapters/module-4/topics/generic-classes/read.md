# Legacy Classes and Interfaces in Java Collections Framework

## Introduction to Legacy Classes

The Java Collections Framework (JCF) was introduced in Java 1.2 to provide a unified architecture for representing and manipulating collections. However, prior to JCF, Java had several collection classes that are now referred to as "Legacy Classes." These classes are still part of Java for backward compatibility but are largely superseded by the newer JCF classes.

Legacy classes reside primarily in the `java.util` package and include:

- Vector
- Stack
- Hashtable
- Properties
- Dictionary (abstract class)
- Enumeration (interface)

## Key Legacy Classes

### Vector Class

The `Vector` class implements a dynamic array that can grow or shrink as needed. It is similar to `ArrayList` but with two key differences: synchronization and enumeration.

```java
// Creating a Vector
Vector<String> vector = new Vector<>();
vector.add("Element1");
vector.add("Element2");

// Vector specific methods
vector.insertElementAt("New Element", 0); // Insert at specific position
vector.setSize(10); // Force size, null-padding if needed
```

**Key Characteristics:**

- Synchronized (thread-safe)
- Implements List interface
- Slower than ArrayList due to synchronization overhead
- Has additional legacy methods like `elementAt()`, `insertElementAt()`

### Stack Class

The `Stack` class extends `Vector` to implement a last-in-first-out (LIFO) stack.

```java
Stack<Integer> stack = new Stack<>();
stack.push(10); // Push element
stack.push(20);
Integer top = stack.pop(); // Remove and return top element (20)
Integer peek = stack.peek(); // View top without removal (10)
```

**Methods:**

- `push(E item)` - Adds element to top
- `pop()` - Removes and returns top element
- `peek()` - Returns top element without removal
- `empty()` - Checks if stack is empty
- `search(Object o)` - Returns position from top (1-based)

### Hashtable Class

`Hashtable` is a hash-based implementation of the Map interface, similar to `HashMap` but with key differences.

```java
Hashtable<Integer, String> hashtable = new Hashtable<>();
hashtable.put(1, "Value1");
hashtable.put(2, "Value2");

// Legacy enumeration approach
Enumeration<String> values = hashtable.elements();
while (values.hasMoreElements()) {
    System.out.println(values.nextElement());
}
```

**Characteristics:**

- Synchronized (thread-safe)
- Doesn't allow null keys or values
- Slower than HashMap due to synchronization
- Extends Dictionary abstract class

### Properties Class

The `Properties` class extends `Hashtable` and is specifically designed to handle configuration properties with string keys and values.

```java
Properties props = new Properties();
// Setting properties
props.setProperty("db.url", "jdbc:mysql://localhost:3306/mydb");
props.setProperty("db.user", "admin");

// Loading from stream
try (InputStream input = new FileInputStream("config.properties")) {
    props.load(input);
}

// Getting properties
String url = props.getProperty("db.url");
String user = props.getProperty("db.user", "default_user"); // With default
```

**Key Methods:**

- `setProperty(String key, String value)`
- `getProperty(String key)`
- `getProperty(String key, String defaultValue)`
- `load(InputStream inStream)`
- `store(OutputStream out, String comments)`

### Dictionary Abstract Class

`Dictionary` is an abstract class that served as the parent class for `Hashtable`. It's now largely obsolete but represents the early attempt at key-value mapping.

```java
// Dictionary was used like this (now deprecated approach)
Dictionary<Integer, String> dict = new Hashtable<>();
dict.put(1, "One");
String value = dict.get(1);
```

## Legacy Enumeration Interface

Before `Iterator`, Java used the `Enumeration` interface to traverse collections.

```java
Vector<String> vector = new Vector<>();
vector.add("A");
vector.add("B");
vector.add("C");

Enumeration<String> enumeration = vector.elements();
while (enumeration.hasMoreElements()) {
    String element = enumeration.nextElement();
    System.out.println(element);
}
```

**Enumeration vs Iterator:**

```
+----------------+---------------------+-----------------------+
| Feature        | Enumeration         | Iterator             |
+----------------+---------------------+-----------------------+
| Introduction   | Java 1.0            | Java 1.2             |
| Remove support | No                  | Yes (remove() method)|
| Method names   | hasMoreElements()   | hasNext()            |
|                | nextElement()       | next()               |
| Fail-fast      | No                  | Yes (in most cases)  |
| Legacy         | Yes                 | Modern standard      |
+----------------+---------------------+-----------------------+
```

## Migration from Legacy to Modern Collections

### Vector to ArrayList

```java
// Legacy approach
Vector<String> legacyVector = new Vector<>();
legacyVector.add("item");

// Modern approach - convert to ArrayList
List<String> modernList = new ArrayList<>(legacyVector);

// Or use Collections.synchronizedList for thread safety
List<String> syncList = Collections.synchronizedList(new ArrayList<>());
```

### Hashtable to HashMap

```java
// Legacy approach
Hashtable<Integer, String> legacyTable = new Hashtable<>();
legacyTable.put(1, "value");

// Modern approach
Map<Integer, String> modernMap = new HashMap<>(legacyTable);

// For thread-safe alternative
Map<Integer, String> syncMap = Collections.synchronizedMap(new HashMap<>());
```

### Stack to Deque

```java
// Legacy approach
Stack<String> legacyStack = new Stack<>();
legacyStack.push("item");

// Modern approach - use ArrayDeque
Deque<String> modernStack = new ArrayDeque<>();
modernStack.push("item");
String item = modernStack.pop();
```

## Performance Comparison

```
+----------------+-----------------+-----------------+---------------------+
| Collection     | Thread-safe     | Null allowed     | Performance         |
+----------------+-----------------+-----------------+---------------------+
| Vector         | Yes             | Yes             | Slower (synchronized)|
| ArrayList      | No              | Yes             | Faster              |
| Hashtable      | Yes             | No              | Slower (synchronized)|
| HashMap        | No              | Yes             | Faster              |
| Stack          | Yes             | Yes             | Slower (inherits    |
|                |                 |                 | Vector overhead)    |
| ArrayDeque     | No              | No              | Fastest for stacks  |
+----------------+-----------------+-----------------+---------------------+
```

## When to Use Legacy Classes

Despite being legacy, these classes still have valid use cases:

1. **Thread Safety Requirements**: When you need simple thread safety without external synchronization
2. **Backward Compatibility**: When maintaining older code that uses these classes
3. **Properties File Handling**: `Properties` class is still the standard for configuration files
4. **Stack Operations**: Though `ArrayDeque` is preferred, `Stack` is still functional

## ASCII Diagram: Legacy Collection Hierarchy

```
java.util
│
├── Dictionary (abstract) ← Obsolete
│   └── Hashtable
│       └── Properties
│
├── Vector
│   └── Stack
│
├── Enumeration (interface) ← Legacy iteration
│
└── Modern Collections Framework (Java 1.2+)
    ├── Collection (interface)
    ├── List (interface) ← Vector implements this
    ├── Map (interface) ← Hashtable implements this
    ├── Iterator (interface) ← Replaces Enumeration
    └── Various implementations
```

## Code Example: Legacy and Modern Interoperability

```java
import java.util.*;

public class LegacyModernInterop {
    public static void main(String[] args) {
        // Legacy collection
        Vector<String> legacyVector = new Vector<>();
        legacyVector.add("First");
        legacyVector.add("Second");

        // Convert to modern collection
        List<String> modernList = new ArrayList<>(legacyVector);

        // Modern collection to legacy (rarely needed)
        Vector<String> backToLegacy = new Vector<>(modernList);

        // Using Enumeration with modern collections
        Enumeration<String> enumeration = Collections.enumeration(modernList);
        while (enumeration.hasMoreElements()) {
            System.out.println(enumeration.nextElement());
        }

        // Using Iterator with legacy collections
        Iterator<String> iterator = legacyVector.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
```

## Exam Tips

1. **Remember synchronization**: Vector and Hashtable are synchronized; ArrayList and HashMap are not
2. **Null values**: Hashtable doesn't allow null keys or values; HashMap does
3. **Enumeration vs Iterator**: Know the method differences and capabilities
4. **Stack extends Vector**: This inheritance affects Stack's behavior and performance
5. **Properties specialization**: Understand it's designed specifically for string key-value pairs
6. **Conversion methods**: Know how to convert between legacy and modern collections
7. **Performance implications**: Be prepared to discuss why modern collections are generally preferred
