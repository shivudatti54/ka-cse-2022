# Interrupts – Interrupt Hardware - Summary

## Key Definitions and Concepts

- **Interrupt**: An asynchronous signal sent to the CPU by hardware indicating an event that requires immediate attention.
- **Interrupt Request (IRQ)**: A signal line connecting a peripheral device to the interrupt hardware.
- **Interrupt Service Routine (ISR)**: A specialized function executed in response to a specific interrupt.
- **Interrupt Controller**: Hardware that manages multiple interrupt requests, determines priority, and interfaces with the CPU.
- **Interrupt Vector Table**: A data structure containing addresses of ISRs indexed by interrupt vector numbers.
- **Interrupt Latency**: The time delay between interrupt request assertion and the start of ISR execution.
- **Maskable Interrupt**: An interrupt that can be temporarily disabled by the CPU.
- **Non-Maskable Interrupt (NMI)**: A critical interrupt that cannot be disabled.

## Important Formulas and Theorems

- **Interrupt Handling Sequence**: IRQ Asserted → CPU Completes Instruction → Check Interrupt Enable → Acknowledge → Get Vector → Save State → Execute ISR → Restore State → Resume Program
- **Priority Resolution**: When multiple IRQs are active, priority encoder selects the highest priority interrupt to service first.

## Key Points

- Interrupts allow peripherals to get CPU attention without continuous polling, improving system efficiency.
- Interrupt controllers like 8259A (PIC) and APIC manage multiple interrupt sources and handle priority resolution.
- Level-triggered interrupts remain active as long as the signal level is maintained; edge-triggered respond to transitions.
- The CPU saves its execution state (program counter, status register) before jumping to the ISR to ensure correct resumption.
- Interrupt vector tables provide mapping between interrupt numbers and handler addresses.
- Non-maskable interrupts are reserved for critical events like hardware failures.
- Daisy chaining and priority encoders are two common methods for resolving conflicts when multiple devices interrupt simultaneously.
- Interrupt latency is critical in real-time systems where timely response to events is mandatory.

## Common Mistakes to Avoid

- Confusing polling with interrupts—polling is CPU-driven while interrupts are device-driven.
- Forgetting that the CPU must save state before executing the ISR; failure to do so would corrupt the interrupted program.
- Misunderstanding level-triggered interrupts—they can cause repeated interrupts if not properly cleared by the ISR.
- Not recognizing that NMI cannot be disabled regardless of interrupt flag settings.

## Revision Tips

1. Draw the complete interrupt handling sequence from memory to ensure you understand each step.
2. Compare maskable vs non-maskable interrupts with concrete examples (keyboard vs memory parity error).
3. Memorize the functions of an interrupt controller—these frequently appear in exam questions.
4. Understand why interrupt latency matters, especially in embedded and real-time systems.
5. Practice explaining how the interrupt vector table enables the CPU to find the correct ISR quickly.