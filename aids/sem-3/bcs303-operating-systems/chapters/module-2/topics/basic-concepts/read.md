# Basic Concepts of Operating Systems

## Introduction

An Operating System (OS) serves as the fundamental software layer that bridges the gap between computer hardware and user applications. It is the most critical component of system software, managing hardware resources efficiently while providing an interface for users and application programs to interact with the computer system. Without an operating system, computers would be unusable—users would need to directly control hardware registers, manage memory allocation, and handle input-output operations through complex machine code.

The study of operating system concepts is essential for any computer science student because it provides insight into how modern computing systems function at their core level. For University of Delhi students preparing for examinations, understanding these fundamental concepts forms the foundation for more advanced topics like process management, memory management, file systems, and security. The operating system acts as a resource manager, arbitrating competing demands from multiple processes while maintaining system stability and efficiency. Whether you are using a smartphone, working on a desktop computer, or accessing a cloud server, operating systems are silently managing your computational experience.

## Key Concepts

### Definition and Purpose of an Operating System

An operating system is defined as system software that controls hardware resources and provides services to application programs. It serves dual purposes: as a resource manager that allocates and controls hardware components, and as an extended machine that abstracts hardware complexity from users and developers. The operating system presents a virtual machine that is easier to program than the actual physical hardware. From a user perspective, the OS provides a user interface (CLI or GUI) and makes computing convenient. From a system perspective, it efficiently manages resources and ensures fair allocation among competing processes.

### Goals of an Operating System

The primary goals of an operating system include convenience, efficiency, and the ability to evolve. Convenience makes the computer system easier to use by providing user interfaces and abstracting hardware complexity. Efficiency ensures optimal utilization of system resources like CPU, memory, and I/O devices. The evolution goal allows the OS to be modified and upgraded over time without disrupting existing services—new features, improved algorithms, and bug fixes can be incorporated through updates.

### Functions of an Operating System

The operating system performs several critical functions:

**Process Management**: The OS creates, schedules, and terminates processes. It handles process synchronization and communication between multiple processes. The CPU scheduler decides which process gets CPU time and for how long, while the dispatcher context switches between processes.

**Memory Management**: The OS tracks which portions of memory are in use and which are free, allocates memory to processes when needed, and deallocates when processes terminate. It implements virtual memory to extend apparent memory capacity using disk space.

**File Management**: The OS creates, deletes, and organizes files and directories. It manages free space on storage devices and maintains file access permissions and security.

**Device Management**: The OS communicates with hardware devices through device drivers, manages device queues, and handles interrupts. It provides a uniform interface for I/O operations regardless of specific hardware details.

**Security and Protection**: The OS implements access control mechanisms, authentication procedures, and protection policies to prevent unauthorized access to system resources.

### Types of Operating Systems

**Batch Operating Systems**: Jobs are prepared offline and submitted in batches. Programs and data are collected and processed sequentially. Examples include early mainframe systems. These systems lack interactive user communication and have high turnaround time.

**Time-Sharing Systems**: Multiple users can access the computer simultaneously through terminals. The CPU is rapidly switched among users, creating the illusion of simultaneous access. Examples include UNIX, Linux, and modern multi-user systems.

**Real-Time Operating Systems**: These systems process data and respond within strict time constraints. They are used in embedded systems, industrial control, and applications requiring immediate response. Examples include VxWorks and QNX.

**Distributed Operating Systems**: Multiple computers work together as a single system, appearing as one machine to users. They manage resources across a network. Examples include distributed file systems and cluster computing environments.

**Network Operating Systems**: These provide networking capabilities and allow computers to communicate over a network. They include server software for network resource sharing. Examples include Windows Server and Linux server distributions.

### System Calls

System calls provide the interface between user programs and the OS kernel. They allow user applications to request services like file operations, process control, and memory allocation. Common types of system calls include process control (fork, exec, wait), file management (open, read, write, close), device management (read, write, request), information maintenance (getpid, getuid), and communication (pipe, socket). When a program makes a system call, it switches from user mode to kernel mode, where the OS performs the requested operation with elevated privileges.

### Operating System Structure

**Monolithic Systems**: The entire OS runs as a single program in kernel mode with no internal structure. While efficient, this makes maintenance and extension difficult. Traditional UNIX exemplifies this approach.

**Layered Systems**: The OS is organized in layers, where each layer uses services only from layers below it. This provides modularity and ease of debugging. The hardware is at the bottom, and user interface at the top.

**Microkernel Architecture**: Only essential functions reside in the kernel; other services run as user-level processes. This improves reliability and makes the system more extensible. Examples include MINIX and Mach.

**Client-Server Model**: The OS is organized as a collection of servers that provide services to client processes. This enables distribution and scalability.

### Bootstrap Process

When a computer starts, the bootstrap program initializes the system. It is stored in ROM or EEPROM and performs POST (Power-On Self-Test), detects hardware components, loads the OS kernel from storage into memory, and transfers control to the kernel. The bootstrap process is fundamental to system initialization and must be understood for troubleshooting boot failures.

## Examples

**Example 1: Understanding System Calls in Practice**

Consider a simple C program that writes "Hello, DU Students!" to a file:

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("message.txt", O_WRONLY | O_CREAT, 0644);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    
    char buffer[] = "Hello, DU Students!";
    ssize_t bytes = write(fd, buffer, sizeof(buffer));
    
    close(fd);
    return 0;
}
```

When this program executes, it makes several system calls. The `open()` system call switches from user mode to kernel mode, where the OS checks file permissions, allocates a file descriptor, and creates the file if it doesn't exist. The `write()` system call transfers the data from user space to kernel space, then to the disk controller. The `close()` system call releases the file descriptor. Each system call involves mode switch overhead, making them expensive operations compared to regular function calls.

**Example 2: OS as a Resource Manager**

Imagine a university computer lab with 30 students, each wanting to use the single printer. Without an OS, chaos would ensue—print jobs would intermingle, and students would fight for the printer. The OS acts as a printer spooler, queueing print requests, managing the order of printing, and ensuring each job completes without interference. Similarly, when multiple programs run simultaneously, the OS allocates CPU time to each process through scheduling algorithms, divides physical memory among processes through memory management, and ensures each process gets fair access to I/O devices.

**Example 3: Time-Sharing System Demonstration**

In a time-sharing system like Linux, when you open multiple applications (browser, text editor, music player), the OS appears to run them simultaneously. In reality, the CPU executes instructions from one program for a short time slice (typically 1-100 milliseconds), then switches to another. This is called context switching. If the system has 4 CPU cores, it can truly run 4 programs in parallel through multiprocessing, while time-sharing creates parallelism for the remaining programs. The OS maintains process control blocks (PCB) for each process, storing CPU registers, memory mapping, file descriptors, and scheduling information. When context switching occurs, the entire process state is saved to its PCB and another process's state is restored.

## Exam Tips

1. Understand the dual role of OS: as a resource manager and as an extended virtual machine. This distinction frequently appears in exam questions.

2. Memorize the five main functions of an operating system: Process Management, Memory Management, File Management, Device Management, and Security/Protection.

3. Know the differences between various OS types—batch, time-sharing, real-time, distributed, and network—with concrete examples of each.

4. System calls are the interface between user programs and kernel. Be prepared to explain what happens during a system call and list common types.

5. The bootstrap process is fundamental—understand POST, BIOS/UEFI, and kernel loading sequence.

6. When answering questions about OS structure, explain monolithic, layered, microkernel approaches with advantages and disadvantages.

7. Time-sharing vs. multiprocessing: Understand how modern OSes create illusion of simultaneous execution through both mechanisms.

8. Practice diagram-based questions showing OS architecture and layer structure.

9. Remember that OS goals (convenience, efficiency, evolution) directly influence design decisions.

10. Be ready to give real-world examples (Android, Windows, UNIX) when discussing OS types and characteristics.