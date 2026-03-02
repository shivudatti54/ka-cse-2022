# Registers in ARM Embedded Systems

## Table of Contents

- [Registers in ARM Embedded Systems](#registers-in-arm-embedded-systems)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [General-Purpose Registers (R0-R12)](#general-purpose-registers-r0-r12)
  - [Stack Pointer (SP) - R13](#stack-pointer-sp---r13)
  - [Link Register (LR) - R14](#link-register-lr---r14)
  - [Program Counter (PC) - R15](#program-counter-pc---r15)
  - [Current Program Status Register (CPSR)](#current-program-status-register-cpsr)
  - [Saved Program Status Register (SPSR)](#saved-program-status-register-spsr)
  - [Banked Registers and Processor Modes](#banked-registers-and-processor-modes)
- [Examples](#examples)
  - [Example 1: Function Call Register Usage](#example-1-function-call-register-usage)
  - [Example 2: Interrupt Handling with Banked Registers](#example-2-interrupt-handling-with-banked-registers)
  - [Example 3: Analyzing CPSR Flag Usage](#example-3-analyzing-cpsr-flag-usage)
- [Exam Tips](#exam-tips)

## Introduction

The register architecture of ARM processors represents a fundamental aspect of the RISC design philosophy, emphasizing simplicity, regularity, and efficiency in instruction execution. ARM (Advanced RISC Machines) processors utilize a register-based instruction set where most operations occur between registers, minimizing memory access and maximizing pipeline efficiency. The ARM architecture defines a comprehensive register set comprising 37 registers in the ARMv7 architecture, each serving specific roles in program execution, mode transitions, and state management.

Understanding ARM registers is essential for embedded systems programming because registers are the primary means of data manipulation, function calling, and interrupt handling. Unlike complex instruction set computers (CISC) architectures that include numerous special-purpose registers with restricted functionality, ARM provides a uniform register file with consistent 32-bit widths, enabling predictable instruction timing and efficient compiler optimization. The register organization also incorporates banked registers that provide separate register sets for different processor modes, enabling fast context switching without memory access penalties.

## Key Concepts

### General-Purpose Registers (R0-R12)

The ARM processor includes thirteen general-purpose registers designated R0 through R12. Each register is a 32-bit wide register capable of holding unsigned or signed integers, addresses, and floating-point values when used with appropriate coprocessors. These registers are accessible in all processor modes, though different modes may access different physical instances through the banking mechanism.

The conventional usage of general-purpose registers follows the ARM Architecture Procedure Call Standard (AAPCS), which defines a standard convention for function calls. R0-R3 are used to pass arguments to functions and return values, with additional arguments passed on the stack. R4-R11 typically hold local variables within functions, with R11 serving as the frame pointer in debugging. R12 (also known as IP or Intra-Procedure Call) acts as a temporary register for function call mechanics. Register R0 additionally holds the return value for functions returning 32-bit or smaller values.

### Stack Pointer (SP) - R13

The Stack Pointer, accessible as both SP and R13, is a dedicated register that points to the current top of the stack in memory. The ARM architecture maintains separate banked Stack Pointers for different processor modes: the Main Stack Pointer (MSP) serves the main execution context and exception handlers, while the Process Stack Pointer (PSP) is available in Thread mode for user applications. This separation is particularly valuable in embedded systems using real-time operating systems (RTOS) where kernel and user stacks must be isolated for security and stability.

The Stack Pointer must be aligned to a word boundary (4-byte alignment) in ARM state, with certain instructions enforcing stricter alignment requirements. Incorrect stack pointer alignment can lead to unpredictable behavior or memory access exceptions. In Thumb state, the Stack Pointer requires only halfword alignment, reflecting the reduced instruction width.

### Link Register (LR) - R14

The Link Register, also known as LR or R14, stores the return address when a subroutine call is executed using branch-with-link instructions (BL or BLX). When a function is called, the processor automatically saves the address of the instruction following the branch in LR, enabling the called function to return execution to the correct location using the MOV PC, LR or POP {PC} instructions. This mechanism eliminates the need for manual return address management, simplifying function call implementation and reducing code size.

During exception handling, the LR holds a special return value that indicates the required processor state and return address. For instance, in IRQ exception mode, LR contains the address to return to plus 4, accounting for the pipeline behavior where the PC has advanced beyond the interrupted instruction. The processor automatically copies the CPSR to the SPSR and loads the exception vector address into the PC.

### Program Counter (PC) - R15

The Program Counter, designated PC or R15, holds the address of the next instruction to be executed. In ARM state, the PC is always word-aligned, with bits[1:0] read as zero and bits[31:2] containing the address. In Thumb state, the PC is halfword-aligned, with bit[0] read as zero and bits[31:1] containing the address. This alignment reflects the variable-length nature of Thumb instructions.

The PC participates directly in instruction execution through the pipeline mechanism. In ARM's three-stage pipeline, the PC points to the instruction being fetched while the previously fetched instruction is being decoded, and the instruction before that is being executed. Consequently, reading the PC in ARM state yields the address of the current instruction plus 8 (or plus 4 in Thumb state), a detail that must be considered when calculating branch offsets or examining program counter values.

### Current Program Status Register (CPSR)

The Current Program Status Register is a critical 32-bit register that contains condition flags, processor mode bits, and state control information. The CPSR flags (bits[31:28]) include the Negative (N), Zero (Z), Carry (C), and Overflow (V) flags, which reflect the results of arithmetic and logical operations and control conditional execution throughout the instruction set. The N flag sets when a result is negative, the Z flag sets when a result is zero, the C flag carries from addition or borrows from subtraction, and the V flag indicates signed overflow.

The processor mode bits (bits[4:0]) select between User, FIQ, IRQ, Supervisor, Abort, Undefined, and System modes, determining which register bank is active and what privileges are available. The T bit (bit[5]) indicates whether the processor is in ARM state (T=0) or Thumb state (T=1), while the J bit (bit[24]) indicates Jazelle state for Java bytecode execution in ARMv6 and later. The interrupts disable bits I (bit[7]) and F (bit[6]) control IRQ and FIQ masking respectively.

### Saved Program Status Register (SPSR)

The Saved Program Status Register (SPSR) preserves the CPSR value when an exception occurs, allowing the processor state to be fully restored upon returning from the exception handler. Each exception mode (FIQ, IRQ, Supervisor, Abort, Undefined) has its own SPSR instance that is automatically loaded when entering the exception and restored when exiting. User and System modes do not have SPSR since these modes cannot be entered via exception.

The SPSR structure mirrors the CPSR, containing the same flag bits, mode bits, and state control bits. Exception handlers typically save the SPSR value on the stack if they need to perform nested exception handling, as subsequent exceptions will overwrite the current SPSR contents. The instruction to restore the CPSR from SPSR (MRS CPSR_c, SPSR or CPSR_svc, SPSR, depending on syntax) is a privileged operation.

### Banked Registers and Processor Modes

The ARM architecture implements register banking to provide fast, zero-overhead context switching between processor modes. When the processor enters an exception or privileged mode, a different set of registers becomes accessible without requiring explicit save and restore operations. Banked registers are physically separate registers that are mapped to the same logical register numbers when in their designated mode.

In User and System modes, the banked registers include R13 (SP) and R14 (LR), while FIQ mode provides banked versions of R8-R12, R13 (SP), and R14 (LR) in addition to its own SPSR. IRQ mode banks R13 and R14 along with the SPSR. Supervisor, Abort, and Undefined modes each bank R13, R14, and SPSR. This organization enables efficient interrupt handling where the processor can immediately begin using fresh registers without first preserving the interrupted program's state.

The following table summarizes banked registers by processor mode:

| Mode        | Banked Registers                         |
| ----------- | ---------------------------------------- |
| User/System | None (R13, R14 are same as in all modes) |
| FIQ         | R8-R12, R13 (SP), R14 (LR), SPSR_fiq     |
| IRQ         | R13 (SP), R14 (LR), SPSR_irq             |
| Supervisor  | R13 (SP), R14 (LR), SPSR_svc             |
| Abort       | R13 (SP), R14 (LR), SPSR_abt             |
| Undefined   | R13 (SP), R14 (LR), SPSR_und             |

## Examples

### Example 1: Function Call Register Usage

Consider a C function call in ARM assembly following AAPCS:

```assembly
; Calling function
MOV R0, #10 ; First argument = 10
MOV R1, #20 ; Second argument = 20
BL add_numbers ; Branch with link to function
; R0 now contains result (30)

; Called function
add_numbers:
ADD R0, R0, R1 ; R0 = R0 + R1 = 30
BX LR ; Return to caller
```

This example demonstrates the AAPCS convention where the first four arguments are passed in R0-R3, with the return value placed in R0. The BL instruction automatically saves the return address in LR, and the function returns by branching to LR.

### Example 2: Interrupt Handling with Banked Registers

When an IRQ interrupt occurs, the processor automatically:

1. Copies CPSR to SPSR_irq
2. Changes to IRQ mode
3. Disables IRQs (sets I bit)
4. Loads the IRQ vector address into PC
5. Saves the return address in LR_irq

The handler can then execute using banked registers R13_irq (stack pointer) and R14_irq without affecting the User mode registers:

```assembly
IRQ_Handler:
 PUSH {R0-R3, R12, LR} ; Save caller-saved registers
 ; Handler code uses banked R13_irq and R14_irq
 BL service_routine
 POP {R0-R3, R12, LR} ; Restore registers
 SUBS PC, LR, #4 ; Return and restore CPSR from SPSR
```

### Example 3: Analyzing CPSR Flag Usage

Given the ARM instruction sequence:

```assembly
MOVS R0, #0x80000000 ; N flag set, C unaffected (imm rotated)
ADDS R1, R0, R0 ; R1 = 0x100000000, C=1, V=1 (overflow)
ADCS R2, R1, R1 ; R2 = 0x200000000 with C, C=1, V=0
```

The S suffix on each instruction updates CPSR flags. The first MOVS sets the N flag because bit 31 of the result is set (negative in signed interpretation). The second ADDS demonstrates signed overflow: adding 0x80000000 to itself produces 0x100000000, which cannot fit in 32 bits, setting both C and V flags. The ADCS instruction adds with carry, propagating the carry bit.

## Exam Tips

1. **Remember register width**: All ARM registers in ARMv7 are 32-bit wide, with 64-bit support available through NEON or DSP extensions.

2. **AAPCS conventions are examinable**: Know that R0-R3 are argument/return registers, R4-R11 are callee-saved, R12 is temporary, SP is R13, LR is R14, and PC is R15.

3. **Understand banking overhead**: Banked registers provide zero-cost context switching for exceptions, but non-banked registers require explicit save/restore operations.

4. **CPSR flag conditions**: N=Negative, Z=Zero, C=Carry, V=Overflow. Remember which instructions affect which flags.

5. **Mode bit patterns**: Know the binary encoding for processor modes (e.g., 0b10011 = Supervisor, 0b10001 = IRQ, 0b10000 = User).

6. **Pipeline PC offset**: Reading PC in ARM state gives address+8 due to the 3-stage pipeline; in Thumb state it gives address+4.

7. **SPSR availability**: Remember that User and System modes lack SPSR since they cannot be entered via exception; attempting to access SPSR in these modes is undefined.
