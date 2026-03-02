# What Operating Systems Do

## Introduction

An Operating System (OS) is the most fundamental software that manages computer hardware resources and provides services to application programs. It acts as an intermediary between the user and the computer hardware, creating an environment where users can execute programs conveniently and efficiently. The operating system is the backbone of any computing system, whether it is a personal computer, a smartphone, or a supercomputer.

The primary purpose of an operating system is to make the computer system convenient to use while efficiently managing its resources. From the user's perspective, the OS provides a user-friendly interface that simplifies complex hardware interactions. From the system's perspective, it acts as a resource manager, allocating and controlling access to critical resources like CPU time, memory space, storage, and input/output devices. Understanding what operating systems do is crucial for any computer science student, as this forms the foundation for comprehending advanced topics in process management, memory management, and system security.

This chapter explores the fundamental roles of an operating system: as a resource manager, as a user interface provider, and as a system call interface. We will examine how these roles have evolved over time and why they remain essential to modern computing.

## Key Concepts

### Operating System as a Resource Manager

The most fundamental role of an operating system is to manage computer system resources efficiently. A computer system consists of multiple resources including the central processing unit (CPU), memory (RAM), storage devices (hard disks, SSDs), input/output devices (keyboard, mouse, printer, network cards), and more. The OS must coordinate the use of these resources among multiple programs and users simultaneously.

As a resource manager, the OS performs several critical functions. First, it performs resource allocation, ensuring that each process receives the necessary resources to execute properly. Second, it implements resource accounting to track which resources are being used and by whom, which is essential for system monitoring and billing in multi-user systems. Third, the OS provides resource protection, preventing unauthorized access to sensitive resources and ensuring that one process cannot interfere with another's execution.

The resource management function becomes particularly complex in modern systems where multiple applications run simultaneously. The OS must make intelligent decisions about resource allocation, considering factors like process priority, waiting time, and system throughput. This requires sophisticated algorithms for CPU scheduling, memory management, and disk scheduling.

### Operating System as a User Interface

The operating system provides multiple interfaces through which users interact with the computer system. These interfaces have evolved significantly over the years, from command-line interfaces (CLI) to graphical user interfaces (GUI) and modern touch-based interfaces.

The Command-Line Interface (CLI) allows users to type commands to perform tasks. While less intuitive than graphical interfaces, CLI offers advantages like faster execution for experienced users, lower system overhead, and powerful scripting capabilities. In Unix/Linux systems, shells like Bash provide extensive command processing capabilities.

The Graphical User Interface (GUI) provides visual elements like windows, icons, menus, and pointers (WIMP) for user interaction. GUIs make computers more accessible to novice users by allowing them to interact with visual representations of files and applications. Modern operating systems like Windows, macOS, and Linux desktop environments provide sophisticated GUIs.

Touch-based interfaces represent the latest evolution in user interaction, primarily used in smartphones and tablets. These interfaces rely on gestures like tapping, swiping, and pinching, eliminating traditional input devices like keyboards and mice.

### Operating System as a System Call Interface

System calls provide the mechanism by which user programs request services from the operating system kernel. They form the boundary between user space and kernel space, serving as the API (Application Programming Interface) through which applications access system resources and services.

System calls cover a wide range of functions including process management (creating, terminating, waiting for processes), memory management (allocating, releasing memory), file management (opening, reading, writing, closing files), device management (requesting devices, reading from devices), and information maintenance (getting/setting system time, process attributes).

When a program needs OS services, it executes a system call that switches the processor from user mode to kernel mode (privileged mode). The kernel then performs the requested operation and returns control to the user program along with any results. This transition is facilitated by special instructions like `syscall` in modern processors.

### Evolution of Operating System Functions

Operating systems have evolved dramatically since the early days of computing. In the 1940s and 1950s, computers had no operating systems; operators loaded programs manually using front panel switches. The first batch processing systems emerged in the late 1950s, allowing jobs to be prepared offline and executed in batches.

Time-sharing systems in the 1960s and 1970s introduced the concept of multiple users interacting with the computer simultaneously through terminals. This led to significant advances in resource management and user interface design. The development of Unix in the early 1970s established many principles that remain relevant today.

Personal computer operating systems in the 1980s focused on single-user, single-task environments. However, as hardware capabilities increased, modern operating systems evolved to support multiple users running multiple applications simultaneously, leading to sophisticated multiprocessing and multitasking capabilities.

### Goals of an Operating System

Operating systems are designed to achieve several key objectives. Convenience makes computers easier to use by abstracting hardware complexity. Efficiency ensures optimal utilization of system resources. Throughput measures the amount of work completed per unit time. Reliability ensures the system functions correctly even in adverse conditions. Security protects system resources from unauthorized access. Scalability allows the system to handle increasing workloads as hardware improves.

## Examples

### Example 1: Resource Allocation in Action

Consider a user running a web browser while also playing music and downloading a file. The operating system's role as a resource manager becomes evident:

1. **CPU Allocation**: The OS uses CPU scheduling algorithms to allocate processor time among the browser, music player, and download manager. If the user is typing in the browser, the OS may give higher priority to the browser process to ensure responsive interaction.

2. **Memory Allocation**: Each running application is allocated a portion of RAM. The OS maintains a virtual memory system that may use part of the hard disk as extended memory if physical RAM is insufficient. The OS ensures each application cannot access memory allocated to other applications (memory protection).

3. **I/O Device Allocation**: When the music player needs to output audio, the OS allocates the sound card. When the browser needs to display web page content, the OS coordinates access to the display. The OS manages these requests efficiently, potentially allowing multiple applications to share devices through buffering and caching.

### Example 2: System Call Sequence for File Reading

When a C program reads a file, several system calls are involved:

```c
int fd = open("example.txt", O_RDONLY);  // System call
char buffer[100];
read(fd, buffer, 100);                    // System call
close(fd);                                 // System call
```

The `open()` system call transitions the processor from user mode to kernel mode, checks file permissions, allocates a file descriptor, and returns control to the user program. The `read()` system call copies data from the file system buffer cache or storage device into the user-provided buffer. The `close()` system call releases the file descriptor and updates file system structures. Each system call involves mode switching overhead, which is why the OS minimizes the number of system calls needed for operations.

### Example 3: User Interface Evolution

Windows operating system evolution illustrates user interface development:

- **Windows 1.0 (1985)**: Basic windows with tiled rectangles
- **Windows 95 (1995)**: Start menu, taskbar, plug and play
- **Windows XP (2001)**: Green-themed interface, grouping similar tasks
- **Windows 10 (2015)**: Cortana integration, virtual desktops, continuous updates
- **Windows 11 (2021)**: Centered taskbar, rounded corners, snap layouts

Each evolution maintained backward compatibility while introducing new interaction paradigms, demonstrating how OS user interfaces must balance innovation with user expectations.

## Exam Tips

1. **Understand the dual role of OS**: Remember that an operating system serves both users (providing convenient interface) and the computer system itself (managing resources efficiently). This dual perspective is fundamental to understanding OS design.

2. **Differentiate between user mode and kernel mode**: In exams, questions frequently ask about the distinction between user mode and kernel mode (privileged mode). Be clear that system calls are the only way for user programs to transition to kernel mode.

3. **Know the types of system calls**: The five main categories are process control, file management, device management, information maintenance, and communication. Be able to give examples of each.

4. **Explain with real-world analogies**: During exam answers, use analogies like the OS as a manager/secretary, or as a government providing services to citizens, to explain abstract concepts.

5. **Remember the evolution timeline**: Know the sequence from batch processing to time-sharing to modern distributed systems, understanding how OS functions evolved with hardware capabilities.

6. **Focus on efficiency vs. convenience trade-off**: This is a key concept in OS design. The OS must balance making the system easy to use with using resources efficiently.

7. **Know the components of GUI**: Remember WIMP - Windows, Icons, Menus, Pointers - as the standard components of graphical user interfaces.