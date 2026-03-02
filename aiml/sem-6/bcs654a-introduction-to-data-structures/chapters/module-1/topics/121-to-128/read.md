# **12.1-12.8: Introduction to Arrays**

## **Introduction**

An array is a collection of elements of the same data type stored in contiguous memory locations. Arrays are a fundamental data structure in programming, used to store and manipulate collections of data.

## **Key Concepts**

- **Array Indexing**: The process of accessing and manipulating elements in an array using their position, known as the index.
- **Array Size**: The number of elements in an array.
- **Array Dimensions**: The number of arrays that can be created from a single array, represented by the number of subscripts.

## **Types of Arrays**

### 12.1: One-Dimensional Arrays

A one-dimensional array is an array that stores elements in a single row or column.

**Properties**

- Each element is identified by a unique index.
- All elements are of the same data type.
- Can be accessed and manipulated using a single subscript.

**Example**

```c
int arr[5] = {1, 2, 3, 4, 5};
```

### 12.2: Two-Dimensional Arrays

A two-dimensional array is an array that stores elements in multiple rows and columns.

**Properties**

- Each element is identified by a pair of indices, one for rows and one for columns.
- All elements are of the same data type.
- Can be accessed and manipulated using two subscripts.

**Example**

```c
int arr[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

### 12.3: Initializing Two-Dimensional Arrays

You can initialize a two-dimensional array using the following methods:

- **Row-wise Initialization**: Initialize each row individually.
- **Column-wise Initialization**: Initialize each column individually.

**Example**

```c
int arr[2][3] = {
    {1, 2, 3},  // Row-wise initialization
    {4, 5, 6}   // Row-wise initialization
};
```

**Example**

```c
int arr[2][3] = {
    {1, 4, 7},  // Column-wise initialization
    {2, 5, 8}   // Column-wise initialization
};
```

### 12.4: Accessing Elements in a Two-Dimensional Array

You can access elements in a two-dimensional array using two subscripts, one for rows and one for columns.

**Example**

```c
int arr[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

int value = arr[0][0];  // Accessing the first element
```

### 12.5: Modifying Elements in a Two-Dimensional Array

You can modify elements in a two-dimensional array using two subscripts, one for rows and one for columns.

**Example**

```c
int arr[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

arr[0][0] = 10;  // Modifying the first element
```

### 12.6: Array Operations

You can perform various operations on arrays, including:

- **Assignment**: Assigning one array to another.
- **Comparison**: Comparing two arrays using inequalities and equality operators.
- **Iteration**: Iterating over an array using for loops.

**Example**

```c
int arr1[5] = {1, 2, 3, 4, 5};
int arr2[5] = {6, 7, 8, 9, 10};

// Assignment
arr1[0] = arr2[0];

// Comparison
if (arr1[0] == arr2[0]) {
    printf("Arrays are equal\n");
}

// Iteration
for (int i = 0; i < 5; i++) {
    printf("%d ", arr1[i]);
}
```

### 12.7: Array Functions

You can use various functions to manipulate arrays, including:

- **memset**: Filling an array with a specific value.
- **memcpy**: Copying data from one array to another.

**Example**

```c
int arr[5] = {1, 2, 3, 4, 5};

// memset
memset(arr, 10, sizeof(arr));

// memcpy
memcpy(arr, arr + 1, 4 * sizeof(int));
```

### 12.8: Array Limitations

Arrays have some limitations, including:

- **Fixed Size**: Arrays have a fixed size, which can be difficult to manage in some situations.
- **No Dynamic Allocation**: Arrays do not support dynamic allocation, which means you cannot add or remove elements after the array is declared.

## **Conclusion**

In this topic, we covered the basics of arrays, including one-dimensional and two-dimensional arrays, array indexing, array size, and array dimensions. We also discussed array operations, array functions, and array limitations. Understanding these concepts is essential for working with arrays in programming.
