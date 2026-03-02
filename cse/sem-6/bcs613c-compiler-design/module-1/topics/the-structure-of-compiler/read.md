# Structure of a Compiler

## Introduction

A compiler is a sophisticated software system that translates source code written in a high-level programming language (like C, Java, Python) into a low-level language (like machine code or assembly language) that can be executed by a computer. Understanding its internal structure is fundamental to the field of compiler design. The compilation process is not a single monolithic task but is divided into a series of well-defined phases, each with a specific responsibility. These phases are often grouped into two major parts: the **Analysis** (Front End) and the **Synthesis** (Back End).

## Major Phases of a Compiler

The compilation process can be broken down into the following primary phases:

```
+-------------------+ +-------------------+ +-------------------+ +-------------------+
| Source Program | -> | Lexical Analyzer | -> | Syntax Analyzer | -> | Semantic Analyzer |
+-------------------+ +-------------------+ +-------------------+ +-------------------+
 |
 v
+-------------------+ +-------------------+ +-------------------+ +-------------------+
| Target Program | <- | Code Optimizer | <- | Intermediate Code | <- | Intermediate Code |
| | | | | Generator | | Generator |
+-------------------+ +-------------------+ +-------------------+ +-------------------+
```

### 1. Lexical Analysis (Scanning)

This is the first phase of the compiler. The lexical analyzer reads the stream of characters constituting the source program and groups them into meaningful sequences called **lexemes**. For each lexeme, it produces a **token** as output.

- **Token:** A pair consisting of a _token name_ and an optional _attribute value_. The token name is an abstract symbol representing a kind of lexical unit, e.g., identifier, keyword, operator.
- **Function:** It removes whitespace, comments, and other non-significant characters. It also enters identifiers (variable names, etc.) into the **symbol table** for later use.
- **Example:** For the statement `position = initial + rate * 60;`, the lexical analyzer might generate the following token stream:
- `<id, 1>` (where `position` is found at symbol table entry 1)
- `<assign_op>`
- `<id, 2>` (`initial`)
- `<add_op>`
- `<id, 3>` (`rate`)
- `<mult_op>`
- `<number, 60>`
- `<semicolon>`

### 2. Syntax Analysis (Parsing)

The syntax analyzer takes the stream of tokens from the lexical analyzer and checks if they form a syntactically correct program according to the **context-free grammar** (CFG) of the source language. It groups tokens together into hierarchical structures, ultimately building a **parse tree**.

- **Function:** It verifies the structure of the program. It detects syntax errors like missing semicolons, mismatched brackets, or incorrect operator placement.
- **Output:** A parse tree or, more commonly, a simplified abstract syntax tree (AST). The AST is a condensed representation of the parse tree that omits nodes for redundant syntax like parentheses.
- **Example:** For the tokens generated above, the syntax analyzer would recognize the structure as an assignment statement where the right-hand side is an expression following the rules of arithmetic operator precedence (`*` before `+`).

### 3. Semantic Analysis

This phase uses the syntax tree and information from the symbol table to check the source program for **semantic consistency** with the language definition. It performs tasks that require a deeper understanding than just syntax.

- **Function:**
- **Type Checking:** Ensures operands of an operator are compatible (e.g., not adding an integer to an array).
- **Scope Resolution:** Checks that variables are declared before use and that scoping rules are followed.
- **Output:** An annotated syntax tree with type information. It also updates the symbol table with type and other relevant attributes.

### 4. Intermediate Code Generation

After semantic analysis, the compiler often generates an explicit intermediate representation (IR) of the source program. This representation is abstract and sits between the high-level source and the low-level target machine code.

- **Purpose:** It allows the compiler to be more portable. The front end can be designed for a specific source language, and the back end can be designed for a specific target machine. They are connected via the common IR.
- **Common Forms:** Three-address code (TAC) is a popular IR. Each TAC instruction has at most one operator and three operands (usually names or constants).
- **Example:** The statement `position = initial + rate * 60;` might be translated to the following TAC sequence:

```
t1 = inttofloat(60) // Convert integer 60 to float
t2 = id3 * t1 // rate * 60.0
t3 = id2 + t2 // initial + t2
id1 = t3 // position = t3
```

### 5. Code Optimization

The optional code optimization phase attempts to improve the intermediate code so that the resulting target program runs faster and/or uses less memory. The goal is to produce better code without changing the program's meaning.

- **Techniques:** These include removing redundant computations, simplifying algebraic expressions, constant folding (e.g., calculating `2 * 3.14` at compile time instead of runtime), and loop optimizations.
- **Example:** The above TAC code can be optimized. Since `60` is a constant, the conversion and multiplication can be done at compile time.

```
t1 = id3 * 60.0 // rate * 60.0 (compile-time constant)
t2 = id2 + t1 // initial + t1
id1 = t2 // position = t2
```

### 6. Code Generation

This is the final phase of the back end. The code generator takes the optimized intermediate code and maps it onto the instruction set of the target machine. It involves crucial decisions like memory management (which variables go in registers vs. memory) and instruction selection.

- **Output:** The target machine code or assembly code.
- **Example (Hypothetical Assembly):**

```
LOAD R1, id3 ; Load 'rate' into register R1
MUL R1, R1, #60.0 ; Multiply R1 by 60.0
LOAD R2, id2 ; Load 'initial' into register R2
ADD R2, R2, R1 ; Add R1 to R2
STORE R2, id1 ; Store result into 'position'
```

### 7. Symbol Table Management

The **symbol table** is a data structure maintained throughout the compilation process. It stores information about various entities (identifiers) in the source program, such as:

- Name
- Type
- Scope (where it's valid)
- Memory location (for code generation)
  It is accessed and updated by almost all phases of the compiler. Efficient symbol table organization is crucial for compiler performance.

### 8. Error Handling

Every phase of the compiler must be equipped to handle errors. A good compiler should not crash upon finding an error; instead, it should attempt to **recover** and continue processing to find as many errors as possible in a single run.

- **Lexical:** Illegal character.
- **Syntax:** Missing token, incorrect structure.
- **Semantic:** Type mismatch, undeclared variable.

## The Two-Part Structure: Front End vs. Back End

The phases are commonly grouped into two parts:
| Aspect | Front End (Analysis) | Back End (Synthesis) |
| :--- | :--- | :--- |
| **Phases** | Lexical Analysis, Syntax Analysis, Semantic Analysis, Intermediate Code Gen | Code Optimization, Code Generation |
| **Input** | Source Program | Intermediate Representation |
| **Output** | Intermediate Representation + Symbol Table | Target Machine Code |
| **Dependency** | **Source Language** dependent | **Target Machine** dependent |
| **Purpose** | Understand the meaning and structure of the source code. | Translate the understood meaning into efficient machine code. |

This separation is a key design principle that promotes **portability**. A compiler for a new machine architecture only requires a new back end, and a compiler for a new language only requires a new front end, both working with the same IR.

## Exam Tips

1. **Memorize the Phases:** Be able to list all phases of a compiler in the correct order and state the primary function of each. This is a very common question.
2. **Understand the Input/Output:** For any given phase, you should know what its input is and what it produces as output (e.g., Lexical Analyzer: Input=characters, Output=tokens).
3. **Front End vs. Back End:** Clearly distinguish which phases belong to the front end and which to the back end, and understand the significance of this division.
4. **Symbol Table & Error Handling:** Remember that the symbol table is a central repository of information used across phases, and that error handling is a continuous activity.
5. **Trace an Example:** Be prepared to trace a simple statement (like `a = b + c * 10;`) through each phase, describing the output. This demonstrates a deep understanding of the process.
