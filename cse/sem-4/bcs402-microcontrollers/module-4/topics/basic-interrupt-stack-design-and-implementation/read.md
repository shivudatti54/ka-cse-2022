# Basic Interrupt Stack Design And Implementation

## Introduction

Interrupt stack design constitutes a fundamental aspect of firmware development for ARM Cortex-M based microcontrollers. When an exception or interrupt occurs, the processor must preserve the current execution context before transferring control to the exception handler. This context preservation mechanism relies heavily on proper stack design and implementation, making it essential for firmware developers to understand how the stack frame is constructed, which registers are automatically saved, and how the stack pointer manages memory during interrupt servicing.

The ARM Cortex-M architecture provides hardware-supported interrupt handling through its nested vectored interrupt controller (NVIC) and dedicated stack frame operations. Unlike earlier microprocessor architectures that required manual context saving, Cortex-M processors automatically push a subset of registers onto the stack when entering an exception handler. This hardware-level optimization significantly reduces interrupt latency but necessitates careful stack initialization and management by the firmware developer. Understanding the interplay between the main stack pointer (MSP) and process stack pointer (PSP), along with proper vector table configuration, forms the cornerstone of reliable interrupt-driven embedded systems.

This topic examines the complete interrupt stack design workflow in ARM Cortex-M microcontrollers, covering stack frame composition, exception entry and exit sequences, nested interrupt handling considerations, and practical implementation guidelines. The content aligns with the ARM firmware suite module and builds upon related topics such as ARM processor exceptions and modes, IRQ and FIQ exceptions, and exception handling mechanisms.

## Key Concepts

### Exception Types and Priority in ARM Cortex-M

The ARM Cortex-M architecture defines several exception types with predetermined priorities. The reset exception occupies priority -3, followed by NMI at -2, hard fault at -1, and SVCall at configurable priority levels. The PendSV and SysTick exceptions provide operating system support, while peripheral interrupts (IRQs) numbered from IRQ0 through IRQ239 are routed through the NVIC. Each interrupt source can be assigned a priority level from 0 (highest) to 255 (lowest), with the NVIC managing priority grouping and preemption behavior.

When multiple pending interrupts have the same priority level, the hardware determines servicing order based on their position in the vector table. This deterministic behavior ensures predictable real-time system performance but requires careful interrupt priority assignment during system design. The priority grouping mechanism allows firmware developers to create critical timing boundaries between different interrupt levels, ensuring that time-critical operations cannot be preempted by less urgent interrupts.

### Vector Table Structure and Location

The vector table represents a critical data structure containing initialization values for the stack pointer and entry points for all exception handlers. Located at the flash memory starting address (typically 0x00000000 or 0x08000000 depending on memory mapping), the vector table begins with the initial stack pointer value followed by the address of the reset handler. Subsequent entries correspond to NMI handler, hard fault handler, and other exception types in a predefined order, with peripheral interrupt handlers occupying the final entries.

The vector table must be aligned to a 128-word (512-byte) boundary for Cortex-M devices, though some implementations require 256-word alignment. Modern ARM Cortex-M devices support vector table offset registers (VTOR) that allow runtime relocation of the vector table, enabling bootloaders and application firmware to maintain separate vector tables in different memory regions. This capability proves essential for firmware update mechanisms and secure boot implementations where the vector table location changes during the boot process.

### Stack Frame Composition During Exception Entry

When an exception occurs in thread mode, the Cortex-M processor automatically pushes an eight-register stack frame onto the currently active stack. This stack frame contains R0, R1, R2, R3, R12, the return address (LR), the program counter at the time of exception (PC), and the xPSR status register. The hardware push operation occurs atomically, ensuring that no context can be lost during the interrupt entry sequence. The pushed PC value points to the next instruction that would have been executed had the interrupt not occurred, enabling proper return and continuation of the interrupted code.

The stack frame layout follows a specific order in memory, with R0 at the lowest address and xPSR at the highest. This arrangement enables efficient exception return mechanisms that utilize load-multiple instructions to restore the saved context. When the exception occurs in handler mode (indicating nested interrupt), the processor does not push an additional stack frame since the current context was already saved during the original exception entry. Instead, the processor simply updates the LR register with the appropriate EXC_RETURN value to manage the nested return sequence.

### Stack Pointer Selection: MSP versus PSP

ARM Cortex-M processors implement two stack pointers: the main stack pointer (MSP) and the process stack pointer (PSP). The MSP serves as the default stack pointer used during reset, in handler mode, and for system initialization code. The PSP operates exclusively in thread mode and finds primary use in operating system environments where separate stacks for application tasks improve memory isolation and fault tolerance. The CONTROL register's bit 0 determines which stack pointer is active in thread mode, while handler mode invariably uses the MSP.

Firmware developers must initialize the MSP during system startup, typically by loading it with the top-of-stack address located in the vector table's first entry. The PSP, when used, requires explicit initialization in thread mode before enabling interrupts. This dual-stack design enables robust embedded systems where kernel code and interrupt handlers use the MSP (providing a dedicated stack for exception handling), while user tasks maintain separate stacks using the PSP. This separation prevents stack overflow in user tasks from corrupting the kernel's operation and provides clearer fault diagnosis when stack-related errors occur.

### Exception Entry and Exit Sequences

The exception entry sequence involves multiple coordinated operations beyond the hardware stack frame push. After pushing the eight-register stack frame, the processor loads the PC with the exception handler address from the vector table while simultaneously loading the EXC_RETURN value into the LR register. This EXC_RETURN value encodes critical information including which stack pointer was active, whether the exception originated from thread or handler mode, and which stack frame format applies. The processor also updates various status registers including the IPSR to reflect the current exception number and the CONTROL register to indicate handler mode execution.

The exception exit sequence utilizes special return instructions, typically POP operations that restore the saved registers and trigger the EXC_RETURN mechanism. When the EXC_RETURN value indicates a valid return from exception, the processor performs an implicit stack pop of the eight-register frame and transitions back to thread mode. The specific return mechanism depends on whether returning to a floating-point state (requiring additional FPSCR restoration) and whether the original exception involved stack frame alignment adjustments. Proper implementation of exception exit sequences ensures complete context restoration and maintains processor state consistency across interrupt boundaries.

### Nested Interrupt Handling Implementation

Nested interrupt handling permits higher-priority interrupts to preempt currently executing interrupt service routines, enabling systems to meet stringent real-time deadlines. Implementation requires explicit firmware actions beyond the hardware-provided exception entry sequence. The ISR must save additional registers (beyond the automatic stack frame) that it will modify, typically including R4-R11 and any floating-point registers. The handler then sets the priority of the currently executing interrupt to a lower level before enabling nested interrupts through the PRIMASK or BASEPRI register.

When implementing nested interrupts, developers must carefully manage the stack to prevent overflow during deep nesting scenarios. Each nesting level consumes stack space equal to the manual register saves plus the hardware-pushed frame. The LR value must be preserved across nesting levels since it contains the EXC_RETURN information needed to properly exit each nested exception level. Common implementation patterns involve pushing the current LR onto the stack, loading a new EXC_RETURN value for the outer exception level, and enabling interrupts. Upon exiting nested handlers, the saved EXC_RETURN values must be restored in reverse order to ensure proper mode transitions.

### Stack Overflow Detection Mechanisms

Reliable embedded systems require mechanisms to detect and respond to stack overflow conditions before they cause unpredictable behavior or data corruption. The Cortex-M architecture provides optional stack limit checking through the PSPLIM and MSPLIM registers that compare the stack pointer against predefined boundaries before each push operation. When a push would cross the stack limit, a MemManage fault exception occurs rather than allowing uncontrolled memory access. This hardware-enforced boundary provides deterministic overflow detection compared to software-based approaches.

Firmware-based stack monitoring offers additional flexibility for applications requiring more sophisticated overflow handling. A common technique involves placing a known pattern (often called a stack canary) at the stack boundary and periodically checking whether this pattern remains intact. This approach can detect gradual stack growth that might not immediately trigger a fault but could eventually lead to corruption. Runtime monitoring systems may also track maximum stack usage during development through instrumentation code that records peak stack consumption, enabling proper sizing of stack allocations for production systems.

## Examples

### Example 1: ISR Prologue and Epilogue Implementation

Consider a typical ISR that performs moderate computational work requiring the use of registers R4-R7. The exception entry provides automatic saving of R0-R3, R12, LR, PC, and xPSR. The firmware must manually save R4-R7 in the prologue and restore them in the epilogue:

```c
void TIM2_IRQHandler(void) {
 // Prologue: Manual register saving
 __asm volatile (
 "PUSH {R4-R7, LR}\n" // Save callee-saved regs and LR
 );

 // Clear interrupt flag and process
 TIM2->SR &= ~TIM_SR_UIF;
 volatile uint32_t data = TIM2->DR;

 // Process data (using R0-R3 which were auto-saved)
 process_timer_event(data);

 // Epilogue: Register restoration
 __asm volatile (
 "POP {R4-R7, PC}\n" // Restore regs, use PC for return
 );
}
```

The PUSH operation in the prologue saves R4-R7 along with LR (containing EXC_RETURN) onto the stack. The POP operation in the epilogue restores R4-R7 and simultaneously loads the PC with the return address extracted from the saved LR, triggering the exception return mechanism. This implementation supports nested interrupts since the LR value is preserved on the stack, allowing proper return to either thread mode or an outer interrupt handler.

### Example 2: Nested Interrupt Stack Analysis

Analyzing stack usage during nested interrupts reveals critical design considerations. Assuming each nesting level saves four registers (R4-R7) plus LR manually, plus the eight-register hardware frame, each nesting level consumes 24 bytes of stack space:

```c
void HighPriority_IRQHandler(void) {
 __asm volatile ("PUSH {R4-R7, LR}");

 // Enable nested interrupts - lower priority handlers can preempt
 __enable_irq();

 // This section can be preempted by lower-priority interrupts
 process_high_priority_data();

 __asm volatile ("POP {R4-R7, PC}");
}

void MediumPriority_IRQHandler(void) {
 __asm volatile ("PUSH {R4-R7, LR}");

 // Process medium priority work
 handle_medium_priority_event();

 __asm volatile ("POP {R4-R7, PC}");
}
```

If HighPriority_IRQHandler is executing and gets preempted by MediumPriority_IRQHandler, the stack grows by 48 bytes (24 bytes per level). For a system with maximum three levels of nesting and each handler using 24 bytes, the worst-case stack requirement equals 72 bytes plus the original thread stack usage. This analysis demonstrates why firmware developers must calculate maximum stack depth during system design to prevent overflow during complex interrupt sequences.

### Example 3: Stack Depth Calculation for Real-Time System

A real-time control system requires analysis of worst-case stack usage to ensure reliable operation. Given the following interrupt configuration:

- Timer interrupt (highest priority): Uses R4-R7, calls subroutine
- UART interrupt (medium priority): Uses R4-R7, processes receive buffer
- ADC interrupt (low priority): Uses R4-R7 only

The maximum nesting depth occurs when Timer is executing and gets preempted by both UART and ADC interrupts. Stack consumption calculation:

- Hardware frame (exception entry): 8 registers × 4 bytes = 32 bytes
- Manual saves per ISR level: 5 registers (R4-R7, LR) × 4 bytes = 20 bytes
- Subroutine call in Timer handler (BL instruction): 4 bytes (LR save)

Total per nesting level: 32 + 20 + 4 = 56 bytes

Maximum stack growth: 3 levels × 56 bytes = 168 bytes

Adding a safety margin of 50% for stack growth beyond expected conditions yields a recommended stack reservation of 252 bytes for the interrupt stack. This calculation demonstrates the systematic approach required for professional embedded systems development.

## Exam Tips

When preparing for examinations on interrupt stack design, focus on understanding the complete exception sequence rather than memorizing isolated facts. Examiners frequently ask students to trace through exception entry and exit sequences, identifying which registers are saved at each stage and how the stack pointer changes.

Always distinguish between hardware-saved and software-saved registers in Cortex-M exceptions, as this distinction forms the basis for most analysis questions. Remember that the automatic stack frame contains exactly eight registers and is pushed only when transitioning from thread mode to handler mode.

Practice calculating worst-case stack depth for nested interrupt scenarios, as numerical problems testing this skill appear frequently in examinations. Include all contributions: hardware frame, manual saves, and any additional stack frames for function calls within handlers.

Understand the purpose and encoding of EXC_RETURN values, as questions frequently test whether students comprehend how the processor knows which stack pointer to use and which mode to return to upon exception completion.

Pay attention to the differences between MSP and PSP usage, and be able to explain scenarios where each is appropriate. Many examination questions present specific application requirements and ask which stack pointer configuration would best suit the system.

When answering questions about stack overflow detection, explain both hardware mechanisms (PSPLIM/MSPLIM) and software approaches (stack canaries), comparing their advantages and limitations in different application contexts.

Remember that vector table alignment requirements vary by device, but the general principle remains that the vector table must be aligned to a power-of-two boundary larger than the number of exception entries.
