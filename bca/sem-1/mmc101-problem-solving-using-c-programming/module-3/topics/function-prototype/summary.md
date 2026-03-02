# Function Prototype - Summary

## Key Definitions and Concepts

- **Function Prototype**: A declaration that specifies a function's return type, name, and parameter types to the compiler before the actual function definition
- **Forward Reference**: The ability to call a function before it is defined, made possible by declaring its prototype
- **Type Checking**: The compiler's ability to verify argument types match parameter types using prototype information
- **Parameter List**: The part of the prototype that specifies the types (and optionally names) of arguments the function accepts

## Important Formulas and Theorems

The general syntax of a function prototype is:
```
return_type function_name(parameter_type1, parameter_type2, ...);
```

Key variations include:
- No parameters: `return_type function_name(void);`
- Pointer parameters: `return_type function_name(int *ptr);`
- Array parameters: `return_type function_name(int arr[]);` or `return_type function_name(int *arr);`

## Key Points

- Function prototypes must end with a semicolon
- Parameter names in prototypes are optional but improve readability
- The prototype must exactly match the function definition in return type and parameter types
- Use void in the parameter list to explicitly indicate no parameters
- Arrays passed to functions are automatically treated as pointers
- Function prototypes enable the compiler to perform type checking at compile time
- Prototypes should be placed before main() or in header files for modular programs

## Common Mistakes to Avoid

1. Forgetting the semicolon after the function prototype
2. Confusing empty parameter list `func()` with `func(void)` - the former means unspecified parameters in modern C
3. Mismatching parameter types between prototype and definition
4. Not declaring prototypes for functions defined after main()

## Revision Tips

1. Practice writing prototypes for various function scenarios including different return types and pointer parameters
2. Remember: any function call before its definition requires a prototype declaration
3. The compiler treats array parameters as pointers, so `int func(int arr[10])` and `int func(int *arr)` are equivalent
4. Always explicitly specify return types - do not rely on implicit int return
5. Review previous year question papers to understand exam patterns for this topic