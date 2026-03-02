# Arrays in C: One-Dimensional and Two-Dimensional Operations - Summary

## Key Definitions and Concepts

- **Array:** A homogeneous data structure storing multiple elements of the same data type in contiguous memory locations, accessible via indices.
- **One-Dimensional Array:** Linear collection of elements accessed using a single index (0 to n-1).
- **Two-Dimensional Array:** Matrix-like structure with rows and columns, accessed using two indices.
- **Row-Major Order:** C stores 2D arrays row-by-row in contiguous memory.
- **Sparse Matrix:** A matrix with more zero elements than non-zero elements.

## Important Formulas and Theorems

- **Address Calculation:** `&arr[i] = base_address + (i × sizeof(datatype))`
- **2D Array Address:** `&A[i][j] = base + ((i × cols) + j) × sizeof(datatype)`
- **Binary Search Condition:** Array must be sorted before application
- **Matrix Multiplication Dimensions:** If A is (m×n) and B is (n×p), then C is (m×p)
- **Time Complexity - Linear Search:** O(n)
- **Time Complexity - Binary Search:** O(log n)
- **Time Complexity - Bubble Sort:** O(n²)

## Key Points

1. Array indices in C start from 0, not 1; accessing arr[-1] or arr[n] causes undefined behavior.

2. Array name acts as a constant pointer pointing to the first element's address.

3. For 2D arrays passed to functions, at least the second dimension must be specified: `void func(int arr[][10])`.

4. Bubble sort repeatedly swaps adjacent elements if they're in wrong order; stable sort maintaining relative order of equal elements.

5. Binary search requires sorted array and has O(log n) complexity but only works on sorted data.

6. Matrix addition requires both matrices to have identical dimensions.

7. When passing arrays to functions, always pass the size as a separate parameter since `sizeof()` gives pointer size inside functions.

8. Initialization at declaration: `int arr[5] = {1,2,3,4,5};` is valid; separate assignment requires loop.

9. Partial array initialization sets remaining elements to zero automatically.

10. The middle element of odd-dimension diagonal matrices is counted in both principal and secondary diagonal sums.

## Common Mistakes to Avoid

1. **Index Out of Bounds:** Never access array elements outside valid index range [0, n-1].

2. **Array Size Modification:** You cannot resize an array after declaration; use dynamic memory (malloc) for variable sizes.

3. **Forgetting Array Size:** Always track array size separately when passing to functions.

4. **Uninitialized Arrays:** Declared arrays contain garbage values unless initialized.

5. **Matrix Dimension Mismatch:** Always verify dimensions before matrix operations like addition and multiplication.

## Revision Tips

1. Practice writing code for all basic operations: traversal, searching, sorting, insertion, deletion.

2. Draw memory layouts for both 1D and 2D arrays to understand storage representation.

3. Work through at least 3-4 complete programs covering both array types before exams.

4. Memorize time complexities of different algorithms as they're frequently asked in examinations.

5. Review pointer-arithmetic relationship with arrays as it's crucial for understanding array behavior in C.