# HDL Models of Combinational Circuits – Adder

### Digital Design and Computer Organization

#### Overview

- An adder is a combinational digital circuit that adds two or more binary numbers.
- It is a fundamental building block in digital systems.

#### Key Concepts

- **Half Adder**
  - A simple adder that adds two binary digits (0 or 1).
  - Formula: A = X ⊕ Y, B = X ∧ Y
- **Full Adder**
  - An adder that adds three binary digits (0 or 1).
  - Formula: A = (X ⊕ Y) ⊕ Z, B = X ∧ Y, C = X ∧ (Y ⊕ Z)
- **Carry-In and Carry-Out**
  - Carry-In (CI): input from a previous adder.
  - Carry-Out (CO): output of a previous adder.

#### Theorems

- **De Morgan's Law**
  - A ⊕ B = A ∧ ¬B ∨ ¬A ∧ B
  - A ∧ B = ¬(A ⊕ B)

#### Important Formulas

- **Adder Formula**
  - A = (X ⊕ Y) ⊕ Z
  - B = X ∧ Y
  - C = X ∧ (Y ⊕ Z)

#### HDL Models

- **Verilog**
  - Example: `always @(*) begin ... end`
- **VHDL**
  - Example: `always @(posedge clock) begin ... end`

#### Revision Tips

- Review half and full adder formulas and their applications.
- Practice designing adders using HDL models.
- Focus on De Morgan's Law and carry-in, carry-out concepts.
