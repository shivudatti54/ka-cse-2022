# **System Structures: What Operating Systems Do**

## **Introduction**

Operating systems (OS) are complex software that manage computer hardware resources and provide common services to computer programs. At its core, an operating system is a system structure that provides a platform for running applications and managing system resources. In this module, we will delve into the different system structures that operating systems do, exploring their historical context, modern developments, and applications.

## **System Structures**

An operating system performs a variety of tasks, which can be categorized into three main system structures:

### 1. Process Management

Process management refers to the ability of an operating system to create, schedule, and terminate processes. A process is a program in execution, and the operating system manages the allocation and deallocation of system resources such as memory, I/O devices, and CPU time.

**Process Creation**

When a process is created, the operating system allocates resources such as:

- Memory: The operating system reserves a block of memory for the process and loads the program into it.
- CPU Time: The operating system allocates CPU time for the process, which is the amount of time the CPU spends executing the process.
- I/O Devices: The operating system assigns I/O devices such as disk drives, network interfaces, and printers to the process.

**Process Scheduling**

Process scheduling is the task of allocating CPU time to processes. The operating system uses various algorithms to schedule processes, such as:

- First-Come-First-Served (FCFS): The operating system allocates CPU time to the first process in the queue.
- Shortest Job First (SJF): The operating system allocates CPU time to the process with the shortest execution time.
- Priority Scheduling: The operating system allocates CPU time to processes based on their priority.

**Process Termination**

When a process is terminated, the operating system releases its allocated resources. The operating system can terminate a process in various ways, such as:

- Abortion: The operating system terminates a process immediately.
- Suspension: The operating system suspends a process, which can be resumed later.

### 2. Memory Management

Memory management refers to the ability of an operating system to allocate and deallocate memory for processes. The operating system uses various techniques to manage memory, such as:

- Paged Virtual Memory: The operating system divides the physical memory into fixed-size blocks called pages. Processes can request pages from the operating system, which can allocate or deallocate pages as needed.
- Segmented Memory: The operating system divides the memory into fixed-size blocks called segments. Processes can request segments from the operating system, which can allocate or deallocate segments as needed.

### 3. File System Management

File system management refers to the ability of an operating system to manage files and directories. The operating system uses various techniques to manage files, such as:

- Hierarchical File System: The operating system organizes files into a hierarchical structure, with directories and subdirectories.
- Indexed File System: The operating system uses an index to locate files and directories.

**Case Study: File System Hierarchy Standard (FHS)**

The File System Hierarchy Standard (FHS) is a standard for organizing files on a Linux system. The FHS specifies the location of system files and directories, such as `/bin`, `/etc`, and `/usr`. The FHS ensures consistency and readability across different Linux systems, making it easier for developers to write portable code.

## **Applications of System Structures**

System structures are essential for operating systems, as they enable the efficient management of system resources and the execution of applications. Some applications of system structures include:

- **Desktop Operating Systems**: Windows, macOS, and Linux desktop operating systems use various system structures to manage processes, memory, and files.
- **Mobile Operating Systems**: Android and iOS mobile operating systems use various system structures to manage processes, memory, and files on mobile devices.
- **Server Operating Systems**: Linux and Windows Server operating systems use various system structures to manage processes, memory, and files on servers.

## **Modern Developments**

Modern operating systems have evolved to include various features and technologies, such as:

- **Virtualization**: Operating systems can create virtual machines, which can run multiple operating systems on a single physical machine.
- **Cloud Computing**: Operating systems can provide cloud-based services, such as storage and computing resources.
- **Artificial Intelligence**: Operating systems can use artificial intelligence to optimize system performance and provide personalized services to users.

## **Diagrams and Descriptions**

### Process Scheduling Algorithm

The following diagram illustrates the process scheduling algorithm:

```markdown
+---------------+
| Process |
+---------------+
|
| Scheduling Algorithm
v
+---------------+
| First-Come-First-Served |
+---------------+
|
| SJF: Shortest Job First
v
+---------------+
| Priority Scheduling |
+---------------+
```

### Memory Management Techniques

The following diagram illustrates the memory management techniques:

```markdown
+---------------+
| Paged Virtual Memory |
+---------------+
|
| Pages
v
+---------------+
| Physical Memory |
+---------------+
|
| Segmented Memory
v
+---------------+
| Segmented Memory |
+---------------+
```

## **Further Reading**

- "Operating System Concepts" by Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne
- "The Art of Operating System Design" by Martin F. Cowling and Brian N. Bershad
- "Linux Device Drivers" by Jonathan Corbet, Alessandro Rubini, and Greg Kroah-Hartman

In conclusion, system structures are a fundamental aspect of operating systems, enabling the efficient management of system resources and the execution of applications. Understanding system structures is essential for developing operating systems, as well as for improving the performance and security of existing systems.
