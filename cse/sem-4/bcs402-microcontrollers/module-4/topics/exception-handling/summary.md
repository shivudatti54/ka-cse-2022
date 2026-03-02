# Exception Handling in ARM Microcontrollers - Summary

## Key Definitions

- **Exception**: An event that disrupts normal program execution, causing the processor to suspend current operations and transfer control to a handler routine.
- **Vector Table**: A fixed memory structure containing branch instructions or addresses for each exception type's handler.
- **Interrupt Latency**: The time interval between an interrupt request signal and the first instruction of the interrupt handler execution.
- **Banked Registers**: Processor registers that have multiple instances, with separate copies for different processor modes.
- **SPSR (Saved Program Status Register)**: A mode-specific register that保存保存 the CPSR at the time an exception occurs.
- **FIQ (Fast Interrupt Request)**: A high-priority interrupt type with dedicated registers and reduced latency.

## Important Formulas

- **Vector Table Address**: `Base_Address + (Exception_Type × 4)` where each vector occupies 4 bytes
- **LR Return Offset (IRQ/Prefetch Abort)**: `LR - 4` to account for pipeline
- **LR Return Offset (FIQ/Data Abort)**: `LR - 8` to account for pipeline and prefetch
- **CPSR Mode Bits**: Bits 0-4 encode the processor mode (0x10=User, 0x11=FIQ, 0x12=IRQ, 0x13=Supervisor, 0x1B=Abort, 0x1F=System)

## Key Points

1. ARM supports seven exception types, each associated with a specific processor mode and vector table entry.

2. The processor automatically saves CPSR to SPSR and switches to the appropriate exception mode when an exception occurs.

3. The Link Register (LR) saves the return address, with different offsets depending on the exception type due to pipeline effects.

4. FIQ provides lower latency than IRQ because it has dedicated banked registers (R8-R12) and can be placed at the end of the vector table.

5. The vector table can be relocated using the Vector Table Offset Register (VTOR) in ARMv7 and later architectures.

6. Exception priority is fixed: Reset > Data Abort > FIQ > IRQ > Prefetch Abort > Undefined > SWI.

7. Exception handlers must carefully restore all saved registers and execute the correct return instruction to restore CPSR from SPSR.

8. Interrupt latency depends on current processor state, memory access times, pipeline depth, and interrupt priority.

## Common Mistakes

1. **Incorrect LR Offset**: Forgetting that the LR value saved during exception handling includes the pipeline offset, leading to wrong return addresses.

2. **Forgetting to Clear Interrupts**: Failing to clear the peripheral interrupt flag before returning, causing immediate re-entry into the handler.

3. **Stack Alignment**: Not maintaining proper stack alignment (8-byte for ARM AAPCS), which can cause errors in subsequent function calls.

4. **Missing Context Restoration**: Incomplete register saving/restoration, especially forgetting to restore CPSR from SPSR, corrupting processor state.

5. **Confusing Vector Addresses**: Mixing up the base address (0x00000000 vs 0xFFFF0000) or miscalculating individual vector offsets in the table.