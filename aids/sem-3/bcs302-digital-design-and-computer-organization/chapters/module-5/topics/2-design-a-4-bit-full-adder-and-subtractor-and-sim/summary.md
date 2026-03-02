# **2 Design a 4 bit full adder and subtractor and simulate the same using basic gates**

### Overview

---

- Design a 4-bit full adder and subtractor using basic gates
- Simulate the design using truth tables and K-map
- Understand the digital circuit design and basic gates

### Key Points

---

#### Full Adder

---

- Definition: A two-bit full adder is a digital circuit that adds two binary numbers and produces a sum and carry-out
- Formula: `A + B = sum, A \* B = carry-out`
- Four-bit full adder:
  - Inputs: A, B, Cin (carry-in)
  - Outputs: sum, sum2, carry-out
  - Gates used: AND, OR, NOT, XOR

#### Subtractor

---

- Definition: A two-bit subtractor is a digital circuit that subtracts two binary numbers and produces a difference and borrow-out
- Formula: `A - B = difference, A \* (B + 1) = borrow-out`
- Four-bit subtractor:
  - Inputs: A, B, Cin (carry-in)
  - Outputs: difference, difference2, borrow-out
  - Gates used: AND, OR, NOT, XOR

#### Basic Gates

---

- NOT gate: `NOT A = A'`
- AND gate: `A \* B = AB`
- OR gate: `A + B = A \* B + A \* B' = AB + A'B`
- XOR gate: `A \^ B = (A + B) \* (A \* B') = AB + A'B`

### Important Formulas and Theorems

---

- Karnaugh map (K-map) for simplifying digital circuits
- Boolean algebra for logical operations

### Revision Tips

---

- Understand the truth tables and K-map for simulating digital circuits
- Learn the digital circuit design principles and basic gates
- Practice designing digital circuits using basic gates and truth tables
