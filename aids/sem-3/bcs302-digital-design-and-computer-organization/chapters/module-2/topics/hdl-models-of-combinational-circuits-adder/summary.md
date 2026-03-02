# HDL Models of Combinational Circuits – Adder

=============================================

### Overview

---

- An adder is a digital circuit that adds two or more binary numbers.
- HDL (Hardware Description Language) models of adders are used to design and verify digital circuits.

### Key Concepts

---

- **Half Adder**: A 2-bit adder that adds two binary digits (0 or 1).
- **Full Adder**: A 3-bit adder that adds three binary digits (0 or 1).
- **Adder Subtraction**: The process of subtracting one binary number from another.

### HDL Model of Adder

---

- **Half Adder HDL Model**:
  - Inputs: A, B (2 bits)
  - Outputs: S, C (1 bit)
  - Formula: S = A ⊕ B, C = A ∧ B
- **Full Adder HDL Model**:
  - Inputs: A, B, C_in (3 bits)
  - Outputs: S, C_out (1 bit)
  - Formula: S = A ⊕ B ⊕ C_in, C_out = A ∧ B
- **Adder Equation**:
  - Let A, B, C be the input bits
  - Let S, C_out be the output bits
  - C_out = C_in ⊕ (A ⊕ B)

### Important Formulas and Definitions

---

- **XOR (Exclusive OR)**: A ⊕ B = 1 if A ≠ B
- **AND (Conjunction)**: A ∧ B = 1 if A = 1 and B = 1
- **XNOR (Exclusive NOR)**: A ⊕ B = 1 if A = B
- **De Morgan's Law**: ¬(A ∧ B) = ¬A ∨ ¬B, ¬(A ∨ B) = ¬A ∧ ¬B

### Theorems

---

- **Theorem**: For any binary numbers A, B, C, the adder equation holds true.

### Quick Revision Points

---

- Half Adder: 2-bit adder with 2 inputs and 2 outputs
- Full Adder: 3-bit adder with 3 inputs and 2 outputs
- Adder Subtraction: The process of subtracting one binary number from another
- HDL model of Adder: Half Adder and Full Adder models
- Important Formulas and Definitions: XOR, AND, XNOR, De Morgan's Law
