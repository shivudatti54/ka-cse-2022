# Arrays as a Fundamental Data Structure


## Table of Contents

- [Arrays as a Fundamental Data Structure](#arrays-as-a-fundamental-data-structure)
- [1. Introduction and Formal Definition](#1-introduction-and-formal-definition)
  - [1.1 Mathematical Definition](#11-mathematical-definition)
- [2. Array as an Abstract Data Type (ADT)](#2-array-as-an-abstract-data-type-adt)
  - [2.1 Array ADT Specification](#21-array-adt-specification)
- [3. Declaration and Initialization in C](#3-declaration-and-initialization-in-c)
  - [3.1 Static Allocation (Stack Memory)](#31-static-allocation-stack-memory)
  - [3.2 Dynamic Allocation (Heap Memory)](#32-dynamic-allocation-heap-memory)
- [4. Memory Representation and Address Calculation](#4-memory-representation-and-address-calculation)
  - [4.1 Contiguous Memory Layout](#41-contiguous-memory-layout)
  - [4.2 Formal Proof: Address Calculation Theorem](#42-formal-proof-address-calculation-theorem)
  - [4.3 Worked Examples](#43-worked-examples)
- [5. Array Operations: Implementation and Complexity Analysis](#5-array-operations-implementation-and-complexity-analysis)
  - [5.1 Traversal Operation](#51-traversal-operation)
  - [5.2 Insertion Operation](#52-insertion-operation)
  - [5.3 Deletion Operation](#53-deletion-operation)
  - [5.4 Search Operations](#54-search-operations)
  - [5.5 Complexity Summary Table](#55-complexity-summary-table)
- [6. Multidimensional Arrays](#6-multidimensional-arrays)
  - [6.1 Two-Dimensional Arrays in Memory](#61-two-dimensional-arrays-in-memory)
  - [6.2 Worked Example: 2D Array Address Calculation](#62-worked-example-2d-array-address-calculation)
- [7. Dynamic Array Resizing and Amortized Analysis](#7-dynamic-array-resizing-and-amortized-analysis)
  - [7.1 Growth Strategy](#71-growth-strategy)
  - [7.2 Amortized Analysis](#72-amortized-analysis)
- [8. Conclusion](#8-conclusion)

## 1. Introduction and Formal Definition

An **array** constitutes a fundamental linear data structure in computer science, characterized by the storage of a finite, fixed number of elements of the **same primitive or composite data type** in **contiguous memory locations**. This contiguity of storage represents a critical distinguishing characteristic that differentiates arrays from other linear data structures such as linked lists, wherein elements may be dispersed throughout memory in a non-sequential manner.

The defining operational property of arrays is **random access** — any element can be accessed directly in constant time O(1) by computing its memory address from its index through a simple arithmetic formula. This characteristic provides arrays with their exceptional performance profile for access operations, establishing them as the preferred data structure for scenarios requiring frequent element retrieval by position.

### 1.1 Mathematical Definition

A one-dimensional array A of size n is formally defined as a finite ordered sequence of n elements:

```
A = {A[0], A[1], A[2], ..., A[n-1]}
```

where each element A[i] (0 ≤ i < n) belongs to the same data type T, and the index i is a non-negative integer that uniquely identifies the position of an element within the array. The size n remains fixed subsequent to allocation, though the underlying storage may be relocated during dynamic resizing operations.

## 2. Array as an Abstract Data Type (ADT)

An Abstract Data Type (ADT) provides a rigorous mathematical specification of a data structure, defining the domain of stored data and the complete set of permissible operations, without committing to specific implementation details. The Array ADT establishes a contract between the interface and its implementations.

### 2.1 Array ADT Specification

**Data Component:**

- A collection of n elements (where n ≥ 0) belonging to a homogeneous data type T
- Elements are stored at sequential indices from 0 through n-1
- The cardinality n is established at allocation time and remains static for static arrays

**Operations:**

| Operation  | Signature                       | Description                                       |
| ---------- | ------------------------------- | ------------------------------------------------- |
| `create`   | `create(n, T) → Array`          | Allocates storage for n elements of type T        |
| `get`      | `get(A, i) → Element`           | Returns element at index i in O(1) time           |
| `set`      | `set(A, i, value) → void`       | Stores value at index i in O(1) time              |
| `length`   | `length(A) → n`                 | Returns the number of elements in O(1) time       |
| `insert`   | `insert(A, i, value) → boolean` | Inserts value at index i, shifting elements right |
| `delete`   | `delete(A, i) → Element`        | Removes and returns element at index i            |
| `search`   | `search(A, key) → index`        | Returns index of key, -1 if absent                |
| `traverse` | `traverse(A, visit)`            | Applies visit function to each element            |

## 3. Declaration and Initialization in C

### 3.1 Static Allocation (Stack Memory)

In C, arrays may be declared with static allocation using compile-time constant sizes, wherein the compiler allocates memory at program load time:

```c
/* Declaration without initialization - contents are indeterminate (garbage values) */
int arr_static[10];

/* Declaration with size inference from initializer list */
int arr_infer[] = {10, 20, 30, 40, 50};

/* Complete initialization with explicit size - all 5 elements specified */
int arr_complete[5] = {10, 20, 30, 40, 50};

/* Partial initialization - elements 0,1 initialized; 2,3,4 default to zero */
int arr_partial[5] = {10, 20};

/* Zero initialization - all elements explicitly set to 0 */
int arr_zero[5] = {0};

/* Character array (string literal initialization) */
char str[] = "Hello";  /* Creates array of 6 chars: 'H','e','l','l','o','\0' */

/* Multi-dimensional array declaration */
int matrix[3][4];  /* 3 rows, 4 columns */
```

### 3.2 Dynamic Allocation (Heap Memory)

For arrays whose dimensions are determined at runtime, dynamic allocation employing `malloc()` becomes necessary. This approach provides flexibility but requires explicit memory management:

```c
#include <stdlib.h>
#include <stdio.h>

int *createDynamicArray(size_t n) {
    int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }
    return arr;
}

/* Create and initialize array with zero values */
int *createZeroedArray(size_t n) {
    int *arr = (int *)calloc(n, sizeof(int));
    if (arr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }
    return arr;
}

void freeArray(int *arr) {
    free(arr);
}

/* Resize existing array - copies old data to new allocation */
int *resizeArray(int *old_arr, size_t old_size, size_t new_size) {
    int *new_arr = (int *)malloc(new_size * sizeof(int));
    if (new_arr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }
    /* Copy minimum of old and new sizes */
    size_t copy_size = (old_size < new_size) ? old_size : new_size;
    for (size_t i = 0; i < copy_size; i++) {
        new_arr[i] = old_arr[i];
    }
    free(old_arr);
    return new_arr;
}

/* Usage demonstration */
int main() {
    size_t n = 100;
    int *dynamic_arr = createDynamicArray(n);
    if (dynamic_arr != NULL) {
        dynamic_arr[0] = 42;
        printf("Element at index 0: %d\n", dynamic_arr[0]);
        freeArray(dynamic_arr);
    }
    return 0;
}
```

**Critical Considerations:** The programmer must invariably verify that `malloc()` returns a non-NULL pointer before utilization, and must invoke `free()` precisely once for each successful allocation to prevent both memory leaks and undefined behavior.

## 4. Memory Representation and Address Calculation

### 4.1 Contiguous Memory Layout

When an array is declared, the compiler allocates a contiguous block of memory equal to n) bytes. Consider an integer array of 5 elements wherein sizeof(int) = × sizeof(element_type 4 bytes:

```
Array:   [10]   [20]   [30]   [40]   [50]
Index:    0      1      2      3      4
Memory: +------+------+------+------+------+
        |  10  |  20  |  30  |  40  |  50  |
        +------+------+------+------+------+
Addr:   2000   2004   2008   2012   2016  (bytes)
```

Each successive element resides at an address offset by precisely sizeof(element_type) bytes from its predecessor, enabling deterministic address computation.

### 4.2 Formal Proof: Address Calculation Theorem

**Theorem:** For a one-dimensional array with base address B (representing the address of arr[0]), element size w bytes, the address of element arr[i] is given by:

```
Address(arr[i]) = B + (i × w)
```

**Proof by Mathematical Induction:**

1. **Base Case (i = 0):** The first element arr[0] is stored at the base address by definition.

   ```
   Address(arr[0]) = B + (0 × w) = B ✓
   ```

2. **Inductive Hypothesis:** Assume the formula holds for arr[i], i.e., `Address(arr[i]) = B + i × w`.

3. **Inductive Step:** For arr[i+1], since elements are stored contiguously in memory:
   ```
   Address(arr[i+1]) = Address(arr[i]) + w
                     = (B + i × w) + w
                     = B + (i + 1) × w
   ```
   This matches the formula for index i+1. By the principle of mathematical induction, the formula holds universally for all valid indices where 0 ≤ i < n. ∎

**Corollary:** Random access operates in O(1) time because address computation involves precisely one multiplication operation and one addition operation, both of which execute in constant time independent of array size n.

### 4.3 Worked Examples

**Example 1:** Base address B = 1000, sizeof(int) = 4, array size = 8

| Index  | Calculation   | Address |
| ------ | ------------- | ------- |
| arr[0] | 1000 + (0)(4) | 1000    |
| arr[1] | 1000 + (1)(4) | 1004    |
| arr[2] | 1000 + (2)(4) | 1008    |
| arr[7] | 1000 + (7)(4) | 1028    |

**Example 2:** Character array: Base = 5000, sizeof(char) = 1

- arr[100] = 5000 + (100)(1) = 5100

**Example 3:** Double array: Base = 10000, sizeof(double) = 8

- arr[25] = 10000 + (25)(8) = 10000 + 200 = 10200

## 5. Array Operations: Implementation and Complexity Analysis

### 5.1 Traversal Operation

```c
void traverse(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
}
```

- **Time Complexity:** O(n) — must visit each element exactly once
- **Space Complexity:** O(1) — uses only loop counter variable

### 5.2 Insertion Operation

Insertion at position i requires shifting all elements from i through n-1 one position to the right:

```c
/* Inserts value at index i, shifting elements right */
/* Returns 1 on success, 0 on failure (array full or invalid index) */
/* Assumes array has sufficient capacity - caller must ensure */
int insert(int arr[], int *n, int i, int value) {
    if (i < 0 || i > *n) {
        return 0;  /* Invalid index */
    }
    /* Shift elements from position *n-1 down to i, moving right */
    for (int j = *n; j > i; j--) {
        arr[j] = arr[j-1];
    }
    arr[i] = value;
    (*n)++;
    return 1;
}
```

- **Time Complexity:** O(n) in worst case (insertion at index 0), O(1) in best case (insertion at index n)
- **Space Complexity:** O(1)

### 5.3 Deletion Operation

Deletion at position i requires shifting all elements from i+1 through n-1 one position to the left:

```c
/* Deletes and returns element at index i */
/* Returns value through pointer, returns 1 on success, 0 on failure */
int delete(int arr[], int *n, int i, int *deleted_value) {
    if (i < 0 || i >= *n) {
        return 0;  /* Invalid index or empty array */
    }
    *deleted_value = arr[i];
    /* Shift elements from i+1 up to *n-1, moving left */
    for (int j = i; j < *n - 1; j++) {
        arr[j] = arr[j+1];
    }
    (*n)--;
    return 1;
}
```

- **Time Complexity:** O(n) in worst case (deletion at index 0), O(1) in best case (deletion at index n-1)
- **Space Complexity:** O(1)

### 5.4 Search Operations

**Linear Search:** Examines elements sequentially until a match is found or the array is exhausted:

```c
/* Returns index of key if found, -1 otherwise */
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i;
        }
    }
    return -1;
}
```

- **Time Complexity:** O(n) worst case, O(1) best case (element at index 0)
- **Space Complexity:** O(1)

**Binary Search:** Requires sorted array; divides search space in half each iteration:

```c
/* Returns index of key if found, -1 otherwise */
/* Precondition: arr must be sorted in ascending order */
int binarySearch(int arr[], int n, int key) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;  /* Prevents integer overflow */
        if (arr[mid] == key) {
            return mid;
        } else if (arr[mid] < key) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
```

- **Time Complexity:** O(log n) — search space halves each iteration
- **Space Complexity:** O(1)

### 5.5 Complexity Summary Table

| Operation         | Best Case | Worst Case | Space |
| ----------------- | --------- | ---------- | ----- |
| Access (by index) | O(1)      | O(1)       | O(1)  |
| Search (Linear)   | O(1)      | O(n)       | O(1)  |
| Search (Binary)   | O(1)      | O(log n)   | O(1)  |
| Insertion         | O(1)      | O(n)       | O(1)  |
| Deletion          | O(1)      | O(n)       | O(1)  |
| Traversal         | O(n)      | O(n)       | O(1)  |

## 6. Multidimensional Arrays

### 6.1 Two-Dimensional Arrays in Memory

Multidimensional arrays in C are stored in **row-major order**, wherein consecutive memory locations contain elements of the first row followed by elements of the second row, and so forth. For an m × n matrix (m rows, n columns), the address formula becomes:

```
Address(A[i][j]) = B + (i × n + j) × w
```

Where B represents the base address, n represents the number of columns, i represents the row index, j represents the column index, and w represents the element size in bytes.

**Proof:** In row-major storage, i complete rows precede row i, contributing i × n elements. Within row i, j elements precede the element at column j. Therefore, the total number of elements preceding A[i][j] equals i × n + j, yielding the address formula stated above.

### 6.2 Worked Example: 2D Array Address Calculation

Given a 3 × 4 integer matrix (3 rows, 4 columns), base address B = 1000, sizeof(int) = 4:

```
Matrix visualization:
    Col 0  Col 1  Col 2  Col 3
Row 0 [ 10 ] [ 20 ] [ 30 ] [ 40 ]
Row 1 [ 50 ] [ 60 ] [ 70 ] [ 80 ]
Row 2 [ 90 ] [100 ] [110 ] [120 ]

Memory layout (row-major):
[10][20][30][40][50][60][70][80][90][100][110][120]
```

Address calculations:

- A[0][0]: 1000 + (0×4 + 0)×4 = 1000
- A[1][2]: 1000 + (1×4 + 2)×4 = 1000 + (6)×4 = 1024
- A[2][3]: 1000 + (2×4 + 3)×4 = 1000 + (11)×4 = 1044

## 7. Dynamic Array Resizing and Amortized Analysis

### 7.1 Growth Strategy

Dynamic arrays typically employ a geometric growth strategy: when capacity is exhausted, allocate a new array with capacity multiplied by a growth factor α (commonly α = 2). This strategy ensures that the amortized cost of insertion remains constant.

### 7.2 Amortized Analysis

**Theorem:** Insertion into a dynamic array with geometric growth has an amortized cost of O(1) per operation.

**Proof:** Consider a sequence of n insertions into an initially empty dynamic array with growth factor α = 2. Let the costs be: 1 for each successful insertion, plus the cost of copying elements during resizing. If the array grows from capacity 2^k to 2^(k+1), exactly 2^k elements are copied at cost 2^k.

Total cost of n insertions:

- Sum of individual insertion costs: n (each insertion costs 1)
- Sum of copying costs: 1 + 2 + 4 + 8 + ... + 2^⌊log₂(n)⌋ < 2n

Therefore, total cost < 3n, yielding amortized cost per operation < 3 = O(1). ∎

## 8. Conclusion

Arrays represent the most fundamental contiguous-memory data structure in computer science, providing exceptional O(1) random access performance through deterministic address calculation. Their simplicity, combined with cache-friendly memory access patterns, makes them indispensable for performance-critical applications. Understanding the formal mathematical properties, including address calculation formulas and amortized complexity analyses, equips computer scientists and engineers with the theoretical foundation necessary for informed data structure selection and optimization.
