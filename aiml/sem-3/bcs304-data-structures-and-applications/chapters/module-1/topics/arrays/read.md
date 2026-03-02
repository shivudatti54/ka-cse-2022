# Arrays

## Introduction

Arrays represent one of the most fundamental and widely used data structures in computer science and programming. An array is a collection of elements of the same data type stored at contiguous memory locations, which allows for efficient access to any element using its index. The concept of arrays forms the backbone of many advanced data structures and algorithms, making it essential for any computer science student to master this topic thoroughly.

In the context of the University of Delhi's Computer Science curriculum, arrays serve as the foundation for understanding how data is organized and manipulated in memory. Whether you are implementing simple list operations or building complex algorithmic solutions, arrays provide the underlying mechanism for sequential data storage. The importance of arrays extends beyond theoretical knowledge—they are extensively used in competitive programming, database systems, image processing, scientific computations, and virtually every application that handles collections of data.

This chapter explores arrays in depth, covering single-dimensional arrays, multidimensional arrays, operations on arrays, memory representation, and practical applications. Understanding these concepts is crucial for performing well in both internal assessments and end-semester examinations, as questions on arrays regularly appear in DU question papers.

## Key Concepts

### Definition and Characteristics of Arrays

An array is a homogeneous collection of elements, meaning all elements must be of the same data type (integers, floats, characters, or strings). Each element in an array can be accessed directly by its index, which typically starts from 0 in most programming languages including C, C++, and Java. The size of an array is fixed at the time of declaration and remains constant throughout program execution, though dynamic arrays in languages like Python and Java provide flexibility.

The primary characteristics of arrays include:
- Contiguous memory allocation: All elements are stored in consecutive memory locations
- Fixed size: The number of elements is determined at compile time (for static arrays)
- Random access: Any element can be accessed in constant time O(1) using its index
- Homogeneous elements: All elements share the same data type

### One-Dimensional Arrays

A one-dimensional array (1D array) is the simplest form of array, representing a linear collection of elements. In memory, a 1D array is stored as a continuous block where each element occupies a fixed number of bytes determined by its data type. For example, in a character array, each element occupies 1 byte, while an integer array typically requires 4 bytes per element.

The syntax for declaring a one-dimensional array varies across programming languages. In C language, the declaration `int arr[10];` creates an array named `arr` that can hold 10 integer values. The first element is accessed as `arr[0]`, the second as `arr[1]`, and so forth, with the last element at `arr[9]`.

### Multidimensional Arrays

Multidimensional arrays extend the concept of arrays to multiple dimensions. The most common type is the two-dimensional array (2D array), which can be visualized as a matrix or table with rows and columns. Two-dimensional arrays are extensively used in matrix operations, spreadsheet applications, image representation (as pixel grids), and table data handling.

A two-dimensional array `int matrix[3][4];` declares a matrix with 3 rows and 4 columns, containing 12 total elements. In memory, 2D arrays can be stored using either row-major order (elements stored row by row, as in C and Python) or column-major order (elements stored column by column, as in Fortran and MATLAB). Understanding memory organization is crucial for efficient traversal and access patterns.

Three-dimensional arrays and higher-dimensional arrays are used in more specialized applications such as 3D graphics (representing cubes or volumes), scientific simulations, and complex mathematical computations.

### Memory Representation

The memory representation of arrays is fundamental to understanding their efficiency. In a one-dimensional array, the address of any element can be calculated using the formula:

**Address of arr[i] = Base Address + (i × size of each element)**

For example, if an integer array starts at memory address 1000 and each integer occupies 4 bytes, the element at index 5 will be stored at address 1000 + (5 × 4) = 1020.

In row-major two-dimensional arrays with m rows and n columns, the address calculation becomes:

**Address of arr[i][j] = Base Address + ((i × n) + j) × size of each element**

This formula assumes zero-based indexing for both rows and columns. Students must remember these formulas as they frequently appear in examination questions.

### Dynamic Arrays

Static arrays have fixed sizes, but many real-world applications require arrays that can grow and shrink during program execution. Dynamic arrays, such as `ArrayList` in Java, `list` in Python, and `vector` in C++, address this limitation by automatically resizing when needed. These structures typically maintain an underlying static array and create a larger array when the current one becomes full, copying all elements to the new location—a process that has amortized O(1) time complexity for append operations.

### Array Operations

The fundamental operations performed on arrays include:
- **Traversal**: Visiting each element exactly once
- **Insertion**: Adding a new element at a specified position
- **Deletion**: Removing an element from a specified position
- **Searching**: Finding the position of a target element (linear search, binary search)
- **Sorting**: Arranging elements in a particular order (bubble sort, insertion sort, selection sort)

The time complexity of these operations varies: traversal takes O(n), searching takes O(n) for linear search or O(log n) for binary search on sorted arrays, while insertion and deletion at the beginning take O(n) due to the need to shift elements.

## Examples

### Example 1: Finding the Sum and Maximum Element

Given an integer array of n elements, write a program to find the sum of all elements and the maximum element.

```c
#include <stdio.h>

int main() {
    int n, arr[100];
    
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    printf("Enter %d elements: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    // Calculate sum
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    
    // Find maximum
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    
    printf("Sum: %d\n", sum);
    printf("Maximum: %d\n", max);
    
    return 0;
}
```

**Step-by-step explanation**: First, we accept the number of elements and read them into the array. For finding the sum, we initialize sum to 0 and add each element using a loop. For finding the maximum, we assume the first element is the maximum and compare it with each subsequent element, updating the maximum whenever a larger value is found. The time complexity of this solution is O(n).

### Example 2: Matrix Addition using 2D Arrays

Write a program to add two 3×3 matrices.

```c
#include <stdio.h>

int main() {
    int A[3][3], B[3][3], C[3][3];
    
    printf("Enter elements of first matrix:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            scanf("%d", &A[i][j]);
        }
    }
    
    printf("Enter elements of second matrix:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            scanf("%d", &B[i][j]);
        }
    }
    
    // Addition
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    
    printf("Resultant matrix:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```

**Step-by-step explanation**: We first input both matrices element by element using nested loops. The outer loop iterates through rows while the inner loop iterates through columns. Matrix addition is performed by adding corresponding elements: C[i][j] = A[i][j] + B[i][j]. Finally, we display the result matrix in a formatted manner.

### Example 3: Binary Search Implementation

Implement binary search on a sorted array.

```c
#include <stdio.h>

int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1, mid;
    
    while (low <= high) {
        mid = (low + high) / 2;
        
        if (arr[mid] == key) {
            return mid;  // Element found
        }
        else if (arr[mid] < key) {
            low = mid + 1;  // Search right half
        }
        else {
            high = mid - 1;  // Search left half
        }
    }
    
    return -1;  // Element not found
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 23;
    
    int result = binarySearch(arr, n, key);
    
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    
    return 0;
}
```

**Step-by-step explanation**: Binary search requires a sorted array. We maintain two pointers, low and high, defining the search range. In each iteration, we calculate the middle index and compare the middle element with the key. If they match, we return the index. If the key is greater, we search the right half by updating low = mid + 1. If the key is smaller, we search the left half by updating high = mid - 1. The loop continues until low exceeds high, indicating the element is not present. Binary search has O(log n) time complexity, making it significantly faster than linear search for large datasets.

## Exam Tips

For students appearing in DU semester examinations, the following tips will help maximize scores on array-related questions:

1. **Understand address calculation formulas thoroughly**: Questions on finding memory addresses of array elements are frequently asked in examinations. Remember the formulas for both one-dimensional and two-dimensional arrays and practice numerical problems.

2. **Know time complexities**: Be prepared to state and prove time complexities of various array operations. Linear search is O(n), binary search is O(log n), and insertion/deletion at a specific position is O(n).

3. **Differentiate between row-major and column-major storage**: When answering questions about 2D array memory representation, clearly mention whether the system uses row-major or column-major order, as this affects address calculations.

4. **Practice boundary conditions**: Questions often test understanding of edge cases such as accessing negative indices, exceeding array bounds, and handling empty arrays. Always check for validity of indices before accessing elements.

5. **Master sorting algorithms**: Bubble sort, insertion sort, and selection sort are commonly asked in practical exams. Understand their logic, time complexity (all O(n²) for basic implementations), and space complexity.

6. **Pay attention to indexing**: Remember that array indices start from 0 in most languages. The valid indices for an array of size n are 0 to n-1. Accessing index n leads to buffer overflow.

7. **Understand the difference between static and dynamic arrays**: Be clear about when to use static arrays (fixed size known at compile time) versus dynamic arrays (size determined at runtime using pointers and memory allocation functions).

8. **Practice C programs extensively**: The DU practical examination primarily tests C programming skills. Write clean, well-commented code with proper header files and return statements.