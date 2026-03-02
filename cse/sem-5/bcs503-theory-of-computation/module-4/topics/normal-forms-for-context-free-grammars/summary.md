# Normal Forms for Context-Free Grammars - Summary

## Key Definitions and Concepts

- **Chomsky Normal Form (CNF)**: A CFG where all productions are either A → a (single terminal) or A → BC (two non-terminals), with no ε-productions (except possibly S → ε) and no unit productions

- **Greibach Normal Form (GNF)**: A CFG where every production begins with a terminal symbol followed by zero or more non-terminals (A → aα)

- **Nullable Symbol**: A non-terminal that can derive the empty string ε

- **Unit Production**: A production of the form A → B where both are non-terminals

- **Useless Symbol**: A non-terminal that either cannot derive any terminal string or is not reachable from the start symbol

## Important Formulas and Theorems

- **Chomsky's Theorem**: Every CFG without ε-productions can be converted to CNF
- **Greibach's Theorem**: Every CFG can be converted to GNF
- **CNF Conversion Order**: Remove ε-productions → Remove unit productions → Remove useless symbols → Convert to binary form
- **GNF Property**: Productions start with terminal; right-hand side length equals 1 + number of non-terminals

## Key Points

- CNF simplifies parsing algorithms like CYK; requires binary productions
- GNF is essential for top-down parsing and LL(k) parsers
- Always handle start symbol separately when removing ε-productions
- Unit pair elimination requires finding all pairs (A,B) where A derives B through unit productions
- Binary form conversion: Replace A → X₁X₂...Xₙ with A → X₁A₁, A₁ → X₂A₂, ..., Aₙ₋₁ → Xₙ₋₁Xₙ
- CNF productions have either 1 or 2 symbols on RHS
- GNF productions always start with a terminal
- Removing useless symbols is essential for clean normal form conversion

## Common Mistakes to Avoid

- Forgetting to add productions when removing ε-productions (consider all combinations)
- Not removing unit productions before converting to binary form
- Ignoring the start symbol when checking for reachability
- Converting to GNF without first converting to CNF (when using the standard method)
- Not handling the special case S → ε in CNF conversion

## Revision Tips

1. Practice converting at least 3-4 grammars to CNF and GNF manually
2. Remember the order of CNF conversion steps - this is frequently tested
3. Know that CYK parsing requires CNF; LL parsing relates to GNF
4. Draw derivation trees to visualize the conversion process
5. Memorize both definitions clearly: CNF = terminal or two non-terminals, GNF = starts with terminal
