# Half Adder & Full Adder — Quick Revision Summary

## Introduction

Adders are fundamental combinational circuits in digital electronics, forming the building block for arithmetic logic units (ALUs) in computer processors. They perform binary addition of two bits, with half adders handling single-bit addition and full adders managing multi-bit addition with carry propagation. These circuits are essential for understanding arithmetic operations in computer system architecture.

---

## Half Adder

A **half adder** adds two single-bit binary numbers (A and B) and produces a **Sum (S)** and **Carry (C)** output.

- **Inputs:** A, B (1-bit each)
- **Outputs:** Sum, Carry
- **Logic Gates:** One XOR gate (for Sum) + one AND gate (for Carry)
- **Truth Table:**
  - 0 + 0 → S=0, C=0
  - 0 + 1 → S=1, C=0
  - 1 + 0 → S=1, C=0
  - 1 + 1 → S=0, C=1
- **Boolean Expressions:**
  - Sum = A ⊕ B
  - Carry = A · B
- **Limitation:** Cannot accept carry input from previous stage

---

## Full Adder

A **full adder** adds three input bits: two significant bits (A, B) and an incoming carry (Cin), producing **Sum (S)** and **Carry_out (Cout)**.

- **Inputs:** A, B, Cin (1-bit each)
- **Outputs:** Sum, Carry_out
- **Logic Gates:** Two XOR + Two AND + One OR gate (or alternative implementations)
- **Truth Table:** 8 combinations (000 to 111)
- **Boolean Expressions:**
  - Sum = A ⊕ B ⊕ Cin
  - Carry_out = (A · B) + (Cin · (A ⊕ B))
- **Advantage:** Can be cascaded for multi-bit addition

---

## Half Adder vs Full Adder

| Feature | Half Adder | Full Adder |
|---------|-----------|-----------|
| Inputs | 2 (A, B) | 3 (A, B, Cin) |
| Outputs | Sum, Carry | Sum, Carry_out |
| Carry Input | Not supported | Supported |
| Implementation | Simple (XOR + AND) | Complex |
| Application | Basic circuits | Multi-bit addition |

---

## Implementation & Cascading

- **Ripple Carry Adder:** Created by connecting multiple full adders in series; each full adder's Cout becomes the next stage's Cin
- **Half adders** are used only for the least significant bit when cascading
- **Propagation delay** is a key concern in ripple carry adders (addressed by carry lookahead adders in advanced designs)

---

## Delhi University Syllabus Alignment

*(As per BSc (Hons) Computer Science, NEP 2024 UGCF – Computer System Architecture)*

- Understanding binary addition fundamentals
- Logic gate implementation of adders
- Circuit design and optimization
- Application in ALU design and processor architecture

---

## Conclusion

Half adders and full adders are essential building blocks for arithmetic operations in digital computers. While the half adder performs basic 2-bit addition, the full adder enables multi-bit addition through carry propagation. Mastery of these circuits is crucial for understanding processor design and digital system architecture, forming the foundation for more complex arithmetic units in modern computing.