# Parameter Passing Techniques in C - Summary

## Key Definitions and Concepts

- **Parameter Passing**: The mechanism by which data is transferred between calling and called functions
- **Pass by Value**: A technique where a copy of the argument's value is passed to the function; modifications do not affect the original
- **Pass by Reference**: A technique using pointers where the memory address of a variable is passed, allowing modification of original data
- **Actual Parameter**: The variable or value used in the function call
- **Formal Parameter**: The parameter variable declared in the function definition
- **Pointer**: A variable that stores the memory address of another variable

## Important Formulas and Theorems

- In pass by value: Function receives COPY of data; original remains unchanged
- In pass by reference: Function receives ADDRESS; modifications affect original through dereferencing
- Array name as parameter decays to pointer (pass by reference automatically)
- Pointer size is typically 4 bytes (32-bit) or 8 bytes (64-bit) regardless of data type pointed to

## Key Points

- C uses pass by value as default mechanism for all parameters
- Pass by reference in C is implemented using pointers and address-of operator (&)
- Pass by value provides data protection but cannot modify caller variables
- Pass by reference enables modification of multiple variables and efficient handling of large data
- Arrays are automatically passed by reference (as pointers) in C
- Even pointers themselves are passed by value—the pointed-to data can be modified
- Passing large structures by value creates performance overhead; use pointers instead
- Pass by reference is necessary for functions that need to "return" multiple values

## Common Mistakes to Avoid

- Forgetting to use the address-of operator (&) when calling functions expecting pointers
- Dereferencing uninitialized pointers, causing undefined behavior
- Confusing the pointer variable itself with the data it points to
- Assuming arrays are passed by value—they are always passed by reference

## Revision Tips

1. Practice writing swap functions both ways to solidify understanding of both techniques
2. Trace through code manually by drawing memory boxes and showing value copies vs addresses
3. Remember: PASS BY VALUE = COPY = PROTECTED; PASS BY REFERENCE = ADDRESS = MODIFIABLE
4. Review pointer basics before exam: declaration, initialization, dereferencing, and address-of operator
5. Solve previous year DU question papers to understand the exam pattern and common question types