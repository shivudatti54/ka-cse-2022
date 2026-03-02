# The General Form of a C++ Program - Summary

## Key Definitions and Concepts

- **Preprocessor Directives**: Instructions to the compiler processed before compilation begins; begin with `#` symbol (e.g., `#include`).
- **Header Files**: Files containing declarations of functions, classes, and variables that provide interfaces to libraries.
- **Namespace**: A declarative region that provides scope for identifiers; `std` is the standard C++ library namespace.
- **main() Function**: The entry point of every C++ program; execution begins from this function.
- **cout**: Standard output stream object used for displaying output.
- **cin**: Standard input stream object used for reading input.
- **Statement**: A complete instruction that ends with a semicolon (;).
- **Block**: A group of zero or more statements enclosed in curly braces { }.

## Important Formulas and Concepts

- **Stream Insertion Operator**: `cout << variable;` - outputs data to console
- **Stream Extraction Operator**: `cin >> variable;` - reads input from console
- **Return Value Convention**: `return 0;` indicates successful execution; non-zero indicates error

## Key Points

1. Every C++ program must have a `main()` function as the entry point.

2. Preprocessor directives (like `#include`) must appear before any other code.

3. Header files provide access to pre-defined functions and classes.

4. The `using namespace std;` directive makes standard library names accessible without the `std::` prefix.

5. C++ is case-sensitive; `main` and `Main` are different identifiers.

6. All executable statements must end with a semicolon.

7. Class definitions in C++ must end with a semicolon after the closing brace.

8. The `return` statement in `main()` returns an exit status to the operating system.

## Common Mistakes to Avoid

1. **Forgetting the semicolon**: Every statement (except blocks) must end with a semicolon.

2. **Incorrect header file syntax**: Using wrong delimiters (`< >` vs `" "`).

3. **Missing main function**: Programs cannot execute without the main function.

4. **Case sensitivity errors**: Writing `Main` or `MAIN` instead of `main`.

5. **Missing return statement**: Always include `return 0;` in main.

## Revision Tips

1. Practice writing the basic program structure repeatedly until it becomes automatic.

2. Memorize the standard header files and their purposes.

3. Remember the flow: Preprocessor directives → Namespace → main() function → Statements.

4. Review previous university question papers to understand the pattern of questions on this topic.

5. Compile and run various simple programs to reinforce understanding of the structure.
