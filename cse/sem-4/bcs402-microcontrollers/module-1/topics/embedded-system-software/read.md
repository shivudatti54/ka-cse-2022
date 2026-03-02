# Embedded System Software

## Table of Contents

- [Embedded System Software](#embedded-system-software)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [ARM Embedded Software Architecture](#arm-embedded-software-architecture)
  - [Memory Organization and Linker Scripts](#memory-organization-and-linker-scripts)
  - [Cross-Compilation and Toolchain](#cross-compilation-and-toolchain)
  - [Real-Time Operating Systems (RTOS)](#real-time-operating-systems-rtos)
  - [Interrupt Service Routines (ISRs)](#interrupt-service-routines-isrs)
- [Examples](#examples)
- [Exam Tips](#exam-tips)

## Introduction

Embedded system software forms the critical bridge between hardware and application functionality in ARM-based microcontroller systems. Unlike general-purpose computing software, embedded software must operate within stringent constraints of memory footprint, processing power, and real-time responsiveness. In ARM embedded systems, the software architecture is heavily influenced by the RISC design philosophy, which emphasizes simplified instruction sets enabling efficient compiler generation and predictable execution timing—properties essential for real-time applications.

The software stack for ARM microcontrollers typically comprises multiple layers: the startup code (bootloader), hardware abstraction layer (HAL), device drivers, real-time operating system (RTOS) when applicable, and user applications. Understanding this software ecosystem requires familiarity with ARM-specific toolchains, memory organization, and interrupt handling mechanisms that distinguish ARM-based embedded systems from other architectures.

## Key Concepts

### ARM Embedded Software Architecture

The embedded software architecture for ARM microcontrollers follows a hierarchical structure designed for efficiency and maintainability. At the lowest level lies the **startup code** (also termed bootstrap or initialization code), which executes immediately after reset and before the main application begins. This code configures the stack pointer, initializes the .data section (copying initialized global variables from flash to RAM), zeros the .bss section (uninitialized globals), and optionally configures the clock system and peripheral clocks before branching to the main() function.

The **Hardware Abstraction Layer (HAL)** provides a standardized API for accessing peripheral registers, abstracts hardware details, and facilitates portability across different ARM Cortex-M variants. For ARM Cortex-M processors, the CMSIS (Cortex Microcontroller Software Interface Standard) defines this abstraction layer, including device header files, interrupt definitions, and core access functions.

### Memory Organization and Linker Scripts

ARM microcontrollers employ a memory-mapped I/O architecture where peripheral registers and memory occupy a unified address space. The typical Flash memory (0x08000000 start) stores program code and const data, while SRAM (0x20000000 start) holds variables requiring read-write access. Linker scripts (.ld files) define memory regions, placement of code and data sections, and the vector table location—critical for ARM processors where the vector table contains initial stack pointer and reset handler address.

### Cross-Compilation and Toolchain

Embedded software for ARM requires **cross-compilation** since the development host (x86/x64) differs from the target ARM processor. The ARM toolchain comprises: (a) GNU Arm Embedded Toolchain (Arm GCC) or Keil MDK, (b) assembler (arm-none-eabi-as), (c) compiler (arm-none-eabi-gcc), (d) linker (arm-none-eabi-ld), and (e) objcopy for generating binary formats (HEX, BIN). The compilation produces ELF (Executable and Linkable Format) files containing debug information, which can be loaded via JTAG/SWD debuggers.

### Real-Time Operating Systems (RTOS)

When applications require concurrent task execution with timing guarantees, an RTOS becomes essential. ARM Cortex-M processors support the **PendSV** and **SVC** exceptions facilitating RTOS context switching. Common RTOS choices for ARM include FreeRTOS, µC/OS-II, and Azure RTOS.

**Rate Monotonic Scheduling (RMS)** is the fundamental fixed-priority scheduling algorithm for periodic real-time tasks. The theorem states: A set of n periodic tasks with periods T_i and execution times C_i is schedulable under RMS if Σ(C_i/T_i) ≤ n(2^(1/n) - 1). This bound approaches ln(2) ≈ 0.693 as n increases. Tasks are assigned priorities inversely proportional to their periods—shorter period implies higher priority.

### Interrupt Service Routines (ISRs)

ARM Cortex-M processors implement a vectored interrupt architecture where the vector table (located at address 0x00000000 by default, configurable) contains addresses of exception handlers. The **Nested Vectored Interrupt Controller (NVIC)** manages interrupts with configurable priority levels. ISRs execute in Handler mode with priority masking, and the processor automatically saves context upon exception entry, enabling relatively low-latency interrupt handling consistent with RISC design principles.

## Examples

**Example 1: ARM Startup Code Analysis**

Consider a minimal ARM Cortex-M startup sequence:

```c
// Simplified startup pseudocode
void Reset_Handler(void) {
    // Copy .data section from flash to RAM
    for (int *src = &_sidata, *dst = &_sdata; dst < &_edata; )
        *dst++ = *src++;

    // Zero .bss section
    for (int *dst = &_sbss; dst < &_ebss; )
        *dst++ = 0;

    // Initialize system clock
    SystemInit();

    // Call main
    main();

    // If main returns, loop forever
    while(1);
}
```

This demonstrates how embedded software handles memory initialization essential for C runtime on ARM microcontrollers.

**Example 2: RMS Schedulability Analysis**

Given three periodic tasks for an ARM-based real-time controller:

- Task 1: C₁ = 10ms, T₁ = 50ms
- Task 2: C₂ = 20ms, T₂ = 100ms
- Task 3: C₃ = 15ms, T₃ = 150ms

Calculate CPU utilization: U = 10/50 + 20/100 + 15/150 = 0.2 + 0.2 + 0.1 = 0.5

RMS bound for n=3: 3(2^(1/3) - 1) = 3(0.26) = 0.78

Since U = 0.5 < 0.78, the task set is schedulable under Rate Monotonic Scheduling on the ARM target.

**Example 3: Memory Map Calculation**

For an ARM Cortex-M4 with 256KB Flash and 64KB RAM:

- Flash: 0x08000000 to 0x0803FFFF
- SRAM: 0x20000000 to 0x2000FFFF

The linker script must allocate:

- .text (code): 0x08000000
- .rodata (const): follows .text
- .data (initialized globals): 0x20000000
- .bss (uninitialized): follows .data
- Heap: grows upward from end of .bss
- Stack: grows downward from 0x2000FFFF

## Exam Tips

1. **ARM-Specific Focus**: Always relate embedded software concepts to ARM architecture—know the Cortex-M vector table structure and NVIC priority grouping.

2. **Startup Sequence**: Memorize the complete ARM boot sequence: Power-on → Reset → Stack initialization → .data/.bss initialization → SystemInit() → main().

3. **RTOS Proofs**: Remember the RMS schedulability bound formula and be prepared to prove task set feasibility using utilization bounds or response time analysis.

4. **Toolchain Components**: Know the complete ARM toolchain workflow: source → assembly → object → linked ELF → binary (HEX/BIN).

5. **Memory Constraints**: Understand the distinction between Flash (non-volatile, stores code) and SRAM (volatile, stores variables), critical for embedded software design.

6. **Interrupt Latency**: ARM Cortex-M provides low-latency interrupt handling; know the sequence: interrupt request → NVIC prioritization → exception entry → context save → ISR execution.

7. **Cross-Compilation**: Recognize that embedded ARM software requires cross-compilation and understand why native compilation is impossible for ARM targets.
