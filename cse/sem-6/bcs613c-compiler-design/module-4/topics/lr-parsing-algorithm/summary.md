# LR Parsing Algorithm

## Overview

The LR parsing algorithm is a table-driven bottom-up technique using a stack and two-part parsing table. It scans input left-to-right, producing rightmost derivations in reverse through shift and reduce operations.

## Key Points

- **Components**: Input buffer with $, stack storing states and symbols, ACTION/GOTO tables
- **Shift Action**: Push input symbol and next state onto stack
- **Reduce Action**: Pop 2×|β| symbols for A→β, push A and GOTO[s',A]
- **Accept Action**: Parsing completes successfully when S' → S• is recognized
- **LR(0) Items**: Track parsing progress with dot marker in productions
- **Closure/Goto Functions**: Build canonical collection of LR(0) item sets forming states
- **Parser Types**: LR(0) (no lookahead), SLR(1) (FOLLOW sets), LALR(1) (merged states), CLR(1) (explicit lookahead)

## Important Concepts

- Shift-reduce conflicts: ambiguity between shifting and reducing
- Reduce-reduce conflicts: multiple possible reductions
- More powerful than LL parsers, handles left-recursive grammars
- LALR(1) used in parser generators like YACC/Bison

## Notes

- Practice tracing stack contents during parsing steps
- Understand difference between LR parser types in power vs table size
- Focus on closure and goto operations for state construction
