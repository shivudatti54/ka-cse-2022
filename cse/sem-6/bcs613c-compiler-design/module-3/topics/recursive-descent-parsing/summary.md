# Recursive Descent Parsing

## Overview

Recursive descent parsing is a top-down technique using mutually recursive functions, one per non-terminal. Each function examines the lookahead token to decide which production to apply, making recursive calls for non-terminals and matching terminals.

## Key Points

- **Function Structure**: For each non-terminal A, function parseA() reads tokens derivable from A
- **Lookahead Decisions**: Uses current token and FIRST sets to choose productions
- **Terminal Handling**: match() function checks and consumes expected terminals
- **Non-Terminal Handling**: Recursive calls to corresponding parse functions
- **Left Recursion Problem**: Causes infinite loops; must eliminate before implementation
- **Predictive Variant**: Uses FIRST/FOLLOW sets for deterministic choices without backtracking
- **Grammar Requirements**: Must be LL(1) with left-recursion removed and common prefixes factored

## Important Concepts

- Code structure mirrors grammar productions directly
- FIRST sets determine valid production choices
- FOLLOW sets handle epsilon productions
- Left recursion A → Aα transformed to right recursion A → βA'

## Notes

- Practice eliminating left recursion and left factoring
- Trace function call sequences for sample inputs
- Understand why predictive parsing avoids backtracking through lookahead
