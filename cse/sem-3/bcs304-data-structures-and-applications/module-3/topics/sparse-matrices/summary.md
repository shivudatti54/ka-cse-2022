# Sparse Matrices

## Overview

A sparse matrix is a matrix in which most elements are zero. Using linked lists can efficiently represent sparse matrices, overcoming limitations of array-based representations. This summary covers key concepts, node structure, and operations like transpose and addition.

## Key Points

- A sparse matrix has most elements as zero, making array representations inefficient.
- Linked lists can represent sparse matrices, allowing dynamic allocation and efficient insertion/deletion.
- Each non-zero element is a node with five fields: row, col, value, next_row, and next_col.
- The multilist representation uses header nodes to anchor row and column lists.
- Transpose is achieved by swapping row/col indices and rebuilding header arrays.
- Addition is done by merging row lists, handling elements in A, B, or both.
- Linked lists are suitable for dynamic matrices or when column-wise access is needed.

## Important Definitions

- **Sparse Matrix**: A matrix with most elements as zero.
- **Node**: A structure representing a non-zero element with five fields.
- **Multilist**: A linked list representation using header nodes for rows and columns.
- **Transpose**: Swapping row and column indices to convert rows to columns and vice versa.

## Key Formulas / Syntax

- Node structure: `typedef struct SparseNode { int row; int col; int value; struct SparseNode *next_row; struct SparseNode *next_col; } SparseNode;`
- Transpose algorithm: `SparseMatrix* transposeSparse(SparseMatrix *mat) { ... }`
- Addition algorithm: `SparseMatrix* addSparse(SparseMatrix *A, SparseMatrix *B) { ... }`

## Comparisons

| Aspect        | Array (Triplet)     | Linked List (Multilist) |
| ------------- | ------------------- | ----------------------- |
| Memory        | Fixed array         | Dynamic allocation      |
| Insertion     | O(n)                | O(r + c)                |
| Deletion      | O(n)                | O(r + c)                |
| Row access    | Scan entire array   | Direct via row_head     |
| Column access | Scan entire array   | Direct via col_head     |
| Transpose     | O(cols \* non_zero) | O(non_zero)             |
| Addition      | O(nA + nB)          | O(nA + nB)              |

## Exam Tips

- Draw the multilist representation of a given sparse matrix.
- Write the C struct for a node with all five fields.
- Compare array and linked list representations.
- Understand the transpose algorithm.
- Know the addition algorithm for merging row lists.
- Choose the right representation based on matrix characteristics.
- Always state the number of non-zero elements and matrix dimensions.
