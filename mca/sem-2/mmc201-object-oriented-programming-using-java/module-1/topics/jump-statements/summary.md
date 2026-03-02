# Jump Statements in Java - Summary

## Key Definitions and Concepts

- **Jump statements** are control transfer statements that alter the normal sequential execution flow in Java
- **Break statement** terminates a loop or switch block immediately
- **Continue statement** skips the current iteration and proceeds to the next iteration
- **Return statement** exits a method and optionally returns a value
- **Labels** are identifiers followed by colon (:) used with break/continue to control outer loops

## Important Formulas and Techniques

- Break syntax: `break;` or `break labelName;`
- Continue syntax: `continue;` or `continue labelName;`
- Return syntax: `return;` or `return expression;`
- Label syntax: `labelName: for(...)`

## Key Points

1. Break terminates the innermost loop or switch when used without a label
2. Continue skips only the current iteration, not the entire loop
3. Labeled break/continue is essential for controlling multiple nested loops
4. Return statement completely exits the method, unlike break which only exits the loop
5. In switch statements, break prevents fall-through to subsequent cases
6. Unlabeled break/continue affects only the innermost enclosing loop
7. Using labels with break/continue improves code readability in nested structures

## Common Mistakes to Avoid

1. Forgetting break in switch cases leads to unintended fall-through
2. Placing continue incorrectly can cause infinite loops
3. Using break outside loops or switch causes compilation error
4. Confusing break (exit loop) with continue (skip iteration)

## Revision Tips

1. Practice writing nested loops with labeled break and continue
2. Trace through code examples to understand control flow
3. Remember that return always exits the method, not just the loop
4. Use flowcharts to visualize how jump statements change execution path
5. Solve previous university exam questions involving loops and jump statements
