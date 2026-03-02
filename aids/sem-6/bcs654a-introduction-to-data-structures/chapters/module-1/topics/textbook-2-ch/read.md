# **INTRODUCTION TO DATA STRUCTURES**

## **Modules**

- Arrays: Introduction, One-Dimensional Arrays, Two-Dimensional Arrays, Initializing Two-Dimensional Arrays

## **Arrays: Introduction**

### Definition

An array is a collection of elements of the same data type stored in contiguous memory locations. The elements are identified by their indices or keys.

### Characteristics

- Arrays are ordered collections of elements.
- Elements are stored in a contiguous block of memory.
- Arrays have a fixed size, but the elements can be of any data type.
- Arrays are mutable, meaning their elements can be modified after creation.

### Types of Arrays

#### 1. One-Dimensional Arrays

A one-dimensional array is a collection of elements stored in a single row or column.

- Elements are identified by their indices, which range from 0 to `n-1`, where `n` is the number of elements.
- Accessing an element at index `i` returns the element at that position.
- Example: `int arr[] = {1, 2, 3, 4, 5};`

#### 2. Two-Dimensional Arrays

A two-dimensional array is a collection of rows, each containing a one-dimensional array.

- Elements are identified by their row and column indices, which range from 0 to `m-1` and `n-1`, respectively.
- Accessing an element at row `i` and column `j` returns the element at that position.
- Example: `int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};`

## **Arrays: One-Dimensional**

### Initializing One-Dimensional Arrays

To initialize a one-dimensional array, you can use the following syntax:

- `datatype arr[size];`
- `datatype arr[size];`

### Example

```c
#include <stdio.h>

int main() {
    int arr[5]; // Initialize an array of 5 integers
    arr[0] = 10; // Assign a value to the first element
    arr[1] = 20; // Assign a value to the second element
    printf("%d %d\n", arr[0], arr[1]); // print the values
    return 0;
}
```

### Accessing Elements in a One-Dimensional Array

To access an element in a one-dimensional array, you can use the following syntax:

- `arr[index];`

### Example

```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5}; // Initialize an array of 5 integers
    printf("%d\n", arr[2]); // print the third element
    return 0;
}
```

## **Arrays: Two-Dimensional**

### Initializing Two-Dimensional Arrays

To initialize a two-dimensional array, you can use the following syntax:

- `datatype arr[rows][columns];`
- `datatype arr[rows][columns] = {{value1, value2}, {value3, value4}};`

### Example

```c
#include <stdio.h>

int main() {
    int arr[2][3] = {{1, 2, 3}, {4, 5, 6}}; // Initialize a 2x3 matrix
    printf("%d %d %d\n", arr[0][0], arr[0][1], arr[0][2]); // print the first row
    return 0;
}
```

### Accessing Elements in a Two-Dimensional Array

To access an element in a two-dimensional array, you can use the following syntax:

- `arr[row][column];`

### Example

```c
#include <stdio.h>

int main() {
    int arr[2][3] = {{1, 2, 3}, {4, 5, 6}}; // Initialize a 2x3 matrix
    printf("%d\n", arr[1][2]); // print the element at row 1, column 2
    return 0;
}
```
