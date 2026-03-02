# Using Dynamic Arrays - Summary

## Key Definitions and Concepts

- **Dynamic Array**: A resizable array data structure that maintains separate capacity and size variables, automatically resizing when capacity is exceeded
- **Amortized Analysis**: A method of analyzing time complexity where the total cost of a sequence of operations is distributed across all operations, providing average performance
- **LIFO (Last-In-First-Out)**: The ordering principle for stacks where the most recently added element is removed first
- **FIFO (First-In-First-Out)**: The ordering principle for queues where the earliest added element is removed first
- **Circular Queue**: A queue implementation using a circular array where indices wrap around, enabling O(1) dequeue without element shifting

## Important Formulas and Theorems

- **Amortized push cost**: O(1) for doubling strategy because total copies = n - 1 ≈ n for n insertions
- **Resizing condition**: Trigger resize when size equals capacity (for expansion) or when size drops to capacity/4 (for shrinkage)
- **Circular queue indices**: New rear = (rear + 1) % capacity, new front = (front + 1) % capacity

## Key Points

- Dynamic arrays separate logical size from physical capacity, allowing runtime flexibility
- Stack implementation using dynamic arrays maintains a single pointer (top index) plus size and capacity variables
- Queue implementation requires front and rear indices, with circular buffering preventing front index drift
- Doubling capacity provides O(1) amortized time for push/enqueue operations despite occasional O(n) resize costs
- Array-based implementations offer better cache locality compared to linked lists
- Memory must be explicitly deallocated in languages like C/C++ to prevent leaks
- Circular queues wrap index values using modulo arithmetic when reaching array boundaries

## Common Mistakes to Avoid

- Confusing size with capacity—this is a frequent exam error as these represent different quantities
- Forgetting to update pointers/indices after resize operations, leading to incorrect state tracking
- Not handling underflow conditions (pop/dequeue on empty structures) in implementations
- Incorrect circular index calculation, especially when the front index is not at position 0

## Revision Tips

- Practice tracing operation sequences by hand, showing exact array states after each operation
- Memorize the mathematical proof for why doubling strategy yields O(1) amortized cost
- Draw memory diagrams for circular queues to visualize index wrapping behavior
- Review linked list implementations to compare trade-offs with array-based approaches