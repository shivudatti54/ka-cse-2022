# Variables in Java - Summary

## Key Definitions and Concepts

- **Variable**: A named storage location in memory that holds a value which can be modified during program execution
- **Variable Declaration**: The statement that specifies the data type and name of a variable before using it
- **Variable Initialization**: Assigning an initial value to a variable at the time of declaration or before first use
- **Scope**: The region of code where a variable can be accessed and used

## Important Formulas and Techniques

```java
// Basic declaration
dataType variableName;

// Declaration with initialization
dataType variableName = value;

// Static variable
static dataType variableName;

// Final constant
final dataType VARIABLE_NAME = value;

// Type inference
var variableName = value;
```

## Key Points

- Java has four types of variables: instance, static (class), local, and parameters
- Instance variables are declared in a class outside methods and belong to objects
- Static variables are shared among all objects and declared with the `static` keyword
- Local variables exist only within the method or block where they are declared
- Local variables MUST be initialized before use; they do not have default values
- Instance and static variables receive default values (0, false, null)
- The `final` keyword creates constants that cannot be reassigned
- The `var` keyword (Java 10+) enables local variable type inference
- Variable names follow camelCase convention; constants use UPPERCASE

## Common Mistakes to Avoid

1. Using uninitialized local variables (causes compile error)
2. Confusing instance variables with static variables
3. Trying to use `var` for method parameters or return types
4. Using Java keywords as variable names
5. Forgetting that variable names are case-sensitive

## Revision Tips

1. Practice declaring all four types of variables in sample programs
2. Create a table comparing scope, default values, and memory allocation for each variable type
3. Write programs that demonstrate variable shadowing and understand how it works
4. Remember that static variables are initialized when the class is loaded, not when objects are created
5. Review previous year exam questions on variables to understand the question pattern and important topics