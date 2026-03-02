# Quantifiers

### Definitions

- **Quantifier**: A logical symbol used to restrict the domain of a predicate or function.
- **Universal Quantifier (∀)**: For all elements in the domain
- **Existential Quantifier (∃)**: There exists at least one element in the domain

### Key Formulas and Theorems

- **Universal Quantification**: ∀x P(x) ⇔ ∀x (P(x) → Bool)
- **Existential Quantification**: ∃x P(x) ⇔ ¬∀x (¬P(x))
- **Quantifier Negation**: ¬∀x P(x) ⇔ ∃x ¬P(x)
- **Quantifier Elimination**:
  - ∀x P(x) → P(a) for some a
  - ∃x P(x) → P(b) for some b
- **Monadic and Poladic Quantifiers**:
  - ∀x P(x) ∧ Q(x) ⇔ ∀x (P(x) ∧ Q(x))
  - ∃x P(x) ∨ Q(x) ⇔ ∃x (P(x) ∨ Q(x))

### Important Concepts

- **Domain**: The set of elements over which a predicate or function is defined.
- **Scope**: The part of the formula where the quantifier applies.
- **Bound Variable**: A variable that is not free in a formula (i.e., its scope is limited).

### Important Theorems

- **Löwenheim-Skolem Theorem**: Every countable model of a first-order theory has a countable model.
- **Compactness Theorem**: A set of first-order formulas has a model if and only if every finite subset of it has a model.

### Quick Revision Tips

- Understand the difference between universal and existential quantification.
- Be able to apply quantifier negation and elimination.
- Familiarize yourself with monadic and poladic quantifiers.
- Know the key formulas and theorems related to quantifiers.
