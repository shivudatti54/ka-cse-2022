# Arrays: Operations and Applications

## Introduction

Arrays are the most fundamental and widely used data structures in computer science and programming. An array is a collection of elements of the same data type stored in contiguous memory locations, which allows for efficient random access to any element using its index. The concept of arrays forms the backbone of many complex data structures and algorithms that you will encounter throughout your computer science journey.

In the context of the University of Delhi's BSc (Hons) Computer Science program, understanding arrays is essential not only for data structure coursework but also for practical programming in languages like C, C++, Java, and Python. Arrays provide the foundation for implementing more advanced structures such as stacks, queues, heaps, and hash tables. Given that internal assessments and end-semester examinations carry significant weight (25% and 75% respectively), mastering arrays operations and their applications will give you a competitive edge in achieving high scores.

This topic covers the essential operations that can be performed on arrays—traversal, insertion, deletion, searching, and sorting—along with their time complexities and practical applications in real-world scenarios. We will also explore multi-dimensional arrays and the advantages and limitations of using arrays as data storage structures.

## Key Concepts

### Definition and Characteristics of Arrays

An array is a linear data structure that stores a collection of elements of the same data type in contiguous memory locations. Each element in an array can be accessed directly using its index, which typically starts from 0 (in C, C++, Java) or 1 (in some languages like Fortran). The key characteristics of arrays include:

- **Homogeneous elements**: All elements must be of the same data type (integers, floats, characters, etc.)
- **Contiguous memory**: Elements are stored in consecutive memory locations
- **Fixed size**: In most static implementations, array size is defined at compile time
- **Random access**: Any element can be accessed in O(1) time using its index

### Array Representation in Memory

In most programming languages, arrays are implemented with a base address that points to the first element. For an array `arr` with base address `base`, the address of any element at index `i` can be calculated as:

```
Address(arr[i]) = base + (i × size_of_element)
```

For example, in a C program with an integer array (assuming 4 bytes per integer), if the base address is 1000, then the address of arr[3] would be 1000 + (3 × 4) = 1012.

### Operations on Arrays

#### 1. Traversal
Traversal refers to visiting each element of the array exactly once. This operation is fundamental and serves as the basis for many other operations like searching and sorting.

```c
// C program to traverse an array
#include <stdio.h>

void traverse(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = sizeof(arr) / sizeof(arr[0]);
    traverse(arr, n);
    return 0;
}
```

Time Complexity: O(n)

#### 2. Insertion
Insertion involves adding a new element at a specified position. In a static array, insertion requires shifting elements to the right to make space.

```c
// Insert element at position pos
void insert(int arr[], int n, int pos, int value) {
    if (n >= 100) {  // Assuming max size is 100
        printf("Array is full\n");
        return;
    }
    if (pos < 0 || pos > n) {
        printf("Invalid position\n");
        return;
    }
    for (int i = n; i > pos; i--) {
        arr[i] = arr[i-1];
    }
    arr[pos] = value;
}
```

Time Complexity: O(n) in worst case (inserting at position 0), O(1) in best case (inserting at end)

#### 3. Deletion
Deletion removes an element from a specified position and shifts the remaining elements to the left to fill the gap.

```c
// Delete element at position pos
void delete(int arr[], int n, int pos) {
    if (n == 0) {
        printf("Array is empty\n");
        return;
    }
    if (pos < 0 || pos >= n) {
        printf("Invalid position\n");
        return;
    }
    for (int i = pos; i < n - 1; i++) {
        arr[i] = arr[i+1];
    }
}
```

Time Complexity: O(n) in worst case (deleting at position 0), O(1) in best case (deleting at end)

#### 4. Searching

**Linear Search**: Sequentially checks each element until a match is found.

```c
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i;  // Return index if found
        }
    }
    return -1;  // Not found
}
```

Time Complexity: O(n)

**Binary Search**: Requires sorted array; divides search space in half each iteration.

```c
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) {
            return mid;
        }
        if (arr[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
```

Time Complexity: O(log n)

#### 5. Sorting

**Bubble Sort**: Repeatedly swaps adjacent elements if they are in wrong order.

```c
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```

Time Complexity: O(n²), Space Complexity: O(1)

**Selection Sort**: Finds minimum element and places it at beginning.

```c
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}
```

Time Complexity: O(n²), Space Complexity: O(1)

### Multi-Dimensional Arrays

Multi-dimensional arrays extend the concept to rows and columns. The most common is the 2D array, which can represent matrices, grids, and tables.

**Memory Representation**: 2D arrays can be stored in two ways:
- **Row-major order**: Elements are stored row by row (used in C, C++, Python)
- **Column-major order**: Elements are stored column by column (used in Fortran, MATLAB)

For a 2D array `arr[m][n]`, the address of element `arr[i][j]` in row-major order:
```
Address(arr[i][j]) = base + (i × n + j) × size_of_element
```

### Applications of Arrays

Arrays are used extensively in various computing applications:

1. **Matrix operations**: Mathematical matrices are naturally represented as 2D arrays for operations like addition, multiplication, and transposition.

2. **Database records**: Arrays can store records of student information, employee data, or any structured data in memory.

3. **Lookup tables**: Pre-computed values stored in arrays for quick access (e.g., trigonometric tables, currency conversion rates).

4. **Buffers**: Used in I/O operations as temporary storage for data being transferred.

5. **Implementing other data structures**: Arrays serve as the underlying structure for stacks, queues, heaps, and hash tables.

6. **Image processing**: Digital images are represented as 2D arrays of pixels.

7. **Polynomial representation**: Polynomials can be stored using arrays where the index represents the power of x.

## Examples

### Example 1: Finding Duplicates in an Array

**Problem**: Given an array of n integers (range 1 to n-1), find if there are any duplicates.

**Solution Approach**: Since the range is limited, we can use an auxiliary boolean array to track seen elements.

```c
#include <stdio.h>

int findDuplicate(int arr[], int n) {
    int seen[n];  // Assuming n > 1
    for (int i = 0; i < n; i++) {
        seen[i] = 0;
    }
    
    for (int i = 0; i < n; i++) {
        if (seen[arr[i]] == 1) {
            return arr[i];  // Duplicate found
        }
        seen[arr[i]] = 1;
    }
    return -1;  // No duplicate
}

int main() {
    int arr[] = {1, 3, 4, 2, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = findDuplicate(arr, n);
    if (result != -1) {
        printf("Duplicate found: %d\n", result);
    } else {
        printf("No duplicate found\n");
    }
    return 0;
}
```

**Output**: Duplicate found: 2

**Time Complexity**: O(n), **Space Complexity**: O(n)

### Example 2: Rotating an Array

**Problem**: Rotate an array of n elements by d positions to the left.

**Solution Approach**: Use reversal algorithm - reverse the first d elements, reverse the remaining n-d elements, then reverse the entire array.

```c
#include <stdio.h>

void reverse(int arr[], int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

void rotateLeft(int arr[], int n, int d) {
    if (d == 0) return;
    d = d % n;  // Handle if d > n
    
    // Reverse first d elements
    reverse(arr, 0, d - 1);
    // Reverse remaining n-d elements
    reverse(arr, d, n - 1);
    // Reverse entire array
    reverse(arr, 0, n - 1);
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    int d = 2;
    
    printf("Original array: ");
    printArray(arr, n);
    
    rotateLeft(arr, n, d);
    
    printf("After rotation by %d: ", d);
    printArray(arr, n);
    
    return 0;
}
```

**Output**:
```
Original array: 1 2 3 4 5 6 7 
After rotation by 2: 3 4 5 6 7 1 2 
```

**Time Complexity**: O(n), **Space Complexity**: O(1)

### Example 3: Two-Dimensional Array for Matrix Multiplication

**Problem**: Multiply two 3×3 matrices.

```c
#include <stdio.h>

#define N 3

void multiplyMatrices(int A[][N], int B[][N], int C[][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            C[i][j] = 0;
            for (int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void printMatrix(int M[][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", M[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int A[N][N] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[N][N] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int C[N][N];
    
    multiplyMatrices(A, B, C);
    
    printf("Result of A × B:\n");
    printMatrix(C);
    
    return 0;
}
```

**Output**:
```
Result of A × B:
30 24 18 
84 69 54 
138 114 90 
```

**Time Complexity**: O(n³) for n×n matrices

## Exam Tips

1. **Remember index conventions**: In C, C++, and Java, array indices start from 0. Accessing arr[-1] or arr[n] (out of bounds) leads to undefined behavior.

2. **Time complexity is crucial**: Be prepared to analyze the time complexity of each operation. In exams, you may be asked to compare linear search vs binary search or bubble sort vs selection sort.

3. **Binary search prerequisites**: Always remember that binary search only works on sorted arrays. This is a common trick question in exams.

4. **Space complexity matters**: When analyzing array operations, consider both time and space complexity. For example, insertion in an unsorted array is O(1) if position doesn't matter.

5. **Row-major vs column-major**: Know the difference and be able to calculate addresses in 2D arrays for both storage methods.

6. **Diagrams help**: In exams, draw array representations showing indices and memory addresses to demonstrate your understanding.

7. **Practical applications**: Be ready to explain real-world applications of arrays like matrix operations, database records, and lookup tables.

8. **Edge cases matter**: Consider boundary conditions - inserting at position 0, deleting the last element, searching in empty arrays, etc.