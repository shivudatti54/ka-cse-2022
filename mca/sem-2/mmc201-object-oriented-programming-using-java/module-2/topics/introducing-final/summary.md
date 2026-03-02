# Final Keyword in Java - Summary

## Key Definitions and Concepts

- **Final Variable**: A variable declared with the `final` keyword that must be initialized exactly once and cannot be modified after initialization
- **Final Method**: A method that cannot be overridden by subclasses but can be inherited
- **Final Class**: A class that cannot be extended/inherited by any other class
- **Blank Final Variable**: A final variable declared but not initialized at the time of declaration

## Important Formulas and Theorems

The `final` keyword has no formula but follows these rules:

- Final variables: Must be initialized exactly once
- Final methods: Cannot be overridden but can be overloaded
- Final classes: Cannot be inherited

## Key Points

- The `final` keyword in Java enforces immutability at variable, method, and class levels
- Final variables (constants) should be named in UPPERCASE (e.g., MAX_VALUE, PI)
- Static final variables are class-level constants shared across all instances
- Final parameters in methods prevent modification of argument values inside the method
- Final methods provide security by preventing unintended overriding of critical methods
- Final classes like String, Math are immutable by design in Java API
- Final reference variables cannot be reassigned to point to different objects
- Blank final variables must be initialized in all constructors of the class

## Common Mistakes to Avoid

- Forgetting to initialize blank final variables in all constructors
- Attempting to override final methods in subclasses
- Trying to extend a final class
- Confusing final with static - they serve different purposes
- Thinking final objects cannot be modified (only the reference is final)

## Revision Tips

1. Remember the three applications: Variables → Methods → Classes
2. Practice identifying compilation errors in code using final keyword
3. Understand that final provides restriction, not complete immutability for objects
4. Review Java API classes that are final (String, Integer, Math, etc.)
5. Write small programs to reinforce understanding of blank final variables
