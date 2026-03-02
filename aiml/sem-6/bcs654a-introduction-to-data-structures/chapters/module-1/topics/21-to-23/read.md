# **2.1 Introduction to Arrays**

### Definition

An array is a collection of elements of the same data type stored in contiguous memory locations. It is a fundamental data structure in programming that allows for efficient storage and manipulation of large amounts of data.

### Characteristics

- Arrays are used to store multiple values in a single variable.
- Elements of an array are accessed using an index or subscript.
- Arrays can be of any data type, including integers, floating-point numbers, characters, and strings.

### Benefits

- Arrays provide efficient storage and retrieval of data.
- They allow for easy manipulation and modification of data elements.
- Arrays can be used to represent complex data structures, such as graphs and matrices.

**2.2 One-Dimensional Arrays**
================-----------

### Definition

A one-dimensional array is an array that consists of elements stored in a single row or column.

### Characteristics

- One-dimensional arrays are denoted by square brackets `[]` and are of the form `arrayName[arraySize]`.
- Elements of a one-dimensional array are accessed using an index or subscript, starting from 0.
- One-dimensional arrays are used to represent arrays that can be one-dimensional.

### Examples

- `int scores[5];` declares a one-dimensional array of integers with 5 elements.
- `char colors[4] = {'R', 'G', 'B', 'Y'};` declares a one-dimensional array of characters with 4 elements.

### Key Concepts

- Element access: `arrayName[index]`
- Array initialization: `arrayName[arraySize] = {value1, value2, ..., valueN};`

# **2.3 Two-Dimensional Arrays**

### Definition

A two-dimensional array is an array that consists of elements stored in multiple rows and columns.

### Characteristics

- Two-dimensional arrays are denoted by double square brackets `[][]` and are of the form `arrayName[rowSize][columnSize]`.
- Elements of a two-dimensional array are accessed using two indices or subscripts, one for rows and one for columns.
- Two-dimensional arrays are used to represent arrays that can be two-dimensional.

### Examples

- `int matrix[3][3];` declares a two-dimensional array of integers with 3 rows and 3 columns.
- `char text[2][4] = {{"A", "B", "C", "D"}, {"E", "F", "G", "H"}};` declares a two-dimensional array of characters with 2 rows and 4 columns.

### Key Concepts

- Element access: `arrayName[rowIndex][columnIndex]`
- Array initialization: `arrayName[rowSize][columnSize] = {value1, value2, ..., valueN};`

### Exercises

1.  Declare a one-dimensional array of integers with 5 elements.
2.  Declare a two-dimensional array of characters with 2 rows and 4 columns.
3.  Initialize a one-dimensional array of integers with 3 elements.
4.  Initialize a two-dimensional array of characters with 2 rows and 3 columns.

### Code Example

```c
#include <stdio.h>

int main() {
    // One-dimensional array
    int scores[5] = {90, 80, 70, 60, 50};
    printf("One-dimensional array: %d, %d, %d, %d, %d\n", scores[0], scores[1], scores[2], scores[3], scores[4]);

    // Two-dimensional array
    char text[2][4] = {{"A", "B", "C", "D"}, {"E", "F", "G", "H"}};
    printf("Two-dimensional array:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%c ", text[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

This study material covers the basics of arrays, including one-dimensional and two-dimensional arrays, and provides examples and exercises to help you understand the concepts.
