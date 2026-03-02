# What Operating Systems Do

## Introduction to Operating Systems

An Operating System (OS) is the most fundamental software that runs on a computer. It acts as an intermediary between the user and the computer hardware. The primary purpose of an operating system is to provide an environment in which a user can execute programs conveniently and efficiently. Without an operating system, every application would need to include its own code to handle low-level hardware operations, which would be incredibly inefficient and make software development immensely complex.

At its core, an operating system is a resource manager. It manages all the components of a computer system, from the central processing unit (CPU) and memory to storage devices and input/output (I/O) peripherals, ensuring they work together harmoniously to perform the tasks requested by the user and the applications.

## The Four Core Functions of an Operating System

An operating system performs four primary functions, which can be summarized as follows:

### 1. Process Management

The CPU can only execute one instruction from one program at a time. However, a modern computer system gives the illusion that many programs are running simultaneously (e.g., a web browser, a word processor, and a music player). This is called **multitasking**. The OS is responsible for this illusion.

- **Process Scheduling:** The OS decides which process gets the CPU, when, and for how long. This is handled by the **CPU Scheduler**. Different scheduling algorithms (e.g., First-Come, First-Served, Round Robin) are used to maximize CPU utilization and ensure fairness.
- **Process Creation and Termination:** The OS provides mechanisms (like the `fork()` system call) to create new processes and to end them.
- **Inter-Process Communication (IPC):** Processes often need to communicate with each other or synchronize their actions to avoid conflicts (e.g., two programs trying to print to the same printer). The OS provides methods like shared memory and message passing to facilitate this.

```
+-------------------+ +-------------------+
| Process A | | Process B |
| (Web Browser) | | (Word Processor) |
+-------------------+ +-------------------+
 | |
 v v
+---------------------------------------------+
| OPERATING SYSTEM (OS) |
| +-----------------------------------------+ |
| | CPU SCHEDULER | |
| | (Decides which process runs on the CPU) | |
| +-----------------------------------------+ |
+---------------------------------------------+
 | |
 v v
+---------------------------------------------+
| HARDWARE |
| (The CPU itself) |
+---------------------------------------------+
```

### 2. Memory Management

A computer's main memory (RAM) is a critical resource that must be carefully managed. Every program needs memory to store its instructions and data. The OS is responsible for:

- **Allocation and Deallocation:** Keeping track of which parts of memory are in use and by which process. When a process requests memory, the OS allocates it; when the process terminates, the OS reclaims that memory.
- **Protection:** Ensuring that one process cannot access the memory space of another process. This is crucial for system stability and security.
- **Virtual Memory:** Using the hard disk to extend the apparent size of physical RAM. This allows systems to run programs larger than the physical memory available. The OS handles the complex task of swapping data between RAM and disk transparently.

```
Program's View (Virtual Address Space) OS's View (Physical Memory)
+-------------------------+ +-----------------------------+
| Stack | | Process B (Segment) |
| (grows downwards) | +-----------------------------+
|-------------------------| | Process A (Segment) |
| Heap | +-----------------------------+
| (grows upwards) | | Operating System |
|-------------------------| +-----------------------------+
| Data Segment |
|-------------------------|
| Code (Text) Segment |
+-------------------------+
```

### 3. File System Management

The OS provides a uniform, logical view of information storage on various physical media (hard drives, SSDs, USB drives, etc.). It abstracts the messy details of tracks and sectors into a user-friendly concept of files and directories.

- **File Creation/Deletion:** Provides commands and APIs for programs to create and delete files.
- **Directory Organization:** Organizes files into a hierarchical directory structure for easy navigation and organization.
- **Access Control:** Determines who can access which files and what they can do with them (read, write, execute).
- **Disk Scheduling:** Optimizes the order of read/write requests to a disk to minimize seek time and maximize disk throughput.

### 4. Device Management (I/O System Management)

A computer system has many peripheral devices (keyboard, mouse, monitor, printer, network card). The OS:

- **Provides a Driver Interface:** Device drivers are OS-specific software that know how to communicate with specific hardware. The OS provides a standard interface for these drivers, so the rest of the OS doesn't need device-specific code.
- **Buffering and Caching:** Temporarily holds data in memory to smooth out the speed differences between fast CPUs and slower I/O devices.
- **Spooling:** Manages requests for devices that cannot be multiplexed, like a printer. It queues print jobs so multiple applications can "print" at once, even though the printer can only handle one job at a time.

## Operating System as an Extended Machine

This perspective, often attributed to computer scientist Maurice Wilkes, views the OS as a **virtual machine**. The raw hardware (the "bare metal") is complex and difficult to program. For instance, a programmer would not want to write code to directly manage the read/write head of a hard disk.

The OS provides a simpler, more beautiful, and more powerful abstraction. It hides the tedious hardware details and presents the programmer with a clean, elegant set of system calls (APIs) to use. For example, instead of writing to specific disk sectors, a programmer can simply call `fwrite("myfile.txt", data)`.

## Operating System as a Resource Manager

This is the other key viewpoint. The OS acts as a referee and allocator for the computer's resources.

- **Resource Allocation:** When multiple users or multiple jobs are running, the OS must allocate resources (CPU cycles, memory, file storage, I/O devices) to each of them. Allocation policies must be fair and efficient to avoid starvation (a process never getting a resource) and deadlock (processes waiting for each other indefinitely).
- **Control and Protection:** The OS must control the use of these resources, ensuring that erroneous or malicious programs cannot cause the whole system to crash. It enforces rules about which processes can access which resources.

## Key OS Services

To achieve its goals, an operating system provides a set of common services to application programs and users:

| Service                      | Description                                                                                                                                                  |
| :--------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Interface (UI)**      | Allows users to interact with the system. Can be a Command-Line Interface (CLI), Graphical User Interface (GUI), or touch-based.                             |
| **Program Execution**        | The system must be able to load a program into memory and run it, ending its execution either normally or abnormally.                                        |
| **I/O Operations**           | Provides a mechanism for running programs to perform input and output, shielding them from the specifics of device management.                               |
| **File System Manipulation** | Programs need to read, write, create, and delete files. The OS handles these operations and the necessary permission checks.                                 |
| **Communications**           | Allows processes to exchange information, either on the same computer or between computers over a network.                                                   |
| **Error Detection**          | The OS must be constantly aware of possible errors (e.g., in the CPU, memory, I/O devices, or in user programs) and take appropriate action to correct them. |
| **Resource Allocation**      | Allocates resources to multiple users or multiple jobs running concurrently.                                                                                 |
| **Accounting**               | Keeps track of which users use how much and what kinds of computer resources. This can be for billing or simple usage statistics.                            |
| **Protection and Security**  | Controls access to system resources, ensuring that all access is controlled and that the system is secure from external threats.                             |

## Exam Tips

1. **Dual Role:** Always remember the two main roles of an OS: **Extended Machine** (hides hardware complexity) and **Resource Manager** (allocates and protects hardware components).
2. **The Kernel is Key:** Understand that the core, most privileged part of the OS that performs these fundamental tasks is called the **kernel**. It is always resident in memory.
3. **System Calls are the Gateway:** Application programs request OS services via **system calls**. This is the fundamental interface between a process and the OS. Be prepared to explain this mechanism.
4. **Think in Abstractions:** For each function (process, memory, file), identify what abstraction the OS provides (process/thread, virtual address space, file/directory) and why that abstraction is useful.
5. **Compare and Contrast:** Be able to compare the responsibilities of the OS in process management vs. memory management. They are distinct but deeply interrelated.
6. **Examples Matter:** Use concrete examples. Instead of just saying "manages devices," say "manages the printer through spooling to allow multiple users to print at once."
