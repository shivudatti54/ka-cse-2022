# Arithmetic Microoperations

## Introduction
Arithmetic microoperations are fundamental operations performed by the ALU (Arithmetic Logic Unit) on binary data stored in registers. These operations form the building blocks for complex computational tasks in computer systems. According to Delhi University NEP 2024 syllabus (Ge2C: Computer System Architecture), understanding these microoperations is essential for comprehending how CPUs execute arithmetic instructions.

## Key Concepts

### 1. Definition & Classification
- **Arithmetic Microoperations**: Basic operations that perform arithmetic computations on data stored in registers
- Types: **Basic** (addition, subtraction, increment, decrement) and **Multiplication/Division** (implemented through repeated operations)

### 2. Basic Arithmetic Microoperations

| Operation | RTL Notation | Description |
|-----------|--------------|-------------|
| Addition | R3 ← R1 + R2 | Binary addition of contents |
| Subtraction | R3 ← R1 – R2 | Binary subtraction (2's complement) |
| Increment | R1 ← R1 + 1 | Add 1 to register |
| Decrement | R1 ← R1 – 1 | Subtract 1 from register |
| Complement | R1 ← R1' | 1's complement |
| Negate | R1 ← R1' + 1 | 2's complement (for subtraction) |

### 3. Binary Adder Implementation
- **Half Adder**: Adds 2 bits (sum, carry outputs) — XOR + AND gates
- **Full Adder**: Adds 3 bits (2 operands + carry-in) — used for multi-bit addition
- **Parallel Adder**: Cascade of full adders for n-bit addition (propagates carry)
- **Carry Look-Ahead Adder**: Reduces propagation delay using carry generate/propagate logic

### 4. Subtraction Methods
- **Method 1**: Direct binary subtraction using borrow
- **Method 2 (Preferred)**: Add minuend to 2's complement of subtrahend
- **Overflow Detection**: Occurs when signs differ and result sign changes

### 5. BCD (Binary Coded Decimal) Addition
- Add each decimal digit using binary addition
- If sum > 9 (or carry generated), add 6 (0110) to correct result
- Handles decimal arithmetic for financial applications

### 6. ALU (Arithmetic Logic Unit)
- Integrates arithmetic and logic operations
- Select lines choose desired operation
- Status flags: Zero (Z), Carry (C), Sign (S), Overflow (V)

### 7. Register Transfer Language (RTL)
- Used to specify microoperations precisely
- Example: `R1 ← R2 + R3` means add contents of R2 and R3, store in R1

## Conclusion
Arithmetic microoperations are the foundation of CPU computation. Mastery of binary addition, subtraction, and their hardware implementations (adders, ALU) is crucial for understanding computer architecture and digital systems—key topics for Delhi University exams.