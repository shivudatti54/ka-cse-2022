# FIRST and FOLLOW Sets

## Overview

FIRST and FOLLOW sets are fundamental tools for constructing LL(1) parsers. FIRST determines which terminals can begin derivations, while FOLLOW identifies terminals that can appear after non-terminals, enabling predictive parsing decisions.

## Key Points

- **FIRST(α)**: Terminals beginning strings derived from α; includes ε if α can derive empty string
- **FIRST Rules**: For terminal X, FIRST(X)={X}; for X→Y₁Y₂...Yₖ, propagate through nullable symbols
- **FOLLOW(A)**: Terminals appearing immediately after non-terminal A in sentential forms
- **FOLLOW Rules**: FOLLOW(S)={$}; for A→αBβ, add FIRST(β)-{ε}; if β nullable, add FOLLOW(A)
- **LL(1) Table Construction**: For A→α, populate M[A,a] using FIRST(α) and FOLLOW(A) for ε-productions
- **LL(1) Conditions**: FIRST sets of alternative productions must be disjoint; proper ε handling required

## Important Concepts

- Iterative fixed-point algorithm for computation
- Dependency on ε-derivation capability
- LL(1) grammar verification using FIRST/FOLLOW disjointness
- Parsing table entries populated systematically

## Notes

- Always detect which non-terminals can derive ε first
- Follow rules systematically without skipping steps
- Check for left recursion before computing FIRST sets
- Remember: FOLLOW never contains ε, always has $ for start symbol
