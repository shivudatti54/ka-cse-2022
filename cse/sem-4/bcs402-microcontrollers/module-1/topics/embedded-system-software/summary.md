# Embedded System Software - Summary

## Key Definitions

- **Firmware**: Low-level software stored in non-volatile memory that provides control and monitoring functions for embedded hardware.

- **Startup Code**: Assembly language routines executed immediately after processor reset that initialize registers, stack, and memory sections.

- **Linker Script**: A file defining memory regions and section placement for mapping application code to physical memory addresses.

- **Cross-Compilation**: The process of compiling code on a host machine to generate executable code for a different target architecture.

- **RTOS (Real-Time Operating System)**: Specialized operating system ensuring predictable response times for time-critical embedded applications.

- **ISR (Interrupt Service Routine)**: Special function executed in response to hardware interrupts, requiring careful implementation to preserve processor context.

## Important Formulas

- **RMS Utilization Bound**: $U_{bound} = n(2^{1/n} - 1)$ where n is the number of tasks

- **CPU Utilization**: $U = \sum_{i=1}^{n} \frac{C_i}{T_i}$ where C_i is execution time and T_i is period

- **Interrupt Latency (ARM Cortex-M)**: Typically 12 cycles from interrupt request to first instruction of ISR

## Key Points

1. ARM Cortex-M uses a vectored interrupt mechanism with the NVIC, enabling low-latency interrupt handling essential for real-time applications.

2. The startup code performs critical initialization: stack pointer setup, .data section copying from flash to RAM, and .bss section zeroing.

3. Layered architecture with HAL promotes code portability across different ARM microcontroller variants from various manufacturers.

4. The RISC design philosophy simplifies software development through uniform instruction formats and a load-store architecture requiring explicit memory operations.

5. Linker scripts define memory layout for Flash (code storage) and SRAM (variables and stack), critical for resource-constrained embedded systems.

6. Cross-compilation toolchains (ARM GCC, Keil, IAR) are essential as ARM microcontrollers cannot typically host development environments.

7. Rate Monotonic Scheduling provides guaranteed schedulability for periodic tasks when CPU utilization stays below the theoretical bound.

8. ELF (Executable and Linkable Format) is the standard binary format for ARM embedded applications, containing debug information for debuggers.

## Common Mistakes

1. **Ignoring Memory Constraints**: Failing to account for stack growth and heap allocation in SRAM leading to overflow issues.

2. **Incorrect Vector Table Placement**: Placing the vector table at wrong memory addresses causes failure to handle interrupts or reset properly.

3. **ISR Implementation Errors**: Using function calls or blocking operations within ISRs violates real-time constraints and may cause system instability.

4. **Neglecting Endianness**: ARM Cortex-M processors are little-endian; misunderstanding byte ordering causes data corruption in communication protocols.

5. **Improper Linker Script Configuration**: Misconfiguring memory regions results in code execution failures or inefficient memory utilization.