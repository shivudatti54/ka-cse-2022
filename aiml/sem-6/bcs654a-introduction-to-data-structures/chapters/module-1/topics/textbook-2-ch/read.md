**Textbook 2: Ch**
**INTRODUCTION TO DATA STRUCTURES**
**Module: Arrays: Introduction, One-Dimensional Arrays, Two-Dimensional Arrays, Initializing Two-**

## **What are Arrays?**

An array is a collection of elements of the same data type stored in contiguous memory locations. Arrays allow us to store and manipulate large amounts of data in a single variable.

**Key Characteristics of Arrays:**

- A fixed number of elements
- Elements are stored in contiguous memory locations
- All elements of an array are of the same data type
- Arrays are homogeneous, meaning all elements are of the same data type

**Types of Arrays:**

### One-Dimensional Arrays

A one-dimensional array is an array that has only one dimension. It stores elements in a single row or column.

**Example:**

```c
int arr[5] = {1, 2, 3, 4, 5};
```

In this example, `arr` is a one-dimensional array of 5 integers.

**Key Concepts of One-Dimensional Arrays:**

- Indexing: Accessing elements of an array using an index (starts from 0)
- Array Declaration: Declaring an array with a specific size
- Array Initialization: Initializing elements of an array with a specific value

### Two-Dimensional Arrays

A two-dimensional array is an array that has two dimensions. It stores elements in multiple rows and columns.

**Example:**

```c
int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
```

In this example, `arr` is a two-dimensional array of 2 rows and 3 columns.

**Key Concepts of Two-Dimensional Arrays:**

- Indexing: Accessing elements of a 2D array using row and column indices (starts from 0)
- Array Declaration: Declaring a 2D array with specific row and column sizes
- Array Initialization: Initializing elements of a 2D array with a specific value

## **Initializing Arrays**

Arrays can be initialized with a specific value, a range of values, or a sequence of values.

**Example:**

```c
int arr[5] = {0, 1, 2, 3, 4};  // Initializing with a range of values
int arr2[5] = {'a', 'b', 'c', 'd', 'e'};  // Initializing with a sequence of values
```

In the first example, `arr` is initialized with a range of values from 0 to 4. In the second example, `arr2` is initialized with a sequence of characters.

**Best Practices for Arrays:**

- Use meaningful variable names for arrays
- Declare arrays with a specific size to avoid runtime errors
- Initialize arrays with a specific value to avoid undefined behavior

**Common Operations on Arrays:**

- Assigning values to elements of an array
- Accessing elements of an array
- Updating elements of an array
- Comparison operations (e.g., equality, inequality)
