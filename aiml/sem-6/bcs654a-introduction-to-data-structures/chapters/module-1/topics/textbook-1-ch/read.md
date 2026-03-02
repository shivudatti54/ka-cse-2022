# Introduction to Data Structures: Arrays

=====================================================

## Table of Contents

---

- [What are Arrays?](#what-are-arrays)
- [One-Dimensional Arrays](#one-dimensional-arrays)
- [Two-Dimensional Arrays](#two-dimensional-arrays)
- [Initializing Two-Dimensional Arrays](#initializing-two-dimensional-arrays)
- [Key Concepts](#key-concepts)

## What are Arrays?

---

An array is a collection of elements of the same data type stored in contiguous memory locations. Arrays allow us to store and manipulate large amounts of data efficiently.

### Definition

A single-dimensional array is a collection of elements of the same data type stored in contiguous memory locations.

### Characteristics

- Each element in the array is identified by an index or subscript.
- The elements are stored in a single dimension.

## One-Dimensional Arrays

---

One-dimensional arrays are the simplest type of array. They consist of a single row of elements.

### Example

```c
int arr1[5];
arr1[0] = 10;
arr1[1] = 20;
arr1[2] = 30;
arr1[3] = 40;
arr1[4] = 50;
```

### Key Concepts

- `int arr1[5];` declares a one-dimensional array with 5 elements of type `int`.
- `arr1[0] = 10;` assigns the value 10 to the first element.
- `arr1[1] = 20;` assigns the value 20 to the second element.

## Two-Dimensional Arrays

---

Two-dimensional arrays are an extension of one-dimensional arrays. They consist of multiple rows and columns of elements.

### Example

```c
int arr2[2][3];
arr2[0][0] = 10;
arr2[0][1] = 20;
arr2[0][2] = 30;
arr2[1][0] = 40;
arr2[1][1] = 50;
arr2[1][2] = 60;
```

### Key Concepts

- `int arr2[2][3];` declares a two-dimensional array with 2 rows and 3 columns of elements of type `int`.
- `arr2[0][0] = 10;` assigns the value 10 to the top-left element.
- `arr2[1][1] = 50;` assigns the value 50 to the bottom-right element.

## Initializing Two-Dimensional Arrays

---

Two-dimensional arrays can be initialized using a single statement that specifies the number of rows and columns.

### Example

```c
int arr3[2][3] = {{10, 20, 30}, {40, 50, 60}};
```

### Key Concepts

- `int arr3[2][3] = {{10, 20, 30}, {40, 50, 60}};` initializes the array with the specified values.

## Key Concepts

---

- Arrays are used to store and manipulate large amounts of data efficiently.
- One-dimensional arrays consist of a single row of elements.
- Two-dimensional arrays consist of multiple rows and columns of elements.
- Arrays can be initialized using a single statement that specifies the number of rows and columns.
- Arrays are an essential data structure in programming.
