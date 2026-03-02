# Operating Systems: Definition, Structure, and Operations

## A Comprehensive Study Material for BSc Physical Science (CS) - Ge5A Operating Systems

---

## 1. Introduction and Real-World Relevance

Imagine waking up to your smartphone alarm, checking your emails on a laptop, withdrawing cash from an ATM, or booking a ride through a rideshare application. What do all these diverse technological experiences have in common? At the core of every computing device—from the smallest embedded system to the most powerful supercomputer—lies an **Operating System (OS)** that orchestrates all hardware and software interactions.

The operating system serves as the **intermediary between computer hardware and user applications**. Without an operating system, users would need to write complex low-level code to control every hardware component directly. The OS abstracts this complexity, providing a consistent and user-friendly interface while efficiently managing system resources.

In today's digital economy, operating systems power everything from personal computers and mobile devices to cloud infrastructure and Internet of Things (IoT) devices. Understanding OS concepts is fundamental for any computer science professional, as it provides insight into how software interacts with hardware, how system resources are managed, and how security and stability are maintained.

This study material covers the **Delhi University NEP 2024 syllabus** requirements for the "Os Definition Structure Operations" topic in the Ge5A Operating Systems course, addressing all key concepts with detailed explanations, practical examples, and comprehensive assessment items.

---

## 2. Operating System Definition and Objectives

### 2.1 What is an Operating System?

An **Operating System** is a system software that acts as an interface between computer hardware and end-users. It provides a platform for application programs to run and serves as a resource manager, controlling and allocating system resources efficiently.

According to renowned computer scientist **Andrew Tanenbaum**, an OS is "the program that, after being initially loaded into the computer by a boot program, manages all the other programs in a computer."

### 2.2 Goals of an Operating System

The primary objectives of an operating system include:

| Goal | Description |
|------|-------------|
| **Convenience** | Make computer usage easier and more user-friendly |
| **Efficiency** | Ensure optimal utilization of system resources (CPU, memory, I/O devices) |
| **Ability to Evolve** | Allow for system improvements and enhancements without disrupting services |
| **Isolation** | Provide protection and security between different processes and users |

### 2.3 OS as a Resource Manager

The operating system functions as a **resource manager** for the following system components:

- **Processor (CPU)**: Manages process scheduling and execution
- **Main Memory**: Allocates and deallocates memory space to processes
- **Secondary Storage**: Controls file systems and data persistence
- **I/O Devices**: Handles input/output operations through device drivers

### 2.4 OS as a Virtual Machine (Extended Machine)

Operating systems provide **abstraction** by hiding hardware complexities:

- Users see a simplified interface rather than complex hardware details
- Application programs interact with the OS through standard interfaces
- Hardware variations are managed by the OS, ensuring portability

---

## 3. Operating System Structure Types

The internal organization of an operating system determines its architecture. The three fundamental OS structure types are:

### 3.1 Monolithic Structure

In a **monolithic architecture**, the entire operating system runs as a single, large kernel with all components (process management, memory management, file system, device drivers) tightly integrated.

**Characteristics:**
- All OS services reside in kernel space
- Direct function calls between components
- High performance due to minimal overhead
- Difficult to maintain and extend
- Single point of failure

**Examples:**
- Traditional UNIX (e.g., Bell Labs UNIX, early Linux versions)
- MS-DOS

**Advantages:**
- Efficient inter-component communication
- High performance due to kernel-level execution

**Disadvantages:**
- Complex and difficult to modify
- Bug in any component can crash the entire system
- Poor scalability

### 3.2 Microkernel Structure

**Microkernel architecture** minimizes the kernel, moving most services (file systems, device drivers, process scheduling) to user-space servers. The kernel only handles essential functions: basic IPC, memory management, and CPU scheduling.

**Characteristics:**
- Minimal kernel (only ~10,000 lines of code)
- Services run as separate processes in user mode
- Communication via message passing
- High modularity and extensibility

**Examples:**
- MINIX 3
- GNU Hurd
- macOS (hybrid approach using microkernel for core functions)

**Code Example: Microkernel Message Passing**

```c
// Simple message passing structure in a microkernel
typedef struct {
    int source;           // Source process ID
    int destination;      // Destination process ID
    int type;             // Message type
    void *data;           // Message payload
    size_t size;          // Data size
} message_t;

// Send message function
int send_message(message_t *msg) {
    // Validate message
    if (!msg || msg->destination < 0) {
        return -1;  // Error
    }
    
    // Add to destination's message queue
    return kernel_route_message(msg);
}

// Receive message function
int receive_message(message_t *msg, int sender) {
    return kernel_dequeue_message(get_current_process_id(), sender, msg);
}
```

**Advantages:**
- High reliability (failure in one service doesn't crash system)
- Easy to extend and maintain
- Better security through isolation
- Portability across different hardware platforms

**Disadvantages:**
- Higher overhead due to message passing
- Potentially slower performance compared to monolithic systems

### 3.3 Layered Structure

**Layered architecture** organizes the OS into hierarchical layers, where each layer provides services to the layer above it and uses services from the layer below.

**Typical Layer Hierarchy:**

| Layer | Function |
|-------|----------|
| Layer 0 | Hardware (CPU, Memory, Devices) |
| Layer 1 | Processor Management & Interrupt Handling |
| Layer 2 | Memory Management |
| Layer 3 | Device Driver Management |
| Layer 4 | File System |
| Layer 5 | User Interface / Shell |

**Characteristics:**
- Clear separation of concerns
- Each layer only interacts with adjacent layers
- Easier to debug and modify
- Provides protection through well-defined interfaces

**Examples:**
- THE (Technische Hogeschool Eindhoven) OS - Dijkstra's pioneering layered OS
- Windows NT (hybrid approach with layered design)
- Modern UNIX systems

**Advantages:**
- Simplified design and implementation
- Ease of debugging (isolated layers)
- Flexibility in implementation

**Disadvantages:**
- Strict layer hierarchy can limit performance
- Overhead from layer-to-layer communication

---

## 4. Boot Process

The **boot process** (bootstrap) is the sequence of events that occurs when a computer is powered on, loading the operating system into memory. Understanding the boot process is essential for system administrators and developers.

### 4.1 Detailed Boot Sequence

```
┌─────────────────────────────────────────────────────────────┐
│                    COMPUTER POWER ON                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  1. POST (Power-On Self-Test)                               │
│     - Basic hardware initialization                         │
│     - Memory test, video adapter check                      │
│     - BIOS/UEFI firmware execution                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. BIOS/UEFI Initialization                                │
│     - Load configuration settings                           │
│     - Identify boot device (HDD, SSD, USB, Network)        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Boot Loader Execution                                   │
│     - MBR (Master Boot Record) / GPT read                   │
│     - Load boot loader from boot device                     │
│     - Examples: GRUB, Windows Boot Manager                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  4. Kernel Loading                                          │
│     - Kernel image copied to RAM                            │
│     - Kernel decompression (if compressed)                  │
│     - Control transferred to kernel entry point             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  5. Kernel Initialization                                   │
│     - CPU mode switch (real to protected mode)              │
│     - Memory management initialization                      │
│     - Device driver initialization                          │
│     - Root file system mounting                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  6. Init Process (Systemd/init)                             │
│     - First process (PID 1) starts                          │
│     - Run system services and daemons                       │
│     - Start graphical interface/login manager               │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Key Boot Components

**BIOS (Basic Input/Output System):**
- Legacy firmware stored in ROM
- Performs POST and loads MBR
- Limited to 16-bit mode addressing

**UEFI (Unified Extensible Firmware Interface):**
- Modern replacement for BIOS
- Supports GPT partitioning (GUID Partition Table)
- Faster boot times and better security (Secure Boot)
- GUI support in firmware settings

**Boot Loader:**
- Small program that loads the OS kernel
- GRUB (Grand Unified Boot Loader) for Linux
- Windows Boot Manager for Windows systems

---

## 5. System Calls

**System calls** are the fundamental interface between user programs and the operating system kernel. They provide a controlled entry point to kernel services, allowing user applications to request privileged operations.

### 5.1 Types of System Calls

| Category | System Calls | Purpose |
|----------|--------------|---------|
| **Process Control** | fork(), exec(), wait(), exit() | Create, manage, and terminate processes |
| **File Management** | open(), read(), write(), close(), lseek() | Create, read, write, and manage files |
| **Device Management** | ioctl(), read(), write() | Communicate with hardware devices |
| **Information Maintenance** | getpid(), getuid(), uname() | Retrieve system and process information |
| **Communication** | pipe(), socket(), connect() | Inter-process communication (IPC) |
| **Protection** | chmod(), chown(), setuid() | File permissions and access control |

### 5.2 System Call Implementation

When a program makes a system call, the following sequence occurs:

```
User Program → Library Wrapper (glibc) → System Call Interface → Kernel → Hardware
```

**Example: System Call for Process Creation (fork)**

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    
    printf("Before fork - Process ID: %d\n", getpid());
    
    // fork() system call creates a new process
    pid = fork();
    
    if (pid < 0) {
        // Error occurred
        fprintf(stderr, "Fork failed!\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process
        printf("I am the child process (PID: %d, Parent PID: %d)\n", 
               getpid(), getppid());
    }
    else {
        // Parent process
        printf("I am the parent process (PID: %d, Child PID: %d)\n", 
               getpid(), pid);
    }
    
    return 0;
}
```

**Example: System Call for File Operations**

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd;
    char buffer[] = "Hello from Operating Systems course!";
    char read_buffer[100];
    
    // open() system call - create/open a file
    fd = open("example.txt", O_CREAT | O_WRONLY, 0644);
    
    if (fd < 0) {
        perror("Error opening file");
        return 1;
    }
    
    // write() system call - write to file
    write(fd, buffer, strlen(buffer));
    
    // close() system call - close file descriptor
    close(fd);
    
    // Reopen for reading
    fd = open("example.txt", O_RDONLY);
    
    // read() system call - read from file
    read(fd, read_buffer, sizeof(read_buffer));
    
    printf("Read from file: %s\n", read_buffer);
    close(fd);
    
    return 0;
}
```

### 5.3 System Call vs Function Call

| Aspect | System Call | Function Call |
|--------|-------------|---------------|
| Execution Mode | User mode → Kernel mode | User mode only |
| Privileges | Can execute privileged instructions | Cannot access hardware directly |
| Speed | Slower (mode switch overhead) | Faster (same address space) |
| Purpose | Request OS services | Local computation |

---

## 6. Operating System Operations

The operating system performs several critical operations to manage system resources and provide services to users and applications.

### 6.1 Process Management

A **process** is an instance of a program in execution. The OS is responsible for:

- **Process Creation and Termination**: Creating new processes and cleaning up after completion
- **Process Scheduling**: Determining which process runs on the CPU and when
- **Process Synchronization**: Managing concurrent access to shared resources
- **Process Communication**: Enabling inter-process communication (IPC)

**Process States:**
```
        ┌──────────────┐
        │    NEW      │
        │  (Created)  │
        └──────┬───────┘
               │ admitted
               ▼
        ┌──────────────┐
        │   READY      │◄─────────────┐
        │   (Waiting)  │               │ scheduler dispatch
        └──────┬───────┘               │
               │                       │
               ▼                       │
        ┌──────────────┐               │
        │   RUNNING    │───────────────┘
        │  (Executing) │
        └──────┬───────┘
               │ interrupt / I/O wait
               ▼
        ┌──────────────┐
        │    WAITING   │ (Blocked for I/O)
        └──────┬───────┘
               │ I/O completion
               ▼
        ┌──────────────┐
        │   TERMINATED │
        └──────────────┘
```

### 6.2 Memory Management

Memory management ensures efficient use of RAM by:

- **Allocation**: Assigning memory to processes
- **Deallocation**: reclaiming memory when processes terminate
- **Protection**: Preventing unauthorized access to memory regions
- **Virtual Memory**: Extending available memory using disk space

**Memory Management Techniques:**
1. **Contiguous Allocation**: Single block of memory per process
2. **Paging**: Fixed-size pages mapped to frames
3. **Segmentation**: Variable-sized segments with logical meaning
4. **Page Tables**: Translation from virtual to physical addresses

### 6.3 File Management

The OS provides a hierarchical file system with:

- **File Operations**: Create, read, write, delete, rename
- **Directory Management**: Organizing files in a hierarchy
- **File Protection**: Access control based on permissions
- **Space Allocation**: Managing disk space for files

### 6.4 I/O Device Management

The OS handles I/O through:

- **Device Drivers**: Software modules that control hardware
- **Buffering**: Temporary storage for data during transfer
- **Caching**: Fast storage for frequently accessed data
- **Spooling**: Queueing I/O requests for sequential devices (e.g., printers)

---

## 7. Assessment Items

### 7.1 Multiple Choice Questions (MCQs)

**Level 1: Easy**

1. Which of the following is NOT a goal of an Operating System?
   - A) Convenience
   - B) Efficiency
   - C) Compilation
   - D) Ability to Evolve

2. In which OS structure type do most services run in user space?
   - A) Monolithic
   - B) Layered
   - C) Microkernel
   - D) Hybrid

3. What is the first program that runs when a computer boots?
   - A) Kernel
   - B) Boot Loader
   - C) BIOS/UEFI
   - D) Init Process

**Level 2: Medium**

4. Which system call is used to create a new process in Unix/Linux?
   - A) create()
   - B) fork()
   - C) new()
   - D) spawn()

5. In a layered operating system structure, which layer is closest to the hardware?
   - A) Layer 5 (User Interface)
   - B) Layer 3 (Device Drivers)
   - C) Layer 1 (Processor Management)
   - D) Layer 0 (Hardware)

6. What type of kernel architecture does Linux primarily use?
   - A) Pure Microkernel
   - B) Layered
   - C) Monolithic with loadable modules
   - D) Hybrid

7. Which of the following is a function of the OS as a resource manager?
   - A) Providing user interface
   - B) Managing CPU scheduling
   - C) Running application software
   - D) Compiling source code

**Level 3: Hard**

8. In the microkernel architecture, communication between user-level services typically uses:
   - A) Shared memory
   - B) Direct function calls
   - C) Message passing
   - D) Interrupt handling

9. Which boot component is responsible for loading the operating system kernel into memory?
   - A) BIOS/UEFI
   - B) Boot Loader
   - C) POST
   - D) Init process

10. The operating system provides protection by:
    - A) Allowing all processes unrestricted access to memory
    - B) Defining user permissions and enforcing isolation
    - C) Disabling antivirus software
    - D) Limiting network access

### 7.2 Flashcards

| # | Term/Concept | Definition/Explanation |
|---|---------------|------------------------|
| 1 | **Operating System** | System software that acts as an interface between hardware and users, managing resources and providing services |
| 2 | **Monolithic Kernel** | OS architecture where all services run in kernel space with direct function calls; high performance but less modular |
| 3 | **Microkernel** | Minimal kernel design where most services run in user space; communicates via message passing for better reliability |
| 4 | **Boot Process** | Sequence from power-on through POST, BIOS/UEFI, boot loader, kernel loading to init process startup |
| 5 | **System Call** | Programming interface for user programs to request kernel services; involves mode switch from user to kernel mode |
| 6 | **Process** | An instance of a program in execution with its own address space, program counter, and system resources |
| 7 | **Virtual Memory** | Memory management technique that extends available memory using disk space, providing illusion of larger RAM |
| 8 | **Device Driver** | Kernel module that interfaces between OS and hardware devices, translating generic I/O requests to device-specific commands |

---

## 8. Key Takeaways

1. **OS Definition**: An operating system is system software that serves as an interface between hardware and users, managing resources efficiently while providing convenience and isolation.

2. **OS Structure Types**:
   - **Monolithic**: All services in kernel space; high performance but complex maintenance
   - **Microkernel**: Minimal kernel with services in user space; better reliability through message passing
   - **Layered**: Hierarchical organization where each layer uses services from below

3. **Boot Process**: Power-on → POST → BIOS/UEFI → Boot Loader → Kernel Loading → Init Process → User Login

4. **System Calls**: Controlled interface for user programs to access kernel services; examples include fork(), open(), read(), write()

5. **OS Operations**: Process management (scheduling, synchronization), memory management (allocation, virtual memory), file management (hierarchical organization), and I/O device management (device drivers)

6. **Real-World Relevance**: Understanding OS concepts is essential for software development, system administration, cybersecurity, and cloud computing careers

---

## References and Further Reading

- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
- Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems* (4th ed.). Pearson.
- Stallings, W. (2018). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson.
- Delhi University, NEP 2024 Syllabus - Ge5A Operating Systems

---

*This study material is prepared for BSc Physical Science (CS) students at Delhi University as part of the NEP 2024 curriculum.*