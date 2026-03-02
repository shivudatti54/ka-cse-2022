# **2.1 Introduction to Arrays**

### Definition and Concept

An array is a collection of elements of the same data type stored in contiguous memory locations. It is a fundamental data structure in programming that allows us to store and manipulate large amounts of data efficiently.

### Key Characteristics

- A fixed number of elements
- All elements are of the same data type
- Elements are stored in contiguous memory locations
- Arrays can be one-dimensional or two-dimensional

### Importance of Arrays

Arrays are used in various applications, such as:

- Storing data in a spreadsheet or table
- Representing matrices and vectors in linear algebra
- Implementing algorithms and data structures, such as sorting and searching

# **2.2 One-Dimensional Arrays**

### Definition

A one-dimensional array, also known as a vector or a sequence, is an array that contains elements of the same data type in a single row or column.

### Syntax

The syntax for declaring a one-dimensional array is as follows:

```c
type array_name[length];
```

For example:

```c
int scores[5];
```

This declares an array called `scores` with five elements of type `int`.

### Operations on One-Dimensional Arrays

- Indexing: Accessing an element using its index, which is the position of the element in the array.

      ```c

  int scores[5] = {10, 20, 30, 40, 50};
  int fifth_score = scores[4];

````

*   Assigning values: Assigning a new value to an element using its index.

    ```c
int scores[5] = {10, 20, 30, 40, 50};
scores[2] = 35;
````

### Examples

- Storing exam scores in an array:

      ```c

  int scores[5] = {10, 20, 30, 40, 50};
  for (int i = 0; i < 5; i++) {
  printf("Score %d: %d\n", i + 1, scores[i]);
  }

````

*   Calculating the average score:

    ```c
int scores[5] = {10, 20, 30, 40, 50};
int sum = 0;
for (int i = 0; i < 5; i++) {
    sum += scores[i];
}
double average = (double) sum / 5;
printf("Average score: %.2f\n", average);
````

# **2.3 Two-Dimensional Arrays**

### Definition

A two-dimensional array, also known as a matrix or a table, is an array that contains elements of the same data type in multiple rows and columns.

### Syntax

The syntax for declaring a two-dimensional array is as follows:

```c
type array_name[row_length][column_length];
```

For example:

```c
int scores[3][4];
```

This declares a two-dimensional array called `scores` with three rows and four columns, where each element is of type `int`.

### Operations on Two-Dimensional Arrays

- Indexing: Accessing an element using its row and column indices.

      ```c

  int scores[3][4] = {
  {10, 20, 30, 40},
  {50, 60, 70, 80},
  {90, 100, 110, 120}
  };
  int first_score = scores[0][0];

````

*   Assigning values: Assigning a new value to an element using its row and column indices.

    ```c
int scores[3][4] = {
    {10, 20, 30, 40},
    {50, 60, 70, 80},
    {90, 100, 110, 120}
};
scores[1][2] = 75;
````

### Examples

- Storing grades in a matrix:

      ```c

  int grades[3][4] = {
  {90, 80, 70, 60},
  {70, 60, 50, 40},
  {40, 30, 20, 10}
  };
  for (int i = 0; i < 3; i++) {
  for (int j = 0; j < 4; j++) {
  printf("Grade %d, %d: %d\n", i + 1, j + 1, grades[i][j]);
  }
  }

````

*   Calculating the average grade:

    ```c
int grades[3][4] = {
    {90, 80, 70, 60},
    {70, 60, 50, 40},
    {40, 30, 20, 10}
};
int sum = 0;
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        sum += grades[i][j];
    }
}
double average = (double) sum / 12;
printf("Average grade: %.2f\n", average);
````
