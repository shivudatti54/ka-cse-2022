# Stacks, Queues, and Deques - Summary

## Key Definitions and Concepts

- **Stack**: A linear data structure following LIFO (Last-In-First-Out) principle with operations push, pop, and peek.
- **Queue**: A linear data structure following FIFO (First-In-First-Out) principle with operations enqueue, dequeue, front, and rear.
- **Deque**: A double-ended queue allowing insertion and deletion from both front and rear ends.
- **Overflow**: Condition when attempting to insert into a full data structure.
- **Underflow**: Condition when attempting to remove from an empty data structure.
- **Circular Queue**: An efficient queue implementation that wraps around the array, utilizing space optimally.

## Important Formulas and Theorems

- **Stack Array Implementation**: top initialized to -1, incremented after push
- **Circular Queue Full Condition**: `(rear + 1) % capacity == front`
- **Circular Queue Empty Condition**: `rear == front`
- **Circular Index Update**: `index = (index + 1) % capacity`
- **Amortized Analysis for Queue using Two Stacks**: O(1) for both enqueue and dequeue

## Key Points

1. All basic operations on stacks, queues, and deques have O(1) time complexity.
2. Stack is used in expression evaluation, recursion, and backtracking algorithms.
3. Queue is essential for BFS, level-order traversal, and scheduling problems.
4. Deque efficiently supports operations at both ends, useful in sliding window problems.
5. Circular queue prevents space wastage by wrapping around the array.
6. Stack overflow occurs with deep recursion; queue overflow occurs with sustained high load.
7. Linked list implementation provides dynamic size; array implementation has fixed capacity.
8. Deque can simulate both stack and queue functionalities.

## Common Mistakes to Avoid

1. Confusing front and rear pointer movements in queue operations.
2. Forgetting to check for overflow/underflow conditions before operations.
3. Not handling the wrap-around correctly in circular queue implementation.
4. Using stack where queue is required (or vice versa) in algorithm implementation.
5. Initializing front and rear pointers incorrectly (common in array-based implementations).

## Revision Tips

1. Practice implementing all three data structures from scratch in C/C++ or Python.
2. Solve at least 5 problems each on stacks and queues from previous year question papers.
3. Memorize the circular queue formulas - they are frequently tested in exams.
4. Understand the relationship between recursion and stack data structure.
5. Review the application areas of each data structure to identify which to use in problem-solving.
6. Practice converting between infix, postfix, and prefix expressions using stack.