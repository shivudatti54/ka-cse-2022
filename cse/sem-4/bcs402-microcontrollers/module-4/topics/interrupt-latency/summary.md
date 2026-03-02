# Interrupt Latency - Summary

## Key Definitions and Concepts

- **Interrupt Latency**: The time interval between the generation of an interrupt request (IRQ) and the execution of the first instruction of the corresponding interrupt service routine (ISR)

- **Detection Latency**: Time required for the processor to detect that an interrupt has occurred

- **Completion Latency**: Time taken for the currently executing instruction to complete before the processor can respond to the interrupt

- **Context Saving Latency**: Time needed to save processor state (registers, PC, status flags) before transferring control to ISR

- **Vector Fetching Latency**: Time required to fetch the interrupt vector address and load the ISR starting address

## Important Formulas and Theorems

- **8051 Machine Cycle**: 1 machine cycle = 12 oscillator periods
- **Total Latency** = Completion Latency + Vector Fetch Latency + Context Save Latency
- **Maximum Latency** = (Maximum Instruction Cycles + Vector Cycles + Context Save Cycles) × Machine Cycle Time
- At 8051 clock frequency f, machine cycle time = 12/f seconds

## Key Points

1. Interrupt latency must be deterministic and bounded for real-time systems

2. The 8051 requires 1-4 machine cycles to complete current instruction plus 2 cycles for vector fetch and 2-4 cycles for context saving

3. Complex instructions (MUL, DIV) significantly increase latency due to their multi-cycle execution

4. Interrupt nesting allows higher priority interrupts to preempt lower priority ISR execution

5. Register banking in 8051 reduces context saving overhead by providing quick register set switching

6. Global interrupt disable during critical sections increases effective latency for pending interrupts

7. Flash wait states and external memory access can substantially increase interrupt latency

8. DMA controllers can reduce CPU interrupt burden by handling data transfers independently

## Common Mistakes to Avoid

1. Confusing interrupt latency with interrupt response time or ISR execution time

2. Forgetting that one 8051 machine cycle equals 12 clock periods, not 1

3. Assuming interrupt latency is constant - it varies based on instruction type and system state

4. Ignoring the impact of interrupt priority and nesting on latency calculations

5. Not considering that context saving requirements differ based on architecture

## Revision Tips

1. Practice calculating 8051 latency for different instruction types at various clock frequencies

2. Memorize the formula: Total Machine Cycles = Instruction Cycles + Vector Fetch + Context Save

3. Remember that edge-triggered external interrupts in 8051 have lower latency than level-triggered

4. Review 8051 interrupt vector addresses (External0: 0003H, Timer0: 000BH, External1: 0013H, Timer1: 001BH, Serial: 0023H)

5. Focus on understanding the relationship between clock frequency, machine cycles, and actual time in microseconds
