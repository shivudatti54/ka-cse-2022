# Collection Algorithms and Arrays

## Introduction to Collection Algorithms

The Java Collections Framework provides a set of powerful, reusable algorithms that operate on collections. These algorithms are defined as static methods in the `Collections` class and perform common operations such as sorting, searching, shuffling, and finding extreme values. Understanding these algorithms is crucial for efficient data manipulation in Java applications.

### Key Characteristics of Collection Algorithms

- **Polymorphic**: Work on any collection that implements the appropriate interface
- **Efficient**: Implement optimized algorithms with good time complexity
- **Type-safe**: Use generics for compile-time type checking
- **Convenient**: Provide ready-to-use solutions for common operations

## Commonly Used Collection Algorithms

### Sorting Collections

The `Collections.sort()` method is used to sort lists that implement the `List` interface. It uses a modified mergesort algorithm that offers O(n log n) performance.

```java
List<Integer> numbers = Arrays.asList(5, 2, 8, 1, 9);
Collections.sort(numbers); // Natural ordering
System.out.println(numbers); // [1, 2, 5, 8, 9]

List<String> names = Arrays.asList("John", "Alice", "Bob");
Collections.sort(names); // Alphabetical order
System.out.println(names); // [Alice, Bob, John]
```

For custom sorting, you can provide a `Comparator`:

```java
Collections.sort(names, Comparator.reverseOrder());
System.out.println(names); // [John, Bob, Alice]

// Custom comparator for string length
Collections.sort(names, Comparator.comparingInt(String::length));
```

### Searching in Collections

The `Collections.binarySearch()` method performs binary search on sorted lists with O(log n) time complexity.

```java
List<Integer> sortedList = Arrays.asList(1, 3, 5, 7, 9);
int index = Collections.binarySearch(sortedList, 5);
System.out.println(index); // 2 (zero-based index)

index = Collections.binarySearch(sortedList, 4);
System.out.println(index); // Negative value: -3 (insertion point would be index 2)
```

**Important**: The list must be sorted before using binary search, otherwise the results are undefined.

### Shuffling Collections

The `Collections.shuffle()` method randomly permutes the specified list.

```java
List<Integer> cards = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
Collections.shuffle(cards);
System.out.println(cards); // Random order each time
```

### Finding Extreme Values

```java
List<Integer> numbers = Arrays.asList(4, 2, 9, 1, 5);
Integer min = Collections.min(numbers); // 1
Integer max = Collections.max(numbers); // 9

// With custom comparator
List<String> words = Arrays.asList("apple", "banana", "cherry");
String shortest = Collections.min(words, Comparator.comparingInt(String::length)); // "apple"
String longest = Collections.max(words, Comparator.comparingInt(String::length)); // "banana"
```

### Frequency and Disjoint Operations

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 4, 2, 5);
int frequency = Collections.frequency(numbers, 2); // 3

List<Integer> list1 = Arrays.asList(1, 2, 3);
List<Integer> list2 = Arrays.asList(4, 5, 6);
boolean disjoint = Collections.disjoint(list1, list2); // true
```

### Copying and Filling Collections

```java
List<String> source = Arrays.asList("A", "B", "C");
List<String> destination = Arrays.asList("X", "Y", "Z");
Collections.copy(destination, source);
System.out.println(destination); // [A, B, C]

List<Integer> numbers = new ArrayList<>(Collections.nCopies(5, 0));
Collections.fill(numbers, 42);
System.out.println(numbers); // [42, 42, 42, 42, 42]
```

## The Arrays Utility Class

The `Arrays` class provides static methods for manipulating arrays (sorting, searching, comparing, filling, etc.). It serves a similar purpose for arrays as the `Collections` class does for collections.

### Sorting Arrays

```java
int[] numbers = {5, 2, 8, 1, 9};
Arrays.sort(numbers); // [1, 2, 5, 8, 9]

String[] names = {"John", "Alice", "Bob"};
Arrays.sort(names); // [Alice, Bob, John]

// Partial array sorting
int[] partialArray = {5, 2, 8, 1, 9, 3, 7};
Arrays.sort(partialArray, 2, 5); // Sort from index 2 (inclusive) to 5 (exclusive)
// Result: [5, 2, 1, 8, 9, 3, 7]
```

### Binary Search in Arrays

```java
int[] sortedArray = {1, 3, 5, 7, 9};
int index = Arrays.binarySearch(sortedArray, 5); // 2
index = Arrays.binarySearch(sortedArray, 4); // -3
```

### Comparing Arrays

```java
int[] array1 = {1, 2, 3};
int[] array2 = {1, 2, 3};
int[] array3 = {1, 2, 4};

boolean equal1 = Arrays.equals(array1, array2); // true
boolean equal2 = Arrays.equals(array1, array3); // false

// Deep comparison for multi-dimensional arrays
int[][] multi1 = {{1, 2}, {3, 4}};
int[][] multi2 = {{1, 2}, {3, 4}};
boolean deepEqual = Arrays.deepEquals(multi1, multi2); // true
```

### Filling Arrays

```java
int[] numbers = new int[5];
Arrays.fill(numbers, 42); // [42, 42, 42, 42, 42]

// Partial filling
int[] partialFill = new int[7];
Arrays.fill(partialFill, 2, 5, 99); // Fill from index 2 to 4 with value 99
// Result: [0, 0, 99, 99, 99, 0, 0]
```

### Converting Arrays to Strings

```java
int[] numbers = {1, 2, 3, 4, 5};
String arrayString = Arrays.toString(numbers);
// "[1, 2, 3, 4, 5]"

int[][] multiArray = {{1, 2}, {3, 4}};
String deepString = Arrays.deepToString(multiArray);
// "[[1, 2], [3, 4]]"
```

### Converting Arrays to Lists

```java
String[] namesArray = {"Alice", "Bob", "Charlie"};
List<String> namesList = Arrays.asList(namesArray);

// Note: The returned list is fixed-size and backed by the original array
namesList.set(0, "Alex"); // Modifies both list and array
// namesArray[0] is now "Alex"

// namesList.add("David"); // throws UnsupportedOperationException
// namesList.remove(0); // throws UnsupportedOperationException
```

## Performance Comparison

| Operation     | Collections (List)           | Arrays                  | Time Complexity |
| ------------- | ---------------------------- | ----------------------- | --------------- |
| Sort          | `Collections.sort()`         | `Arrays.sort()`         | O(n log n)      |
| Binary Search | `Collections.binarySearch()` | `Arrays.binarySearch()` | O(log n)        |
| Shuffle       | `Collections.shuffle()`      | Manual implementation   | O(n)            |
| Min/Max       | `Collections.min()/max()`    | Manual iteration        | O(n)            |
| Fill          | `Collections.fill()`         | `Arrays.fill()`         | O(n)            |

## Algorithm Visualization

### Binary Search Process

```
Array: [1, 3, 5, 7, 9, 11, 13]
Search for: 7

Step 1: low=0, high=6, mid=3 → value=7 → found!
```

```
Search for: 6

Step 1: low=0, high=6, mid=3 → value=7 > 6 → search left
Step 2: low=0, high=2, mid=1 → value=3 < 6 → search right
Step 3: low=2, high=2, mid=2 → value=5 < 6 → not found
Return: -(3) - 1 = -4
```

### Sorting Algorithm Comparison

```
Merge Sort (Collections.sort()):
[5, 2, 8, 1, 9] → Divide → [5, 2] [8, 1, 9] → Sort halves → [2, 5] [1, 8, 9] → Merge → [1, 2, 5, 8, 9]

Quick Sort (Arrays.sort() for primitives):
[5, 2, 8, 1, 9] → Pivot=5 → [2, 1] [5] [8, 9] → Sort subarrays → [1, 2] [5] [8, 9] → Combine → [1, 2, 5, 8, 9]
```

## Practical Examples

### Example 1: Student Grade Management

```java
class Student implements Comparable<Student> {
 String name;
 int grade;

 public Student(String name, int grade) {
 this.name = name;
 this.grade = grade;
 }

 @Override
 public int compareTo(Student other) {
 return Integer.compare(this.grade, other.grade);
 }

 @Override
 public String toString() {
 return name + ": " + grade;
 }
}

// Usage
List<Student> students = Arrays.asList(
 new Student("Alice", 85),
 new Student("Bob", 92),
 new Student("Charlie", 78)
);

Collections.sort(students); // Sort by grade
System.out.println("Sorted by grade: " + students);

// Sort by name using comparator
Collections.sort(students, Comparator.comparing(s -> s.name));
System.out.println("Sorted by name: " + students);
```

### Example 2: Deck of Cards

```java
List<String> deck = new ArrayList<>();
String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};
String[] ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};

for (String suit : suits) {
 for (String rank : ranks) {
 deck.add(rank + " of " + suit);
 }
}

Collections.shuffle(deck);
System.out.println("Shuffled deck: " + deck.subList(0, 5));

Collections.sort(deck);
System.out.println("Sorted deck: " + deck.subList(0, 5));
```

## Exam Tips

1. **Remember the class names**: `Collections` for collection operations, `Arrays` for array operations
2. **Binary search prerequisite**: Always ensure the collection/array is sorted before using binary search
3. **List from Arrays.asList()**: Remember it's fixed-size and backed by the original array
4. **Time complexity**: Know the Big-O notation for common operations (sort: O(n log n), search: O(log n), etc.)
5. **Comparator usage**: Practice creating custom comparators for complex sorting scenarios
6. **Multi-dimensional arrays**: Use `Arrays.deepEquals()` and `Arrays.deepToString()` for nested arrays
7. **Common pitfalls**:

- Modifying lists returned by `Arrays.asList()` throws UnsupportedOperationException
- Using binary search on unsorted data gives undefined results
- `Collections.sort()` only works with Lists, not other Collections
