# Textbook 1: Ch - Introduction to Data Structures

## Module: Arrays

### Introduction, One-Dimensional Arrays, Two-Dimensional Arrays

#### Key Points

- **Definition:** An array is a collection of elements of the same data type stored in contiguous memory locations.
- **One-Dimensional Arrays:**
  - A single row or column of elements.
  - Typically denoted by square brackets `[]`.
  - Example: `int scores[5] = {90, 85, 95, 88, 92};`
- **Two-Dimensional Arrays:**
  - A table of elements, where each element is an array of a specific type.
  - Typically denoted by square brackets `[]` with a row and column index.
  - Example: `int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};`
- **Initializing Two-Dimensional Arrays:**
  - Elements are initialized using curly brackets `{}`.
  - Example: `int scores[2][3] = {{90, 85, 95}, {88, 92, 76}};`

#### Important Formulas and Definitions

- **Array Indexing:**
  - Elements are accessed using their index, starting from 0.
  - Example: `scores[0]` accesses the first element.
- **Array Operations:**
  - Arithmetic operations can be performed on arrays.
  - Example: `scores[0] += 5;` increments the first element by 5.

#### Theorems

- **Theorem:** An array of `n` elements can be accessed and modified using a single pointer.
- **Proof:** By using the index operator `[]` to access and modify elements.
