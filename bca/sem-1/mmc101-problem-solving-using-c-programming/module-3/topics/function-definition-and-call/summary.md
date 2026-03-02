# Function Definition And Call - Summary

## Key Definitions and Concepts

- FUNCTION: A self-contained block of code that performs a specific task and can be called from other parts of a program.

- FUNCTION DEFINITION: The complete implementation of a function specifying return type, name, parameters, and body.

- FUNCTION CALL: The mechanism that transfers control from the calling function to the called function, with arguments passed to parameters.

- ACTUAL PARAMETERS (ARGUMENTS): Variables or expressions passed to a function at the time of calling.

- FORMAL PARAMETERS: Variables declared in the function definition that receive copies of actual parameters.

- PASS-BY-VALUE: The parameter passing mechanism in C where copies of actual parameter values are assigned to formal parameters.

- RETURN STATEMENT: Statement that terminates function execution and optionally returns a value to the calling function.

## Important Formulas and Theorems

The general syntax for function definition:
```
return_type function_name(parameter_list) {
    declarations
    statements
    return expression;
}
```

The general syntax for function call:
```
function_name(argument_list);
```

## Key Points

- Every C program must have a main() function where execution begins.
- Parameters are passed by value in C; modifications inside the function do not affect original variables.
- Functions can return at most one value using the return statement.
- A function can have multiple return statements, but only one executes per call.
- Void functions use return without a value to exit early.
- Variables declared inside a function have block scope and automatic storage duration by default.
- Static variables retain their values between function calls.
- Function prototypes enable compile-time type checking.

## Common Mistakes to Avoid

- Forgetting the return statement in functions with non-void return type.
- Mismatching the number, type, or order of actual and formal parameters.
- Attempting to modify actual parameters inside the function (they are copies).
- Declaring a function with a return type but not using the return statement.
- Confusion between function declaration (prototype) and function definition.

## Revision Tips

- Practice writing at least 5 different function definitions covering various scenarios.
- Trace through example programs step-by-step to understand control flow.
- Remember that pass-by-value means changes inside functions don't affect calling variables.
- Review old exam questions on function calls and parameter passing.
- Write small programs and manually trace the execution to verify understanding.