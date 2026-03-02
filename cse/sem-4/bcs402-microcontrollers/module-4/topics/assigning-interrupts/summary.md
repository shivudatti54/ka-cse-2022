# Assigning Interrupts - Summary

## Key Definitions

- **NVIC (Nested Vectored Interrupt Controller)**: Integrated interrupt controller in ARM Cortex-M processors that manages all interrupt-related functions including enable, priority, and pending status.

- **Vector Table**: Memory structure containing addresses of exception and interrupt handlers, with the first entry being the initial stack pointer.

- **Interrupt Priority**: Numerical value determining the order of interrupt servicing; lower values indicate higher priority in ARM Cortex-M.

- **VTOR (Vector Table Offset Register)**: Register allowing runtime relocation of the vector table for bootloader support.

## Important Formulas

- **Vector Table Alignment**: Must be aligned to 32-word (128-byte) boundary
- **Priority Field Width**: 8 bits (actual implementation uses 3-4 bits depending on microcontroller)
- **Maximum Interrupts**: Up to 240 interrupt sources supported by NVIC

## Key Points

1. The vector table starts at address 0x00000000 by default and contains handler addresses arranged by exception number.

2. NVIC registers are memory-mapped and accessed via CMSIS functions or direct register manipulation.

3. Each interrupt must be enabled both at the peripheral level (generating the interrupt) and in the NVIC.

4. Priority grouping via AIRCR divides the priority field into preemptive priority and subpriority components.

5. Interrupts with higher preemptive priority can interrupt (preempt) lower priority interrupt handlers.

6. The VTOR register enables vector table relocation for systems requiring bootloader functionality.

7. Shared interrupts require flag checking within the handler to determine the specific interrupt source.

## Common Mistakes

1. Forgetting to clear peripheral interrupt flags within the ISR, causing immediate re-entry into the handler.

2. Setting peripheral interrupt enable before configuring the peripheral, potentially causing spurious interrupts.

3. Confusing priority numbering: remembering that lower values mean higher priority in ARM Cortex-M.

4. Neglecting vector table alignment requirements, leading to HardFault or memory management faults.

5. Enabling interrupts in NVIC before the peripheral interrupt source is properly configured.