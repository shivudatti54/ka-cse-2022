# Arrays: Operations and Applications - Summary

## Key Definitions and Concepts

- **Array**: A linear data structure storing homogeneous elements in contiguous memory locations, accessible via indices
- **Element**: Individual data item stored in an array position
- **Index**: Non-negative integer used to access array elements (starts from 0 in most languages)
- **Contiguous Memory**: Adjacent memory locations used for storing array elements
- **Multi-dimensional Array**: Array with multiple dimensions (2D, 3D) representing matrices or higher-dimensional data

## Important Formulas and Theorems

- **Address Calculation**: `Address(arr[i]) = base + (i × size_of_element)`
- **2D Array Address (Row-major)**: `Address(arr[i][j]) = base + (i × n + j) × size_of_element`
- **Linear Search**: O(n) time complexity
- **Binary Search**: O(log n) time complexity (requires sorted array)
- **Insertion/Deletion**: O(n) worst case, O(1) best case
- **Sorting algorithms**: O(n²) for bubble sort and selection sort

## Key Points

- Arrays provide O(1) random access time due to contiguous memory allocation
- Binary search is significantly faster than linear search for large sorted datasets (log n vs n)
- Insertion at the beginning requires shifting all elements (O(n)), while insertion at end is O(1) if space available
- Deletion is inverse of insertion - shifting elements left to fill gaps
- Bubble sort repeatedly swaps adjacent elements; selection sort finds minimum each pass
- 2D arrays can be stored in row-major (C, Python) or column-major (Fortran) order
- Arrays have fixed size in static implementations; dynamic arrays (like ArrayList in Java) overcome this limitation

## Common Mistakes to Avoid

- Confusing 0-based indexing with 1-based indexing - most languages use 0-based
- Applying binary search on unsorted arrays - always ensure array is sorted first
- Not checking for array overflow before insertion operations
- Forgetting that array indices start from 0, not 1
- Assuming O(1) for all operations - insertion/deletion can be O(n) depending on position

## Revision Tips

1. Practice writing code for all basic operations - traversal, insertion, deletion, searching, sorting
2. Memorize time complexities of all operations - this is frequently tested in exams
3. Draw memory diagrams for array operations to visualize how elements shift
4. Solve at least 5-10 array problems covering different operations
5. Remember the address calculation formula and practice problems involving memory addressing