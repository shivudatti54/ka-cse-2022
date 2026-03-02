# Chomsky Normal Form (CNF) - Summary

## Key Definitions and Concepts

- **Chomsky Normal Form**: A context-free grammar where every production is either of the form A → BC (two non-terminals) or A → a (single terminal).

- **Nullable Non-terminal**: A non-terminal N such that N ⇒* ε (derives the empty string).

- **Unit Production**: A production of the form A → B where both A and B are non-terminals.

- **Useless Symbol**: A symbol that either cannot derive any terminal string or cannot be reached from the start symbol.

## Important Formulas and Theorems

- **CNF Conversion Steps**:
  1. Eliminate ε-productions
  2. Eliminate unit productions
  3. Remove useless symbols
  4. Convert to binary form (A → BC)

- **CYK Algorithm**: Requires grammar in CNF, time complexity O(n³ × |G|)

## Key Points

- CNF was developed by Noam Chomsky as part of formal language theory in the 1950s.

- Every context-free grammar without ε-productions can be converted to CNF.

- The order of elimination is crucial: ε-productions first, then unit productions, then binary conversion.

- When eliminating ε-productions, identify all nullable non-terminals and generate new productions by replacing them.

- Unit productions are eliminated using the transitive closure of the unit relation.

- New non-terminals must be introduced when converting productions with more than two symbols.

- CNF is essential for the CYK parsing algorithm and for proving properties like the pumping lemma for CFLs.

## Common Mistakes to Avoid

- Forgetting to add all combinations when eliminating ε-productions (missing productions like A → αβ when both A and B are nullable).

- Not checking for useless symbols before final conversion, leading to incomplete CNF.

- Introducing duplicate productions when eliminating unit productions.

- Confusing CNF with Greibach Normal Form (GNF), where productions are of the form A → aα.

## Revision Tips

- Practice converting at least 5 different grammars to CNF before the exam.

- Remember the two strict conditions: A → BC or A → a (strict binary/terminal form).

- Keep track of the start symbol—if nullable, you may keep S → ε in some definitions.

- Understand that CNF simplifies theoretical proofs but cannot derive ε directly (except via special start symbol rule).