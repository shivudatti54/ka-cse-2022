# Introduction to Compiler Design

## Overview

A compiler is a translator that converts high-level programming language code into machine-executable code while performing error detection and optimization. The compilation process is divided into six main phases that work together to transform source code into efficient target code.

## Key Points

- **Compiler Definition**: A translator that converts human-readable source code into machine-executable code while checking for errors and optimizing output
- **Six Phases**: Lexical Analysis, Syntax Analysis, Semantic Analysis, Intermediate Code Generation, Code Optimization, and Code Generation
- **Front End vs Back End**: Analysis phases (front end) are source-language dependent, while synthesis phases (back end) are target-machine dependent
- **Symbol Table**: Data structure that stores information about identifiers (variables, functions) used throughout all compilation phases
- **Error Handling**: Compilers detect lexical, syntax, semantic, and logical errors at different phases
- **Compiler Types**: Single-pass, multi-pass, cross-compiler, and JIT (Just-In-Time) compilers serve different purposes

## Important Concepts

- Tokens, patterns, and lexemes in lexical analysis
- Parse trees and syntax trees in syntax analysis
- Type checking and scope resolution in semantic analysis
- Three-address code and intermediate representations
- Machine-independent and machine-dependent optimizations

## Notes

- Understanding the six phases and their input/output is crucial for exam questions
- Be able to trace a simple statement through all compilation phases
- Focus on distinguishing compiler from interpreter characteristics
