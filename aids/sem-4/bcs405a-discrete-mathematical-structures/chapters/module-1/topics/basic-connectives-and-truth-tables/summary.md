# **Basic Connectives and Truth Tables**

### Definitions and Notations

- **Connective**: A logical operator that combines two or more propositions.
- **Proposition**: A statement that can be true or false.
- **Truth Table**: A table that shows the truth values of a proposition for all possible combinations of its premises.

### Basic Connectives

- **Negation**: NOT (¬)
  - Definition: The opposite of a proposition.
  - Formula: ¬p → p
- **Conjunction**: AND (∧)
  - Definition: Both premises are true.
  - Formula: p ∧ q → (p ∨ q)
- **Disjunction**: OR (∨)
  - Definition: At least one premise is true.
  - Formula: p ∨ q → (¬p ∧ ¬q)
- **Implication**: IF-THEN (→)
  - Definition: If the premise is true, then the conclusion is true.
  - Formula: p → q ≡ ¬p ∨ q
- **Equivalence**: IF AND ONLY IF (≡)
  - Definition: The two propositions have the same truth value.
  - Formula: p ≡ q ≡ p → q

### Truth Tables

- **Truth Table for Conjunction (∧)**:
  - p ∧ q = T if and only if both p and q are T
- **Truth Table for Disjunction (∨)**:
  - p ∨ q = T if and only if at least one of p or q is T
- **Truth Table for Implication (→)**:
  - p → q = F if and only if p is T and q is F
- **Truth Table for Equivalence (≡)**:
  - p ≡ q = F if and only if p and q have different truth values

### Important Theorems

- **De Morgan's Law**: ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q
- **The Law of Excluded Middle**: p ∨ ¬p = T
