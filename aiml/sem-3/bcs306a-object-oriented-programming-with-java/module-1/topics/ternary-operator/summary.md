# Ternary Operator in Java - Summary

## Key Definitions and Concepts

- **Ternary Operator**: A conditional operator in Java that takes three operands (hence "ternary") - a condition and two expressions. It provides a concise way to make binary decisions.
- **Syntax**: `condition ? expression1 : expression2` where if condition is true, expression1 is evaluated; otherwise expression2 is evaluated.
- **Conditional Expression**: An expression that returns a value based on the evaluation of a boolean condition.

## Important Formulas and Syntax

```
variable = (condition) ? valueIfTrue : valueIfFalse
```

For nested ternary (right-to-left associativity):

```
a ? b : c ? d : e → a ? b : (c ? d : e)
```

## Key Points

- The ternary operator is the only Java operator that takes three operands
- It returns a value and can be used inline within expressions
- Both expressions must be type-compatible or promotion-compatible
- Right-to-left associativity is crucial for nested ternary operations
- It evaluates only one of the two expressions (short-circuit evaluation)
- Suitable for simple binary decisions, not complex control flow
- Can be nested but should be limited to 2-3 levels for readability

## Common Mistakes to Avoid

1. **Confusing the order**: Remember it's "condition ? true : false" not "true ? condition : false"
2. **Forgetting the colon**: Both the question mark and colon are mandatory
3. **Type mismatch**: Both expressions should return compatible types; primitive promotion may cause unexpected results
4. **Over-nesting**: Excessive nesting makes code unreadable and hard to debug

## Revision Tips

1. Practice writing simple ternary expressions first, then gradually move to nested ones
2. Remember that ternary operator is an expression, not a statement - it returns a value
3. When in doubt about nested ternary, add parentheses to make evaluation order explicit
4. Review previous year university exam questions on ternary operators for pattern understanding
5. Compare ternary with if-else: use ternary for simple value selection, use if-else for complex logic
