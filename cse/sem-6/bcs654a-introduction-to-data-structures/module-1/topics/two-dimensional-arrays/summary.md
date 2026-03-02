# Two-Dimensional Arrays

## Overview

Two-dimensional arrays extend the concept of linear arrays to represent tabular data with rows and columns. They are stored in row-major order in contiguous memory locations and are essential for matrix operations, game boards, and image processing applications.

## Key Points

- **Tabular Format**: Organized as a matrix with rows and columns for structured data representation
- **Memory Layout**: Row-major order storage means all elements of row 0, then row 1, consecutively
- **Declaration**: `data_type array_name[rows][columns];` with both dimensions specified
- **Initialization Flexibility**: Fully specified with braces, partial, flattened, or row dimension omitted
- **Element Access**: Uses two indices array[i][j] where i is row, j is column (both zero-based)
- **Processing Pattern**: Nested loops with outer loop iterating rows, inner loop iterating columns
- **Pointer Relationship**: Array name points to first row; \*(matrix[i] + j) accesses element

## Important Concepts

- Total memory required is rows × columns × sizeof(data_type) bytes
- Column dimension must always be specified, row dimension can be compiler-deduced
- Row-wise and column-wise operations have different time complexities
- Common operations include sum calculation, transposition, and matrix multiplication
- Better cache performance achieved by processing in row-major order

## Notes

- Always be mindful of index boundaries to avoid undefined behavior
- Understand pointer notation equivalence: array[i][j] ≡ _(_(array + i) + j)
- Practice writing functions to process 2D arrays with proper parameter passing
- Know applications in mathematical operations, image processing, and graph algorithms
- Remember partial initialization sets unspecified elements to zero
