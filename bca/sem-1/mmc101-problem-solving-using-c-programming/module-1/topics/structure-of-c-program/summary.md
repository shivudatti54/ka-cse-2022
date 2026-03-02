# Structure of C Program - Summary

## Key Definitions and Concepts

- **Documentation Section**: Comments at the beginning of a program providing information about the program, author, date, and purpose. Comments are ignored by the compiler.

- **Preprocessor Directives**: Commands beginning with `#` that are processed before compilation. Includes `#include` for header files and `#define` for macros.

- **Global Declaration Section**: Contains global variables and function prototypes accessible throughout the program.

- **main() Function**: The mandatory entry point of every C program where execution begins and ends.

- **User-Defined Functions**: Custom functions created by the programmer to perform specific tasks, promoting modularity and code reuse.

- **Function Prototype**: A declaration that specifies the function's return type, name, and parameter types before its actual definition.

- **Compound Statement (Block)**: A group of statements enclosed in curly braces `{ }`.

## Important Formulas and Theorems

There are no specific formulas for program structure, but the standard organization follows this hierarchy:

1. Documentation (Comments)
2. Preprocessor Directives (#include, #define)
3. Global Declarations (variables, function prototypes)
4. main() Function
5. User-Defined Functions (definitions)

## Key Points

- Every executable C program MUST contain a main() function as the entry point.

- Preprocessor directives are processed before compilation through text substitution.

- Global variables are accessible from any function; local variables are confined to their declaring function.

- The return value of main() indicates program exit status to the operating system (0 = success).

- Comments (`/* */` or `//`) are ignored by the compiler and improve code readability.

- Function prototypes enable forward references and provide compile-time type checking.

- The sequence of sections in a C program is not arbitrary—it reflects the compilation process.

- Header files like `<stdio.h>` provide declarations for standard library functions.

## Common Mistakes to Avoid

- Forgetting to include the return statement in main() function
- Placing function definitions before their prototypes when using the function in main()
- Confusing global variables with local variables in terms of scope
- Adding semicolons after preprocessor directives (except in macro definitions)
- Omitting necessary header files for functions like printf() and scanf()

## Revision Tips

1. Practice writing the skeleton of a C program repeatedly until the structure becomes automatic.

2. Trace through compilation errors related to undefined functions and remember to add prototypes.

3. Create your own template file with the standard structure to use as a starting point for all programs.

4. Use meaningful comments in your programs to develop the habit of proper documentation.