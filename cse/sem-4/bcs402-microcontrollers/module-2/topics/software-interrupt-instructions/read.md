# Software Interrupt Instructions in Microcontrollers

## Table of Contents

- [Software Interrupt Instructions in Microcontrollers](#software-interrupt-instructions-in-microcontrollers)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Software Interrupt Mechanism](#software-interrupt-mechanism)
  - [ARM SWI Instruction](#arm-swi-instruction)
  - [Interrupt Enable/Disable Mechanisms](#interrupt-enabledisable-mechanisms)
  - [Return from Interrupt: RETI Instruction](#return-from-interrupt-reti-instruction)
  - [Stack Operations During Software Interrupt](#stack-operations-during-software-interrupt)
- [Examples](#examples)
  - [Example 1: 8051 Software Interrupt Service Routine for System Call](#example-1-8051-software-interrupt-service-routine-for-system-call)
  - [Example 2: Calculating Stack Pointer After Software Interrupt](#example-2-calculating-stack-pointer-after-software-interrupt)
  - [Example 3: ARM SWI for System Call Implementation](#example-3-arm-swi-for-system-call-implementation)
- [Exam Tips](#exam-tips)

## Introduction

Software interrupt instructions represent a fundamental mechanism in microcontroller architectures that allow software to deliberately invoke interrupt handling procedures. Unlike hardware interrupts which are triggered by external events or internal peripherals, software interrupts are explicitly initiated by program code through dedicated instructions. These instructions serve critical roles in implementing system calls, operating system kernels, debugging mechanisms, and context switching operations.

The fundamental distinction between software interrupts and subroutine calls lies in their execution context and hardware interaction. Subroutine calls (such as ACALL and LCALL in 8051) merely save the program counter on the stack and transfer control to a subroutine, whereas software interrupt instructions trigger a full interrupt response sequence that typically involves saving the program status word, switching to interrupt mode, and potentially modifying privilege levels. This comprehensive context saving enables nested interrupt handling and provides a secure mechanism for transitioning between user and privileged modes in more advanced architectures.

Software interrupts provide several advantages over traditional subroutine calls in embedded systems. They offer a standardized entry point for operating system services, enable controlled access to protected resources, facilitate debugging through breakpoint mechanisms, and allow for flexible implementation of exception handling. The vector-based dispatch mechanism used by software interrupts also simplifies the addition of new system services without modifying existing calling code.

## Key Concepts

### Software Interrupt Mechanism

The software interrupt mechanism in microcontrollers involves a precise sequence of hardware operations. When a software interrupt instruction is executed, the microcontroller completes the current instruction, saves critical state information onto the stack, loads the program counter with the interrupt vector address from the interrupt vector table, and switches to the appropriate processor mode. This sequence ensures that the interrupt service routine (ISR) executes in a well-defined environment with all necessary context information preserved.

In the 8051 microcontroller architecture, the TRAP interrupt (interrupt vector 0x0023) serves as the primary software-initiated interrupt mechanism. The TRAP interrupt is non-maskable at the individual enable level, meaning it cannot be disabled through the IE register, though it can be globally disabled by clearing the EA bit. The vector address 0x0023 represents the fixed location in program memory where the ISR for TRAP begins. Upon triggering, the 8051 automatically pushes the current program counter (both PC high and PC low bytes) onto the stack, followed by the program status word (PSW), before vectoring to the ISR.

The interrupt vector table in 8051 contains fixed addresses for all interrupt sources. The software interrupt (TRAP) vector at 0x0023 is located between external interrupt 1 (INT1 at 0x0013) and the serial port interrupt (0x0023). This fixed mapping allows predictable response times for software interrupt handling, which is critical in real-time embedded applications.

### ARM SWI Instruction

The ARM architecture provides the SWI (Software Interrupt) instruction as a primary mechanism for invoking operating system services. The SWI instruction is encoded as a 32-bit thumb instruction that triggers the Supervisor mode, causing the processor to branch to the SWI vector (address 0x00000008 in ARM state). The instruction format includes a 24-bit immediate field that can be used to pass a system call number or parameter to the operating system.

When an SWI instruction is executed, the ARM processor performs the following operations: it saves the address of the next instruction (the return address) in the Link Register (R14_svc), copies the current Program Status Register (CPSR) to the Saved Program Status Register (SPSR_svc), sets the CPSR to enter Supervisor mode with interrupts disabled, and branches to the SWI vector address. The operating system can then examine the SWI number encoded in the instruction to determine which service to provide.

The ARM SWI mechanism supports both privileged and unprivileged execution. User programs can execute SWI instructions to request privileged operations, with the operating system validating the request before performing the operation. This forms the basis for system call implementations in ARM-based operating systems.

### Interrupt Enable/Disable Mechanisms

Effective management of software interrupts requires understanding the interrupt enable/disable mechanisms. In the 8051 architecture, the Interrupt Enable (IE) register at address 0xA8 controls interrupt responsiveness. The IE register contains bits for enabling individual interrupt sources (EX0, ET0, EX1, ET1, ES) along with a global enable bit (EA). For software interrupts specifically, the EA bit must be set to enable any interrupt response, while the specific software interrupt enable bit (if available in the variant) must also be enabled.

The IE register bit structure is as follows: bit 7 (EA) enables or disables all interrupts globally, bit 6 is reserved, bit 5 (ET2) enables timer 2 overflow interrupt, bit 4 (ES) enables serial port interrupt, bit 3 (ET1) enables timer 1 overflow, bit 2 (EX1) enables external interrupt 1, bit 1 (ET0) enables timer 0 overflow, and bit 0 (EX0) enables external interrupt 0. Proper configuration of these bits is essential for predictable software interrupt behavior.

### Return from Interrupt: RETI Instruction

The Return from Interrupt (RETI) instruction is distinct from the Return (RET) instruction used for subroutines. In the 8051, RETI performs two critical operations: it restores the program counter from the stack (popping the two bytes pushed during interrupt entry), and it signals the interrupt hardware that the current interrupt service routine has completed. This second function is crucial because it allows the interrupt controller to recognize that nested interrupt handling can proceed.

The distinction between RET and RETI is particularly important in systems requiring nested interrupt handling. When RETI executes, the interrupt logic recognizes that the service routine has completed and can enable higher-priority interrupts that were blocked while the current ISR executed. Using RET instead of RETI would restore the program counter but would not inform the interrupt system of the ISR's completion, potentially causing the interrupt system to remain in a state where it believes an interrupt is still being serviced.

### Stack Operations During Software Interrupt

Understanding stack operations during software interrupt handling is essential for writing correct interrupt service routines and for analyzing interrupt latency. When a software interrupt is triggered in the 8051, the microcontroller automatically pushes the current PC value onto the stack (two bytes: PCL then PCH), followed by the PSW. This automatic push operation requires that the stack pointer be properly initialized before interrupts are enabled.

The total stack space required for a software interrupt entry is three bytes: two for the program counter and one for the PSW. If nested interrupts are used, each nested interrupt entry consumes an additional three bytes. For applications requiring deep nesting, careful calculation of stack requirements is necessary to prevent stack overflow. The stack pointer should be initialized to a value that provides sufficient space for the worst-case interrupt nesting scenario plus any local variables pushed by the ISR.

## Examples

### Example 1: 8051 Software Interrupt Service Routine for System Call

Consider implementing a system call mechanism using the 8051 TRAP interrupt. The system call number is passed in accumulator A, with the return value also returned in A.

```assembly
; Interrupt Vector Table
ORG 0000H
LJMP MAIN

ORG 0023H ; TRAP interrupt vector address
LJMP SWI_HANDLER

; Main program
ORG 0100H
MAIN:
 MOV SP, #30H ; Initialize stack pointer
 SETB EA ; Enable global interrupts
 MOV A, #01H ; System call number (e.g., READ)
 TRAP ; Invoke software interrupt

; System Call Handler
SWI_HANDLER:
 PUSH PSW ; Save additional registers needed
 PUSH ACC

 if ; Dispatch based on system call number in A
 CJNE A, #01H, CHECK_WRITE
 ; Handle READ system call
 LJMP SYSCALL_DONE

CHECK_WRITE:
 CJNE A, #02H, UNKNOWN_CALL
 ; Handle WRITE system call
 LJMP SYSCALL_DONE

UNKNOWN_CALL:
 ; Handle unknown system call

SYSCALL_DONE:
 POP ACC ; Restore registers
 POP PSW
 RETI ; Return from interrupt
```

This example demonstrates the proper structure of a software interrupt service routine, including saving additional registers beyond those automatically saved by hardware, dispatching based on parameters passed by the calling code, and using RETI to return to the interrupted program.

### Example 2: Calculating Stack Pointer After Software Interrupt

For an 8051 with stack pointer initialized to 0x40, analyze the stack pointer value after a TRAP interrupt is serviced and control returns to the calling program.

**Solution:**

Initial state:

- SP = 0x40 (indicates next byte will be stored at 0x40)

Upon TRAP execution:

1. Current PC is saved: PCH pushed to 0x40, then PCL pushed to 0x41
2. PSW is pushed to 0x42
3. SP is decremented after each push (8051 post-decrement behavior)
4. After hardware save: SP = 0x3F (pointing to next free location)

During ISR (assuming no additional pushes):

- SP remains at 0x3F during ISR execution

Upon RETI execution:

1. PSW is popped from 0x42, SP becomes 0x41
2. PC is popped (PCL from 0x41, PCH from 0x40), SP becomes 0x3F

After RETI completes, SP = 0x3F. However, upon returning to the main program, the stack should be at the same level as before the interrupt. The 8051 automatically handles the PC restoration, so the calling program continues with SP = 0x3F, which differs from the original 0x40 because the PSW was also pushed and remains on the stack until explicitly popped.

### Example 3: ARM SWI for System Call Implementation

Implementation of a simple system call using ARM SWI instruction:

```assembly
; ARM Assembly - System call to exit program
AREA |.text|, CODE, READONLY
ENTRY

; System call: exit with status code
; Linux ARM syscall: exit(int status)
; syscall number __NR_exit = 1

MOV R7, #1 ; Load syscall number for exit
MOV R0, #0 ; Exit status = 0
SWI 0x0 ; Invoke software interrupt

; Alternative: write syscall number embedded in SWI
WRITE_SVC:
 MOV R7, #4 ; __NR_write
 MOV R0, #1 ; file descriptor (stdout)
 LDR R1, =message
 MOV R2, #13 ; message length
 SWI 0x0

message DCB "Hello World!",0
END
```

This example demonstrates how the ARM SWI instruction provides a clean mechanism for invoking operating system services. The system call number is loaded into R7, with arguments in R0-R6, following the ARM EABI convention for system calls.

## Exam Tips

1. **Distinguish between ACALL/LCALL and true software interrupts**: ACALL and LCALL are subroutine calls that do not trigger interrupt handling sequences. True software interrupts (like TRAP in 8051 or SWI in ARM) save PSW, change processor mode, and may block further interrupts.

2. **Remember the TRAP vector address**: In 8051, the TRAP interrupt vector is at address 0x0023. This is a fixed location and must be memorized for exam questions.

3. **RETI versus RET**: Always use RETI for returning from interrupt service routines. Using RET instead of RETI will prevent proper nested interrupt handling and may cause undefined behavior in the interrupt system.

4. **Stack pointer initialization**: Before enabling interrupts, ensure the stack pointer is properly initialized. For 8051, a typical initialization is MOV SP, #30H or higher to avoid collision with register banks.

5. **IE register configuration**: The EA bit (bit 7 of IE register) must be set to enable any interrupt handling. Individual enable bits must also be set for specific interrupt sources.

6. **Software interrupt timing**: Software interrupt latency includes the time to complete the current instruction plus the hardware save sequence. This is typically 2-4 machine cycles depending on the architecture.

7. **Nested interrupt considerations**: When implementing nested interrupts, save all registers used by the ISR, enable interrupts after saving context, and use RETI to properly restore interrupt state.
