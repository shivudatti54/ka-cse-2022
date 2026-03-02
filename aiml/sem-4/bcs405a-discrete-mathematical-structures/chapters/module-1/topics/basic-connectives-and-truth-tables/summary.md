# **Basic Connectives and Truth Tables**

### Definitions

- **Connective**: A logical operator that combines two propositions to form a new proposition.
- **Proposition**: A statement that can be either true (T) or false (F).

### Basic Connectives

- **Conjunction (AND)**: ∧
  - Definition: p ∧ q is true if and only if both p and q are true.
  - Formula: p ∧ q ≡ (p ∨ q) ∧ (¬p ∨ ¬q)
- **Disjunction (OR)**: ∨
  - Definition: p ∨ q is true if and only if at least one of p and q is true.
  - Formula: p ∨ q ≡ (¬p ∧ ¬q)
- **Negation (NOT)**: ¬
  - Definition: ¬p is true if and only if p is false.
  - Formula: ¬p ≡ (p → F)
- **Implication (IF-THEN)**: →
  - Definition: p → q is true if and only if either p is false or q is true.
  - Formula: p → q ≡ (¬p ∨ q)

### Truth Tables

| Connective | p   | q   | p ∧ q | p ∨ q | ¬p  | ¬q  | p → q |
| ---------- | --- | --- | ----- | ----- | --- | --- | ----- |
| ∧          | T   | T   | T     | T     | F   | F   | T     |
| ∧          | T   | F   | F     | T     | F   | T   | F     |
| ∧          | F   | T   | F     | T     | T   | F   | T     |
| ∧          | F   | F   | F     | F     | T   | T   | T     |
| ∨          | T   | T   | T     | T     | F   | F   | T     |
| ∨          | T   | F   | T     | T     | F   | T   | T     |
| ∨          | F   | T   | T     | T     | T   | F   | T     |
| ∨          | F   | F   | F     | F     | T   | T   | T     |
| ¬          | T   | T   | F     | F     | F   | F   | F     |
| ¬          | T   | F   | F     | T     | F   | T   | T     |
| ¬          | F   | T   | F     | T     | T   | F   | T     |
| ¬          | F   | F   | F     | F     | T   | T   | T     |

### Important Formulas and Theorems

- De Morgan's Laws:
  - ¬(p ∧ q) ≡ (¬p ∨ ¬q)
  - ¬(p ∨ q) ≡ (¬p ∧ ¬q)
- Distributive Law:
  - p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
  - p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
