# Link Register Offsets in ARM Cortex-M - Summary

## Key Definitions and Concepts

- **Link Register (LR/R14)**: A special-purpose register in ARM architecture that stores return addresses during subroutine calls and exception handling
- **EXC_RETURN**: A 32-bit pattern (0xFFxxxxxx) placed in LR when returning from exceptions, encoding processor state information
- **Stack Frame**: Automatically pushed by the processor during exception entry, containing saved registers including LR at offset +20 bytes

## Important Formulas and Theorems

- **Standard stack frame LR offset**: LR at SP + 20 (5 × 4 bytes), PC at SP + 24, xPSR at SP + 28
- **Common EXC_RETURN values**:
  - 0xFFFFFFF9: Thread mode, MSP, no FP frame
  - 0xFFFFFFFD: Thread mode, PSP, no FP frame
  - 0xFFFFFFF1: Handler mode, MSP, no FP frame
- **Bit interpretation**: Bit[4]=Thread/Handler, Bit[1]=MSP/PSP, Bit[0]=FP frame presence

## Key Points

- EXC_RETURN values always have 0xFF as their upper 8 bits, distinguishing them from normal return addresses
- Handler mode always uses MSP, while Thread mode can use either MSP or PSP depending on configuration
- The LR offset +20 from SP in standard stack frames enables stack unwinding for debugging
- Cortex-M4/M7 with FPU support lazy stacking, deferring FP register saves until actually needed
- Function prologues typically PUSH {LR} and epilogues POP {PC} for return address restoration

## Common Mistakes to Avoid

- Confusing MSP and PSP selection bits - bit [1] being 1 means PSP was in use, not MSP
- Forgetting that EXC_RETURN values have 0xFF in upper 8 bits - this is how the processor identifies them
- Overlooking the floating-point frame bit when handling exceptions on Cortex-M4/M7
- Using wrong offset calculations when manually accessing saved registers in exception handlers

## Revision Tips

- Practice identifying EXC_RETURN values and their meanings for different scenarios
- Memorize the standard stack frame layout with register order and offsets
- Understand the relationship between Thread/Handler mode and MSP/PSP selection
- Review how function prologue/epilogue use LR for subroutine calls
