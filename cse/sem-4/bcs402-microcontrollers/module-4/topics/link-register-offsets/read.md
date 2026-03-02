# Link Register Offsets in ARM Cortex-M Microcontrollers

## Table of Contents

- [Link Register Offsets in ARM Cortex-M Microcontrollers](#link-register-offsets-in-arm-cortex-m-microcontrollers)
- [Introduction](#introduction)
- [Theoretical Foundation](#theoretical-foundation)
  - [The Link Register Architecture](#the-link-register-architecture)
  - [Exception Handling and EXC_RETURN Mechanism](#exception-handling-and-excreturn-mechanism)
- [EXC_RETURN Bit-Field Analysis](#excreturn-bit-field-analysis)
  - [Standard EXC_RETURN Values](#standard-excreturn-values)
- [Stack Frame Layouts and Offset Calculations](#stack-frame-layouts-and-offset-calculations)
  - [Basic Stack Frame](#basic-stack-frame)
  - [Extended Stack Frame with Floating-Point](#extended-stack-frame-with-floating-point)
- [Nested Interrupt Handling Analysis](#nested-interrupt-handling-analysis)
- [Offset Calculation Problems](#offset-calculation-problems)
- [Conclusion](#conclusion)

## Introduction

The Link Register (LR), designated as R14 in the ARM processor architecture, constitutes a fundamental mechanism for subroutine return address management and exception handling in ARM Cortex-M microcontrollers. Understanding the Link Register and its associated offset values is indispensable for embedded systems developers engaged in writing efficient, reliable firmware for resource-constrained microcontroller applications. The LR stores the return address whenever a function call is executed using the Branch with Link (BL) instruction, or when an exception interrupts normal program execution. The concept of "link register offsets" assumes particular significance when implementing exception return mechanisms, stack frame manipulation, nested interrupt handling, and operating system context switching in ARM Cortex-M based embedded systems.

This document provides a comprehensive treatment of the Link Register, EXC_RETURN value encoding, stack frame layouts, and the mathematical relationships governing offset calculations in ARM Cortex-M processors. The material is structured to equip students with both theoretical understanding and practical analytical skills required for embedded systems development.

## Theoretical Foundation

### The Link Register Architecture

In the ARM Procedure Call Standard (AAPCS), the Link Register serves as the repository for return addresses during subroutine calls. When the processor executes a Branch with Link (BL) instruction, the address of the instruction immediately following the BL is automatically stored into the LR (R14). This mechanism enables the called subroutine to return control to the correct location using either the MOV PC, LR instruction or POP {..., PC} instruction, which loads the PC with the stored return address.

**Theorem 1: LR Preservation in Function Calls**

_Proof_: Consider a function call sequence where the caller executes BL subroutine. The ARM architecture guarantees that the processor automatically stores (PC + 4) into LR, where PC is the address of the BL instruction itself. This occurs because the PC is already incremented by 4 (or 2 in Thumb mode) during instruction decode. Therefore, for a BL instruction at address A, the LR receives the return address A + 4. The called function may either use LR directly for return or push LR onto the stack for nested calls, preserving the return address through additional function nesting levels.

**Corollary**: When implementing nested function calls, the callee must preserve LR by pushing it onto the stack (PUSH {LR}) and popping it back before returning (POP {PC}), otherwise the original return address is lost when the callee overwrites LR with its own return address.

### Exception Handling and EXC_RETURN Mechanism

In ARM Cortex-M processors, the LR serves a critical dual function during exception handling. Upon exception entry, the processor automatically loads the LR with a special 32-bit pattern known as the EXC_RETURN value. This value encodes essential information about the processor state that must be restored upon exception return, including the execution mode, stack pointer selection, and floating-point state presence.

The EXC_RETURN mechanism operates on the fundamental principle that valid return addresses in ARM Thumb mode have bit[0] set to 1 (indicating Thumb state). The processor distinguishes exception returns from normal function returns by detecting the pattern 0xFFFFFFxx in the LR, where the upper 24 bits are all set to 1. When the processor executes an instruction that loads PC from LR and detects this pattern, it initiates the exception return sequence rather than a standard branch.

## EXC_RETURN Bit-Field Analysis

The EXC_RETURN value is a 32-bit pattern with specific bit positions encoding distinct aspects of the pre-exception processor state. The complete bit-field breakdown is presented in Table 1.

**Table 1: EXC_RETURN Bit-Field Definition**

| Bits    | Field Name | Description                     | Values                                                |
| ------- | ---------- | ------------------------------- | ----------------------------------------------------- |
| [31:28] | Reserved   | Must be 0xF                     | 0xF                                                   |
| [7:6]   | Reserved   | Must be 0x3                     | 0x3                                                   |
| [5]     | DCRS       | Default Current Instruction Set | 0 = Return to ARM state, 1 = Return to Thumb state    |
| [4]     | S          | Stack Frame Type                | 0 = Extended frame with FP registers, 1 = Basic frame |
| [3]     | Mode       | Execution Mode                  | 0 = Return to Handler mode, 1 = Return to Thread mode |
| [2]     | SPSEL      | Stack Pointer Selection         | 0 = Return using MSP, 1 = Return using PSP            |
| [1]     | Reserved   | Must be 1                       | 1                                                     |
| [0]     | ES         | Exception Secure                | 0 = Secure exception, 1 = Non-secure exception        |

**Theorem 2: EXC_RETURN Value Derivation**

_Proof_: The valid EXC_RETURN values are constructed by setting the required bits according to Table 1 while maintaining the constraint that bits [31:28] = 0xF and bits [7:6] = 0x3. For the standard non-secure Thumb state return (bit[5]=1, bit[1]=1, bit[0]=1), the derivation yields:

```
EXC_RETURN = 0xF0000000 + 0x0C000000 + 0x02000000 + (S << 4) + (Mode << 3) + (SPSEL << 2) + 0x02 + 0x01
 = 0xFF000000 + (S << 4) + (Mode << 3) + (SPSEL << 2) + 0x03
```

For basic frame (S=1), Thread mode (Mode=1), MSP (SPSEL=0):
0xFF000000 + 0x10 + 0x08 + 0x00 + 0x03 = 0xFFFFFFF9

For basic frame (S=1), Thread mode (Mode=1), PSP (SPSEL=1):
0xFF000000 + 0x10 + 0x08 + 0x04 + 0x03 = 0xFFFFFFFD

This derivation confirms the standard EXC_RETURN values used in practice.

### Standard EXC_RETURN Values

The four primary EXC_RETURN values used in Cortex-M processors are:

**0xFFFFFFF1 (Return to Handler mode using MSP)**

- Binary: 1111 1111 1111 1111 1111 1111 1111 0001
- Interpretation: Return to Handler mode (bit[3]=0), use MSP (bit[2]=0), basic stack frame (bit[4]=1), non-secure (bit[0]=1)
- Application: Used when returning from exception handlers (IRQ, SysTick, or fault handlers)

**0xFFFFFFF9 (Return to Thread mode using MSP)**

- Binary: 1111 1111 1111 1111 1111 1111 1111 1001
- Interpretation: Return to Thread mode (bit[3]=1), use MSP (bit[2]=0), basic stack frame (bit[4]=1), non-secure (bit[0]=1)
- Application: Standard return from exception to main program execution using main stack

**0xFFFFFFFD (Return to Thread mode using PSP)**

- Binary: 1111 1111 1111 1111 1111 1111 1111 1101
- Interpretation: Return to Thread mode (bit[3]=1), use PSP (bit[2]=1), basic stack frame (bit[4]=1), non-secure (bit[0]=1)
- Application: Return to Thread mode when process stack pointer was in use (RTOS applications)

**0xFFFFFFFA (Return to Thread mode using PSP, Handler stack frame)**

- Binary: 1111 1111 1111 1111 1111 1111 1111 1010
- Interpretation: Return to Thread mode (bit[3]=1), use PSP (bit[2]=1), basic stack frame (bit[4]=1), bit[1]=0 indicates exception taken from Handler mode
- Application: Returning from a nested exception where outer exception was in Handler mode

Extended EXC_RETURN values (with bit[4]=0) indicate floating-point state frames:

- 0xFFFFFFE1: Handler mode, MSP, with FP frame
- 0xFFFFFFE9: Thread mode, MSP, with FP frame
- 0xFFFFFFED: Thread mode, PSP, with FP frame

## Stack Frame Layouts and Offset Calculations

### Basic Stack Frame

When an exception occurs in ARM Cortex-M processors, the processor automatically pushes an 8-register stack frame onto the current stack. This frame is pushed atomically by hardware and contains all registers necessary for exception handler execution and subsequent return to interrupted code.

**Table 2: Basic Stack Frame Layout**

| Offset from SP | Register            | Size    |
| -------------- | ------------------- | ------- |
| +0             | R0                  | 4 bytes |
| +4             | R1                  | 4 bytes |
| +8             | R2                  | 4 bytes |
| +12            | R3                  | 4 bytes |
| +16            | R12                 | 4 bytes |
| +20            | LR (Return Address) | 4 bytes |
| +24            | PC (Return address) | 4 bytes |
| +28            | xPSR                | 4 bytes |

**Total Basic Stack Frame Size: 32 bytes (8 registers × 4 bytes)**

**Theorem 3: LR Offset Verification**

_Proof_: The ARM Cortex-M exception entry sequence pushes registers onto the stack in a specific order: PUSH {R0-R3, R12, LR, PC, xPSR}. Since each register is 32 bits (4 bytes), the stacking order determines their offsets. R0 is pushed first at offset 0, followed by R1 at offset 4, R2 at offset 8, R3 at offset 12, R12 at offset 16, and LR at offset 20. Therefore, the LR is always located at stack pointer offset +20 bytes from the value of SP at the start of the exception entry sequence.

**Corollary**: When manually unwinding a stack or implementing custom exception handling, the return address stored in the stack frame at offset +24 (the saved PC) represents the address of the instruction that was executing when the exception occurred, plus 4 for Thumb mode (indicating the next instruction to execute).

### Extended Stack Frame with Floating-Point

When the processor includes floating-point unit support (Cortex-M4, Cortex-M7, Cortex-M33 with FPU) and lazy stacking is disabled, an extended stack frame is created that includes the floating-point registers. The extended frame contains an additional 16 S-registers (S0-S15), FPSCR, and reserved space.

**Table 3: Extended Stack Frame Layout (with FPU)**

| Offset from Original SP | Register | Size     |
| ----------------------- | -------- | -------- |
| +0 to +60               | S0-S15   | 64 bytes |
| +64                     | FPSCR    | 4 bytes  |
| +68 to +71              | Reserved | 4 bytes  |
| +72                     | R0       | 4 bytes  |
| +76                     | R1       | 4 bytes  |
| +80                     | R2       | 4 bytes  |
| +84                     | R3       | 4 bytes  |
| +88                     | R12      | 4 bytes  |
| +92                     | LR       | 4 bytes  |
| +96                     | PC       | 4 bytes  |
| +100                    | xPSR     | 4 bytes  |

**Total Extended Stack Frame Size: 104 bytes**

**Note**: When lazy stacking is enabled (default configuration), the processor reserves space for the floating-point frame but defers saving S0-S15 until the exception handler actually accesses them, thereby reducing interrupt latency.

## Nested Interrupt Handling Analysis

Understanding LR manipulation is essential for implementing nested interrupt handling in embedded systems. Consider the following analysis of nested exception scenarios:

**Example 1: Nested IRQ Handler**

When a higher-priority interrupt preempts a lower-priority interrupt handler, the LR value changes to reflect the new exception context:

1. Initial state: Thread mode, executing main program (LR = return address)
2. Exception entry (Timer IRQ): LR → 0xFFFFFFF9 (Handler mode, MSP)
3. Within Timer IRQ handler, another IRQ (UART IRQ) preempts:

- Processor pushes another stack frame
- LR → 0xFFFFFFF1 (nested Handler mode return)

4. UART IRQ completes: EXC_RETURN 0xFFFFFFF1 used to return to Timer IRQ
5. Timer IRQ completes: EXC_RETURN 0xFFFFFFF9 used to return to main

**Theorem 4: Stack Pointer Selection Proof**

_Proof_: The processor uses the stack pointer indicated by bit[2] of EXC_RETURN to determine which stack to pop from during exception return. When SPSEL (bit[2]) = 0, the Main Stack Pointer (MSP) is used. When SPSEL = 1, the Process Stack Pointer (PSP) is used. The selection occurs because the processor reads the EXC_RETURN value before initiating the return sequence and configures the stack pointer accordingly. In multi-threaded applications using an RTOS, Thread mode typically uses PSP for task stacks while the kernel uses MSP, allowing clean isolation between task contexts.

## Offset Calculation Problems

**Problem 1**: Given a Cortex-M4 processor with lazy stacking disabled and an exception taken from Thread mode using PSP, determine the EXC_RETURN value and verify that the saved LR is located at offset +92 in the extended stack frame.

_Solution_: Thread mode (bit[3]=1), PSP (bit[2]=1), Extended frame (bit[4]=0), Non-secure (bit[0]=1):
EXC_RETURN = 0xF0000000 + 0x0C000000 + 0x02000000 + 0x00 + 0x08 + 0x04 + 0x02 + 0x01 = 0xFFFFFFED

For extended frame: Base offset for standard registers = 72 bytes (S0-S15 + FPSCR + reserved)
LR offset = 72 + 20 = 92 bytes ✓

**Problem 2**: An embedded system developer examines a stack dump and finds the value 0xFFFFFFE9 at the LR location in the stack frame. Analyze the processor state and determine which registers were automatically saved.

_Solution_: 0xFFFFFFE9:

- Bits [31:28] = 0xF (valid EXC_RETURN)
- Bit[4] = 0 (Extended frame with FPU registers)
- Bit[3] = 1 (Return to Thread mode)
- Bit[2] = 0 (Return using MSP)
- Bit[0] = 1 (Non-secure)

This indicates Thread mode return using MSP with floating-point state frame present. The stack frame contains S0-S15, FPSCR, R0-R3, R12, LR, PC, xPSR (104 bytes total).

## Conclusion

The Link Register and EXC_RETURN mechanism in ARM Cortex-M processors provide a sophisticated framework for managing exception returns and maintaining processor state across interrupts. The structured bit-field encoding of EXC_RETURN values enables precise reconstruction of pre-exception contexts, while the standardized stack frame layouts facilitate reliable stack unwinding and debugging. Mastery of these concepts is essential for developing robust embedded systems with proper interrupt handling, RTOS integration, and fault tolerance.
