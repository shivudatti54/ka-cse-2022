# Topic: 2 Design a 4 bit full adder and subtractor and simulate the same using basic gates

=====================================================

## Introduction

---

In this module, we will be learning about digital design and computer organization. We will be designing a 4-bit full adder and subtractor using basic gates. A full adder is a digital circuit that adds two binary numbers along with a carry input and produces a sum and a carry output. A subtractor is a digital circuit that subtracts one binary number from another and produces a borrow output.

## Full Adder

---

A full adder is a digital circuit that adds two binary numbers along with a carry input and produces a sum and a carry output.

### Components of a Full Adder

---

- Two binary inputs (A and B)
- A carry input (Cin)
- A sum output (S)
- A carry output (Cout)

### Truth Table for a Full Adder

---

| A   | B   | Cin | S   | Cout |
| --- | --- | --- | --- | ---- |
| 0   | 0   | 0   | 0   | 0    |
| 0   | 0   | 1   | 0   | 1    |
| 0   | 1   | 0   | 1   | 0    |
| 0   | 1   | 1   | 1   | 1    |
| 1   | 0   | 0   | 1   | 0    |
| 1   | 0   | 1   | 0   | 1    |
| 1   | 1   | 0   | 0   | 1    |
| 1   | 1   | 1   | 1   | 0    |

### Design of a 4-bit Full Adder

---

To design a 4-bit full adder, we can use the following logic equations:

- S = A ⊕ B ⊕ Cin (where ⊕ represents the XOR operation)
- Cout = (A \* B) + (A \* Cin) + (B \* Cin)

Where ⊕ represents the XOR operation, \* represents the AND operation, and + represents the OR operation.

### Example

---

Here is an example of how a 4-bit full adder can be implemented using basic gates:

```
  +-------+       +-------+       +-------+
  |  A    |       |  B    |       |  Cin   |
  +-------+       +-------+       +-------+
           |                       |
           |  XOR                      |
           |                       |
           v                       v
  +-------+       +-------+       +-------+
  |  S    |       |  Cout  |       |  GND  |
  +-------+       +-------+       +-------+
```

In this example, the XOR gates are used to implement the XOR operation, the AND gates are used to implement the AND operation, and the OR gates are used to implement the OR operation.

## Subtractor

---

A subtractor is a digital circuit that subtracts one binary number from another and produces a borrow output.

### Components of a Subtractor

---

- Two binary inputs (A and B)
- A borrow input (Bor)
- A output (Y)

### Truth Table for a Subtractor

---

| A   | B   | Bor | Y   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   |
| 0   | 1   | 0   | 1   |
| 0   | 1   | 1   | 0   |
| 1   | 0   | 0   | 1   |
| 1   | 0   | 1   | 0   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 1   |

### Design of a 4-bit Subtractor

---

To design a 4-bit subtractor, we can use the following logic equations:

- Y = A ⊕ B ⊕ Bor
- Bor = (A \* B) + (A \* Bor) + (B \* Bor)

Where ⊕ represents the XOR operation, \* represents the AND operation, and + represents the OR operation.

### Example

---

Here is an example of how a 4-bit subtractor can be implemented using basic gates:

```
  +-------+       +-------+       +-------+
  |  A    |       |  B    |       |  Bor  |
  +-------+       +-------+       +-------+
           |                       |
           |  XOR                      |
           |                       |
           v                       v
  +-------+       +-------+       +-------+
  |  Y    |       |  GND  |       |  Bor  |
  +-------+       +-------+       +-------+
```

In this example, the XOR gates are used to implement the XOR operation, the AND gates are used to implement the AND operation, and the OR gates are used to implement the OR operation.

## Simulation

---

To simulate the full adder and subtractor, we can use a digital logic simulator. The simulator will allow us to input values for the inputs and outputs and observe the behavior of the circuit.

### Simulation Steps

---

1.  Input values for the inputs (A, B, Cin) and outputs (S, Cout, Y, Bor)
2.  Run the simulation and observe the output values
3.  Verify that the output values match the expected values from the truth tables

### Simulation Results

---

Here are some example simulation results for the full adder and subtractor:

```
  +-------+       +-------+       +-------+
  |  A    |       |  B    |       |  Cin   |
  |  0    |       |  0    |       |  0     |
  +-------+       +-------+       +-------+
           |                       |
           |  XOR                      |
           |                       |
           v                       v
  +-------+       +-------+       +-------+
  |  S    |       |  Cout  |       |  GND  |
  |  0    |       |  0     |       |  0     |
  +-------+       +-------+       +-------+

  +-------+       +-------+       +-------+
  |  A    |       |  B    |       |  Bor  |
  |  0    |       |  0    |       |  1     |
  +-------+       +-------+       +-------+
           |                       |
           |  XOR                      |
           |                       |
           v                       v
  +-------+       +-------+       +-------+
  |  Y    |       |  GND  |       |  Bor  |
  |  1    |       |  GND  |       |  1     |
  +-------+       +-------+       +-------+
```

In this example, the simulator has input values of (A = 0, B = 0, Cin = 0) for the full adder and (A = 0, B = 0, Bor = 1) for the subtractor. The output values are verified to match the expected values from the truth tables.
