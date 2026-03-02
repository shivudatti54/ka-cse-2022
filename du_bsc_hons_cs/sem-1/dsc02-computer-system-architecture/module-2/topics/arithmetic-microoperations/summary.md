# Arithmetic Microoperations

## Introduction
Arithmetic microoperations are fundamental operations performed by the Arithmetic Logic Unit (ALU) on binary data. They form the building blocks for complex arithmetic operations in computer systems. According to the Delhi University NEP 2024 UGCF syllabus (Computer System Architecture), understanding these microoperations is essential for comprehending how processors execute arithmetic instructions at the hardware level.

## Key Concepts

### Basic Arithmetic Microoperations
- **Addition (A + B)**: Adds two binary numbers stored in registers; result stored in destination register
- **Subtraction (A - B)**: Performed using 2's complement addition (A + B̅ + 1)
- **Increment (A + 1)**: Adds 1 to the operand
- **Decrement (A - 1)**: Subtracts 1 from the operand

### Binary Adder Implementation
- **Half Adder**: Adds 2 bits, produces sum and carry
- **Full Adder**: Adds 3 bits (2 operands + carry-in), produces sum and carry-out
- **Ripple Carry Adder**: Cascaded full adders for n-bit addition (propagation delay issue)

### Subtraction Methods
- **Borrow Method**: Traditional binary subtraction with borrow
- **2's Complement Method**: Add minuend to 2's complement of subtrahend (A + B̅ + 1)

### Arithmetic Logic Unit (ALU)
- Integrated circuit performing arithmetic and logical operations
- Select lines determine the operation to be performed
- Status flags: Zero (Z), Carry (C), Sign (S), Overflow (V)

### Multiplication & Division Microoperations
- **Multiplication**: Repeated addition using shift-and-add algorithm
- **Division**: Repeated subtraction using shift-and-subtract algorithm
- Implemented through iterative microoperations in the control unit

### Overflow Detection
- **Signed Numbers**: Occurs when carry into sign bit differs from carry out
- **Unsigned Numbers**: Occurs when final carry-out is 1

### Register Transfer Language (RTL) Notation
- R1 ← R2 + R3 (Add contents of R2 and R3, store in R1)
- R1 ← R1 + 1 (Increment)
- R1 ← R1 - 1 (Decrement)

## Conclusion
Arithmetic microoperations are essential for processor design and computer architecture. Mastering these concepts enables understanding of instruction execution, ALU design, and performance optimization. These fundamentals are crucial for exam success and future studies in digital systems and microprocessor design.