# Program Status Register (PSR) Instructions

## Introduction

The Program Status Register (PSR) is a fundamental component of ARM microcontroller architecture that plays a crucial role in controlling and monitoring the execution state of the processor. In ARM-based microcontrollers, particularly those following the ARM7TDMI or Cortex-M architecture, the PSR contains critical information about the current processor state, including condition flags, processor mode, and interrupt disable bits. Understanding the PSR and its associated instructions is essential for writing efficient and reliable embedded systems code.

The PSR provides real-time feedback about the results of arithmetic and logical operations, enabling the processor to make decisions through conditional execution of instructions. This conditional execution capability is one of the most powerful features of the ARM architecture, allowing developers to write compact and efficient code without using explicit branch instructions in many cases. The PSR acts as the "brain" of the processor's decision-making process, storing the outcomes of previous operations that subsequent instructions can test and respond to accordingly.

In the context of the university's BCS402 Microcontrollers course, a thorough understanding of PSR instructions is vital for successfully implementing interrupt handling, arithmetic operations, and flow control in ARM-based embedded applications. This knowledge forms the foundation for advanced topics like exception handling, context switching, and real-time operating system implementation.

## Key Concepts

### Structure of Program Status Register

The Program Status Register is a 32-bit register divided into several fields that store different types of status information. The complete PSR structure in ARM architecture (ARMv4T and later) is organized as follows:

**Bit Layout of CPSR (Current Program Status Register):**

```
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
 N Z C V - - - - - - - - - - - - - - - - - - - - I F T M4 M3 M2 M1 M0
```

**Condition Flags (bits 31-28):** These four flags indicate the outcome of the most recent arithmetic or logical operation:

- **N (Negative) Flag (bit 31):** Set when the result of a signed arithmetic operation is negative. For unsigned operations, this flag indicates whether the most significant bit of the result is 1. Mathematically, N = result[31], indicating the sign bit.

- **Z (Zero) Flag (bit 30):** Set when the result of an operation is exactly zero (Z = 1). This flag is crucial for implementing equality comparisons and loop termination conditions. The flag is cleared when the result is non-zero (Z = 0).

- **C (Carry) Flag (bit 29):** Set when an arithmetic operation produces a carry out of the most significant bit (for unsigned arithmetic). It also indicates NOT borrow in subtraction operations. Specifically, for subtraction (CMP, SUBS), C = 1 indicates no borrow (unsigned greater than or equal), while C = 0 indicates borrow (unsigned less than).

- **V (Overflow) Flag (bit 28):** Set when a signed arithmetic operation produces an overflow, meaning the result is too large or too small to fit in the available bits. This occurs when the signs of the operands differ but the sign of the result differs from the sign of the operands.

**Processor Mode Bits (bits 4-0):** These five bits determine the current processor mode:

| Mode Bits (M[4:0]) | Mode Name  | Description                    |
| ------------------ | ---------- | ------------------------------ |
| 10000              | User (USR) | Normal execution mode          |
| 10001              | FIQ        | Fast Interrupt Request         |
| 10010              | IRQ        | Interrupt Request              |
| 10011              | Supervisor | Software interrupt mode        |
| 10111              | Abort      | Memory fault handling          |
| 11011              | Undefined  | Undefined instruction handling |
| 11111              | System     | Privileged User mode           |

**Control Bits:**

- **I Bit (bit 7):** IRQ disable flag. When set (I=1), IRQ interrupts are disabled.
- **F Bit (bit 6):** FIQ disable flag. When set (F=1), FIQ interrupts are disabled.
- **T Bit (bit 5):** Thumb state bit. T=1 indicates Thumb instruction set, T=0 indicates ARM instruction set.

### Application Program Status Register (APSR)

The APSR contains only the condition flags (N, Z, C, V, and Q). This is the portion most commonly accessed by application programmers. In ARMv7+ architectures, the APSR is accessible as a separate register for reading condition flags without affecting mode bits. The APSR bit positions are identical to the corresponding bits in the CPSR.

### Saved Program Status Register (SPSR)

The SPSR is used to preserve the CPSR when an exception occurs. Each processor mode (except User and System modes) has its own SPSR. When an exception is taken, the processor automatically saves the current CPSR to the SPSR corresponding to the new mode. This allows the exception handler to restore the original processor state when returning from the exception.

**Exception Types and SPSR Usage:**

- **FIQ Exception:** SPSR_fiq stores the CPSR
- **IRQ Exception:** SPSR_irq stores the CPSR
- **Supervisor Exception:** SPSR_svc stores the CPSR
- **Abort Exception:** SPSR_abt stores the CPSR
- **Undefined Instruction Exception:** SPSR_und stores the CPSR

### Condition Codes

ARM instructions can be executed conditionally based on the state of the condition flags. The condition field is encoded in bits 31-28 of every instruction. The following table summarizes the standard condition codes:

| Mnemonic | Meaning                           | Flags Tested    | Application Example            |
| -------- | --------------------------------- | --------------- | ------------------------------ |
| EQ       | Equal                             | Z = 1           | CMP R0, R1; BEQ label          |
| NE       | Not Equal                         | Z = 0           | CMP R0, R1; BNE label          |
| CS/HS    | Carry Set/Unsigned Higher or Same | C = 1           | Check unsigned ≥ comparison    |
| CC/LO    | Carry Clear/Unsigned Lower        | C = 0           | Check unsigned < comparison    |
| MI       | Minus/Negative                    | N = 1           | Check negative result          |
| PL       | Plus/Positive or Zero             | N = 0           | Check non-negative result      |
| VS       | Overflow Set                      | V = 1           | Check signed overflow occurred |
| VC       | Overflow Clear                    | V = 0           | Check no signed overflow       |
| HI       | Unsigned Higher                   | C = 1 and Z = 0 | Check unsigned > comparison    |
| LS       | Unsigned Lower or Same            | C = 0 or Z = 1  | Check unsigned ≤ comparison    |
| GE       | Signed Greater than or Equal      | N = V           | Check signed ≥ comparison      |
| LT       | Signed Less Than                  | N ≠ V           | Check signed < comparison      |
| GT       | Signed Greater Than               | Z = 0 and N = V | Check signed > comparison      |
| LE       | Signed Less than or Equal         | Z = 1 or N ≠ V  | Check signed ≤ comparison      |
| AL       | Always (default)                  | Any             | Unconditional execution        |

### PSR Transfer Instructions

ARM provides two special instructions for transferring data between the PSR and general-purpose registers. These instructions are privilege-controlled and can only be used in privileged processor modes.

#### MRS (Move from Status Register)

The MRS instruction reads the CPSR or SPSR into a general-purpose register. This is the only way to directly read the processor status.

**Syntax:**

```
MRS{Rd,} PSR_
```

Where:

- Rd is the destination general-purpose register (Rd cannot be PC)
- PSR\_ is either CPSR or SPSR

**Operational Semantics:**

```
Rd ← PSR_
```

**Examples:**

```
MRS R0, CPSR ; Read current processor status
MRS R1, SPSR ; Read saved status (only in privileged modes)
MRS R5, CPSR ; Copy CPSR to R5 for analysis
```

**Use Case - Reading Condition Flags:**
To test individual flags, the programmer typically reads the CPSR and then uses logical operations to isolate specific bits:

```
MRS R0, CPSR ; Move CPSR to R0
TST R0, #0x80000000 ; Test N flag (bit 31)
BNE negative ; Branch if negative
```

#### MSR (Move to Status Register)

The MSR instruction writes a value to the CPSR or SPSR, allowing modification of flags, mode bits, or control bits.

**Syntax:**

```
MSR{PSR_, #<imm>}
MSR{PSR_, <Rm>}
```

Where the optional field specifiers determine which parts of the PSR are modified:

- **c** - Control field (bits 0-7): Contains mode bits (M[4:0]), T bit, I and F flags
- **x** - Extension field (bits 8-15): Reserved for implementation-defined use
- **s** - Status field (bits 16-23): Reserved for future use
- **f** - Flags field (bits 24-31): Contains condition flags (N, Z, C, V)

**Examples:**

```
MSR CPSR_f, R0 ; Move R0 to CPSR flags only (N,Z,C,V)
MSR CPSR_c, #0xD3 ; Move immediate to control bits (set SVC mode, disable IRQ/FIQ)
MSR SPSR_f, R1 ; Move R1 to SPSR flags only
MSR CPSR_cxsf, R2 ; Move R2 to all CPSR fields
MSR CPSR_fsxc, R3 ; Move R3 to flags, status, extension, and control fields
```

**Common Mode Switching Example:**

```
; Switch from User to Supervisor mode
MRS R0, CPSR ; Read current status
BIC R0, R0, #0x1F ; Clear mode bits (bits 0-4)
ORR R0, R0, #0x13 ; Set Supervisor mode (0x13 = 10011)
MSR CPSR_c, R0 ; Write back control bits only
```

**Enabling Interrupts:**

```
; Enable IRQ interrupts
MRS R0, CPSR
BIC R0, R0, #0x80 ; Clear I bit (bit 7)
MSR CPSR_c, R0
```

### Arithmetic Flags Modification

Most arithmetic and logical instructions can optionally update the CPSR flags based on their results. This is controlled by the 'S' suffix in the instruction. When the S bit is set, the instruction updates the condition flags according to the result.

**Flag Update Instructions:**

```
ADDS R0, R1, R2 ; Add and update flags (R0 = R1 + R2)
SUBS R3, R4, R5 ; Subtract and update flags (R3 = R4 - R5)
ANDS R6, R7, R8 ; Logical AND and update flags
EORS R9, R10, R11 ; Logical XOR and update flags
```

**Compare Instructions:**
The CMP and CMN instructions perform arithmetic operations but discard the result, updating only the flags:

- **CMP (Compare):** Subtracts the second operand from the first (flags ← Rn - Rm)
- **CMN (Compare Negative):** Adds the second operand to the first (flags ← Rn + Rm)

```
CMP R0, R1 ; Set flags based on R0 - R1
CMN R2, R3 ; Set flags based on R2 + R3
```

**Test Instructions:**
The TST and TEQ instructions perform bitwise operations and update flags:

- **TST (Test):** Performs logical AND (flags ← Rn AND Rm)
- **TEQ (Test Equivalence):** Performs logical XOR (flags ← Rn XOR Rm)

```
TST R0, #0x01 ; Test bit 0 of R0
TEQ R1, R2 ; Test if R1 equals R2 (without affecting C/V)
```

### Flag Manipulation Theorems

Understanding how flags are set requires knowledge of the underlying arithmetic properties:

**Overflow Detection in Two's Complement Addition:**
V is set if both operands have the same sign and the result has a different sign:

```
V = (Rn[31] == Rm[31]) AND (Rn[31] != Result[31])
```

**Overflow Detection in Two's Complement Subtraction:**
V is set when the signs of the operands differ and the sign of the result differs from the sign of the first operand:

```
V = (Rn[31] != Rm[31]) AND (Rn[31] != Result[31])
```

**Carry Detection in Addition:**
C is set when the addition produces a carry out of bit 31:

```
C = (Result[31:0] < Rn) OR (Result[31:0] < Rm) [unsigned interpretation]
```

**Borrow Detection in Subtraction:**
For subtraction, C is set when NO borrow occurs:

```
C = NOT (Rn < Rm) [unsigned interpretation]
```

This explains why CMP (which computes Rn - Rm) sets C=1 when Rn ≥ Rm (unsigned) and C=0 when Rn < Rm.
