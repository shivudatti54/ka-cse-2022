# **Execution of a Complete Instruction**

## **Module 8, 8 hours**

### Overview

The execution of a complete instruction is the process of decoding, fetching, and executing all the components of a CPU instruction.

### Key Points

- **Instruction Execution Cycle**:
  - Fetch
  - Decode
  - Execute
  - Store (optional)
- **Instruction Fetch**:
  - Random access memory (RAM) provides the instruction
  - Instruction length determines the number of clock cycles
- **Instruction Decode**:
  - Decodes the instruction into machine code
  - Determines the operation and operands
- **Instruction Execution**:
  - Arithmetic and logical units (ALUs) perform operations
  - Registers store data temporarily
- **Instruction Storage**:
  - Stores the result of the instruction
  - Depends on the instruction type

### Important Formulas and Definitions

- **Instruction Length** (IL):
  - IL = Number of bits required to represent the instruction
- **Clock Cycle** (CC):
  - CC = IL / 8 (assuming 8-bit instructions)
- **Execution Time** (ET):
  - ET = CC x Execution Time (in clock cycles)

### Theorems and Concepts

- **Fetch-Decode-Execute Cycle**:
  - A fundamental concept in computer architecture
- **Instruction-Level Parallelism**:
  - The ability of a processor to execute multiple instructions simultaneously
