# Arrays - Summary

## Key Definitions and Concepts

- **Array**: A homogeneous collection of elements stored in contiguous memory locations, accessible through indices
- **One-Dimensional Array**: Linear collection with single index access
- **Two-Dimensional Array**: Tabular structure with row and column indices (matrix form)
- **Sparse Matrix**: Matrix where most elements are zero; stored using special representations to save memory
- **Dynamic Array**: Arrays allocated at runtime using heap memory

## Important Formulas and Theorems

**1D Array Address**:
```
Address(arr[i]) = B + i × w
```
where B = base address, w = word size (bytes per element)

**2D Array Address (Row-Major)**:
```
Address(A[i][j]) = B + (i × n + j) × w
```
where n = number of columns

**2D Array Address (Column-Major)**:
```
Address(A[i][j]) = B + (j × m + i) × w
```
where m = number of rows

## Key Points

- Arrays provide O(1) constant time access to any element via index
- Array indices start from 0 in C/C++ (zero-based indexing)
- C uses row-major order; elements stored row by row in memory
- Dynamic arrays use malloc/calloc for memory allocation at runtime
- Sparse matrices store only non-zero elements, reducing space complexity
- Polynomials can be represented as arrays where index = exponent, value = coefficient
- Arrays are homogeneous - all elements must be of the same data type
- Array name serves as a pointer to the first element (base address)

## Common Mistakes to Avoid

1. **Index Out of Bounds**: Remember that valid indices go from 0 to (size-1), not 1 to size
2. **Confusing Row-Major and Column-Major**: C uses row-major; always clarify in exam answers
3. **Forgetting to Free Dynamic Memory**: Always use free() after malloc/calloc to prevent memory leaks
4. **Incorrect Address Calculation**: Double-check formulas - common error is using row count instead of column count

## Revision Tips

1. Practice address calculation problems repeatedly - they appear frequently in exams
2. Write small C programs to implement array operations (traversal, search, transpose)
3. Create a table comparing static vs dynamic arrays, row-major vs column-major
4. Memorize the time complexities: Access O(1), Search O(n), Insertion O(n), Deletion O(n)
5. Solve previous year DU question papers to understand the exam pattern and important topics