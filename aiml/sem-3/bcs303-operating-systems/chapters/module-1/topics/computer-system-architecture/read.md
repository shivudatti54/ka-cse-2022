# Computer System Architecture

## Introduction

Computer System Architecture forms the foundational layer of understanding for any Operating System course. Before we can appreciate how operating systems manage resources, schedule processes, or provide security, we must first comprehend the underlying hardware organization that makes these software abstractions possible. The operating system serves as an intermediary between the user and the computer hardware, and its effectiveness is intrinsically tied to the architectural design of the system it controls.

The study of computer system architecture in the context of operating systems focuses on three primary aspects: the structural organization of computer hardware components, the mechanisms of communication between these components, and the hardware-level support that enables operating system functions such as protection, security, and process management. Understanding these fundamentals is crucial because the operating system must efficiently manage hardware resources, provide isolation between processes, and ensure fair access to system resources among competing users and applications.

In this chapter, we will examine the key architectural components of a computer system, including the central processing unit (CPU), memory hierarchy, input/output subsystems, and the bus structures that interconnect these elements. We will also explore how modern computer systems implement hardware protection mechanisms that operating systems rely upon to ensure system stability and security. This knowledge will serve as the bedrock upon which we build our understanding of operating system concepts in subsequent chapters.

## Key Concepts

### 1. Central Processing Unit (CPU)

The Central Processing Unit (CPU) constitutes the brain of any computer system. It executes instructions stored in memory and performs arithmetic, logical, and control operations. The CPU consists of several key components:

The **Control Unit (CU)** directs the operation of the processor by interpreting instructions and generating control signals that coordinate the activities of other components. It manages the fetch-decode-execute cycle and ensures proper sequencing of operations.

The **Arithmetic Logic Unit (ALU)** performs actual computational operations including addition, subtraction, multiplication, division, and logical operations such as AND, OR, and NOT. Modern CPUs contain multiple ALUs to enable parallel execution of instructions.

**Registers** are high-speed storage locations within the CPU used to hold temporary data and control information. Critical registers include:
- **Program Counter (PC)**: Holds address of the next instruction to be fetched
- **Instruction Register (IR)**: Holds the currently executing instruction
- **Accumulator (ACC)**: Used for arithmetic operations
- **Stack Pointer (SP)**: Points to top of stack in memory
- **Base and Limit Registers**: Used for memory protection

Modern CPUs employ **pipelining**, **superscalar execution**, and **multiple cores** to increase instruction throughput. A multi-core processor contains multiple complete processing units on a single chip, enabling true parallel execution of instructions.

### 2. Memory Hierarchy

Computer memory is organized in a hierarchy based on speed, cost, and capacity. Understanding this hierarchy is essential for appreciating how operating systems manage memory:

**Primary Memory (Main Memory/RAM)**: Random Access Memory provides fast read/write access to data and instructions currently being processed. It is volatile—contents are lost when power is removed. RAM is significantly faster than secondary storage but more expensive per byte.

**Cache Memory**: A small, high-speed memory located between the CPU and main memory. It stores frequently accessed data and instructions to reduce memory access latency. Modern systems have multiple cache levels (L1, L2, L3) with varying sizes and speeds.

**Secondary Storage**: Magnetic disks, solid-state drives, and optical media provide persistent storage at lower cost per byte but with significantly higher access times. Operating systems manage secondary storage through file systems.

**Registers**: The fastest storage location, located within the CPU, with access times measured in nanoseconds.

The operating system must manage data movement between these levels through techniques like caching, virtual memory, and swapping to provide the illusion of a large, fast primary memory.

### 3. Input/Output (I/O) Devices

I/O devices enable communication between the computer system and the external world. They are categorized into three main types:

**Storage Devices**: Hard disk drives (HDD), solid-state drives (SSD), magnetic tape, and optical drives provide permanent data storage. HDDs use rotating platters and read/write heads, while SSDs use flash memory for faster access.

**Input Devices**: Keyboards, mice, scanners, microphones, and touchscreens allow users to input data and commands.

**Output Devices**: Monitors, printers, and speakers present processed information to users.

I/O devices communicate with the CPU through **I/O controllers** (also called device controllers or adapters). These controllers manage communication between the CPU and specific device types, handling details like data format conversion and error detection. The CPU communicates with controllers through memory-mapped I/O or isolated I/O port addressing.

### 4. Bus Structures

A bus is a set of conductors that transmit data, address, and control signals between components. Computer systems use several types of buses:

**System Bus**: Connects the CPU, memory, and other major components. It carries address, data, and control signals.

**I/O Bus**: Connects various I/O devices to the system bus through expansion slots or dedicated controllers.

**Memory Bus**: Dedicated path between CPU and main memory for high-speed data transfer.

Modern systems use **point-to-point interconnects** like Intel's QuickPath Interconnect (QPI) or AMD's HyperTransport instead of traditional shared buses for improved scalability.

### 5. Interrupt Mechanism

Interrupts are essential for efficient I/O handling. Rather than the CPU continuously polling devices for status, devices interrupt the CPU when they need attention:

**Interrupt Types**:
- **Hardware Interrupts**: Generated by I/O devices, timers, or other hardware components
- **Software Interrupts (Traps)**: Generated by exceptional conditions (division by zero, illegal memory access) or system calls

**Interrupt Handling Process**:
1. Device raises an interrupt signal
2. CPU completes current instruction
3. CPU saves current state (program counter, status flags)
4. CPU transfers control to the appropriate interrupt service routine (ISR)
5. ISR processes the interrupt
6. CPU restores state and resumes normal execution

The **Interrupt Vector Table** maps interrupt types to their corresponding service routines. Modern systems support **interrupt prioritization** and **nested interrupts** for handling multiple simultaneous interrupts.

### 6. Hardware Protection Mechanisms

Modern CPUs provide hardware support for operating system protection:

**Dual-Mode Operation**: CPUs support at least two execution modes:
- **User Mode**: Restricted access to hardware resources
- **Kernel Mode (Privileged Mode)**: Full access to all instructions and hardware resources

The CPU maintains a **mode bit** to indicate the current execution mode. User programs execute in user mode and must request OS services through **system calls** to transition to kernel mode.

**Timer**: A hardware timer interrupts the CPU after a specified period, ensuring the OS regains control from user programs. This prevents infinite loops or malicious code from monopolizing the CPU. The timer is used to implement time-sharing and preemption.

**Memory Protection**: The **Base and Limit registers** define the range of legal addresses a process may access. Any memory reference outside this range triggers a trap to the operating system. More sophisticated systems use **segmentation** and **paging** for flexible memory protection.

**I/O Protection**: User programs cannot directly access I/O devices; all I/O operations must be performed through the OS. Some systems provide privileged I/O instructions that can only be executed in kernel mode.

## Examples

### Example 1: Understanding the Fetch-Decode-Execute Cycle

Consider a simple assembly instruction: `ADD R1, R2, R3` (add contents of R2 and R3, store result in R1).

**Step 1 - Fetch**: The CPU copies the instruction from memory address in PC to the Instruction Register (IR), then increments PC.

**Step 2 - Decode**: The Control Unit interprets the instruction opcode, determines this is an ADD operation, and identifies source (R2, R3) and destination (R1) registers.

**Step 3 - Execute**: The ALU receives operands from R2 and R3, performs addition, and stores result in R1.

**Step 4 - Store Result**: The result is written to register R1.

The operating system manages this cycle by loading programs into memory, setting up the PC to point to the first instruction, and handling any interrupts or exceptions that occur during execution. The timer ensures that no single program can hog the CPU by forcing a return to the OS after the quantum expires.

### Example 2: Memory Protection in Action

Consider a user program that attempts to access memory address 0xFFFF1000, but the OS has set Base = 0x00001000 and Limit = 0x0000F000 for this process.

**Legal Address Range**: 0x00001000 to 0x0000FFFF

**Attempted Address**: 0xFFFF1000

When the CPU executes this memory access instruction:
1. Hardware computes effective address using base register: 0xFFFF1000 - (impossible, base is smaller)
2. Alternatively, with simple base/limit: CPU checks if 0xFFFF1000 > (Base + Limit)
3. Since 0xFFFF1000 exceeds the allowed range, CPU generates a **memory fault interrupt**
4. Control transfers to the OS memory management handler
5. OS typically terminates the offending process with a segmentation fault error

This hardware-enforced protection ensures one process cannot access another's memory, providing isolation essential for multi-programming security.

### Example 3: System Call Mechanism

When a user program needs to read a file, it cannot directly access the disk. Instead, it uses the operating system's file read service through a system call:

```
// User program requesting file read
char buffer[1024];
int bytes_read = read(file_descriptor, buffer, 1024);
```

**Execution Flow**:
1. User program executes `read()` library function
2. Library function places system call number in a designated register (e.g., EAX on x86)
3. Library function places parameters (file_descriptor, buffer address, size) in other registers
4. Library function executes `INT 0x80` (software interrupt) or `SYSCALL` instruction
5. CPU switches from User Mode to Kernel Mode (sets mode bit)
6. CPU looks up interrupt handler in Interrupt Vector Table
7. OS kernel's system call handler executes:
   - Validates parameters
   - Checks file descriptor validity
   - Calls appropriate file system driver
   - Driver initiates disk I/O
8. If data immediately available, handler copies to user buffer
9. If I/O needed, handler may block process and context switch
10. Handler returns (with success code or error in EAX)
11. CPU switches back to User Mode
12. User program continues execution

This mechanism ensures that privileged operations (file access, memory allocation, process creation) are controlled by the OS while appearing seamless to applications.

## Exam Tips

1. **Know the distinction between hardware and software interrupts**: Hardware interrupts are asynchronous (generated by devices), while software interrupts are synchronous (generated by program execution or system calls).

2. **Remember dual-mode operation**: The mode bit in CPU indicates whether executing in user mode or kernel mode. This is fundamental to OS protection.

3. **Understand base and limit registers**: These hardware registers define a process's legal memory address space and generate traps on illegal access attempts.

4. **Timer is crucial for preemption**: The timer interrupt ensures the OS regains control from user programs, enabling time-sharing and preventing CPU monopolization.

5. **Cache vs. RAM vs. Secondary Storage**: Know the trade-offs in speed, cost, and volatility. This helps explain why OS memory management is necessary.

6. **System call interface**: Understand the complete flow from user program to kernel and back—this is a frequent exam question.

7. **I/O handling methods**: Know the three main approaches—programmed I/O, interrupt-driven I/O, and DMA—and their relative advantages.

8. **Multi-core considerations**: Understand how multi-core CPUs affect OS design, requiring support for true parallelism and shared memory management.

9. **Memory hierarchy impact on performance**: Recognize why cache misses are expensive and how OS policies affect cache behavior.

10. **Interrupt prioritization**: When multiple interrupts occur simultaneously, the CPU must have a mechanism to determine which to handle first—this is typically handled by interrupt controllers.