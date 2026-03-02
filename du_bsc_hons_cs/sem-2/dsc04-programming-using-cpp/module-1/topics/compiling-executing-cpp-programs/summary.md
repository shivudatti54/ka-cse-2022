# Compiling and Executing C++ Programs - Summary

## Key Definitions and Concepts

- **Preprocessor**: Processes directives (#include, #define) before compilation, expands macros and includes header files
- **Compiler**: Translates C++ code to assembly language, performs syntax and semantic analysis
- **Assembler**: Converts assembly instructions to machine code (binary)
- **Linker**: Resolves references between object files and libraries, produces final executable
- **g++**: GNU C++ compiler, standard tool for compiling C++ programs on Linux/Unix systems

## Important Commands

- Basic compilation: `g++ program.cpp -o program`
- Compile with warnings: `g++ -Wall program.cpp -o program`
- Compile multiple files: `g++ file1.cpp file2.cpp -o program`
- Compile to object file only: `g++ -c program.cpp`
- Debug build: `g++ -g program.cpp -o program`
- Optimization: `g++ -O2 program.cpp -o program`
- Specify C++ standard: `g++ -std=c++17 program.cpp -o program`

## Key Points

1. C++ compilation involves four distinct phases: preprocessing → compilation → assembly → linking

2. Preprocessor handles all lines starting with # (include, define, ifdef)

3. Compiler errors indicate syntax mistakes; linker errors indicate missing function/variable definitions

4. The `-c` flag stops after assembly, producing .o object files without linking

5. Multiple source files must be compiled together or linked after individual compilation

6. Header files (.h) provide declarations; source files (.cpp) provide definitions

7. Object files contain machine code but aren't executable until linked

8. The linker connects your code with standard library functions

## Common Mistakes to Avoid

- Forgetting to link multiple source files together
- Using .h files in #include without proper setup
- Confusing compilation errors with linking errors
- Not using -Wall flag to catch potential warnings
- Trying to run source files directly instead of executables

## Revision Tips

1. Draw the compilation pipeline from memory and label each stage's input/output

2. Practice compiling the same program with different flags and observe outputs

3. Create intentional errors (missing semicolon, undefined function) and identify error types

4. Review practical exam questions involving command-line compilation

5. Remember: Preprocessor doesn't know C++ syntax, only text substitution