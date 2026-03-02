# Automatic Type Promotion in Expressions - Summary

## Key Definitions and Concepts

- **Type Promotion (Widening)**: Automatic conversion of a smaller data type to a larger data type by the Java compiler during expression evaluation.
- **Widening Conversion**: Safe conversion where no data loss occurs (e.g., int to long).
- **Implicit Conversion**: Automatic type conversion performed by the compiler without programmer intervention.

## Important Formulas and Promotion Rules

The promotion hierarchy (from smallest to largest):

```
byte → short → int → long → float → double
```

**Rule Priority:**

1. If any operand is `double` → result is `double`
2. Else if any operand is `float` → result is `float`
3. Else if any operand is `long` → result is `long`
4. Else → both operands become `int`

## Key Points

- All `byte` and `short` operands are automatically promoted to `int` in arithmetic expressions.
- Integer literals (like 100) can be assigned to `byte`/`short` if within range, without casting.
- Character type (`char`) is promoted to `int` in expressions.
- The result type depends on operands, not the variable being assigned to.
- Integer division (/) truncates decimal; real division requires at least one `double` or `float` operand.
- Compound expressions evaluate step-by-step with promotion at each operation.

## Common Mistakes to Avoid

1. Assuming `byte + byte = byte` - it actually equals `int`
2. Forgetting that `char + char = int`, not `char`
3. Confusing assignment context with expression context
4. Not realizing integer division happens before type promotion in assignments like `double d = a / b`

## Revision Tips

1. Remember: "All integer arithmetic results in at least int"
2. When in doubt, trace through operations step by step
3. Look at the largest operand type to predict the result type
4. Practice identifying promotion in mixed-type expressions
5. Remember that double literal (2.0) promotes differently than integer literal (2)
