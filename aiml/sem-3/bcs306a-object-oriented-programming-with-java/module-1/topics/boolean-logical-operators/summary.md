# Boolean Logical Operators - Summary

## Key Definitions and Concepts

- **Boolean:** A primitive data type in Java that holds only `true` or `false` values
- **Logical Operators:** Operators that work with boolean values to create compound boolean expressions
- **Short-Circuit Evaluation:** Optimization where evaluation stops as soon as the result is determined

## Important Formulas and Theorems

| Operator | Name              | Description                                   |
| -------- | ----------------- | --------------------------------------------- |
| `!`      | NOT               | Inverts boolean value                         |
| `&`      | AND               | Returns true if both operands are true        |
| `\|`     | OR                | Returns true if at least one operand is true  |
| `^`      | XOR               | Returns true if exactly one operand is true   |
| `&&`     | Short-Circuit AND | Same as & but stops if first operand is false |
| `\|\|`   | Short-Circuit OR  | Same as \| but stops if first operand is true |

**Precedence Order:** `!` → `&/&&` → `^` → `|/||`

## Key Points

- Java provides six boolean logical operators: !, &, |, ^, &&, ||
- Short-circuit operators (&&, ||) are preferred in most cases for better performance
- The & operator always evaluates both operands; && skips the second if first is false
- The | operator always evaluates both operands; || skips the second if first is true
- XOR (^) returns true only when exactly one operand is true (not both)
- NOT (!) is a unary operator that inverts the boolean value
- Using && prevents NullPointerException when checking object properties

## Common Mistakes to Avoid

1. Confusing & with && and | with || without understanding short-circuit behavior
2. Forgetting that XOR returns false when both operands are true
3. Writing complex expressions without parentheses, leading to incorrect precedence
4. Using bitwise operators (&, |, ^) on integers when logical operators are needed

## Revision Tips

1. Practice writing truth tables for all operators until they become automatic
2. Remember the mnemonic: "AND means both, OR means either, XOR means one but not both"
3. Always use short-circuit operators (&&, ||) unless you specifically need both operands evaluated
4. Review previous year university exam questions on boolean operators for pattern recognition
5. Write small test programs to verify operator behavior and build muscle memory
