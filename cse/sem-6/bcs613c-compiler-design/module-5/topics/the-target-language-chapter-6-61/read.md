# The Target Language

## Chapter 6.1

---

## 1. Introduction

In the compilation process, the **target language** refers to the output language that a compiler generates from the source program. The target language typically represents a form closer to machine execution, bridging the gap between high-level source code and the hardware that executes it. Understanding the target language is essential for the **code generation** phase, where intermediate representations are transformed into executable instructions.

This chapter examines the theoretical and practical aspects of target language design, including instruction set architectures, addressing modes, and the trade-offs involved in selecting appropriate target representations.

---

## 2. Definition and Role of Target Language

### 2.1 Formal Definition

The **target language** $L_T$ is defined as the programming language into which a compiler translates the source language $L_S$. Mathematically, the compilation process can be expressed as a mapping:

$$C: L_S \longrightarrow L_T$$

where $C$ represents the compiler, $L_S$ is the source language, and $L_T$ is the target language.

The target language serves as an intermediate representation that can subsequently be translated into **machine code**—the binary instructions that the processor executes directly.

### 2.2 Role in Compilation

The target language appears in the **backend** of a compiler, following the optimization phase. Its primary responsibilities include:

- **Instruction Selection**: Choosing appropriate machine instructions for each intermediate code operation.
- **Register Allocation**: Assigning variables to a finite set of processor registers.
- **Instruction Scheduling**: Ordering instructions to maximize pipeline efficiency.
- **Addressing Mode Selection**: Determining how operands are accessed in memory.

---

## 3. Target Machine Model

To effectively generate code, compilers construct an abstract model of the target machine, comprising:

### 3.1 Register Set

Modern processors contain a finite number of registers, typically categorized as:

| Category        | Purpose                 | Example (x86-64)   |
| --------------- | ----------------------- | ------------------ |
| General Purpose | Temporary computation   | RAX, RBX, RCX, RDX |
| Index           | Indexed addressing      | RSI, RDI           |
| Base Pointer    | Stack frame management  | RBP                |
| Stack Pointer   | Memory stack operations | RSP                |
| Program Counter | Instruction sequencing  | RIP                |

### 3.2 Memory Organization

The target machine memory is typically organized as a hierarchy:

- **Primary Memory (RAM)**: Fast access, volatile storage
- **Cache Levels**: L1, L2, L3 with decreasing speed and increasing size
- **Secondary Storage**: Persistent, slower access

Compilers must consider memory hierarchy when generating code to maximize **locality of reference** and minimize cache misses.

### 3.3 Instruction Formats

Instruction format defines the binary encoding of machine instructions. Common formats include:

- **Zero-address**: Stack-based instructions (e.g., JVM bytecode)
- **One-address**: Accumulator-based instructions
- **Two-address**: Most modern RISC architectures
- **Three-address**: Typical RISC instruction format

For example, in a three-address format:

```
ADD R1, R2, R3 ; R1 ← R2 + R3
```

Each field specifies: operation code (opcode), destination register, and two source registers.

---

## 4. Addressing Modes

**Addressing modes** specify how operands are located in memory or registers. The choice of addressing mode significantly impacts code efficiency.

### 4.1 Types of Addressing Modes

1. **Immediate Addressing**: Operand value is constant in instruction

```assembly
MOV R1, #10 ; R1 ← 10
```

2. **Direct (Absolute) Addressing**: Operand address is explicit

```assembly
MOV R1, [1000] ; R1 ← contents of memory address 1000
```

3. **Indirect (Register Deferred) Addressing**: Register contains memory address

```assembly
MOV R1, [R2] ; R1 ← contents of address in R2
```

4. **Indexed Addressing**: Address computed by adding base and index

```assembly
MOV R1, [R2 + R3] ; R1 ← contents of (R2 + R3)
```

5. **Relative Addressing**: Address relative to program counter

```assembly
JMP +12 ; Jump 12 bytes forward from current PC
```

### 4.2 Cost Analysis

The number of memory references ($M$) and clock cycles ($C$) varies by addressing mode:

| Addressing Mode | Memory References | Relative Cost |
| --------------- | ----------------- | ------------- |
| Register        | 0                 | 1×            |
| Immediate       | 0                 | 1×            |
| Direct          | 1                 | ~2×           |
| Indirect        | 2                 | ~3×           |
| Indexed         | 2                 | ~3×           |

---

## 5. RISC vs CISC Architecture

The target language design is heavily influenced by the underlying processor architecture.

### 5.1 Reduced Instruction Set Computer (RISC)

**Characteristics**:

- Fixed-length instructions (typically 32 bits)
- Load-store architecture (arithmetic only between registers)
- Large register file (32-128 registers)
- Simple instructions (one cycle per instruction)
- Pipeline-friendly design

**Example RISC Instruction (MIPS)**:

```assembly
ADD $t0, $t1, $t2 ; $t0 = $t1 + $t2
LW $t0, 0($t1) ; Load word from memory
```

### 5.2 Complex Instruction Set Computer (CISC)

**Characteristics**:

- Variable-length instructions
- Memory-to-memory operations permitted
- Fewer registers
- Complex instructions (multiple clock cycles)
- Microcode implementation

**Example CISC Instruction (x86)**:

```assembly
ADD EAX, [EBX] ; EAX = EAX + memory at EBX
MOV AX, [BX+SI+4] ; Complex addressing with displacement
```

### 5.3 Comparative Analysis

| Feature                  | RISC          | CISC             |
| ------------------------ | ------------- | ---------------- |
| Instruction Count        | Higher        | Lower            |
| Clock Cycles/Instruction | 1 (typically) | Variable (1-10+) |
| Pipeline Efficiency      | High          | Moderate         |
| Code Size                | Larger        | Smaller          |
| Hardware Complexity      | Lower         | Higher           |
| Compiler Complexity      | Higher        | Lower            |

**Theorem 6.1**: For any source program, the code generated for a RISC target requires at least as many instructions as the equivalent CISC code, but each instruction typically completes in fewer clock cycles.

_Proof_: This follows from the complexity equivalence principle—complex operations must be decomposed into multiple RISC instructions. However, RISC instructions are designed to execute in a single cycle, whereas CISC instructions may require multiple micro-operations. ∎

---

## 6. Code Generation Considerations

### 6.1 Instruction Selection

The code generator must map intermediate code operations to target machine instructions optimally. This involves:

- **Pattern Matching**: Matching intermediate code patterns to instruction templates
- **Cost Estimation**: Evaluating instruction sequences based on execution time
- **Addressing Mode Optimization**: Selecting the most efficient addressing for each operand

### 6.2 Register Allocation

With limited registers, compilers employ **graph coloring** algorithms for register allocation:

**Theorem 6.2 (Chaitin's Algorithm)**: A program is $k$-colorable (assignable to $k$ registers) if and only if its interference graph does not contain a $K_{k+1}$ clique.

_Proof Sketch_: The interference graph represents conflicts between variables that cannot share a register. If a $(k+1)$-clique exists, at least $k+1$ variables are simultaneously live, requiring $k+1$ registers. Conversely, if no such clique exists, graph coloring with $k$ colors is possible. ∎

### 6.3 Peephole Optimization

Local transformations that improve instruction sequences:

```assembly
; Before optimization
MOV R1, R2
ADD R3, R1, R0

; After peephole (remove redundant move)
ADD R3, R2, R0
```

---

## 7. Example: Code Generation for Expression Evaluation

Consider the expression: `x = a + b * c`

**Three-Address Code**:

```
t1 = b * c
t2 = a + t1
x = t2
```

**x86-64 Assembly (with optimization)**:

```assembly
IMUL RBX, RCX ; RBX = b * c
LEA RAX, [RBX+RDX] ; RAX = a + (b * c) using LEA
MOV [x], RAX ; Store result
```

---

## 8. Key Concepts Summary

| Term                  | Definition                                                     |
| --------------------- | -------------------------------------------------------------- |
| Target Language       | Output language of compilation, typically assembly or bytecode |
| Instruction Set       | Complete set of operations supported by the processor          |
| Addressing Mode       | Method of specifying operand location                          |
| Register Allocation   | Process of assigning variables to processor registers          |
| RISC                  | Processor design with simple, fixed-format instructions        |
| CISC                  | Processor design with complex, variable-format instructions    |
| Peephole Optimization | Local instruction sequence improvement                         |

---

## 9. Chapter Summary

This chapter established the foundational concepts of target language design in compiler construction. We examined:

1. The formal definition of target language as a compilation output
2. The abstract machine model required for code generation
3. Various addressing modes and their performance implications
4. The architectural differences between RISC and CISC paradigms
5. Practical considerations in instruction selection and register allocation

These concepts provide the theoretical framework necessary for understanding subsequent chapters on optimization and code generation algorithms.

---

### Key Takeaways

- The target language bridges high-level source code and machine-executable instructions
- Understanding processor architecture (RISC vs CISC) is essential for effective code generation
- Addressing mode selection significantly impacts execution performance
- Register allocation, typically via graph coloring, manages limited processor resources
- Modern compilers must consider pipeline characteristics and cache behavior
