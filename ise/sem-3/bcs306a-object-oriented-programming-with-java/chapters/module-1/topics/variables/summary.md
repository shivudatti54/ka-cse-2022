# Variables in Java - Summary

## Key Definitions and Concepts

- **Variable:** A named storage location in memory that holds a value which can be modified during program execution.
- **Variable Declaration:** The statement that specifies a variable's data type and name.
- **Variable Initialization:** Assigning a value to a variable for the first time.
- **Scope:** The region of code where a variable is accessible.
- **Lifetime:** The period during which a variable exists in memory.
- **Instance Variable:** A variable declared in a class but outside methods, unique to each object.
- **Static Variable:** A variable declared with the static keyword, shared by all objects of a class.
- **Local Variable:** A variable declared inside a method or block, accessible only within that scope.
- **Parameter:** A variable in a method definition that receives passed values.

## Important Formulas and Theorems

- Variable declaration syntax: `dataType variableName;`
- Declaration with initialization: `dataType variableName = value;`
- Static variable declaration: `static dataType variableName = value;`
- Default values: int → 0, double → 0.0, boolean → false, reference → null

## Key Points

- Java is a statically typed language; variable types must be declared at compile time.
- Four types of variables exist: instance, static, local, and parameters.
- Instance and static variables have default values; local variables do not.
- Static variables belong to the class and are shared across all objects.
- Local variables must be initialized before use; otherwise, compilation error occurs.
- Variable scope is determined by the block where the variable is declared.
- Use camelCase for regular variables and UPPERCASE for constants.
- Java keywords cannot be used as variable names.
- Variables can contain letters, digits, underscores, and dollar signs; first character cannot be digit.
- Inner blocks can access outer variables, but not vice versa.

## Common Mistakes to Avoid

- Using uninitialized local variables (causes compilation error).
- Confusing static variables with instance variables regarding sharing behavior.
- Using Java keywords as variable names.
- Declaring variables with names starting with digits.
- Forgetting that variables declared inside loops or if blocks are not accessible outside them.
- Not understanding that instance variables get default values but local variables do not.

## Revision Tips

1. Create a table comparing all four variable types with their scope, default values, and memory location.

2. Write small programs to practice declaring and using different types of variables.

3. Memorize the default values for primitive types and object references.

4. Review Java naming conventions and ensure your code follows them.

5. Solve previous year exam questions related to variable scope and initialization.