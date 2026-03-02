# Computer System Organization

## Introduction

Computer System Organization forms the foundational bedrock upon which modern computing is built. Understanding how the various hardware components of a computer system work together is essential for any computer science student, as it provides the context within which operating systems function. When we study operating systems, we are essentially studying the software that manages and coordinates the hardware resources of a computer system.

A computer system consists of three primary components: the Central Processing Unit (CPU) that performs computations, the memory subsystem that stores data and instructions, and the Input/Output (I/O) subsystem that enables communication with the external world. The way these components are organized and how they interact with each other determines the overall performance, efficiency, and capabilities of the computer system. In the context of operating systems, this organization is critical because the OS must effectively manage these hardware resources, schedule processes, allocate memory, and handle I/O operations seamlessly.

This topic explores the internal structure and organization of computer systems, examining how data flows between components, how instructions are executed, and how the different parts of the system communicate. This knowledge is prerequisite to understanding operating system concepts such as process management, memory management, and device handling.

## Key Concepts

### 1. Basic Structure of a Computer System

A computer system can be visualized as having three main subsystems connected through a common bus:

- **Central Processing Unit (CPU)**: The brain of the computer that executes instructions. It consists of the Control Unit, Arithmetic Logic Unit (ALU), and registers.

- **Memory Subsystem**: Includes Primary Memory (RAM, ROM) for temporary storage and Secondary Memory (hard disks, SSDs) for permanent storage.

- **Input/Output Subsystem**: Comprises all devices that allow the computer to communicate with the external environment, including keyboards, monitors, printers, network cards, and storage devices.

The **System Bus** serves as the communication pathway connecting these three subsystems, carrying address, data, and control signals between components.

### 2. Central Processing Unit (CPU) Architecture

The CPU is the most critical component of any computer system. Its architecture comprises several key elements:

**Control Unit (CU)**: The control unit directs the operation of the processor. It fetches instructions from memory, decodes them, and generates control signals to execute the operations. The control unit uses the program counter (PC) to keep track of the next instruction to execute and the instruction register (IR) to hold the currently executing instruction.

**Arithmetic Logic Unit (ALU)**: The ALU performs all arithmetic operations (addition, subtraction, multiplication, division) and logical operations (AND, OR, NOT, comparisons). It operates on data stored in registers and returns results back to registers or memory.

**Registers**: These are small, high-speed storage locations within the CPU used for temporary data storage during instruction execution. Important registers include:

- **Program Counter (PC)**: Holds the address of the next instruction to be fetched
- **Instruction Register (IR)**: Holds the currently executing instruction
- **Accumulator (ACC)**: A special-purpose register used for arithmetic and logical operations
- **Memory Address Register (MAR)**: Holds the memory address being accessed
- **Memory Data Register (MDR)**: Holds data being transferred to or from memory
- **Index Register**: Used for addressing modes
- **Stack Pointer (SP)**: Points to the top of the stack in memory

### 3. Instruction Cycle

The CPU executes instructions through a cycle known as the instruction cycle or fetch-decode-execute cycle. This cycle consists of two main phases:

**Fetch Phase**:
1. The Program Counter (PC) contains the address of the next instruction
2. The address is copied to the Memory Address Register (MAR)
3. The control unit sends a READ signal to memory
4. The instruction is fetched from memory and placed in the Memory Data Register (MDR)
5. The instruction is transferred to the Instruction Register (IR)
6. The Program Counter is incremented to point to the next instruction

**Execute Phase**:
1. The Control Unit decodes the instruction to determine what operation to perform
2. If the instruction requires data from memory, the address is placed in MAR and data is fetched
3. The ALU performs the operation specified by the instruction
4. The result is stored in the accumulator or other specified register
5. The status flags are updated based on the result
6. The cycle repeats with the next instruction

### 4. Memory Hierarchy

Computer systems use a hierarchy of memory types to balance speed, capacity, and cost:

**Primary Memory (Main Memory)**:
- **Random Access Memory (RAM)**: Volatile memory that can be read and written. It is the main working memory where programs and data are stored while being processed.
- **Read-Only Memory (ROM)**: Non-volatile memory that contains permanently stored instructions, such as the bootstrap program.

**Cache Memory**: A small, high-speed memory located between the CPU and main memory. It stores frequently accessed data and instructions to reduce the time the CPU waits for memory accesses. Cache memory operates on the principle of locality:

- **Temporal Locality**: Recently accessed items are likely to be accessed again
- **Spatial Locality**: Items near recently accessed items are likely to be accessed soon

Cache levels typically include:
- **L1 Cache**: Smallest and fastest, usually within the CPU chip
- **L2 Cache**: Larger and slower, may be on the CPU or motherboard
- **L3 Cache**: Largest and slowest, shared among CPU cores

**Secondary Storage**: Non-volatile storage devices like hard disk drives (HDD) and solid-state drives (SSD) that provide permanent storage for data and programs.

### 5. I/O Organization

Input/Output devices enable the computer system to interact with the external world. I/O organization involves:

**I/O Devices**: Categorized into three types:
- **Input Devices**: Keyboard, mouse, scanner, microphone
- **Output Devices**: Monitor, printer, speaker
- **Storage Devices**: Hard disk, SSD, optical drives, USB drives

**I/O Controllers**: Special-purpose processors that manage communication between the CPU and I/O devices. They handle device-specific details and provide a uniform interface to the CPU.

**I/O Techniques**:
- **Programmed I/O**: CPU directly controls I/O operations, actively waiting for completion
- **Interrupt-Driven I/O**: Device notifies CPU when ready, allowing CPU to perform other tasks
- **Direct Memory Access (DMA)**: DMA controller transfers data directly between I/O devices and memory without CPU intervention

### 6. Bus Structure

A bus is a set of parallel wires that transmit data, addresses, and control signals. Computer systems use several types of buses:

**System Bus**: Connects the CPU, memory, and I/O devices. It includes:
- **Data Bus**: Carries actual data between components (bidirectional)
- **Address Bus**: Carries memory addresses for read/write operations (unidirectional from CPU)
- **Control Bus**: Carries control signals like READ, WRITE, MEMORY ACCESS, and INTERRUPT signals

**Expansion Buses**: Allow connection of additional components:
- **PCI Express (PCIe)**: High-speed bus for graphics cards and high-bandwidth devices
- **Universal Serial Bus (USB)**: Standard for connecting peripheral devices
- **SATA**: Interface for storage devices

### 7. Interrupts and Interrupt Handling

An interrupt is a signal to the CPU indicating an event that requires immediate attention. Interrupts allow devices to communicate with the CPU without continuous polling.

**Types of Interrupts**:
- **Hardware Interrupts**: Generated by external devices (keyboard, mouse, timer)
- **Software Interrupts**: Generated by programs executing instructions (system calls)
- **Internal Interrupts**: Generated by CPU conditions (division by zero, overflow, page fault)

**Interrupt Handling Process**:
1. Device raises an interrupt request (IRQ)
2. CPU finishes current instruction
3. CPU saves current state (program counter, flags)
4. CPU identifies the interrupt source
5. CPU executes the appropriate interrupt service routine (ISR)
6. CPU restores the saved state and continues execution

The **Interrupt Vector Table** maps interrupt types to their corresponding service routines.

## Examples

### Example 1: Tracing Instruction Execution

Consider the assembly instruction: `ADD [500], AX`

This instruction adds the contents of the AX register to the value stored at memory address 500 and stores the result at address 500. Let's trace through the fetch-decode-execute cycle:

**Fetch Cycle**:
1. PC contains address 1000 (location of this instruction)
2. MAR ← 1000
3. Memory READ operation initiated
4. Instruction fetched from memory address 1000
5. MDR ← "ADD [500], AX"
6. IR ← MDR contents
7. PC ← PC + 1 (now 1001)

**Decode Phase**:
1. Control unit decodes "ADD [500], AX"
2. Identifies it as a memory-addressed ADD operation
3. Determines source is memory location 500 and register AX

**Execute Phase**:
1. MAR ← 500 (address of operand)
2. Memory READ initiated
3. Operand fetched from address 500 into MDR
4. MDR contents moved to ALU
5. AX register contents moved to ALU
6. ALU performs addition
7. Result stored back to MDR
8. MAR ← 500
9. Memory WRITE initiated
10. Result stored at memory address 500

This example demonstrates how the CPU orchestrates memory access and arithmetic operations through its internal registers and the system bus.

### Example 2: Understanding Cache Locality

Suppose a program accesses an array element by element in a loop:

```
for (i = 0; i < 1000; i++)
    sum += array[i];
```

**Temporal Locality**: The variable `sum` is accessed repeatedly in each iteration, so it likely remains in cache after first access.

**Spatial Locality**: Array elements are accessed sequentially. When `array[0]` is fetched, the cache controller loads not just that byte but an entire cache line bytes). This means (typically 64 subsequent accesses to `array[1]`, `array[2]`, etc., will find their data already in cache, dramatically reducing memory access time.

If the array were 1000 integers (4000 bytes) and cache line size is 64 bytes:
- Without cache: 1000 main memory accesses
- With cache: Only the first access to each cache line causes a miss (approximately 4000/64 = 63 misses)

This demonstrates why understanding memory hierarchy is crucial for writing efficient programs.

### Example 3: DMA vs. Programmed I/O

Scenario: Copying 1MB of data from a hard disk to main memory.

**Programmed I/O Approach**:
1. CPU issues READ command to disk controller
2. CPU polls disk controller in a loop, waiting for data ready
3. For each 4-byte word: CPU reads from disk buffer, writes to memory
4. CPU repeats until all data transferred

CPU involvement: Continuous polling, cannot perform other tasks

**DMA Approach**:
1. CPU sets up DMA controller: source address, destination address, transfer size
2. CPU issues START TRANSFER command to DMA controller
3. CPU continues executing other programs
4. DMA controller handles data transfer directly between disk and memory
5. DMA controller sends interrupt to CPU when transfer completes

CPU involvement: Only for setup and completion notification, can perform other tasks during transfer

This example illustrates how hardware organization directly impacts system efficiency and multitasking capabilities.

## Exam Tips

1. **Understand the Fetch-Decode-Execute Cycle**: This is a fundamental concept that frequently appears in exams. Be able to trace through each step and explain the purpose of each register involved.

2. **Differentiate Between Bus Types**: Remember that the data bus is bidirectional, while the address bus is unidirectional (from CPU to memory). The control bus carries mixed signals in both directions.

3. **Cache Memory Concepts**: Know the difference between temporal and spatial locality, and explain how cache uses these principles to improve performance.

4. **Interrupt Handling Steps**: Be able to list and explain the sequence of events when an interrupt occurs, including state saving and restoration.

5. **DMA Advantages**: Understand why DMA is preferred over programmed I/O for bulk data transfers—specifically, it allows the CPU to perform other tasks during transfer.

6. **Register Functions**: Memorize the purposes of key CPU registers like PC, IR, MAR, MDR, and ACC. Exams often ask about their roles in instruction execution.

7. **Memory Hierarchy Performance**: Understand the trade-offs between speed, capacity, and cost in the memory hierarchy. Know why cache is needed despite having main memory.

8. **Distinguish I/O Techniques**: Be clear about the differences between programmed I/O, interrupt-driven I/O, and DMA—know when each is appropriate.

9. **ISA and Microarchitecture**: Understand the relationship between Instruction Set Architecture (the programmer's view) and microarchitecture (the implementation).

10. **Work with Examples**: Practice drawing and interpreting diagrams of computer organization, including the data flow between CPU, memory, and I/O devices during instruction execution.