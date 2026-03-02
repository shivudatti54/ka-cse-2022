# Decision Making Statements in C - Summary

## Key Definitions and Concepts

- Decision making statements are control structures that allow conditional execution of code blocks based on evaluated conditions.

- The `if` statement evaluates a condition and executes code only if the condition is true (non-zero).

- The `if-else` statement provides alternative code execution paths for both true and false conditions.

- Nested if-else involves placing if-else constructs inside other if or else blocks for multi-level decisions.

- The else-if ladder chains multiple conditions checked sequentially, with the first true condition determining the execution path.

## Important Formulas and Theorems

- Basic if syntax: `if (condition) { statements; }`

- If-else syntax: `if (condition) { statements; } else { statements; }`

- Else-if ladder pattern: `if (cond1) {...} else if (cond2) {...} else {...}`

- Common operators in conditions: relational (`<`, `>`, `<=`, `>=`, `==`, `!=`) and logical (`&&`, `||`, `!`)

- In C, any non-zero value evaluates to true; zero evaluates to false.

## Key Points

- Conditions in decision statements must be scalar expressions evaluating to numeric values.

- Use `==` for comparison, not `=` (assignment), to avoid unintended behavior.

- Each `else` associates with the nearest unmatched `if` in the same block.

- The else-if ladder stops execution at the first true condition; order matters.

- Curly braces are required when combining multiple statements in if or else blocks.

- The final else clause is optional but recommended for handling unexpected cases.

- Nested if-else can become hard to read; maintain proper indentation and consider alternatives for deep nesting.

## Common Mistakes to Avoid

- Confusing assignment (`=`) with equality comparison (`==`) in conditions.

- Forgetting curly braces when using multiple statements in if/else blocks, causing logic errors.

- Incorrectly associating else clauses due to improper nesting or missing braces.

- Assuming conditions are evaluated in a particular order without verification.

- Not handling all possible cases, especially boundary conditions and edge cases.

## Revision Tips

- Practice writing all three types of decision structures (if, if-else, else-if ladder) with proper syntax.

- Trace through example programs with multiple test cases covering different scenarios.

- Remember that C treats any non-zero value as true, including negative numbers.

- Review the operator precedence chart to understand how complex conditions are evaluated.

- Solve previous year DU examination questions on decision making statements to understand the exam pattern and difficulty level.