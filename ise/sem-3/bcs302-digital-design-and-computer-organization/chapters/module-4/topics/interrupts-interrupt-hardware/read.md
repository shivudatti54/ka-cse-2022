# Interrupts – Interrupt Hardware

## Introduction

In modern computer systems, the processor must interact with numerous peripheral devices that operate at vastly different speeds. A keyboard may require attention only when a key is pressed, a hard disk may need to transfer large blocks of data, and network cards must handle incoming packets at unpredictable intervals. The traditional method of polling—where the processor repeatedly checks each device to see if it needs attention—is extremely inefficient because it wastes precious CPU cycles on devices that rarely require service.

The interrupt mechanism provides an elegant solution to this problem. Instead of the processor constantly checking devices, peripheral devices notify the processor when they need attention by sending an interrupt signal. This allows the CPU to execute its normal program (called the main program or foreground task) until an interrupt occurs, at which point it temporarily suspends execution, handles the interrupt request, and then resumes the interrupted program. This asynchronous event-driven approach dramatically improves system efficiency and responsiveness.

The hardware responsible for managing interrupts is crucial to the proper functioning of any computer system. Understanding interrupt hardware is essential for computer science students because it forms the backbone of operating systems, device drivers, and real-time systems. In this chapter, we explore the hardware components that enable the interrupt mechanism, including interrupt controllers, interrupt lines, vector tables, and priority resolution logic.

## Key Concepts

### Basic Interrupt Mechanism

The fundamental interrupt mechanism involves three key entities: the CPU, the peripheral device, and interrupt hardware. When a peripheral device requires attention, it asserts an interrupt request (IRQ) line connected to the processor. The CPU completes its current instruction execution and then checks if interrupts are enabled. If enabled, the CPU acknowledges the interrupt and transfers control to an interrupt service routine (ISR) that handles the specific device.

The hardware support for interrupts includes several critical components. The interrupt request line carries the signal from the peripheral to the CPU. The interrupt acknowledge line allows the CPU to confirm receipt of the interrupt. The interrupt vector table stores the addresses of different interrupt service routines, enabling the CPU to quickly locate the appropriate handler for each type of interrupt.

### Interrupt Controller

The interrupt controller is a dedicated hardware component that manages multiple interrupt requests from various peripherals. In systems with many devices, a single CPU interrupt line would be insufficient. The interrupt controller acts as an intermediary, collecting multiple interrupt requests, determining their priority, and presenting them to the processor in an organized manner.

The 8259A programmable interrupt controller (PIC) is a classic example widely used in x86 systems. It can manage up to eight interrupt request lines and can be cascaded to handle up to 64 interrupts. The PIC performs several essential functions: it masks individual interrupts, assigns priority levels to different interrupt sources, and provides an interrupt vector number to the CPU when an interrupt is acknowledged.

Modern systems use Advanced Programmable Interrupt Controllers (APICs) that offer greater flexibility and scalability. APICs support more interrupt lines, allow dynamic assignment of interrupt priorities, and can be distributed across multiple processors in symmetric multiprocessing (SMP) systems.

### Interrupt Lines and Signal Types

Interrupt lines are physical connections between devices and the interrupt hardware. These lines can be categorized based on how they are triggered. Level-triggered interrupts are asserted when the interrupt line maintains a specific voltage level. As long as the line remains at that level, the interrupt remains active. This type is susceptible to spurious interrupts if the device does not properly deassert the signal.

Edge-triggered interrupts are activated by a transition in the signal, typically from low to high. These are less prone to spurious interrupts but may miss brief pulses if the CPU is not checking at that exact moment. Many modern systems use a hybrid approach that combines both triggering methods.

The distinction between maskable and non-maskable interrupts (NMI) is also crucial. Maskable interrupts can be temporarily disabled by the CPU using the interrupt flag in the processor status register. Non-maskable interrupts cannot be disabled and are reserved for critical events like hardware failures or power supply issues.

### Interrupt Vector Tables

When an interrupt occurs, the CPU must determine which interrupt service routine to execute. The interrupt vector table provides this mapping. Each interrupt source is assigned a unique interrupt vector number, which serves as an index into the vector table. The table contains the memory addresses of the corresponding interrupt service routines.

In simple systems, the vector table might be fixed in read-only memory, with each entry containing a jump instruction to the appropriate ISR. More sophisticated systems allow the operating system to modify the vector table dynamically, enabling flexible handling of different devices and supporting hot-plugging of hardware.

### Priority and Daisy Chaining

When multiple devices assert interrupt requests simultaneously, the system must determine which one to service first. Hardware priority encoders resolve this conflict by examining all active interrupt requests and selecting the highest-priority one. The priority scheme can be fixed (static priority) or dynamic, where priority changes based on recent interrupt activity.

Daisy chaining is an alternative approach where devices are connected in a series. Each device has an interrupt output connected to the interrupt input of the next device. When an interrupt occurs, the signal propagates through the chain until it reaches a device that can handle it. This simpler design was common in early computer systems but offers less flexibility than centralized priority schemes.

### Interrupt Acknowledgment and Handling Sequence

The complete interrupt handling sequence involves several steps. First, the peripheral asserts its interrupt request line. The interrupt controller (if present) receives this request and determines priority. When the CPU is ready to handle interrupts, it acknowledges the interrupt request. The interrupt controller then provides the interrupt vector number. The CPU uses this vector to locate the appropriate interrupt service routine in the vector table. The processor saves the current program counter and status information on the stack. Control transfers to the ISR, which executes the necessary handling code. Upon completion, the ISR restores the saved state, and the CPU resumes execution of the interrupted program.

This entire sequence must happen quickly to minimize interrupt latency—the time between when an interrupt is asserted and when the ISR begins execution. Real-time systems impose strict deadlines on interrupt latency to ensure timely response to critical events.

## Examples

### Example 1: Understanding Interrupt Priority Resolution

Consider a system with three devices: a keyboard (priority 1), a mouse (priority 2), and a hard disk (priority 3), where higher numbers indicate higher priority. Assume the keyboard and hard disk both request interrupts simultaneously.

The priority encoder examines the three interrupt request lines. It sees that both IRQ1 (keyboard) and IRQ3 (hard disk) are active. Since the hard disk has priority 3 (highest), the encoder outputs the vector number for the hard disk interrupt. The CPU services the hard disk first, handling the data transfer. After completing the hard disk ISR, the CPU checks for pending interrupts and finds the keyboard request still active, so it then services the keyboard interrupt.

This example demonstrates how hardware priority resolution ensures that more important or time-critical devices are served first when multiple interrupts occur simultaneously.

### Example 2: Tracing the Interrupt Handling Sequence

Suppose a user presses a key on the keyboard while the CPU is executing a program calculating Fibonacci numbers. The following sequence occurs:

1. The keyboard controller detects the key press and asserts IRQ1.
2. The interrupt controller receives the request and, if not masked, passes it to the CPU.
3. The CPU finishes executing the current instruction (say, calculating the 1000th Fibonacci number).
4. The CPU checks its interrupt enable flag. Finding it set, it acknowledges the interrupt.
5. The interrupt controller provides vector number 9 (standard keyboard vector on PC architecture).
6. The CPU saves its current program counter and processor status on the stack.
7. The CPU reads the address from interrupt vector table entry 9.
8. Control transfers to the keyboard ISR, the scan which reads code from the keyboard controller.
9. The ISR stores the scan code in a buffer and signals a waiting process.
10. The ISR restores the saved state from the stack.
11. The CPU resumes execution of the Fibonacci calculation program from where it left off.

This example illustrates how the interrupt mechanism allows the CPU to seamlessly switch between its main task and interrupt handling without losing program state.

### Example 3: Maskable vs Non-Maskable Interrupts

In a computer system, the NMI line might be connected to a parity error detector or a critical temperature sensor. When a parity error occurs in memory, the memory controller asserts NMI. Regardless of what program is running, the CPU must immediately handle this potentially catastrophic error.

Unlike maskable interrupts (like keyboard or mouse) which can be temporarily disabled during critical sections of code (such as context switching in an operating system), NMI cannot be disabled. This ensures that fatal hardware errors are never ignored, even when the system is in a sensitive state. The NMI handler typically logs the error and may initiate an orderly system shutdown to prevent data corruption.

## Exam Tips

1. **DIFFERENTIATE BETWEEN POLLING AND INTERRUPTS**: In exams, clearly explain that polling continuously checks devices (wastes CPU cycles) while interrupts allow devices to notify the CPU (efficient). Many questions ask for advantages of interrupts over polling.

2. **KNOW THE INTERRUPT HANDLING SEQUENCE**: Memorize the exact sequence: interrupt request → CPU acknowledges → CPU saves state → fetch ISR address → execute ISR → restore state → resume. This is a frequently asked question.

3. **UNDERSTAND INTERRUPT LATENCY**: Be prepared to define interrupt latency as the time between interrupt request and ISR execution. Real-time systems require minimal latency.

4. **EXPLAIN INTERRUPT CONTROLLER FUNCTIONS**: List the functions: collecting IRQ signals, determining priority, providing interrupt vectors to CPU, masking interrupts.

5. **DISTINGUISH MASKABLE AND NON-MASKABLE INTERRUPTS**: Remember that maskable interrupts can be enabled/disabled using the interrupt flag (IF) in the processor status word, while NMI cannot be disabled.

6. **LEVEL-TRIGGERED VS EDGE-TRIGGERED**: Know that level-triggered interrupts are sensitive to signal level (can cause repeated interrupts if not cleared), while edge-triggered respond to signal transitions.

7. **INTERRUPT VECTOR TABLE PURPOSE**: Understand that this table maps interrupt request numbers to ISR addresses, enabling the CPU to quickly locate the correct handler.

8. **RELEVANCE TO OPERATING SYSTEMS**: Connect this topic to OS concepts—interrupt handlers are the basis for device drivers, and understanding interrupts helps explain how the OS achieves multiprogramming.