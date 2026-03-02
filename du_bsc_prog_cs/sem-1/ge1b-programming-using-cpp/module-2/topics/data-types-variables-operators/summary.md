# Data Types, Variables, and Operators in C++ - Summary

## Key Definitions and Concepts

- **Data Type**: A classification specifying the type of value a variable can hold and the operations that can be performed on it.
- **Variable**: A named memory location that stores a value which can be modified during program execution.
- **Operator**: A symbol that performs specific mathematical or logical operations on operands.
- **Scope**: The region of code where a variable is accessible and can be referenced.
- **Storage Duration**: The period during which a variable exists in memory (automatic, static, or dynamic).

## Important Formulas and Theorems

| Data Type | Typical Size | Typical Range |
|-----------|--------------|---------------|
| int | 4 bytes | -2,147,483,648 to 2,147,483,647 |
| float | 4 bytes | ±3.4e±38 (6-7 significant digits) |
| double | 8 bytes | ±1.7e±308 (15-16 significant digits) |
| char | 1 byte | -128 to 127 or 0 to 255 |
| bool | 1 byte | true (1) or false (0) |

**Key Operators:**
- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Relational: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `&&`, `||`, `!`
- Bitwise: `&`, `|`, `^`, `~`, `<<`, `>>`
- Assignment: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- Increment/Decrement: `++`, `--`

## Key Points

- C++ is a strongly-typed language requiring explicit data type declaration for all variables.
- Use brace initialization `{}` to prevent narrowing conversions and ensure type safety.
- Integer division truncates decimal part; use floating-point literals or casts for decimal results.
- Pre-increment (`++x`) modifies before use; post-increment (`x++`) uses before modifying.
- Bitwise operators work on individual bits and are essential for low-level programming.
- Constants should be declared with `const` or `constexpr`; avoid `#define` in modern C++.
- Operator precedence follows standard mathematical rules; use parentheses for clarity.
- Variables should always be initialized before use to avoid undefined behavior.

## Common Mistakes to Avoid

1. **Using integer division for floating-point results**: Remember `7/2 = 3`, not `3.5`.
2. **Confusing `=` with `==`**: Assignment sets value, equality checks value.
3. **Not initializing variables**: Leads to garbage values and unpredictable behavior.
4. **Mixing signed and unsigned**: Can produce unexpected results due to range differences.
5. **Ignoring operator precedence**: Always use parentheses when uncertain.

## Revision Tips

1. Practice declaring variables of different types and printing their sizes using `sizeof()`.
2. Write programs demonstrating all operator types to reinforce understanding.
3. Remember the operator precedence table — this is frequently tested in exams.
4. Review type casting examples to understand implicit vs explicit conversions.
5. Solve previous year questions on data types and operators for exam pattern familiarity.