# **8.1 Introduction to Arrays**

### Definition

An array is a collection of elements of the same data type stored in contiguous memory locations. It allows us to store a large number of elements in a single variable.

### Characteristics

- Elements are stored in a fixed layout.
- Elements are of the same data type.
- Elements are accessed using an index or subscript.
- Arrays can be initialized using various methods.

### Example

```c
int scores[5] = {90, 85, 95, 80, 92};
```

### Declaration

```c
// Declare a 1D array with 5 elements
int scores[5];

// Declare a 1D array with initial values
int scores[5] = {90, 85, 95, 80, 92};
```

# **8.2 One-Dimensional Arrays**

### Definition

A one-dimensional array is an array that has only one dimension. It stores elements in a single row or column.

### Features

- Elements are accessed using a single index or subscript.
- Elements are of the same data type.
- Elements are stored in contiguous memory locations.
- One-dimensional arrays can be used to store values of any data type.

### Example

```c
int main() {
    int marks[5] = {85, 90, 78, 92, 88};
    int marks[5][5]; // Declare a 2D array
    return 0;
}
```

# **8.3 Two-Dimensional Arrays**

### Definition

A two-dimensional array is an array that has two dimensions. It stores elements in rows and columns.

### Features

- Elements are accessed using two indices or subscripts.
- Elements are of the same data type.
- Elements are stored in non-contiguous memory locations (each row has its own allocation).
- Two-dimensional arrays can be used to store matrices, tables, or any other rectangular data structure.

### Example

```c
int main() {
    int marks[2][3] = {{85, 90, 78}, {92, 88, 95}};
    return 0;
}
```

# **8.4 Initializing Two-Dimensional Arrays**

There are two ways to initialize two-dimensional arrays in C/C++:

### Method 1: Using the Row-Wise Initialization Method

```c
int marks[2][3] = {
    {85, 90, 78},
    {92, 88, 95}
};
```

### Method 2: Using the Column-Wise Initialization Method

```c
int marks[2][3] = {
    [0][0] = 85, [0][1] = 90, [0][2] = 78,
    [1][0] = 92, [1][1] = 88, [1][2] = 95
};
```

### Method 3: Using the Matrix Initialization Method

```c
int marks[2][3] = {{85, 90, 78}, {92, 88, 95}};
```

### Method 4: Using the Nested Initialization Method

```c
int marks[2][3] = {
    {85, 90, 78},
    {92, 88, 95}
};
```

### Method 5: Using the Contiguous Initialization Method

```c
int marks[2][3] = {
    [0][0] = 85, [0][1] = 90, [0][2] = 78,
    [1][0] = 92, [1][1] = 88, [1][2] = 95
};
```

### Method 6: Using the Aggregate Initialization Method

```c
int marks[2][3] = {{85, 90, 78}, {92, 88, 95}};
```

### Method 7: Using the Compound Literal Initialization Method

```c
int marks[2][3] = {{85, 90, 78}, {92, 88, 95}};
```

### Method 8: Using the Uniform Initialization Method

```c
int marks[2][3] = {[0][0] = 85, [0][1] = 90, [0][2] = 78, [1][0] = 92, [1][1] = 88, [1][2] = 95};
```
