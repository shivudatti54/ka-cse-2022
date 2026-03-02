# Introduction to Operating Systems

## Introduction

An Operating System (OS) is the fundamental software that manages computer hardware resources and provides services to application programs. It serves as an intermediary between the computer user and the computer hardware, creating an environment where users can execute programs conveniently and efficiently. Without an operating system, a computer would be useless—users would need to directly control every hardware component, which would require extensive knowledge of each device's technical specifications.

The operating system is arguably the most important piece of software on any computer system. It controls the allocation and usage of hardware resources such as the CPU, memory, disk storage, and input/output devices. Modern operating systems like Windows, macOS, Linux, and Android have evolved significantly since the early days of computing, becoming incredibly sophisticated pieces of engineering that handle thousands of tasks simultaneously while maintaining security, stability, and user-friendliness.

For students studying Computer Science at the University of Delhi, understanding operating systems is crucial because it provides insight into how software interacts with hardware, how system resources are managed, and how multiple processes can run concurrently on a single machine. This knowledge forms the foundation for advanced topics in system programming, distributed computing, and computer architecture.

## Key Concepts

### Definition and Purpose of an Operating System

An operating system is a collection of system software that acts as an interface between computer hardware and users. It performs two primary functions: as a resource manager and as an extended machine (or virtual machine). As a resource manager, the OS allocates and controls access to hardware resources like CPU time, memory space, disk storage, and peripheral devices. As an extended machine, the OS hides the complexities of hardware and presents users with a simpler, more abstract interface to work with.

The main goals of an operating system include:

1. Convenience: Making the computer easy to use
2. Efficiency: Allowing system resources to be used productively
3. Ability to evolve: Permitting new system functions to be added without interfering with existing services

### Evolution of Operating Systems

The development of operating systems has progressed through several distinct phases:

**Batch Processing Systems**: In the early 1950s, computers were operated using punch cards. Jobs were collected in batches and processed sequentially. The operator would load one job at a time, and the computer would execute it before moving to the next. This approach was inefficient because the CPU often sat idle waiting for slow I/O operations.

**Multiprogrammed Batch Systems**: To improve CPU utilization, multiprogramming was introduced. This allowed multiple jobs to reside in memory simultaneously. When one job waited for I/O, the CPU could switch to another ready job. This significantly improved throughput—the amount of work completed per unit time.

**Time-Sharing Systems**: Developed in the 1960s and 1970s, time-sharing systems allowed multiple users to interact with the computer simultaneously. The CPU rapidly switches between users, giving each the illusion of dedicated access. This led to the development of interactive computing and paved the way for modern personal computers.

**Personal Computer Operating Systems**: With the advent of microprocessors in the 1970s and 1980s, personal computers became mainstream. Operating systems like MS-DOS, Windows, and Mac OS provided graphical user interfaces that made computers accessible to ordinary users.

**Modern Operating Systems**: Contemporary OS designs support multitasking, multi-threading, virtualization, distributed computing, and real-time operations. Examples include Windows 11, macOS, Linux distributions, Android, and iOS.

### Types of Operating Systems

**Batch Operating Systems**: Process jobs in batches without user interaction. Suitable for tasks requiring large computations without manual intervention.

**Time-Sharing Operating Systems**: Allow multiple users to access the system simultaneously through terminals. Examples include UNIX, VMS, and modern multi-user systems.

**Distributed Operating Systems**: Manage multiple interconnected computers that appear as a single system to users. Examples include Amoeba, Plan 9, and distributed versions of Linux.

**Real-Time Operating Systems (RTOS)**: Guarantee response to external events within strict time constraints. Used in embedded systems, industrial control, and medical devices. Examples include VxWorks, FreeRTOS, and QNX.

**Network Operating Systems**: Provide networking capabilities and allow computers to share resources across a network. Examples include Windows Server, Novell NetWare, and UNIX systems.

**Mobile Operating Systems**: Designed for smartphones and tablets. Examples include Android, iOS, and Windows Phone.

### Functions of an Operating System

The primary functions of an operating system include:

1. **Process Management**: Creating, scheduling, and terminating processes; handling inter-process communication; managing process synchronization.

2. **Memory Management**: Allocating and deallocating memory space to programs; implementing virtual memory; protecting memory from unauthorized access.

3. **File Management**: Creating, deleting, and organizing files and directories; managing free space on storage devices; providing file access control.

4. **Device Management**: Managing input/output devices through drivers; handling device scheduling; providing abstract interfaces for device access.

5. **Security and Protection**: Implementing user authentication; controlling access to system resources; protecting against unauthorized access and malicious software.

6. **Error Detection and Recovery**: Detecting hardware and software errors; implementing error recovery mechanisms; logging system errors for analysis.

### Operating System as Resource Manager

The OS acts as a resource manager for the computer system, controlling and coordinating the use of hardware resources among various application programs. The main resources managed include:

- **CPU**: The OS performs CPU scheduling to determine which process gets the CPU and for how long. This involves algorithms like First-Come-First-Served, Shortest Job First, Round Robin, and Priority Scheduling.

- **Memory**: The OS tracks which parts of memory are in use and by which processes. It implements virtual memory to extend available memory using disk space and protects memory regions from unauthorized access.

- **I/O Devices**: The OS manages I/O devices through device drivers, handles interrupts, and provides buffering and caching to improve I/O performance.

### Operating System as Virtual Machine

The OS abstracts the complexities of hardware and presents users with a virtual machine that is easier to program against. Instead of dealing with physical hardware details like memory addresses, disk sectors, and device registers, programmers interact with high-level abstractions like files, processes, and system calls. This abstraction layer allows application programs to be written without concern for specific hardware implementations.

### Bootstrap Process

When a computer is powered on, it executes a bootstrap program stored in ROM or EEPROM. This program initializes CPU registers, device controllers, and memory contents. It then loads the operating system kernel into memory and transfers control to it. The kernel then initializes system data structures, starts system services, and finally presents a login prompt or desktop environment to the user.

## Examples

### Example 1: Understanding OS Resource Management

Consider a scenario where you are running a web browser while also listening to music and downloading a file. Explain how the OS manages this situation.

**Solution:**

The operating system handles this through process management and CPU scheduling:

1. Each application (browser, music player, download manager) is represented as a separate process in the system.

2. The OS maintains a process control block (PCB) for each process, storing information like process state, program counter, CPU registers, and memory management information.

3. The CPU scheduler decides how to allocate CPU time among these processes. When you are browsing, the browser gets CPU time. When the download manager waits for network data, the CPU switches to the music player.

4. Memory management ensures each process has its own address space. The browser cannot access the memory allocated to the music player.

5. The OS handles I/O requests from all three applications, queuing them appropriately and managing the hardware.

This demonstrates how the OS enables multiple applications to run concurrently while managing hardware resources efficiently.

### Example 2: Distinguishing Between OS Types

A hospital needs a computer system to monitor patient vital signs in real-time. Which type of operating system would be most suitable and why?

**Solution:**

A Real-Time Operating System (RTOS) would be most suitable for this hospital monitoring system because:

1. **Deterministic Response**: RTOS guarantees that critical operations will complete within a specified time frame. In patient monitoring, delayed response could be life-threatening.

2. **Priority-Based Scheduling**: RTOS can prioritize critical patient data over less important tasks, ensuring immediate attention to dangerous conditions.

3. **Minimal Latency**: RTOS is designed to minimize interrupt latency and context-switching time, providing fast response to changes in vital signs.

4. **Reliability**: RTOS systems are typically highly reliable and predictable, essential for medical applications.

5. **Examples of RTOS for medical use**: VxWorks, QNX, and FreeRTOS are commonly used in medical devices.

If this were a general-purpose hospital administration system, a time-sharing or general-purpose operating system would be appropriate.

### Example 3: Understanding System Boot Process

Describe what happens when you turn on your computer, from the moment you press the power button until the desktop appears.

**Solution:**

1. **Power-On Self Test (POST)**: When power is applied, the BIOS/UEFI firmware performs a hardware initialization test to verify memory, keyboard, and other essential components.

2. **Boot Device Selection**: The firmware checks configured boot devices in order (typically hard drive, then USB, then network) to find a bootable device.

3. **Boot Loader Execution**: The MBR (Master Boot Record) or UEFI boot manager loads the boot loader (like GRUB or Windows Boot Manager) from the selected device.

4. **Kernel Loading**: The boot loader reads the OS kernel into memory and prepares to execute it.

5. **Kernel Initialization**: The kernel starts with basic system initialization:
   - Sets up memory management
   - Initializes interrupt handlers
   - Configures device drivers
   - Creates essential kernel data structures

6. **System Services Start**: The kernel starts system services and daemons (in Unix) or services (in Windows).

7. **User Session Initiation**: The OS starts the graphical user interface (GUI) subsystem and displays the login screen or desktop.

This entire process typically takes between 10 seconds to a few minutes depending on the system.

## Exam Tips

1. **Know the definitions**: Be able to define an operating system clearly in your own words. The most common exam question asks "What is an operating system?"—practice writing a concise 2-3 line definition.

2. **Understand the dual role**: Remember that an OS serves two purposes—AS A RESOURCE MANAGER and AS AN EXTENDED MACHINE. This is a frequently tested concept.

3. **Types of OS**: Be familiar with all types (Batch, Time-sharing, Distributed, Real-time, Network, Mobile) and their characteristics. Questions often ask to identify the appropriate OS type for a given scenario.

4. **Evolution timeline**: Know the chronological evolution of operating systems from batch processing to modern systems. Understand WHY each evolution occurred (mainly to improve CPU utilization).

5. **Functions of OS**: Memorize all six main functions: Process Management, Memory Management, File Management, Device Management, Security and Protection, Error Detection.

6. **Bootstrap process**: Understand the step-by-step boot process from power-on to user login. This is a common long-answer question.

7. **Examples and applications**: For each type of OS, know at least one real-world example. For instance, RTOS is used in medical devices and aerospace.

8. **Difference between multiprogramming and time-sharing**: This is a common exam question. Multiprogramming improves CPU utilization by having multiple jobs in memory, while time-sharing allows multiple users to interact with the computer simultaneously.

9. **Draw diagrams**: Be prepared to draw and explain diagrams like the OS as intermediate layer, boot process, or OS structure.

10. **Answer structure**: For long-answer questions, follow a structured approach: definition → characteristics → types → functions → examples → conclusion.