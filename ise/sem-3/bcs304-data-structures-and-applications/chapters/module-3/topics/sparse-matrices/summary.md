# Sparse Matrices - Summary

## Key Definitions and Concepts

- **Sparse Matrix**: A matrix where most elements are zero; typically defined when non-zero elements constitute less than 10-50% of total elements
- **Sparsity**: Ratio of zero elements to total elements (zeros/(m×n)); complement is density
- **Triplet Form**: Storage scheme storing each non-zero element as (row_index, column_index, value)
- **CSR (Compressed Sparse Row)**: Array-based format using VALUES, COL_INDICES, and ROW_PTR arrays
- **CSC (Compressed Sparse Column)**: Column-oriented version of CSR using VALUES, ROW_INDICES, and COL_PTR arrays

## Important Formulas and Theorems

- **Space Comparison**: Dense storage = m×n locations; Sparse storage ≈ 3k locations (where k = non-zero count)
- **Sparsity Calculation**: Sparsity = (m×n - k) / (m×n), where k is count of non-zero elements
- **CSR ROW_PTR**: ROW_PTR[i] gives starting index of row i in VALUES array; ROW_PTR has m+1 elements
- **Time Complexity Principle**: Sparse algorithms should have complexity expressed in terms of k (non-zeros) rather than m×n

## Key Points

- Sparse matrices arise frequently in web connectivity, finite element methods, social networks, and recommendation systems
- Triplet representation is simplest and serves as foundation for understanding other formats
- CSR excels at row-wise operations and matrix-vector multiplication
- CSC is preferred for column-oriented operations and algorithms
- Linked list representation supports dynamic insertion/deletion but has slower random access
- Sparse storage provides significant memory savings when density is below 30-40%
- Operations on sparse matrices should skip zero elements to maintain efficiency

## Common Mistakes to Avoid

- Confusing row and column indices when constructing CSR/CSC formats
- Forgetting that ROW_PTR has m+1 elements (extra element stores total count)
- Applying sparse storage to dense matrices, which wastes memory on index overhead
- Incorrectly calculating starting and ending positions in VALUES array when extracting rows/columns
- Mixing up CSR and CSC characteristics in exam questions

## Revision Tips

- Practice converting between dense, triplet, CSR, and CSC representations multiple times
- Memorize the three-array structure for both CSR and CSC with clear understanding of each array's purpose
- Work through at least two examples of each conversion type to build procedural memory
- Remember the key advantage: sparse storage complexity depends on non-zero count, not total elements
- Review linked list variant for sparse matrices to understand dynamic modification scenarios