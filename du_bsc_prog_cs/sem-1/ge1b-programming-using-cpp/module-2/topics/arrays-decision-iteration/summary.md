# Arrays, Decision Making, and Iteration in C++ - Summary

## Key Definitions and Concepts

- **Array:** A contiguous memory structure storing multiple elements of the same data type under a single variable name
- **Zero-indexed:** Array indices start at 0, not 1; valid range is 0 to (n-1) for array of size n
- **Decision Making:** Conditional execution of code based on boolean expressions (true/false)
- **Iteration:** Repetitive execution of code blocks using loop constructs
- **Loop Control Statements:** break (exits loop), continue (skips current iteration)

## Important Formulas and Theorems

- **Array element access:** `arr[index]` - O(1) time complexity
- **Linear search:** O(n) time complexity - checks each element sequentially
- **2D Array memory:** Row-major order - elements stored row by row
- **Loop bounds:** Use `<` for 0 to n-1, `<=` for 1 to n

## Key Points

- Arrays provide efficient random access but require contiguous memory
- Always validate array indices to prevent buffer overflow
- Use if-else when conditions are not mutually exclusive or involve ranges
- Prefer switch over long if-else chains for discrete value comparisons
- while loop is pre-test (may not execute); do-while is post-test (executes at least once)
- Nested loops are essential for multi-dimensional data and pattern problems
- Input validation is crucial for robust programs

## Common Mistakes to Avoid

- Using index n (out of bounds) instead of n-1
- Confusing assignment operator (=) with comparison operator (==)
- Forgetting break statements in switch, causing fall-through
- Creating infinite loops by not updating loop variables
- Using uninitialized loop variables

## Revision Tips

- Practice tracing code with sample inputs to understand execution flow
- Memorize the syntax patterns for each construct
- Solve at least 5-10 problems each for arrays, decision statements, and loops
- Draw flowcharts for complex nested logic before coding
- Review previous year DU examination questions for pattern familiarity