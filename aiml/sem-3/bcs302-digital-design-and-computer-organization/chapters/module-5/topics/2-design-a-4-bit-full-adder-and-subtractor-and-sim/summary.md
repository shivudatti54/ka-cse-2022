# **2 Design a 4 Bit Full Adder and Subtractor and Simulate the Same using Basic Gates**

### Introduction

---

- A full adder is a digital circuit that adds two binary numbers and produces a sum and carry output.
- A full subtractor is a digital circuit that subtracts two binary numbers and produces a difference and borrow output.

### Full Adder

---

### Key Points

- **Truth Table**
  | A | B | C_in | Sum | Carry
  |---|---|-------|------|-------
  | 0 | 0 | 0 | 0 | 0
  | 0 | 0 | 1 | 1 | 0
  | 0 | 1 | 0 | 1 | 0
  | 0 | 1 | 1 | 0 | 1
  | 1 | 0 | 0 | 1 | 0
  | 1 | 0 | 1 | 0 | 1
  | 1 | 1 | 0 | 0 | 1
  | 1 | 1 | 1 | 1 | 1
- **Logic Equation**
  `Sum = A ⊕ B ⊕ C_in`
  `Carry = AB + (A + B)C_in`
- **Basic Gate Implementation**
  - AND gate
  - OR gate
  - XOR gate
  - NOT gate

### Full Subtractor

---

### Key Points

- **Truth Table**
  | A | B | C_in | Minuend | Difference | Borrow
  |---|---|-------|---------|-----------|---------
  | 0 | 0 | 0 | 0 | 0 | 0
  | 0 | 0 | 1 | 0 | 1 | 0
  | 0 | 1 | 0 | 0 | 1 | 0
  | 0 | 1 | 1 | 1 | 0 | 1
  | 1 | 0 | 0 | 1 | 0 | 0
  | 1 | 0 | 1 | 0 | 1 | 0
  | 1 | 1 | 0 | 0 | 1 | 0
  | 1 | 1 | 1 | 1 | 0 | 1
- **Logic Equation**
  `Difference = A ⊕ B ⊕ C_in`
  `Borrow = AB + (A + B + C_in)`
- **Basic Gate Implementation**
  - AND gate
  - OR gate
  - XOR gate
  - NOT gate

### Important Formulas, Definitions, Theorems

---

- **Boolean Algebra**
  - Complement law: A + (A') = 1
  - Idempotent law: A + A = A
  - Distributive law: A(B + C) = AB + AC
- **Digital Circuit Analysis**
  - K-map (Karnaugh Map) for minimization
  - Boolean algebra for simplification
