# Half and Full Subtractor

=====================================================

## Introduction

---

In digital design and computer organization, subtraction is a crucial operation that is used extensively in various applications. Subtraction can be performed using two types of subtrahends: half subtrahends and full subtrahends. In this study material, we will focus on half and full subtrahends, their definitions, and their applications.

## Definitions

---

### Half Subtractor

A half subtrahend is a 1-bit digital circuit that subtracts one bit from another. It is also known as a "half-subtractor" or "subtractor half". The output of a half subtrahend is a single bit.

### Full Subtractor

A full subtrahend is a 4-bit digital circuit that subtracts one 4-bit number from another. It is also known as a "full-subtractor" or "adder-subtractor". The output of a full subtrahend is a 4-bit number.

## Half Subtractor Circuit

---

### Half Subtractor Circuit Diagram

Here is the circuit diagram of a half subtrahend:

```markdown
+---------------+
| A (Input) |
+---------------+
|
|
v
+---------------+
| B (Input) |
+---------------+
|
|
v
+---------------+
| Carry-Out |
| (CO) |
+---------------+
|
|
v
+---------------+
| Borrow-Out |
| (BO) |
+---------------+
```

### Half Subtractor Truth Table

Here is the truth table for a half subtrahend:
| A | B | CO | BO |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

## Full Subtractor Circuit

---

### Full Subtractor Circuit Diagram

Here is the circuit diagram of a full subtrahend:

```markdown
+---------------+
| A (Input) |
+---------------+
|
|
v
+---------------+
| B (Input) |
+---------------+
|
|
v
+---------------+
| C (Input) |
+---------------+
|
|
v
+---------------+
| Carry-Out |
| (CO) |
+---------------+
|
|
v
+---------------+
| Borrow-Out |
| (BO) |
+---------------+
|
|
v
+---------------+
| Quotient |
| (Q) |
+---------------+
```

### Full Subtractor Truth Table

Here is the truth table for a full subtrahend:
| A | B | C | CO | BO | Q |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 2 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 | 2 |
| 1 | 1 | 1 | 1 | 1 | 3 |

## Applications

---

Half and full subtrahends have numerous applications in digital design and computer organization, including:

- Digital arithmetic circuits
- Computer architecture
- Microprocessors
- Microcontrollers

## Conclusion

---

In conclusion, half and full subtrahends are essential components of digital design and computer organization. They are used extensively in various applications, including digital arithmetic circuits, computer architecture, and microprocessors. Understanding half and full subtrahends is crucial for designing and implementing efficient digital systems.
