# Multidimensional Arrays

## Overview

Multidimensional arrays are arrays of arrays that extend beyond one dimension to represent data in multiple dimensions like tables (2D), cubes (3D), or higher-dimensional structures. They are stored in row-major order and are useful for complex data representations.

## Key Points

- **Array of Arrays**: Each dimension adds another level of indexing to access elements
- **Row-Major Storage**: Elements stored layer by layer, then row by row, then column by column
- **Memory Layout**: Contiguous storage with address calculation based on all dimensions
- **Initialization Methods**: Full, partial, flattened, or omitting first dimension only
- **Access Pattern**: Nested loops required for each dimension (layer, row, column)
- **Function Parameters**: Must specify all dimensions except the first when passing to functions
- **Dynamic Allocation**: Possible using pointers to pointers for flexible sizing

## Important Concepts

- 2D arrays visualized as tables, 3D as cubes or collection of tables
- Time complexity for accessing single element remains O(1) regardless of dimensions
- Space complexity is O(n^k) for k-dimensional arrays with n elements per dimension
- Common applications include matrices, image processing (RGB), scientific data, and game development
- Static allocation has fixed size, dynamic allocation allows runtime sizing

## Notes

- Remember row-major order for memory layout questions
- Practice writing nested loops for different dimensional arrays
- Know the initialization syntax differences between static and dynamic allocation
- Understand pointer arithmetic for multidimensional array access
- Be able to calculate total memory usage for given dimensions
