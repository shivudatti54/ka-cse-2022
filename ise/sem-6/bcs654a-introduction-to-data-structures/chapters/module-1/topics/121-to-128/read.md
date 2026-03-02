# **12.1: Introduction to Arrays**

### Definition and Purpose

An array is a collection of elements of the same data type stored in contiguous memory locations. Arrays are used to store collections of data that need to be accessed by their index or position.

### Key Characteristics

- Elements of the same data type are stored in adjacent memory locations.
- Array elements can be accessed using their index or position.
- Arrays can be of any data type, including integers, floats, characters, and strings.

### Example

```c
int num[5] = {1, 2, 3, 4, 5};
```

In this example, `num` is an array of 5 integers, and the elements are initialized with values from 1 to 5.

### Benefits of Arrays

- Arrays can store large amounts of data in a single variable.
- Arrays provide efficient access to specific elements using their index.
- Arrays can be used to represent relationships between data.

### 12.2: One-Dimensional Arrays

=====================================

### Definition and Purpose

A one-dimensional array is an array with elements stored in a single row or column. It is also known as a scalar array or a single-row array.

### Key Characteristics

- Elements are stored in a single row or column.
- Each element is identified by a unique index or position.
- One-dimensional arrays can be used to represent single values or small collections of data.

### Example

```c
float score[5] = {90.5, 85.2, 92.1, 88.6, 76.3};
```

In this example, `score` is a one-dimensional array of 5 floating-point numbers.

### Benefits of One-Dimensional Arrays

- One-dimensional arrays are simple to declare and use.
- They can be used to store single values or small collections of data.
- They are memory-efficient and use less memory than two-dimensional arrays.

### 12.3: Two-Dimensional Arrays

=====================================

### Definition and Purpose

A two-dimensional array is an array with elements stored in multiple rows and columns. It is also known as a matrix or a table.

### Key Characteristics

- Elements are stored in multiple rows and columns.
- Each element is identified by a unique index or position (row and column).
- Two-dimensional arrays can be used to represent complex relationships between data.

### Example

```c
int marks[3][4] = {
    {90, 85, 92, 88},
    {76, 95, 89, 91},
    {91, 88, 92, 89}
};
```

In this example, `marks` is a two-dimensional array of 3 rows and 4 columns, where each element represents a student's marks in different subjects.

### Benefits of Two-Dimensional Arrays

- Two-dimensional arrays can store complex data with multiple relationships.
- They provide efficient access to specific elements using their row and column indices.
- They are useful for representing tables or matrices in data structures.

### 12.4: Initializing Two-Dimensional Arrays

=============================================

### Declaring and Initializing Two-Dimensional Arrays

A two-dimensional array can be declared and initialized using the following syntax:

```c
int marks[3][4] = {
    {90, 85, 92, 88},
    {76, 95, 89, 91},
    {91, 88, 92, 89}
};
```

### Initializing Two-Dimensional Arrays Using VLA (Variable Length Arrays)

VLA is a feature introduced in C99 that allows for dynamic memory allocation for arrays. Here's an example of initializing a two-dimensional array using VLA:

```c
int marks[3][4];

for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        marks[i][j] = i * 10 + j;
    }
}
```

### Initializing Two-Dimensional Arrays Using Initialization Lists

You can also initialize a two-dimensional array using an initialization list:

```c
int marks[3][4] = {
    {0, 10, 20, 30},
    {40, 50, 60, 70},
    {80, 90, 100, 110}
};
```

### 12.5: Initializing Arrays

=============================

### Initializing One-Dimensional Arrays

You can initialize a one-dimensional array using the following syntax:

```c
int num[5] = {1, 2, 3, 4, 5};
```

### Initializing Two-Dimensional Arrays

You can initialize a two-dimensional array using the following syntax:

```c
int marks[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};
```

### 12.6: Array Operations

=========================

### Performing Arithmetic Operations on Arrays

You can perform arithmetic operations on arrays using the following syntax:

```c
int num[5] = {1, 2, 3, 4, 5};

int sum = 0;
for (int i = 0; i < 5; i++) {
    sum += num[i];
}

std::cout << "Sum: " << sum << std::endl;
```

### Performing Comparison Operations on Arrays

You can perform comparison operations on arrays using the following syntax:

```c
int num[5] = {1, 2, 3, 4, 5};

bool allGreater = true;
for (int i = 0; i < 5; i++) {
    if (num[i] <= 0) {
        allGreater = false;
        break;
    }
}

std::cout << "All elements are greater than 0: " << (allGreater ? "Yes" : "No") << std::endl;
```

### 12.7: Array Indexing

======================

### Accessing Array Elements Using Index

You can access array elements using their index using the following syntax:

```c
int num[5] = {1, 2, 3, 4, 5};

std::cout << "First element: " << num[0] << std::endl;
```

### Assigning Values to Array Elements

You can assign values to array elements using the following syntax:

```c
int num[5] = {1, 2, 3, 4, 5};

num[0] = 10;

std::cout << "First element: " << num[0] << std::endl;
```

### 12.8: Array Search

=====================

### Searching for an Element in an Array

You can search for an element in an array using the following syntax:

```c
int num[5] = {1, 2, 3, 4, 5};

bool found = false;
for (int i = 0; i < 5; i++) {
    if (num[i] == 3) {
        found = true;
        break;
    }
}

std::cout << "Found: " << (found ? "Yes" : "No") << std::endl;
```

### Searching for a Range of Elements in an Array

You can search for a range of elements in an array using the following syntax:

```c
int num[5] = {1, 2, 3, 4, 5};

bool found = false;
for (int i = 0; i < 5; i++) {
    if (num[i] >= 3 && num[i] <= 4) {
        found = true;
        break;
    }
}

std::cout << "Found: " << (found ? "Yes" : "No") << std::endl;
```
