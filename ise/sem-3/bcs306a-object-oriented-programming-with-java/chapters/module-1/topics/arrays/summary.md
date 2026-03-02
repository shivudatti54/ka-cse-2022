# Arrays in Java - Summary

## Key Definitions and Concepts

- **Array**: A homogeneous collection of elements of the same data type, stored in contiguous memory locations with O(1) random access capability
- **Reference Type**: Arrays in Java are objects stored in heap memory, even when containing primitive types
- **Zero-based Indexing**: Array elements are accessed starting from index 0, with valid indices ranging from 0 to (length-1)
- **Jagged Arrays**: Multi-dimensional arrays where each row can have different lengths

## Important Formulas and Theorems

- Array declaration: `elementType[] arrayName` or `elementType arrayName[]`
- Array initialization with size: `new elementType[size]`
- Array initialization with values: `{val1, val2, val3, ...}`
- Accessing element: `arrayName[index]`
- Array length: `arrayName.length` (property, not method)
- Bounds checking: valid indices = 0 to length-1

## Key Points

- Java arrays have FIXED SIZE determined at creation time and cannot be dynamically resized
- Primitive arrays store actual values; object arrays store references to objects
- Default initialization: 0 for numeric types, false for boolean, null for object references
- The enhanced for loop (for-each) cannot modify array elements when used with primitives
- Always use Arrays.equals() for content comparison, not the == operator
- Arrays.binarySearch() requires a sorted array
- ArrayIndexOutOfBoundsException occurs when accessing invalid indices
- Multi-dimensional arrays in Java are arrays of arrays

## Common Mistakes to Avoid

- Confusing array length with highest index (length=5 means indices 0-4)
- Using == to compare array contents instead of Arrays.equals()
- Attempting to resize arrays after creation
- Forgetting that array indices start at 0
- Not checking for null before accessing array references

## Revision Tips

1. Practice writing array declaration and initialization in both formats until they become automatic
2. Draw memory diagrams to visualize how arrays are stored in Java's heap memory
3. Memorize the key methods in java.util.Arrays class: toString(), sort(), binarySearch(), copyOf(), equals()
4. Solve at least 5-10 array-based coding problems covering searching, sorting, and manipulation
5. Remember: for exams, always use < arr.length in loop conditions, not <=