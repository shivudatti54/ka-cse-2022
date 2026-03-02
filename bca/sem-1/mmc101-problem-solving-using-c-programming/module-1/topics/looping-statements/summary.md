# Looping Statements in C - Summary

## Key Definitions and Concepts

- **Loop:** A control structure that repeats a set of statements until a specified condition is met.
- **Entry-controlled loop:** Condition is checked before loop body executes (while, for loops).
- **Exit-controlled loop:** Condition is checked after loop body executes, guaranteeing at least one execution (do-while loop).
- **Iteration:** One complete execution of the loop body.
- **Loop control statements:** Keywords that modify loop execution (break, continue, goto).

## Important Formulas and Theorems

- **Total iterations in nested loops:** If outer loop runs m times and inner loop runs n times, total iterations = m × n.
- **Sum of first n natural numbers:** n(n+1)/2 (can be verified using loops).
- **Factorial n:** n! = n × (n-1) × ... × 1 (computed using loops).

## Key Points

- **While loop:** `while(condition)` - executes 0 or more times based on condition.
- **Do-while loop:** `do { } while(condition);` - executes 1 or more times; note the mandatory semicolon.
- **For loop:** `for(init; condition; update)` - most compact; all three parts are optional.
- **Break statement:** Immediately exits the innermost loop.
- **Continue statement:** Skips current iteration and proceeds to next iteration.
- **Goto statement:** Transfers control to a labeled statement (avoid in modern programming).
- **Infinite loop:** Occurs when condition never becomes false; can be intentional or due to errors.

## Common Mistakes to Avoid

1. **Semicolon after loop header:** Writing `while(i <= n);` creates an empty loop body, causing infinite execution.
2. **Forgetting update statement:** Leads to infinite loops as the loop variable never changes.
3. **Using wrong loop type:** Using while when do-while is needed (or vice versa) can cause logical errors.
4. **Off-by-one errors:** Incorrect loop boundaries (e.g., using i <= n instead of i < n) cause incorrect iterations.
5. **Missing braces for single statement:** While technically allowed, omitting braces makes code prone to errors.

## Revision Tips

1. Practice writing all three loop types for the same problem to understand when each is most appropriate.
2. Trace through nested loop examples manually, writing down values of loop variables at each iteration.
3. Memorize the syntax differences, especially the semicolon in do-while loops.
4. Solve previous year DU exam questions on loops to understand the question patterns and common pitfalls.
5. When debugging, check three things: initialization, termination condition, and update statement.