# Arrays and Structures - Summary

## Key Definitions and Concepts

- **Array:** A contiguous memory collection of elements of the same data type, accessed via indices starting from 0
- **Structure:** A user-defined data type that groups heterogeneous data items (different types) under a single name
- **Dynamic Array:** An array created at runtime using dynamic memory allocation functions
- **Structure Padding:** Compiler-inserted bytes for memory alignment, causing structure size to exceed sum of member sizes

## Important Formulas and Theorems

- **1D Array Address:** `Address(A[i]) = Base + (i × ElementSize)`
- **2D Array Address (Row-Major):** `Address(A[i][j]) = Base + ((i × n) + j) × ElementSize` where n = number of columns
- **Binary Search Time Complexity:** O(log n) - requires sorted array as prerequisite
- **Linear Search Time Complexity:** O(n)

## Key Points

- Arrays provide O(1) random access to elements while structures enable modeling real-world entities with multiple attributes
- Array indices in C start from 0 and must be within bounds to avoid undefined behavior
- Structures use contiguous memory for members but may include padding bytes for alignment
- Array of structures combines benefits of both - multiple records with different attribute types
- Dynamic memory allocation requires explicit deallocation using free() to prevent memory leaks
- Structures can be assigned entirely using = operator unlike arrays which cannot be directly assigned
- Variable Length Arrays (VLA) in C99 allow runtime-determined array sizes but have limitations

## Common Mistakes to Avoid

- Forgetting to use & operator when scanning array elements or structure members with scanf()
- Attempting to assign one array to another directly - only possible element-by-element or with memcpy()
- Not checking array bounds before accessing elements, causing buffer overflow
- Confusing dot operator (.) with arrow operator (->) - use dot for regular variables, arrow for pointers
- Assuming structure size equals sum of member sizes due to ignoring padding bytes

## Revision Tips

- Practice writing programs that combine arrays and structures, such as sorting an array of structures
- Memorize the address calculation formulas and practice with numerical examples
- Draw memory layouts for both arrays and structures to visualize data organization
- Understand when to use arrays (homogeneous data, random access) versus structures (heterogeneous data, record representation)
- Review previous year question papers to identify important patterns and frequently asked concepts