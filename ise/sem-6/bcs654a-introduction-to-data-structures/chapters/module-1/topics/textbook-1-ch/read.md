# Introduction to Data Structures

=====================================

## Overview

---

Data structures are the fundamental building blocks of computer science, and arrays are one of the most widely used data structures. In this module, we will explore the basics of arrays, including their introduction, one-dimensional arrays, and two-dimensional arrays.

## What is an Array?

---

An array is a collection of elements of the same data type stored in contiguous memory locations. It is a fundamental data structure that allows us to store and manipulate large amounts of data efficiently.

### Key Characteristics of Arrays:

- **Homogeneous**: All elements in an array must be of the same data type.
- **Contiguous Memory**: All elements in an array are stored in contiguous memory locations.
- **Indexed**: Arrays are indexed, meaning that each element is identified by a unique index or key.

### Types of Arrays

---

There are two primary types of arrays:

- **One-Dimensional Arrays**: A single row or column of elements.
- **Two-Dimensional Arrays**: A matrix or table of elements, where each element has both a row index and a column index.

## One-Dimensional Arrays

---

One-dimensional arrays are arrays that have only one dimension or index. They are the simplest type of array and are often used to store small amounts of data.

### Example of a One-Dimensional Array:

```c
int arr[5] = {1, 2, 3, 4, 5};
```

In this example, `arr` is a one-dimensional array that stores five integers.

### Operations on One-Dimensional Arrays:

- **Accessing Elements**: `arr[0]` accesses the first element.
- **Assigning Values**: `arr[0] = 10` assigns the value 10 to the first element.

## Two-Dimensional Arrays

---

Two-dimensional arrays are arrays that have two dimensions or indices. They are often used to store large amounts of data in a table-like structure.

### Example of a Two-Dimensional Array:

```c
int arr[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

In this example, `arr` is a two-dimensional array that stores two rows of three integers.

### Operations on Two-Dimensional Arrays:

- **Accessing Elements**: `arr[0][0]` accesses the first element of the first row.
- **Assigning Values**: `arr[0][0] = 10` assigns the value 10 to the first element of the first row.

## Initializing Two-Dimensional Arrays

---

Two-dimensional arrays can be initialized using a nested loop or a matrix literal.

### Example of Initializing a Two-Dimensional Array:

```c
int arr[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

Or using a nested loop:

```c
int arr[2][3];
for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
        arr[i][j] = i * 3 + j + 1;
    }
}
```

In this example, the two-dimensional array `arr` is initialized with values from 1 to 8.

## Conclusion

---

In this module, we have learned about the basics of arrays, including one-dimensional arrays and two-dimensional arrays. We have also explored operations on arrays, such as accessing elements and assigning values. Understanding arrays is essential for working with data structures in computer science.
