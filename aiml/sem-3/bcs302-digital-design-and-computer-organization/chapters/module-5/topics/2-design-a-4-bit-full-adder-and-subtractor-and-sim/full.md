# **2 Design a 4-bit Full Adder and Subtractor and Simulate the Same using Basic Gates**

## **1. Introduction**

In digital design, a full adder and subtractor are fundamental building blocks for arithmetic circuits. A full adder is used to add two bits and a carry-in bit, while a subtractor is used to subtract one bit from another. In this module, we will design and simulate a 4-bit full adder and subtractor using basic gates. We will cover the historical context, design principles, and applications of these circuits.

## **2. Historical Context**

The first electronic computer, ENIAC, used vacuum tubes and a vast array of diodes and resistors to perform arithmetic operations. In the 1950s and 1960s, transistor-based computers emerged, and the first digital computers were developed. The first microprocessor, the Intel 4004, was released in 1971 and revolutionized the field of digital design.

## **3. Design Principles**

A full adder and subtractor are designed using the following principles:

- **Truth Tables**: Create a truth table to determine the output of the circuit for all possible input combinations.
- **Karnaugh Maps**: Use Karnaugh maps to simplify the truth table and reduce the number of gates required.
- **Basic Gates**: Implement the circuit using basic gates (AND, OR, NOT, and XOR).

## **4. Design of a 4-bit Full Adder**

A full adder is designed to add two bits (A and B) and a carry-in bit (Cin). The output of the full adder is a sum bit (S) and a carry-out bit (Cout).

### 4.1 Truth Table

| A   | B   | Cin | S   | Cout |
| --- | --- | --- | --- | ---- |
| 0   | 0   | 0   | 0   | 0    |
| 0   | 0   | 1   | 1   | 0    |
| 0   | 1   | 0   | 1   | 0    |
| 0   | 1   | 1   | 0   | 1    |
| 1   | 0   | 0   | 1   | 0    |
| 1   | 0   | 1   | 0   | 1    |
| 1   | 1   | 0   | 0   | 1    |
| 1   | 1   | 1   | 1   | 1    |

### 4.2 Karnaugh Map

Create a Karnaugh map to simplify the truth table:

```
  A | B | Cin
---------
S | 0 0 | 0 1 | 1 0 | 1 1
Cout | 0 0 | 0 0 | 1 0 | 1 1
```

### 4.3 Circuit Implementation

Implement the full adder using basic gates:

```
  A | B | Cin
---------
S = A ⊕ B ⊕ Cin
Cout = (A ∧ B) ∨ (A ∧ Cin) ∨ (B ∧ Cin)
```

Use XOR gates to implement the sum bit (S) and OR gates to implement the carry-out bit (Cout).

## **5. Design of a 4-bit Subtractor**

A subtractor is designed to subtract one bit (B) from another (A). The output of the subtractor is a difference bit (D) and a borrow-out bit (Bout).

### 5.1 Truth Table

| A   | B   | D   | Bout |
| --- | --- | --- | ---- |
| 0   | 0   | 0   | 0    |
| 0   | 0   | 1   | 1    |
| 0   | 1   | 1   | 0    |
| 0   | 1   | 0   | 1    |
| 1   | 0   | 1   | 0    |
| 1   | 0   | 0   | 1    |
| 1   | 1   | 0   | 1    |
| 1   | 1   | 1   | 0    |

### 5.2 Karnaugh Map

Create a Karnaugh map to simplify the truth table:

```
  A | B
---------
D | 0 1
Bout | 0 1
```

### 5.3 Circuit Implementation

Implement the subtractor using basic gates:

```
  A | B
---------
D = A ⊕ B
Bout = (A ∧ B) ∨ (A ⊕ B)
```

Use XOR gates to implement the difference bit (D) and OR gates to implement the borrow-out bit (Bout).

## **6. Simulation and Verification**

Use a digital logic simulator to verify the functionality of the full adder and subtractor. The simulator should be able to input the required inputs (A, B, Cin) and output the expected results (S, Cout, D, Bout).

## **7. Applications**

Full adders and subtractors are used in a wide range of applications, including:

- Arithmetic circuits
- Digital computers
- Microprocessors
- Embedded systems

## **8. Further Reading**

- Digital Design and Computer Organization by Morris Mano
- Digital Logic and Computer Design by David Lewis
- Introduction to Digital Logic by John L. Hennessy and David A. Patterson

This module provides a comprehensive overview of the design and simulation of 4-bit full adders and subtractors using basic gates. The design principles and applications of these circuits are discussed in detail, and the simulator is used to verify the functionality of the circuits.
