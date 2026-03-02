# **Revision Notes for 8.1 to 8.5: Introduction to Arrays**

### 8.1: Arrays - Introduction

- An array is a collection of elements of the same data type stored in contiguous memory locations.
- Arrays are useful for storing and manipulating large datasets efficiently.
- Key characteristics:
  - Fixed size
  - Homogeneous elements
  - Can be initialized using the data type or values

### 8.2: One-Dimensional Arrays

- A one-dimensional array is an array that can store elements of the same data type in a single dimension.
- Declaration syntax: `data-type array-name[array-size];`
- Example: `int scores[5];` declares an array of 5 integers

### 8.3: Two-Dimensional Arrays

- A two-dimensional array is an array that can store elements of the same data type in two dimensions.
- Declaration syntax: `data-type array-name[row-size][column-size];`
- Example: `int scores[3][4];` declares a 3x4 two-dimensional array of integers

### 8.4: Initializing Two-Dimensional Arrays

- Elements can be initialized using the first row or column.
- Example: `int scores[3][4] = {{10, 20, 30, 40}, {50, 60, 70, 80}, {90, 100, 110, 120}};` initializes a 3x4 array

### 8.5: Important Formulas and Definitions

- **Array Index** (or **Row Index** and **Column Index**): (row, column)
- **Array Subscripting**:
  - `arr[row][column]`: access element at row `row` and column `column`
  - `arr[i][j]`: access element at row `i` and column `j`
- **Array Slicing**:
  - `arr[i..j]`: access elements from row `i` to row `j`
  - `arr[i..]`: access elements from row `i` to the end of the array
  - `arr[..j]`: access elements from the beginning of the array to row `j`
