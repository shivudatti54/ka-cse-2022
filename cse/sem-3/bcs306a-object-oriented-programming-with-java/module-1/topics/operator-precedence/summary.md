# Operator Precedence in Java - Summary

## Key Definitions and Concepts

- **Operator Precedence**: A set of rules determining the order in which operators are evaluated in expressions with multiple operators.
- **Associativity**: The direction (left-to-right or right-to-left) in which operators of the same precedence are evaluated.
- **Short-circuit Evaluation**: For `&&` and `||`, if the result can be determined from the first operand, the second operand is not evaluated.

## Important Formulas and Theorems

| Precedence Level | Operators (High to Low)                |
| ---------------- | -------------------------------------- | --- | --- |
| Highest          | `()` (parentheses)                     |
| Postfix          | `expr++`, `expr--`                     |
| Unary            | `++expr`, `--expr`, `+`, `-`, `!`, `~` |
| Multiplicative   | `*`, `/`, `%`                          |
| Additive         | `+`, `-`                               |
| Shift            | `<<`, `>>`, `>>>`                      |
| Relational       | `<`, `>`, `<=`, `>=`, `instanceof`     |
| Equality         | `==`, `!=`                             |
| Bitwise AND      | `&`                                    |
| Bitwise XOR      | `^`                                    |
| Bitwise OR       | `                                      | `   |
| Logical AND      | `&&`                                   |
| Logical OR       | `                                      |     | `   |
| Ternary          | `? :`                                  |
| Lowest           | Assignment operators                   |

## Key Points

- Multiplicative operators (`* / %`) are evaluated before additive operators (`+ -`)
- Logical NOT (`!`) has higher precedence than logical AND (`&&`), which has higher precedence than logical OR (`||`)
- Most operators are left-to-right associative; only unary, ternary, and assignment are right-to-left associative
- Parentheses always override default precedence
- Integer division truncates decimal results
- Pre-increment (`++a`) increments before use; post-increment (`a++`) uses before increment

## Common Mistakes to Avoid

- Assuming `a * b + c` means `(a * b) + c` without remembering precedence explicitly
- Forgetting that `&&` has higher precedence than `||` and writing unnecessary parentheses
- Confusing pre-increment and post-increment in complex expressions
- Not considering integer division when both operands are integers

## Revision Tips

1. Memorize the operator precedence table, focusing on the relative order of major operator groups.
2. Practice evaluating 5-10 complex expressions daily to build confidence.
3. Always use parentheses in critical expressions to ensure clarity and correctness.
4. Remember the mnemonic: "Ultrapackage Multiplicative Additive Shift Relational Equality Bitwise Logical Ternary Assignment" (U M A S R E B L T A) for top-to-bottom precedence.
