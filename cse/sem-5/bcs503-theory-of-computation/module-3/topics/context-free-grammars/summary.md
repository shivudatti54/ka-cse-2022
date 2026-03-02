# Context-Free Grammars - Summary

## Key Definitions and Concepts

- **Context-Free Grammar (CFG):** A 4-tuple G = (V, T, P, S) where V is set of variables (non-terminals), T is set of terminals, P is set of production rules, and S is the start symbol.

- **Terminals:** Basic symbols that cannot be expanded further; form the final strings.

- **Non-terminals (Variables):** Placeholders that can be replaced according to production rules.

- **Derivation:** Sequence of applying productions to derive a terminal string from the start symbol.

- **Parse Tree:** Tree representation showing hierarchical structure of derivation; leaves are terminals.

- **Ambiguous Grammar:** Grammar where at least one string has multiple parse trees/derivations.

## Important Formulas and Theorems

- **CNF Form:** Productions must be A → BC (two variables) or A → a (single terminal), plus S → ε allowed.

- **GNF Form:** Productions must be A → aα where a is terminal and α is string of variables.

- **Simplification Order:** Remove ε-productions → Remove unit productions → Remove useless symbols.

## Key Points

- CFGs can generate languages with nested structures that finite automata cannot handle.

- Leftmost and rightmost derivations represent different parsing strategies (top-down vs bottom-up).

- Ambiguity is undesirable in programming languages; precedence and associativity rules resolve it.

- Every CFL can be converted to CNF and GNF through systematic transformations.

- CNF enables the CYK algorithm for parsing; GNF enables direct recursive descent parsing.

- Useless symbols (non-generating or non-reachable) must be removed for proper normal form conversion.

## Common Mistakes to Avoid

- Confusing terminals with non-terminals; terminals cannot appear on left side of productions.

- Forgetting that ε-productions must be removed before converting to CNF.

- Attempting to eliminate ambiguity without checking if the language is inherently ambiguous.

- Not following the correct order of simplification, leading to incorrect normal forms.

## Revision Tips

- Practice constructing CFGs for common language patterns: anbn, palindromes, matching delimiters.

- Draw parse trees for derivations to visualize the hierarchical structure.

- Memorize the step-by-step procedures for CNF and GNF conversion.

- Solve previous exam questions on CFG construction and simplification.
