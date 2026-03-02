# Introduction to Data Structures

## Arrays: Introduction

In this topic, we will be covering the basics of arrays, including one-dimensional arrays, two-dimensional arrays, and initializing two-dimensional arrays.

### Definition of Arrays

An array is a collection of elements of the same data type stored in contiguous memory locations. The elements are identified by their index or subscript, which starts from 0.

### Key Concepts

- A fixed-size collection of elements
- Elements are stored in contiguous memory locations
- Elements are identified by their index or subscript
- Arrays are used to store multiple values of a single data type

### Example of an Array

Consider the following example of an array of integers:

```
int numbers[] = {10, 20, 30, 40, 50};
```

In this example, `numbers` is the name of the array, and `{10, 20, 30, 40, 50}` is the set of elements stored in the array.

###declaring arrays

Arrays are declared in C++ using the following syntax:

```
type name[index];
```

For example:

```
int numbers[5];
```

This declares an array `numbers` with 5 elements of type `int`.

### Initializing Arrays

Arrays can be initialized when declared using the following syntax:

```
type name[index] = {value1, value2, ..., valuen};
```

For example:

```
int numbers[5] = {10, 20, 30, 40, 50};
```

This initializes the array `numbers` with the elements `{10, 20, 30, 40, 50}`.

## One-Dimensional Arrays

One-dimensional arrays are arrays that have only one dimension. They are the most commonly used type of array.

### Example of a One-Dimensional Array

Consider the following example of a one-dimensional array:

```
int numbers[] = {10, 20, 30, 40, 50};
```

In this example, `numbers` is a one-dimensional array of integers.

### Accessing Elements of a One-Dimensional Array

Elements of a one-dimensional array are accessed using their index or subscript. The index starts from 0.

For example:

```
int number = numbers[0];
```

This accesses the first element of the array, which is `10`.

## Two-Dimensional Arrays

Two-dimensional arrays are arrays that have two dimensions. They are used to store multiple arrays within a single array.

### Example of a Two-Dimensional Array

Consider the following example of a two-dimensional array:

```
int numbers[2][3] = {{10, 20, 30}, {40, 50, 60}};
```

In this example, `numbers` is a two-dimensional array of integers. The subscripts `i` and `j` are used to access the elements of the array.

### Accessing Elements of a Two-Dimensional Array

Elements of a two-dimensional array are accessed using their row and column indices. The row index `i` ranges from 0 to `n-1`, and the column index `j` ranges from 0 to `m-1`.

For example:

```
int number = numbers[0][0];
```

This accesses the first element of the array, which is `10`.

## Initializing Two-Dimensional Arrays

Two-dimensional arrays can be initialized when declared using the following syntax:

```
type name[index, index] = {value1, value2, ..., valuen};
```

For example:

```
int numbers[2][3] = {{10, 20, 30}, {40, 50, 60}};
```

This initializes the array `numbers` with the elements `{{10, 20, 30}, {40, 50, 60}}`.

### Key Concepts

- Arrays are used to store multiple values of a single data type
- Arrays are used to store elements in contiguous memory locations
- Arrays are used to access elements using their index or subscript
- Two-dimensional arrays are used to store multiple arrays within a single array
