# Half and Full Subtractor

=====================================================

## Introduction

---

In digital design and computer organization, subtraction is a fundamental operation that is used to find the difference between two binary numbers. This study material covers the concepts of half and full subtractors, which are used to perform subtraction operations in digital circuits.

## Definitions

---

### Half Subtractor

A half subtractor is a digital circuit that performs a subtraction operation between two binary digits (bits). It produces a result and a borrow flag.

### Full Subtractor

A full subtractor is a digital circuit that performs a subtraction operation between three binary digits (bits). It produces a result and three flags: borrow, carry, and result.

## Half Subtractor Circuit

---

The half subtractor circuit consists of two inverters, one AND gate, and two OR gates.

```
  +---------------+
  |               |
  |  Bit A        |
  |  (Input)       |
  +---------------+
           |
           |
           v
  +---------------+
  |  Inverter 1  |
  |  (Not A)     |
  +---------------+
           |
           |
           v
  +---------------+
  |  AND Gate    |
  |  (A and Not A)|
  +---------------+
           |
           |
           v
  +---------------+
  |  Inverter 2  |
  |  (Not B)     |
  +---------------+
           |
           |
           v
  +---------------+
  |  OR Gate     |
  |  (A or Not B) |
  +---------------+
           |
           |
           v
  +---------------+
  |  Output (Result)|
  +---------------+
           |
           |
           v
  +---------------+
  |  Output (Borrow)|
  +---------------+
```

## Half Subtractor Logic

---

The half subtractor logic can be represented using the following truth table:

| A   | B   | Result | Borrow |
| --- | --- | ------ | ------ |
| 0   | 0   | 0      | 0      |
| 0   | 1   | 0      | 1      |
| 1   | 0   | 1      | 0      |
| 1   | 1   | 0      | 1      |

From the truth table, we can derive the following equations:

- `Result = A and Not B`
- `Borrow = A and Not B`

## Full Subtractor Circuit

---

The full subtractor circuit consists of three inverters, one AND gate, three OR gates, and one XOR gate.

```
  +---------------+
  |               |
  |  Bit A        |
  |  (Input)       |
  +---------------+
           |
           |
           v
  +---------------+
  |  Inverter 1  |
  |  (Not A)     |
  +---------------+
           |
           |
           v
  +---------------+
  |  AND Gate    |
  |  (A and Not A)|
  +---------------+
           |
           |
           v
  +---------------+
  |  Inverter 2  |
  |  (Not B)     |
  +---------------+
           |
           |
           v
  +---------------+
  |  OR Gate     |
  |  (A or Not B) |
  +---------------+
           |
           |
           v
  +---------------+
  |  XOR Gate    |
  |  (A and Not C)|
  +---------------+
           |
           |
           v
  +---------------+
  |  OR Gate     |
  |  (Not A and B)|
  +---------------+
           |
           |
           v
  +---------------+
  |  OR Gate     |
  |  (Not A and Not B)|
  +---------------+
           |
           |
           v
  +---------------+
  |  Output (Result)|
  +---------------+
           |
           |
           v
  +---------------+
  |  Output (Borrow)|
  +---------------+
           |
           |
           v
  +---------------+
  |  Output (Carry) |
  +---------------+
```

## Full Subtractor Logic

---

The full subtractor logic can be represented using the following truth table:

| A   | B   | C   | Result | Borrow | Carry |
| --- | --- | --- | ------ | ------ | ----- |
| 0   | 0   | 0   | 0      | 0      | 0     |
| 0   | 0   | 1   | 0      | 0      | 1     |
| 0   | 1   | 0   | 1      | 1      | 0     |
| 0   | 1   | 1   | 0      | 0      | 0     |
| 1   | 0   | 0   | 0      | 0      | 1     |
| 1   | 0   | 1   | 1      | 1      | 1     |
| 1   | 1   | 0   | 0      | 1      | 0     |
| 1   | 1   | 1   | 0      | 0      | 0     |

From the truth table, we can derive the following equations:

- `Result = Not(A and Not B) and Not(A and Not C) and (Not A and B)`
- `Borrow = A and Not B`
- `Carry = (A and Not C) or (Not A and Not B)`

## Conclusion

---

In this study material, we have covered the concepts of half and full subtractors, which are used to perform subtraction operations in digital circuits. We have also derived the logic equations for the half and full subtractors using truth tables. Understanding the concepts and logic of half and full subtractors is essential for designing and implementing digital circuits.

### Key Concepts

- Half subtractor: a digital circuit that performs a subtraction operation between two binary digits (bits)
- Full subtractor: a digital circuit that performs a subtraction operation between three binary digits (bits)
- Truth table: a table used to represent the output of a digital circuit based on the input values
- Logic equations: equations that describe the output of a digital circuit based on the input values
