# Addressing Modes and RISC vs CISC

## Introduction

In the study of Computer System Architecture, two fundamental concepts that form the backbone of processor design and assembly language programming are **addressing modes** and the **RISC vs CISC** architectural debate. Understanding addressing modes is essential because they determine how operands are accessed in memory or registers during instruction execution. Meanwhile, the RISC (Reduced Instruction Set Computer) and CISC (Complex Instruction Set Computer) classification represents one of the most significant philosophical debates in the history of computer architecture.

For students at the University of Delhi, mastering these concepts is crucial not only for acing semester examinations but also for building a strong foundation in low-level programming and system design. Modern processors, including those found in smartphones (ARM - RISC), desktops (x86 - CISC), and servers, embody these architectural principles. The Intel and AMD processors that power most personal computers are CISC-based, while Apple's M-series chips and most mobile processors use ARM's RISC architecture. This real-world relevance makes the topic particularly important for aspiring computer scientists.

## Key Concepts

### Addressing Modes

An addressing mode specifies how to locate the operand (the data to be operated on) of an instruction. The choice of addressing mode affects instruction execution time, code density, and programming flexibility. Processors support multiple addressing modes to accommodate different programming needs.

**1. Immediate Addressing**
In immediate addressing, the operand value is directly included in the instruction itself. This mode is used for constants and initialization operations.
- Example: `MOV AX, 5` — The value 5 is immediately available
- Advantage: No memory access required, fastest mode
- Disadvantage: Limited range; the constant is part of the instruction

**2. Register Addressing**
The operand is located in a register. No memory access is needed.
- Example: `MOV AX, BX` — Copies content of BX into AX
- Advantage: Fastest execution (no memory access)
- Disadvantage: Limited to register-sized operands

**3. Direct (Absolute) Addressing**
The instruction contains the actual memory address of the operand.
- Example: `MOV AX, [1000H]` — Loads value from memory address 1000H
- Advantage: Simple to understand
- Disadvantage: Security concerns; address is fixed at assembly time

**4. Indirect Addressing**
The instruction contains a pointer to the memory location that holds the operand address.
- Example: `MOV AX, [[1000H]]` — First access memory location 1000H to get the actual address, then fetch operand
- Advantage: Allows dynamic address calculation
- Disadvantage: Multiple memory accesses required

**5. Register Indirect Addressing**
The register holds the memory address of the operand.
- Example: `MOV AX, [BX]` — BX contains the memory address
- Advantage: Flexible; address can be changed at runtime
- Disadvantage: Requires register to hold address

**6. Indexed Addressing**
The effective address is computed by adding a constant (displacement) to the contents of an index register.
- Example: `MOV AX, [SI + 1000H]` — Address = SI + 1000H
- Advantage: Useful for accessing array elements
- Disadvantage: Requires index register setup

**7. Base-Register Addressing**
Similar to indexed addressing, but uses a base register (typically for accessing structure fields or tables).
- Example: `MOV AX, [BX + SI]` — Address = BX + SI
- Advantage: Supports complex data structure access

**8. Relative Addressing**
The address is computed relative to the program counter (PC). Used mainly in branch instructions.
- Example: `JMP SHORT Label` — Jumps relative to current PC
- Advantage: Position-independent code possible
- Disadvantage: Limited branch range

**9. Stack Addressing**
Operands are implicitly stored on the stack. The top of stack (TOS) pointer is used.
- Example: `PUSH AX` — Pushes AX onto stack; `POP BX` — Pops into BX
- Advantage: Convenient for subroutine calls and temporary storage

### RISC vs CISC Architecture

**CISC (Complex Instruction Set Computer)**

CISC emerged in the 1960s and 1970s with the philosophy that complex operations should be built into the hardware itself. The goal was to reduce the semantic gap between high-level languages and machine code.

**Key Characteristics:**
- Large instruction set (100-250 instructions)
- Variable instruction lengths (1 to 15 bytes)
- Multiple addressing modes (20+)
- Complex instructions that perform multiple operations
- Microcode implementation (instructions translated into micro-operations)
- Fewer registers (typically 8-16)

**Examples:** Intel x86, AMD x86-64, VAX, Motorola 68000

**Advantages:**
- Higher code density (fewer instructions needed)
- Compiler simplification
- Single instructions can perform complex tasks
- Easier assembly programming

**Disadvantages:**
- Complex hardware design
- Slower clock speeds due to complexity
- Variable execution times
- More transistors required for decode logic

**RISC (Reduced Instruction Set Computer)**

RISC emerged in the 1980s as a reaction to CISC complexity. The RISC philosophy emphasizes simplicity and efficiency.

**Key Characteristics:**
- Small, uniform instruction set (32-100 instructions)
- Fixed instruction length (typically 32 bits)
- Limited addressing modes (3-5)
- Simple instructions (each executes in one clock cycle)
- Load-Store architecture (arithmetic only between registers)
- Large register file (32-128 registers)
- Pipelining-friendly design

**Examples:** ARM (used in iPhones, Android phones), MIPS, SPARC, PowerPC, RISC-V

**Advantages:**
- Simpler hardware, faster clock speeds
- Easier to pipeline (parallel execution)
- Predictable instruction execution time
- Lower power consumption
- Better performance per watt

**Disadvantages:**
- Lower code density (more instructions needed)
- Requires more memory
- More complex compilers

**The Modern Convergence**

Interestingly, modern processors have converged. x86 (CISC) internally translates instructions into RISC-like micro-operations (μops), while ARM (RISC) has added more complex instructions. The distinction has become less clear in practice.

## Examples

**Example 1: Array Sum Calculation**

Consider summing elements of an array using different addressing modes in x86 assembly:

```
; Using Indexed Addressing
MOV SI, 0          ; Initialize index
MOV CX, 10         ; Counter for 10 elements
MOV AX, 0          ; Initialize sum

SUM_LOOP:
    ADD AX, ARRAY[SI]  ; Indexed addressing
    ADD SI, 2         ; Move to next element (word = 2 bytes)
    LOOP SUM_LOOP
```

Here, `ARRAY[SI]` uses indexed addressing where SI acts as the offset from the base address of ARRAY. This is efficient for iterating through arrays.

**Example 2: RISC vs CISC for Computing Sum = A + B**

*CISC Approach (x86):*
```assembly
ADD EAX, EBX    ; Single instruction, adds EBX to EAX
```
The processor uses microcode to break this into: Fetch, Decode, Execute, Store.

*RISC Approach (ARM):*
```assembly
LDR R1, [R2]    ; Load A from memory to R1
LDR R3, [R4]    ; Load B from memory to R3
ADD R5, R1, R3  ; Add registers, store in R5
STR R5, [R6]    ; Store result
```

RISC requires explicit load/store operations, but each instruction executes in exactly one cycle (assuming no pipeline stalls).

**Example 3: Subroutine Call - Stack Addressing**

```
PUSH AX          ; Save AX (uses stack addressing)
PUSH BX          ; Save BX
CALL SUBROUTINE  ; Call procedure
POP BX           ; Restore BX
POP AX           ; Restore AX
```

The CALL instruction pushes the return address onto the stack, and RET pops it back. This demonstrates the automatic nature of stack addressing.

## Exam Tips

1. **Memorize the addressing modes**: Know at least 6-7 modes with definitions and one example each. This is frequently asked in DU exams.

2. **Understand the trade-offs**: Be prepared to explain why different addressing modes exist and when to use each. Questions often ask to "compare" or "differentiate."

3. **RISC vs CISC is a hot topic**: Expect a long-answer question (10-12 marks) on this. Prepare a table comparing at least 8-10 points.

4. **Real-world examples matter**: Mention specific processors (Intel x86 for CISC, ARM for RISC) to demonstrate understanding.

5. **Load-Store Architecture**: Remember that RISC processors only allow arithmetic between registers; memory access requires separate load/store instructions.

6. **Modern relevance**: The convergence of RISC and CISC in modern processors (x86 using micro-ops, ARM adding SIMD) shows updated understanding.

7. **Code density concept**: CISC has higher code density (fewer instructions), while RISC requires more memory instructions. This is a common exam question.

8. **Register philosophy**: CISC has fewer registers (8-16) because complex instructions can use memory; RISC needs many registers (32-128) to avoid memory access.