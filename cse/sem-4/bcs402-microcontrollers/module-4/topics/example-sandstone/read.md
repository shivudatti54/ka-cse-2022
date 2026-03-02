# Example Sandstone: ARM Firmware Implementation Framework

## Introduction

Example Sandstone represents a comprehensive firmware implementation framework designed for ARM Cortex-M based microcontroller systems. Within the context of embedded systems firmware development, "Sandstone" refers to a layered architecture approach that provides robust foundation code for bootloader implementation, exception handling, and interrupt management. This framework exemplifies the principles of ARM firmware suite development, demonstrating how developers can create reliable, maintainable firmware that properly interfaces with ARM processor modes and exception mechanisms.

The framework becomes particularly relevant when considering the complex nature of modern microcontroller applications requiring secure bootloader functionality, deterministic interrupt response, and systematic exception handling. Understanding Example Sandstone and its implementation patterns equips developers with the knowledge required to design firmware solutions that effectively utilize ARM's exception model, vector table configurations, and interrupt priority mechanisms.

This document examines the architectural components of Example Sandstone, its integration with ARM firmware conventions, and practical implementation considerations for embedded systems development.

## Key Concepts

### Framework Architecture Overview

Example Sandstone implements a modular firmware architecture comprising three primary layers: the Hardware Abstraction Layer (HAL), the Core Services Layer, and the Application Interface Layer. The HAL provides low-level peripheral access routines, hiding processor-specific register details from upper software layers. The Core Services Layer implements critical firmware functionality including bootloader routines, exception vector management, and interrupt service routine (ISR) dispatching. The Application Interface Layer offers standardized APIs for common embedded operations.

This layered approach aligns with ARM firmware best practices, where clean abstraction boundaries facilitate code reuse and simplify migration between different ARM Cortex-M variants. The framework typically initializes at a fixed memory location defined by the vector table, establishing the foundation for all subsequent firmware operations.

### Bootloader Implementation

The bootloader component of Example Sandstone follows a structured initialization sequence. Upon reset, the processor executes the initial startup code that configures stack pointers for each processor mode, initializes critical hardware peripherals, and establishes memory timing parameters. The bootloader then performs integrity verification of the application firmware image before transferring control to the main application.

Key bootloader responsibilities include:

- **Stack Initialization**: Configuring stack pointers for Supervisor, IRQ, FIQ, Abort, Undefined, and System modes as required by the ARM exception model
- **Vector Table Relocation**: When implementing vector table offset registers (VTOR), the bootloader may relocate the vector table to RAM for dynamic interrupt handler installation
- **Memory Configuration**: Setting up flash wait states, enabling peripheral clocks, and configuring memory protection units where available

### Exception Handling Integration

Example Sandstone integrates with ARM's exception handling mechanism through the vector table structure. The vector table contains entry points for each exception type: Reset, NMI, Hard Fault, Memory Management Fault, Bus Fault, Usage Fault, and the standard interrupts (IRQ0-IRQn). Each vector entry contains either a handler address or a branch instruction to the corresponding exception handler.

The framework implements exception handlers following ARM's procedure call standard (AAPCS), ensuring proper register preservation and stack alignment. Exception handlers typically follow this structure:

1. Save processor state (PUSH register list)
2. Execute exception-specific handling code
3. Restore processor state (POP register list)
4. Return from exception (typically via LR manipulation)

### Interrupt Latency Considerations

Interrupt latency in Example Sandstone depends on several factors: the current processor state, priority level of the interrupting source, and any higher-priority exceptions being serviced. The framework optimizes latency through:

- **Priority Grouping**: Implementing priority-based interrupt preemption allowing time-critical interrupts to preempt lower-priority handlers
- **Tail-Chaining**: When exiting one interrupt handler to immediately enter a pending higher-priority handler, the processor avoids unnecessary stack operations
- **Late Arrival**: When a higher-priority interrupt arrives during the stacking of a lower-priority interrupt, the processor services the higher-priority interrupt first

### Vector Table Design

The vector table in Example Sandstone follows the ARM Cortex-M specification where the first entry contains the initial stack pointer value (loaded from the main stack pointer MSP), followed by entry points for Reset, NMI, Hard Fault, and other exceptions. Interrupt vectors begin at index 16 (for Cortex-M0/M0+) or index 16-31 depending on the specific Cortex-M variant.

Modern implementations may utilize the Vector Table Offset Register (VTOR) to support:

- Runtime vector table relocation
- Application-specific vector tables in flash
- Bootloader-to-application vector table switching

### IRQ and FIQ Exceptions

ARM processors support two primary interrupt types: IRQ (Interrupt Request) and FIQ (Fast Interrupt Request). Example Sandstone configures FIQ for the highest-priority, latency-critical interrupts:

- **IRQ**: Standard interrupt request, vectored through the vector table, supports nested interrupts via priority configuration
- **FIQ**: Fast interrupt with dedicated register banking (R8-R12), allowing minimal context saving and reduced latency

The framework's interrupt controller abstraction allows developers to assign interrupts to either type based on timing requirements, with FIQ typically reserved for time-critical motor control, communication, or safety functions.

## Examples

### Example 1: Vector Table Configuration

Consider an Example Sandstone implementation for an ARM Cortex-M4 processor with the following vector table entries:

```
Vector Table (Flash Address 0x08000000):
0x08000000: Initial MSP = 0x20030000
0x08000004: Reset_Handler address
0x08000008: NMI_Handler address
0x0800000C: HardFault_Handler address
...
0x08000040: IRQ0_Handler address (External Interrupt 0)
0x08000044: IRQ1_Handler address (External Interrupt 1)
```

Configuration code:

```c
// Configure Vector Table Offset Register (VTOR)
#define SCB_BASE 0xE000ED00
#define SCB_VTOR *(volatile uint32_t *)(SCB_BASE + 0x08)

// Relocate vector table to RAM for dynamic updates
SCB_VTOR = 0x20000000; // RAM base address
```

### Example 2: Interrupt Priority Assignment

Configuring interrupt priorities in Example Sandstone for a three-interrupt system:

```c
// Interrupt priority configuration
#define NVIC_IPR_BASE 0xE000E400
#define PRIORITY_SHIFT 4 // Bits 7:5 for priority (Cortex-M4)

// Configure priorities: Timer=high, UART=medium, Button=low
*(volatile uint8_t *)(NVIC_IPR_BASE + 16) = 0x10; // Timer (high priority)
*(volatile uint8_t *)(NVIC_IPR_BASE + 17) = 0x20; // UART (medium priority)
*(volatile uint8_t *)(NVIC_IPR_BASE + 18) = 0x30; // Button (low priority)

// Enable interrupts in NVIC
#define NVIC_ISER_BASE 0xE000E100
*(volatile uint32_t *)(NVIC_ISER_BASE) = (1 << 16) | (1 << 17) | (1 << 18);
```

### Example 3: Exception Handler Implementation

Implementing a fault handler in Example Sandstone:

```c
void HardFault_Handler(void) {
 // Capture exception context
 __asm volatile (
 "movs r0, #4\n"
 "mov r1, lr\n"
 "tst r0, r1\n"
 "beq _MSP\n"
 "mrs r0, psp\n"
 "b _HALT\n"
 "_MSP:\n"
 "mrs r0, msp\n"
 "_HALT:\n"
 "ldr r1, [r0, #24]\n"
 "ldr r2, handler_address_const\n"
 "bx r2\n"
 "handler_address_const: .word fault_handler_c\n"
 );
}

void fault_handler_c(uint32_t *stack_frame) {
 // Analyze fault - stack frame contains:
 // R0, R1, R2, R3, R12, LR, PC, xPSR
 uint32_t r0 = stack_frame[0];
 uint32_t r1 = stack_frame[1];
 uint32_t pc = stack_frame[6];
 uint32_t xPSR = stack_frame[7];

 // Log fault information or trigger recovery
 while(1); // Debug halt
}
```

## Exam Tips

1. **Vector Table Structure**: Remember that the first vector table entry is the initial stack pointer (MSP), followed by the Reset handler. Interrupt vectors begin at exception number 16.

2. **Exception Priority Levels**: ARM Cortex-M implements configurable priority. Lower numerical priority values indicate higher urgency. FIQ has implicit highest priority and cannot be masked by the ISR bits.

3. **Link Register Offsets**: When exception handlers modify the return address in LR, understand that the value indicates which stack (MSP/PSP) and return mode (thread/handler) the exception exit should use.

4. **Latency Optimization**: Study tail-chaining and late-arrival mechanisms as they reduce effective interrupt latency when multiple interrupts occur in succession.

5. **Bootloader Security**: Understand the difference between plain flash execution and secure bootloader implementations, including image verification and secure boot concepts.

6. **Stack Frame Composition**: For exception handlers, know the exact order of registers pushed onto the stack (R0, R1, R2, R3, R12, LR, PC, xPSR for Cortex-M).

7. **Mode vs. State**: ARM processors operate in different privilege modes (Supervisor, System, IRQ, FIQ, Abort, Undefined) and states (Thumb vs. ARM). Firmware must configure appropriate transitions.
