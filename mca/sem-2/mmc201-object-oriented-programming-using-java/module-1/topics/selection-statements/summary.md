# Selection Statements in Java - Summary

## Key Definitions and Concepts

- **Selection Statements**: Control structures that execute different code blocks based on boolean conditions
- **if Statement**: Executes code only when a specified condition is true
- **if-else Statement**: Provides alternative code paths for true and false conditions
- **else-if Ladder**: Chain of multiple conditions tested in sequence
- **switch Statement**: Multi-way branch construct comparing a variable against constant values
- **Fall-through**: Behavior where execution continues to subsequent cases after a match (when break is missing)
- **Ternary Operator**: Compact conditional operator (? :) returning one of two values

## Important Formulas and Theorems

- **Leap Year Logic**: `(year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)`
- **Switch Expression Syntax (Java 14+)**: `result = switch(val) { case v1 -> expr1; default -> expr2; }`
- **Ternary Syntax**: `result = condition ? valueIfTrue : valueIfFalse`

## Key Points

- Java conditions MUST evaluate to boolean (unlike C/C++); integer conditions cause compilation errors
- Curly braces are optional for single statements but recommended for clarity
- Switch supports: `char`, `byte`, `short`, `int`, `String`, and enum types
- Traditional switch requires `break` to prevent fall-through; arrow syntax eliminates this need
- Only ONE case block executes in switch—the first matching case
- Default case is optional and executes when no other case matches
- Multiple cases can be combined: `case 1, 2, 3 -> ...`
- Ternary operator is right-associative: `a ? b : c ? d : e` is `a ? b : (c ? d : e)`
- Conditions in else-if are evaluated top-to-bottom; first true condition executes

## Common Mistakes to Avoid

- **Forgetting break statements** in traditional switch leads to unintended fall-through
- **Using non-boolean conditions** (e.g., `if (x)` where x is int) causes compilation errors
- **Using variables in case labels** that aren't compile-time constants
- **Comparing Strings with ==** instead of `.equals()` method
- **Missing default case** when handling all possible input values is important

## Revision Tips

1. Practice writing all three forms of if statements (simple, if-else, else-if ladder)
2. Memorize the switch syntax differences between traditional and arrow syntax
3. Remember that switch is more efficient than else-if for single-variable multi-way decisions
4. Always use braces even for single statements to avoid "goto fail" style bugs
5. For university exam questions, first identify whether the problem requires binary (if-else) or multi-way (switch/else-if) decisions
