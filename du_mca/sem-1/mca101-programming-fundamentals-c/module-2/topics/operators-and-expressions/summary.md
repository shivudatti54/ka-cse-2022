# Operators and Expressions in C - Summary

## Key Definitions and Concepts

- **Operator:** A symbol that tells the compiler to perform specific mathematical or logical operations
- **Operand:** The value or variable on which an operator acts
- **Expression:** A combination of operators and operands that evaluates to a value
- **Precedence:** The hierarchy determining which operators are evaluated first in expressions
- **Associativity:** The order in which operators of the same precedence are evaluated
- **Type Conversion:** Automatic or explicit conversion of one data type to another

## Important Formulas and Theorems

- **Integer Division:** `a / b` truncates fractional part when both operands are integers
- **Modulus:** `a % b` returns remainder; works only with integers
- **Left Shift:** `x << n` is equivalent to multiplying by 2^n
- **Right Shift:** `x >> n` is equivalent to dividing by 2^n (for unsigned)
- **Two's Complement:** For an n-bit number, ~x = -(x+1)

## Key Points

- C provides 6 categories of operators: Arithmetic, Relational, Logical, Bitwise, Assignment, and Special (increment, conditional, sizeof, comma)
- Operator precedence: Postfix > Unary > Multiplicative > Additive > Shift > Relational > Equality > Bitwise AND > Bitwise XOR > Bitwise OR > Logical AND > Logical OR > Conditional > Assignment > Comma
- Most operators are left-associative; assignment and conditional are right-associative
- ++a (pre-increment) changes value before use; a++ (post-increment) changes value after use
- Logical && and || use short-circuit evaluation
- Bitwise operators work on individual bits of integer operands
- Implicit type conversion promotes smaller types to larger types in expressions
- The conditional operator (?:) is the only ternary operator in C

## Common Mistakes to Avoid

- Confusing assignment (=) with equality (==) in comparisons
- Assuming integer division produces decimal results
- Forgetting that % modulus operator only works with integers
- Not accounting for side effects in expressions with multiple increments
- Mixing up bitwise operators (&, |, ^) with logical operators (&&, ||)
- Writing expressions with undefined behavior like `arr[i++] = i`

## Revision Tips

1. Create a precedence table and memorize the order; use mnemonics if helpful
2. Practice 20+ output prediction questions focusing on increment operators and precedence
3. Write small programs to verify bitwise operation results
4. Always use parentheses to clarify intent rather than relying on precedence rules
5. Review previous DU question papers to understand the exam pattern and frequently tested concepts