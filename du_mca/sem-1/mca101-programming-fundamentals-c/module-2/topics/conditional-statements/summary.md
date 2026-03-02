# Conditional Statements in C - Summary

## Key Definitions and Concepts

- **Conditional Statement**: A programming construct that executes different code blocks based on whether a specified condition evaluates to true (non-zero) or false (zero).
- **if Statement**: Evaluates a condition and executes code only when the condition is true.
- **if-else Statement**: Provides two mutually exclusive paths — one executes when the condition is true, the other when false.
- **Nested Conditionals**: Conditional statements placed inside other conditional statements for handling dependent conditions.
- **switch Statement**: Multi-way branch statement that compares a single expression against constant case labels.
- **Ternary Operator**: The `?:` operator providing inline conditional expression evaluation.
- **Short-circuit Evaluation**: Optimization where logical AND (`&&`) skips the second operand if the first is false, and logical OR (`||`) skips the second if the first is true.

## Important Formulas and Theorems

- **Leap Year Logic**: Year is leap if `(year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)`
- **Dangling Else Rule**: In C, an else clause associates with the nearest preceding if that has no else
- **Switch Expression Types**: Must evaluate to integer type (int, char, short, long, or enum)

## Key Points

- Always use == for comparison, not = (assignment) — a common examination error
- Switch cases require constant integral values; use if-else for variable conditions
- The default case in switch handles unexpected values gracefully
- Missing break statements cause fall-through behavior in switch constructs
- Logical operators && and || perform short-circuit evaluation
- Order conditions from most specific to most general for correct if-else chain execution
- Ternary operator provides compact syntax but reduces readability when nested

## Common Mistakes to Avoid

1. Using assignment operator (=) instead of comparison operator (==) in conditions
2. Forgetting to use braces around multi-statement if bodies, causing "implicit else" bugs
3. Omitting break statements in switch cases, leading to unintended fall-through
4. Placing conditions in wrong order, causing general conditions to match before specific ones
5. Using variables (instead of constants) as switch case labels

## Revision Tips

1. Practice writing if-else chains for boundary conditions — test edge cases like >= vs >
2. Draw flowcharts for nested conditionals to visualize execution paths before coding
3. Memorize the leap year logic and grade classification examples as they frequently appear in exams
4. Always include default case in switch statements — this demonstrates thorough understanding
5. When debugging, explicitly add braces even for single statements to prevent subtle bugs