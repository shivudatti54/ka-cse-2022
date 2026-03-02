# Main Function and Header Files in C++ - Summary

## Key Definitions and Concepts

- **main() Function**: The entry point of every C++ program where execution begins. The standard form is `int main()` returning 0 for successful execution.

- **Header Files**: Files containing declarations of functions, classes, and constants that can be included in programs using the `#include` preprocessor directive.

- **Namespace (std)**: A container for identifiers that prevents naming conflicts; the Standard Template Library uses the `std` namespace.

- **argc/argv**: Command-line parameters where argc is argument count and argv is an array of argument strings.

## Important Formulas and Concepts

- Standard main function: `int main() { return 0; }`
- Parameterized main: `int main(int argc, char* argv[])`
- Include system header: `#include <filename>`
- Include user header: `#include "filename"`
- Input operator: `std::cin >> variable`
- Output operator: `std::cout << expression`

## Key Points

- Every C++ program must have exactly one main() function
- `void main()` is non-standard and should be avoided
- Header files provide pre-defined functionality without writing code from scratch
- The iostream header enables console input/output operations
- The std namespace contains all standard library components
- Command-line arguments allow passing data to programs at runtime
- `argv[0]` always contains the program name
- Comments (// and /* */) improve code readability but are ignored by compiler

## Common Mistakes to Avoid

1. Using `void main()` instead of `int main()` - this is non-portable
2. Forgetting to include necessary header files before using their functions
3. Not returning a value from main() when declared as int
4. Confusing `std::cin` (input) and `std::cout` (output) operators
5. Using `using namespace std` globally in large programs causes namespace pollution

## Revision Tips

1. Practice writing at least 3-4 complete programs covering different header files
2. Memorize the syntax for parameterized main() function
3. Remember that C++ is case-sensitive - all standard library names are lowercase
4. Focus on understanding the flow: preprocessing → compilation → execution
5. Review previous year question papers to understand exam patterns
6. Make flash cards for common header files and their purposes