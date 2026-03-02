# Vector Table in ARM Cortex-M - Summary

## Key Definitions and Concepts

- **Vector Table**: A memory structure containing 32-bit addresses of exception handlers, located at the start of flash memory (typically 0x00000000 or 0x08000000)
- **Initial MSP**: The first entry in the vector table containing the initial Main Stack Pointer value
- **Reset Handler**: The second entry containing the address where execution begins after reset
- **VTOR (Vector Table Offset Register)**: Register at 0xE000ED08 that allows runtime relocation of the vector table

## Important Formulas and Theorems

- **Vector Address Formula**: Vector Address = Vector Table Base + (Exception Number × 4)
- **Alignment Requirement**: Vector table must be aligned to 2^(N+1) bytes, where N is the number of bits needed for interrupt representation
- **Table Size**: Total entries = (Number of exceptions) + (Number of IRQs), typically 16 + N IRQs

## Key Points

- The first entry (offset 0x000) is the Initial MSP, loaded before any code execution
- The second entry (offset 0x004) is the Reset Handler, where PC jumps after reset
- Cortex-M4 supports up to 240 external interrupts (IRQs) plus 10 system exceptions
- Each vector table entry is 4 bytes (32-bit address)
- The vector table can be relocated to RAM using VTOR for dynamic handler updates
- Startup code typically uses weak aliases for handler functions
- CMSIS framework provides standardized names for all interrupt handlers
- For flash-based microcontrollers like STM32, the vector table starts at 0x08000000
- The NVIC (Nested Vectored Interrupt Controller) uses the vector table for interrupt dispatching

## Common Mistakes to Avoid

- Confusing vector table with the actual interrupt service routines; the table only contains addresses
- Forgetting to clear the interrupt flag in the handler, causing repeated interrupts
- Not enabling the interrupt in both the peripheral and the NVIC
- Incorrect alignment of the vector table leading to hard faults
- Attempting to modify flash-based vector table directly without proper unlock sequence

## Revision Tips

1. Memorize that entry 0 is MSP and entry 1 is Reset Handler - this is the most frequently tested concept
2. Practice calculating vector addresses using the formula: Base + (Exception Number × 4)
3. Remember the VTOR register address: 0xE000ED08
4. Understand the difference between enabling interrupts in peripheral vs. in NVIC
5. Review startup code examples to understand how vector tables are implemented in practice
