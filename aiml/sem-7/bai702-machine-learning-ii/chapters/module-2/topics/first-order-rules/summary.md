# **First-Order Rules**

### Definition

- A first-order rule is a rule that includes only first-order predicate logic, also known as propositional logic without quantifiers.
- It is a set of conditional statements, called clauses, that define a relation.

### Key Points

- **Clause**: A clause is a disjunction of literals, where a literal is a predicate applied to variables (e.g., P(a)).
- **Literal**: A literal is a predicate applied to a single variable (e.g., P(a)) or its negation (e.g., ~P(a)).
- **Clause Form**: A clause can be in one of the following forms:
  - A single literal (e.g., P(a))
  - A disjunction of two literals (e.g., P(a) ∨ ~Q(b))
  - A disjunction of three literals (e.g., P(a) ∨ ~Q(b) ∨ R(c))
- **Rule**: A rule is a set of clauses that define a relation.

### Important Formulas and Theorems

- **Resolution**: A resolution rule that unifies two clauses and generates a new clause.
  - If C1 = P1(a) ∨ ... ∧ Pn(a) and C2 = ~Q(b) ∨ ... ∧ R(c) and C1 and C2 have a common variable, then C3 = C1 ∨ C2.
- **Universal Closure**: A rule that adds all variables to the head of a clause.
  - If C = P(a) ∨ ... ∨ P(b), then ∃x (C' = P(x) ∨ ... ∨ P(b)).

### Applications

- **Rule-Based Systems**: First-order rules are used in expert systems to define knowledge representations and reasoning processes.
- **Machine Learning**: First-order rules are used in decision trees, decision tables, and rule-based classification algorithms.

### Important Concepts

- **First-Order Logic**: A formal system that extends propositional logic with quantifiers.
- **Predicate Logic**: A formal system that extends first-order logic with predicates and variables.
- **Resolution Theorem**: A theorem that states that resolution is a complete and sound algorithm for inference in first-order logic.
