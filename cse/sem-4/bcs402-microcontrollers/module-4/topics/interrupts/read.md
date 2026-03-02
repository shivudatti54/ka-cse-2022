# Interrupts in ARM Cortex-M Microcontrollers

## Table of Contents

- [Interrupts in ARM Cortex-M Microcontrollers](#interrupts-in-arm-cortex-m-microcontrollers)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [ARM Exception Model](#arm-exception-model)
  - [Nested Vectored Interrupt Controller (NVIC)](#nested-vectored-interrupt-controller-nvic)
  - [Interrupt Latency and Response Time](#interrupt-latency-and-response-time)
  - [Interrupt Service Routine Implementation](#interrupt-service-routine-implementation)
- [Examples](#examples)
  - [Example 1: NVIC Configuration for Timer Interrupt](#example-1-nvic-configuration-for-timer-interrupt)
  - [Example 2: Calculating Interrupt Latency](#example-2-calculating-interrupt-latency)
  - [Example 3: Nested Interrupt Configuration](#example-3-nested-interrupt-configuration)
- [Exam Tips](#exam-tips)

## Introduction

Interrupts represent a fundamental mechanism in microcontroller systems that enables efficient handling of asynchronous events without continuous polling of peripheral devices. In the context of ARM Cortex-M processors, which form the backbone of modern embedded systems, interrupt handling is managed through the Nested Vectored Interrupt Controller (NVIC), a tightly integrated component of the processor architecture. Unlike earlier ARM architectures that required separate interrupt controllers, the Cortex-M family incorporates the NVIC directly into the processor core, providing deterministic interrupt response and flexible priority management.

The interrupt mechanism allows the processor to suspend its normal execution flow in response to internal or external events, execute a dedicated service routine, and then resume the interrupted task seamlessly. This approach significantly improves system responsiveness and CPU utilization compared to polling-based designs. The ARM Cortex-M architecture supports multiple interrupt sources, configurable priority levels, and various exception types including IRQ (Interrupt Request) and FIQ (Fast Interrupt Request), each designed to meet specific real-time performance requirements in embedded applications.

This module examines the interrupt architecture of ARM Cortex-M processors, covering exception handling mechanisms, vector table configuration, priority schemes, and practical implementation considerations for firmware development.

## Key Concepts

### ARM Exception Model

The ARM Cortex-M processor implements a hierarchical exception model where exceptions include resets, hardware interrupts (IRQs), fast interrupts (FIQs), memory faults, bus faults, usage faults, and system calls. When an exception occurs, the processor automatically transfers control to a predefined location in memory defined by the vector table. The vector table contains branch instructions or absolute addresses pointing to the appropriate exception handler routines. Each exception type has a specific position in the vector table, with reset vector at address 0x00000000, followed by NMI, hard fault, memory management fault, bus fault, usage fault, and then user-definable IRQ vectors.

Upon exception entry, the processor performs automatic context saving by pushing eight registers onto the stack: R0, R1, R2, R3, R12, LR, PC (return address), and xPSR (program status). This automatic stacking ensures that the handler can execute without manually preserving the application context. The processor also switches to Thread mode with privileged access level and sets the appropriate exception mask bits in the Program Status Register (PSR). The Link Register (LR) is loaded with a special value (EXC_RETURN) that encodes information about the stack frame and processor state before the exception, which is critical for proper exception return.

### Nested Vectored Interrupt Controller (NVIC)

The NVIC in ARM Cortex-M processors provides comprehensive interrupt management capabilities including configurable priority levels, interrupt enable/disable controls, and pending status registers. The NVIC supports up to 240 IRQ lines depending on the specific Cortex-M variant (Cortex-M0, M3, M4, M7), each of which can be individually enabled or disabled. Each interrupt has an 8-bit priority field, though implementation may use fewer bits (typically 3-4 bits for common microcontrollers), providing 2^n priority levels where n is the number of implemented bits.

The NVIC implements a priority grouping mechanism that divides the priority field into group priority (preemption priority) and subpriority components. When multiple pending interrupts become active simultaneously, the NVIC first selects the interrupt with highest group priority. If multiple interrupts share the same group priority, the subpriority determines the order of service. This mechanism enables designers to create nested interrupt schemes where higher-priority interrupts can preempt lower-priority ones, while interrupts of equal priority are serviced in a deterministic sequence. The NVIC also supports level-triggered and pulse-triggered interrupt inputs, accommodating various peripheral interrupt signaling conventions.

### Interrupt Latency and Response Time

Interrupt latency in ARM Cortex-M processors is defined as the time interval between the assertion of an interrupt signal and the execution of the first instruction of the corresponding interrupt service routine. The Cortex-M architecture is designed to achieve low and deterministic interrupt latency, typically requiring 12 cycles for a standard IRQ interrupt when no higher-priority exception is pending. This latency includes the cycles required for the processor to complete the current instruction, recognize the interrupt request, and begin execution of the vector fetch.

The interrupt response time comprises several components: the latency from interrupt assertion to interrupt acknowledgment by the processor, the time to fetch the exception vector, and the cycles required for automatic context saving. For FIQ interrupts, the latency is significantly reduced because FIQ has the highest priority (after NMI) and dedicated banked registers (R8-R12) that eliminate the need to save these registers on the stack. Additionally, the FIQ vector is located at the end of the vector table, allowing designers to place the entire FIQ handler at a fixed address without requiring vector table relocation. These optimizations enable FIQ response times as low as 4 cycles in ideal conditions, making FIQ suitable for time-critical applications such as motor control and high-speed data acquisition.

### Interrupt Service Routine Implementation

Interrupt Service Routines (ISRs) in ARM Cortex-M can be implemented in C or assembly language, with the compiler typically handling the necessary register saving and restoration through built-in attributes and prologue/epilogue sequences. When writing ISRs in C, developers use compiler-specific attributes such as `__attribute__((interrupt))` or `__irq` to inform the compiler that the function is an exception handler, causing appropriate prologue and epilogue code generation. The ISR must adhere to specific conventions: it should execute as quickly as possible, avoid calling blocking functions, and return using the special exception return mechanism.

The exception return mechanism is triggered by executing a return instruction (such as `BX LR` or `POP {PC}`) with the EXC_RETURN value in the LR register. This value tells the processor to pop the saved registers from the stack and restore the previous execution context. The EXC_RETURN value encodes whether the processor was in Thread or Handler mode, which stack was used (Main or Process), and whether floating-point state was saved. Proper handling of the return mechanism is essential; incorrect return sequences can lead to stack corruption, unpredictable behavior, or processor lock-up.

## Examples

### Example 1: NVIC Configuration for Timer Interrupt

Consider configuring the NVIC to enable a timer interrupt with medium priority on an ARM Cortex-M4 processor. The following C code demonstrates the complete configuration sequence:

```c
#define TIMER2_BASE_ADDR 0x40000000
#define TIMER2_IRQn 28

typedef struct {
 volatile uint32_t CR1;
 volatile uint32_t CR2;
 volatile uint32_t DIER;
 volatile uint32_t SR;
 volatile uint32_t CNT;
} TIMER_TypeDef;

#define TIMER2 ((TIMER_TypeDef *)TIMER2_BASE_ADDR)

// Timer interrupt handler
void TIM2_IRQHandler(void) {
 if (TIMER2->SR & 0x0001) { // Check update interrupt flag
 TIMER2->SR &= ~0x0001; // Clear flag
 // User application code here
 }
}

void timer_init(void) {
 // Configure timer for 1ms tick at 16MHz clock
 TIMER2->CR1 = 0x0000; // Disable timer during configuration
 TIMER2->ARR = 16000; // Auto-reload value for 1ms
 TIMER2->CNT = 0;
 TIMER2->DIER = 0x0001; // Enable update interrupt

 // Enable interrupt in NVIC with priority 5
 NVIC_SetPriority(TIMER2_IRQn, 5);
 NVIC_EnableIRQ(TIMER2_IRQn);

 TIMER2->CR1 = 0x0001; // Enable timer
}
```

In this example, `NVIC_SetPriority()` configures the interrupt priority by writing to the appropriate priority register in the NVIC, while `NVIC_EnableIRQ()` sets the enable bit in the NVIC's interrupt set-enable register. The priority value of 5 represents a medium priority level, allowing higher-priority interrupts to preempt this timer's ISR.

### Example 2: Calculating Interrupt Latency

Given an ARM Cortex-M3 system running at 72MHz clock frequency, calculate the worst-case interrupt latency for a standard IRQ interrupt:

**Solution:**

The interrupt latency in clock cycles consists of:

- Synchronization delay: 1 cycle maximum
- Pipeline flush: 3 cycles (for longest instructions like load-multiple)
- Stack push (8 registers): 8 cycles
- Vector fetch: 2 cycles
- Register loading: 1 cycle

Total cycles = 1 + 3 + 8 + 2 + 1 = 15 cycles (worst case)

At 72MHz:
Time = 15 cycles ÷ 72,000,000 cycles/second = 0.208 μs

For FIQ with banked registers (assuming 4-cycle latency):
Time = 4 cycles ÷ 72,000,000 = 0.056 μs

This demonstrates that FIQ provides approximately 3.7x faster response than standard IRQ for time-critical operations.

### Example 3: Nested Interrupt Configuration

To implement nested interrupts where a high-priority interrupt can preempt a lower-priority one, the handler must explicitly lower the priority mask:

```c
void HighPriority_IRQHandler(void) {
 // Save current PRIMASK state
 uint32_t primask = __get_PRIMASK();

 // Enable interrupts (clear PRIMASK)
 __enable_irq();

 // Now this handler can be preempted by higher priority interrupts
 // Perform time-critical operations

 // Restore PRIMASK state
 __set_PRIMASK(primask);
}

void LowPriority_IRQHandler(void) {
 // This handler can be preempted by HighPriority_IRQHandler
 // because it has lower NVIC priority

 // Longer processing here
 process_data();
}
```

The nested interrupt approach requires careful consideration of stack usage, as each level of nesting consumes additional stack space. The maximum nesting depth should be determined during system design to ensure adequate stack allocation.

## Exam Tips

1. **Vector Table Structure**: Remember that the vector table begins at address 0x00000000 (or 0x20000000 for devices with remapping) with the initial Stack Pointer value, followed by the Reset vector and then exception vectors in a fixed order.

2. **EXC_RETURN Values**: The LR register holds special EXC_RETURN values (0xFFFFFFF1, 0xFFFFFFF9, 0xFFFFFFFD) during exception handling that encode the return target. A common mistake is corrupting LR before returning from an ISR.

3. **Priority Grouping**: Understand how priority grouping divides the 8-bit priority field into group priority and subpriority. The grouping is configured via the Application Interrupt and Reset Control Register (AIRCR).

4. **Latency Components**: For exam questions on latency, remember to include all components: synchronization, instruction completion, stacking, vector fetch, and handler entry. FIQ is faster due to dedicated banked registers.

5. **Context Saving**: The automatic stacking saves only eight registers (R0-R3, R12, LR, PC, xPSR). If a handler uses R4-R11, these must be explicitly saved in the function prologue.

6. **Pending Bits**: The NVIC pending bits can be set manually for software-triggered interrupts. This is useful for testing and for implementing software interrupts.

7. **Tail Chaining**: The Cortex-M architecture implements tail chaining to optimize latency when returning from one exception to enter another immediately. This can reduce effective interrupt-to-interrupt time significantly.
