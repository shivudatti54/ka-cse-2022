# Arrays in Java

## Introduction

Arrays are fundamental data structures in Java that allow you to store multiple elements of the same type in a single variable. While primitive data types like int, float, and char hold single values, arrays provide a mechanism to organize and manage collections of related data efficiently. In the context of object-oriented programming, arrays represent one of the simplest ways to aggregate data, serving as a building block for more complex data structures like lists, stacks, and queues.

The importance of arrays in Java cannot be overstated. They form the foundation for understanding collections framework, which is essential for competitive programming and software development. Whether you are processing student marks for a university result management system, storing sensor readings from an IoT device, or managing inventory in a retail application, arrays provide the mechanism to organize and manipulate data systematically. Furthermore, understanding arrays is crucial for grasping how memory is allocated and accessed in Java, which is fundamental to writing efficient code.

In this chapter, we will explore one-dimensional and multi-dimensional arrays, their declaration, initialization, and various operations that can be performed on them. We will also examine the relationship between arrays and objects in Java, as arrays in Java are objects that are allocated in heap memory.

## Key Concepts

### One-Dimensional Arrays

A one-dimensional array is a linear collection of elements of the same type. Each element in the array can be accessed by its index, which starts from 0 and goes to (length-1). In Java, arrays have a fixed size once created, meaning you cannot dynamically resize an array.

**Declaration of Arrays:**

In Java, you can declare an array in two ways:

```java
// Method 1: type[] arrayName;
int[] numbers;

// Method 2: type arrayName[];
int numbers[];
```

The first method is generally preferred as it is more readable and aligns with Java conventions. The square brackets can be placed either after the type or after the variable name.

**Instantiation of Arrays:**

Declaration only creates a reference variable that points to null. To actually create the array and allocate memory, you must instantiate it:

```java
// Create an array of 5 integers
numbers = new int[5];

// Declaration and instantiation together
int[] numbers = new int[5];
```

When you create an array using `new`, all elements are automatically initialized to their default values: 0 for numeric types, false for boolean, and null for reference types.

**Initialization with Values:**

You can also initialize an array with specific values at the time of declaration:

```java
int[] numbers = {10, 20, 30, 40, 50};

// Or using the new keyword
int[] numbers = new int[]{10, 20, 30, 40, 50};
```

### Multi-Dimensional Arrays

Multi-dimensional arrays in Java are arrays of arrays. The most common is the two-dimensional array, which can be visualized as a table with rows and columns.

**Declaration and Instantiation:**

```java
// 2D array with 3 rows and 4 columns
int[][] matrix = new int[3][4];

// Declaration with initialization
int[][] matrix = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};
```

In Java, multi-dimensional arrays can be irregular, meaning each row can have a different number of columns:

```java
int[][] irregular = new int[3][];
irregular[0] = new int[2];  // First row has 2 columns
irregular[1] = new int[4];  // Second row has 4 columns
irregular[2] = new int[3];  // Third row has 3 columns
```

### Array Length and Access

The length of an array is available through the `length` property:

```java
int[] numbers = {10, 20, 30, 40, 50};
System.out.println(numbers.length);  // Output: 5
```

Accessing array elements is done through indexing:

```java
int[] numbers = {10, 20, 30, 40, 50};
System.out.println(numbers[0]);  // Output: 10
System.out.println(numbers[4]);  // Output: 50

// Modify an element
numbers[2] = 35;
```

Java performs bounds checking at runtime. If you try to access an index outside the valid range (0 to length-1), an ArrayIndexOutOfBoundsException is thrown.

### Common Array Operations

**Iterating Through Arrays:**

```java
// Traditional for loop
int[] numbers = {10, 20, 30, 40, 50};
for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}

// Enhanced for loop (for-each)
for (int num : numbers) {
    System.out.println(num);
}
```

**Searching in Arrays:**

Linear search checks each element sequentially:

```java
public static int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
```

**Sorting Arrays:**

The Arrays class provides built-in sorting methods:

```java
import java.util.Arrays;

int[] numbers = {50, 20, 40, 10, 30};
Arrays.sort(numbers);  // Sorts in ascending order
System.out.println(Arrays.toString(numbers));  // [10, 20, 30, 40, 50]
```

### Arrays as Objects

In Java, arrays are objects that are dynamically created. They inherit from java.lang.Object and have several characteristics:

- Arrays have a public final length field that specifies the number of elements
- Arrays implement Cloneable and java.io.Serializable interfaces
- Array elements are stored in contiguous memory locations
- The array name is a reference variable pointing to the array object in heap memory

```java
int[] arr = {1, 2, 3};
System.out.println(arr.getClass());        // class [I (int array)
System.out.println(arr instanceof Object); // true
```

## Examples

### Example 1: Student Grade Management System

Consider a scenario where you need to store and analyze marks for five students:

```java
import java.util.Arrays;
import java.util.Scanner;

public class StudentGrades {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] marks = new int[5];
        
        // Input marks for 5 students
        System.out.println("Enter marks for 5 students:");
        for (int i = 0; i < marks.length; i++) {
            marks[i] = scanner.nextInt();
        }
        
        // Calculate total and average
        int total = 0;
        for (int mark : marks) {
            total += mark;
        }
        double average = (double) total / marks.length;
        
        // Find maximum and minimum
        int max = marks[0];
        int min = marks[0];
        for (int i = 1; i < marks.length; i++) {
            if (marks[i] > max) max = marks[i];
            if (marks[i] < min) min = marks[i];
        }
        
        // Sort marks for median calculation
        int[] sortedMarks = Arrays.copyOf(marks, marks.length);
        Arrays.sort(sortedMarks);
        int median = sortedMarks[sortedMarks.length / 2];
        
        // Display results
        System.out.println("\nResults:");
        System.out.println("Total: " + total);
        System.out.println("Average: " + average);
        System.out.println("Maximum: " + max);
        System.out.println("Minimum: " + min);
        System.out.println("Median: " + median);
        
        scanner.close();
    }
}
```

This example demonstrates array declaration, input handling, iteration, and using the Arrays utility class for sorting.

### Example 2: Matrix Addition using 2D Arrays

```java
public class MatrixAddition {
    public static void main(String[] args) {
        // Initialize two 3x3 matrices
        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        int[][] matrix2 = {
            {9, 8, 7},
            {6, 5, 4},
            {3, 2, 1}
        };
        
        // Create result matrix
        int[][] result = new int[3][3];
        
        // Add matrices
        for (int i = 0; i < matrix1.length; i++) {
            for (int j = 0; j < matrix1[i].length; j++) {
                result[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }
        
        // Print result
        System.out.println("Result Matrix:");
        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result[i].length; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

Output:
```
Result Matrix:
10 10 10 
10 10 10 
10 10 10 
```

### Example 3: Binary Search Implementation

Binary search is efficient for sorted arrays with O(log n) time complexity:

```java
import java.util.Arrays;

public class BinarySearchDemo {
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;  // Prevents integer overflow
            
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;  // Element not found
    }
    
    public static void main(String[] args) {
        int[] sortedArray = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 23;
        
        int result = binarySearch(sortedArray, target);
        
        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found in the array");
        }
        
        // Using built-in binary search
        int builtInResult = Arrays.binarySearch(sortedArray, target);
        System.out.println("Built-in binary search result: " + builtInResult);
    }
}
```

Output:
```
Element found at index: 5
Built-in binary search result: 5
```

## Exam Tips

For DU semester examinations, keep the following points in mind:

1. **Array Indexing**: Remember that Java array indices start from 0, not 1. The last valid index is always (length - 1).

2. **Default Values**: When an array is created using `new`, numeric arrays are initialized to 0, boolean to false, and reference types to null. This is frequently tested in exams.

3. **Array Declaration Styles**: Both `int[] arr` and `int arr[]` are valid, but the first style is recommended. Know the difference between declaration, instantiation, and initialization.

4. **Bounds Checking**: Java throws ArrayIndexOutOfBoundsException if you access an invalid index. Always ensure your loop conditions are correct.

5. **Arrays.toString() and Arrays.deepToString()**: Use Arrays.toString() for 1D arrays and Arrays.deepToString() for multi-dimensional arrays to print them correctly.

6. **Array Length vs String Length**: Arrays use `.length` (a property), while Strings use `.length()` (a method). This distinction is commonly tested.

7. **Enhanced for Loop Limitations**: The enhanced for-each loop cannot modify array elements directly (the loop variable is a copy). Use traditional for loops when you need to modify elements.

8. **Memory Concept**: Arrays in Java are objects stored in heap memory. The array reference variable is stored in the stack.

9. **Jagged Arrays**: Remember that multi-dimensional arrays in Java can have different row lengths (jagged arrays), unlike in some other languages.

10. **Time Complexity**: Be familiar with O(n) for linear search and O(n log n) for sorting. Binary search requires a sorted array and has O(log n) complexity.