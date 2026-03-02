# Half and Full Subtractor

## Digital Design and Computer Organization

### Key Points

- **Definition**: Half subtractor and full subtractor are digital circuits used to perform subtraction operations.
- **Half Subtractor**:
  - Takes two binary numbers as inputs (A, B) and produces:
    - Result
    - Borrow
  - Formula: `(A, B) = (A ⊕ B, A ∧ B)`
- **Full Subtractor**:
  - Takes three binary numbers as inputs (A, B, P) and produces:
    - Result
    - Carry-out
    - Borrow
  - Formula: `(A, B, P) = (A ⊕ B ⊕ P, A ∧ B ⊕ A ∧ P ⊕ B ∧ P, A ∧ B ∧ ¬P)`
- **Theorem**: The full subtractor can be expressed as a combination of two half subtractors.

### Important Formulas

- Half subtractor: `(A, B) = (A ⊕ B, A ∧ B)`
- Full subtractor: `(A, B, P) = (A ⊕ B ⊕ P, A ∧ B ⊕ A ∧ P ⊕ B ∧ P, A ∧ B ∧ ¬P)`

### Important Definitions

- `⊕`: XOR (Exclusive OR) operation
- `∧`: AND operation
- `¬`: NOT operation
