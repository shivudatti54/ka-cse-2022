# Representation of Multidimensional Arrays

## Overview

Multidimensional arrays are stored in linear memory using either row-major or column-major order. Understanding the storage order and address calculation formulas is crucial for programming and optimizing array operations. This summary covers the key concepts, formulas, and tips for exams.

## Key Points

- Multidimensional arrays are mapped onto one-dimensional physical memory.
- Row-major order stores elements row by row, while column-major order stores elements column by column.
- C, C++, and Java use row-major order, while FORTRAN and MATLAB use column-major order.
- Address calculation formulas depend on the storage order and indexing (0-based or 1-based).
- Cache performance is affected by the traversal order, with row-major traversal being faster in C.

## Important Definitions

- **Row-major order**: Elements are stored row by row in memory.
- **Column-major order**: Elements are stored column by column in memory.
- **Spatial locality**: The tendency of a program to access nearby memory locations, improving cache performance.

## Key Formulas / Syntax

- Row-major address formula (0-based): `B + (i * N + j) * w`
- Row-major address formula (1-based): `B + ((i - 1) * N + (j - 1)) * w`
- Column-major address formula (0-based): `B + (j * M + i) * w`
- Column-major address formula (1-based): `B + ((j - 1) * M + (i - 1)) * w`

## Comparisons

| Aspect              | Row-Major         | Column-Major      |
| ------------------- | ----------------- | ----------------- |
| Storage order       | Row by row        | Column by column  |
| Used by             | C, C++, Java      | FORTRAN, MATLAB   |
| Formula (0-based)   | B + (i*N + j) * w | B + (j*M + i) * w |
| Cache-friendly in C | Yes               | No                |

## Exam Tips

- Memorize both row-major and column-major address formulas for 0-based and 1-based indexing.
- Identify the storage order and indexing used in the problem.
- Practice address calculations for 2D and 3D arrays.
- Remember that C always uses row-major order.
- Understand how cache performance is affected by traversal order.
