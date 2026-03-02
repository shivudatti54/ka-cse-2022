# Switch Statement in C - Summary

## Key Definitions and Concepts

- SWITCH STATEMENT: A multi-way branching control structure that evaluates an expression and executes the matching case block.
- CASE LABEL: A constant value that precedes a block of statements within a switch, used for comparison with the switch expression.
- BREAK STATEMENT: A statement that terminates the switch block and transfers control outside the switch.
- DEFAULT CASE: An optional case that executes when no other case matches the switch expression.
- FALL-THROUGH: The behavior when execution continues from one case to the next due to missing break statements.

## Important Formulas and Theorems

The switch statement follows this general form:
```
switch (expression) {
    case constant1: statements; break;
    case constant2: statements; break;
    default: statements;
}
```

Key constraints:
- Expression must evaluate to integral type (int, char, enum, short, long)
- Case labels must be constant expressions (no variables)
- Case labels must be unique within the same switch

## Key Points

- Switch provides cleaner code than multiple if-else statements for discrete value comparisons.
- The default case is optional but recommended for error handling.
- Without break, cases execute sequentially (fall-through behavior).
- Multiple cases can share common code by stacking labels without break.
- Switch expressions cannot be floating-point types.
- The switch statement offers O(1) time complexity for case matching.
- Nested switch statements are allowed but should be used sparingly.

## Common Mistakes to Avoid

- FORGETTING BREAK STATEMENTS: Causes unintended fall-through, leading to incorrect program behavior.
- USING VARIABLES AS CASE LABELS: Case labels must be constant expressions; variables cause compilation errors.
- USING FLOATING-POINT EXPRESSIONS: Switch does not support float or double types.
- NON-UNIQUE CASE LABELS: Duplicate case values within the same switch cause compilation failure.
- MISSING DEFAULT CASE: Not handling unexpected input values leads to silent failures.

## Revision Tips

- PRACTICE WRITING SWITCH STATEMENTS: Solve at least 5-6 problems involving menu-driven programs.
- MEMORIZE THE SYNTAX: Write the switch syntax repeatedly until it becomes natural.
- TRACE EXECUTION: Manually trace programs with and without break statements to understand flow.
- COMPARE WITH IF-ELSE: Review when switch is preferable over if-else chains.
- REVIEW PREVIOUS EXAM QUESTIONS: DU frequently asks switch-based programs in semester examinations.