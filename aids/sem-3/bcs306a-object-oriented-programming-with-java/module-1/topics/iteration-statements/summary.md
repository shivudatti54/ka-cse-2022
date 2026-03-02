# Iteration Statements in Java - Summary

## Key Definitions and Concepts

- **Iteration Statement:** A programming construct that allows a block of code to be executed repeatedly based on a condition.
- **While Loop:** Pre-test loop that checks condition before executing the loop body.
- **Do-While Loop:** Post-test loop that guarantees at least one execution before checking the condition.
- **For Loop:** Compact iteration statement with initialization, condition, and increment/decrement in a single line.
- **Enhanced For Loop:** Simplified loop for traversing arrays and collections without index management.

## Important Formulas and Theorems

- **Loop Condition Syntax:**
- While: `while (condition) { }`
- Do-While: `do { } while (condition);`
- For: `for (init; condition; update) { }`
- Enhanced: `for (type var : collection) { }`

- **Nested Loop Iterations:** Total iterations = iterations of outer loop × iterations of inner loop

## Key Points

1. Java provides four iteration statements: while, do-while, for, and enhanced for-each.

2. While loop is a pre-test loop; do-while is a post-test loop guaranteeing at least one execution.

3. For loop is ideal when the number of iterations is known beforehand.

4. Enhanced for loop simplifies array/collection traversal but cannot modify elements or access indices.

5. Break statement terminates the entire loop; continue skips only the current iteration.

6. Nested loops are essential for pattern printing and multi-dimensional data processing.

7. Always ensure loop termination by properly updating control variables.

## Common Mistakes to Avoid

1. **Forgetting to update loop control variable** - Leads to infinite loops.

2. **Using wrong loop type** - Using while when do-while is needed or vice versa.

3. **Off-by-one errors** - Incorrect initialization or termination conditions in for loops.

4. **Missing braces** - Only the first statement after loop header is considered part of the loop.

5. **Using enhanced for loop when modification is needed** - Enhanced for loop cannot modify array elements.

## Revision Tips

1. Practice writing all four loop types for the same problem to understand when each is most appropriate.

2. Trace through nested loop examples step-by-step to understand execution flow.

3. Memorize the syntax differences between loop types and remember that do-while requires a semicolon after the condition.

4. Focus on break and continue statements as they are frequently tested in practical programming questions.
