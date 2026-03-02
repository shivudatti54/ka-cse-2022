# Parse Trees - Summary

## Key Definitions and Concepts

- **Parse Tree**: An ordered, rooted tree representing the syntactic structure of a string according to a grammar. Root is the start symbol, internal nodes are non-terminals, and leaves are terminals.

- **Yield**: The string obtained by reading leaf nodes from left to right; must equal the input string.

- **Ambiguous Grammar**: A grammar that produces more than one parse tree for the same input string.

- **Leftmost Derivation**: Derivation where the leftmost non-terminal is replaced at each step.

- **Rightmost Derivation**: Derivation where the rightmost non-terminal is replaced at each step.

- **Abstract Syntax Tree (AST)**: A simplified parse tree that removes unnecessary nodes, focusing on essential syntactic structure.

## Important Formulas and Theorems

- Every parse tree corresponds to exactly one leftmost derivation and one rightmost derivation.

- A grammar is ambiguous if ∃ w ∈ L(G) such that w has two or more distinct parse trees.

- Relationship: Parse Tree → Leftmost Derivation (reverse traversal from leaves to root).

## Key Points

- Parse trees bridge lexical analysis and semantic analysis in compilation.

- Root = Start Symbol; Internal Nodes = Non-terminals; Leaves = Terminals (tokens).

- Parse trees include all grammar productions; ASTs are simplified representations.

- Ambiguous grammars must be resolved through left-factoring, left-recursion removal, or precedence rules.

- The yield of a parse tree must exactly match the input token sequence.

- Different derivations (leftmost/rightmost) can produce the same parse tree structure.

## Common Mistakes to Avoid

- Confusing parse trees with ASTs - they are not the same; parse trees are more detailed.

- Forgetting that the yield (leaf sequence) must equal the input string.

- Assuming all grammars are unambiguous - many common grammars (especially for expressions) are ambiguous without proper precedence rules.

- Not understanding that ambiguous grammars cannot be used for deterministic parsing.

## Revision Tips

1. Practice constructing parse trees step-by-step from the start symbol for various input strings.

2. Always verify your parse tree by checking if the yield equals the input string.

3. Remember: Leftmost/rightmost derivations differ in order but produce the same parse tree.

4. Focus on understanding the relationship between grammar rules and tree structure - this is crucial for exam success.
