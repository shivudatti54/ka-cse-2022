# Introduction to Operating Systems

## Introduction

An Operating System (OS) is the fundamental software that manages computer hardware resources and provides services to application programs. It serves as an intermediary between the computer user and the computer hardware, creating an environment in which users can execute programs conveniently and efficiently. Without an operating system, a computer would be useless—users would need to understand complex hardware details to perform even the simplest tasks.

The operating system is perhaps the most important piece of software in any computer system. It controls every file, every memory allocation, and every process running on the system. When you turn on your computer, the OS is loaded into memory and remains active until you shut down. It controls the execution of all other software, from web browsers to text editors, ensuring that multiple programs can run concurrently without interfering with each other.

In the context of the University of Delhi's Computer Science curriculum, understanding operating systems is crucial because it provides insight into how software interacts with hardware, how system resources are managed, and how multiple processes compete for limited resources. This knowledge forms the foundation for advanced topics in system programming, distributed computing, and network administration.

## What is an Operating System?

An operating system is a collection of system software that acts as an interface between computer hardware and users. It performs two primary functions: resource management and user interface provision. The OS manages hardware components like the CPU, memory, storage devices, and input/output devices, allocating these resources efficiently among various programs and users.

From a user perspective, the operating system provides a user-friendly interface that hides the complexities of the underlying hardware. Users interact with the OS through graphical user interfaces (GUIs) or command-line interfaces (CLIs) without needing to understand how the hardware actually works. For example, when you save a document, the OS handles the complex process of finding space on the hard drive, managing file directories, and ensuring data is written correctly.

From a system perspective, the OS acts as a resource manager. It must coordinate and allocate resources to prevent conflicts and ensure system efficiency. The CPU can execute only one instruction at a time, yet we run multiple applications simultaneously. The OS creates the illusion of concurrency through rapid context switching, giving each process a tiny time slice to execute. Similarly, the OS manages memory allocation, ensuring each program has its own address space and preventing unauthorized access to other programs' memory.

## Evolution of Operating Systems

The evolution of operating systems mirrors the development of computer hardware and user requirements. In the earliest computer systems, there was no operating system at all. Programmers interacted directly with the hardware using machine language, and a single program controlled the entire machine. This was extremely inefficient and浪费 (wasteful).

The first operating systems emerged in the 1950s with the advent of batch processing systems. These early OSs automated job transitions, allowing multiple jobs to be queued and processed automatically without manual intervention. The IBM 701 and IBM 704 were among the first computers to use simple batch operating systems.

The 1960s saw the development of multiprogramming systems, which allowed multiple programs to reside in memory simultaneously. This significantly improved CPU utilization by keeping the processor busy while waiting for I/O operations to complete. Time-sharing systems emerged in the late 1960s and 1970s, enabling multiple users to interact with the computer simultaneously through terminals.

The 1980s brought personal computer operating systems like MS-DOS, which provided simple command-line interfaces for individual users. The graphical user interface, pioneered by Apple's Macintosh and later adopted by Microsoft Windows, revolutionized personal computing by making computers accessible to non-technical users.

Modern operating systems, such as Windows, macOS, Linux, and Android, are incredibly sophisticated, supporting complex features like virtual memory, multiprocessing, security mechanisms, and network connectivity. They must manage resources across diverse hardware configurations and provide stable platforms for countless applications.

## Types of Operating Systems

Operating systems can be categorized based on their usage, number of users, and processing capabilities. Understanding these types helps in selecting appropriate systems for different computing environments.

**Batch Operating Systems** process jobs in batches without user interaction. Programs and data are collected and processed together. Though largely obsolete today, batch processing principles are still used in mainframe environments and server systems for handling large volumes of transactions.

**Time-Sharing Operating Systems** allow multiple users to access the computer simultaneously through terminals. The OS rapidly switches between users, creating the illusion that each user has dedicated access to the system. Unix and Linux are prominent examples of time-sharing systems that evolved into modern multiuser operating systems.

**Real-Time Operating Systems** (RTOS) are designed for applications requiring immediate response to external events. These systems are used in industrial control systems, medical devices, aircraft control, and robotics where timing is critical. Real-time systems must guarantee response within strict time constraints.

**Network Operating Systems** provide networking capabilities and allow computers to communicate and share resources over a network. Windows Server and Linux distributions designed for servers fall into this category. These systems include built-in support for network protocols, file sharing, and printer sharing.

**Distributed Operating Systems** manage multiple interconnected computers that appear as a single system to users. The resources and processing load are distributed across multiple machines, providing greater reliability and performance. While true distributed operating systems are rare, distributed computing concepts are fundamental to cloud computing and grid computing environments.

## Functions of an Operating System

The operating system performs several essential functions that enable computer systems to operate efficiently and user-friendly. These functions can be broadly categorized into resource management functions and user interface functions.

**Process Management** involves creating, scheduling, and terminating processes. A process is a program in execution, and the OS must manage multiple processes competing for CPU time. The OS uses scheduling algorithms to determine which process runs when, ensuring fair CPU allocation while maximizing throughput and minimizing turnaround time.

**Memory Management** tracks which parts of memory are in use and which are free, allocates memory to processes when needed, and deallocates memory when processes terminate. Modern operating systems use virtual memory techniques, allowing programs to use more memory than physically available by swapping data between RAM and disk storage.

**File Management** provides mechanisms for storing, retrieving, and organizing data on storage devices. The OS maintains file system structures, manages file directories, handles file operations (create, read, write, delete), and implements security by controlling access to files.

**Device Management** coordinates and controls input/output devices through device drivers. The OS provides a uniform interface for interacting with different devices, handles device scheduling, and manages buffers to improve I/O performance.

**Security and Protection** ensures that system resources are accessed only by authorized users and processes. The OS implements authentication mechanisms, access control lists, and permission systems to protect data and prevent unauthorized system access.

## Operating System as Resource Manager

One of the most important perspectives on operating systems is viewing them as resource managers. A computer system consists of various resources—CPU time, memory space, disk storage, and I/O devices—that must be allocated among competing processes. The OS serves as the resource manager, making critical decisions about resource allocation.

Consider a scenario where multiple applications are running simultaneously: a web browser, a music player, and a document editor. The CPU can execute only one instruction at a time, yet all three applications appear to run simultaneously. The OS achieves this through rapid context switching, allocating small time slices to each process. When the web browser needs to wait for network data, the OS quickly switches to the music player, and then to the document editor, creating the illusion of parallel execution.

Memory management is equally critical. Each process requires its own memory space, and the OS must prevent processes from accessing memory allocated to other processes or the OS itself. Virtual memory extends available memory by using disk space as an extension of RAM, allowing larger programs to run on systems with limited physical memory.

I/O device management requires handling the significant speed difference between CPU and I/O devices. While a process waits for data from a slow disk drive or network, the OS can schedule other processes to use the CPU productively. This technique, known as spooling, is particularly important for optimizing system performance.

## Examples

**Example 1: Process Scheduling in Action**

Consider a single-core CPU running three processes: P1 (compute-intensive), P2 (I/O-bound), and P3 (interactive). Without an OS, only one process could run at a time. With process scheduling, the OS implements time-sharing:

At time 0ms, P1 starts executing. After 10ms, an I/O request is made. Rather than waiting idly, the OS performs a context switch to P2. P2 begins its I/O operation and yields to wait. The OS switches to P3, which handles user input. When P1's I/O completes, the OS switches back to P1. This rapid switching, perhaps hundreds of times per second, creates the illusion that all processes run simultaneously.

This example illustrates how the OS maximizes CPU utilization by keeping the processor busy with productive work whenever possible, rather than waiting for slow I/O operations.

**Example 2: Memory Management with Virtual Memory**

Suppose a system has 4GB of RAM, and a user opens three applications: a video editor requiring 3GB, a browser requiring 1GB, and a spreadsheet requiring 1GB. Total requirement is 5GB, exceeding physical memory.

The OS uses virtual memory to handle this. It allocates 3GB to video editor, 1GB to browser, and initially 0.5GB to spreadsheet. When the spreadsheet needs more memory, the OS identifies rarely used memory pages from other applications, writes them to the swap file on disk, and loads the required pages into physical memory. If the video editor accesses a page that was swapped out, a page fault occurs, and the OS loads the required page back into memory, possibly swapping out another page.

This technique allows programs to use more memory than physically available, though with some performance cost when pages must be swapped.

**Example 3: File System Management**

When a user saves a document named "Assignment.docx", the OS performs numerous operations:

First, the OS searches the file system directory to find available space. It locates clusters on the disk that are not in use. It creates a new directory entry containing the filename, creation date, file size, and pointers to the allocated disk clusters. It updates the file allocation table (FAT) or equivalent structure to mark these clusters as in use. Finally, it writes the document data to the allocated clusters.

If the user later renames the file, only the directory entry is modified—the actual file data remains unchanged. If the user deletes the file, the directory entry is removed, and the clusters are marked as available for reuse. The actual data remains until overwritten by new files.

## Exam Tips

1. DEFINITIONS ARE CRITICAL: Know precise definitions of operating system, process, memory management, and other core concepts. DU exams frequently ask for short definitions.

2. UNDERSTAND THE DUAL ROLE: Remember that an OS serves two primary purposes—as a resource manager and as a user interface. This dual perspective is fundamental to understanding OS design.

3. KNOW DIFFERENT OS TYPES: Be prepared to explain the differences between batch, time-sharing, real-time, network, and distributed operating systems with examples of each.

4. STUDY EVOLUTION HISTORY: Understand the chronological development of operating systems from early batch processing to modern systems. This provides context for current features.

5. FOCUS ON RESOURCE MANAGEMENT: The OS as resource manager is a crucial concept. Understand how CPU, memory, and I/O resources are managed and allocated.

6. MEMORIZE KEY FUNCTIONS: The five main functions of an OS—process management, memory management, file management, device management, and security/protection—are frequently asked in exams.

7. DIFFERENTIATE PROCESS AND PROGRAM: A program is passive instructions stored on disk; a program in execution is called a process. This distinction is important.

8. KNOW VIRTUAL MEMORY: Virtual memory is a critical concept allowing programs larger than physical memory to execute. Understand paging, swapping, and page faults.

9. PREPARE FOR SHORT ANSWER QUESTIONS: Practice writing concise answers (50-100 words) for questions like "What is an operating system?" or "Explain the functions of an OS."

10. UNDERSTAND REAL-TIME SYSTEMS: Real-time operating systems are increasingly important. Know the difference between hard and soft real-time systems.