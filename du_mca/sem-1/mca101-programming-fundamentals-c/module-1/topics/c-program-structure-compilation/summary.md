# C Program Structure and Compilation - Summary

## Key Definitions and Concepts

- **Preprocessor**: A program that processes directives before compilation, handling macro expansion, file inclusion, and conditional compilation.
- **Translation Unit**: A source file together with all included headers, compiled independently into an object file.
- **Linkage**: The property determining whether identifiers (variables, functions) can be accessed across different translation units.
- **Function Prototype**: A declaration specifying a function's return type, name, and parameter types.
- **Header Guard**: Preprocessor directives (#ifndef, #define, #endif) preventing multiple inclusion of header files.

## Important Formulas and Concepts

- **Compilation stages**: Source Code → Preprocessor → Compiler → Assembler → Linker → Executable
- **Variable scope types**: Block scope, function scope, function prototype scope, file scope
- **Linkage types**: External (accessible across files), Internal (restricted to one file), No linkage (local variables)

## Key Points

1. Every executable C program must have a `main()` function as the entry point.
2. The four compilation stages are: Preprocessing, Compilation, Assembly, and Linking.
3. Preprocessor directives begin with '#' and are processed before actual compilation.
4. `#include <file>` searches system directories; `#include "file"` searches current directory first.
5. Header guards prevent multiple inclusion and circular dependency problems.
6. Global variables have file scope and external linkage by default.
7. The `static` keyword changes linkage from external to internal.
8. `extern` keyword declares variables defined in other translation units.
9. The `return 0;` in main() indicates successful program execution.
10. Comments (`/* */` or `//`) are ignored by the compiler but aid readability.

## Common Mistakes to Avoid

- Forgetting to include header files for standard library functions
- Not using header guards in custom header files, causing redefinition errors
- Confusing declaration with definition (declaration announces; definition allocates storage)
- Placing function calls before their declarations without prototypes (causes warnings)
- Omitting the return statement in non-void functions

## Revision Tips

1. Draw the compilation process diagram and explain each stage verbally.
2. Write a simple program and compile with different flags (-E, -S, -c) to see outputs at each stage.
3. Create a multi-file project to understand linking and extern keyword usage.
4. Memorize standard header files and their purposes (<stdio.h>, <stdlib.h>, <string.h>).
5. Practice identifying which compilation stage would catch specific types of errors.