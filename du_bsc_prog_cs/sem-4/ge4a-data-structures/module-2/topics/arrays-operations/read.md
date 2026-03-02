# Arrays: Operations and Implementation

## Introduction

Arrays are the most fundamental and widely used linear data structures in computer science. An array is a collection of elements of the same data type stored in contiguous memory locations, accessible through their indices. In the context of the University of Delhi's Computer Science program, understanding arrays and their operations forms the cornerstone of algorithmic problem-solving and forms the basis for more complex data structures like stacks, queues, and matrices.

The importance of arrays in computer science cannot be overstated. They provide O(1) random access to elements, making them ideal for scenarios where frequent element retrieval by index is required. According to the DU syllabus for Data Structures (GE4A), students must master array operations including traversal, insertion, deletion, searching, and sorting to excel in both internal assessments and end-semester examinations. This topic carries significant weightage in practical exams where students implement these operations in C/C++ programming language.

In real-world applications, arrays are used extensively in database management systems, image processing (where images are represented as 2D arrays of pixels), statistical computing, and game development. Understanding how to efficiently manipulate arrays is therefore not just an academic requirement but a practical skill essential for any software developer.

## Key Concepts

### 1. Array Declaration and Initialization

In C/C++, arrays are declared by specifying the data type, array name, and size. For example:

```c
int marks[10];          // Declaration of integer array of size 10
float prices[5] = {100.5, 200.0, 150.75, 300.0, 50.25};  // Initialization
char name[20] = "Delhi University";  // Character array (string)
```

Memory allocation for arrays is static in C/C++, meaning the size must be known at compile time. The array elements are stored in contiguous memory locations, which is crucial for understanding pointer arithmetic and efficient access.

### 2. Traversal Operation

Traversal refers to visiting each element of the array exactly once. This operation is fundamental and serves as the basis for many other operations like searching, sorting, and computing statistics.

```c
// Traversal: Printing all elements
void traverse(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
}
```

**Time Complexity: O(n)** - We must visit each of the n elements once.

### 3. Insertion Operation

Insertion involves adding a new element at a specified position in the array. There are three scenarios:
- **At the beginning**: Requires shifting all elements to the right - O(n)
- **At the end**: If array has space, O(1); otherwise O(n) for resizing
- **At a specific position**: Requires shifting elements from that position onwards - O(n)

```c
// Insertion at a specific position
int insert(int arr[], int n, int pos, int value) {
    if (n >= MAX_SIZE) {
        printf("Array is full\n");
        return n;
    }
    if (pos < 0 || pos > n) {
        printf("Invalid position\n");
        return n;
    }
    // Shift elements to the right
    for (int i = n; i > pos; i--) {
        arr[i] = arr[i-1];
    }
    arr[pos] = value;
    return n + 1;
}
```

**Time Complexity: O(n)** in the worst case (insertion at beginning), O(1) at the end.

### 4. Deletion Operation

Deletion removes an element from a specified position. Similar to insertion, it requires shifting elements to fill the gap:

```c
// Deletion at a specific position
int delete(int arr[], int n, int pos) {
    if (n == 0) {
        printf("Array is empty\n");
        return n;
    }
    if (pos < 0 || pos >= n) {
        printf("Invalid position\n");
        return n;
    }
    // Shift elements to the left
    for (int i = pos; i < n - 1; i++) {
        arr[i] = arr[i+1];
    }
    return n - 1;
}
```

**Time Complexity: O(n)** in the worst case (deletion at beginning).

### 5. Searching Operations

**Linear Search**: Checks each element sequentially until the target is found or array ends.

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

**Time Complexity: O(n)** - In the worst case, we examine all elements.

**Binary Search**: Works on sorted arrays by repeatedly dividing the search interval in half.

```c
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}
```

**Time Complexity: O(log n)** - The search space is halved with each iteration.

### 6. Sorting Operations

Sorting arranges elements in a specific order (ascending or descending). Key sorting algorithms include:

**Bubble Sort**: Repeatedly swaps adjacent elements if they're in wrong order.

```c
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
```

**Time Complexity: O(n²)**, Space: O(1)

**Selection Sort**: Finds minimum element and places it at the beginning.

```c
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        int minIdx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }
        // Swap
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}
```

**Time Complexity: O(n²)**, Space: O(1)

### 7. Two-Dimensional Arrays

Two-dimensional arrays (matrices) are arrays of arrays, stored in row-major or column-major order:

```c
int matrix[3][4];  // 3 rows, 4 columns

// Accessing element at row i, column j
// In row-major: baseAddress + (i * COLS + j) * size
```

Common operations on 2D arrays include matrix addition, transpose, and multiplication.

## Examples

### Example 1: Implementing Linear Search and Finding Statistics

**Problem**: Given an array of marks obtained by 10 students, write a program to find the highest marks and count how many students scored above the average.

```c
#include <stdio.h>

int main() {
    int marks[10] = {85, 72, 90, 65, 88, 76, 95, 82, 70, 91};
    int n = 10;
    int sum = 0, max = marks[0], countAboveAvg = 0;
    float avg;
    
    // Find sum and maximum
    for (int i = 0; i < n; i++) {
        sum += marks[i];
        if (marks[i] > max)
            max = marks[i];
    }
    
    avg = sum / (float)n;
    
    // Count students above average
    for (int i = 0; i < n; i++) {
        if (marks[i] > avg)
            countAboveAvg++;
    }
    
    printf("Highest Marks: %d\n", max);
    printf("Average: %.2f\n", avg);
    printf("Students above average: %d\n", countAboveAvg);
    
    return 0;
}
```

**Output**:
```
Highest Marks: 95
Average: 81.40
Students above average: 4
```

### Example 2: Insertion and Deletion Operations

**Problem**: Implement a menu-driven program to perform insertion and deletion on an array.

```c
#include <stdio.h>
#define MAX_SIZE 20

void display(int arr[], int n) {
    if (n == 0) {
        printf("Array is empty\n");
        return;
    }
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int insert(int arr[], int n, int pos, int value) {
    if (n >= MAX_SIZE) {
        printf("Overflow: Cannot insert\n");
        return n;
    }
    if (pos < 0 || pos > n) {
        printf("Invalid position\n");
        return n;
    }
    for (int i = n; i > pos; i--)
        arr[i] = arr[i-1];
    arr[pos] = value;
    return n + 1;
}

int delete(int arr[], int n, int pos) {
    if (n == 0) {
        printf("Underflow: Array empty\n");
        return n;
    }
    if (pos < 0 || pos >= n) {
        printf("Invalid position\n");
        return n;
    }
    for (int i = pos; i < n - 1; i++)
        arr[i] = arr[i+1];
    return n - 1;
}

int main() {
    int arr[MAX_SIZE] = {10, 20, 30, 40};
    int n = 4, choice, pos, value;
    
    printf("Initial array: ");
    display(arr, n);
    
    printf("\n1. Insert 2. Delete 3. Display 4. Exit\n");
    scanf("%d", &choice);
    
    switch(choice) {
        case 1:
            printf("Enter position and value: ");
            scanf("%d %d", &pos, &value);
            n = insert(arr, n, pos, value);
            display(arr, n);
            break;
        case 2:
            printf("Enter position to delete: ");
            scanf("%d", &pos);
            n = delete(arr, n, pos);
            display(arr, n);
            break;
        case 3:
            display(arr, n);
            break;
    }
    return 0;
}
```

### Example 3: Binary Search on Sorted Array

**Problem**: Implement binary search to find a number in a sorted array of 8 elements.

```c
#include <stdio.h>

int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;  // Prevents integer overflow
        
        printf("Search range: [%d, %d], Mid index: %d, Mid value: %d\n", 
               low, high, mid, arr[mid]);
        
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main() {
    int arr[] = {12, 23, 34, 45, 56, 67, 78, 89};
    int n = 8;
    int key = 67;
    
    int result = binarySearch(arr, n, key);
    
    if (result != -1)
        printf("Element %d found at index %d\n", key, result);
    else
        printf("Element %d not found in the array\n", key);
    
    return 0;
}
```

**Output**:
```
Search range: [0, 7], Mid index: 3, Mid value: 45
Search range: [4, 7], Mid index: 5, Mid value: 67
Element 67 found at index 5
```

## Exam Tips

For DU semester examinations, keep the following points in mind:

1. **Understand Time Complexities**: Memorize the time complexities of all array operations. Linear search is O(n), binary search is O(log n), and sorting algorithms are typically O(n²) for basic sorts.

2. **Distinguish Between Array Types**: Know the difference between 1D and 2D arrays, static and dynamic arrays, and row-major vs column-major storage.

3. **Practice Code Writing**: DU practical exams require writing C programs. Practice implementing all operations (traversal, insertion, deletion, search, sort) without referring to notes.

4. **Remember Boundary Conditions**: Always check for array overflow (when inserting in full array) and underflow (when deleting from empty array) in your code.

5. **Binary Search Prerequisite**: Remember that binary search only works on sorted arrays. Always sort first or mention this assumption.

6. **Space Complexity Matters**: When discussing algorithms, mention both time and space complexity. Bubble sort and selection sort have O(1) auxiliary space.

7. **Use Meaningful Variable Names**: In exams, use names like `arr`, `n`, `key`, `pos` rather than single letters to make code readable.

8. **Handle Edge Cases**: Your code should handle empty arrays, single-element arrays, and insertion/deletion at first and last positions correctly.

9. **Trace Through Examples**: Be able to manually trace through sorting algorithms step by step - this is frequently asked in theory exams.

10. **Know When to Use What**: For small arrays, linear search is fine; for large sorted arrays, binary search is essential. Selection sort is stable; understand these nuances.