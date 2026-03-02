# Assignment Operators in Java - Summary

## Key Definitions and Concepts

- **Assignment Operator (=):** The fundamental operator that assigns values to variables, with right-to-left associativity.
- **Compound Assignment Operators:** Combine arithmetic/bitwise operations with assignment (+=, -=, \*=, /=, %=, &=, |=, ^=, <<=, >>=, >>>=).
- **Chained Assignment:** Multiple variables assigned in a single statement using the return value of each assignment.
- **Reference Assignment:** For objects, assignment copies the reference (memory address), not the object itself.

## Important Formulas and Theorems

- `variable operator= expression` is equivalent to `variable = variable operator expression`
- Assignment returns the assigned value, enabling chained assignments
- Assignment has lowest precedence (evaluated last) and right-to-left associativity
- Primitive assignment copies value; object assignment copies reference

## Key Points

- The simple assignment operator (=) is fundamental for variable initialization and modification
- Compound operators provide efficiency by evaluating the variable only once
- Type casting may be required for assignment between incompatible types (explicit cast for narrowing)
- Reference assignment in OOP means multiple variables point to the same object
- Assignment expressions can be used anywhere a value is expected
- Integer division in assignment truncates decimal portion
- Bitwise compound operators work on integer types only

## Common Mistakes to Avoid

- Confusing assignment (=) with comparison (==) - Java catches this error at compile time
- Forgetting that object assignment creates shared references, not independent copies
- Not considering data loss when using explicit narrowing casts
- Assuming compound operators work identically to expanded forms with different data types

## Revision Tips

- Practice writing all compound operators and their equivalent expanded forms
- Trace through code examples with reference variables to understand object sharing
- Remember that assignment has right-to-left associativity for chained assignments
- Review type conversion rules between primitive types before the exam
