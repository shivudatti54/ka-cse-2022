# C Program Structure & Compilation

## Introduction
C programming forms the bedrock of system software development and low-level programming. Understanding program structure and compilation is crucial for writing efficient, portable code and debugging complex systems. At DU's MCA program, this foundation enables students to work on embedded systems, operating systems, and performance-critical applications.

The compilation process converts human-readable code into machine-executable binaries through four key stages: preprocessing, compilation proper, assembly, and linking. Mastery of this process helps developers optimize code, manage large projects, and diagnose errors at different build stages.

In industry, this knowledge is vital for cross-platform development, creating shared libraries, and implementing build systems. Companies like Microsoft, NVIDIA, and embedded systems manufacturers specifically test these concepts during interviews for systems programming roles.

## Key Concepts

1. **Basic C Program Structure**
   - Preprocessor Directives (`#include`, `#define`)
   - `main()` Function: Program entry point
   - Function Declarations vs Definitions
   - Header Files vs Source Files
   - Memory Segments: Text, Data, BSS, Stack, Heap

2. **Compilation Stages**
   - **Preprocessing**: Macro expansion, file inclusion
     ```c
     #include <stdio.h>
     #define PI 3.14
     ```
   - **Compilation**: Convert to assembly (`.s` files)
   - **Assembly**: Generate object code (`.o` files)
   - **Linking**: Resolve external references (static/dynamic)

3. **Compiler Toolchain**
   - `gcc` workflow: `cpp → cc1 → as → ld`
   - Flags: `-E` (preprocess), `-S` (assembly), `-c` (compile only)
   - Object File Format (ELF/COFF)
   - Symbol Tables and Relocation Records

4. **Error Types**
   - Syntax Errors (compile-time)
   - Linker Errors (undefined references)
   - Runtime Errors (segmentation faults)

## Examples

**Example 1: Basic Program Analysis**
```c
#include <stdio.h>
#define MSG "Hello DU MCA"

int main() {
    printf("%s\n", MSG);
    return 0;
}
```
*Compilation Steps:*
1. Preprocessor: Expands `#include` and `#define`
2. Compiler: Generates assembly for x86/ARM
3. Assembler: Creates object file with machine code
4. Linker: Combines with libc's printf implementation

**Example 2: Multi-file Compilation**
math.h:
```c
int square(int n);
```
math.c:
```c
int square(int n) { return n*n; }
```
main.c:
```c
#include "math.h"
int main() { return square(5); }
```
*Compilation:*
```bash
gcc -c math.c       # Creates math.o
gcc -c main.c       # Creates main.o
gcc math.o main.o -o prog
```

**Example 3: Preprocessor Debugging**
```c
#include <stdio.h>
#define DEBUG 1

int main() {
    #if DEBUG
        printf("Debug mode\n");
    #endif
    return 0;
}
```
*Preprocessor Output:*
```bash
gcc -E program.c  # Shows expanded code without DEBUG block
```

## Exam Tips
1. Always mention `main()` as the entry point - its return type must be `int`
2. Linker errors often involve missing function implementations or libraries
3. `#include "file.h"` vs `<file.h>`: Quotes for user headers, brackets for system
4. Object files contain relocation information for linker
5. Static linking increases binary size but ensures portability
6. Use `-Wall` flag to catch common mistakes during compilation
7. Segmentation faults occur due to invalid memory accesses (stack/heap errors)