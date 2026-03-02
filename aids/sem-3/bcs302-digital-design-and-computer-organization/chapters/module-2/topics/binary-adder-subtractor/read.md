**Subject: Digital Design and Computer Organization**
**Module: Module 2**
**Topic: Binary Adder-Subtractor**

---

# Binary Adder-Subtractor Circuit

## 1. Introduction

In the core of a computer's Arithmetic Logic Unit (ALU), circuits that perform addition and subtraction are fundamental. While a simple binary adder can add two numbers, we often need to perform subtraction as well. Designing a separate circuit for subtraction is inefficient. Instead, we can cleverly use the principles of binary arithmetic and Boolean algebra to create a single, unified circuit that can perform both addition and subtraction operations: the Binary Adder-Subtractor. This circuit is a prime example of how computer hardware efficiently implements mathematical operations.

## 2. Core Concepts

### A. Foundation: The Full Adder (FA)
The building block of this circuit is the Full Adder. A single Full Adder adds two bits (A and B) and a carry-in (C_in) to produce a sum (S) and a carry-out (C_out).
*   **Sum (S)** = A ⊕ B ⊕ C_in
*   **Carry-out (C_out)** = A·B + B·C_in + A·C_in

To add two n-bit numbers, we cascade n Full Adders to create a **Ripple Carry Adder (RCA)**. The carry output from one stage is fed into the carry input of the next.

### B. Subtraction via Two's Complement
Computers perform subtraction using the **Two's Complement** representation of negative numbers. The key operation is:
**A - B = A + (2's Complement of B) = A + (1's Complement of B + 1)**

### C. The Controlled Inverter (XOR Gate as a Programmable Inverter)
An XOR gate has a unique property:
*   If one input is `0`, the output is the same as the other input (B ⊕ 0 = B).
*   If one input is `1`, the output is the inverted version of the other input (B ⊕ 1 = B').

This makes an XOR gate a **programmable inverter**. This property is the key to building the Adder-Subtractor.

### D. Integrating Addition and Subtraction
The Adder-Subtractor circuit is built around an n-bit Ripple Carry Adder. The critical modification is connecting each bit of the second operand (`B`) to an XOR gate, whose other input is a common control signal—let's call it **`Subtract`**.

*   **When `Subtract = 0` (ADD mode):**
    *   B_i ⊕ 0 = B_i. The original B bits are fed into the adder.
    *   The initial carry-in (C_0) is also `0`.
    *   The circuit performs **A + B**.

*   **When `Subtract = 1` (SUBTRACT mode):**
    *   B_i ⊕ 1 = B_i'. The bits of B are inverted (forming the 1's complement of B).
    *   The initial carry-in (C_0) is set to `1`.
    *   The circuit now calculates **A + (B' + 1)**, which is exactly **A + (2's Complement of B)**, i.e., **A - B**.

The final carry-out (C_out) from the last adder becomes the **borrow** indicator for subtraction. An overflow can be detected by comparing the carry into and out of the most significant bit (MSB).

## 3. Example: 4-bit Adder-Subtractor

Let's perform `A - B` where `A = 6 (0110)` and `B = 3 (0011)` using a 4-bit circuit.

1.  Set `Subtract = 1`.
2.  The XOR gates invert the bits of B: `0011` becomes `1100` (1's complement of 3).
3.  The initial carry-in, C_0, is `1`.
4.  The adder now computes: `0110 (A) + 1100 (~B) + 1 (C_0)`.
5.  Let's add this step-by-step:
    *   Bit 0: 0 + 0 + 1 = 1, Sum_0=1, C_1=0
    *   Bit 1: 1 + 0 + 0 = 1, Sum_1=1, C_2=0
    *   Bit 2: 1 + 1 + 0 = 0, Sum_2=0, C_3=1 (carry generated)
    *   Bit 3: 0 + 1 + 1 = 0, Sum_3=0, C_4=1 (final carry-out)
6.  The result is `0011` which is `3 (6 - 3)`.
7.  The final carry-out `C_4 = 1` indicates no borrow was needed (a positive result). If it were `0`, it would indicate a negative result (in two's complement form).

## 4. Key Points & Summary

| **Aspect** | **Description** |
| :--- | :--- |
| **Purpose** | A single, efficient combinational circuit that performs both binary addition and subtraction. |
| **Foundation** | Built using a Ripple Carry Adder (composed of Full Adders) and a set of XOR gates. |
| **Key Concept** | Uses a **control signal** (`Subtract`) to select between operations. An XOR gate acts as a programmable inverter on the `B` input. |
| **Addition (`Subtract=0`)** | `B` bits pass unchanged. C_in = 0. Result: `A + B`. |
| **Subtraction (`Subtract=1`)** | `B` bits are inverted. C_in = 1. This computes `A + (~B + 1)`, which is `A - B` using two's complement. |
| **Advantage** | Hardware efficiency. Reuses the adder logic for subtraction instead of requiring a separate subtractor unit. |
| **Output** | The result is the computed sum/difference. The final carry-out acts as a borrow indicator for subtraction. |

In summary, the Binary Adder-Subtractor is an elegant and fundamental circuit that demonstrates how basic gate-level components can be configured to perform complex arithmetic operations, forming the bedrock of a computer's computational capabilities.