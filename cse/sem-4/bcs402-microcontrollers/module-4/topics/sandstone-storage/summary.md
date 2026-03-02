# Example Sandstone: ARM Firmware Implementation Framework - Summary

## Key Definitions

- **Example Sandstone**: A firmware implementation framework for ARM Cortex-M microcontrollers providing bootloader, exception handling, and interrupt management components

- **Vector Table**: A memory structure at a fixed location containing the initial stack pointer and entry points for all exception handlers in ARM Cortex-M processors

- **NVIC (Nested Vectored Interrupt Controller)**: ARM's interrupt controller providing configurable interrupt priorities, enable/disable controls, and pending status management

- **Exception Latency**: The time interval from interrupt assertion to execution of the first instruction of the corresponding interrupt service routine

- **Tail-Chaining**: An ARM Cortex-M optimization where the processor exits one interrupt and immediately enters a pending higher-priority interrupt without stacking

## Important Formulas

- **Effective Interrupt Latency (Tail-Chaining)**: 12 cycles (fixed) - no additional stack operations required

- **Exception Stack Frame Size**: 8 registers × 4 bytes = 32 bytes (R0, R1, R2, R3, R12, LR, PC, xPSR)

- **Vector Table Entry Size**: 4 bytes per entry (32-bit address)

- **Priority Bits Calculation**: For n priority bits, 2^n distinct priority levels are available

## Key Points

1. Example Sandstone implements a three-layer architecture: Hardware Abstraction Layer, Core Services Layer, and Application Interface Layer

2. The bootloader configures stack pointers for all ARM processor modes (Supervisor, IRQ, FIQ, Abort, Undefined, System) during initialization

3. Vector table relocation via VTOR allows dynamic interrupt handler updates and supports bootloader-to-application transitions

4. FIQ provides lower latency through dedicated register banking (R8-R12) and cannot be masked by interrupt enable bits

5. Interrupt priority in ARM Cortex-M is configurable per interrupt, with lower numeric values indicating higher priority

6. Exception handlers must follow AAPCS conventions, preserving caller-saved registers and maintaining stack alignment

7. The first vector table entry contains the initial Main Stack Pointer (MSP) value, not a handler address

8. Tail-chaining reduces latency when servicing consecutive interrupts of different priorities

9. Link Register (LR) values during exception return indicate the required processor state transition (handler/thread mode, MSP/PSP)

10. Firmware frameworks like Example Sandstone abstract hardware details, enabling portable and maintainable embedded software development

## Common Mistakes

1. **Confusing MSP and PSP**: The Main Stack Pointer (MSP) is used for exception handling and system initialization, while Process Stack Pointer (PSP) is available for application thread mode

2. **Incorrect Priority Configuration**: Failing to understand that not all priority bits may be implemented in silicon - always verify with device documentation

3. **Improper Exception Handler Exit**: Using incorrect LR values when returning from exceptions can cause undefined processor behavior

4. **Neglecting Memory Barriers**: Omitting Data Synchronization Barrier (DSB) and Instruction Synchronization Barrier (ISB) operations after modifying vector table or priority registers

5. **Stack Alignment Violations**: ARM AAPCS requires 8-byte stack alignment at function call boundaries; violations cause unpredictable behavior
