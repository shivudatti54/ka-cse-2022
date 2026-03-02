# Chomsky Hierarchy and Grammars - Summary

## Key Definitions and Concepts

- **Formal Grammar**: A mathematical model consisting of (N, Σ, P, S) where N is non-terminals, Σ is terminals, P is production rules, and S is the start symbol.

- **Chomsky Hierarchy**: A four-level classification of formal grammars based on restrictions on production rules:
  - Type 0 (Unrestricted): No restrictions except left side contains at least one non-terminal
  - Type 1 (Context-Sensitive): |α| ≤ |β| for all productions
  - Type 2 (Context-Free): Single non-terminal on left side (A → α)
  - Type 3 (Regular): A → aB or A → a (right-linear)

## Important Formulas and Theorems

- **Grammar-Automata Correspondence**:
  - Type 0 ↔ Turing Machine
  - Type 1 ↔ Linear Bounded Automaton
  - Type 2 ↔ Pushdown Automata
  - Type 3 ↔ Finite Automata

- **Containment**: Type 3 ⊂ Type 2 ⊂ Type 1 ⊂ Type 0

- **Chomsky Normal Form**: A → BC or A → a (for CFGs)

- **Greibach Normal Form**: A → aα (for CFGs)

## Key Points

- The Chomsky Hierarchy was proposed by Noam Chomsky in 1956 as a classification system for formal grammars.

- Each increase in grammar type corresponds to increased computational power in the equivalent automaton.

- Context-free grammars (Type 2) are most important for programming languages and natural language processing.

- Regular grammars (Type 3) generate the smallest language class but have the most efficient recognition algorithms.

- Type 0 grammars can generate all recursively enumerable languages.

- The membership problem is decidable for Types 1-3 but undecidable for Type 0.

- Closure properties: Regular and context-free languages are closed under union, concatenation, and Kleene star.

## Common Mistakes to Avoid

1. Confusing left-linear and right-linear regular grammars – they generate the same language class but have different production forms.

2. Thinking context-sensitive grammars always require context – the length constraint (|α| ≤ |β|) is the key defining property.

3. Assuming all programming languages are context-free – modern languages often require context-sensitive features.

4. Forgetting that the empty string (ε) cannot be a terminal but can be generated via productions.

5. Mixing up the direction of the inclusion relationship in the hierarchy.

## Revision Tips

1. Create a comparison table listing each grammar type, its production rule restrictions, equivalent automaton, and example language.

2. Practice constructing grammars for various languages at each level of the hierarchy.

3. Draw derivation trees for context-free grammars to visualize string generation.

4. Solve previous years' DU exam questions on this topic to understand the exam pattern.

5. Focus on understanding why certain language properties require certain grammar types – this conceptual clarity helps in problem-solving.