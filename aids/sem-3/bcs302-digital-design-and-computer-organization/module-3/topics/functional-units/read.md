# Functional Units in Digital Design and Computer Organization


## Table of Contents

- [Functional Units in Digital Design and Computer Organization](#functional-units-in-digital-design-and-computer-organization)
- [Introduction](#introduction)
- [1. The Arithmetic and Logic Unit (ALU)](#1-the-arithmetic-and-logic-unit-alu)
  - [1.1 Operation and Structure](#11-operation-and-structure)
  - [1.2 Status Flags and Flag Generation Logic](#12-status-flags-and-flag-generation-logic)
  - [1.3 Example: 8-bit Addition with Flags](#13-example-8-bit-addition-with-flags)
- [2. The Register File and Data Path](#2-the-register-file-and-data-path)
  - [2.1 Types of Registers](#21-types-of-registers)
  - [2.2 Register File Organization](#22-register-file-organization)
- [3. The Control Unit (CU)](#3-the-control-unit-cu)
  - [3.1 Functions of the Control Unit](#31-functions-of-the-control-unit)
  - [3.2 Implementation Methods](#32-implementation-methods)
  - [3.3 Control Signal Sequencing Example](#33-control-signal-sequencing-example)
- [4. Memory and I/O Units](#4-memory-and-io-units)
  - [4.1 Memory Unit](#41-memory-unit)
  - [4.2 I/O Unit](#42-io-unit)
- [Summary](#summary)

## Introduction

A computer system, particularly one following the **von Neumann architecture**, comprises several fundamental building blocks called **Functional Units**. Each unit is designed to perform a specific, well-defined function, and the coordinated operation of these units enables the execution of instructions. The primary functional units that constitute the core of a processor are the **Arithmetic and Logic Unit (ALU)**, the **Control Unit (CU)**, and the **Register File**, collectively forming the **Central Processing Unit (CPU)**. The CPU interacts with the **Memory Unit** and the **Input/Output (I/O) Unit** to complete its tasks. Understanding these units—their internal structure, operation, and interconnections—is essential for comprehending computer organization and design.

## 1. The Arithmetic and Logic Unit (ALU)

The ALU is the **computational heart** of the CPU. It is a **combinational digital circuit** that performs all arithmetic and logical operations on binary data. Since it is combinational, its outputs depend solely on the current inputs, and it has no internal storage capability.

### 1.1 Operation and Structure

The ALU accepts two primary operands (typically denoted as **A** and **B**) and a set of control signals called the **operation code (opcode)**. The opcode specifies which operation the ALU must perform. Based on these inputs, the ALU produces a result (**F**) and several **status flags** that provide additional information about the operation.

- **Arithmetic Operations:** Addition (ADD), Subtraction (SUB), Multiplication, Division, Increment (INC), Decrement (DEC).
- **Logical Operations:** AND, OR, NOT, XOR, NAND, NOR, XNOR.
- **Shift Operations:** Logical Shift Left/Right, Arithmetic Shift Left/Right, Rotate.

### 1.2 Status Flags and Flag Generation Logic

The ALU updates a special register called the **Status Register** (or Program Status Word - PSW) after every operation. The key flags are:

1. **Zero Flag (Z):** Set to `1` if the result is all zeros.
   $$Z = \overline{F_{n-1}} \cdot \overline{F_{n-2}} \cdot ... \cdot \overline{F_0}$$
   Equivalently, $Z = 1$ if and only if $F = 0$.

2. **Carry Flag (C):** Set to `1` if an arithmetic operation generates a carry-out from the most significant bit (MSB). For subtraction, a borrow is often represented as a complement of carry.
   $$C_{n} = \text{carry out from MSB position}$$

3. **Sign Flag (N) / Negative Flag:** Set to `1` if the result is negative. In **2's complement** representation, this is simply the value of the MSB.
   $$N = F_{n-1}$$

4. **Overflow Flag (V):** Set to `1` if the result of a signed arithmetic operation is invalid (too large or too small to represent in n bits). Overflow occurs when the carry into the MSB differs from the carry out of the MSB.
   $$V = C_{n-1} \oplus C_n$$
   Where $C_{n-1}$ is the carry into the sign bit and $C_n$ is the carry out of the sign bit.

**Proof of Overflow Detection:** In 2's complement addition, overflow occurs when adding two positive numbers yields a negative result, or two negative numbers yields a positive result. This happens precisely when the carry into the sign bit ($C_{n-1}$) is different from the carry out ($C_n$). Therefore, $V = C_{n-1} \oplus C_n$.

### 1.3 Example: 8-bit Addition with Flags

Consider adding $5_{10}$ ($0000\;0101_2$) and $3_{10}$ ($0000\;0011_2$) in an 8-bit ALU.

1. **Inputs:** $A = 5$, $B = 3$, Opcode = `ADD`
2. **Binary Addition:**

```
00000101
+ 00000011
----------
00001000 (8)
```

3. **Flags:**

- **Result (F):** $8$ ($0000\;1000_2$)
- **Zero (Z):** $0$ (result is non-zero)
- **Carry (C):** $0$ (no carry out from bit 7)
- **Negative (N):** $0$ (MSB is 0)
- **Overflow (V):** $0$ ($C_{n-1}=0, C_n=0$, so $0 \oplus 0 = 0$)

**Harder Example:** Add $127_{10}$ ($0111\;1111_2$) and $1_{10}$ ($0000\;0001_2$) in 8-bit signed arithmetic.

- Result: $1000\;0000_2 = -128_{10}$ (in 2's complement)
- **N:** $1$ (MSB is 1)
- **V:** $1$ (Adding two positives gave a negative result: overflow)
- **C:** $0$ (No unsigned carry out: $127+1=128 < 256$)

## 2. The Register File and Data Path

**Registers** are small, high-speed storage elements located within the CPU. They hold operands, intermediate results, addresses, and control information.

### 2.1 Types of Registers

- **General-Purpose Registers (GPRs):** Used for storing temporary data and operands (e.g., R0, R1, R2...). In modern architectures, these may be used for addressing calculations.
- **Special-Purpose Registers (SPRs):** Dedicated to specific control functions:
- **Program Counter (PC):** Contains the address of the **next** instruction to be fetched.
- **Instruction Register (IR):** Holds the **current** instruction being decoded.
- **Memory Address Register (MAR):** Holds the address for a memory operation.
- **Memory Data Register (MDR) / Memory Buffer Register (MBR):** Holds data being transferred to/from memory.
- **Accumulator (ACC):** A traditional register used in simple processors to hold one operand and the result of ALU operations.

### 2.2 Register File Organization

A **Register File** is a collection of registers with separate **read** and **write** ports. It typically consists of:

- **Array of Registers:** $N$ registers, each of width $W$ bits.
- **Decoder:** Selects which register to write to based on a Write Register address.
- **Multiplexers (Mux):** Select data from one of the read ports.

The CPU data path connects these units. In a **single-cycle** data path, data flows from registers → ALU → registers in one clock cycle.

## 3. The Control Unit (CU)

The Control Unit is the **brain** of the CPU. It directs the operation of all other units by generating **timing and control signals**. It is responsible for the **Instruction Cycle**: Fetch, Decode, Execute.

### 3.1 Functions of the Control Unit

1. **Instruction Fetch:** Generates control signals to fetch the instruction pointed to by the PC from memory into the IR, then increments the PC.
2. **Instruction Decode:** Interprets the opcode to determine the operation and the operand specifiers.
3. **Execution Control:** Generates sequences of control signals to route data to the ALU, enable specific registers, and trigger memory operations.

### 3.2 Implementation Methods

The CU can be implemented in two primary ways:

1. **Hardwired Control:**

- Implemented using combinational logic (decoders, state machines, logic gates).
- **Advantages:** Very fast (propagation delay is minimal), suitable for RISC processors.
- **Disadvantages:** Inflexible; any modification requires hardware redesign.

2. **Microprogrammed Control:**

- Control signals are stored in a **Control Memory (ROM/PROM/EPROM)**. Each instruction is implemented as a **microprogram** consisting of micro-instructions.
- **Advantages:** Flexible, easier to design and modify, suitable for CISC processors.
- **Disadvantages:** Slower access time (requires fetching micro-instructions from control memory).

### 3.3 Control Signal Sequencing Example

For a generic **R-type instruction** (e.g., `ADD R1, R2, R3` meaning `R1 = R2 + R3`):

**Cycle 1 (Fetch):**

- PC → MAR; Read; IR ← MBR; PC ← PC + 1

**Cycle 2 (Decode):**

- Decode IR to identify registers R2, R3, R1.

**Cycle 3 (Execute):**

- R2 → A; R3 → B; ALU ← ADD; Flags updated.
- ALU Result → R1 (Write back).

## 4. Memory and I/O Units

### 4.1 Memory Unit

The Memory Unit (RAM) stores instructions and data. The CPU interacts with it via the MAR and MBR:

- **Read:** Address placed in MAR, READ signal asserted → Data appears in MBR.
- **Write:** Address placed in MAR, Data placed in MBR, WRITE signal asserted → Data stored.

### 4.2 I/O Unit

The I/O unit manages communication with peripherals. It uses:

- **Port-mapped I/O:** Dedicated address space for I/O devices.
- **Memory-mapped I/O:** I/O devices are treated as memory locations, allowing standard memory access instructions to communicate with peripherals.

## Summary

The functional units of a computer—ALU, Control Unit, Registers, Memory, and I/O—work in concert to execute instructions. The ALU performs computations, the CU coordinates operations, registers provide fast storage, and memory/I/O handle data persistence and communication. A thorough understanding of their individual roles, internal flag logic (with proofs), and data path connections is fundamental to computer architecture.
