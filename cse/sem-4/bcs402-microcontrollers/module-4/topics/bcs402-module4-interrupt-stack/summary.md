# Basic Interrupt Stack Design And Implementation - Summary

## Key Definitions

- **Stack Frame**: A collection of registers automatically pushed onto the stack by hardware during exception entry, containing R0-R3, R12, LR, PC, and xPSR (32 bytes total).

- **EXC_RETURN**: A special value loaded into the LR register during exception entry that encodes return information including stack pointer selection and execution mode.

- **MSP (Main Stack Pointer)**: The default stack pointer used in handler mode and during system initialization; also serves as the stack pointer for thread mode unless explicitly switched to PSP.

- **PSP (Process Stack Pointer)**: An alternative stack pointer available in thread mode, commonly used in RTOS environments to provide stack isolation between tasks.

- **Vector Table**: A memory structure containing the initial MSP value and handler entry addresses for all exceptions and interrupts, requiring specific alignment based on device type.

- **Nested Interrupt Handling**: A technique allowing higher-priority interrupts to preempt currently executing ISR, requiring explicit firmware management of register saves and priority configuration.

## Important Formulas

- **Stack Frame Size**: 8 registers × 4 bytes = 32 bytes (hardware automatic push)

- **Manual Register Save Size**: (Number of registers) × 4 bytes

- **Maximum Stack Depth for N Nesting Levels**: N × (32 bytes + manual_save_bytes + call_overhead)

- **Vector Table Alignment**: 128-word (512-byte) minimum; 256-word (1024-byte) for some devices

## Key Points

1. ARM Cortex-M automatically pushes an eight-register stack frame during exception entry from thread mode, but not when nesting exceptions in handler mode.

2. The vector table's first entry must contain the initial stack pointer value (MSP initialization), followed by handler addresses in a predefined order.

3. EXC_RETURN values encode critical return information in their bit patterns, allowing the processor to determine stack pointer selection and execution mode upon return.

4. ISR prologue must save any registers beyond the automatic stack frame that will be modified, while epilogue must restore them before returning.

5. Stack overflow can be detected through hardware (PSPLIM/MSPLIM registers triggering MemManage fault) or software (stack canary pattern checking) mechanisms.

6. Nested interrupt handling requires explicit firmware actions including manual register saving, priority manipulation through BASEPRI/PRIMASK, and careful EXC_RETURN management.

7. The MSP serves as the default stack pointer for all exception handling, providing a dedicated stack that cannot be corrupted by application code stack overflow.

8. Proper stack sizing requires analyzing worst-case nesting scenarios and calculating maximum stack consumption including all hardware and software contributions.

## Common Mistakes

1. **Assuming all registers are automatically saved**: Many students forget that only R0-R3, R12, LR, PC, and xPSR are hardware-saved, requiring manual saves of R4-R11 in ISRs.

2. **Confusing thread mode and handler mode**: Failing to recognize that the hardware stack frame is only pushed during transitions from thread to handler mode leads to incorrect stack calculations.

3. **Ignoring EXC_RETURN encoding**: Treating LR as a simple return address during exception handling overlooks its critical role in controlling the return sequence.

4. **Incorrect stack pointer selection**: Using PSP for interrupt handling (which always uses MSP) represents a fundamental misunderstanding of Cortex-M architecture.

5. **Underestimating stack requirements**: Neglecting the stack space consumed by manual register saves and function calls within ISRs leads to insufficient stack allocation and potential overflow.

6. **Forgetting to preserve EXC_RETURN during nesting**: When implementing nested interrupts, failing to save the LR containing EXC_RETURN before enabling further interrupts corrupts the return mechanism.

7. **Assuming uniform vector table size**: Vector table alignment requirements vary between Cortex-M implementations, with some requiring larger alignments than others.
