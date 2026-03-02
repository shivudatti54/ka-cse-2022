# Structure of a Compiler

## Overview

A compiler's structure consists of six major phases organized into front-end (analysis) and back-end (synthesis) components. Each phase transforms the code representation while symbol table and error handling support all phases continuously.

## Key Points

- **Lexical Analysis**: Reads character stream and produces tokens; removes whitespace and comments
- **Syntax Analysis**: Checks grammatical structure using context-free grammars; builds parse tree or AST
- **Semantic Analysis**: Performs type checking, scope resolution, and type coercion; annotates syntax tree
- **Intermediate Code Generation**: Creates machine-independent representation like three-address code
- **Code Optimization**: Improves code efficiency through constant folding, dead code elimination, and loop optimization
- **Code Generation**: Produces target machine code with register allocation and instruction selection
- **Symbol Table**: Central repository storing identifier information (name, type, scope, location)
- **Error Handler**: Detects and recovers from errors at each phase without crashing

## Important Concepts

- Front-end vs back-end separation enables portability
- Each phase has specific input and output formats
- Symbol table accessed by multiple phases
- Parse tree vs Abstract Syntax Tree (AST)

## Notes

- Memorize all six phases in order for exam success
- Be prepared to trace a statement like "a = b + c \* 10" through each phase
- Understand that separation allows new languages (new front-end) or new machines (new back-end)
