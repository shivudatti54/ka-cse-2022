# Quantifiers

### Definitions

- **Quantifier**: A symbol or letter that denotes the scope of a predicate.
- **Universal Quantifier** (∀): For all elements in the domain.
- **Existential Quantifier** (∃): There exists at least one element in the domain.

### Important Formulas and Theorems

- **Predicate Logic**: A formal system for expressing and reasoning with statements that contain variables and predicates.
- **Universal Quantification**:

* ∀x (P(x) → Q(x)) ≡ ∀x P(x) → ∀x Q(x)
* ∀x∈D P(x) ≡ ∀x (x ∈ D → P(x))

- **Existential Quantification**:

* ∃x (P(x) ∧ Q(x)) ≡ P(a) ∧ Q(a) for some a ∈ D
* ∃x∈D P(x) ≡ ∃a ∈ D P(a)

- **Quantifier Negation**:

* ¬∀x P(x) ≡ ∃x ∉ P(x)
* ¬∃x P(x) ≡ ∀x ∉ P(x)

### Important Theorems

- **Liar Paradox**: ∃x (x ≠ x) is true, but ∃x (x = ∃x (x ≠ x)) is false.
- **Barcan Formula**: ∀x P(x) → ∃x ∀x P(x)
- **Burali-Forti Paradox**: ∃x ∀y (y ≠ x) is true, but ∃x ∀x (x ≠ x) is false.

### Quantifier Rules

- **Universal Quantification Rules**:

* ∀x P(x) ∧ Q(x) ≡ ∀x (P(x) ∧ Q(x))
* ∀x P(x) → Q(x) ≡ ∀x (P(x) → Q(x))

- **Existential Quantification Rules**:

* P(x) ∧ ∃x Q(x) ≡ ∃x (P(x) ∧ Q(x))
* P(x) → ∃x Q(x) ≡ ∃x (P(x) → Q(x))

### Quantifier Properties

- **Commutativity**: ∀x P(x) ≡ ∃x P(x)
- **Associativity**: ∀x ∀y ∀z P(x, y, z) ≡ ∃x ∃y ∃z P(x, y, z)
- **Distributivity**: ∀x ∀y P(x, y) ∧ Q(x, y) ≡ ∀x ∀y (P(x, y) ∧ Q(x, y))
