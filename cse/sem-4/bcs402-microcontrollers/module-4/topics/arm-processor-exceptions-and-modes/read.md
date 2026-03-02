# ARM Processor Exceptions and Modes

## Table of Contents

- [ARM Processor Exceptions and Modes](#arm-processor-exceptions-and-modes)
- [Introduction](#introduction)
- [ARM Processor Operational Modes](#arm-processor-operational-modes)
  - [User Mode (USR)](#user-mode-usr)
  - [Fast Interrupt Request Mode (FIQ)](#fast-interrupt-request-mode-fiq)
  - [Interrupt Request Mode (IRQ)](#interrupt-request-mode-irq)
  - [Supervisor Mode (SVC)](#supervisor-mode-svc)
  - [Abort Mode (ABT)](#abort-mode-abt)
  - [Undefined Mode (UND)](#undefined-mode-und)
  - [System Mode (SYS)](#system-mode-sys)
- [Exception Handling Mechanism](#exception-handling-mechanism)
  - [Exception Entry Sequence](#exception-entry-sequence)
  - [Exception Return Sequence](#exception-return-sequence)
- [Exception Vector Table](#exception-vector-table)
- [Exception Priority Scheme](#exception-priority-scheme)
- [Banked Registers in ARM Exception Handling](#banked-registers-in-arm-exception-handling)
- [Assessment Questions](#assessment-questions)
  - [Question 1: Exception Latency Calculation](#question-1-exception-latency-calculation)
  - [Question 2: Mode Transition Analysis](#question-2-mode-transition-analysis)
  - [Question 3: Vector Table Relocation Analysis](#question-3-vector-table-relocation-analysis)

## Introduction

The ARM (Advanced RISC Machines) processor architecture represents one of the most prevalent microprocessor architectures in contemporary embedded systems, mobile computing platforms, and microcontroller applications. The ARM architecture employs a sophisticated exception handling mechanism that enables the processor to respond to various interrupt requests, software exceptions, and hardware faults with predictable latency and minimal overhead. Understanding the intricacies of ARM processor exceptions and operational modes is fundamental for embedded systems developers, firmware engineers, and computer science professionals working with ARM-based microcontrollers.

Exceptions in the ARM architecture are defined as events that disrupt the sequential flow of program execution and necessitate special processing by the processor. When an exception condition is detected, the ARM processor automatically transitions from its current operational mode to a designated exception mode, preserving the processor state, elevating the privilege level, and vectoring execution to a predefined exception handler. This mechanism forms the cornerstone of interrupt-driven systems, real-time operating systems, and hardware abstraction layers in embedded software development.

This comprehensive analysis examines the seven operational modes defined in the ARM architecture, the detailed exception handling sequence including state preservation mechanisms, the exception vector table structure with precise memory addresses, and the priority scheme governing simultaneous exception handling. Furthermore, this document presents advanced-level assessment items that evaluate application-level understanding of exception latency calculations, mode transition analysis, and priority-based interrupt servicing scenarios.

## ARM Processor Operational Modes

The ARM architecture (specifically ARMv4 and subsequent versions) defines seven distinct operational modes, each serving specific functional purposes within the system. These modes are categorized into two primary classifications: privileged modes (six modes) and one non-privileged mode. The selection of operational mode is governed by bits [4:0] in the Current Program Status Register (CPSR), which encodes the processor mode field.

### User Mode (USR)

User Mode represents the standard unprivileged execution context for application programs. In this mode, the processor operates at Privilege Level 0 (PL0) and has restricted access to system resources. The CPSR register can be read but not directly modified to change modes; such transitions must be mediated through privileged modes using supervisor calls (SWI instructions). User Mode has access to a dedicated set of registers (R0-R12, PC, and CPSR) and cannot disable interrupts or access coprocessor system control registers. This mode implements the principle of least privilege, ensuring that user applications cannot compromise system stability or security.

### Fast Interrupt Request Mode (FIQ)

FIQ Mode is specifically engineered for high-priority, low-latency interrupt handling. When the processor enters FIQ mode due to an external fast interrupt request, it gains exclusive access to five banked registers (R8_fiq through R12_fiq) in addition to the standard banked registers (R13_fiq, R14_fiq, and SPSR_fiq). This banked register architecture eliminates the overhead of saving general-purpose registers during interrupt entry, thereby reducing interrupt latency significantly. The FIQ mode has its own dedicated stack pointer (R13_fiq) and link register (R14_fiq) for storing return addresses. In ARM architecture versions prior to ARMv4, FIQ could disable IRQ interrupts automatically while allowing nested FIQ handling.

### Interrupt Request Mode (IRQ)

IRQ Mode serves as the standard interrupt handling context for general-purpose interrupt requests. The IRQ interrupt has lower priority than FIQ and shares general-purpose registers with other exception modes, necessitating explicit register preservation in the interrupt service routine. When an IRQ exception is asserted, the processor saves the return address in R14_irq (the banked link register) and switches to IRQ mode, copying the CPSR to SPSR_irq. The IRQ mode provides a dedicated stack pointer (R13_irq) and link register, enabling nested interrupt handling when properly configured.

### Supervisor Mode (SVC)

Supervisor Mode, historically termed SWI Mode, is entered through the execution of a Software Interrupt (SWI) instruction or upon system reset. This mode operates at Privilege Level 1 (PL1) and provides the operating system kernel with full access to system resources. The SVC mode facilitates controlled transitions from user space to kernel space through the SWI mechanism, where the operating system can validate user requests and perform privileged operations. The banked registers (R13_svc, R14_svc, SPSR_svc) enable the kernel to maintain separate stack contexts and preserve processor state across supervisor calls.

### Abort Mode (ABT)

Abort Mode is activated when a memory access fault occurs during instruction fetch (prefetch abort) or data access (data abort). This mode is critical for implementing memory protection mechanisms, virtual memory systems, and fault-tolerant computing. When an abort exception occurs, the processor saves the faulting address in R14_abt and copies the CPSR to SPSR_abt. The abort mode enables the operating system to implement demand paging, handle page faults gracefully, or terminate errant processes when memory protection violations are detected.

### Undefined Mode (UND)

Undefined Mode is entered when the processor encounters an instruction that is not recognized or cannot be executed in the current processor state (such as coprocessor instructions not implemented in hardware). This mode facilitates software emulation of hardware functions, including floating-point unit operations on processors lacking hardware FPU support. The ARM instruction set allows for expanding the instruction space through undefined instruction handlers that can emulate missing hardware capabilities, providing significant flexibility in system design.

### System Mode (SYS)

System Mode is a privileged operational mode that utilizes the same register set as User Mode but executes with full privilege level (PL1). This mode is particularly useful for operating system tasks that require access to privileged resources while maintaining the user-mode register view. System Mode can be entered through modification of the CPSR mode bits and is essential for implementing context switching in operating systems where kernel code must access user-level registers efficiently.

## Exception Handling Mechanism

The ARM exception handling mechanism implements a deterministic sequence of operations when an exception condition is detected. Understanding this sequence is essential for writing efficient interrupt service routines and implementing reliable embedded systems.

### Exception Entry Sequence

When an exception occurs, the ARM processor executes the following precise sequence of operations:

1. **Link Register Preservation**: The processor saves the return address in the banked Link Register (R14) corresponding to the exception mode. The specific address saved depends on the exception type: for IRQ and FIQ exceptions, LR_offset = address_of_next_instruction (indicating that the interrupted instruction has not executed), while for prefetch abort, LR_offset = address_of_abort_instruction + 4.

2. **CPSR to SPSR Transfer**: The Current Program Status Register (CPSR) contents are atomically copied to the Saved Program Status Register (SPSR) of the target exception mode. This preservation enables complete restoration of the processor state upon exception return.

3. **CPSR Modification**: The CPSR is modified to reflect the new operational mode (bits [4:0]), disable appropriate interrupts (IRQ disabled for all exceptions, FIQ additionally disabled for FIQ mode), and set the instruction set state if transitioning to Thumb state or vice versa.

4. **Program Counter Vectoring**: The program counter (PC) is loaded with the address of the appropriate exception vector from the exception vector table. This vector address is determined by the exception type and the current vector configuration (low vectors at 0x00000000 or high vectors at 0xFFFF0000).

### Exception Return Sequence

Returning from an exception requires restoring the processor state and resuming execution at the correct address. The return mechanism depends on the exception type and utilizes the preserved link register value with specific offsets:

For IRQ and Data Abort exceptions, the return address is calculated as LR - 4, as these exceptions occur after the instruction completes execution. For Prefetch Abort, the return address is LR - 4 (address of the faulting instruction plus 4). For FIQ and SWI exceptions, the return address is LR (the address of the instruction following the SWI or interrupt instruction).

The return sequence typically involves loading the SPSR back to CPSR (restoring flags and mode) and moving the link register to PC with the appropriate offset, using instructions such as "SUBS PC, R14, #4" for IRQ return or "MOVS PC, R14" for FIQ/SWI return.

## Exception Vector Table

The exception vector table comprises fixed memory addresses where the processor commences execution when specific exception conditions arise. The standard vector table occupies 32 bytes (8 vectors × 4 bytes each) and is typically located at address 0x00000000 in systems with low vector configuration.

| Exception Type               | Vector Address (Low) | Vector Address (High) | Priority    |
| ---------------------------- | -------------------- | --------------------- | ----------- |
| Reset                        | 0x00000000           | 0xFFFF0000            | 1 (Highest) |
| Undefined Instruction        | 0x00000004           | 0xFFFF0004            | 6           |
| Software Interrupt (SWI)     | 0x00000008           | 0xFFFF0008            | 6           |
| Prefetch Abort               | 0x0000000C           | 0xFFFF000C            | 5           |
| Data Abort                   | 0x00000010           | 0xFFFF0010            | 2           |
| IRQ (Interrupt Request)      | 0x00000018           | 0xFFFF0018            | 4           |
| FIQ (Fast Interrupt Request) | 0x0000001C           | 0xFFFF001C            | 3           |

The vector table entries typically contain branch instructions (B) to handler code located elsewhere in memory, as the limited space at each vector address is insufficient for complete handler implementation. Modern ARM systems support vector table relocation to high memory addresses (0xFFFF0000) through hardware configuration, enabling systems with external memory at low addresses to maintain proper exception handling.

## Exception Priority Scheme

The ARM architecture defines a fixed priority ordering for handling multiple simultaneous exceptions. The priority hierarchy ensures deterministic behavior when multiple exception conditions occur concurrently:

1. **Reset (Highest Priority)**: Reset has absolute highest priority and is always processed first. Upon reset, all processor state is undefined, and execution begins at the reset vector.

2. **Data Abort**: Memory access faults (data aborts) have second-highest priority, as they indicate critical data integrity issues requiring immediate attention to prevent incorrect computation.

3. **FIQ (Fast Interrupt Request)**: The FIQ interrupt receives priority handling due to its dedicated banked registers and is designed for time-critical operations.

4. **IRQ (Interrupt Request)**: Standard interrupt requests are processed after FIQ, allowing the high-priority fast interrupts to be serviced with minimal latency.

5. **Prefetch Abort**: Instruction fetch faults are handled after standard interrupts, as the instruction has been prefetched but not yet executed.

6. **Undefined Instruction and SWI (Lowest Priority)**: These software exceptions have the lowest priority and are processed only when no higher-priority exception is pending.

Understanding this priority scheme is essential for designing interrupt-driven systems where multiple interrupt sources with varying urgency levels must be managed effectively.

## Banked Registers in ARM Exception Handling

The ARM architecture employs an innovative banked register scheme to accelerate exception handling by providing each exception mode with dedicated registers that require no explicit save/restore operations. This architecture significantly reduces interrupt latency and simplifies exception handler implementation.

Each exception mode (FIQ, IRQ, SVC, ABT, UND) maintains banked versions of R13 (stack pointer) and R14 (link register), while FIQ mode additionally banks R8 through R12. The User and System modes share the same register set, as do the FIQ and System modes' access to user-level registers when required. The Saved Program Status Register (SPSR) is also banked, enabling preservation of flags and processor state across exception handling.

When an exception occurs, the processor automatically switches to the appropriate banked registers, providing immediate access to clean register contexts without software overhead. This hardware-managed register banking represents a significant architectural advantage for real-time embedded applications where interrupt latency is critical.

## Assessment Questions

### Question 1: Exception Latency Calculation

An ARM7TDMI processor operates at 50 MHz with a system clock period of 20ns. The processor is executing a critical data processing routine when an IRQ interrupt is asserted. The IRQ input is sampled at clock edge N, and the interrupt acknowledge cycle begins at clock edge N+3. Given that the FIQ is disabled in the current CPSR state, calculate the minimum IRQ latency in microseconds, assuming the instruction pipeline is empty at the time of interrupt assertion. Additionally, explain whether the latency would increase or decrease if FIQ were enabled, and justify your answer.

### Question 2: Mode Transition Analysis

Consider an ARM processor initially operating in User Mode (CPSR = 0xD0) executing a user application. At a particular instant, an external peripheral generates an IRQ signal while simultaneously a floating-point coprocessor encounters an undefined instruction during emulation. Using your understanding of the ARM exception priority mechanism, determine: (a) The exact sequence of mode transitions that will occur, (b) The contents of CPSR and SPSR after the first exception is processed, (c) The return address saved in R14_irq, and (d) The final mode and state of the processor after both exceptions are handled sequentially.

### Question 3: Vector Table Relocation Analysis

A system designer must implement exception vector handling for an ARM9-based embedded system with external ROM mapped at address 0x00000000 and internal SRAM at 0xFFFF0000. The system requires reliable exception handling even if external ROM fails to respond. Analyze the following: (a) Explain the architectural support for vector table relocation in ARM, including relevant control registers. (b) Determine the vector addresses that would be used when the system is configured for high vector operation. (c) Calculate the offset in bytes between the Data Abort vector and the FIQ vector in both low and high vector configurations. (d) Justify which vector configuration would be more suitable for this system and explain the trade-offs involved.
