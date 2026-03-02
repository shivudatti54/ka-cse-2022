# Top-Down Parsing - Summary

## Key Definitions and Concepts

- **Top-Down Parsing**: Parsing technique that builds parse tree from start symbol (root) towards input terminals (leaves)
- **LL(1) Parsing**: Left-to-right scan, Leftmost derivation, 1 symbol lookahead; uses predictive parsing table
- **Left Recursion**: Production of form A → Aα causing infinite recursion; must be eliminated
- **Left Factoring**: Transforming grammar to remove common prefixes for predictive parsing
- **FIRST(α)**: Set of terminals beginning strings derived from α
- **FOLLOW(A)**: Set of terminals that can appear immediately after A in sentential forms

## Important Formulas and Theorems

- **Left Recursion Elimination**: A → Aα|β transforms to A → βA' and A' → αA'|ε
- **Left Factoring**: A → αβ₁|αβ₂ transforms to A → αA' and A' → β₁|β₂
- **FIRST Rules**: Terminal→{terminal}, ε production→add ε, production X→Y₁...Yₖ: include FIRST(Y₁)-{ε}, if ε∈FIRST(Y₁) include FIRST(Y₂)-{ε}, and so on
- **FOLLOW Rules**: Add $ to FOLLOW(S), for A→αBβ add FIRST(β)-{ε} to FOLLOW(B), for A→αB or A→αBβ with ε∈FIRST(β) add FOLLOW(A) to FOLLOW(B)
- **LL(1) Condition**: FIRST sets of alternatives must be disjoint; if ε∈FIRST(β), then FIRST(α) ∩ FOLLOW(A) = ∅

## Key Points

- LL(1) parsers use no backtracking, making them efficient for programming languages
- Recursive descent parsing is a direct implementation of top-down parsing using procedures
- A grammar must be free of left recursion and left-factored for LL(1) parsing
- ε-productions require special handling in FIRST and FOLLOW computations
- Parsing table with multiple entries indicates grammar is not LL(1)
- Predictive parser uses stack, input pointer, and parsing table M[A, a]
- The parsing algorithm: pop terminal match, pop non-terminal and push production RHS reversed

## Common Mistakes to Avoid

- Forgetting to add $ to FOLLOW of start symbol
- Not removing ε from FIRST sets when propagating to next symbol
- Confusing FIRST and FOLLOW sets and their computation rules
- Failing to check LL(1) conditions before constructing parsing table
- Not reversing the production RHS when pushing onto stack

## Revision Tips

1. Practice FIRST and FOLLOW computations on at least 3 different grammars
2. Memorize the transformation rules for left recursion and left factoring
3. Trace through predictive parsing for multiple input strings
4. Focus on understanding why certain grammars are not LL(1)
5. Review previous year questions on top-down parsing for exam pattern
