# Introduction to Compiler Design

## 1. What is a Compiler?

A **compiler** is a computer program that translates source code written in a high-level programming language (like C, Java, Python) into a lower-level language (such as machine code, assembly language, or bytecode) that can be executed by a computer.

**Key Definition:** A compiler is a translator that converts human-readable source code into machine-executable code while checking for errors and optimizing the output.

### Purpose of Compilers

- **Translation**: Convert high-level code to low-level code
- **Error Detection**: Identify syntax and semantic errors in source code
- **Optimization**: Improve code efficiency (speed and memory usage)
- **Code Generation**: Produce executable or intermediate code

### Compiler vs Interpreter

| Aspect          | Compiler                             | Interpreter              |
| --------------- | ------------------------------------ | ------------------------ |
| Translation     | Translates entire program at once    | Translates line by line  |
| Execution       | Creates executable file              | Executes code directly   |
| Speed           | Faster execution (after compilation) | Slower execution         |
| Error Detection | Reports all errors at once           | Stops at first error     |
| Memory          | Requires more memory                 | Requires less memory     |
| Examples        | C, C++, Java                         | Python, JavaScript, Ruby |

## 2. Phases of a Compiler

A compiler operates in multiple phases, each performing specific tasks. These phases are organized into two main groups: **Analysis (Front End)** and **Synthesis (Back End)**.

```
Source Code
 |
 v
+------------------+
| Lexical Analysis | (Scanner)
+------------------+
 |
 v
+------------------+
| Syntax Analysis | (Parser)
+------------------+
 |
 v
+------------------+
| Semantic Analysis|
+------------------+
 |
 v
+------------------+
| Intermediate Code|
| Generation |
+------------------+
 |
 v
+------------------+
| Code Optimization|
+------------------+
 |
 v
+------------------+
| Code Generation |
+------------------+
 |
 v
Target Code
```

### Phase 1: Lexical Analysis (Scanning)

**Purpose**: Break source code into tokens (smallest meaningful units)

**Input**: Stream of characters
**Output**: Stream of tokens

**Example**:

```c
int sum = a + b;
```

Tokens: `int`, `sum`, `=`, `a`, `+`, `b`, `;`

**Key Concepts**:

- **Token**: A pair consisting of token name and attribute value
- **Lexeme**: Sequence of characters matching token pattern
- **Pattern**: Description of token form

### Phase 2: Syntax Analysis (Parsing)

**Purpose**: Check if tokens follow the grammatical rules of the language

**Input**: Stream of tokens
**Output**: Parse tree or syntax tree

**Example**:

```
Expression: a + b * c

Parse Tree:
 +
 / \
 a *
 / \
 b c
```

**Key Concepts**:

- **Grammar**: Set of production rules defining language syntax
- **Parse Tree**: Hierarchical representation of source code structure
- **Syntax Errors**: Violations of language grammar rules

### Phase 3: Semantic Analysis

**Purpose**: Check for semantic errors and gather type information

**Input**: Syntax tree
**Output**: Annotated syntax tree

**Functions**:

- **Type Checking**: Verify operand types match operator requirements
- **Scope Resolution**: Check if variables are declared before use
- **Type Coercion**: Convert types when necessary

**Example**:

```c
int x = 10;
float y = x + 5.5; // Type coercion: int to float
```

### Phase 4: Intermediate Code Generation

**Purpose**: Generate machine-independent intermediate representation

**Input**: Annotated syntax tree
**Output**: Intermediate code (e.g., three-address code)

**Example**:

```c
Source: y = a * b + c

Three-Address Code:
t1 = a * b
t2 = t1 + c
y = t2
```

**Common Intermediate Representations**:

- Three-address code
- Quadruples
- Triples
- Abstract syntax tree (AST)

### Phase 5: Code Optimization

**Purpose**: Improve intermediate code for better performance

**Types of Optimization**:

- **Machine-Independent**: Dead code elimination, constant folding, loop optimization
- **Machine-Dependent**: Register allocation, instruction scheduling

**Example**:

```
Before: x = 5 + 3
After: x = 8 (Constant folding)

Before: while (i < 100) { x = y + z; }
After: temp = y + z; while (i < 100) { x = temp; } (Code motion)
```

### Phase 6: Code Generation

**Purpose**: Generate target machine code

**Input**: Optimized intermediate code
**Output**: Machine code or assembly code

**Example**:

```
Three-Address Code: t1 = a * b

Assembly Code:
MOV R1, a
MUL R1, b
MOV t1, R1
```

## 3. Symbol Table Management

The **symbol table** is a data structure used by the compiler to store information about identifiers (variables, functions, classes, etc.).

**Information Stored**:

- Name
- Type
- Scope
- Memory location
- Size
- Parameters (for functions)

**Operations**:

- Insert
- Lookup
- Delete
- Update

## 4. Error Handling

Compilers detect and report various types of errors:

| Error Type   | Phase             | Example                          |
| ------------ | ----------------- | -------------------------------- |
| **Lexical**  | Lexical Analysis  | Invalid character: `$variable`   |
| **Syntax**   | Syntax Analysis   | Missing semicolon: `int x = 5`   |
| **Semantic** | Semantic Analysis | Type mismatch: `int x = "hello"` |
| **Logical**  | Runtime           | Division by zero                 |

**Error Recovery Strategies**:

- Panic mode: Skip tokens until synchronization point
- Phrase level: Local corrections
- Error productions: Add grammar rules for common errors
- Global correction: Minimal changes to fix errors

## 5. Types of Compilers

### 5.1 Single-Pass Compiler

- Processes source code in one pass
- Faster compilation
- Limited optimization
- Example: Pascal compilers

### 5.2 Multi-Pass Compiler

- Processes source code multiple times
- Better optimization
- Slower compilation
- Example: GCC, LLVM

### 5.3 Cross Compiler

- Runs on one platform, generates code for another
- Used in embedded systems development
- Example: ARM compiler on x86 machine

### 5.4 Just-In-Time (JIT) Compiler

- Compiles code during execution
- Combines compilation and interpretation
- Example: Java JVM, .NET CLR

## 6. Compiler Construction Tools

Modern compiler development uses various tools:

- **Lex/Flex**: Lexical analyzer generator
- **Yacc/Bison**: Parser generator
- **ANTLR**: Parser and lexer generator
- **LLVM**: Compiler infrastructure

## 7. Real-World Example: Compiling C Code

```c
// Source Code: hello.c
#include <stdio.h>
int main() {
 printf("Hello, World!\n");
 return 0;
}
```

**Compilation Process**:

1. **Preprocessing**: Handle `#include`, expand macros
2. **Compilation**: Generate assembly code
3. **Assembly**: Convert assembly to object code
4. **Linking**: Combine object files and libraries

```bash
gcc -o hello hello.c
```

## 8. Summary

- A compiler translates high-level code to machine code through six main phases
- **Front End** (Analysis): Lexical, Syntax, Semantic analysis
- **Back End** (Synthesis): Intermediate code generation, Optimization, Code generation
- Each phase builds upon the previous phase's output
- Symbol table and error handler support all phases
- Modern compilers use sophisticated optimization techniques
- Understanding compiler design helps in writing efficient code

## Further Reading

Students are encouraged to refer to the following textbooks for comprehensive coverage:

1. **"Compilers: Principles, Techniques, and Tools"** by Aho, Lam, Sethi, and Ullman (The Dragon Book)
2. **"Modern Compiler Implementation in C/Java/ML"** by Andrew W. Appel
3. **"Engineering a Compiler"** by Keith Cooper and Linda Torczon
