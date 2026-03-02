# Instruction Codes and Format

## A Comprehensive Study Material for BSc (Hons) Computer Science – Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

In the heart of every computer system lies the **Instruction Set Architecture (ISA)**—the interface between software and hardware that defines how the processor executes commands. At the core of this architecture are **instruction codes** and **instruction formats**, two fundamental concepts that determine how instructions are represented, stored, and executed within a CPU.

### What Are Instruction Codes?

An **instruction code** is a binary pattern that tells the processor what operation to perform and where to find or store data. Think of it as the "language" that the hardware understands. When you write `ADD R1, R2, R3` in assembly, the compiler translates this into a binary sequence like `0001000100100011` that the CPU decodes and executes.

### Why This Topic Matters

Understanding instruction codes and formats is essential for several reasons:

- **Software Development**: Knowledge of how instructions work helps in writing optimized code and understanding compiler behavior
- **System Programming**: Operating system developers must understand instruction sets for context switching and system calls
- **Computer Architecture**: This forms the foundation for processor design and optimization
- **Career Relevance**: Questions from this topic frequently appear in competitive exams (NET, GATE) and university examinations

### Real-World Relevance

Modern processors from Intel, AMD, and ARM all use instruction codes and formats, though with different implementations. When you run a Python program or play a video game, thousands of instructions are being fetched, decoded, and executed every millisecond—all governed by the principles of instruction codes and formats.

---

## 2. Fundamental Components of an Instruction

Every machine instruction contains two primary parts:

### 2.1 Operation Code (Opcode)

The **opcode** specifies the operation to be performed—such as ADD, SUBTRACT, LOAD, or JUMP. It is the "verb" of the instruction.

```
Example Opcodes (8-bit):
00000000 = HALT
00000001 = LOAD
00000010 = STORE
00000011 = ADD
00000100 = SUBTRACT
00000101 = JUMP
```

### 2.2 Operand

The **operand** specifies the data or location of data. This can be:
- **Register operand**: A reference to a CPU register
- **Memory operand**: A memory address
- **Immediate operand**: A constant value embedded in the instruction

### 2.3 Instruction Format Structure

An instruction format defines the layout of bits within an instruction, specifying which bits represent the opcode, which represent operands, and how they're organized.

```
┌─────────────────────────────────────────────────────────────┐
│                    INSTRUCTION FORMAT                        │
├──────────────┬──────────────────────────────────────────────┤
│   OPCODE     │              OPERAND(S)                      │
│  (k bits)    │              (n bits)                         │
└──────────────┴──────────────────────────────────────────────┘
      Total bits = k + n
```

---

## 3. Types of Instruction Formats

The number of addresses (operands) in an instruction determines the **addressing mode** and affects both the instruction's complexity and the CPU's architectural design.

### 3.1 Zero-Address Instructions

These instructions operate on the **stack**. Operations use the top of the stack, making them compact but slower for complex calculations.

**Examples**: PUSH, POP, ADD (stack-based)

```
Advantages:
- Simple hardware
- Very compact code
- Easy to implement on silicon

Disadvantages:
- Requires stack management
- Slower for complex expressions
- Limited flexibility
```

### 3.2 One-Address Instructions

These instructions use an **accumulator**—a special register that implicitly holds one operand. The accumulator is both the source and destination for operations.

```
Format: OPERATION ACCUMULATOR, MEMORY_ADDRESS

Example: ADD M   ; ACC ← ACC + [M]
         LOAD M ; ACC ← [M]
         STORE M; [M] ← ACC
```

**Real-World Context**: Early processors like the Intel 8086 and Motorola 68000 used accumulator-based architectures extensively.

### 3.3 Two-Address Instructions

Two-address instructions specify two operand locations. One typically serves as both source and destination.

```
Format: OPERATION DESTINATION, SOURCE

Example: ADD R1, R2   ; R1 ← R1 + R2
         MOV R3, R4   ; R3 ← R4
         CMP R5, R6   ; Compare R5 and R6
```

**Note**: This format is common in modern CISC processors like x86.

### 3.4 Three-Address Instructions

Three-address instructions specify two source operands and one destination operand—making the operation explicit and clear.

```
Format: OPERATION DESTINATION, SOURCE1, SOURCE2

Example: ADD R1, R2, R3   ; R1 ← R2 + R3
         SUB R4, R5, R6   ; R4 ← R5 - R6
         AND R7, R8, R9   ; R7 ← R8 AND R9
```

**Advantages**:
- Most explicit and readable
- No accumulator bottleneck
- Allows parallel execution

**Disadvantages**:
- Longer instruction format (more bits)
- More complex decoding

---

## 4. Addressing Modes

Addressing modes define how the **operand field** of an instruction specifies the location of data. This is crucial for instruction format design and significantly impacts program efficiency.

### 4.1 Immediate Addressing

The operand is a constant value embedded directly in the instruction.

```
LOAD R1, #100     ; Load value 100 into R1
ADD R2, #50      ; Add 50 to R2

Binary Format (16-bit instruction):
┌────────────┬────────────┬────────────┐
│  OPCODE    │   REG      │   VALUE    │
│  8 bits    │  4 bits    │  8 bits    │
└────────────┴────────────┴────────────┘
```

### 4.2 Register Addressing

The operand is located in a CPU register.

```
MOV R1, R2       ; Copy R2 into R1
ADD R3, R4, R5   ; R3 = R4 + R5
```

### 4.3 Direct (Absolute) Addressing

The instruction contains the memory address where the operand is stored.

```
LOAD R1, [1000]  ; Load contents of memory address 1000 into R1

Memory Layout:
Address: 1000 → Value: 42
After execution: R1 = 42
```

### 4.4 Indirect Addressing

The instruction contains a pointer to the memory address where the operand is stored.

```
LOAD R1, @1000   ; Load value at address stored in memory location 1000

Memory:
[1000] = 2000    ; (address pointer)
[2000] = 99      ; (actual data)
Result: R1 = 99
```

### 4.5 Register Indirect Addressing

A register contains the memory address of the operand.

```
LOAD R1, [R2]    ; Load value at address contained in R2

Before: R2 = 5000, Memory[5000] = 75
After: R1 = 75
```

### 4.6 Indexed Addressing

Effective address = Base address + Index register

```
LOAD R1, 1000[R2]  ; Address = 1000 + R2

Before: R2 = 50, Memory[1050] = 128
After: R1 = 128
```

### 4.7 Relative Addressing

Effective address = Program Counter (PC) + Offset (used in branch instructions)

```
JUMP +10        ; Jump 10 instructions ahead

PC = 100 → After: PC = 110
```

---

## 5. Detailed Binary Encoding Example

Let's create a complete 16-bit instruction set and show actual binary encoding:

### 5.1 Sample Instruction Set Architecture

| Opcode (4 bits) | Operation | Format | Description |
|-----------------|-----------|--------|-------------|
| 0000 | LOAD | R,Addr | Load from memory to register |
| 0001 | STORE | R,Addr | Store register to memory |
| 0010 | ADD | R1,R2,R3 | R1 = R2 + R3 |
| 0011 | SUB | R1,R2,R3 | R1 = R2 - R3 |
| 0100 | MOV | R1,R2 | R1 = R2 |
| 0101 | JMP | Addr | Jump to address |
| 0110 | JZ | Addr | Jump if zero flag set |
| 0111 | HALT | - | Stop execution |
| 1000 | AND | R1,R2,R3 | R1 = R2 AND R3 |
| 1001 | OR | R1,R2,R3 | R1 = R2 OR R3 |

### 5.2 Instruction Format Definitions

```
Two-Address Format (LOAD/STORE): 16 bits
┌────────┬────────┬─────────────┐
│ OPCODE │  REG   │   ADDRESS   │
│ 4 bits │ 4 bits │   8 bits    │
└────────┴────────┴─────────────┘

Three-Address Format (ADD/SUB/AND/OR): 16 bits
┌────────┬────────┬────────┬────────┐
│ OPCODE │   R1   │   R2   │   R3   │
│ 4 bits │ 4 bits │ 4 bits │ 4 bits │
└────────┴────────┴────────┴────────┘

Register-to-Register (MOV): 8 bits
┌────────┬────────┬────────┐
│ OPCODE │   R1   │   R2   │
│ 4 bits │ 2 bits │ 2 bits │
└────────┴────────┴────────┘

Jump Format: 16 bits
┌────────┬─────────────┐
│ OPCODE │   ADDRESS   │
│ 4 bits │   12 bits   │
└────────┴─────────────┘
```

### 5.3 Encoding Example 1: Loading Data

**Assembly**: `LOAD R5, [256]`

**Binary Encoding**:
- Opcode (LOAD) = `0000` (4 bits)
- Register R5 = `0101` (4 bits)
- Address 256 = `100000000` (9 bits, padded to 8 bits = `00000000` with overflow handling)

```
Result: 0000 0101 00000000
Hex: 0x0500
```

### 5.4 Encoding Example 2: Addition

**Assembly**: `ADD R1, R2, R3` (R1 = R2 + R3)

**Binary Encoding**:
- Opcode (ADD) = `0010` (4 bits)
- Destination R1 = `0001` (4 bits)
- Source R2 = `0010` (4 bits)
- Source R3 = `0011` (4 bits)

```
Result: 0010 0001 0010 0011
Hex: 0x2123
Binary: 0010000100100011
```

### 5.5 Encoding Example 3: Jump Instruction

**Assembly**: `JMP 1024`

**Binary Encoding**:
- Opcode (JMP) = `0101` (4 bits)
- Address 1024 = `010000000000` (12 bits)

```
Result: 0101 010000000000
Hex: 0x5400
```

---

## 6. RISC vs CISC: Instruction Format Implications

The choice of instruction format directly relates to the **RISC (Reduced Instruction Set Computer)** vs **CISC (Complex Instruction Set Computer)** design philosophy.

### 6.1 CISC Characteristics

- **Variable-length instructions**: Can be 1 to 15 bytes long
- **Multiple addressing modes**: Often 10+ different modes
- **Complex operations**: Single instructions can perform complex tasks
- **Memory-to-memory operations**: Direct memory operand support

**Example**: x86-64 instruction `ADD [eax+ebx*4+1000h], 50h`

### 6.2 RISC Characteristics

- **Fixed-length instructions**: Typically 32 bits
- **Limited addressing modes**: Usually 3-5 basic modes
- **Load-Store architecture**: Only LOAD/STORE access memory
- **Register-centric**: Most operations between registers

**Example**: MIPS instruction `add $t0, $t1, $t2`

### 6.3 Comparison Table

| Aspect | RISC | CISC |
|--------|------|------|
| Instruction Length | Fixed (32-bit) | Variable (1-15 bytes) |
| Addressing Modes | 3-5 | 10+ |
| Instructions per Program | More | Fewer |
| Hardware Complexity | Simpler decoder | Complex decoder |
| Register Count | 32+ | Few (8-16 typical) |
| Pipeline Efficiency | High | Moderate |
| Examples | MIPS, ARM, RISC-V | x86, VAX |

### 6.4 Modern Context

Modern processors often **blur the line** between RISC and CISC:
- Intel x86 processors internally **translate** CISC instructions to RISC-like micro-ops (μops)
- ARM processors support both 32-bit (AArch32) and 64-bit (AArch64) architectures
- RISC-V provides modular extensions allowing customizable instruction sets

---

## 7. Practical Examples with Code

### 7.1 Assembly to Binary Translation (MIPS-style)

Let's demonstrate how high-level code translates to instruction codes:

**C Code**: `result = a + b;`

**Assuming**:
- `a` is stored at memory address 100
- `b` is stored at memory address 104
- `result` should be stored at memory address 108
- `$t0`, `$t1`, `$t2` are temporary registers

**MIPS Assembly**:
```mips
lw $t0, 0($gp)      # Load a into $t0 (using global pointer)
lw $t1, 4($gp)      # Load b into $t1
add $t2, $t0, $t1   # $t2 = $t0 + $t1
sw $t2, 8($gp)      # Store result
```

**Binary Encoding**:
```
lw $t0, 0($gp)
Binary: 100011 01000 01000 0000000000000000
       |opcode |rt  |rs  |offset        |
Hex: 0x8C880000

lw $t1, 4($gp)
Binary: 100011 01001 01000 0000000000000100
Hex: 0x8C890004

add $t2, $t0, $t1
Binary: 000000 01000 01001 01010 00000 100000
       |opcode |rs  |rt  |rd  |shamt|funct|
Hex: 0x012A5820

sw $t2, 8($gp)
Binary: 101011 01010 01000 0000000000001000
Hex: 0xAD2A0008
```

### 7.2 Complete Program Execution Trace

Consider a simple calculator program:

```
Memory Layout:
Address 0:  LOAD R1, [100]   ; R1 = 10
Address 3:  LOAD R2, [104]   ; R2 = 20
Address 6:  ADD R3, R1, R2    ; R3 = 30
Address 9:  STORE [108], R3  ; Save result
Address 12: HALT

Memory Values:
[100] = 10
[104] = 20
[108] = ?
```

**Step-by-Step Execution**:

1. **Fetch**: CPU fetches instruction at PC=0
2. **Decode**: `0000 0001 01100100` → LOAD R1, address 100
3. **Execute**: Memory[100] = 10 → R1 = 10
4. **Store Result**: R1 now contains 10
5. **PC = 3**: Fetch next instruction
6. Continue until HALT

---

## 8. Assessment Items

### 8.1 Multiple Choice Questions

**Question 1**: In a three-address instruction format, how many operands can be specified?
- (a) 1
- (b) 2
- (c) 3
- (d) 4

**Answer**: (c) 3 (two sources + one destination)

---

**Question 2**: Which addressing mode embeds the operand value directly in the instruction?
- (a) Direct addressing
- (b) Immediate addressing
- (c) Indirect addressing
- (d) Indexed addressing

**Answer**: (b) Immediate addressing

---

**Question 3**: In the MIPS instruction `lw $t0, 8($s0)`, what is the addressing mode?
- (a) Register direct
- (b) Base register addressing
- (c) Immediate addressing
- (d) Relative addressing

**Answer**: (b) Base register addressing (effective address = $s0 + 8)

---

**Question 4**: A 16-bit instruction has 4-bit opcode and two 6-bit operand fields. How many different operations can be represented?
- (a) 4
- (b) 8
- (c) 16
- (d) 64

**Answer**: (c) 16 (2⁴ = 16 unique opcodes)

---

**Question 5**: Which architecture uses fixed-length 32-bit instructions?
- (a) x86
- (b) VAX
- (c) MIPS
- (d) IA-32

**Answer**: (c) MIPS

---

### 8.2 Short Answer Questions

**Question 1**: Explain the difference between direct and indirect addressing with examples.

**Answer**:
- **Direct Addressing**: The instruction contains the actual memory address of the operand.
  - Example: `LOAD R1, 1000` → Loads data from memory address 1000
- **Indirect Addressing**: The instruction contains a memory address that holds the actual address of the operand.
  - Example: `LOAD R1, @1000` → Reads address 1000 (say, contains 2000), then loads data from address 2000

---

**Question 2**: Why do RISC architectures typically use load-store instructions for memory access?

**Answer**:
RISC architectures use load-store instructions because:
1. **Simplicity**: Keeping memory operations separate from arithmetic operations simplifies the instruction pipeline
2. **Speed**: Register-to-register operations are faster than memory-to-register operations
3. **Predictability**: Fixed-length instructions enable single-cycle fetching and easier pipelining
4. **Parallelism**: With no memory operands in arithmetic instructions, more operations can execute in parallel

---

**Question 3**: Calculate the binary encoding for the instruction `SUB R4, R5, R6` using the following specification:
- Opcode for SUB = 0011 (4 bits)
- Register fields = 4 bits each
- Format: [Opcode][R1][R2][R3]

**Answer**:
```
Binary: 0011 0100 0101 0110
Hex: 0x3456

Breakdown:
0011 = Opcode (SUB)
0100 = R1 (R4)
0101 = R2 (R5)
0110 = R3 (R6)
```

---

### 8.3 Long Answer Questions

**Question 1**: Design a complete instruction set with at least 8 instructions, specify the format for each type, and demonstrate binary encoding for at least 3 instructions.

**[Solution Guidance]**: Students should:
1. Define opcodes for at least 8 operations (arithmetic, logical, data transfer, control)
2. Specify bit allocation for each format type
3. Provide actual binary representations
4. Show step-by-step encoding process

---

**Question 2**: Compare RISC and CISC architectures in terms of instruction formats, addressing modes, and their impact on compiler design and performance.

**[Solution Guidance]**: Students should cover:
- Instruction length differences (fixed vs variable)
- Number of addressing modes
- Register usage philosophy
- Impact on instruction decoding complexity
- Compiler optimization challenges
- Pipeline efficiency considerations
- Modern hybrid approaches

---

### 8.4 Fill in the Blanks

1. The part of an instruction that specifies the operation to be performed is called the **opcode**.
2. In **stack** addressing, operations are performed on data at the top of the stack.
3. The addressing mode where the effective address is obtained by adding a constant to the program counter is called **relative** addressing.
4. **RISC** architectures typically use fixed-length instructions for easier pipelining.
5. In **register indirect** addressing, a register holds the memory address of the operand.

---

## 9. Key Takeaways

### Core Concepts Recap

1. **Instruction Codes**: Binary patterns that represent operations (opcode) and operands; the fundamental unit of CPU communication

2. **Instruction Formats**: Structural layouts determining how bits are allocated:
   - Zero-address (stack-based)
   - One-address (accumulator-based)
   - Two-address (common in CISC)
   - Three-address (explicit, common in RISC)

3. **Addressing Modes**: Methods to specify operand locations:
   - Immediate, Register, Direct, Indirect, Indexed, Relative

4. **Binary Encoding**: Practical application of instruction formats into actual machine code

5. **RISC vs CISC**: Fundamental design philosophies affecting instruction complexity, format, and execution

### Delhi University Syllabus Alignment

This content covers the following from your NEP 2024 UGCF syllabus:
- ✓ Instruction format design
- ✓ Addressing modes (all types)
- ✓ Binary encoding examples
- ✓ RISC/CISC comparison
- ✓ Practical assembly examples
- ✓ Assessment items for examination preparation

### For Examination Success

- Remember the formula: **Instruction Format = Opcode + Operand(s)**
- Practice converting assembly to binary and vice versa
- Understand the trade-offs between different addressing modes
- Know the key differences between RISC and CISC architectures
- Be able to design a simple instruction set

---

*This study material is specifically designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF guidelines. For additional practice, refer to your prescribed textbook and solve previous year question papers.*