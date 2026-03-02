# Parsing Techniques — Quick Revision Summary

## Introduction

Parsing is a fundamental concept in Artificial Intelligence and compiler design that involves analyzing a sequence of tokens (words or symbols) to determine its grammatical structure according to a formal grammar. In AI, parsing techniques are essential for natural language processing, knowledge representation, and expert systems. These techniques enable computers to understand and interpret structured input, forming the backbone of language understanding, reasoning, and problem-solving systems.

## Key Concepts

### 1. Fundamentals of Parsing
- **Parser**: A component that takes input tokens and checks whether they conform to the rules of a grammar
- **Grammar**: A formal specification of language syntax (typically Backus-Naur Form or BNF)
- **Derivation**: The process of generating a string from start symbol using production rules
- **Parse Tree**: A hierarchical tree structure representing the syntactic analysis of input

### 2. Classification of Parsing Techniques

**Top-Down Parsing**
- Starts from the start symbol and attempts to derive the input string
- Constructs parse tree from root to leaves
- Examples: Recursive descent parsing, LL(1) parsing
- Uses leftmost derivation

**Bottom-Up Parsing**
- Starts from the input string and works backwards to the start symbol
- Constructs parse tree from leaves to root
- Examples: LR(0), SLR, LALR, and Canonical LR parsers
- Uses reverse of rightmost derivation

### 3. LL(1) Parsing
- **L**eft-to-right scan of input
- **L**eftmost derivation
- **1** token lookahead
- Uses predictive parsing table
- Requires no left recursion in grammar
- Suitable for simple programming language constructs

### 4. LR Parsing
- **L**eft-to-right scan
- **R**ightmost derivation in reverse
- More powerful than LL(1)
- Handles larger class of grammars
- Types: LR(0), SLR(1), LALR(1), Canonical LR(1)

### 5. Recursive Descent Parsing
- Each non-terminal corresponds to a recursive function
- Simple implementation and debugging
- May require backtracking (not efficient)
- Predictive version uses lookahead to select productions

### 6. Parser Generators
- Automated tools that generate parsers from grammar specifications
- Examples: YACC, Bison, ANTLR
- Produce efficient LALR or LL parsers
- Handle complex grammatical structures automatically

### 7. Ambiguity and Error Handling
- **Ambiguous Grammar**: Multiple parse trees possible for same string
- **Error Recovery**: Techniques to continue parsing after detecting errors
- **Panic Mode**: Skip tokens until synchronization point
- **Phrasal Recovery**: Local error correction

## Conclusion

Parsing techniques form a critical component of AI systems, enabling machines to understand structured input and perform syntactic analysis. Understanding the distinction between top-down and bottom-up approaches, along with practical parser generators, equips students to build language processors and AI applications that require syntax understanding. Mastery of these techniques is essential for compiler construction and natural language processing applications in AI.

---
*Based on Delhi University NEP 2024 UGCF BSc (Hons) Computer Science AI Syllabus*