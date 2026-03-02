# IRQ and FIQ Exceptions - Summary

## Key Definitions and Concepts

- **Exception**: An event that disrupts normal program flow, requiring the processor to execute special handling code
- **IRQ (Interrupt Request)**: Standard interrupt for general-purpose peripherals with moderate latency requirements
- **FIQ (Fast Interrupt Request)**: High-priority, low-latency interrupt for time-critical operations
- **CPSR (Current Program Status Register)**: Contains interrupt mask bits (I and F) and processor mode bits
- **SPSR (Saved Program Status Register)**: Stores CPSR during exception handling for later restoration

## Important Formulas and Concepts

- **IRQ Vector Address**: 0x00000018
- **FIQ Vector Address**: 0x0000001C
- **Return Address Calculation**: LR - 4 (accounts for pipeline effect)
- **CPSR Mode Bits**: User (10000), FIQ (10001), IRQ (10010), Supervisor (10011)
- **Interrupt Mask Bits**: I bit (bit 7) masks IRQ, F bit (bit 6) masks FIQ

## Key Points

- FIQ has higher priority than IRQ and cannot be interrupted by IRQ when enabled
- FIQ uses dedicated register bank (r8-r14), eliminating register saving overhead
- Exception handling involves: saving state → switching to exception mode → executing handler → restoring state
- The vector table is typically located at 0x00000000, with FIQ placed last for direct handler execution
- Cortex-M processors use NVIC for vectored interrupt handling with priority levels
- Nested interrupts require explicitly saving SPSR and re-enabling interrupts in handler

## Common Mistakes to Avoid

1. Forgetting to save/restore registers in IRQ handler, causing corruption of interrupted program state
2. Incorrect return address calculation (using LR directly instead of LR-4)
3. Not clearing interrupt flags in peripheral, leading to repeated interrupt triggering
4. Confusing CPSR and SPSR roles - CPSR is current state, SPSR is saved state
5. Enabling FIQ without proper handler, causing unpredictable behavior

## Revision Tips

1. Practice drawing and memorizing the exception vector table
2. Write sample IRQ and FIQ handlers in assembly to understand the save/restore mechanism
3. Focus on the key differences between IRQ and FIQ: priority, latency, register banking
4. Review CPSR bit assignments, especially I and F mask bits
5. Understand why FIQ is placed at the end of vector table and how this enables direct execution
6. Compare traditional ARM7 exception handling with Cortex-M NVIC approach
