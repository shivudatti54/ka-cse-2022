# Sparse Matrices - Summary

## Key Definitions and Concepts

- **Sparse Matrix**: A matrix in which most elements (typically more than 50-70%) are zero. The sparsity is calculated as (total_elements - non_zero_elements) / total_elements.

- **Triplet Representation**: A method storing only non-zero elements along with their row index, column index, and value in a compact three-column array format.

- **Linked Representation**: Uses nodes containing row index, column index, value, and pointers (right/down) to create a two-dimensional linked structure.

## Important Formulas and Theorems

- **Memory for Dense Matrix**: M × N integer locations
- **Memory for Triplet**: (NZ + 1) × 3 locations where NZ is number of non-zero elements
- **Sparsity**: (M×N - NZ) / (M×N)
- **Fast Transpose Time Complexity**: O(NZ + columns) compared to O(NZ × columns) for simple transpose

## Key Points

- Sparse matrices are used to optimize memory when dealing with matrices containing mostly zero values.

- Triplet representation stores only non-zero elements with their coordinates, dramatically reducing memory for highly sparse matrices.

- Fast transpose algorithm pre-computes column counts to place elements directly in correct positions.

- Linked representation provides dynamic memory allocation and efficient insertion/deletion of non-zero elements.

- The cross-linked representation uses two pointers per node—right pointer for next element in row, down pointer for next element in column.

- Sparse matrix operations (transpose, addition) must handle the case when corresponding positions in both matrices are non-zero (add values), one is non-zero (copy value), or both are zero (exclude from result).

- Dense representation becomes preferable when sparsity is less than 50% approximately.

## Common Mistakes to Avoid

- Confusing row and column indices—remember arrays are typically row-major (elements stored row by row).

- Forgetting to update the header row in triplet representation with correct matrix dimensions and non-zero count.

- In fast transpose, failing to maintain separate arrays for counting elements and calculating starting positions.

- Including zero values in sparse representation—only non-zero elements should be stored.

## Revision Tips

- Practice converting between matrix form and triplet representation until it becomes automatic.

- Trace through the fast transpose algorithm step-by-step on paper multiple times.

- Memorize the node structure for linked representation: row, col, value, right, down.

- Solve at least 5-10 previous year examination questions on this topic.

- Understand when to use dense vs sparse representation based on sparsity percentage.