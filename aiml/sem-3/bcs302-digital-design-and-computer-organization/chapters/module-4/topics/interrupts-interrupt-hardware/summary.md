# Interrupts – Interrupt Hardware - Summary

## Key Definitions and Concepts

- **Interrupt**: A hardware-generated signal that temporarily suspends normal program execution and transfers control to an Interrupt Service Routine (ISR)
- **Interrupt Request Line (IRQ)**: A dedicated line through which peripheral devices signal the processor when they require attention
- **Interrupt Controller**: Hardware (like the 8259A PIC) that manages multiple interrupt sources, implements priority, and provides interrupt vectors to the processor
- **Interrupt Service Routine (ISR)**: A special software routine that executes in response to an interrupt to handle the requesting device
- **Interrupt Vector**: A numeric identifier that indexes into the interrupt vector table to locate the appropriate ISR
- **Maskable Interrupt**: An interrupt that can be disabled by clearing the interrupt enable flag in the processor
- **Non-Maskable Interrupt (NMI)**: A critical interrupt that cannot be disabled and is used for events like power failure

## Important Formulas and Theorems

No specific formulas apply to this topic. The key relationships are logical and architectural rather than mathematical:

- Processor monitors IRQ lines continuously during execution
- Interrupt controller prioritizes among multiple simultaneous requests
- Interrupt vector = index into IVT/IDT = address of ISR
- Priority determines which interrupt is serviced first when multiple requests exist

## Key Points

1. Interrupts allow devices to alert the processor asynchronously without requiring continuous polling, significantly improving system efficiency.

2. The complete interrupt handling sequence is: detect interrupt → finish current instruction → save processor state → fetch ISR address → execute ISR → restore state → resume interrupted program.

3. The 8259A PIC manages up to 8 IRQ lines, implements priority resolution, and translates IRQ numbers to interrupt vectors for the processor.

4. The processor automatically saves flags, code segment, and instruction pointer on interrupt entry, enabling transparent return to the interrupted program.

5. Level-triggered interrupts remain active as long as the signal is high; edge-triggered interrupts activate only on signal transitions.

6. Non-maskable interrupts (NMI) bypass the interrupt enable flag and are reserved for critical system events requiring immediate attention.

7. The Interrupt Descriptor Table (IDT) maps interrupt numbers to the addresses of their respective service routines.

8. Interrupt nesting allows higher-priority interrupts to preempt lower-priority ones, enabling responsive handling of critical events.

## Common Mistakes to Confuse or Avoid

1. Confusing interrupt vectors with memory addresses: the vector is an index or number used to look up the actual handler address in the IDT.

2. Forgetting that the processor automatically saves state on interrupt entry—students sometimes incorrectly assume software must save all registers.

3. Believing interrupts can occur between any two instructions: the processor completes the current instruction before checking for pending interrupts.

4. Confusing the interrupt controller with the processor—the controller manages interrupt sources; the processor handles the interrupt.

## Revision Tips

1. Draw a complete diagram showing the flow from peripheral device → IRQ line → interrupt controller → processor → ISR, and verbally explain each step.

2. Create a table comparing polled I/O versus interrupt-driven I/O, focusing on efficiency, response time, and hardware complexity.

3. Memorize the exact sequence of actions the processor takes when handling an interrupt—this is a frequently examined topic.

4. Review the initialization sequence for the 8259A PIC as it demonstrates the programmable nature of interrupt hardware.