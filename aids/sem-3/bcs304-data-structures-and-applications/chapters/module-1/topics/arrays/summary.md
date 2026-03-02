# Arrays - Summary

## Key Definitions and Concepts

- ARRAY: A homogeneous collection of elements stored in contiguous memory locations, accessible through indices.
- STATIC ARRAYS: Arrays with fixed size determined at compile time.
- DYNAMIC ARRAYS: Arrays with memory allocated at runtime using functions like malloc() and calloc().
- ROW-MAJOR ORDER: Storage of 2D array elements row by row consecutively.
- COLUMN-MAJOR ORDER: Storage of 2D array elements column by column consecutively.

## Important Formulas and Theorems

- One-dimensional array address: Address of arr[i] = Base Address + (i × size of element)
- Two-dimensional array address (row-major): Address of A[i][j] = Base Address + ((i × n) + j) × size
- Two-dimensional array address (column-major): Address of A[i][j] = Base Address + ((j × m) + i) × size
- Where m = number of rows, n = number of columns

## Key Points

- Array indices start from 0 in most programming languages including C, C++, and Java.
- Array provides O(1) constant time access to any element through its index.
- Search in unsorted array takes O(n) time complexity.
- malloc() does not initialize memory while calloc() initializes to zero.
- Always check for NULL after dynamic memory allocation.
- Array name acts as a constant pointer to the first element.
- In 2D arrays, row-major stores elements row by row, column-major stores column by column.
- Arrays of structures are used for storing multiple records of different data types.

## Common Mistakes to Avoid

- CONFUSING ARRAY INDEX: Remember array indices start at 0, not 1. The last element is at index n-1 for an array of size n.
- FORGETTING TO FREE MEMORY: Always use free() after dynamic allocation to prevent memory leaks.
- NOT CHECKING FOR NULL: Failing to check if malloc/calloc returned NULL can lead to segmentation faults.
- USING WRONG STORAGE ORDER: Using row-major formula for column-major storage (or vice versa) produces incorrect addresses.

## Revision Tips

- PRACTICE ADDRESS CALCULATION PROBLEMS daily until you can solve them quickly and accurately.
- MEMORIZE THE DIFFERENCE between malloc and calloc, as this is frequently tested in multiple-choice questions.
- UNDERSTAND POINTER-ARRAY RELATIONSHIP thoroughly as it forms the basis for dynamic memory management.
- SOLVE PREVIOUS YEAR QUESTION PAPERS to understand the exam pattern and frequently asked concepts.