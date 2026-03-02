# **Logical Implication – Rules of Inference**

### Definitions and Notations

- **Logical Implication**: A logical statement of the form A → B, read as "A implies B" or "if A then B".
- **Truth Table**: A table used to evaluate the truth values of logical statements.

### Rules of Inference

- **Modus Ponens (MP)**: If A → B and B, then A → B.
  - Formula: (A → B) ∧ B ⊢ A → B
- **Universal Instantiation (UI)**: If A ⊢ B, then ∀x (A(x) ⊢ B(x)).
  - Formula: A ⊢ ∀x B
- **Existential Instantiation (EI)**: If A ⊢ B, then ∃x (A(x) ⊢ B(x)).
  - Formula: A ⊢ ∃x B
- **Modus Tollens (MT)**: If A → B and ¬B, then ¬A.
  - Formula: (A → B) ∧ ¬B ⊢ ¬A
- **Hypothetical Syllogism (HS)**: If A → B and B → C, then A → C.
  - Formula: (A → B) ∧ (B → C) ⊢ (A → C)

### Important Formulas and Theorems

- **De Morgan's Laws**:
  - ¬(A ∧ B) = ¬A ∨ ¬B
  - ¬(A ∨ B) = ¬A ∧ ¬B
- **Distributive Law**:
  - (A ∧ B) ∨ (A ∧ C) = (A ∨ A) ∧ (B ∨ C)
  - (A ∨ B) ∧ (A ∨ C) = (A ∧ A) ∨ (B ∧ C)

### Key Concepts

- **Conclusion**: A logical statement that follows logically from a set of premises.
- **Premises**: Logical statements that are used to support a conclusion.
- **Valid Argument**: An argument that always leads to a valid conclusion, regardless of the truth values of the premises.
