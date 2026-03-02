# Stacks and Implementations - Summary

## Key Definitions and Concepts

- **Stack**: An abstract data type that follows the Last In, First Out (LIFO) principle, where elements are added and removed from only one end called the "top".

- **Push**: Operation to add an element to the top of the stack. May cause stack overflow if stack is full.

- **Pop**: Operation to remove and return the element from the top of the stack. May cause stack underflow if stack is empty.

- **Peek/Top**: Operation to view the top element without removing it from the stack.

- **Stack Overflow**: Error condition when trying to push into a full stack (in array implementation).

- **Stack Underflow**: Error condition when trying to pop from an empty stack.

## Important Formulas and Theorems

| Operation | Array Implementation | Linked List Implementation |
|-----------|---------------------|---------------------------|
| Push      | O(1)                | O(1)                      |
| Pop       | O(1)                | O(1)                      |
| Peek      | O(1)                | O(1)                      |
| isEmpty   | O(1)                | O(1)                      |

- **Space Complexity**: O(n) for both implementations where n is the number of elements
- Array: Contiguous memory allocation with fixed size
- Linked List: Dynamic memory with node overhead (data + pointer)

## Key Points

1. A stack is a LIFO (Last In, First Out) data structure — elements are added and removed from the same end (top).

2. The two primary implementations are: **Array-based** (static, fixed size) and **Linked List-based** (dynamic, grows as needed).

3. Array implementation uses a fixed-size array with a `top` index initialized to -1 for empty stack.

4. Linked list implementation uses the head node as the top; push adds at head, pop removes from head.

5. All primary stack operations (push, pop, peek, isEmpty) have O(1) time complexity in both implementations.

6. Stack overflow occurs when pushing into a full stack; stack underflow occurs when popping from an empty stack.

7. Key applications include function call management, expression evaluation, undo mechanisms, parenthesis matching, and DFS algorithms.

8. Array implementation is simpler but wastes memory if stack remains mostly empty; linked list uses extra memory for pointers.

## Common Mistakes to Avoid

1. **Forgetting to check for empty/full conditions**: Always verify stack status before push/pop operations to prevent overflow/underflow errors.

2. **Incorrect top initialization**: In array implementation, initialize `top = -1` (not 0) to correctly represent an empty stack.

3. **Memory leaks in linked list implementation**: Always free the node memory when popping in linked list implementation.

4. **Confusing peek and pop**: Remember that peek returns the top element without removing it, while pop removes it.

5. **Not handling all bracket types**: When checking balanced parentheses, ensure matching pairs for '(', '[', and '{'.

## Revision Tips

1. **Practice writing code**: Implement both array and linked list stack versions from memory multiple times.

2. **Draw stack states**: Visualize how the stack looks after each push and pop operation to build intuition.

3. **Memorize complexities**: Remember that all basic operations are O(1) — this is a key advantage of stacks.

4. **Solve problems**: Practice parenthesis matching and expression evaluation problems that use stacks.

5. **Understand real-world connections**: Relate stack concepts to familiar applications like browser back button or text editor undo feature.