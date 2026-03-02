# Operating System Structure

## Introduction

The design and internal organization of an operating system varies significantly across different systems. Since an OS is a large and complex piece of software, it must be engineered carefully. A common approach is to partition the OS into smaller, well-defined components (modules) rather than having one monolithic program. The way these components are interconnected and organized defines the **structure** of the operating system.

## 1. Simple / Monolithic Structure

### MS-DOS Structure

MS-DOS was designed to provide the most functionality in the least space. It was **not divided into well-defined modules**. Although MS-DOS had some structure, its interfaces and levels of functionality were not well separated.

```
+------------------------------------------+
| Application Programs |
+------------------------------------------+
| Resident System Program |
+------------------------------------------+
| MS-DOS Device Drivers |
+------------------------------------------+
| ROM BIOS Device Drivers |
+------------------------------------------+
```

**Limitations of MS-DOS:**

- Application programs could access hardware directly (bypassing the OS)
- No separation between user mode and kernel mode
- A single misbehaving application could crash the entire system
- No memory protection between processes

### Early UNIX Structure (Monolithic Kernel)

The original UNIX operating system had a limited structure. It consisted of two separable parts: the kernel and the system programs. The kernel was further structured into a series of interfaces and device drivers, but everything below the system call interface and above the physical hardware was the kernel.

```
+------------------------------------------+
| Users |
+------------------------------------------+
| Shells and Commands |
| Compilers and Interpreters |
| System Libraries |
+------------------------------------------+ <-- System Call Interface
| |
| Signals Terminal Character I/O |
| Handling system Terminal drivers |
| |
| File System Swapping Block I/O |
| Demand system |
| Paging Disk drivers |
| |
| CPU Scheduling Page Replacement |
| Virtual Memory |
+------------------------------------------+ <-- Kernel Interface to Hardware
| Terminal Controllers Device Controllers|
| Memory Controllers Terminals |
| Physical Memory Disks |
+------------------------------------------+
```

**Characteristics of Monolithic Structure:**

- All OS functionality is packed into a single layer (the kernel)
- Very fast execution because there is minimal overhead
- Difficult to maintain and extend -- a bug in one part can crash the entire kernel
- No clear separation of concerns
- **Examples:** Traditional UNIX, Linux (partially), MS-DOS

### Advantages and Disadvantages

| Aspect            | Details                                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| **Advantages**    | High performance (direct function calls within kernel), simple to implement initially                     |
| **Disadvantages** | Hard to debug and modify, one error can crash the whole system, difficult to maintain as the system grows |

## 2. Layered Approach

In the layered approach, the OS is divided into a number of layers (levels), each built on top of lower layers. The bottom layer (layer 0) is the hardware; the highest layer (layer N) is the user interface.

Each layer uses only the functions and services of the layer directly below it.

```
+------------------------------------------+
| Layer N: User Interface |
+------------------------------------------+
| Layer N-1: ... |
+------------------------------------------+
| ... |
+------------------------------------------+
| Layer 2: Memory Management |
+------------------------------------------+
| Layer 1: CPU Scheduling |
+------------------------------------------+
| Layer 0: Hardware |
+------------------------------------------+
```

### THE Operating System (by Dijkstra, 1968)

The THE system was the first layered OS, developed by Edsger Dijkstra:

| Layer | Function                       |
| ----- | ------------------------------ |
| 5     | User programs                  |
| 4     | Buffering for I/O devices      |
| 3     | Operator-console device driver |
| 2     | Memory management              |
| 1     | CPU scheduling                 |
| 0     | Hardware                       |

### Advantages of Layered Approach

- **Simplicity of construction and debugging:** Each layer is implemented using only operations provided by lower layers. Errors can be isolated to a specific layer.
- **Abstraction:** Each layer hides the details of its implementation from higher layers.
- **Modularity:** Easy to replace or modify one layer without affecting others.

### Disadvantages of Layered Approach

- **Difficult to define layers appropriately:** It is challenging to determine the correct ordering of layers. For example, the device driver for disk space must be at a lower level than memory management routines.
- **Performance overhead:** Each layer adds overhead because a request must pass through multiple layers. A system call may need to traverse several layers before reaching the hardware.
- **Less efficient** than monolithic systems due to inter-layer communication overhead.

## 3. Microkernel Architecture

A microkernel approach structures the OS by removing all non-essential components from the kernel and implementing them as user-level programs. The result is a smaller kernel that provides only the most essential functions:

- **Inter-process communication (IPC)**
- **Basic memory management**
- **CPU scheduling**
- **Low-level I/O**

All other services (file system, device drivers, networking) run in **user space** as separate processes.

```
+-------+ +-------+ +-------+ +--------+
| File | |Device | |Network| | App |
|System | |Driver | |Server | |Program |
+---+---+ +---+---+ +---+---+ +---+----+
 | | | |
 +----------+----+-----+----------+
 |
 +-------+-------+
 | Microkernel |
 | (IPC, Memory, |
 | Scheduling) |
 +-------+-------+
 |
 +-------+-------+
 | Hardware |
 +---------------+
```

Communication between user-level services happens through **message passing** via the microkernel.

### Examples of Microkernel Systems

- **Mach** (Carnegie Mellon University) -- foundation for macOS
- **MINIX** -- educational OS by Andrew Tanenbaum
- **QNX** -- real-time OS used in automotive and embedded systems
- **L4** -- high-performance microkernel family

### Advantages of Microkernel

| Advantage         | Explanation                                                           |
| ----------------- | --------------------------------------------------------------------- |
| **Reliability**   | If a user-level service crashes, it does not bring down the entire OS |
| **Security**      | Less code running in kernel mode means a smaller attack surface       |
| **Portability**   | Easier to port to new hardware (only the microkernel needs changes)   |
| **Extensibility** | New services can be added to user space without modifying the kernel  |
| **Flexibility**   | Services can be started/stopped independently                         |

### Disadvantages of Microkernel

| Disadvantage                    | Explanation                                                                                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Performance overhead**        | Message passing between user-space services and the kernel is slower than direct function calls in a monolithic kernel |
| **Increased system complexity** | Designing efficient IPC mechanisms is challenging                                                                      |
| **Context switching overhead**  | Frequent switches between user mode and kernel mode                                                                    |

## 4. Modular Approach / Loadable Kernel Modules (LKM)

The modular approach uses **object-oriented programming** techniques to create a modular kernel. The kernel has a set of core components and can dynamically link in additional services either at boot time or at runtime through **loadable kernel modules (LKMs)**.

```
+------------------------------------------+
| Core Kernel |
| +----------+ +----------+ +--------+ |
| | Process | | Memory | | Core | |
| | Sched. | | Mgmt. | | IPC | |
| +----------+ +----------+ +--------+ |
| |
| Loadable Modules: |
| +--------+ +--------+ +--------+ |
| | File | | Device | |Network | ... |
| | System | | Driver | | Stack | |
| +--------+ +--------+ +--------+ |
+------------------------------------------+
```

### Key Features

- Each core function is a **separate module** with well-defined interfaces
- Modules can be **loaded and unloaded dynamically** at runtime using commands like `insmod` and `rmmod` in Linux
- Any module can communicate with any other module directly (unlike the layered approach)
- Similar to microkernel in modularity but more efficient because modules run in **kernel space** (no message passing overhead)

### Examples

- **Linux** -- uses loadable kernel modules extensively (e.g., device drivers, file systems)
- **Solaris** -- modular kernel design with dynamically loadable modules

### Advantages

- Flexible: new functionality added without rebooting
- Efficient: modules communicate directly in kernel space
- Combines the best of monolithic (performance) and microkernel (modularity)

### Disadvantages

- A buggy module can still crash the kernel (runs in kernel space)
- Less isolation compared to microkernel approach

## 5. Hybrid Systems

Most modern operating systems are not purely one structure but combine multiple approaches to address performance, security, and usability needs.

### macOS / iOS (Apple)

macOS uses a **hybrid approach** combining:

- **Mach microkernel** -- provides memory management, IPC, thread scheduling
- **BSD subsystem** -- provides CLI interface, networking, file systems, POSIX API
- Combined into the **XNU kernel** (X is Not Unix)
- Cocoa framework provides the GUI (Aqua interface)

```
+------------------------------------------+
| User Experience (Aqua GUI) |
+------------------------------------------+
| Application Frameworks (Cocoa) |
+------------------------------------------+
| Core Frameworks |
+------------------------------------------+
| Kernel Environment |
| +--------+ +---------+ +----------+ |
| | Mach | | BSD | | I/O Kit | |
| +--------+ +---------+ +----------+ |
+------------------------------------------+
```

### Windows

Windows is largely **monolithic** but incorporates a **microkernel-like** layered design:

- **HAL (Hardware Abstraction Layer)** at the bottom
- **Executive** services (process management, memory, I/O, security)
- **Kernel** provides thread scheduling, interrupt handling
- Subsystems (Win32, POSIX) run partly in user space

### Android

Android uses a **modified Linux kernel** at the base with:

- Linux kernel for process management, memory, drivers
- Android Runtime (ART) for running applications
- Application Framework providing high-level services
- Applications at the top layer

## Comparison of OS Structures

| Feature             | Simple/Monolithic | Layered  | Microkernel      | Modular        | Hybrid                  |
| ------------------- | ----------------- | -------- | ---------------- | -------------- | ----------------------- |
| **Performance**     | High              | Moderate | Lower            | High           | High                    |
| **Reliability**     | Low               | Moderate | High             | Moderate       | High                    |
| **Maintainability** | Low               | High     | High             | High           | Moderate                |
| **Extensibility**   | Low               | Moderate | High             | High           | High                    |
| **Portability**     | Low               | Moderate | High             | Moderate       | Moderate                |
| **Complexity**      | Low               | Moderate | High             | Moderate       | High                    |
| **Examples**        | MS-DOS, UNIX      | THE      | Mach, QNX, MINIX | Linux, Solaris | macOS, Windows, Android |

## Key Differences at a Glance

```
Monolithic: [Everything in Kernel] --> Fast but fragile

Layered: [Layer N] --> [Layer N-1] --> ... --> [Hardware]
 Ordered but slow

Microkernel: [Minimal Kernel] + [User-space Services]
 Safe but slow IPC

Modular: [Core Kernel] + [Loadable Modules in Kernel Space]
 Flexible and fast

Hybrid: Combines multiple approaches for real-world needs
```

## Exam Tips

1. **Draw diagrams:** exams frequently ask you to draw the structure of MS-DOS, UNIX, or microkernel systems. Practice drawing clean, labeled diagrams.
2. **Comparison table:** "Compare monolithic, layered, and microkernel architectures" is a classic 10-mark question. Know the comparison table well.
3. **Know examples for each:** MS-DOS and UNIX for monolithic, THE for layered, Mach/QNX/MINIX for microkernel, Linux/Solaris for modular.
4. **Layered approach:** Remember the THE system layers (0 to 5) -- Dijkstra's contribution.
5. **Microkernel key concept:** Services run in user space, communicate via message passing. This improves reliability but reduces performance.
6. **Modular vs Microkernel:** Both are modular, but modules run in kernel space (modular) vs user space (microkernel). This is a subtle but important difference.
7. **Hybrid systems:** Modern OSes like macOS (Mach + BSD), Windows (monolithic + layered), and Android (Linux kernel + framework) combine approaches. Mentioning these shows deeper understanding.
8. **Loadable Kernel Modules:** Know that Linux uses `insmod`, `rmmod`, `lsmod` commands to manage kernel modules dynamically.
