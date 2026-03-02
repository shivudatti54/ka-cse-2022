# Propositional Logic and Predicate Logic - Summary

## Key Definitions and Concepts

- **Proposition**: A declarative statement that is either true or false
- **Logical Connectives**: Negation (¬), Conjunction (∧), Disjunction (∨), Implication (→), Biconditional (↔)
- **Predicate**: A statement with variables that becomes a proposition when variables are assigned values
- **Quantifiers**: Universal (∀) - "for all", Existential (∃) - "there exists"
- **Tautology**: Always true compound proposition
- **Contradiction**: Always false compound proposition
- **Contingency**: Neither tautology nor contradiction

## Important Formulas and Theorems

- Implication equivalence: P → Q ≡ ¬P ∨ Q
- De Morgan's Laws: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q; ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
- Modus Ponens: (P → Q), P ⊢ Q
- Modus Tollens: (P → Q), ¬Q ⊢ ¬P
- Translation rules: "Every" → ∀ with → ; "Some" → ∃ with ∧

## Key Points

- Implication P → Q is false only when P is true and Q is false
- For n propositions, truth table has 2^n rows
- Universal quantifier with implication: ∀x (S(x) → P(x))
- Existential quantifier with conjunction: ∃x (S(x) ∧ P(x))
- Order of quantifiers matters: ∀x∃y P(x,y) ≠ ∃y∀x P(x,y) in general
- Logical equivalences help simplify complex expressions
- Rules of inference form the basis for automated reasoning

## Common Mistakes to Avoid

1. Treating implication as equivalence—P → Q ≠ P ↔ Q
2. Confusing conjunction with disjunction in translations
3. Forgetting that quantifier scope affects variable binding
4. Applying De Morgan's laws incorrectly (not distributing negation to both parts)
5. Using ∧ where → is required in universal quantifier statements

## Revision Tips

1. Practice constructing truth tables for at least 5 different compound propositions
2. Memorize the truth table for implication—most questions test this
3. Write 3-5 English sentences and translate them into predicate logic
4. Create a quick reference card with all logical equivalences and rules of inference
5. Solve at least 3 proof problems using modus ponens and modus tollens before the exam
