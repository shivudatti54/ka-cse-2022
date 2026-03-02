# Binary Adder Subtractor

## Introduction

Binary adders and subtractors are fundamental combinational circuits in computer arithmetic. They form the building blocks for ALUs (Arithmetic Logic Units), enabling processors to perform arithmetic operations on binary numbers. Understanding these circuits is essential for comprehending how CPUs execute mathematical computations.

## Key Concepts

### 1. Half Adder
- Adds two 1-bit binary numbers
- Produces **Sum** and **Carry** outputs
- Implementation: One XOR gate (for Sum) + one AND gate (for Carry)
- Truth table: 0+0=0, 0+1=1, 1+0=1, 1+0=1 with carry for 1+1

### 2. Full Adder
- Adds three 1-bit inputs (A, B, and Carry-in)
- Produces **Sum** and **Carry-out**
- Can be constructed using two half adders + one OR gate
- Essential for multi-bit addition

### 3. Binary Parallel Adder (Ripple Carry Adder)
- Cascades multiple full adders for n-bit addition
- Carries propagate sequentially (ripple effect)
- **Disadvantage:** Propagation delay increases with bit-width
- Example: 4-bit RCA = 4 full adders connected in series

### 4. Look Ahead Carry Adder (LCA)
- Solves propagation delay problem
- Generates carry signals simultaneously using **Generate (G)** and **Propagate (P)** terms
- Formulas:
  - Generate: G = A · B
  - Propagate: P = A ⊕ B
  - Carry: C₁ = G₀ + P₀·C₀
- Faster but more complex circuitry

### 5. Binary Subtractor
- **Half Subtractor:** Subtracts two bits, produces **Difference** and **Borrow**
- **Full Subtractor:** Handles borrow-in from previous stage
- **Implementation:** Can be designed separately or using adder circuits

### 6. Adder-Subtractor Circuit
- Combines addition and subtraction in one circuit
- Uses **2's complement** method for subtraction
- Control signal (M): M=0 for addition, M=1 for subtraction
- XOR gates used to complement B input when M=1

## Conclusion

Binary adders and subtractors are critical components in digital computer architecture. While Ripple Carry Adders are simple to implement, Look Ahead Carry Adders offer superior performance for high-speed processors. The unified Adder-Subtractor circuit demonstrates the elegance of digital design where a single circuit handles multiple operations through control signals.

**Exam Tip:** Remember the difference between Half Adder (2 inputs) and Full Adder (3 inputs), and understand how carry propagates in multi-bit addition.

*Based on Delhi University BSc (Hons) Computer Science NEP 2024 UGCF Syllabus*