# Sparse Matrix Representation Using Linked Lists

## 1. Introduction and Background

A **sparse matrix** is defined as a matrix in which the majority of elements (typically > 90%) are zero. The efficient storage and manipulation of sparse matrices is a fundamental problem in computational science, numerical analysis, and database systems. Module 1 covered the **array-based triplet representation**, which stores only non-zero elements as `(row, column, value)` tuples in a 1D array. This section provides an in-depth treatment of the **linked list representation**, which offers significant advantages over array-based approaches for dynamic operations.

### Illustrative Example

Consider a 4×5 sparse matrix:

```
    Col 0    Col 1    Col 2    Col 3    Col 4
Row 0   0        0        3        0        4
Row 1   0        0        5        7        0
Row 2   0        0        0        0        0
Row 3   0        2        6        0        0
```

Non-zero elements: (0,2,3), (0,4,4), (1,2,5), (1,3,7), (3,1,2), (3,2,6) — only 6 out of 20 elements (30% density).

## 2. Limitations of Triplet Array Representation

While the triplet representation reduces storage from O(m×n) to O(k) where k is the number of non-zero elements, it suffers from several fundamental limitations:

| Limitation                        | Impact                                                                                   |
| --------------------------------- | ---------------------------------------------------------------------------------------- |
| **Fixed Size Allocation**         | Maximum number of non-zero elements must be known a priori; reallocation is costly       |
| **Sequential Insertion/Deletion** | Insertion or deletion requires shifting O(k) elements, resulting in O(k) time complexity |
| **Column Traversal Inefficiency** | Finding all elements in a specific column requires scanning the entire array             |
| **Matrix Operations Overhead**    | Transpose and addition operations require auxiliary arrays                               |

These limitations motivate the linked list representation, which provides dynamic memory allocation and efficient pointer-based operations.

## 3. Linked List Node Structure

Each non-zero element is stored as a node containing five fields:

```c
typedef struct SparseNode {
    int row;           // Row index of the element
    int col;           // Column index of the element
    int value;         // Non-zero value stored
    struct SparseNode *next_row;  // Pointer to next node in same column
    struct SparseNode *next_col;  // Pointer to next node in same row
} SparseNode;
```

**Field Purpose:**

- `row` and `col`: Maintain positional information for each element
- `value`: Stores the actual non-zero data
- `next_row`: Enables vertical traversal (down a column) — links elements in the same column
- `next_col`: Enables horizontal traversal (across a row) — links elements in the same row

## 4. Multilist (Cross-Linked) Representation

The sparse matrix is represented as a **multilist** (also called a orthogonal list), where each non-zero element belongs simultaneously to two linked lists:

1. **Row List**: All non-zero elements in row r, linked left-to-right via `next_col` pointers
2. **Column List**: All non-zero elements in column c, linked top-to-bottom via `next_row` pointers

### Header Node Structure

To facilitate O(1) access to the first element of each row and column, we employ header nodes:

```c
typedef struct SparseMatrix {
    int rows;              // Number of rows in the matrix
    int cols;              // Number of columns in the matrix
    int numNonZero;        // Count of non-zero elements (k)
    SparseNode **row_head; // Array of row header pointers (size: rows)
    SparseNode **col_head; // Array of column header pointers (size: cols)
} SparseMatrix;
```

Each `row_head[i]` points to the first non-zero element in row i, and each `col_head[j]` points to the first non-zero element in column j. If a row or column contains no non-zero elements, the corresponding header pointer is NULL.

### Visual Representation

For the example matrix:

```
        Col 0     Col 1     Col 2     Col 3     Col 4
        (NULL)    (3,1,2)   (0,2,3)   (1,3,7)   (0,4,4)
            |        |         |         |         |
Row 0  ---> NULL ---> NULL ---> (3) ---> NULL ---> (4) ---> NULL
            |                          |
Row 1  ---> NULL ---> NULL ---> (5) ---> (7) ---> NULL
            |
Row 2  ---> NULL ---> NULL ---> NULL ---> NULL ---> NULL
            |        |         |
Row 3  ---> NULL ---> (2) ---> (6) ---> NULL ---> NULL
```

## 5. Row-Major vs Column-Major Representation

Two primary variants of the linked representation exist, each with distinct performance characteristics:

### Row-Major Representation

- Elements within each row are sorted by column index
- `next_col` links traverse left-to-right within a row
- `next_row` links traverse top-to-bottom within a column

### Column-Major Representation

- Elements within each column are sorted by row index
- `next_row` links traverse top-to-bottom within a column
- `next_col` links traverse left-to-right within a row

### Complexity Comparison

| Operation                         | Row-Major         | Column-Major      |
| --------------------------------- | ----------------- | ----------------- |
| Traverse all elements in row i    | O(k_i + 1)\*      | O(k)              |
| Traverse all elements in column j | O(k)              | O(k_j + 1)\*      |
| Find element at (i, j)            | O(k_i) worst case | O(k_j) worst case |
| Insertion (sorted by position)    | O(k_i + k_j)      | O(k_i + k_j)      |

\*k_i = non-zeros in row i, k_j = non-zeros in column j

The multilist structure (using both row and column headers) effectively provides O(1) access to any row or column, making it optimal for applications requiring mixed access patterns.

## 6. Complete Algorithm Implementations

### 6.1 Matrix Creation

```c
SparseMatrix* createSparseMatrix(int rows, int cols) {
    SparseMatrix *mat = (SparseMatrix *)malloc(sizeof(SparseMatrix));
    mat->rows = rows;
    mat->cols = cols;
    mat->numNonZero = 0;

    // Allocate row header array
    mat->row_head = (SparseNode **)calloc(rows, sizeof(SparseNode *));
    // Allocate column header array
    mat->col_head = (SparseNode **)calloc(cols, sizeof(SparseNode *));

    return mat;
}
```

**Time Complexity:** O(m + n) where m = rows, n = columns  
**Space Complexity:** O(m + n) for header arrays

### 6.2 Node Creation

```c
SparseNode* createNode(int row, int col, int value) {
    SparseNode *node = (SparseNode *)malloc(sizeof(SparseNode));
    node->row = row;
    node->col = col;
    node->value = value;
    node->next_row = NULL;
    node->next_col = NULL;
    return node;
}
```

**Time Complexity:** O(1)  
**Space Complexity:** O(1) per node

### 6.3 Insertion Operation

The insertion maintains the multilist invariant — elements are sorted by column within each row and by row within each column:

```c
void insertElement(SparseMatrix *mat, int row, int col, int value) {
    // Reject zero values and invalid positions
    if (value == 0 || row < 0 || row >= mat->rows ||
        col < 0 || col >= mat->cols) {
        return;
    }

    // Create new node
    SparseNode *node = createNode(row, col, value);

    // ====== Insert into row list ======
    // Case 1: Empty row or new element precedes first element
    if (mat->row_head[row] == NULL || mat->row_head[row]->col > col) {
        node->next_col = mat->row_head[row];
        mat->row_head[row] = node;
    } else {
        // Case 2: Find proper position in row (sorted by column)
        SparseNode *curr = mat->row_head[row];
        while (curr->next_col != NULL && curr->next_col->col < col) {
            curr = curr->next_col;
        }
        node->next_col = curr->next_col;
        curr->next_col = node;
    }

    // ====== Insert into column list ======
    // Similar logic for column-wise insertion
    if (mat->col_head[col] == NULL || mat->col_head[col]->row > row) {
        node->next_row = mat->col_head[col];
        mat->col_head[col] = node;
    } else {
        SparseNode *curr = mat->col_head[col];
        while (curr->next_row != NULL && curr->next_row->row < row) {
            curr = curr->next_row;
        }
        node->next_row = curr->next_row;
        curr->next_row = node;
    }

    mat->numNonZero++;
}
```

**Time Complexity Analysis:**  
The insertion traverses both the row list and column list to find the correct position. If k_i is the number of non-zero elements in row i and k_j is the number in column j:

- Row insertion: O(k_i)
- Column insertion: O(k_j)
- **Total: O(k_i + k_j)** which is bounded by O(k) where k is total non-zeros

**Proof of Correctness:** The algorithm maintains sorted order in both lists by:

1. Traversing until the next element has index ≥ the new element's index
2. Inserting at that position, preserving the sorted invariant
3. Both row and column pointers are updated atomically, ensuring consistency

### 6.4 Traversal Operations

**Row-wise Traversal:**

```c
void traverseRow(SparseMatrix *mat, int row) {
    printf("Row %d: ", row);
    SparseNode *node = mat->row_head[row];
    while (node != NULL) {
        printf("(%d,%d,%d) ", node->row, node->col, node->value);
        node = node->next_col;
    }
    printf("\n");
}
```

**Column-wise Traversal:**

```c
void traverseColumn(SparseMatrix *mat, int col) {
    printf("Column %d: ", col);
    SparseNode *node = mat->col_head[col];
    while (node != NULL) {
        printf("(%d,%d,%d) ", node->row, node->col, node->value);
        node = node->next_row;
    }
    printf("\n");
}
```

**Complete Matrix Traversal:**

```c
void traverseAll(SparseMatrix *mat) {
    printf("Sparse Matrix (%dx%d) with %d non-zero elements:\n",
           mat->rows, mat->cols, mat->numNonZero);
    for (int i = 0; i < mat->rows; i++) {
        traverseRow(mat, i);
    }
}
```

**Time Complexity:** O(k) where k is the number of non-zero elements — each node is visited exactly once.

### 6.5 Search Operation

```c
SparseNode* searchElement(SparseMatrix *mat, int row, int col) {
    // Start from the beginning of the row
    SparseNode *node = mat->row_head[row];

    while (node != NULL && node->col <= col) {
        if (node->col == col) {
            return node;  // Found
        }
        node = node->next_col;
    }
    return NULL;  // Not found
}
```

**Time Complexity:** O(k_i) where k_i is the number of non-zeros in row i. In the worst case (element not present), we traverse the entire row.

### 6.6 Matrix Transpose

The transpose operation swaps row and column indices. Using the linked representation, we can achieve this without reallocation:

```c
SparseMatrix* transpose(SparseMatrix *mat) {
    // Create new matrix with swapped dimensions
    SparseMatrix *result = createSparseMatrix(mat->cols, mat->rows);

    // Traverse all elements and insert with swapped indices
    for (int i = 0; i < mat->rows; i++) {
        SparseNode *node = mat->row_head[i];
        while (node != NULL) {
            insertElement(result, node->col, node->row, node->value);
            node = node->next_col;
        }
    }
    return result;
}
```

**Time Complexity:** O(k × (k_i + k_j)) = O(k²) in the worst case, but O(k × m) or O(k × n) depending on matrix structure. Each insertion is O(k_i + k_j) and we perform k insertions.

### 6.7 Matrix Addition

Adding two sparse matrices A and B produces matrix C where C[i][j] = A[i][j] + B[i][j]:

```c
SparseMatrix* addMatrices(SparseMatrix *A, SparseMatrix *B) {
    if (A->rows != B->rows || A->cols != B->cols) {
        return NULL;  // Dimension mismatch
    }

    SparseMatrix *result = createSparseMatrix(A->rows, A->cols);

    // Traverse all elements of A
    for (int i = 0; i < A->rows; i++) {
        SparseNode *nodeA = A->row_head[i];
        while (nodeA != NULL) {
            // Check if B has element at same position
            SparseNode *nodeB = searchElement(B, nodeA->col, nodeA->row); // Note: search takes row first

            if (nodeB != NULL) {
                // Both matrices have element at this position
                int sum = nodeA->value + nodeB->value;
                if (sum != 0) {
                    insertElement(result, nodeA->row, nodeA->col, sum);
                }
                // Move B pointer
                nodeB = nodeB->next_col;
            } else {
                insertElement(result, nodeA->row, nodeA->col, nodeA->value);
            }
            nodeA = nodeA->next_col;
        }
    }

    // Add remaining elements from B
    for (int i = 0; i < B->rows; i++) {
        SparseNode *nodeB = B->row_head[i];
        while (nodeB != NULL) {
            SparseNode *nodeA = searchElement(A, nodeB->row, nodeB->col);
            if (nodeA == NULL) {
                insertElement(result, nodeB->row, nodeB->col, nodeB->value);
            }
            nodeB = nodeB->next_col;
        }
    }

    return result;
}
```

**Time Complexity:** O(k_A × k_B) in worst case due to search operations, where k_A and k_B are non-zero counts in matrices A and B respectively.

### 6.8 Deletion Operation

```c
void deleteElement(SparseMatrix *mat, int row, int col) {
    // Find and remove from row list
    SparseNode *prev = NULL;
    SparseNode *curr = mat->row_head[row];

    while (curr != NULL && curr->col < col) {
        prev = curr;
        curr = curr->next_col;
    }

    if (curr == NULL || curr->col != col) {
        return;  // Element not found
    }

    // Remove from row list
    if (prev == NULL) {
        mat->row_head[row] = curr->next_col;
    } else {
        prev->next_col = curr->next_col;
    }

    // Remove from column list
    prev = NULL;
    curr = mat->col_head[col];
    while (curr != NULL && curr->row < row) {
        prev = curr;
        curr = curr->next_row;
    }

    if (prev == NULL) {
        mat->col_head[col] = curr->next_row;
    } else {
        prev->next_row = curr->next_row;
    }

    free(curr);
    mat->numNonZero--;
}
```

**Time Complexity:** O(k_i + k_j) — traversing both row and column lists to find and remove the element.

## 7. Complete Example with Driver Program

```c
#include <stdio.h>
#include <stdlib.h>

// [Include all structures and functions defined above]

int main() {
    // Create a 4x5 sparse matrix
    SparseMatrix *mat = createSparseMatrix(4, 5);

    // Insert non-zero elements
    insertElement(mat, 0, 2, 3);
    insertElement(mat, 0, 4, 4);
    insertElement(mat, 1, 2, 5);
    insertElement(mat, 1, 3, 7);
    insertElement(mat, 3, 1, 2);
    insertElement(mat, 3, 2, 6);

    // Display the matrix
    printf("Original Sparse Matrix:\n");
    traverseAll(mat);

    // Search for element
    SparseNode *found = searchElement(mat, 1, 3);
    if (found) {
        printf("\nElement at (1,3): %d\n", found->value);
    }

    // Transpose
    SparseMatrix *trans = transpose(mat);
    printf("\nTransposed Matrix:\n");
    traverseAll(trans);

    return 0;
}
```

**Expected Output:**

```
Original Sparse Matrix (4x5) with 6 non-zero elements:
Row 0: (0,2,3) (0,4,4)
Row 1: (1,2,5) (1,3,7)
Row 2:
Row 3: (3,1,2) (3,2,6)

Element at (1,3): 7

Transposed Matrix (5x4) with 6 non-zero elements:
Row 0:
Row 1: (1,3,2)
Row 2: (2,0,3) (2,1,5) (2,3,6)
Row 3: (3,1,7)
Row 4: (4,0,4)
```

## 8. Summary of Complexity Analysis

| Operation       | Time Complexity    | Space Complexity |
| --------------- | ------------------ | ---------------- |
| Create Matrix   | O(m + n)           | O(m + n)         |
| Insert Element  | O(k_i + k_j)       | O(1)             |
| Delete Element  | O(k_i + k_j)       | O(1)             |
| Search Element  | O(k_i)             | O(1)             |
| Traverse Row    | O(k_i)             | O(1)             |
| Traverse Column | O(k_j)             | O(1)             |
| Traverse All    | O(k)               | O(1)             |
| Transpose       | O(k × (k_i + k_j)) | O(k)             |
| Matrix Addition | O(k_A × k_B)       | O(k_A + k_B)     |

Where: m = rows, n = columns, k = total non-zeros, k_i = non-zeros in row i, k_j = non-zeros in column j.

## 9. Advantages and Disadvantages

### Advantages

1. **Dynamic Size**: Memory allocated as needed; no pre-allocation required
2. **Efficient Insertion/Deletion**: O(1) pointer adjustment (locally) without element shifting
3. **Efficient Row/Column Access**: O(k_i) or O(k_j) traversal using header nodes
4. **No Memory Waste**: Only non-zero elements stored; no space for zeros
5. **Suitable for Matrix Operations**: Pointer manipulation facilitates transpose and addition

### Disadvantages

1. **Memory Overhead**: Each node stores two pointers (16 bytes on 64-bit systems) plus metadata
2. **Complex Implementation**: More intricate than array-based approaches
3. **No Direct Random Access**: Cannot access A[i][j] directly; requires traversal
4. **Cache Inefficiency**: Non-contiguous memory allocation affects cache performance

## 10. Application-Based Questions

### Question 1

Given a sparse matrix represented using the multilist structure with row and column headers, what is the time complexity to find all non-zero elements in column j?

**(A)** O(m × n)  
**(B)** O(k)  
**(C)** O(k_j) where k_j is the number of non-zeros in column j  
**(D)** O(1)

**Answer:** (C) Using the column header `col_head[j]`, we can directly access the first element in column j and traverse down using `next_row` pointers, visiting exactly k_j nodes.

### Question 2

A sparse matrix has dimensions 1000 × 1000 with only 50 non-zero elements. What is the space complexity for storing this matrix using the linked list representation?

**(A)** O(1,000,000)  
**(B)** O(50)  
**(C)** O(50 + 1000 + 1000)  
**(D)** O(50 × 2)

**Answer:** (C) Space required = k nodes × 5 fields each + row headers (m) + column headers (n). For k=50, m=1000, n=1000: O(50 + 2000) = O(2050).

### Question 3

In the multilist representation, if we insert element (2, 3, 15) into a sparse matrix, which pointers need to be updated?

**(A)** Only next_row of node in row 2  
**(B)** Only next_col of node in column 3  
**(C)** Both next_row and next_col of the new node, plus adjacent nodes  
**(D)** No pointer updates needed

**Answer:** (C) The new node's `next_row` must point to the current first element in column 3, and `next_col` must point to the current first element in row 2. Additionally, the previous first elements in both row 2 and column 3 must be updated to point to the new node.

### Question 4

Consider two sparse matrices A and B, each with dimensions m × n and k non-zero elements. What is the worst-case time complexity of adding these matrices using the linked list representation?

**(A)** O(m + n)  
**(B)** O(k)  
**(C)** O(k²)  
**(D)** O(k_A × k_B)

**Answer:** (D) For each non-zero element in A, we may search the entire matrix B (O(k_B) in worst case), resulting in O(k_A × k_B).
