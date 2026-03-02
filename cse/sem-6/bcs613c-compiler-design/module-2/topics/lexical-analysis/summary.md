# Lexical Analysis

## Overview

Lexical analysis is the first phase of compilation that transforms a character stream into a token stream. The lexical analyzer (scanner) groups characters into meaningful lexemes and produces tokens for the parser while removing whitespace and comments.

## Key Points

- **Token**: Pair consisting of token name and attribute value (e.g., <id, pointer to symbol table>)
- **Pattern**: Description of token form using regular expressions
- **Lexeme**: Actual character sequence matching a token pattern
- **Finite Automata**: Recognition engine using DFA (efficient) or NFA (easier to construct)
- **Input Buffering**: Two-buffer scheme for efficient character reading from disk
- **Tool Support**: Lex/Flex automate scanner construction from regular expressions

## Important Concepts

- Regular expressions specify token patterns
- Thompson's construction: regex → NFA
- Subset construction: NFA → DFA
- DFA minimization for optimal performance
- Panic mode error recovery

## Notes

- Understand the conversion pipeline: regex → NFA → DFA → minimized DFA
- Practice drawing transition diagrams for identifiers, integers, and operators
- Remember why separation from parsing improves design, efficiency, and portability
