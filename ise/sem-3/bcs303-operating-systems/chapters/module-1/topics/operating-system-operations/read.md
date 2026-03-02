# Operating System Operations

## Introduction

An operating system (OS) serves as the fundamental layer of software that manages a computer system's hardware resources and provides services to application programs. Understanding how an operating system performs its core operations is essential for any computer science student, as it forms the backbone of modern computing. The operating system acts as an intermediary between the user and the computer hardware, creating an environment where users can execute programs efficiently without worrying about the underlying hardware complexities.

The study of operating system operations encompasses the mechanisms and procedures that enable the OS to function effectively as a resource manager and service provider. These operations include the boot process, interrupt handling, system calls, dual-mode operation, and various management functions. For students at the University of Delhi, a thorough grasp of these concepts is crucial, as they form the foundation for understanding system programming, distributed computing, and advanced operating system design. The operations discussed in this chapter are fundamental to how computers execute multiple processes concurrently while maintaining system stability and security.

## Key Concepts

### Bootstrap Process

The bootstrap process, also known as booting, is the sequence of operations that occurs when a computer is turned on or reset. This process initializes the system hardware and loads the operating system into main memory. The bootstrap program, typically stored in read-only memory (ROM) or electrically erasable programmable read-only memory (EEPROM), performs a power-on self-test (POST) to verify hardware components are functioning correctly. After the POST, the bootstrap loader locates the operating system kernel and loads it into memory, transferring control to the operating system once the kernel is in place.

The bootstrap process follows a hierarchical approach: first, the ROM BIOS (Basic Input/Output System) or UEFI (Unified Extensible Firmware Interface) initializes essential hardware; second, the boot loader (such as GRUB in Linux or Boot Manager in Windows) is executed to locate and load the kernel; finally, the kernel initializes device drivers, file systems, and system services. This multi-stage process ensures that all necessary components are properly initialized before the system becomes operational for user programs.

### Dual-Mode Operation

Modern operating systems employ dual-mode operation to protect critical system resources from unauthorized access and ensure system stability. This concept divides the execution environment into two distinct modes: kernel mode (also called supervisor mode, system mode, or privileged mode) and user mode. In kernel mode, the CPU can execute any instruction and access any memory location, giving the operating system complete control over hardware resources. In user mode, the CPU can only execute a subset of instructions and access limited memory regions, preventing user programs from directly manipulating hardware or accessing protected system data.

The transition between these modes occurs through carefully controlled mechanisms. When a user program requests a service from the operating system, it executes a special instruction (such as `syscall` in x86 architecture) that triggers a transition from user mode to kernel mode. This transition is known as a mode switch or context switch at the privilege level. The operating system performs the requested operation in kernel mode and then returns control to the user program, transitioning back to user mode. This architecture ensures that sensitive operations can only be performed by trusted system code, maintaining system integrity and security.

### Interrupts and Exception Handling

Interrupts are fundamental to the operation of modern operating systems, enabling asynchronous event handling and efficient resource utilization. An interrupt is a signal sent to the CPU by hardware or software indicating an event that requires immediate attention. When an interrupt occurs, the CPU suspends its current execution, saves the state of the currently running program, and transfers control to an interrupt service routine (ISR) that handles the specific interrupt. Common sources of interrupts include I/O device completion, timer ticks, hardware failures, and software-generated exceptions.

The interrupt handling mechanism involves several steps: first, the interrupt controller (such as Programmable Interrupt Controller or PIC) prioritizes and routes interrupts to the CPU; second, the CPU completes its current instruction and saves the program counter and processor status; third, the CPU loads the interrupt vector and begins executing the ISR; fourth, the ISR processes the interrupt and may perform I/O operations or notify waiting processes; finally, the ISR restores the saved state and resumes the interrupted program. This mechanism allows the operating system to respond quickly to external events while maintaining the illusion of concurrent execution.

### Timer Interrupts

Timer interrupts play a crucial role in implementing time-sharing and pre-emptive multitasking in operating systems. A hardware timer generates periodic interrupts at predetermined intervals, allowing the operating system to regain control of the CPU from user programs. When a timer interrupt occurs, the operating system can implement context switching, ensuring that no single program monopolizes the CPU and that all processes receive fair allocation of processing time.

The timer interrupt mechanism works as follows: the operating system programs the hardware timer to generate interrupts at specific intervals (such as every 10 milliseconds); when the timer interrupt occurs, the interrupt service routine saves the current process's state, invokes the scheduler to determine which process should run next, loads the state of the selected process, and resumes execution. This pre-emptive scheduling approach prevents runaway programs from crashing the system and enables responsive multi-tasking. Without timer interrupts, cooperative multitasking would require programs to voluntarily yield the CPU, making the system vulnerable to poorly written or malicious code.

### System Calls

System calls provide the interface through which user programs request services from the operating system. These calls represent the boundary between user space and kernel space, offering controlled access to privileged operations that cannot be performed directly in user mode. System calls cover a wide range of operations, including process management (fork, exec, exit), file operations (open, read, write, close), device communication, memory allocation, and interprocess communication.

The system call mechanism typically involves several steps: the user program prepares arguments specifying what operation to perform and what parameters to use; the program executes a trap instruction (syscall) that switches the CPU from user mode to kernel mode; the kernel validates the arguments and checks permissions; the kernel performs the requested operation using privileged instructions; the kernel returns the result to the user program; and finally, control returns to user mode. Each operating system provides a standard library (such as glibc in Linux) that provides convenient wrapper functions for making system calls, abstracting the low-level trap mechanism from application programmers.

### Process Management Operations

Process management forms one of the core responsibilities of an operating system, involving the creation, scheduling, and termination of processes. A process is an instance of a program in execution, containing its own program counter, register values, stack, and memory space. The operating system maintains a process control block (PCB) for each process, storing essential information such as process state, program counter, CPU registers, memory management information, and accounting data.

Key process management operations include process creation (where a parent process creates a child process using fork or CreateProcess), process termination (where a process completes execution or is forcefully terminated), process synchronization (ensuring processes cooperate without interfering with each other), and process scheduling (determining which process runs on the CPU and for how long). The operating system's process management subsystem ensures that multiple processes can execute concurrently while maintaining system stability and fairness.

### Memory Management Operations

Memory management operations enable the operating system to efficiently allocate and deallocate memory to processes, ensuring each process has access to the memory it needs while preventing unauthorized access to memory belonging to other processes or the operating system itself. These operations include memory allocation (providing memory to processes upon request), memory deallocation (reclaiming memory when processes terminate or release it), address translation (converting logical addresses to physical addresses), and memory protection (preventing processes from accessing memory outside their allocated space).

The operating system maintains data structures such as memory allocation tables, page tables, and segment tables to track memory usage. Memory management techniques include contiguous allocation, paging, segmentation, and virtual memory, each with its own advantages and trade-offs. Efficient memory management is crucial for system performance, as memory access is one of the slowest operations in the computer hierarchy, and improper memory management can lead to memory leaks, fragmentation, and system instability.

### I/O Device Management

I/O device management operations handle communication between the CPU and peripheral devices such as keyboards, mice, printers, hard drives, and network adapters. The operating system provides device drivers—specialized kernel-mode modules that understand the specific communication protocols of each device. When a user program requests an I/O operation, the operating system uses the appropriate device driver to translate the request into device-specific commands.

I/O management includes buffering (temporarily storing data in memory to accommodate speed differences between CPU and devices), caching (keeping frequently accessed data in fast memory), spooling (queuing I/O requests for sequential devices like printers), and device scheduling (determining the order in which I/O requests are processed). These operations optimize I/O performance and enable multiple processes to share devices efficiently. The operating system also handles device interrupts, waking up processes that are waiting for I/O completion and ensuring efficient use of device bandwidth.

## Examples

### Example 1: System Call Sequence for File Reading

Consider a C program that opens and reads a file. The system call sequence demonstrates the transition between user mode and kernel mode:

```c
#include <fcntl.h>
#include <unistd.h>

int main() {
    char buffer[100];
    int fd = open("example.txt", O_RDONLY);  // System call 1
    if (fd == -1) return 1;
    
    ssize_t bytes_read = read(fd, buffer, 100);  // System call 2
    if (bytes_read > 0) {
        // Process the data
    }
    
    close(fd);  // System call 3
    return 0;
}
```

Step-by-step execution:
1. The `open()` system call switches to kernel mode, validates the file path, checks permissions, allocates a file descriptor, and returns control to user mode
2. The `read()` system call switches to kernel mode again, locates the file structure associated with the file descriptor, initiates the I/O operation, and may block the process if data is not immediately available
3. When the I/O operation completes (generating a hardware interrupt), the operating system wakes up the process and returns the number of bytes read
4. The `close()` system call releases the file descriptor and associated resources

Each system call involves at least two mode transitions: user to kernel and back to user. This overhead is unavoidable for protected operations but represents a significant portion of operating system overhead in I/O-intensive applications.

### Example 2: Timer Interrupt and Context Switch

In a pre-emptive multitasking system, the timer interrupt enables the operating system to implement time-slicing:

1. Process A is executing in user mode when a timer interrupt occurs
2. The CPU automatically switches to kernel mode, saving Process A's program counter and registers onto its stack
3. The timer interrupt service routine invokes the scheduler
4. The scheduler determines that Process B should run next (perhaps because Process A has used its time quantum)
5. The scheduler saves Process A's complete state (including CPU registers, memory management information) into its Process Control Block
6. The scheduler loads Process B's state from its Process Control Block into CPU registers
7. The interrupt service routine returns, resuming execution in Process B's context

This entire sequence occurs transparently to the processes, creating the illusion that multiple programs execute simultaneously. The operating system must save and restore the entire processor state (including condition codes, floating-point registers, and memory management registers) to ensure processes do not interfere with each other.

### Example 3: Boot Process Analysis

When a computer system starts, the bootstrap process follows this sequence:

1. **Power-On Self-Test (POST)**: The BIOS or UEFI firmware performs diagnostics on CPU, memory, and essential hardware components
2. **Boot Device Selection**: The firmware scans available boot devices (hard drive, SSD, USB, network) based on configured boot order
3. **MBR/GPT Reading**: For traditional BIOS systems, the Master Boot Record (512 bytes) is read from the first sector of the boot device; for UEFI systems, the EFI System Partition is accessed
4. **Boot Loader Execution**: The boot loader (such as GRUB for Linux or Windows Boot Manager) is loaded into memory
5. **Kernel Selection**: The boot loader presents a menu of available operating systems and loads the selected kernel into memory
6. **Kernel Initialization**: The Linux kernel (for example) decompresses itself, initializes memory management, sets up interrupt descriptors, and mounts the root file system
7. **Init Process**: The kernel starts the first user-space process (init in traditional Linux, systemd in modern distributions), which then spawns all other system services

Each step represents a critical failure point where boot problems can occur, making understanding this sequence essential for system administrators and software developers debugging startup issues.

## Exam Tips

1. **Distinguish between mode switch and context switch**: A mode switch changes the CPU privilege level (user to kernel or vice versa) but keeps the same process; a context switch saves the entire process state and switches to a different process.

2. **Remember the two types of interrupts**: Hardware interrupts are generated by external devices, while software interrupts (traps or exceptions) are generated by the CPU itself, typically for system calls or error conditions.

3. **System calls vs library functions**: Library functions like `printf()` may look like system calls but typically buffer output and make fewer actual system calls. Understand which functions result in mode transitions and which remain in user mode.

4. **The role of the interrupt vector**: The interrupt vector is a table of pointers to interrupt service routines, indexed by interrupt number. The CPU uses this table to quickly locate and execute the appropriate handler.

5. **Timer interrupt is essential for pre-emptive scheduling**: Without timer interrupts, the operating system cannot forcibly take the CPU away from a running process, making it vulnerable to malicious or buggy code that never yields control.

6. **Boot process is hardware-dependent**: While the conceptual sequence (POST → boot loader → kernel → init) is universal, the specific implementations differ between BIOS and UEFI systems and between operating systems.

7. **Process Control Block contents**: Remember that the PCB stores process state, program counter, CPU registers, memory management information, accounting data, and I/O status information.

8. **Why dual-mode is necessary**: Without dual-mode operation, any user program could execute privileged instructions, access any memory location, and compromise system security and stability.