# Role of the Lexical Analyzer

## Overview

The lexical analyzer serves as the first compiler phase, bridging raw character streams and structured token streams. It operates as a coroutine with the parser, providing tokens on-demand while managing the symbol table and handling lexical errors.

## Key Points

- **Primary Functions**: Reading source code, removing whitespace/comments, tokenization, and symbol table interaction
- **Tokenization**: Groups character sequences into tokens with names and optional attribute values
- **Symbol Table Interaction**: Inserts new identifiers and maintains pointers to existing entries
- **Separation Benefits**: Simplicity (easier parser design), efficiency (specialized buffering), portability (platform isolation)
- **Coroutine Model**: Parser calls getNextToken() on-demand rather than batch processing
- **Error Handling**: Detects ill-formed numbers, unclosed strings, and invalid characters

## Important Concepts

- Token vs lexeme distinction
- Lexemebegin and forward pointers in buffering
- Panic mode and character deletion recovery strategies
- Why finite automata are perfect for regular patterns

## Notes

- Always distinguish token (category) from lexeme (specific string)
- Trace token production for simple statements like "if (x == 42) {"
- Justify separation using simplicity and efficiency arguments
