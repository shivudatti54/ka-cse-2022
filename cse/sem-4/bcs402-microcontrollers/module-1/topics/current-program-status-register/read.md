# Current Program Status Register (CPSR) in ARM Architecture

## Introduction

The Current Program Status Register (CPSR) constitutes one of the most fundamental control registers in the ARM (Advanced RISC Machines) microprocessor architecture. As a 32-bit special-purpose register, the CPSR plays a pivotal role in governing the processor's operational state, monitoring the execution status of instructions, and managing the various processor operating modes. In ARM7, ARM9, and other ARM processors extensively utilized in embedded systems and microcontroller applications, the CPSR serves as the primary mechanism for controlling conditional execution, interrupt handling, and processor mode transitions.

The CPSR is essential for understanding the elegant design philosophy of ARM architecture, particularly its provision for conditional execution of most instructions based on the state of status flags. This feature significantly reduces branch prediction penalties and enables more efficient pipeline utilization. Furthermore, the CPSR facilitates interrupt management through its disable bits and enables the processor to operate in different privilege modes, each with distinct access levels to system resources.

In the context of the BCS402 Microcontrollers course, the CPSR forms the foundational concepts covered in Module 1 as part of ARM architecture fundamentals. This topic frequently appears in university examinations, requiring students to possess not only theoretical knowledge but also the ability to analyze flag states after specific operations and understand the implications of mode bits in various scenarios.

## Theoretical Framework

### 1. CPSR Architecture and Bit Field Organization

The CPSR is a 32-bit register organized into distinct fields, each serving specific functions in processor control and status monitoring. The complete bit-field structure is as follows:

| Bits | Field Name   | Description                                                            |
| ---- | ------------ | ---------------------------------------------------------------------- |
| 31   | N (Negative) | Set when result is negative in signed arithmetic                       |
| 30   | Z (Zero)     | Set when result is zero                                                |
| 29   | C (Carry)    | Set when arithmetic operation generates carry/borrow                   |
| 28   | V (Overflow) | Set when signed arithmetic operation produces overflow                 |
| 27   | Q (Sticky)   | Set on saturation in DSP operations (ARMv5TE and above)                |
| 26-8 | Reserved     | Reserved for future architecture extensions                            |
| 7    | I (IRQ)      | When set to 1, disables IRQ interrupts                                 |
| 6    | F (FIQ)      | When set to 1, disables FIQ interrupts                                 |
| 5    | T (State)    | Indicates ARM (0) or Thumb (1) instruction set state                   |
| 4-0  | Mode (M)     | Processor mode field encoding (10000=User, 10001=FIQ, 10010=IRQ, etc.) |

**Theorem 1.1: Flag Update Mechanism**
The condition flags N, Z, C, and V are updated according to the result of the executed instruction. Specifically:

- The N flag is set to bit[31] of the result (the sign bit in two's complement representation)
- The Z flag is set if and only if all 32 bits of the result are zero
- The C flag is set if and only if the instruction generates a carry out of bit[31] (unsigned overflow)
- The V flag is set if and only if the signed result cannot be represented in 32-bit two's complement

### 2. Condition Flags: Detailed Analysis

#### 2.1 Negative Flag (N) - Bit 31

The Negative flag (N) provides critical information about the signed arithmetic result of the most recent operation. In two's complement representation, the most significant bit (MSB) serves as the sign bit, where a value of 1 indicates a negative number and 0 indicates a non-negative number. When the processor executes an arithmetic or logical operation that updates the flags, it copies the result's MSB to the N flag.

**Proof of N Flag Behavior:**
For any 32-bit signed integer representation using two's complement, the value of bit[31] determines both the sign and the interpretation of the number. If we denote the result as R, then:

- N = 1 if and only if R[31] = 1 (indicating R < 0 in signed interpretation)
- N = 0 if and only if R[31] = 0 (indicating R ≥ 0 in signed interpretation)

This flag is particularly significant in signed comparison operations and conditional branches where the sign of the result determines program flow.

#### 2.2 Zero Flag (Z) - Bit 30

The Zero flag (Z) serves as an indicator of whether the result of the most recent operation equals zero. This flag is extensively used in conditional branching and comparison operations. The CMP (Compare) instruction explicitly sets the flags based on the difference of its operands without storing the result, making the Z flag essential for equality checks.

**Theorem 2.1: Z Flag in Comparisons**
For a CMP instruction computing (Rn - Operand), the Z flag is set if and only if Rn equals Operand, because:

- If Rn = Operand, then (Rn - Operand) = 0, thus Z = 1
- If Rn ≠ Operand, then (Rn - Operand) ≠ 0, thus Z = 0

#### 2.3 Carry Flag (C) - Bit 29

The Carry flag (C) serves dual purposes in ARM arithmetic operations. For unsigned addition operations, it indicates whether a carry out of the MSB occurred, which is equivalent to unsigned overflow. For unsigned subtraction operations, it indicates whether a borrow was required, representing the complement of the logical borrow.

**Proof of C Flag Behavior in Subtraction:**
In ARM, the CMP and SUBS instructions compute Rn - Operand. The carry flag is set as follows:

- C = 1 if no borrow occurred (i.e., Rn ≥ Operand as unsigned)
- C = 0 if borrow occurred (i.e., Rn < Operand as unsigned)

This behavior can be verified by considering binary subtraction: when subtracting a larger number from a smaller number, a borrow propagates through the most significant bits, clearing the final carry.

#### 2.4 Overflow Flag (V) - Bit 28

The Overflow flag (V) indicates when a signed arithmetic operation produces a result that cannot be correctly represented in 32-bit two's complement representation. This occurs when the mathematical sum or difference exceeds the range [−2^31, 2^31 − 1].

**Theorem 2.2: V Flag Detection**
For signed addition (Rn + Operand), V is set if and only if:

- Rn and Operand have the same sign bit, AND
- The result has a different sign bit than Rn (and Operand)

For signed subtraction (Rn − Operand), which ARM implements as Rn + (−Operand), the same logic applies using two's complement negation.

**Proof of V Flag in Addition:**
Let a and b be signed 32-bit integers. Define s = a + b. The addition overflows (in signed arithmetic) when:

- a ≥ 0 and b ≥ 0 but s < 0 (positive + positive = negative)
- a < 0 and b < 0 but s ≥ 0 (negative + negative = non-negative)

In terms of bit operations, overflow occurs when bit[31] of a equals bit[31] of b, but bit[31] of s differs from bit[31] of a. The ARM processor implements this using exclusive-or operations: V = (a[31] ⊕ b[31]) · (a[31] ⊕ s[31]).

#### 2.5 Sticky Q Flag (Q) - Bit 27

The Q flag is a sticky overflow flag specific to Digital Signal Processing (DSP) operations in ARMv5TE and subsequent architectures. Unlike the condition flags that update with every arithmetic operation, the Q flag operates as a latched overflow indicator: once set due to saturation in a multiply-accumulate (MLA) or similar DSP instruction, it remains set until explicitly cleared by software writing 0 to bit[27].

### 3. Processor Control Bits

#### 3.1 Interrupt Disable Bits (I and F)

Bits 7 and 6 of the CPSR provide global control over interrupt handling:

- **I bit (IRQ disable)**: When set to 1, the processor masks all IRQ (Interrupt Request) exceptions. IRQ interrupts are typically used for general-purpose peripherals and timer interrupts in embedded systems.
- **F bit (FIQ disable)**: When set to 1, the processor masks all FIQ (Fast Interrupt Request) exceptions. FIQ is reserved for high-priority, low-latency interrupt handling.

**Theorem 3.1: Interrupt Priority**
Since FIQ has higher priority than IRQ in ARM architecture, the F bit must be cleared (F = 0) to enable FIQ interrupts, regardless of the I bit state. Conversely, to enable IRQ interrupts, both I = 0 and F = 0 must hold.

#### 3.2 State Bit (T) - Bit 5

The T bit indicates the current instruction set state:

- T = 0: ARM instruction set (32-bit)
- T = 1: Thumb instruction set (16-bit)

Switching between ARM and Thumb states occurs through branch instructions (BX, BLX) or by modifying the T bit directly via the CPSR during mode transitions.

#### 3.3 Mode Field (M[4:0]) - Bits 4-0

The 5-bit mode field encodes the processor's current privilege and execution mode:

| M[4:0] | Mode       | Privilege Level | Description                                        |
| ------ | ---------- | --------------- | -------------------------------------------------- |
| 10000  | User       | PL0             | Unprivileged mode, standard program execution      |
| 10001  | FIQ        | PL1             | Fast Interrupt Request, dedicated R8-R12 registers |
| 10010  | IRQ        | PL1             | Interrupt Request, standard interrupt handling     |
| 10011  | Supervisor | PL1             | Software interrupt (SWI) mode, OS kernel access    |
| 10111  | Abort      | PL1             | Memory access fault handling                       |
| 11011  | Undefined  | PL1             | Instruction fetch fault handling                   |
| 11111  | System     | PL1             | Privileged User mode, full register access         |

**Theorem 3.2: CPSR Accessibility**
In User mode (PL0), software can read the CPSR but cannot modify most fields except through specific instructions like CPS. In privileged modes (PL1), the full CPSR is both readable and writable, enabling exception handling and mode transitions.

### 4. Saved Program Status Register (SPSR)

The SPSR (Saved Program Status Register) serves as a shadow register that preserves the CPSR state during exception handling. When an exception occurs in ARM architecture, the processor automatically saves the current CPSR to the SPSR corresponding to the target exception mode before switching to the exception mode and entering the exception vector.

**Theorem 4.1: Exception Return Mechanism**
To return from an exception handler, the instruction `MOVS PC, LR` (or `SUBS PC, LR, #4` for certain exceptions) restores the CPSR from the SPSR, thereby restoring the pre-exception processor state including flags, mode, and instruction set state.

### 5. CPSR Access Instructions

ARM provides two primary instructions for accessing the CPSR:

- **MRS (Move from Status Register)**: Transfers CPSR contents to a general-purpose register

  ```assembly
  MRS R0, CPSR    ; Read CPSR into R0
  ```

- **MSR (Move to Status Register)**: Transfers register contents to CPSR
  ```assembly
  MSR CPSR_f, R0  ; Write to flag bits only (N,Z,C,V,Q)
  MSR CPSR_c, R0  ; Write to control bits (I,F,T,M)
  MSR CPSR_cxsf, R0 ; Write to all CPSR fields
  ```

### 6. Conditional Execution in ARM

One of the most distinctive features of ARM architecture is that most instructions can execute conditionally based on the state of the condition flags in CPSR. The condition field occupies bits 31-28 of every instruction, enabling the processor to conditionally execute an instruction without branch prediction penalties.

**Theorem 6.1: Conditional Execution Validity**
An instruction with condition code XN (where N indicates the flag state) executes if and only if the corresponding condition is satisfied:

- EQ (Equal): Z = 1
- NE (Not Equal): Z = 0
- CS/HS (Carry Set/Unsigned Higher or Same): C = 1
- CC/LO (Carry Clear/Unsigned Lower): C = 0
- MI (Minus/Negative): N = 1
- PL (Plus/Positive or Zero): N = 0
- VS (Overflow Set): V = 1
- VC (Overflow Clear): V = 0
- HI (Unsigned Higher): C = 1 AND Z = 0
- LS (Unsigned Lower or Same): C = 0 OR Z = 1
- GE (Signed Greater or Equal): N == V
- LT (Signed Less Than): N != V
- GT (Signed Greater Than): Z = 0 AND (N == V)
- LE (Signed Less or Equal): Z = 1 OR (N != V)

**Example 6.1: Conditional Execution Application**

```assembly
    CMP R0, R1      ; Compare R0 and R1, update flags
    ADDGT R2, R3, R4 ; If R0 > R1 (signed), then R2 = R3 + R4
    SUBLE R5, R6, R7 ; If R0 ≤ R1 (signed), then R5 = R6 - R7
```

## Summary

The Current Program Status Register (CPSR) serves as the central control unit in ARM processors, integrating condition flags (N, Z, C, V, Q), interrupt management (I, F), instruction set state (T), and processor mode (M) into a unified 32-bit register. Understanding CPSR is essential for embedded systems programming, exception handling, and optimizing code through conditional execution. The interplay between CPSR and SPSR during exception handling ensures seamless transitions between privileged and user modes while preserving processor state.

## Assessment

### Multiple Choice Questions

1. **Question 1**: An ARM processor executes the instruction `CMP R0, #0x80000000`. After execution, which of the following statements is TRUE regarding the CPSR flags? (Assume R0 contained 0x7FFFFFFF before the comparison)

   a) N = 1, Z = 0, C = 1, V = 1  
   b) N = 0, Z = 0, C = 1, V = 1  
   c) N = 1, Z = 0, C = 0, V = 0  
   d) N = 0, Z = 0, C = 0, V = 1

   **Answer**: (a)  
   **Explanation**: The comparison computes 0x7FFFFFFF - 0x80000000 = -1 (0xFFFFFFFF). Since the result is negative, N = 1. The result is non-zero, so Z = 0. In unsigned arithmetic, 0x7FFFFFFF < 0x80000000, so a borrow occurs and C = 0. However, in signed arithmetic, -1 is a valid negative number representable in 32-bit two's complement, so V = 0. Wait - let us reconsider: actually, subtracting 0x80000000 (the most negative signed value) from 0x7FFFFFFF causes signed overflow. The correct analysis: Mathematically, 0x7FFFFFFF - 0x80000000 = -2147483649, which is less than the minimum 32-bit signed value (-2147483648). Thus signed overflow occurs, setting V = 1. For C flag in subtraction: since 0x80000000 > 0x7FFFFFFF (unsigned), borrow is required, so C = 0. Therefore N = 1 (sign bit of 0xFFFFFFFF), Z = 0, C = 0, V = 1. The correct answer is actually (d).

2. **Question 2**: The CPSR of an ARM processor has the value `0x60000010`. Which of the following statements is INCORRECT?

   a) The processor is currently in User mode  
   b) Both IRQ and FIQ interrupts are enabled  
   c) The processor is in ARM state (not Thumb)  
   d) The N and Z flags are both clear

   **Answer**: (b)  
   **Explanation**: Analyzing CPSR = 0x60000010:
   - Bits 4-0 = 0x10 (10000b) = User mode ✓
   - Bit 5 (T) = 0 → ARM state ✓
   - Bit 7 (I) = 0 → IRQ enabled
   - Bit 6 (F) = 0 → FIQ enabled
   - Bit 31 (N) = 0, Bit 30 (Z) = 0 ✓

   Statement (b) is INCORRECT because both I = 0 and F = 0, meaning both IRQ and FIQ interrupts are ENABLED, not disabled. The statement says they are enabled, but the question asks which is INCORRECT. Actually re-reading: statement (b) says "both IRQ and FIQ interrupts are enabled" - this is TRUE based on the CPSR value. Let me reconsider: the CPSR value is 0x60000010. In binary: 0110 0000 0000 0000 0000 0000 0001 0000. Bit 7 = 0 (IRQ enabled), Bit 6 = 0 (FIQ enabled). So statement (b) saying they are enabled is actually CORRECT. Let me re-analyze: wait, I need to check - the question asks for INCORRECT statement. Let me look again at the CPSR: 0x60000010 = bits 31-28 = 0110 = N=0, Z=0, C=1, V=0. Actually wait - 0x6 in bits 31-28 is 0110 in binary: bit 31=0 (N), bit 30=1 (Z), bit 29=1 (C), bit 28=0 (V). So N=0, Z=1. Statement (d) says "The N and Z flags are both clear" - this is FALSE because Z is set. So (d) is INCORRECT.

3. **Question 3**: In ARM processor exception handling, which register holds the CPSR value when an exception is taken?

   a) CPSR is overwritten and cannot be recovered  
   b) The SPSR of the exception mode  
   c) The Link Register (LR)  
   d) The Stack Pointer (SP)

   **Answer**: (b)  
   **Explanation**: When an exception occurs, the ARM processor automatically copies the current CPSR to the SPSR (Saved Program Status Register) of the target exception mode before switching to that mode. This allows the exception handler to restore the original processor state upon return using the `MOVS PC, LR` or equivalent instruction.

### Numerical Problems

**Problem 1**: Given the following ARM assembly code snippet, determine the state of N, Z, C, and V flags after each instruction:

```assembly
    MOVS R0, #0xFFFFFFFF
    ADDS R1, R0, #1
```

**Solution**:

- After `MOVS R0, #0xFFFFFFFF`: This loads 0xFFFFFFFF into R0. The S suffix updates flags: N = 1 (MSB is 1), Z = 0, C = 0 (no carry out), V = 0.
- After `ADDS R1, R0, #1`: Computing 0xFFFFFFFF + 1 = 0x100000000. In 32-bit representation, this wraps to 0x00000000.
  - Result = 0x00000000, so Z = 1, N = 0
  - Carry out from bit[31] occurred (the 33rd bit), so C = 1
  - No signed overflow: adding 0xFFFFFFFF (-1) and 1 gives 0, which is representable, so V = 0.

**Final state**: N=0, Z=1, C=1, V=0.

**Problem 2**: A processor is in Supervisor mode with CPSR = 0xD3 (0b11010011). Determine:
(a) The current processor mode  
(b) State of interrupt enables  
(c) Instruction set state  
(d) Condition flag values

**Solution**:

- CPSR = 0xD3 = 0b11010011
- Bits 4-0 = 10011 (0x13) = Supervisor mode
- Bit 5 (T) = 1? No, bit 5 = 0 (bit 5 is the 6th bit from LSB): 0xD3 = 11010011, bit 5 = 0 → ARM state
- Bit 7 (I) = 1 → IRQ disabled
- Bit 6 (F) = 1 → FIQ disabled
- Bits 31-28 = 1101 = N=1, Z=0, C=1, V=0
