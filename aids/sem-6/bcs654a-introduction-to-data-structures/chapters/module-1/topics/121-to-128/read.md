# **12.1: Introduction to Arrays**

### Definition

An array is a collection of elements of the same data type stored in contiguous memory locations. It is a fundamental data structure in programming, allowing for efficient storage and manipulation of data.

### Characteristics

- A collection of elements of the same data type
- Elements are stored in contiguous memory locations
- Array indices are used to access and manipulate elements

### Types of Arrays

- **One-Dimensional Arrays**: An array where each element is accessed using a single index.
- **Two-Dimensional Arrays**: An array where each element is accessed using a pair of indices (row and column).

### Benefits of Arrays

- Efficient storage and manipulation of data
- Fast access and modification of elements
- Allow for dynamic memory allocation

### Example

```c
int scores[5] = {90, 85, 95, 80, 92};
```

In this example, `scores` is a one-dimensional array containing five integer elements.

# **12.2: Initializing an Array**

### Methods of Initialization

- **Direct Initialization**: Elements are initialized directly when the array is declared.
- **Indirect Initialization**: Elements are initialized using an array of initial values.
- **Nested Initialization**: Sub-arrays are initialized using nested arrays.

### Example

```c
int scores[5] = {90, 85, 95, 80, 92};

// Direct initialization
int grades[3] = {90, 85, 95};
```

# **12.3: Working with One-Dimensional Arrays**

### Accessing Elements

- **Indexing**: Elements are accessed using their index value.
- **Array Operations**: Operations can be performed on arrays, such as adding or multiplying elements.

### Example

```c
int scores[5] = {90, 85, 95, 80, 92};

// Accessing elements
int score1 = scores[0];  // score1 = 90
int score2 = scores[scores.length - 1];  // score2 = 92

// Array operations
int sum = 0;
for (int i = 0; i < scores.length; i++) {
    sum += scores[i];
}
```

# **12.4: Working with Two-Dimensional Arrays**

### Accessing Elements

- **Indexing**: Elements are accessed using a pair of index values (row and column).
- **Array Operations**: Operations can be performed on 2D arrays, such as adding or multiplying elements.

### Example

```c
int scores[2][3] = {
    {90, 85, 95},
    {80, 92, 88}
};

// Accessing elements
int score1 = scores[0][0];  // score1 = 90
int score2 = scores[1][2];  // score2 = 88

// Array operations
int sum = 0;
for (int i = 0; i < scores.length; i++) {
    for (int j = 0; j < scores[i].length; j++) {
        sum += scores[i][j];
    }
}
```

# **12.5: Initializing a 2D Array**

### Methods of Initialization

- **Direct Initialization**: Elements are initialized directly when the array is declared.
- **Indirect Initialization**: Elements are initialized using nested arrays.
- **Nested Initialization**: Sub-arrays are initialized using nested arrays.

### Example

```c
int scores[2][3] = {
    {90, 85, 95},
    {80, 92, 88}
};

// Direct initialization
int grades[3][2] = {
    {90, 85},
    {80, 92},
    {95, 88}
};
```

# **12.6: Total and Available Memory**

### Calculating Total Memory

- **Total Memory**: The total amount of memory allocated to an array.
- **Available Memory**: The amount of free memory available for use.

### Example

```c
int scores[5] = {90, 85, 95, 80, 92};

// Calculating total memory
int totalMemory = sizeof(scores);
System.out.println("Total memory: " + totalMemory);

// Calculating available memory
int availableMemory = totalMemory - sizeof(scores[0]);
System.out.println("Available memory: " + availableMemory);
```

# **12.7: Dynamic Memory Allocation**

### Methods of Dynamic Allocation

- **Using `malloc()`**: Dynamically allocates memory using the `malloc()` function.
- **Using `calloc()`**: Dynamically allocates memory using the `calloc()` function.
- **Using `realloc()`**: Dynamically allocates memory using the `realloc()` function.

### Example

```c
int* scores = (int*)malloc(5 * sizeof(int));
if (scores == NULL) {
    System.out.println("Memory allocation failed");
    return;
}

// Initialize scores
scores[0] = 90;
scores[1] = 85;
scores[2] = 95;
scores[3] = 80;
scores[4] = 92;

// Deallocate memory
free(scores);
```

# **12.8: Memory Deallocation**

### Methods of Deallocation

- **Using `free()`**: Deallocates memory using the `free()` function.

### Example

```c
int* scores = (int*)malloc(5 * sizeof(int));
if (scores == NULL) {
    System.out.println("Memory allocation failed");
    return;
}

// Initialize scores
scores[0] = 90;
scores[1] = 85;
scores[2] = 95;
scores[3] = 80;
scores[4] = 92;

// Deallocate memory
free(scores);
```

### Best Practices

- Always deallocate memory when it's no longer needed.
- Use `free()` to deallocate memory.
- Avoid using `malloc()` inside a loop, as it can lead to memory leaks.
- Use `calloc()` to initialize memory to zero.
- Use `realloc()` to dynamically resize arrays.
