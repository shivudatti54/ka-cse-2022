# ARRAYS IN JAVA

## Introduction

Arrays are fundamental data structures in Java that allow you to store multiple values of the same type in a single variable. Instead of declaring separate variables for each value (such as `int score1`, `score2`, `score3`, and so on), you can declare a single array variable that holds references to multiple elements. Arrays in Java are objects, which means they are stored in the heap memory and come with built-in properties and methods.

The importance of arrays in programming cannot be overstated. They provide efficient access to elements using indices, enable efficient memory usage by storing related data contiguously, and form the foundation for more complex data structures like matrices, lists, and trees. In the context of the University of Delhi Computer Science curriculum, understanding arrays is essential because they appear repeatedly in algorithm design, data manipulation, and problem-solving scenarios that form the core of programming examinations.

Java arrays are zero-indexed, meaning the first element is accessed using index 0, the second element with index 1, and so forth. This systematic indexing, combined with Java's type safety and boundary checking, makes arrays a reliable and powerful tool for handling collections of data in any Java application.

## Key Concepts

### Declaring Array Variables

In Java, an array variable is declared by specifying the type of elements the array will hold, followed by square brackets `[]`. The square brackets can be placed either after the type name or after the variable name. Both syntaxes are valid, though the convention often places them with the type.

```java
int[] numbers;        // Preferred style
int numbers[];        // Also valid but less common
String[] names;
double[] prices;
```

It is important to note that declaring an array variable does not create the array itself. The array object is created using the `new` keyword or through array initialization syntax.

### Creating and Initializing Arrays

Arrays in Java must be created using the `new` keyword or direct initialization. When you create an array with `new`, Java allocates the required memory and initializes the elements to default values (0 for numeric types, `null` for object references, `false` for boolean).

```java
// Creating an array of 5 integers
int[] scores = new int[5];

// Direct initialization with values
int[] marks = {85, 90, 78, 92, 88};

// Creating an array of strings
String[] fruits = new String[3];
fruits[0] = "Apple";
fruits[1] = "Banana";
fruits[2] = "Orange";
```

The `length` property of an array gives the total number of elements it can hold. This is particularly useful when iterating through arrays using loops.

```java
int[] data = {10, 20, 30, 40, 50};
System.out.println(data.length);  // Output: 5
```

### Accessing Array Elements

Array elements are accessed using their index position enclosed in square brackets. Java performs bounds checking at runtime, meaning if you try to access an index outside the valid range (0 to length-1), an `ArrayIndexOutOfBoundsException` is thrown.

```java
int[] numbers = {100, 200, 300, 400, 500};

System.out.println(numbers[0]);   // First element: 100
System.out.println(numbers[2]);  // Third element: 300
System.out.println(numbers[4]);   // Last element: 500
```

### Iterating Through Arrays

The most common way to iterate through arrays is using the `for` loop or the enhanced `for-each` loop introduced in Java 5.

```java
int[] values = {5, 10, 15, 20, 25};

// Using traditional for loop
for (int i = 0; i < values.length; i++) {
    System.out.println("Element at index " + i + ": " + values[i]);
}

// Using enhanced for-each loop
for (int val : values) {
    System.out.println("Value: " + val);
}
```

### Multi-Dimensional Arrays

Java supports multi-dimensional arrays, which are arrays of arrays. The most common is the two-dimensional array, often used to represent matrices or tables.

```java
// Declaring a 2D array
int[][] matrix = new int[3][4];  // 3 rows, 4 columns

// Initializing a 2D array with values
int[][] table = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Accessing elements
System.out.println(table[1][2]);  // Output: 6

// Iterating through a 2D array
for (int i = 0; i < table.length; i++) {
    for (int j = 0; j < table[i].length; j++) {
        System.out.print(table[i][j] + " ");
    }
    System.out.println();
}
```

Jagged arrays are a special type of multi-dimensional array where each row can have a different number of columns.

```java
int[][] jagged = new int[3][];
jagged[0] = new int[2];
jagged[1] = new int[4];
jagged[2] = new int[1];
```

### Arrays as Method Parameters

Arrays can be passed to methods just like other parameters. When you pass an array to a method, you are passing a reference to the original array, meaning any changes made inside the method will affect the original array.

```java
public static void doubleValues(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        arr[i] = arr[i] * 2;
    }
}

public static void main(String[] args) {
    int[] numbers = {3, 6, 9};
    doubleValues(numbers);
    // numbers is now {6, 12, 18}
}
```

### The Arrays Class

Java provides the `java.util.Arrays` class with utility methods for working with arrays. These include sorting, searching, filling, and comparing arrays.

```java
import java.util.Arrays;

int[] arr = {42, 15, 8, 23, 16};

// Sorting the array
Arrays.sort(arr);
System.out.println(Arrays.toString(arr));  // [8, 15, 16, 23, 42]

// Binary search (array must be sorted)
int index = Arrays.binarySearch(arr, 16);  // Returns 2

// Filling an array with a specific value
int[] filled = new int[5];
Arrays.fill(filled, 100);  // [100, 100, 100, 100, 100]

// Comparing arrays
int[] a = {1, 2, 3};
int[] b = {1, 2, 3};
System.out.println(Arrays.equals(a, b));  // true
```

## Examples

### Example 1: Finding the Maximum and Minimum Elements

Write a Java program to find the maximum and minimum values in an integer array.

```java
public class FindMinMax {
    public static void main(String[] args) {
        int[] numbers = {34, 78, 12, 45, 67, 89, 23, 56};
        
        int max = numbers[0];
        int min = numbers[0];
        
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > max) {
                max = numbers[i];
            }
            if (numbers[i] < min) {
                min = numbers[i];
            }
        }
        
        System.out.println("Maximum value: " + max);
        System.out.println("Minimum value: " + min);
    }
}
```

Output:
```
Maximum value: 89
Minimum value: 12
```

### Example 2: Calculating Average and Summing Elements

Create a program that calculates the sum and average of all elements in an array.

```java
public class AverageCalculator {
    public static void main(String[] args) {
        double[] temperatures = {22.5, 24.1, 19.8, 21.3, 25.0, 23.7, 20.5};
        
        double sum = 0;
        for (double temp : temperatures) {
            sum += temp;
        }
        
        double average = sum / temperatures.length;
        
        System.out.println("Total sum: " + sum);
        System.out.println("Average temperature: " + average);
    }
}
```

Output:
```
Total sum: 156.9
Average temperature: 22.414285714285715
```

### Example 3: Matrix Addition Using 2D Arrays

Write a program to add two 3x3 matrices using multi-dimensional arrays.

```java
public class MatrixAddition {
    public static void main(String[] args) {
        int[][] matrixA = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        int[][] matrixB = {
            {9, 8, 7},
            {6, 5, 4},
            {3, 2, 1}
        };
        
        int[][] result = new int[3][3];
        
        // Adding matrices
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                result[i][j] = matrixA[i][j] + matrixB[i][j];
            }
        }
        
        // Displaying result
        System.out.println("Resultant Matrix:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

Output:
```
Resultant Matrix:
10 10 10 
10 10 10 
10 10 10 
```

## Exam Tips

1. Remember that Java arrays are zero-indexed, meaning the first element is always at index 0, not index 1.

2. Always check array bounds before accessing elements to avoid `ArrayIndexOutOfBoundsException` during runtime.

3. The `length` property gives the total capacity of an array, while for strings, `length()` is a method.

4. When initializing arrays with curly braces `{...}`, you must do it at the time of declaration. You cannot separate declaration and initialization with curly braces.

5. Enhanced for-each loop is useful for traversing arrays but cannot be used when you need to modify array elements or know the index position.

6. Arrays are passed by reference in Java, so methods can modify the original array contents.

7. The `Arrays.toString()` method is extremely useful for printing array contents in a readable format during debugging.

8. For multi-dimensional arrays, remember that each row may have a different length in jagged arrays.

9. Default values for uninitialized array elements are: 0 for numeric types, false for boolean, and null for object references.

10. The `Arrays.sort()` method uses the dual-pivot Quicksort for primitive types and merge sort for object types.