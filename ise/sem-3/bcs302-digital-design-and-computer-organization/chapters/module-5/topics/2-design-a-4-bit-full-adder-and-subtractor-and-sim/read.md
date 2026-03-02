# **Digital Design and Computer Organization**

## **Module 8: 4 Bit Full Adder and Subtraction**

### Introduction

In this topic, we will design and simulate a 4-bit full adder and subtractor using basic gates. A full adder is a digital circuit that adds three bits of data and a carry-in bit, while a subtractor is a digital circuit that subtracts two bits of data and a borrow-in bit.

### Full Adder

A full adder is a digital circuit that adds three bits of data (A, B, and C) and a carry-in bit (Ci). The output of the full adder is represented by the bits S, C, and C_out.

**How it Works**

- The full adder consists of four basic gates: AND, OR, NOT, and XOR.
- The inputs to the full adder are:
  - A, B, and C (bits to be added)
  - Ci (carry-in bit)
- The output of the full adder is:
  - S (sum bit)
  - C (carry bit)
  - C_out (carry-out bit)

### Full Adder Logic

Here is the logic for the full adder:

- S = A ⊕ B ⊕ Ci (XOR operation between A and B, and Ci)
- C = A ∧ B ∧ Ci (AND operation between A, B, and Ci)
- C_out = S ∧ A ∧ B (AND operation between S, A, and B)

### Subtractor

A subtractor is a digital circuit that subtracts two bits of data (A and B) and a borrow-in bit (Bi). The output of the subtractor is represented by the bits S, B, and B_out.

**How it Works**

- The subtractor consists of four basic gates: AND, OR, NOT, and XOR.
- The inputs to the subtractor are:
  - A, B, and Bi (bits to be subtracted)
- The output of the subtractor is:
  - S (difference bit)
  - B (borrow bit)
  - B_out (borrow-out bit)

### Subtractor Logic

Here is the logic for the subtractor:

- S = (A ⊕ B) ∧ Bi (XOR operation between A and B, and Bi)
- B = A ∧ B ∧ ¬Bi (AND operation between A, B, and NOT Bi)
- B_out = S ∧ A ∧ B (AND operation between S, A, and B)

### Simulation using Basic Gates

We can simulate the full adder and subtractor using basic gates (AND, OR, NOT, and XOR) using a truth table or a KMAP (Karnaugh Map) method.

Here is the truth table for the full adder:

| A   | B   | C   | Ci  | S   | C   | C_out |
| --- | --- | --- | --- | --- | --- | ----- |
| 0   | 0   | 0   | 0   | 0   | 0   | 0     |
| 0   | 0   | 0   | 1   | 0   | 0   | 0     |
| 0   | 0   | 1   | 0   | 0   | 0   | 0     |
| 0   | 0   | 1   | 1   | 1   | 1   | 0     |
| 0   | 1   | 0   | 0   | 1   | 0   | 0     |
| 0   | 1   | 0   | 1   | 1   | 0   | 0     |
| 0   | 1   | 1   | 0   | 1   | 0   | 0     |
| 0   | 1   | 1   | 1   | 0   | 0   | 0     |
| 1   | 0   | 0   | 0   | 1   | 0   | 0     |
| 1   | 0   | 0   | 1   | 1   | 0   | 1     |
| 1   | 0   | 1   | 0   | 0   | 1   | 0     |
| 1   | 0   | 1   | 1   | 1   | 1   | 1     |
| 1   | 1   | 0   | 0   | 0   | 1   | 0     |
| 1   | 1   | 0   | 1   | 1   | 1   | 1     |
| 1   | 1   | 1   | 0   | 0   | 1   | 0     |
| 1   | 1   | 1   | 1   | 1   | 1   | 1     |

And here is the truth table for the subtractor:

| A   | B   | Bi  | S   | B   | B_out |
| --- | --- | --- | --- | --- | ----- |
| 0   | 0   | 0   | 0   | 0   | 0     |
| 0   | 0   | 1   | 1   | 0   | 0     |
| 0   | 1   | 0   | 1   | 1   | 0     |
| 0   | 1   | 1   | 0   | 1   | 0     |
| 1   | 0   | 0   | 1   | 0   | 0     |
| 1   | 0   | 1   | 0   | 1   | 1     |
| 1   | 1   | 0   | 0   | 0   | 0     |
| 1   | 1   | 1   | 0   | 0   | 0     |

### Conclusion

In this topic, we designed and simulated a 4-bit full adder and subtractor using basic gates. We covered the concepts of how these circuits work, their logic, and how to simulate them using truth tables and KMAP methods. This knowledge is essential for understanding digital design and computer organization.
