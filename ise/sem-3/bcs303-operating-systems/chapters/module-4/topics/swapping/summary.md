# **Swapping**

### Definitions and Formulas

- **Swapping**: A operation that exchanges two elements in an array or list.
- **Swapping Algorithm**: A technique used to swap two elements without using a temporary variable.

### Important Formulas and Theorems

- **Index Swapping Formula**: `temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;`
- **Explanation of Swapping Algorithm**: This algorithm works by using the elements themselves to swap values, eliminating the need for an extra variable.

### Key Points

- **Time Complexity**: O(1) for swapping two elements
- **Space Complexity**: O(1) as no extra space is required
- **Swap Operators**: `std::swap()` function in C++ and Python's tuple unpacking
- **Advantages**:
  - Efficient in terms of time and space complexity
  - Does not require additional memory
- **Disadvantages**:
  - May cause unexpected behavior if not used carefully
  - May not be suitable for large datasets

### Important Theorems

- **Theorem of Swapping**: If `arr[i]` and `arr[j]` are the two elements to be swapped, then `arr[i]` will be replaced by `arr[j]` and `arr[j]` will be replaced by `arr[i]`.
- **Theorem of Swap Stability**: Swapping two elements in an array does not affect the relative order of the other elements.
