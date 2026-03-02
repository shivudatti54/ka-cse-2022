# **Text Book 1: Ch**

## **Collection Overview**

In Java, collections are a fundamental concept that allows you to store and manipulate groups of objects. The Java Collections Framework provides a wide range of data structures, such as lists, sets, maps, and queues, that can be used to store and retrieve data in a variety of ways.

**Key Concepts:**

- A collection is a group of objects that can be accessed and manipulated using a common interface.
- Collections provide a way to store and retrieve data in a way that is efficient and scalable.
- Collections are used extensively in Java programming to solve real-world problems.

## **Collection Interfaces**

Java provides several collection interfaces that define the basic operations that can be performed on a collection. These interfaces include:

- `Iterable`: defines the operation to iterate over a collection.
- `Collection`: defines the basic operations to add, remove, and retrieve elements from a collection.
- `List`: defines the operations to add, remove, and retrieve elements from a list.
- `Set`: defines the operations to add, remove, and retrieve elements from a set.
- `Map`: defines the operations to add, remove, and retrieve elements from a map.

**Key Concepts:**

- An interface defines a contract that must be implemented by any class that implements it.
- Interfaces are used to define a common set of methods that can be used by multiple classes.
- Interfaces are abstract and cannot be instantiated on their own.

## **Collection Classes**

Java provides several collection classes that implement the collection interfaces. These classes include:

- `ArrayList`: implements the `List` interface and provides a dynamic array-based implementation of a list.
- `LinkedList`: implements the `List` interface and provides a doubly-linked list-based implementation of a list.
- `HashSet`: implements the `Set` interface and provides a hash table-based implementation of a set.
- `HashMap`: implements the `Map` interface and provides a hash table-based implementation of a map.

**Key Concepts:**

- A class is a concrete implementation of an interface.
- Classes can provide additional methods and functionality beyond those defined in the interface.
- Classes can be instantiated and used in a variety of contexts.

## **Example Use Cases**

### Using a List

```java
import java.util.ArrayList;
import java.util.List;

public class Example {
    public static void main(String[] args) {
        // Create a list
        List<String> list = new ArrayList<>();

        // Add elements to the list
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");

        // Retrieve elements from the list
        System.out.println(list.get(0)); // prints "Apple"
        System.out.println(list.get(1)); // prints "Banana"
        System.out.println(list.get(2)); // prints "Cherry"

        // Remove an element from the list
        list.remove(1);

        // Print the updated list
        System.out.println(list); // prints "[Apple, Cherry]"
    }
}
```

### Using a Set

```java
import java.util.HashSet;
import java.util.Set;

public class Example {
    public static void main(String[] args) {
        // Create a set
        Set<String> set = new HashSet<>();

        // Add elements to the set
        set.add("Apple");
        set.add("Banana");
        set.add("Cherry");

        // Retrieve elements from the set
        System.out.println(set); // prints "[Apple, Banana, Cherry]"

        // Remove an element from the set
        set.remove("Banana");

        // Print the updated set
        System.out.println(set); // prints "[Apple, Cherry]"
    }
}
```

### Using a Map

```java
import java.util.HashMap;
import java.util.Map;

public class Example {
    public static void main(String[] args) {
        // Create a map
        Map<String, Integer> map = new HashMap<>();

        // Add elements to the map
        map.put("Apple", 1);
        map.put("Banana", 2);
        map.put("Cherry", 3);

        // Retrieve elements from the map
        System.out.println(map.get("Apple")); // prints 1
        System.out.println(map.get("Banana")); // prints 2
        System.out.println(map.get("Cherry")); // prints 3

        // Update an element in the map
        map.put("Banana", 4);

        // Print the updated map
        System.out.println(map); // prints "{Apple=1, Banana=4, Cherry=3}"
    }
}
```
