# Using Dynamic Arrays - Summary

## Key Definitions and Concepts

- **Dynamic Array**: A resizable array data structure that grows and shrinks during runtime, allocating memory as needed rather than at compile time
- **Capacity**: The maximum number of elements that can be stored in the allocated memory before resizing is required
- **Size**: The current number of elements actually stored in the array
- **Growth Factor**: The multiplier used when increasing array capacity (typically 2)
- **Amortized Analysis**: A technique for analyzing time complexity where expensive operations are averaged over all operations
- **Realloc**: C function that attempts to resize a previously allocated memory block

## Important Formulas and Theorems

- **Amortized Insert Cost**: O(1) for dynamic array with doubling strategy
- **Total Resize Cost**: 1 + 2 + 4 + 8 + ... + n ≈ 2n - 1 = O(n)
- **Array Element Address**: address = base_address + (index × element_size)
- **Resize Condition**: When size == capacity, resize to capacity × growth_factor
- **Shrink Condition**: When size < capacity/4, resize to capacity/2

## Key Points

- Dynamic arrays solve the fixed-size limitation of static arrays by allocating memory at runtime
- The doubling strategy ensures O(1) amortized time for append operations
- Random access in arrays is O(1) due to contiguous memory and direct address calculation
- Memory must be explicitly managed with malloc/calloc for allocation and free for deallocation
- The trade-off between dynamic arrays and linked lists involves access time versus insertion/deletion flexibility
- A growth factor of 2 balances memory usage and resize frequency
- Shrinking should use a lower threshold than growing to prevent thrashing

## Common Mistakes to Avoid

- Confusing size with capacity - they represent different values
- Forgetting to free dynamically allocated memory, causing memory leaks
- Not checking for NULL after malloc/realloc calls
- Using realloc incorrectly - never assign directly without a temporary pointer
- Assuming array indices start at 1 - they always start at 0 in C

## Revision Tips

1. Practice implementing dynamic array from scratch - this reinforces understanding of memory management
2. Work through the amortized cost proof by summing the geometric series
3. Compare implementations with standard library equivalents (vector in C++, ArrayList in Java)
4. Draw memory diagrams showing array before and after resizing
5. Memorize the time complexities: access O(1), search O(n), insert O(1) amortized, delete O(1)