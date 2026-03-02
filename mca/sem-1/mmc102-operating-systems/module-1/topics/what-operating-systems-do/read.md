# What Operating Systems Do


## Table of Contents

- [What Operating Systems Do](#what-operating-systems-do)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The Operating System as an Extended Machine](#the-operating-system-as-an-extended-machine)
  - [The Operating System as a Resource Manager](#the-operating-system-as-a-resource-manager)
  - [Operating System Services](#operating-system-services)
  - [Evolution of Operating Systems](#evolution-of-operating-systems)
  - [Types of Operating Systems](#types-of-operating-systems)
- [Examples](#examples)
  - [Example 1: Process Creation and Management](#example-1-process-creation-and-management)
  - [Example 2: Memory Management in Action](#example-2-memory-management-in-action)
  - [Example 3: Device Management and I/O Scheduling](#example-3-device-management-and-io-scheduling)
- [Exam Tips](#exam-tips)

## Introduction

An Operating System (OS) serves as the fundamental software layer between computer hardware and user applications, acting as an indispensable intermediary that manages hardware resources while providing a consistent interface for application software. The operating system is arguably the most critical component of any computer system, whether it manifests as the familiar Windows desktop, the command-line driven Linux distributions, or the embedded systems controlling household appliances. Without an operating system, users would need to interact directly with complex hardware through tedious machine code, making computing accessible only to highly specialized programmers. The operating system abstracts this complexity, presenting users and applications with a simplified, logical view of the system while efficiently coordinating the underlying physical resources.

The importance of operating systems in modern computing cannot be overstated. Every computational task, from sending an email to training machine learning models, ultimately depends on the services provided by the operating system. When a user clicks an icon, the OS translates this action into hardware operations; when an application requires memory, the OS allocates and manages this resource; when multiple programs run simultaneously, the OS ensures fair and efficient sharing of the CPU. This dual role as both a service provider to applications and a manager of hardware resources defines the essence of what operating systems do. For students studying computer science, understanding operating system concepts is fundamental because these principles underlie all modern software development and system administration.

## Key Concepts

### The Operating System as an Extended Machine

One of the most illuminating perspectives on operating systems views them as providing a virtual or extended machine that abstracts the complexities of raw hardware. Hardware components such as disk drives, memory modules, and CPU registers possess intricate technical specifications and operational details that application programmers should not need to understand. The operating system presents a clean, abstract interface that hides these implementation details. For instance, when an application needs to store data, it invokes high-level file operations like "create," "read," or "write" without needing to know the specifics of magnetic disk organization, solid-state drive wear leveling, or sector-level encoding. This abstraction layer transforms the complex physical machine into a logical device that is easier to program against, effectively extending the capabilities of the underlying hardware.

The concept of virtualization extends this idea further. Modern operating systems create virtual representations of hardware components, such as virtual memory that makes programs appear to have access to more memory than physically available, or virtual CPUs that allow multiple processes to share a single processor. This virtualization enables features like memory protection, where one program cannot access the memory allocated to another, and process isolation, which prevents failures in one application from crashing the entire system. Operating systems like VMware and Hyper-V take this concept to the next level by virtualizing entire computers, allowing multiple operating systems to run simultaneously on a single physical machine.

### The Operating System as a Resource Manager

The second fundamental view characterizes the operating system as a resource manager that controls and allocates the various hardware components of a computer system. A computer system consists of multiple resources, including the central processing unit (CPU), main memory, secondary storage, input/output devices, and network bandwidth. The operating system must manage these resources efficiently, ensuring that all computational tasks receive adequate resources while preventing any single task from monopolizing the entire system. This resource management role becomes particularly critical in multi-user and multi-tasking environments where numerous processes compete for limited resources.

Resource management in operating systems involves several key functions. The CPU scheduler determines which process gets to execute and for how long, implementing time-sharing through rapid context switching. Memory management tracks which portions of RAM are in use and by whom, allocating memory to processes as needed and swapping data between main memory and secondary storage when RAM becomes exhausted. The file system manages the organization and access to data stored on disks, maintaining metadata about files and directories while ensuring data integrity and security. Device drivers, which are specialized software modules within the operating system, manage communication with hardware peripherals, translating generic I/O requests into device-specific commands.

The efficiency of resource management directly impacts system performance. A poorly designed operating system may suffer from excessive context switching overhead, memory thrashing where pages are constantly swapped in and out of memory, or I/O bottlenecks that leave the CPU waiting idle. Modern operating systems employ sophisticated algorithms and heuristics to optimize resource allocation, using techniques like priority scheduling, caching, and prefetching to improve throughput and responsiveness. Understanding these resource management mechanisms is essential for system administrators and software developers who need to configure and optimize computing environments.

### Operating System Services

Operating systems provide a wide range of services that support both users and application programs. These services form the interface through which software interacts with the system, and understanding them is crucial for comprehending operating system design. The most fundamental services include program execution, which involves loading programs into memory, initializing them for execution, and managing their completion; I/O operations, which provide interfaces for reading from and writing to devices; file system manipulation, which allows creating, deleting, reading, and modifying files and directories; communications, which enable processes to exchange data either on the same machine or across a network; and error detection, which monitors the system for hardware malfunctions and software errors, taking appropriate corrective action.

Beyond these basic services, modern operating systems provide additional capabilities for system protection and security. User authentication verifies the identity of individuals attempting to access the system, typically through passwords, biometric scans, or security tokens. Access control lists and permission mechanisms determine which resources each user can access and what operations they can perform. Auditing and logging facilities record system activities for security analysis and troubleshooting. These security features have become increasingly important as computers store sensitive information and connect to networks where malicious actors may attempt unauthorized access.

### Evolution of Operating Systems

The role and complexity of operating systems have evolved dramatically since the earliest electronic computers. Early machines lacked any operating system; programmers interacted directly with hardware through front panels, entering binary instructions manually. The first operating systems emerged in the 1950s to automate job scheduling and reduce the time lost to manual setup between programs. Batch processing systems collected jobs into batches and executed them sequentially, using a monitor program to control the transition between jobs. These early operating systems were primitive by modern standards but established fundamental concepts like job queues and system calls.

The development of multiprogramming in the 1960s represented a major advancement, allowing multiple jobs to reside in memory simultaneously and enabling the CPU to switch between them when one waited for I/O. This approach dramatically improved CPU utilization by keeping the processor busy while some jobs waited for slow I/O operations. Time-sharing systems, which emerged in the 1970s, extended this concept to support multiple users interacting with the system simultaneously through terminals. The UNIX operating system, developed at Bell Labs, popularized many concepts that remain central to modern operating systems, including a hierarchical file system, hierarchical memory management, and a consistent device abstraction where devices appear as files in the file system.

Personal computer operating systems in the 1980s and 1990s simplified computing for non-technical users by emphasizing graphical user interfaces and ease of use. The Apple Macintosh, Microsoft Windows, and various versions of UNIX for PCs brought operating system concepts to mainstream computing. The rise of the internet in the 1990s and mobile computing in the 2000s introduced new requirements for networking, security, and power management. Modern operating systems like Windows, macOS, Linux, iOS, and Android continue to evolve, incorporating support for multi-core processors, virtualization, containerization, and cloud integration.

### Types of Operating Systems

Operating systems can be categorized based on their intended use and the number of users they support. Single-user operating systems, such as early versions of MS-DOS, serve one user at a time and typically lack sophisticated multi-tasking or security features. Single-task operating systems can run only one program at a time, though they may allow switching between programs through a simple interface. Multi-tasking operating systems can run multiple programs concurrently, giving the appearance that programs execute simultaneously through rapid context switching. Multi-user operating systems extend these capabilities to support multiple users accessing the system simultaneously, typically through terminals or network connections.

Real-time operating systems (RTOS) represent a specialized category designed for applications with strict timing requirements. Unlike general-purpose operating systems that optimize for throughput or fairness, real-time systems guarantee that tasks complete within specified time constraints. These systems are essential for embedded applications like automotive control systems, medical devices, and industrial automation where delayed responses could have serious consequences. Examples of real-time operating systems include VxWorks, FreeRTOS, and QNX. Understanding the characteristics of different operating system types helps in selecting the appropriate system for specific applications and in comprehending how operating system design involves trade-offs between competing objectives.

## Examples

### Example 1: Process Creation and Management

Consider the scenario where a user double-clicks a document icon to open it in a word processor. The operating system performs a sequence of operations to fulfill this request. First, the file manager locates the executable file associated with the word processor application and verifies that the user has permission to execute it. The operating system then creates a new process, allocating a process control block that contains information about the process, including its process identifier, priority, and current state. Memory management allocates address space for the program, loading the executable code and any required libraries into memory. The CPU scheduler adds the new process to the ready queue, and eventually the dispatcher switches the CPU to execute the word processor, displaying the document to the user.

When the user opens the document file, the application issues a system call to read the file. The operating system validates the request, checks file permissions, and if the data is not already cached in memory, issues a request to the disk driver. While the disk controller reads the data from physical storage, the operating system may suspend the word processor process and schedule another ready process to use the CPU productively. When the disk operation completes, the operating system copies the data into the application's memory and marks the word processor as ready to run again. This example illustrates how the operating system coordinates multiple hardware components and manages competing demands from different parts of the system.

### Example 2: Memory Management in Action

Suppose a user opens five different applications simultaneously on a computer with 8 gigabytes of RAM, where each application requires 2 gigabytes of memory. Clearly, the total requested memory (10 GB) exceeds the available physical memory. The operating system uses virtual memory management to handle this situation transparently. Each application operates in its own address space, believing it has access to the full 2 GB it requested. The operating system maintains page tables that map virtual addresses used by applications to physical addresses in RAM.

When an application accesses memory that is not currently in RAM, a page fault occurs. The operating system must retrieve the required page from secondary storage (typically a swap file or partition). If RAM is full, the memory manager selects a page to evict, writing it to swap if it has been modified. The required page is then read from swap into the freed physical memory, the page table is updated, and the application continues execution as if nothing happened. This entire process is invisible to the application program. The operating system may also use techniques like demand paging, where pages are loaded only when first accessed, and working set management, where it memory the pages that processes are keeps in actively using.

### Example 3: Device Management and I/O Scheduling

When a user prints a document, the operating system manages this I/O operation through several layers of abstraction. The application sends the document to the print subsystem using a high-level interface like "print document." The operating system's print spooler adds the job to a queue, managing multiple print requests fairly. The spooler communicates with the appropriate printer driver, which translates generic print commands into the specific language understood by the printer model. The driver interacts with the hardware through a device controller, sending data across the system bus to the printer.

In a system with multiple print jobs, the I/O scheduler determines the order in which requests are processed. Various scheduling algorithms may be employed: First-Come-First-Served processes requests in the order received; Shortest Job First minimizes average waiting time for short documents; or priority scheduling ensures important documents print before routine ones. The operating system buffers data between the application and printer, allowing the application to continue working while printing occurs in the background. If the printer is busy, the spooler holds additional jobs until the printer becomes available. This example demonstrates how operating systems provide device independence, allowing applications to use generic I/O operations regardless of the specific hardware installed.

## Exam Tips

Understanding operating system fundamentals requires grasping both theoretical concepts and practical implementations. The following points will help you perform well in examinations on this topic.

First, be able to explain the dual nature of operating systems as both an extended machine and a resource manager. This conceptual distinction is fundamental to understanding why operating systems exist and what functions they perform. Examiners frequently ask questions requiring you to describe these two views and explain how they relate to each other.

Second, memorize the key services that operating systems provide to users and applications. These include program execution, I/O operations, file system manipulation, communications, and error detection. Being able to list and briefly explain these services demonstrates your understanding of the operating system's role as an intermediary between applications and hardware.

Third, understand the evolution of operating systems from early batch processing through time-sharing to modern multi-purpose systems. Knowing how operating systems have evolved helps contextualize current features and understand why certain design decisions were made. Be familiar with major milestones and the operating systems associated with each era.

Fourth, be clear about the different types of operating systems based on their characteristics: single-user versus multi-user, single-task versus multi-task, and real-time versus general-purpose. Understanding the distinctions between these types and knowing examples of each will help you answer classification and comparison questions.

Fifth, practice drawing and explaining diagrams showing how operating systems interact with hardware and applications. Visual representations help clarify concepts and are often expected in exam answers. Be prepared to draw the layered architecture of operating systems and explain how each layer communicates with adjacent layers.

Sixth, understand key terms like system call, kernel, shell, device driver, and process. These terms frequently appear in examinations, and being able to define them precisely demonstrates your technical vocabulary. The kernel, in particular, is the core of the operating system that manages resources and provides essential services.

Seventh, be prepared to explain how operating systems handle resource conflicts when multiple processes compete for the same resources. This involves understanding concepts like scheduling, deadlock, and synchronization. Even at an introductory level, you should be able to explain why resource management is challenging and how operating systems address these challenges.