# Interrupts – Interrupt Hardware

## Introduction

In modern computer systems, the processor must efficiently handle numerous peripheral devices that operate at vastly different speeds. Imagine a scenario where a user is typing on a keyboard while music plays in the background and data downloads from the internet. The processor cannot afford to constantly check each device for activity—this would waste precious CPU cycles. Instead, peripheral devices need a mechanism to signal the processor when they require attention. This is precisely what interrupts accomplish.

An interrupt is a hardware-generated signal that temporarily suspends the normal execution of a program and transfers control to a special routine called an Interrupt Service Routine (ISR). The ISR handles the specific event that triggered the interrupt—perhaps reading a keystroke from the keyboard or processing a network packet—and then returns control to the interrupted program. This asynchronous mechanism allows the CPU to remain productive rather than continuously polling devices for status changes. The hardware that enables this elegant communication between peripherals and the processor forms the backbone of efficient I/O handling in virtually all modern computing systems, from simple microcontrollers to sophisticated server systems.

Understanding interrupt hardware is essential for computer science students because it bridges the gap between low-level hardware and high-level software. When you write application code, you rarely think about interrupts, yet they underpin every interactive computing experience. The printer finishes a job and notifies the system; the network card receives data and wakes the operating system; the hard drive completes a read operation and alerts waiting software. Without interrupts, computers would be far less responsive and far more inefficient. This topic examines the hardware mechanisms that make this possible.

## Key Concepts

### Interrupt Mechanism Fundamentals

The interrupt mechanism operates through a carefully choreographed sequence of hardware signals and software responses. When a peripheral device needs processor attention, it raises an interrupt request line (IRQ) connected to the processor. The processor monitors these lines continuously during its normal execution cycle. When an interrupt request is detected and interrupts are enabled, the processor completes its current instruction, saves sufficient state to resume later, and begins executing the appropriate interrupt service routine.

The hardware components involved in this process include the interrupt request lines themselves, interrupt controllers that manage multiple interrupt sources and determine priority, the processor's interrupt handling unit, and memory structures that map interrupt requests to specific handler addresses. Each component plays a crucial role in ensuring interrupts are handled correctly, quickly, and without losing data or missing critical events.

### Interrupt Request Lines and Controllers

In most computer systems, multiple devices share a limited number of interrupt request lines. The processor typically supports only a small number of hardware interrupt pins—often just two or three. To accommodate many more devices, systems use an interrupt controller, such as the widely-used Intel 8259A Programmable Interrupt Controller (PIC) found in original IBM PC architectures.

The interrupt controller accepts multiple interrupt requests from different devices, implements a priority scheme to determine which request should be serviced first when multiple interrupts occur simultaneously, and sends a single interrupt signal to the processor. The controller also provides an interrupt vector—a numeric identifier that tells the processor which device requires attention. When the processor acknowledges the interrupt, the controller places this vector on the data bus, allowing the processor to locate the correct interrupt service routine.

Modern systems use more sophisticated interrupt controllers, including the Advanced Programmable Interrupt Controller (APIC) found in Pentium and later processors. The APIC supports more interrupt sources, enables processor-to-processor interrupts in multi-core systems, and allows for flexible priority and routing configurations. Understanding the 8259A PIC remains valuable pedagogically because it clearly illustrates the fundamental principles of interrupt control.

### Interrupt Vector Table

The interrupt vector table (IVT) or Interrupt Descriptor Table (IDT) in x86 systems is a data structure that maps interrupt request numbers to the addresses of their corresponding interrupt service routines. When an interrupt occurs, the processor uses the interrupt vector provided by the hardware to index into this table and fetch the address of the appropriate ISR.

In real-mode DOS systems, the IVT occupies the first 1KB of memory (addresses 00000h to 003FFh), with each of the 256 possible interrupts having a 4-byte entry containing a segment:offset pointer to its handler. In protected-mode and long-mode operation, the IDT uses more complex descriptors that include privilege levels and additional control information. The operating system initializes this table during boot, setting up handlers for hardware interrupts, software interrupts, and exception conditions.

### Types of Interrupts

Hardware interrupts are broadly categorized into maskable and non-maskable interrupts (NMI). Maskable interrupts can be temporarily ignored by the processor when the interrupt enable flag in the processor's status register is cleared. This allows critical code sequences to execute without interruption. The operating system carefully manages this flag to ensure important operations complete before interrupts are serviced.

Non-maskable interrupts (NMI) cannot be disabled by software and are reserved for critical events that require immediate attention, such as imminent power failure or catastrophic hardware errors. When an NMI occurs, the processor immediately transfers control to its designated handler regardless of the state of the interrupt enable flag. In x86 processors, NMI is typically associated with IRQ 2 (though this varies by system configuration).

Interrupts can also be classified by their triggering mechanism. Level-triggered interrupts remain active as long as the interrupt request line is held high. This simple mechanism can lead to issues where an interrupt is repeatedly triggered if not properly handled. Edge-triggered interrupts activate on a specific transition (rising or falling edge) of the signal and are less prone to this problem. Many modern systems use level-triggered interrupts with additional hardware logic to handle the complexities of multiple simultaneous requests.

### Interrupt Handling Sequence

When the processor receives an interrupt signal and interrupts are enabled, it follows a specific sequence of operations. First, the processor finishes executing the current instruction completely—this is crucial for maintaining correct program state. Next, the processor automatically pushes the current flags register, code segment register, and instruction pointer onto the stack. This allows the ISR to return to exactly the point where the interrupt occurred.

The processor then loads the new flags, code segment, and instruction pointer from the interrupt descriptor table entry corresponding to the interrupt number. Execution continues at the interrupt service routine. The ISR typically begins by saving additional processor registers that it will modify, performs the necessary device-specific operations, restores those registers, and executes the IRET (Interrupt Return) instruction to pop the saved state from the stack and resume the interrupted program.

This entire sequence occurs with no explicit instruction from the software—the hardware automatically handles the state save and transfer. This is what makes interrupts so efficient compared to software-implemented polling schemes.

### Priority and Interrupt Nesting

When multiple devices request interrupts simultaneously, the system must determine which to service first. The interrupt controller implements priority logic to resolve these conflicts. Higher-priority interrupts can preempt lower-priority ones, allowing critical events to be handled immediately.

Interrupt nesting refers to the ability of a higher-priority interrupt to interrupt the handling of a lower-priority interrupt. When this is allowed, the ISR for the first interrupt must save sufficient processor state to allow resumption, then enable interrupts before handling the device. This creates a more complex but more responsive system. Not all systems enable full interrupt nesting due to the increased complexity and potential for stack overflow or priority inversion problems.

## Examples

### Example 1: Keyboard Interrupt Handling

Consider a user pressing a key on a keyboard connected via the legacy PS/2 interface. The keyboard controller raises IRQ 1, which is routed through the 8259A PIC. The following sequence occurs:

1. The keyboard hardware sets the IRQ 1 line high on the PIC
2. The PIC checks its priority logic and, if IRQ 1 is the highest pending request, raises the INT pin on the processor
3. The processor finishes its current instruction, checks the interrupt enable flag, and if enabled, performs an interrupt acknowledge cycle
4. The PIC places interrupt vector 0x09 (IRQ 1 maps to vector 9 in the IBM PC) on the data bus
5. The processor uses this vector to index into the Interrupt Descriptor Table and fetches the address of the keyboard ISR
6. The processor pushes EFLAGS, CS, and EIP onto the stack and transfers to the ISR
7. The keyboard ISR reads the scancode from keyboard port 0x60, processes it, places it in a keyboard buffer, and signals the operating system
8. The ISR executes IRET, popping the saved state and resuming the interrupted program

This entire process typically completes in microseconds, allowing the system to appear responsive to user input.

### Example 2: Configuring the 8259A PIC

The 8259A PIC requires careful initialization through its control registers. Consider setting up the PIC with the following configuration: base interrupt vector of 0x20 for IRQ 0-7, fully nested mode (not cascaded), and edge-triggered operation. The initialization sequence involves sending three initialization command words (ICWs) followed optionally by operational command words (OCWs).

The first ICW (ICW1) tells the PIC that we are starting initialization, the PIC is cascaded (has a slave), and edge-triggered mode is used. This is done by writing 0x11 to port 0x20. ICW2 specifies the base vector—writing 0x20 sets IRQ 0 to vector 0x20, IRQ 1 to 0x21, and so on. ICW3 in cascaded mode specifies which IRQ line the slave PIC is connected to—writing 0x02 connects the slave to IRQ 2. Finally, ICW4 specifies the mode—in this case, 0x01 selects 8086/88 mode.

After initialization, the PIC begins accepting interrupt requests. However, interrupts from the PIC are still masked by default, so the operating system must unmask desired IRQ lines by writing to the interrupt mask register (IMR) before devices can generate interrupts.

### Example 3: Disk I/O with DMA and Interrupts

When the processor requests a disk read operation using Direct Memory Access (DMA), the interrupt mechanism plays a crucial role in signaling completion. The steps are:

1. The processor programs the DMA controller with the source address (disk), destination address (memory), and transfer length
2. The processor programs the disk controller to read the requested data
3. The processor may continue executing other instructions while the DMA controller handles the data transfer
4. When the DMA transfer completes, the disk controller raises an interrupt (typically IRQ 14 or 15 for IDE/ATA drives)
5. The interrupt service routine is invoked, indicating that the data is now available in memory
6. The ISR may notify the waiting process through operating system mechanisms that its I/O request is complete
7. The process that requested the data can now access it in memory

This pattern—initiating an operation and using interrupts to signal completion—allows the processor to overlap computation with I/O, dramatically improving system throughput.

## Exam Tips

1. Memorize the sequence of processor actions when an interrupt occurs: finish current instruction, save flags/CS/IP, fetch ISR address from IDT, execute ISR, return via IRET. This is a frequently asked question in DU examinations.

2. Understand the difference between maskable and non-maskable interrupts. Remember that NMI cannot be disabled and is used for critical events like power failure.

3. Be able to explain why interrupt-driven I/O is superior to polled I/O. Key points include: processor efficiency (no busy waiting), better response time, and ability to handle asynchronous events.

4. Know the role of the interrupt controller. The PIC accepts multiple IRQ inputs, implements priority resolution, and provides interrupt vectors to the processor.

5. Remember that interrupt vectors are used to locate the appropriate ISR in the interrupt vector table. The vector is an index, not a direct memory address.

6. Understand edge-triggered versus level-triggered interrupts. Edge-triggered interrupts activate on signal transitions, while level-triggered interrupts remain active as long as the signal is asserted.

7. Be prepared to draw and explain a diagram showing the relationship between devices, IRQ lines, the interrupt controller, and the processor.

8. Know that the processor automatically saves sufficient state (flags, CS, IP/EIP) on interrupt entry and restores it on IRET, making the interrupted program resumable without any explicit action by the software.