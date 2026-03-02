# Operators and Expressions in Python - Summary

## Key Definitions and Concepts

- **Expression**: A combination of values, variables, operators, and function calls that evaluates to a single value.
- **Operator**: A special symbol that performs operations on operands (values or variables).
- **Operand**: The value or variable on which an operator operates.
- **Short-Circuit Evaluation**: Optimization where logical operators stop evaluating once the result is determined.

## Important Formulas and Theorems

- **Floor Division**: `a // b` equals the quotient rounded down toward negative infinity
- **Modulus**: `a % b` always has the same sign as the divisor; `a = (a // b) * b + (a % b)`
- **Bitwise NOT**: `~n = -(n + 1)` (ones complement in Python uses two's complement representation)
- **Left Shift**: `n << k` equals `n * 2^k`
- **Right Shift**: `n >> k` equals `n // 2^k` (for positive integers)

## Key Points

- Python has 7 categories of operators: Arithmetic, Comparison, Logical, Assignment, Bitwise, Identity, and Membership.
- The `/` operator always returns a float; use `//` for integer floor division.
- Comparison, identity, and membership operators have lower precedence than arithmetic but higher than logical `not`.
- Logical operators use short-circuit evaluation: `and` returns first falsy value; `or` returns first truthy value.
- Bitwise operators work on individual bits and are useful for flags, permissions, and optimization.
- Use `is` for comparing with singletons (None, True, False); use `==` for value equality.
- Membership (`in`) checks keys in dictionaries, elements in sequences.
- Exponentiation (`**`) is right-associative: `2 ** 3 ** 2` equals `2 ** 9` = 512.

## Common Mistakes to Avoid

- Using `=` instead of `==` for comparison (causes assignment instead of comparison).
- Confusing `/` with `//` — division vs. floor division.
- Forgetting that `not` has higher precedence than `and` and `or`.
- Using mutable default arguments in functions (though not directly operators-related, common in expressions).
- Not accounting for float results when doing division in integer contexts.

## Revision Tips

- Practice writing expressions and predicting their output manually before running code.
- Create a precedence table and memorize the order (PEMDAS with bitwise and logical operators).
- Work through competitive programming problems involving bitwise operations.
- Remember the short-circuit behavior — it's frequently tested in exams.
- Use Python's `help()` or documentation to verify operator behavior when unsure.