# **8.1 - Arrays: Introduction**

### What are Arrays?

Arrays are a fundamental data structure in computer science, used to store a collection of elements of the same data type in a single variable. Arrays provide efficient storage and retrieval of data, making them a popular choice for many applications.

### Key Characteristics of Arrays:

- **Homogeneous**: Arrays store elements of the same data type.
- **Indexed**: Arrays use an index to access and manipulate elements.
- **Dynamic**: Arrays can grow or shrink dynamically as elements are added or removed.

### Benefits of Arrays:

- **Efficient Storage**: Arrays store elements in contiguous memory locations, reducing memory overhead.
- **Fast Access**: Arrays allow for fast access and manipulation of elements using their index.
- **Flexible**: Arrays can be used to store a wide range of data types.

# **8.2 - One-Dimensional Arrays**

### Definition:

A one-dimensional array is an array that stores elements in a single row or column. Each element in the array is identified by an index that corresponds to its position in the array.

### Example:

```c
int myArray[5];
myArray[0] = 10;
myArray[1] = 20;
myArray[2] = 30;
myArray[3] = 40;
myArray[4] = 50;
```

### Key Concepts:

- **Indexing**: Elements in a one-dimensional array are accessed using an index that starts from 0.
- **Initialization**: Elements in a one-dimensional array can be initialized using the assignment operator (=).
- **Accessing Elements**: Elements in a one-dimensional array can be accessed using their index.

# **8.3 - Two-Dimensional Arrays**

### Definition:

A two-dimensional array is an array that stores elements in rows and columns. Each element in the array is identified by an index that corresponds to its position in the array.

### Example:

```c
int myArray[3][4];
myArray[0][0] = 10;
myArray[0][1] = 20;
myArray[0][2] = 30;
myArray[0][3] = 40;
myArray[1][0] = 50;
myArray[1][1] = 60;
myArray[1][2] = 70;
myArray[1][3] = 80;
myArray[2][0] = 90;
myArray[2][1] = 100;
myArray[2][2] = 110;
myArray[2][3] = 120;
```

### Key Concepts:

- **Indexing**: Elements in a two-dimensional array are accessed using an index that consists of two parts: row and column indices.
- **Initialization**: Elements in a two-dimensional array can be initialized using the assignment operator (=).
- **Accessing Elements**: Elements in a two-dimensional array can be accessed using their row and column indices.

# **8.4 - Initializing Two-Dimensional Arrays**

### Methods to Initialize Two-Dimensional Arrays:

- **Using the Assignment Operator**: Elements can be initialized using the assignment operator (=).
- **Using a Loop**: Elements can be initialized using a loop that iterates over the array.
- **Using a Matrix**: Elements can be initialized using a matrix that stores the initial values.

### Example:

```c
int myArray[3][4] = {
    {10, 20, 30, 40},
    {50, 60, 70, 80},
    {90, 100, 110, 120}
};
```

### Key Concepts:

- **Matrix Initialization**: Two-dimensional arrays can be initialized using a matrix that stores the initial values.
- **Loop Initialization**: Two-dimensional arrays can be initialized using a loop that iterates over the array.

# **8.5 - Common Operations on Arrays**

### Key Operations:

- **Assignment**: Elements can be assigned a new value using the assignment operator (=).
- **Arithmetic Operations**: Elements can be manipulated using arithmetic operators (+, -, \*, /).
- **Comparison Operations**: Elements can be compared using comparison operators (==, !=, <, >).

### Example:

```c
int myArray[3][4] = {
    {10, 20, 30, 40},
    {50, 60, 70, 80},
    {90, 100, 110, 120}
};

// Assignment
myArray[0][0] = 100;

// Arithmetic Operations
myArray[1][1] *= 2;

// Comparison Operations
if (myArray[2][2] > 105) {
    printf("Condition met\n");
}
```

### Key Concepts:

- **Assignment**: Elements can be assigned a new value using the assignment operator (=).
- **Arithmetic Operations**: Elements can be manipulated using arithmetic operators (+, -, \*, /).
- **Comparison Operations**: Elements can be compared using comparison operators (==, !=, <, >).
