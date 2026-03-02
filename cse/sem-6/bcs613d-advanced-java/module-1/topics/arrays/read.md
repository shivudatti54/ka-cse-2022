# Arrays in Java

## Introduction to Java Arrays

An **array** in Java is a container object that holds a fixed number of values of a single type. Arrays are fundamental data structures in Java that allow you to store multiple values of the same type in a single variable, making it easier to organize and manipulate related data.

```java
// Array declaration and initialization
int[] numbers = {10, 20, 30, 40, 50};
String[] names = {"Alice", "Bob", "Charlie"};
```

## Key Characteristics of Java Arrays

| Property              | Description                                  |
| --------------------- | -------------------------------------------- |
| **Fixed Size**        | Once created, array size cannot be changed   |
| **Homogeneous**       | All elements must be of the same type        |
| **Index-Based**       | Elements accessed using zero-based indexing  |
| **Object Type**       | Arrays are objects in Java                   |
| **Contiguous Memory** | Elements stored in adjacent memory locations |

## Array Declaration and Creation

### Method 1: Declaration and Initialization Separately

```java
// Declare array
int[] numbers;

// Create array with size 5
numbers = new int[5];

// Initialize elements
numbers[0] = 10;
numbers[1] = 20;
numbers[2] = 30;
numbers[3] = 40;
numbers[4] = 50;
```

### Method 2: Declaration with Initialization

```java
// All in one line
int[] numbers = {10, 20, 30, 40, 50};

// Using new keyword
String[] fruits = new String[]{"Apple", "Banana", "Orange"};
```

### Method 3: Anonymous Array

```java
// Creating array without reference variable
printArray(new int[]{1, 2, 3, 4, 5});
```

## Types of Arrays in Java

### Single-Dimensional Arrays

```java
// Integer array
int[] scores = new int[5];
scores[0] = 85;
scores[1] = 92;
scores[2] = 78;

// String array
String[] days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};

// Double array
double[] prices = {19.99, 29.99, 39.99, 49.99};
```

### Multi-Dimensional Arrays

#### Two-Dimensional Arrays (Matrix)

```java
// Declare and create 2D array
int[][] matrix = new int[3][4]; // 3 rows, 4 columns

// Initialize 2D array
int[][] table = {
 {1, 2, 3, 4},
 {5, 6, 7, 8},
 {9, 10, 11, 12}
};

// Access elements
int value = table[1][2]; // Access element at row 1, column 2 (value = 7)
```

#### Jagged Arrays (Arrays of Arrays)

```java
// Each row can have different number of columns
int[][] jagged = new int[3][];
jagged[0] = new int[2]; // First row has 2 columns
jagged[1] = new int[4]; // Second row has 4 columns
jagged[2] = new int[3]; // Third row has 3 columns

// Example with initialization
int[][] triangle = {
 {1},
 {2, 3},
 {4, 5, 6},
 {7, 8, 9, 10}
};
```

## Common Array Operations

### Traversing Arrays

```java
int[] numbers = {10, 20, 30, 40, 50};

// Using for loop
for (int i = 0; i < numbers.length; i++) {
 System.out.println(numbers[i]);
}

// Using enhanced for loop (for-each)
for (int num : numbers) {
 System.out.println(num);
}
```

### Finding Array Length

```java
int[] arr = {1, 2, 3, 4, 5};
int size = arr.length; // Note: length is a property, not a method
System.out.println("Array length: " + size); // Output: 5
```

### Copying Arrays

```java
int[] original = {1, 2, 3, 4, 5};

// Method 1: Using clone()
int[] copy1 = original.clone();

// Method 2: Using System.arraycopy()
int[] copy2 = new int[5];
System.arraycopy(original, 0, copy2, 0, original.length);

// Method 3: Using Arrays.copyOf()
int[] copy3 = Arrays.copyOf(original, original.length);
```

### Sorting Arrays

```java
import java.util.Arrays;

int[] numbers = {5, 2, 8, 1, 9};

// Sort in ascending order
Arrays.sort(numbers);
System.out.println(Arrays.toString(numbers)); // [1, 2, 5, 8, 9]

// Sort a portion of array
int[] arr = {9, 3, 7, 1, 5};
Arrays.sort(arr, 1, 4); // Sort from index 1 to 3
System.out.println(Arrays.toString(arr)); // [9, 1, 3, 7, 5]
```

### Searching Arrays

```java
import java.util.Arrays;

int[] numbers = {1, 3, 5, 7, 9, 11};

// Binary search (array must be sorted)
int index = Arrays.binarySearch(numbers, 7);
System.out.println("Found at index: " + index); // Output: 3

// Linear search (manual implementation)
public static int linearSearch(int[] arr, int target) {
 for (int i = 0; i < arr.length; i++) {
 if (arr[i] == target) {
 return i;
 }
 }
 return -1; // Not found
}
```

## Arrays Class Utility Methods

The `java.util.Arrays` class provides many useful static methods for array manipulation:

```java
import java.util.Arrays;

int[] arr = {5, 2, 8, 1, 9};

// Convert array to string
String str = Arrays.toString(arr);
System.out.println(str); // [5, 2, 8, 1, 9]

// Fill array with specific value
int[] filled = new int[5];
Arrays.fill(filled, 10);
System.out.println(Arrays.toString(filled)); // [10, 10, 10, 10, 10]

// Compare arrays for equality
int[] arr1 = {1, 2, 3};
int[] arr2 = {1, 2, 3};
boolean equal = Arrays.equals(arr1, arr2);
System.out.println(equal); // true
```

## Array of Objects

```java
// Array of String objects
String[] names = new String[3];
names[0] = "Alice";
names[1] = "Bob";
names[2] = "Charlie";

// Array of custom objects
class Student {
 String name;
 int rollNo;

 Student(String name, int rollNo) {
 this.name = name;
 this.rollNo = rollNo;
 }
}

Student[] students = new Student[3];
students[0] = new Student("Alice", 101);
students[1] = new Student("Bob", 102);
students[2] = new Student("Charlie", 103);

// Access student information
System.out.println(students[0].name); // Alice
```

## Common Array Pitfalls

### ArrayIndexOutOfBoundsException

```java
int[] arr = {1, 2, 3, 4, 5};

// This will throw ArrayIndexOutOfBoundsException
// arr[5] = 10; // Error: Valid indices are 0-4

// Correct way with bounds checking
if (index >= 0 && index < arr.length) {
 arr[index] = value;
}
```

### NullPointerException

```java
int[] arr = null;

// This will throw NullPointerException
// System.out.println(arr.length);

// Correct way with null check
if (arr != null) {
 System.out.println(arr.length);
}
```

## Arrays vs Collections

| Feature         | Arrays                          | Collections              |
| --------------- | ------------------------------- | ------------------------ |
| **Size**        | Fixed size                      | Dynamic size             |
| **Type**        | Can hold primitives and objects | Only hold objects        |
| **Performance** | Faster access                   | Slightly slower          |
| **Features**    | Basic operations                | Rich set of methods      |
| **Type Safety** | Not parameterized               | Parameterized (generics) |

## Practical Example: Student Grade Management

```java
import java.util.Arrays;
import java.util.Scanner;

public class GradeManager {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);

 // Create array for student grades
 System.out.print("Enter number of students: ");
 int n = sc.nextInt();
 int[] grades = new int[n];

 // Input grades
 for (int i = 0; i < n; i++) {
 System.out.print("Enter grade for student " + (i + 1) + ": ");
 grades[i] = sc.nextInt();
 }

 // Calculate average
 double average = calculateAverage(grades);
 System.out.println("Average grade: " + average);

 // Find highest and lowest
 Arrays.sort(grades);
 System.out.println("Lowest grade: " + grades[0]);
 System.out.println("Highest grade: " + grades[n - 1]);

 // Display sorted grades
 System.out.println("Sorted grades: " + Arrays.toString(grades));

 sc.close();
 }

 static double calculateAverage(int[] arr) {
 int sum = 0;
 for (int grade : arr) {
 sum += grade;
 }
 return (double) sum / arr.length;
 }
}
```

## Command-Line Arguments

Java's `main` method receives command-line arguments as a String array:

```java
public class CommandLineDemo {
 public static void main(String[] args) {
 System.out.println("Number of arguments: " + args.length);

 for (int i = 0; i < args.length; i++) {
 System.out.println("Argument " + i + ": " + args[i]);
 }
 }
}

// Run: java CommandLineDemo Hello World 123
// Output:
// Number of arguments: 3
// Argument 0: Hello
// Argument 1: World
// Argument 2: 123
```

## Exam Tips

1. **Remember Zero-Based Indexing**: First element is at index 0, last at length-1
2. **Array Length**: Use `.length` (property, not a method) to get array size
3. **Fixed Size**: Arrays cannot grow or shrink after creation
4. **Default Values**: int arrays initialize to 0, boolean to false, objects to null
5. **Arrays.toString()**: Use this to print array contents easily
6. **Enhanced For Loop**: Best for read-only traversal
7. **ArrayIndexOutOfBoundsException**: Always check bounds before accessing
8. **Multi-dimensional Arrays**: Java supports arrays of arrays (jagged arrays)

## Further Reading

For more information on Java arrays and advanced topics like ArrayList, refer to the official Java documentation and advanced Java collections framework materials.
