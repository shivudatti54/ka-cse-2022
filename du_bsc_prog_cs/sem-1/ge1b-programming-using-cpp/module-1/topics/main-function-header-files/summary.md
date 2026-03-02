# Main Function and Header Files in C++ - Summary

## Key Definitions and Concepts

- **main() Function**: The mandatory entry point of every C++ program. Must have return type `int` and should return 0 for successful execution.

- **Header Files**: Files containing declarations for functions, classes, and variables that provide interfaces to pre-compiled library code.

- **#include Directive**: A preprocessor directive that inserts the contents of a header file into the source code before compilation.

- **Namespace**: A container that groups related identifiers to avoid naming conflicts. The C++ Standard Library uses the `std` namespace.

- **Command-line Arguments**: Parameters passed to main() via `argc` (argument count) and `argv` (argument vector) when running the program from the terminal.

## Important Formulas and Theorems

- **main() Signature**: `int main(int argc, char* argv[])` - allows command-line argument handling
- **Input extraction**: `cin >> variable;` - extracts value from standard input
- **Output insertion**: `cout << expression;` - sends value to standard output
- **Formatting**: `setprecision(n)`, `setw(n)`, `fixed` from `<iomanip>`
- **Math functions**: `pow(x, y)` for x^y, `sqrt(x)` for square root from `<cmath>`

## Key Points

- Every executable C++ program must contain exactly one `int main()` function
- Return 0 from main() indicates successful program completion
- Angle brackets `#include <header>` are for system headers; quotes are for user-defined headers
- `<iostream>` provides cin, cout, cerr for input/output operations
- Always use `std::` prefix or appropriate using declarations for standard library identifiers
- `endl` flushes the buffer; prefer `'\n'` for better performance in loops
- Command-line arguments include the program name in argc count
- Use `<string>` for C++ string class, not C-style character arrays

## Common Mistakes to Avoid

- Using `void main()` instead of `int main()` - this is non-standard
- Forgetting to return a value from main() or returning the wrong type
- Using `#include "iostream"` instead of `#include <iostream>` for standard headers
- Confusing `cin >>` with `cin <<` (extraction vs insertion operators)
- Using integer division when floating-point division is needed (5/2 vs 5.0/2)
- Not flushing output buffers when needed using `endl`

## Revision Tips

- Practice writing at least 3-4 complete programs covering different header files before the exam
- Memorize the standard headers and their purposes: iostream (I/O), iomanip (formatting), string (strings), cmath (math), cstdlib (utilities)
- Understand the flow: preprocessor → compilation → linking → execution
- Review command-line argument programs as this is a common examination topic
- Remember that `using namespace std;` is acceptable in small programs but explicit `std::` is better practice