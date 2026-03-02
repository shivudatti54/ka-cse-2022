# Comparators in Advanced Java

## Introduction

The Comparator interface in Java is a powerful mechanism for defining custom ordering of objects. While the Comparable interface provides a natural ordering for classes (implemented by the objects themselves), Comparator allows external control over sorting logic without modifying the original class. This becomes particularly valuable when working with third-party classes where the source code cannot be altered, or when multiple different sort orders are needed for the same class.

The Comparator interface was introduced in Java 1.2 and has been significantly enhanced in Java 8 with the addition of default methods and static factory methods, making it far more versatile than its original implementation. Understanding Comparators is essential for effective use of the Java Collections Framework, particularly with sorted collections like TreeSet, TreeMap, and sorting algorithms that accept custom comparators.

This topic builds upon your understanding of the Collections Framework and prepares you for implementing complex sorting requirements in real-world applications.

## Key Concepts

### The Comparator Interface

The Comparator<T> interface is defined in java.util package and contains two key methods:

1. **int compare(T o1, T o2)**: Compares its two arguments for order. Returns a negative integer, zero, or positive integer if the first argument is less than, equal to, or greater than the second argument.

2. **boolean equals(Object obj)**: Indicates whether some other object is "equal to" this comparator. This method is already implemented in Object class, so overriding is optional.

```java
public interface Comparator<T> {
 int compare(T o1, T o2);
 boolean equals(Object obj);

 // Default methods added in Java 8
 default Comparator<T> reversed() { ... }
 default Comparator<T> thenComparing(Comparator<? super T> other) { ... }
 default <U> Comparator<T> thenComparing(Function<? super T, ? extends U> keyExtractor,
 Comparator<? super U> keyComparator) { ... }

 // Static methods added in Java 8
 public static <T> Comparator<T> comparing(Function<? super T, ? extends U> keyExtractor) { ... }
 public static <T> Comparator<T> nullsFirst(Comparator<? super T> comparator) { ... }
 public static <T> Comparator<T> nullsLast(Comparator<? super T> comparator) { ... }
}
```

### Comparator vs Comparable

| Aspect            | Comparable                            | Comparator                          |
| ----------------- | ------------------------------------- | ----------------------------------- |
| Package           | java.lang                             | java.util                           |
| Implementation    | Implemented by the class being sorted | Separate class or lambda expression |
| Modification      | Modifies the original class           | Does not modify the class           |
| Sorting method    | Collections.sort(list)                | Collections.sort(list, comparator)  |
| Single sort order | Only one natural ordering             | Multiple sort orders possible       |
| Purpose           | Defines natural ordering              | Defines custom ordering             |

### Using Comparator with Collections

Comparator is extensively used with various collection classes:

**With Collections.sort():**

```java
List<Employee> employees = new ArrayList<>();
employees.add(new Employee("John", 50000));
employees.add(new Employee("Alice", 30000));

// Using anonymous class
Collections.sort(employees, new Comparator<Employee>() {
 @Override
 public int compare(Employee e1, Employee e2) {
 return e1.getName().compareTo(e2.getName());
 }
});

// Using lambda expression (Java 8+)
employees.sort((e1, e2) -> e1.getName().compareTo(e2.getName()));
```

**With TreeSet:**

```java
TreeSet<Employee> treeSet = new TreeSet<>(new Comparator<Employee>() {
 @Override
 public int compare(Employee e1, Employee e2) {
 return e1.getSalary() - e2.getSalary();
 }
});
```

**With TreeMap:**

```java
TreeMap<Employee, String> treeMap = new TreeMap<>(new Comparator<Employee>() {
 @Override
 public int compare(Employee e1, Employee e2) {
 return e1.getName().compareTo(e2.getName());
 }
});
```

### Comparator Chaining with thenComparing()

Java 8 introduced the thenComparing() method for chaining multiple comparison criteria:

```java
List<Employee> employees = new ArrayList<>();

// Sort by name, then by salary (if names are equal)
employees.sort(Comparator
 .comparing(Employee::getName)
 .thenComparing(Employee::getSalary));
```

### Static Factory Methods

Java 8 provides convenient static factory methods:

**comparing():**

```java
Comparator<Employee> byName = Comparator.comparing(Employee::getName);
Comparator<Employee> bySalary = Comparator.comparing(Employee::getSalary);
```

**reversed():**

```java
Comparator<Employee> bySalaryDesc = Comparator.comparing(Employee::getSalary).reversed();
```

**nullsFirst() and nullsLast():**

```java
// Handle null values - nulls appear first
Comparator<Employee> nullsFirst = Comparator.nullsFirst(
 Comparator.comparing(Employee::getName)
);

// Handle null values - nulls appear last
Comparator<Employee> nullsLast = Comparator.nullsLast(
 Comparator.comparing(Employee::getName)
);
```

### Using Comparator with Arrays

```java
Employee[] employees = new Employee[3];
// ... initialize array ...

// Using Arrays.sort with Comparator
Arrays.sort(employees, Comparator.comparing(Employee::getName));

// Using parallelSort for large arrays
Arrays.parallelSort(employees, Comparator.comparing(Employee::getSalary));
```

## Examples

### Example 1: Sorting a List of Strings by Length

```java
import java.util.*;

public class StringLengthComparator {
 public static void main(String[] args) {
 List<String> words = Arrays.asList("cat", "elephant", "a", "dog", "tiger");

 System.out.println("Original: " + words);

 // Sort by string length
 Collections.sort(words, new Comparator<String>() {
 @Override
 public int compare(String s1, String s2) {
 return Integer.compare(s1.length(), s2.length());
 }
 });

 System.out.println("By length: " + words);

 // Using lambda expression
 words.sort((s1, s2) -> Integer.compare(s1.length(), s2.length()));
 System.out.println("By length (lambda): " + words);
 }
}
```

Output:

```
Original: [cat, elephant, a, dog, tiger]
By length: [a, cat, dog, tiger, elephant]
By length (lambda): [a, cat, dog, tiger, elephant]
```

### Example 2: Multiple Sorting Criteria for Employee Class

```java
import java.util.*;

class Employee {
 private String name;
 private int age;
 private double salary;

 public Employee(String name, int age, double salary) {
 this.name = name;
 this.age = age;
 this.salary = salary;
 }

 // Getters
 public String getName() { return name; }
 public int getAge() { return age; }
 public double getSalary() { return salary; }

 @Override
 public String toString() {
 return name + "(" + age + ")" + salary;
 }
}

public class EmployeeSorting {
 public static void main(String[] args) {
 List<Employee> employees = new ArrayList<>();
 employees.add(new Employee("John", 30, 50000));
 employees.add(new Employee("Alice", 25, 60000));
 employees.add(new Employee("Bob", 30, 45000));
 employees.add(new Employee("Alice", 22, 55000));

 // Sort by name, then age, then salary
 employees.sort(Comparator
 .comparing(Employee::getName)
 .thenComparing(Employee::getAge)
 .thenComparing(Employee::getSalary));

 System.out.println("Sorted by name -> age -> salary:");
 employees.forEach(System.out::println);
 }
}
```

Output:

```
Sorted by name -> age -> salary:
Alice(22)55000.0
Alice(25)60000.0
Bob(30)45000.0
John(30)50000.0
```

### Example 3: Handling Null Values in Sorting

```java
import java.util.*;

public class NullHandling {
 public static void main(String[] args) {
 List<String> names = Arrays.asList("John", null, "Alice", "Bob", null, "Diana");

 // Without null handling - will throw NullPointerException
 try {
 Collections.sort(names, Comparator.comparing(s -> s));
 } catch (NullPointerException e) {
 System.out.println("Exception without null handling");
 }

 // With nullsFirst
 Collections.sort(names, Comparator.nullsFirst(Comparator.naturalOrder()));
 System.out.println("Nulls first: " + names);

 // With nullsLast and reverse order
 names = Arrays.asList("John", null, "Alice", "Bob", null, "Diana");
 Collections.sort(names, Comparator.nullsLast(Comparator.reverseOrder()));
 System.out.println("Nulls last (reverse): " + names);
 }
}
```

Output:

```
Exception without null handling
Nulls first: [null, null, Alice, Bob, Diana, John]
Nulls last (reverse): [John, Diana, Bob, Alice, null, null]
```

## Exam Tips

1. **Remember the return value convention**: compare() returns negative if o1 < o2, zero if o1 == o2, and positive if o1 > o2. Many students confuse this.

2. **Use Integer.compare() for primitive comparisons**: Avoid direct subtraction (a - b) as it can cause overflow with large integers.

3. **Comparator is a functional interface**: This means it can be implemented using lambda expressions, making code concise and readable.

4. **Comparator vs Comparable**: Know when to use each - Comparable for natural ordering within the class, Comparator for external/custom ordering.

5. **TreeSet and TreeMap use Comparator**: Unlike HashSet/HashMap, TreeSet and TreeMap require either Comparable implementation or a Comparator constructor argument.

6. **Method chaining**: Remember that thenComparing() returns a new Comparator, enabling fluent API usage.

7. **Default methods in Java 8**: Know the important default methods like reversed(), thenComparing() and static methods like comparing(), nullsFirst(), nullsLast().

8. **Stability of sorting**: Collections.sort() and Arrays.sort() are stable - equal elements maintain their relative order.
