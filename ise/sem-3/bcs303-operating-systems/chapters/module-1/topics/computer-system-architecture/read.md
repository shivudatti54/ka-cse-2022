# Computer System Architecture

## Introduction

Computer System Architecture forms the foundational layer upon which Operating Systems are built. Understanding the architecture of a computer system is essential for any student of Computer Science because the Operating System serves as an interface between the user and the hardware. The architecture determines how efficiently the OS can manage resources, schedule processes, and coordinate between various hardware components.

The study of computer system architecture encompasses the design and organization of the major components of a computer system, including the Central Processing Unit (CPU), memory hierarchy, input/output systems, and the interconnection mechanisms that allow these components to communicate. For Operating Systems, this knowledge is crucial because the OS must effectively manage and allocate these hardware resources among multiple processes and users.

In the context of the University of Delhi's Computer Science curriculum, this topic establishes the groundwork for understanding subsequent concepts such as process management, memory management, and storage management. The relationship between hardware architecture and operating system design is symbiotic—the OS must be tailored to exploit the features of the underlying hardware architecture while providing abstractions that make the system user-friendly and efficient.

## Key Concepts

### 1. Basic Components of a Computer System

A computer system consists of four fundamental components that work in tandem:

**Central Processing Unit (CPU):** The CPU is the brain of the computer system. It executes instructions stored in memory and controls the operation of all other components. The CPU contains the Control Unit (CU), which directs the operation of the processor, and the Arithmetic Logic Unit (ALU), which performs arithmetic and logical operations. Modern CPUs feature multiple cores, allowing parallel processing and improved performance.

**Memory:** Memory in a computer system is organized in a hierarchy to balance speed, capacity, and cost. The hierarchy includes:
- **Register Memory:** Fastest but smallest, located within the CPU
- **Cache Memory:** High-speed memory that stores frequently accessed data
- **Primary Memory (RAM):** Main memory used for storing data and instructions currently in use
- **Secondary Storage:** Hard disks, SSDs, and other persistent storage devices

**Input/Output Devices:** These include all devices that allow data to be entered into the system (keyboard, mouse, scanners) or output results (monitors, printers, speakers). I/O devices operate at much slower speeds than the CPU, creating a significant speed mismatch that the OS must manage.

**System Bus:** The bus is the communication channel that connects all components of the computer system. The system bus typically consists of:
- **Data Bus:** Transfers actual data between components
- **Address Bus:** Carries memory addresses for data access
- **Control Bus:** Carries control signals and timing information

### 2. Instruction Execution Cycle

The CPU executes instructions through a fundamental cycle known as the Fetch-Decode-Execute cycle:

1. **Fetch:** The CPU fetches the instruction from memory whose address is stored in the Program Counter (PC)
2. **Decode:** The Control Unit decodes the instruction to determine what operation to perform
3. **Execute:** The ALU performs the operation specified by the instruction
4. **Store:** The result is stored back in memory or registers

This cycle repeats continuously, and the Operating System manages this process through process scheduling and context switching.

### 3. Interrupt-Driven Architecture

Modern computer systems use interrupts to handle asynchronous events. When an I/O device needs attention, it sends an interrupt signal to the CPU. The CPU halts its current execution, saves its state, and transfers control to an interrupt service routine (ISR) to handle the event. This mechanism allows the CPU to efficiently handle multiple I/O operations without constantly polling devices.

The OS manages interrupt handling through the Interrupt Descriptor Table (IDT) and provides device drivers that contain the specific ISRs for different hardware devices.

### 4. I/O Communication Techniques

The OS supports three primary methods for I/O communication:

**Programmed I/O:** The CPU actively polls devices and transfers data byte-by-byte. This method is simple but wastes CPU cycles.

**Interrupt-Driven I/O:** The CPU initiates I/O and continues with other tasks. The device interrupts the CPU when ready, allowing for more efficient CPU utilization.

**Direct Memory Access (DMA):** DMA controllers transfer data directly between I/O devices and memory without CPU intervention. This offloads data transfer overhead from the CPU, significantly improving system performance for large data transfers.

### 5. Multiprocessor and Multi-Core Architectures

Modern computer systems increasingly use multiprocessing architectures:

**Symmetric Multiprocessing (SMP):** Multiple processors share a common memory space and are controlled by a single OS. All processors are equal and can execute any task.

**Multi-Core Processors:** A single physical processor contains multiple independent processing cores, each capable of executing instructions independently. This approach offers the benefits of parallel processing while maintaining a single processor footprint.

**Cache Coherency:** In multiprocessor systems, maintaining consistency between cached copies of data in different processors' caches is critical. Hardware-level cache coherence protocols (like MESI) help ensure data consistency.

### 6. Memory Architecture and Addressing

The OS must manage memory through various addressing schemes:

**Physical Addressing:** The actual addresses in hardware memory
**Logical/Virtual Addressing:** Addresses used by programs, which the OS translates to physical addresses through the Memory Management Unit (MMU)

The separation between logical and physical addresses enables memory protection, virtual memory, and efficient sharing of physical memory among multiple processes.

## Examples

### Example 1: Calculating Effective Memory Access Time

Consider a computer system with the following memory hierarchy:
- L1 Cache: Access time = 1 ns, Hit rate = 95%
- Main Memory: Access time = 100 ns

Calculate the effective memory access time.

**Solution:**

The effective access time is calculated using the formula:
Effective Access Time = (Hit Rate × Cache Access Time) + (Miss Rate × Main Memory Access Time)

Given:
- Hit Rate = 95% = 0.95
- Miss Rate = 5% = 0.05
- Cache Access Time = 1 ns
- Main Memory Access Time = 100 ns

Calculation:
Effective Access Time = (0.95 × 1) + (0.05 × 100)
= 0.95 + 5
= 5.95 ns

This represents a significant improvement over accessing main memory directly (100 ns), demonstrating why cache memory is crucial for system performance.

### Example 2: Understanding Interrupt Handling

Suppose a user presses a key on the keyboard while the CPU is executing a program. Describe the sequence of events that occurs.

**Solution:**

1. **Interrupt Generation:** The keyboard controller detects the key press and generates an interrupt request (IRQ) signal on the control bus.

2. **Interrupt Acknowledgment:** The CPU completes its current instruction, then checks for pending interrupts. It acknowledges the interrupt by reading an interrupt acknowledgment signal.

3. **Context Saving:** The CPU saves the current state (program counter, processor status, and other registers) onto the stack or in a control register.

4. **Interrupt Vector Lookup:** The CPU uses the interrupt number to look up the corresponding interrupt service routine (ISR) address in the Interrupt Descriptor Table (IDT).

5. **ISR Execution:** Control transfers to the keyboard driver ISR, which reads the key code from the keyboard controller's data register.

6. **Processing:** The OS processes the key press, possibly updating the active application or storing the character in a buffer.

7. **Context Restoration:** After the ISR completes, the CPU restores the saved state and resumes execution of the interrupted program.

### Example 3: DMA vs. Interrupt-Driven I/O

A disk read operation needs to transfer 4 KB of data to memory. Compare the CPU overhead for interrupt-driven I/O versus DMA, assuming:
- Each interrupt handling requires 500 CPU cycles
- DMA transfer requires setup of 1000 CPU cycles
- Disk can transfer 1 byte per interrupt

**Solution:**

**Interrupt-Driven I/O:**
- Number of interrupts required = 4 KB = 4096 interrupts (1 byte per interrupt)
- CPU cycles = 4096 × 500 = 2,048,000 cycles

**DMA:**
- Setup overhead = 1000 cycles
- Data transfer handled by DMA controller = 0 CPU cycles during transfer
- Total CPU cycles = 1000 cycles

**Comparison:**
The DMA approach requires only 1000 cycles compared to 2,048,000 cycles for interrupt-driven I/O. This represents a savings of 99.95% in CPU overhead, demonstrating why DMA is essential for efficient I/O operations in modern systems.

## Exam Tips

1. **Know the Fetch-Decode-Execute Cycle:** This is a fundamental concept that frequently appears in exams. Be prepared to explain each step and its significance for OS process management.

2. **Understand Interrupt Types:** Be familiar with hardware interrupts, software interrupts, and exceptions. Know the difference between maskable and non-maskable interrupts (NMI).

3. **Memory Hierarchy is Crucial:** Understand the trade-offs between speed, capacity, and cost in memory design. Be able to explain why caches improve performance.

4. **I/O Methods Comparison:** Know the differences between programmed I/O, interrupt-driven I/O, and DMA. Understand when each is appropriate and their respective advantages and disadvantages.

5. **Bus Architectures:** Understand the three types of system buses (data, address, control) and their roles in computer communication.

6. **Multiprocessor Concepts:** Be familiar with SMP architecture and multi-core processing, as these are increasingly important in modern computing environments.

7. **DMA Controllers:** Understand how DMA works to offload I/O transfers from the CPU, and why this is important for system performance.

8. **Relationship with OS:** Remember that the OS manages all these hardware components. Understand how OS abstractions relate to underlying hardware architecture.