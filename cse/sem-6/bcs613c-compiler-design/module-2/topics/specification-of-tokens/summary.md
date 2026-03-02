# Specification of Tokens

## Overview

Token specification provides formal mathematical descriptions of token patterns using regular expressions. These specifications enable systematic construction of lexical analyzers either manually or through automated tools like Lex.

## Key Points

- **Regular Expression Operations**: Concatenation (ab), alternation (a|b), Kleene closure (a\*), positive closure (a+), optional (a?)
- **Common Patterns**: Identifier = [a-zA-Z][a-zA-Z0-9]\*, Integer = [0-9]+, Float = [0-9]+\.[0-9]+
- **Extended Notations**: Character classes [abc], ranges [a-z], complement [^0-9]
- **Lex Tool Structure**: Three sections - declarations, rules (regex + action), auxiliary code
- **Ambiguity Resolution**: Longest match principle, rule priority (earlier rules win)
- **Error Handling**: Skip illegal characters, report with line numbers, attempt recovery

## Important Concepts

- Regular expressions define token patterns precisely
- Transition diagrams visualize finite automata
- Lex automates scanner generation from specifications
- FIRST sets help determine which production to apply

## Notes

- Practice writing regular expressions for identifiers, numbers, and strings
- Understand longest match principle with example "intvalue" vs "int" + "value"
- Remember Lex file structure: definitions %% rules %% user code
