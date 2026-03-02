# Propositional versus First-Order Inference - Summary

## Key Definitions and Concepts

- **Propositional Logic**: A logical system dealing with propositions (true/false statements) using connectives like ∧, ∨, ¬, →. Limited to representing facts without internal structure.

- **First-Order Logic (FOL)**: Extended logic with objects, predicates, variables, and quantifiers (∀, ∃). Can represent general rules about categories of objects.

- **Inference**: The process of deriving new facts from known facts using logical rules.

- **Unification**: Finding substitutions that make two atomic formulas identical; fundamental operation in FOL inference.

- **Resolution**: A complete inference rule for FOL that works by proving contradiction of negated goal.

## Important Formulas and Theorems

- **Modus Ponens**: From P and (P → Q), infer Q

- **Universal Instantiation**: From ∀x P(x), infer P(c) for any constant c

- **Existential Instantiation**: From ∃x P(x), infer P(c) for a new constant c

- **Resolution Rule**: From (A ∨ B) and (¬B ∨ C), infer (A ∨ C)

- **Expressiveness**: ∀x (Human(x) → Mortal(x)) represents "All humans are mortal" in FOL

## Key Points

- Propositional logic requires separate facts for each instance; FOL uses variables and quantifiers for general rules

- FOL can express relationships between objects using predicates with multiple arguments

- Unification must perform occurs check to prevent infinite structures (variable mapping to containing term)

- Resolution in FOL requires converting formulas to clause form (CNF)

- Forward chaining is data-driven; backward chaining is goal-driven

- Horn clauses (at most one positive literal) enable efficient linear-time inference

- Propositional inference is NP-complete; FOL inference is semi-decidable

## Common Mistakes to Avoid

1. Confusing universal (∀) and existential (∃) quantifiers—their instantiations differ significantly

2. Forgetting the occurs check during unification, which can lead to incorrect substitutions

3. Applying propositional inference rules directly to quantified statements without instantiation

4. Neglecting to convert FOL formulas to clause form before applying resolution

5. Assuming propositional logic can represent general rules about object categories

## Revision Tips

1. Practice unification on 3-4 examples until comfortable with the algorithm steps

2. Memorize the conversion process from FOL to clause form for resolution

3. Compare equivalent representations in propositional vs first-order logic for the same domain

4. Review Horn clause examples to understand efficient forward/backward chaining

5. Focus on understanding why FOL is more expressive rather than just memorizing differences
