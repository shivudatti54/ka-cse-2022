# Arrays in Java


## Table of Contents

- [Arrays in Java](#arrays-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Single-Dimensional Arrays](#single-dimensional-arrays)
  - [Multi-Dimensional Arrays](#multi-dimensional-arrays)
  - [Array Operations](#array-operations)
  - [Common Array Methods](#common-array-methods)
  - [Arrays of Objects](#arrays-of-objects)
- [Examples](#examples)
  - [Example 1: Finding Maximum and Minimum in an Array](#example-1-finding-maximum-and-minimum-in-an-array)
  - [Example 2: Matrix Addition using 2D Arrays](#example-2-matrix-addition-using-2d-arrays)
  - [Example 3: Searching an Element (Linear Search)](#example-3-searching-an-element-linear-search)
- [Exam Tips](#exam-tips)

## Introduction

Arrays are fundamental data structures in Java that allow you to store multiple values of the same type in a single variable. Instead of declaring separate variables for each value (like int score1, score2, score3...), arrays enable you to create a collection of elements that can be accessed using an index. This makes arrays essential for managing lists of related data efficiently in any Java application.

In the context of Object-Oriented Programming with Java, understanding arrays is crucial because they form the foundation for more complex data structures and collections. Arrays in Java are objects that store primitive data types or references to objects. They provide random access to elements, meaning you can directly access any element in constant time using its index, which is a significant advantage for performance-critical applications.

For the university's BCS306A course, arrays are covered in Module 1 as they establish the groundwork for understanding how Java handles collections of data. This topic appears frequently in university examinations and forms the basis for understanding more advanced topics like ArrayList, sorting algorithms, and matrix operations.

## Key Concepts

### Single-Dimensional Arrays

A single-dimensional array is a linear collection of elements of the same type. In Java, arrays have a fixed size that is determined at the time of creation and cannot be changed during runtime.

**Declaration of Arrays:**

There are multiple ways to declare an array in Java:

```java
// Method 1: Declaration with size
int[] numbers = new int[5];

// Method 2: Declaration with initialization
int[] numbers = {1, 2, 3, 4, 5};

// Method 3: Traditional approach
int numbers[] = new int[5];
```

The first method creates an array of 5 integers with default values (0 for int). The second method creates and initializes the array with specific values. The third method uses the C-style declaration, though the first method is preferred in Java.

**Array Indexing:**

Array indices in Java start from 0 and go up to (length-1). For example, if you have an array of size 5, valid indices are 0, 1, 2, 3, and 4. Attempting to access an index outside this range results in an ArrayIndexOutOfBoundsException.

**Default Initializations:**

When arrays are created using the `new` keyword, primitive numeric arrays are automatically initialized to zero, boolean arrays to false, and reference type arrays to null.

### Multi-Dimensional Arrays

Multi-dimensional arrays are arrays of arrays. The most common type is the two-dimensional array, which is essentially a table with rows and columns.

**Declaration and Initialization:**

```java
// Method 1: 2D array with specified dimensions
int[][] matrix = new int[3][4]; // 3 rows, 4 columns

// Method 2: 2D array with explicit values
int[][] matrix = {
 {1, 2, 3, 4},
 {5, 6, 7, 8},
 {9, 10, 11, 12}
};

// Method 3: Jagged array (rows with different column lengths)
int[][] jagged = new int[3][];
jagged[0] = new int[2];
jagged[1] = new int[4];
jagged[2] = new int[1];
```

**Memory Representation:**

In Java, 2D arrays are stored as arrays of arrays. Each row can be thought of as a separate 1D array. This is important because it allows for jagged arrays where each row can have a different number of columns.

### Array Operations

**Traversing Arrays:**

Using for loop:

```java
int[] numbers = {10, 20, 30, 40, 50};
for (int i = 0; i < numbers.length; i++) {
 System.out.println("Element at index " + i + ": " + numbers[i]);
}
```

Using enhanced for loop (for-each):

```java
for (int num : numbers) {
 System.out.println(num);
}
```

**Finding Array Length:**

The `length` property gives the number of elements in an array:

```java
int[] arr = {1, 2, 3, 4, 5};
int len = arr.length; // Returns 5
```

### Common Array Methods

Java provides several utility methods through the Arrays class (java.util.Arrays):

**Sorting:**

```java
import java.util.Arrays;
int[] numbers = {5, 2, 8, 1, 9};
Arrays.sort(numbers); // Sorts in ascending order
```

**Binary Search:**

```java
int[] arr = {1, 2, 3, 4, 5};
int index = Arrays.binarySearch(arr, 3); // Returns 2
```

**Filling Arrays:**

```java
int[] arr = new int[5];
Arrays.fill(arr, 10); // Fills all elements with 10
```

**Converting to String:**

```java
int[] arr = {1, 2, 3};
String str = Arrays.toString(arr); // Returns "[1, 2, 3]"
```

**Comparing Arrays:**

```java
int[] arr1 = {1, 2, 3};
int[] arr2 = {1, 2, 3};
boolean equal = Arrays.equals(arr1, arr2); // Returns true
```

### Arrays of Objects

Arrays can hold not only primitive types but also object references:

```java
String[] names = new String[3];
names[0] = "Alice";
names[1] = "Bob";
names[2] = "Charlie";

Student[] students = new Student[2];
students[0] = new Student("John", 101);
students[1] = new Student("Jane", 102);
```

## Examples

### Example 1: Finding Maximum and Minimum in an Array

**Problem:** Write a Java program to find the maximum and minimum elements in an integer array.

**Solution:**

```java
import java.util.Scanner;

public class FindMinMax {
 public static void main(String[] args) {
 Scanner scanner = new Scanner(System.in);

 System.out.print("Enter the number of elements: ");
 int n = scanner.nextInt();

 int[] arr = new int[n];

 System.out.println("Enter " + n + " elements:");
 for (int i = 0; i < n; i++) {
 arr[i] = scanner.nextInt();
 }

 int max = arr[0];
 int min = arr[0];

 for (int i = 1; i < n; i++) {
 if (arr[i] > max) {
 max = arr[i];
 }
 if (arr[i] < min) {
 min = arr[i];
 }
 }

 System.out.println("Maximum element: " + max);
 System.out.println("Minimum element: " + min);

 scanner.close();
 }
}
```

**Step-by-step explanation:**

1. First, we create a Scanner object to take user input
2. We read the number of elements and create an array of that size
3. We initialize max and min with the first element (arr[0])
4. We iterate from index 1 to n-1, comparing each element with current max and min
5. If an element is greater than max, we update max; if less than min, we update min
6. Finally, we print the results

### Example 2: Matrix Addition using 2D Arrays

**Problem:** Write a Java program to add two 3x3 matrices.

**Solution:**

```java
import java.util.Scanner;

public class MatrixAddition {
 public static void main(String[] args) {
 Scanner scanner = new Scanner(System.in);

 int[][] matrix1 = new int[3][3];
 int[][] matrix2 = new int[3][3];
 int[][] sum = new int[3][3];

 System.out.println("Enter elements of first matrix:");
 for (int i = 0; i < 3; i++) {
 for (int j = 0; j < 3; j++) {
 matrix1[i][j] = scanner.nextInt();
 }
 }

 System.out.println("Enter elements of second matrix:");
 for (int i = 0; i < 3; i++) {
 for (int j = 0; j < 3; j++) {
 matrix2[i][j] = scanner.nextInt();
 }
 }

 // Adding matrices
 for (int i = 0; i < 3; i++) {
 for (int j = 0; j < 3; j++) {
 sum[i][j] = matrix1[i][j] + matrix2[i][j];
 }
 }

 System.out.println("Sum of the two matrices:");
 for (int i = 0; i < 3; i++) {
 for (int j = 0; j < 3; j++) {
 System.out.print(sum[i][j] + " ");
 }
 System.out.println();
 }

 scanner.close();
 }
}
```

**Step-by-step explanation:**

1. We declare three 2D arrays: two for input matrices and one for the result
2. We use nested for loops to accept elements for the first matrix
3. We use another nested loop to accept elements for the second matrix
4. We perform element-by-element addition using nested loops
5. Finally, we display the result matrix using nested loops

### Example 3: Searching an Element (Linear Search)

**Problem:** Write a Java program to search for an element in an array and display its position.

**Solution:**

```java
import java.util.Scanner;

public class LinearSearch {
 public static void main(String[] args) {
 int[] arr = {12, 45, 67, 89, 23, 56, 91};
 int key;
 int position = -1;

 Scanner scanner = new Scanner(System.in);
 System.out.print("Enter the element to search: ");
 key = scanner.nextInt();

 for (int i = 0; i < arr.length; i++) {
 if (arr[i] == key) {
 position = i;
 break;
 }
 }

 if (position != -1) {
 System.out.println("Element " + key + " found at index " + position);
 } else {
 System.out.println("Element " + key + " not found in the array");
 }

 scanner.close();
 }
}
```

**Step-by-step explanation:**

1. We create an array with predefined values
2. We accept the search key from the user
3. We initialize position to -1 (indicating not found)
4. We iterate through each element using a for loop
5. If the current element matches the key, we store the index in position and break
6. After the loop, we check if position was updated and display the appropriate message

## Exam Tips

1. **Remember Array Indexing:** Array indices always start from 0 in Java. A common mistake is trying to access index 1 as the first element. The valid range is 0 to (length-1).

2. **Understand Array Declaration Syntax:** The preferred way to declare arrays in Java is `int[] arr` rather than `int arr[]`. This is because the type is "int array" not "int."

3. **Default Values are Important:** When you create an array with `new`, numeric arrays get 0, boolean arrays get false, and reference arrays get null. This is frequently tested in exams.

4. **Array Length vs String Length:** Remember that for arrays, you use `.length` (a property), while for Strings, you use `.length()` (a method).

5. **ArrayIndexOutOfBoundsException:** This exception occurs when you try to access an index outside the valid range. Always ensure your loop condition is `i < array.length`, not `i <= array.length`.

6. **Jagged Arrays in 2D:** Remember that in Java, 2D arrays don't need to be rectangular. Each row can have a different number of columns, which is called a jagged array.

7. **Enhanced for Loop Limitations:** The enhanced for loop (for-each) cannot be used when you need to modify array elements or when you need the index. Use traditional for loop in such cases.

8. **Arrays Class Utility Methods:** Know how to use Arrays.sort(), Arrays.binarySearch(), Arrays.fill(), and Arrays.toString() as they simplify many array operations.

9. **Memory Representation:** Understand that arrays are objects stored in heap memory, and the array variable is a reference to this memory location.

10. **Copying Arrays:** To copy arrays, you can use System.arraycopy(), Arrays.copyOf(), or clone(). Simply assigning one array to another doesn't create a copy—it creates another reference to the same array.
