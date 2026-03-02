# Learning Objectives

After studying this topic, you should be able to:

1. Explain what an interrupt is and describe the fundamental difference between interrupt-driven I/O and polled I/O in terms of efficiency and responsiveness.

2. Identify and describe the hardware components involved in interrupt handling, including interrupt request lines, interrupt controllers, and the processor's interrupt mechanism.

3. Explain the role and function of an interrupt controller, using the 8259A PIC as a concrete example to illustrate priority resolution and vector generation.

4. Describe the complete sequence of operations that occurs when the processor handles an interrupt, from detecting the interrupt request to returning from the ISR.

5. Differentiate between maskable and non-maskable interrupts, explaining their purposes and the scenarios in which each is used.

6. Explain what an interrupt vector table is and how it is used to locate the appropriate interrupt service routine for a given interrupt.

7. Understand the concepts of interrupt priority and nesting, and explain how the system handles multiple simultaneous interrupt requests.