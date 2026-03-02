# **Textbook 1: Chapter 5: 5.1**

## **FUNDAMENTALS OF OPERATING SYSTEMS**

### 5.1 Introduction to Operating Systems

---

## **What is an Operating System?**

An operating system (OS) is a software that manages computer hardware resources and provides a platform for running application software. The OS acts as an intermediary between computer hardware and user-level applications, providing a layer of abstraction and making it easier to interact with the computer.

## **History of Operating Systems**

The first operating system, CP-40, was developed in 1956 by the Massachusetts Institute of Technology (MIT). However, the first commercially available operating system, CTSS (Compatible Time-Sharing System), was developed in 1961 by the MIT. The first successful commercial operating system, UNIX, was developed in 1969 by Bell Labs.

## **Types of Operating Systems**

There are three main types of operating systems:

1. **Single-user, single-tasking operating systems**: These operating systems allow only one user to run one application at a time. Examples include MS-DOS and early versions of Windows.
2. **Single-user, multi-tasking operating systems**: These operating systems allow one user to run multiple applications simultaneously. Examples include modern versions of Windows and macOS.
3. **Multi-user, multi-tasking operating systems**: These operating systems allow multiple users to run multiple applications simultaneously. Examples include Linux and Unix-like operating systems.

### 5.1.1 System Components

---

An operating system consists of several components that work together to manage computer hardware resources and provide a platform for running application software.

## **1. Hardware Abstraction Layer (HAL)**

The HAL is a layer of software that abstracts the underlying hardware components of the computer, making it easier to develop and maintain applications that run on the computer.

## **2. Device Drivers**

Device drivers are software components that manage the interaction between the operating system and device hardware. They translate operating system requests into hardware-specific commands and vice versa.

## **3. Memory Management Unit (MMU)**

The MMU is a hardware component that manages the allocation and deallocation of memory for running applications.

## **4. Process Management**

Process management is the set of functions that manage the creation, execution, and termination of processes. The operating system allocates resources such as memory and I/O devices to each process.

## **5. File System**

A file system is a hierarchical structure that organizes files and directories on the computer. The operating system manages the creation, deletion, and retrieval of files and directories.

### 5.1.2 System Calls

---

System calls are functions that are made by a program to request a service from the operating system. System calls provide a way for programs to interact with the operating system and its resources.

## **Types of System Calls**

There are two types of system calls:

1. **Process-related system calls**: These system calls manage the creation, execution, and termination of processes.
2. **I/O-related system calls**: These system calls manage the interaction between programs and I/O devices such as files, keyboards, and displays.

### 5.1.3 Interrupts

---

Interrupts are signals sent by hardware to the operating system to request attention. The operating system handles interrupts by temporarily suspending the current process and switching to the interrupt handler.

## **Types of Interrupts**

There are two types of interrupts:

1. **Hardware interrupts**: These interrupts are sent by hardware components such as I/O devices.
2. **Software interrupts**: These interrupts are sent by software components such as the operating system.

### 5.1.4 Scheduling

---

Scheduling is the process of allocating the CPU to a process. The operating system schedules processes using a scheduling algorithm that determines which process should run next.

## **Scheduling Algorithms**

There are several scheduling algorithms:

1. **First-Come-First-Served (FCFS)**: This algorithm allocates the CPU to the process that arrived first.
2. **Shortest Job First (SJF)**: This algorithm allocates the CPU to the process with the shortest execution time.
3. **Priority Scheduling**: This algorithm allocates the CPU to the process with the highest priority.

### 5.1.5 Memory Management

---

Memory management is the process of managing the allocation and deallocation of memory for running applications.

## **Memory Management Algorithms**

There are several memory management algorithms:

1. **Virtual Memory**: This algorithm uses a combination of RAM and disk storage to manage memory.
2. **Paging**: This algorithm divides memory into fixed-size blocks called pages.

### 5.1.6 I/O Management

---

I/O management is the process of managing the interaction between programs and I/O devices such as files, keyboards, and displays.

## **I/O Devices**

I/O devices are hardware components that allow programs to interact with external devices such as files, keyboards, and displays.

### 5.1.7 Networking

---

Networking is the process of managing the interaction between programs and network devices such as routers, switches, and servers.

## **Network Devices**

Network devices are hardware components that allow programs to interact with network devices such as routers, switches, and servers.

### 5.1.8 Security

---

Security is the process of protecting computer systems and data from unauthorized access.

## **Security Measures**

There are several security measures:

1. **Access Control**: This measure controls access to computer systems and data.
2. **Encryption**: This measure protects data from unauthorized access.
3. **Firewalls**: This measure controls incoming and outgoing network traffic.

### 5.1.9 Conclusion

---

In conclusion, an operating system is a software that manages computer hardware resources and provides a platform for running application software. The operating system consists of several components that work together to manage computer hardware resources and provide a platform for running application software.

## **Further Reading**

- **"Operating System Concepts"** by Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne
- **"Operating System Design and Implementation"** by Andrew S. Tanenbaum and Maarten van Steen
- **"The Art of Operating System Design"** by David R. Butenhof

**Diagram Descriptions**

- **Hardware Abstraction Layer (HAL) Diagram**: A block diagram of the HAL, showing the abstraction of hardware components.
- **Device Drivers Diagram**: A block diagram of device drivers, showing the interaction between the operating system and device hardware.
- **Memory Management Diagram**: A block diagram of memory management, showing the allocation and deallocation of memory.
- **Process Management Diagram**: A block diagram of process management, showing the creation, execution, and termination of processes.
