# Tokens, Data Types, and Variables – Programming Fundamentals C (MCA Delhi University)

## Introduction
This summary covers the foundational concepts of Tokens, Data Types, and Variables in C, as per the Delhi University MCA syllabus (Revised June 2024). It is designed for quick revision before exams.

## Tokens
Tokens are the smallest units of a C program, categorized as:
- **Keywords**: Reserved words (e.g., `int`, `if`, `while`) with predefined meanings.
- **Identifiers**: User-defined names for variables, functions, or arrays (e.g., `sum`, `main`); must start with a letter or underscore, case-sensitive.
- **Constants**: Fixed values (e.g., `10`, `'A'`) that do not change during execution.
- **Strings**: Sequences of characters enclosed in double quotes (e.g., `"Hello"`).
- **Operators**: Symbols performing operations (e.g., `+`, `-`, `*`, `/`).
- **Punctuators**: Symbols like `;`, `,`, `{}`, `()` used for syntax.

## Data Types
C supports several data types, essential for defining the type of data a variable can hold:
- **Primary Data Types**: `int` (integer), `float` (floating-point), `char` (character), `double` (double-precision float).
- **Derived Data Types**: Arrays, pointers, functions.
- **User-Defined Data Types**: Structures, unions, enumerations.
- **Type Modifiers**: `short`, `long`, `signed`, `unsigned` (e.g., `short int`, `unsigned char`).

## Variables
Variables are named storage locations in memory that hold values:
- **Declaration**: Specifies data type and variable name (e.g., `int age;`).
- **Definition**: Declaration + memory allocation (e.g., `int age = 20;`).
- **Initialization**: Assigning an initial value at declaration (e.g., `float pi = 3.14;`).
- **Scope**: 
  - **Local**: Inside a block or function.
  - **Global**: Outside all functions, accessible throughout the program.
- **Storage Classes**: 
  - `auto` (default for local), `static`, `extern`, `register`.

## Key Points for Exam
- Tokens form the lexical structure of C programs.
- Data types determine memory size and operations (e.g., `int` typically 2 or 4 bytes).
- Variables must be declared before use; naming follows identifier rules.
- Constants are defined using `#define` or `const` keyword.
- Delhi University syllabus emphasizes understanding types, declarations, and basic memory concepts.

## Conclusion
Mastering tokens, data types, and variables is crucial for writing effective C programs. These concepts are foundational for topics like operators, control structures, and functions in the syllabus. Ensure thorough practice with declarations, initializations, and scope for exam success.