# Compiling and Executing C++ Programs

## A Comprehensive Study Guide for BSc Physical Science (CS) - Delhi University NEP 2024

---

## 1. Introduction

### 1.1 What is Compilation?

Compilation is the process of converting source code written in a high-level programming language (like C++) into machine code that can be executed directly by the computer's processor. This process is fundamental to software development and represents a critical skill for every programmer.

### 1.2 Why This Topic Matters

Understanding the compilation and execution process is essential for several reasons:

- **Debugging**: Knowing what happens at each phase helps identify and fix errors
- **Optimization**: Understanding compilation phases allows developers to write more efficient code
- **Build Systems**: Modern software development requires knowledge of build tools
- **Career Relevance**: This forms the foundation for systems programming, embedded systems, and performance-critical applications

### 1.3 Real-World Relevance

Every software you use—from Microsoft Office to video games—undergoes compilation. When you run a C++ program, the compilation process happens behind the scenes. Major companies like Google, Facebook, and game studios rely on C++ compilation expertise to build high-performance applications. Understanding this process gives you control over how your code transforms into an executable program.

---

## 2. The C++ Compilation Process: A Detailed Overview

The C++ compilation process consists of four distinct phases, each transforming your code in specific ways:

### 2.1 Phase 1: Preprocessing

The preprocessor handles directives that begin with `#` (hash symbols). These are instructions for the compiler to be processed before actual compilation begins.

**Key Preprocessor Directives:**

- `#include`: Includes header files
- `#define`: Defines macros
- `#ifdef`, `#ifndef`, `#endif`: Conditional compilation
- `#pragma`: Implementation-specific directives

**What Happens During Preprocessing:**

1. File inclusion: The contents of included headers are copied into the source file
2. Macro expansion: `#define` macros are replaced with their values
3. Conditional compilation: Code blocks are included/excluded based on conditions
4. Line control: Line numbers are updated for error reporting

**Example of Preprocessing:**

```cpp
// File: constants.h
#define PI 3.14159
#define SQUARE(x) ((x) * (x))

// File: main.cpp
#include <iostream>
#include "constants.h"

int main() {
    std::cout << "Value of PI: " << PI << std::endl;
    std::cout << "Square of 5: " << SQUARE(5) << std::endl;
    return 0;
}
```

After preprocessing, the `main.cpp` file expands to include all the code from `iostream` and `constants.h`.

### 2.2 Phase 2: Compilation (Translation to Assembly)

The compiler parses the preprocessed code, checks for syntax and semantic errors, and translates the C++ code into assembly language instructions.

**Compiler Tasks:**

1. **Lexical Analysis**: Breaks source code into tokens (keywords, identifiers, operators, literals)
2. **Syntax Analysis**: Checks if tokens follow C++ grammar rules
3. **Semantic Analysis**: Checks type compatibility, scope rules, and other semantic constraints
4. **Code Generation**: Generates intermediate representation (IR) and finally assembly code
5. **Optimization**: Applies various optimizations to improve performance

**Example - C++ to Assembly:**

```cpp
// Source C++ code
int add(int a, int b) {
    return a + b;
}

// Generated Assembly (x86-64, simplified)
add:
    push    rbp
    mov     rbp, rsp
    mov     edi, edi          ; parameter a
    mov     esi, esi          ; parameter b
    lea     eax, [rdi+rsi]    ; eax = a + b
    pop     rbp
    ret
```

### 2.3 Phase 3: Assembly

The assembler converts assembly language instructions into machine code—binary instructions that the processor can execute directly. This phase produces **object files** (`.o` or `.obj` files).

**Object File Contents:**

- **Machine Code**: Binary instructions for the processor
- **Symbol Table**: Names of functions and variables defined/referenced
- **Relocation Information**: Addresses that need adjustment during linking
- **Debugging Information**: Source line numbers and variable information (if compiled with `-g`)

**Types of Object Files:**

| Type | Extension | Description |
|------|-----------|-------------|
| COFF | `.obj` | Common Object File Format (Windows) |
| ELF | `.o` | Executable and Linkable Format (Linux) |
| Mach-O | `.o` | Mach Object format (macOS) |

### 2.4 Phase 4: Linking

The linker combines one or more object files and libraries to create the final executable program.

**Linker Responsibilities:**

1. **Symbol Resolution**: Matches function calls and variable references across object files
2. **Address Relocation**: Adjusts memory addresses based on final layout
3. **Library Linking**: Incorporates code from static libraries
4. **Symbol Binding**: Connects external symbols to their definitions

**Types of Linking:**

- **Static Linking**: Library code is copied into the final executable at compile time
- **Dynamic Linking**: Library code is loaded at runtime (`.dll` on Windows, `.so` on Linux)

---

## 3. Practical Examples: Using g++ Compiler

### 3.1 Basic Compilation Commands

**Example 1: Simple Program Compilation**

```cpp
// File: hello.cpp
#include <iostream>

int main() {
    std::cout << "Hello, Delhi University!" << std::endl;
    std::cout << "Welcome to C++ Programming" << std::endl;
    return 0;
}
```

**Compilation Commands:**

```bash
# Basic compilation (creates a.out)
g++ hello.cpp

# Compile with output filename
g++ hello.cpp -o hello

# Compile with optimization (-O2 or -O3)
g++ hello.cpp -o hello -O2

# Compile with debugging symbols
g++ hello.cpp -o hello -g
```

**Execution:**

```bash
./hello
```

Output:
```
Hello, Delhi University!
Welcome to C++ Programming
```

### 3.2 Multi-File Compilation Example

**File 1: math_operations.h**

```cpp
#ifndef MATH_OPERATIONS_H
#define MATH_OPERATIONS_H

int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
double divide(double a, double b);

#endif
```

**File 2: math_operations.cpp**

```cpp
#include "math_operations.h"

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

double divide(double a, double b) {
    if (b == 0) {
        return 0; // Handle division by zero
    }
    return a / b;
}
```

**File 3: main.cpp**

```cpp
#include <iostream>
#include "math_operations.h"

int main() {
    int x = 20, y = 10;
    
    std::cout << "Addition: " << add(x, y) << std::endl;
    std::cout << "Subtraction: " << subtract(x, y) << std::endl;
    std::cout << "Multiplication: " << multiply(x, y) << std::endl;
    std::cout << "Division: " << divide(x, y) << std::endl;
    
    return 0;
}
```

**Compilation Methods:**

```bash
# Method 1: Compile all files at once
g++ main.cpp math_operations.cpp -o calculator

# Method 2: Compile to object files first, then link
g++ -c main.cpp -o main.o
g++ -c math_operations.cpp -o math_operations.o
g++ main.o math_operations.o -o calculator

# Method 3: With optimization and warnings
g++ -Wall -O2 main.cpp math_operations.cpp -o calculator
```

**Execution:**

```bash
./calculator
```

Output:
```
Addition: 30
Subtraction: 10
Multiplication: 200
Division: 2
```

### 3.3 Viewing Intermediate Files

```bash
# Preprocess only (save to hello.i)
g++ -E hello.cpp -o hello.i

# Compile to assembly only (save to hello.s)
g++ -S hello.cpp -o hello.s

# Assemble to object file (save to hello.o)
g++ -c hello.cpp -o hello.o

# View object file symbols
nm hello.o

# View object file information
objdump -f hello.o
```

---

## 4. Build Systems

### 4.1 Why Build Systems?

When projects grow larger with hundreds of source files, manually compiling each file becomes impractical. Build systems automate the compilation process, track dependencies, and manage complex builds.

### 4.2 Make and Makefiles

**Makefile Example:**

```makefile
# Makefile for calculator project

CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17
TARGET = calculator
OBJS = main.o math_operations.o

# Main target
$(TARGET): $(OBJS)
	$(CXX) $(OBJS) -o $(TARGET)

# Compile main.cpp
main.o: main.cpp math_operations.h
	$(CXX) $(CXXFLAGS) -c main.cpp -o main.o

# Compile math_operations.cpp
math_operations.o: math_operations.cpp math_operations.h
	$(CXX) $(CXXFLAGS) -c math_operations.cpp -o math_operations.o

# Clean build artifacts
clean:
	rm -f $(OBJS) $(TARGET)

.PHONY: clean
```

**Makefile Commands:**

```bash
# Build the project
make

# Clean build artifacts
make clean

# Build specific target
make math_operations.o
```

### 4.3 CMake (Cross-Platform Build System)

**CMakeLists.txt:**

```cmake
cmake_minimum_required(VERSION 3.10)
project(CalculatorApp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add executable
add_executable(calculator 
    main.cpp 
    math_operations.cpp
    math_operations.h
)

# Add compiler warnings
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(calculator PRIVATE -Wall -Wextra)
endif()
```

**CMake Commands:**

```bash
# Create build directory
mkdir build
cd build

# Configure project
cmake ..

# Build project
cmake --build .

# Run executable
./calculator
```

---

## 5. Common Compilation Errors and Debugging

### 5.1 Preprocessor Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `No such file or directory` | Header file not found | Check include paths with `-I` flag |
| `Macro expansion error` | Syntax error in macro | Check parentheses in macro definitions |
| `Unexpected #endif` | Mismatched conditional directives | Verify all `#if`/`#ifdef` have matching `#endif` |

**Example Fix:**

```bash
# Include custom header directory
g++ main.cpp -I./include -o main
```

### 5.2 Compilation Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Syntax error` | Invalid C++ syntax | Check code syntax carefully |
| `Undefined reference` | Function/variable not declared | Add proper declarations |
| `Incompatible types` | Type mismatch | Check variable types |
| `Multiple definition` | Duplicate definitions | Use header guards |

**Example: Fixing Undefined Reference**

```cpp
// Error: Undefined reference to 'function'
// Solution: Ensure function is defined or linked

// math_utils.cpp
int square(int x) {
    return x * x;
}

// main.cpp - ensure math_utils.cpp is compiled and linked
int square(int x);  // Declaration

int main() {
    return square(5);
}
```

```bash
# Correct compilation
g++ main.cpp math_utils.cpp -o main
```

### 5.3 Linking Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Undefined reference to main` | No main() function | Add main() function |
| `Multiple definition` | Same symbol in multiple files | Use extern or separate definitions |
| `Cannot find -l<library>` | Library not found | Use `-L` to specify library path |

**Example Fix:**

```bash
# Specify library search path and link math library
g++ main.cpp -o main -L/usr/lib -lm
```

---

## 6. Important Compiler Flags

```bash
# Standard and version
g++ -std=c++17 main.cpp          # Use C++17 standard
g++ -std=c++20 main.cpp          # Use C++20 standard

# Optimization levels
g++ -O0 main.cpp                 # No optimization (faster compile)
g++ -O1 main.cpp                 # Basic optimization
g++ -O2 main.cpp                 # Standard optimization
g++ -O3 main.cpp                 # Aggressive optimization

# Debugging
g++ -g main.cpp                  # Include debug symbols
g++ -g -O0 main.cpp              # Debug with no optimization

# Warnings
g++ -Wall main.cpp               # Enable all warnings
g++ -Wextra main.cpp             # Enable extra warnings
g++ -Werror main.cpp             # Treat warnings as errors

# Include paths
g++ -I./include main.cpp         # Add include directory
g++ -I./include -I./src main.cpp # Multiple include directories

# Library paths
g++ -L./lib main.cpp             # Add library search path
g++ -lmymath main.cpp            # Link libmymath.so/a

# Preprocessor
g++ -DDEBUG main.cpp             # Define DEBUG macro
g++ -E main.cpp                  # Preprocess only
g++ -S main.cpp                  # Compile to assembly only
g++ -c main.cpp                  # Compile to object file only
```

---

## 7. Delhi University Syllabus Context

This topic aligns with the **Ge1B: Programming Using C++** course under the NEP 2024 curriculum for BSc Physical Science (CS). The compilation and execution process forms the foundation for understanding:

- Program structure and organization
- Header files and modular programming
- Error handling and debugging
- Software development lifecycle
- Build automation

**Expected Learning Outcomes:**

1. Understand the complete compilation pipeline
2. Execute C++ programs using command-line tools
3. Handle multi-file projects
4. Debug compilation and linking errors
5. Use build tools effectively

---

## 8. Key Takeaways

1. **Four-Phase Process**: The C++ compilation involves preprocessing, compilation (to assembly), assembly (to object code), and linking.

2. **Preprocessor**: Handles `#include`, `#define`, and conditional compilation before actual compilation begins.

3. **Compiler**: Translates C++ to assembly language, performing syntax checking, semantic analysis, and optimization.

4. **Assembler**: Converts assembly to machine code object files containing binary instructions and symbol tables.

5. **Linker**: Combines object files and libraries to create the final executable, resolving all symbol references.

6. **g++ Commands**: Master commands like `g++ -c`, `g++ -o`, `g++ -Wall`, `g++ -O2`, and `g++ -g` for various compilation needs.

7. **Multi-File Projects**: Compile multiple source files together or create object files separately and link them.

8. **Build Systems**: Use Make or CMake for automating builds in larger projects with many source files.

9. **Error Identification**: Understanding which compilation phase produces which type of error is crucial for debugging.

10. **Compiler Flags**: Use appropriate flags for optimization, debugging, standards compliance, and warnings.

---

## 9. Flashcards

| Term | Definition |
|------|------------|
| **Preprocessor** | Program that processes directives (#include, #define) before compilation |
| **Compiler** | Translates C++ source code to assembly language |
| **Assembler** | Converts assembly language to machine code (object files) |
| **Linker** | Combines object files and libraries to create executable |
| **Object File** | Binary file containing machine code and symbol information |
| **Symbol Resolution** | Process of matching function calls with their definitions |
| **Static Linking** | Linking at compile time; library code copied into executable |
| **Dynamic Linking** | Linking at runtime; library loaded when program runs |
| **Makefile** | Build configuration file for the make utility |
| **Header Guard** | Preprocessor directive to prevent multiple inclusion |

---

## 10. Multiple Choice Questions

### Question 1
Which phase of C++ compilation handles the `#include` directive?

A) Assembly  
B) Linking  
C) Preprocessing  
D) Compilation  

**Answer: C** - The preprocessor handles all directives starting with `#`, including `#include`.

---

### Question 2
What is the file extension of an object file in Linux?

A) `.obj`  
B) `.o`  
C) `.exe`  
D) `.so`  

**Answer: B** - In Linux (ELF), object files typically have the `.o` extension.

---

### Question 3
Which g++ flag produces an object file without creating an executable?

A) `-o`  
B) `-c`  
C) `-S`  
D) `-E`  

**Answer: B** - The `-c` flag compiles source files to object files without linking.

---

### Question 4
What does the linker do?

A) Checks syntax errors  
B) Converts assembly to machine code  
C) Combines object files and resolves symbol references  
D) Preprocesses header files  

**Answer: C** - The linker combines object files and resolves external symbol references.

---

### Question 5
Which flag enables all warnings in g++?

A) `-warn`  
B) `-Wall`  
C) `-Wextra`  
D) `-error`  

**Answer: B** - `-Wall` enables all common warnings in g++.

---

### Question 6
What is the purpose of the `-D` flag in g++?

A) Define a macro  
B) Delete a file  
C) Debug mode  
D) Display information  

**Answer: A** - The `-D` flag defines preprocessor macros.

---

### Question 7
In which format are Windows DLLs typically linked?

A) Static linking  
B) Dynamic linking  
C) No linking  
D) Pre-linking  

**Answer: B** - DLLs (Dynamic Link Libraries) are linked dynamically at runtime.

---

### Question 8
What does `nm` command display?

A) Number of lines in source file  
B) Symbol table of object files  
C) Machine code  
D) Preprocessed output  

**Answer: B** - The `nm` command displays symbols (functions, variables) in object files.

---

### Question 9
Which C++ standard flag specifies C++17?

A) `-std=c++14`  
B) `-std=c++17`  
C) `-std=c++20`  
D) `-std=c++11`  

**Answer: B** - `-std=c++17` specifies the C++17 standard.

---

### Question 10
What is the purpose of a header guard?

A) Protect files from viruses  
B) Prevent multiple inclusion of headers  
C) Encrypt source code  
D) Compress header files  

**Answer: B** - Header guards (#ifndef/#define/#endif) prevent a header from being included multiple times.

---

*End of Study Material*