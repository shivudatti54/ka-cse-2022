# Two Dimensional Arrays - Summary

## Key Definitions and Concepts

- **Two Dimensional Array:** A collection of elements of the same type arranged in rows and columns, accessed using two indices.
- **Row-Major Order:** C's method of storing 2D arrays where all elements of row 0 are stored first, followed by all elements of row 1, and so on.
- **Matrix:** A mathematical representation of a 2D array, commonly used in linear algebra.
- **Element Address Formula:** Address of a[i][j] = Base + (i × columns + j) × sizeof(datatype)

## Important Formulas and Theorems

- **Total Elements:** For array[m][n], total elements = m × n
- **Memory Required:** bytes = rows × cols × sizeof(datatype)
- **Address Calculation:** 
  - Row-major: `&A[i][j] = base + (i × N + j) × size`
  - Where N is the number of columns
- **Valid Index Range:** 0 to (rows-1) for row index, 0 to (cols-1) for column index

## Key Points

- Two dimensional arrays in C are declared as `data_type array_name[rows][cols]`
- Both dimensions must be constant expressions except in C99 with VLAs
- Initialization can be done using nested braces: `int arr[2][3] = {{1,2,3},{4,5,6}}`
- The first dimension can be omitted when initializing: `int arr[][3] = {...}`
- When passing to functions, only the second dimension must be specified
- Row-wise traversal is more cache-efficient than column-wise traversal
- Uninitialized arrays contain garbage values
- Array indices start from 0, not 1
- Common operations include transpose, addition, multiplication, and finding sums

## Common Mistakes to Avoid

- Forgetting that array indices start from 0 and accessing index [rows] instead of [rows-1]
- Omitting the column dimension when declaring function parameters for 2D arrays
- Not initializing arrays before using them in calculations, leading to garbage results
- Confusing row and column indices—remember row comes first: array[row][col]
- Attempting to return a 2D array from a function directly without using pointers or dynamic allocation

## Revision Tips

- Practice writing declaration, initialization, and access patterns until they become automatic
- Memorize the address calculation formula as it frequently appears in exams
- Implement all basic matrix operations (addition, transpose, multiplication) multiple times
- Trace through small 2D array examples on paper to reinforce understanding of nested loops
- Remember that when you see `arr[i][j]`, the first index i represents the row and the second index j represents the column