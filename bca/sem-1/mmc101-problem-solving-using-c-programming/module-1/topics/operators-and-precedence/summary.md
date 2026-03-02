# Operators and Precedence in C - Summary

## Key Definitions and Concepts

- **OPERATOR**: A symbol that tells the compiler to perform specific mathematical or logical operations.
- **OPERAND**: The value or variable on which an operator performs its operation.
- **EXPRESSION**: A combination of operators and operands that evaluates to a single value.
- **PRECEDENCE**: Rules determining which operator is evaluated first when multiple operators appear in an expression.
- **ASSOCIATIVITY**: The direction (left-to-right or right-to-left) in which operators of the same precedence are evaluated.
- **SHORT-CIRCUIT EVALUATION**: Optimization where the second operand is not evaluated if the result is already determined by the first operand.

## Important Formulas and Theorems

- Precedence hierarchy (highest to lowest): postfix → unary → multiplicative (* / %) → additive (+ -) → shift → relational → equality → bitwise AND → bitwise XOR → bitwise OR → logical AND → logical OR → ternary → assignment → comma.
- Associativity: Most operators associate LEFT-TO-RIGHT; assignment and ternary operators associate RIGHT-TO-LEFT.
- Usual arithmetic conversions: Smaller types are converted to larger types before operations (int → float, etc.).

## Key Points

- INCREMENT (++) adds 1, DECREMENT (--) subtracts 1 from a variable.
- PREFIX operators (++i) modify value before use; POSTFIX operators (i++) use value before modification.
- LOGICAL AND (&&) returns true only if BOTH operands are true; LOGICAL OR (||) returns true if AT LEAST ONE is true.
- ASSIGNMENT operators (+=, -=, *=, /=) combine operation with assignment in one step.
- BITWISE operators work at the individual bit level: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift).
- INTEGER DIVISION (/) truncates decimal portion; use casting for floating-point results.
- MODULUS (%) returns remainder and works only with integers.
- Parentheses override default precedence and improve code readability.

## Common Mistakes to Avoid

1. CONFUSING assignment (=) with equality (==) in conditions - this is a frequent source of bugs.
2. Using % with floating-point operands - causes compile error.
3. Assuming left-to-right evaluation for all operators - assignment and ternary evaluate right-to-left.
4. Forgetting that integer division truncates - 7/3 yields 2, not 2.333.
5. Misunderstanding prefix vs postfix behavior in complex expressions.

## Revision Tips

1. CREATE A PRECEDENCE TABLE and memorize the hierarchy from highest to lowest.
2. PRACTICE BY HAND - evaluate expressions on paper following precedence rules step by step.
3. USE PARENTHESES liberally in your code to make intended order explicit.
4. RUN CODE EXPERIMENTS - test increment/decrement in printf to see actual behavior.
5. FOCUS ON OPERATOR INTERACTION - questions often combine different operator types in single expressions.