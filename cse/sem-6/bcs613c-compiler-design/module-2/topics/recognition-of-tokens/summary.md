# Recognition of Tokens

## Overview

Token recognition is the fundamental process where the lexical analyzer scans source code character-by-character, identifying patterns that form valid tokens. This process uses finite automata for efficient, systematic pattern matching.

## Key Points

- **Recognition Process**: Reading input, identifying patterns, classifying into token types, producing token stream
- **LR(0) Items**: Production with dot (•) showing how much has been seen (e.g., A → α•Xβ)
- **Closure Operation**: Expands item sets by adding productions for non-terminals after the dot
- **Goto Operation**: Defines state transitions when moving dot across a symbol
- **DFA Simulation**: Most efficient approach with one state transition per input character
- **Error Recovery**: Panic mode (skip to synchronizing token), character deletion/insertion/replacement

## Important Concepts

- Transition diagrams represent finite automata visually
- Double buffer scheme with lexemebegin and forward pointers
- Lookahead and retraction for operators like >= vs >
- Lex tool automates DFA-based scanner generation

## Notes

- Practice drawing transition diagrams for common tokens
- Trace lexer steps for input like "sum=42+val;" showing pointer movements
- Understand NFA→DFA conversion pipeline thoroughly
