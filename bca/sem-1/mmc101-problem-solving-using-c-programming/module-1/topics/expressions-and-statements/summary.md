# Expressions and Statements in C Programming - Summary

## Key Definitions and Concepts

- **Expression:** A combination of operands and operators that evaluates to a single value. Examples include arithmetic expressions (a + b), relational expressions (x > y), and assignment expressions (x = 5).

- **Statement:** A complete executable instruction that ends with a semicolon. Types include expression statements, compound statements (blocks), selection statements, and iteration statements.

- **Sequence Points:** Points in program execution where all side effects from previous evaluations are complete. The comma operator, logical operators && and ||, and the conditional operator introduce sequence points.

- **Side Effects:** Modifications to variables or external state during expression evaluation, such as assignment or increment operations.

## Important Formulas and Theorems

- **Usual Arithmetic Conversion:** When binary operators combine operands of different types, smaller types are promoted to larger types to preserve precision (e.g., int + float → float + float).

- **Operator Precedence Hierarchy:** Parentheses > Postfix > Unary > Multiplicative > Additive > Relational > Equality > Bitwise > Logical > Conditional > Assignment > Comma

- **Heron's Formula:** Area = √(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2, demonstrating nested arithmetic expressions with function calls.

## Key Points

- Every expression produces a value, but not every value-producing construct is a statement.

- The equality operator (==) compares values, while the assignment operator (=) assigns values—a common source of bugs.

- Integer division (7/3 = 2) differs from floating-point division (7.0/3.0 = 2.333).

- Short-circuit evaluation in logical expressions (&& and ||) stops evaluation when the result is determined.

- Compound assignment operators (x += 5) are more efficient than simple assignment (x = x + 5).

- Type casting using (type) expression explicitly converts types, overriding implicit conversions.

- The ternary operator (condition ? expr1 : expr2) provides compact conditional evaluation.

- Modifying a variable multiple times without sequence points causes undefined behavior.

## Common Mistakes to Avoid

- Confusing assignment (=) with equality (==) in conditional statements, causing logical errors rather than compilation errors.

- Forgetting that integer division truncates decimal portions instead of rounding.

- Using uninitialized variables in expressions, leading to unpredictable results.

- Assuming left-to-right evaluation for all operators—only assignment and comma operators guarantee right-to-left evaluation.

- Neglecting to use parentheses when mixing different operator types, leading to incorrect results due to precedence rules.

## Revision Tips

- Practice writing and evaluating expressions with multiple operators to reinforce precedence rules.

- Create quick reference cards for operator precedence and associativity.

- Write programs that demonstrate type conversion and casting to understand implicit behavior.

- Review past DU examination questions on expressions and statements for pattern familiarization.

- Solve problems requiring both expressions and statements to understand their interplay in practical programming.