# Two-Dimensional Arrays

## Overview

Two-dimensional arrays store elements in a tabular format with rows and columns, forming a matrix-like structure. They are stored in row-major order in contiguous memory and are useful for representing grids, matrices, and spreadsheet data.

## Key Points

- **Declaration Syntax**: `data_type array_name[rows][columns];` specifies dimensions
- **Row-Major Order**: All elements of row 0 stored first, then row 1, and so on
- **Memory Calculation**: Total memory = rows × columns × sizeof(data_type)
- **Access Pattern**: Elements accessed using two indices: array[row_index][column_index]
- **Initialization Methods**: Fully specified, partial, flattened, or omitting row dimension
- **Nested Loops**: Processing requires outer loop for rows, inner loop for columns
- **Pointer Notation**: array[i][j] equivalent to _(_(array + i) + j)

## Important Concepts

- Row dimension can be omitted in initialization, but column dimension must be specified
- Common operations include row-wise sum, column-wise sum, and matrix traversal
- Applications include matrix operations, image processing, game boards, and graphs
- Accessing elements in row-major order provides better cache performance
- Time complexity for traversal is O(n×m) where n is rows and m is columns

## Notes

- Remember that 2D arrays are stored contiguously in row-major order
- Practice initializing arrays using different methods
- Understand pointer relationship for accessing elements
- Be able to write nested loops for processing 2D arrays
- Know common applications like matrix addition and adjacency matrices
