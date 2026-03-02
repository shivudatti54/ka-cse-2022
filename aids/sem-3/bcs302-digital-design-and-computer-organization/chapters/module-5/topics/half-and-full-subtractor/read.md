# Half and Full Subtractor

==========================

## Overview

---

Half and full subtractors are digital circuits used to perform subtraction operations in digital design and computer organization. These circuits are essential for implementing arithmetic logic units (ALUs) and arithmetic circuits in digital computers.

## Half Subtractor

---

A half subtractor is a digital circuit that subtracts a single bit from a bit. It produces a result of 0 and 1, depending on the difference between the two input bits.

### Half Subtractor Truth Table

| Input 1 | Input 2 | Output |
| ------- | ------- | ------ |
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |

### Half Subtractor Circuit

A half subtractor circuit consists of two inverters and an XOR gate.

1.  Inverter 1: Inverts the second input bit.
2.  XOR gate: Computes the difference between the two input bits.

### Example

Suppose we want to subtract 1 from 0 using a half subtractor.

- Input 1: 0
- Input 2: 1
- Output: 1 (because 0 - 1 = -1, which is equivalent to 1 in binary)

## Full Subtractor

---

A full subtractor is a digital circuit that subtracts two bits and produces a result of 0, 1, or 2 bits.

### Full Subtractor Truth Table

| Input 1 | Input 2 | Input 3 | Output |
| ------- | ------- | ------- | ------ |
| 0       | 0       | 0       | 0      |
| 0       | 0       | 1       | 0      |
| 0       | 1       | 0       | 1      |
| 0       | 1       | 1       | 0      |
| 1       | 0       | 0       | 1      |
| 1       | 0       | 1       | 0      |
| 1       | 1       | 0       | 0      |
| 1       | 1       | 1       | 1      |

### Full Subtractor Circuit

A full subtractor circuit consists of four inverters, two XOR gates, and an OR gate.

1.  Inverter 1: Inverts the first input bit.
2.  Inverter 2: Inverts the second input bit.
3.  XOR gate 1: Computes the difference between the first and second input bits.
4.  XOR gate 2: Computes the difference between the first input bit and the third input bit.
5.  OR gate: Computes the final result by ORing the outputs of XOR gate 1 and XOR gate 2.

### Example

Suppose we want to subtract 1 from 1 using a full subtractor.

- Input 1: 1
- Input 2: 1
- Input 3: 0
- Output: 0 (because 1 - 1 = 0)

## Comparison of Half and Full Subtractors

---

|                  | Half Subtractor              | Full Subtractor                                       |
| ---------------- | ---------------------------- | ----------------------------------------------------- |
| **Inputs**       | 2                            | 3                                                     |
| **Outputs**      | 1 bit                        | 0, 1, or 2 bits                                       |
| **Complexity**   | Low                          | High                                                  |
| **Applications** | Simple arithmetic operations | Arithmetic logic units (ALUs) and arithmetic circuits |

## Key Concepts

---

- Half and full subtractors are digital circuits used to perform subtraction operations.
- Half subtractor produces a result of 0 and 1, depending on the difference between the two input bits.
- Full subtractor produces a result of 0, 1, or 2 bits, depending on the difference between the three input bits.
- Half and full subtractors are essential for implementing arithmetic logic units (ALUs) and arithmetic circuits in digital computers.

## Practice Problems

---

1.  Design a half subtractor circuit using logic gates.
2.  Design a full subtractor circuit using logic gates.
3.  Implement a half subtractor and full subtractor using a digital computer.

## References

---

- "Digital Logic and Computer Organization" by John L. Hennessy and David A. Patterson.
- "Computer Organization and Design" by David A. Patterson and John L. Hennessy.
- "Digital Design and Computer Organization" by Umar S. Qureshi and Sheikh M. Shamim.
