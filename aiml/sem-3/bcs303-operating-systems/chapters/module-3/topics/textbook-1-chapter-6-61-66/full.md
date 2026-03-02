# **Textbook 1: Chapter – 6 (6.1-6.6) - Operating Systems**

## **6.1 Introduction to Operating Systems**

An operating system (OS) is a software that manages computer hardware resources and provides common services to computer programs. It acts as an intermediary between computer hardware and user-level applications. The primary functions of an OS include:

- **Process Management**: creating, scheduling, and terminating processes
- **Memory Management**: managing memory allocation and deallocation
- **File Management**: creating, deleting, and managing files
- **Input/Output Management**: handling input/output operations between devices and programs
- **Security and Protection**: providing user authentication, access control, and memory protection

### History of Operating Systems

The first operating system, **CTSS (Compatible Time-Sharing System)**, was developed in the 1960s at the Massachusetts Institute of Technology (MIT). It was designed to support multiple users and provide a time-sharing environment.

In the 1970s, the development of the **Unix Operating System** revolutionized the field of operating systems. Unix was designed to be a multi-user, multi-tasking operating system that provided a portable and efficient way of managing computer resources.

In the 1980s, the **Microsoft Windows Operating System** was introduced, which provided a graphical user interface (GUI) and became widely popular in the 1990s.

Today, operating systems are ubiquitous in modern computing, ranging from mobile devices to servers and supercomputers.

## **6.2 Types of Operating Systems**

There are several types of operating systems, including:

### 1. **Single-User Operating Systems**

Single-user operating systems allow only one user to access the system at a time. Examples include:

- **MS-DOS**: an early operating system developed by Microsoft
- **Mac OS**: the original operating system for Apple Mac computers

### 2. **Multi-User Operating Systems**

Multi-user operating systems allow multiple users to access the system simultaneously. Examples include:

- **Unix**: a multi-user, multi-tasking operating system
- **Linux**: a free and open-source operating system based on Unix
- **Windows NT**: a multi-user, multi-tasking operating system developed by Microsoft

### 3. **Real-Time Operating Systems**

Real-time operating systems are designed to meet strict timing requirements, often used in embedded systems and control systems. Examples include:

- **VxWorks**: a real-time operating system used in military and aerospace applications
- **QNX**: a real-time operating system used in automotive and industrial control systems

### 4. **Mobile Operating Systems**

Mobile operating systems are designed for mobile devices, such as smartphones and tablets. Examples include:

- **Android**: a mobile operating system developed by Google
- **iOS**: a mobile operating system developed by Apple

## **6.3 Process Scheduling**

Process scheduling is the mechanism by which an operating system manages the execution of processes. There are several process scheduling algorithms, including:

### 1. **First-Come-First-Served (FCFS)**

In FCFS scheduling, the process that arrives first is executed first.

Example:

- Process A arrives at time 0 and executes for 5 units of time
- Process B arrives at time 5 and executes for 3 units of time

### 2. **Shortest Job First (SJF)**

In SJF scheduling, the process with the shortest execution time is executed first.

Example:

- Process A arrives at time 0 and executes for 5 units of time
- Process B arrives at time 5 and executes for 3 units of time
- Process C arrives at time 8 and executes for 2 units of time

### 3. **Priority Scheduling**

In priority scheduling, processes are assigned a priority based on their characteristics, and the process with the highest priority is executed first.

Example:

- Process A has a high priority and executes for 5 units of time
- Process B has a medium priority and executes for 3 units of time
- Process C has a low priority and executes for 2 units of time

## **6.4 Memory Management**

Memory management is the process of allocating and deallocating memory for running programs. There are several memory management algorithms, including:

### 1. **Virtual Memory**

Virtual memory is a memory management technique that uses a combination of physical and virtual memory to provide a larger address space.

Example:

- The operating system allocates a block of virtual memory to a process
- The physical memory is divided into frames, and the operating system swaps out frames to disk when they are not in use

### 2. **Paging**

Paging is a memory management technique that divides memory into fixed-size blocks called pages.

Example:

- The operating system divides the memory into 4KB pages
- The operating system allocates a page to a process and transfers it to physical memory if it is available

### 3. **Segmentation**

Segmentation is a memory management technique that divides memory into smaller segments.

Example:

- The operating system divides the memory into 4KB segments
- The operating system allocates a segment to a process and transfers it to physical memory if it is available

## **6.5 File Systems**

File systems are the mechanisms by which an operating system manages files on a storage device. There are several file system algorithms, including:

### 1. **Inode-Based File System**

Inode-based file systems use an inode to store file metadata.

Example:

- The operating system creates an inode for a file
- The inode contains information about the file, such as its permissions and location on disk

### 2. **Block-Based File System**

Block-based file systems use blocks to store file data.

Example:

- The operating system divides the disk into 512-byte blocks
- The operating system allocates a block to a file and updates the inode to reflect the new location

### 3. **Journaling File System**

Journaling file systems use a journal to log changes to the file system.

Example:

- The operating system writes data to disk and updates the journal
- The operating system reads the journal to reconstruct the file system in case of a failure

## **6.6 Security and Protection**

Security and protection are critical components of an operating system, ensuring that user data and system resources are protected from unauthorized access.

### 1. **User Authentication**

User authentication is the process of verifying a user's identity before allowing them to access the system.

Example:

- The operating system prompts the user for a username and password
- The operating system checks the username and password against a database to verify the user's identity

### 2. **Access Control**

Access control is the mechanism by which an operating system restricts access to system resources.

Example:

- The operating system assigns a security label to a file or directory
- The operating system checks the security label against the user's permissions to determine access

### 3. **Memory Protection**

Memory protection is the mechanism by which an operating system prevents a process from accessing memory that it does not own.

Example:

- The operating system divides the memory into regions, each with its own protection mechanism
- The operating system enforces access control lists (ACLs) to ensure that processes only access memory they are authorized to access

**Further Reading**

- **"Operating System Concepts"** by Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne
- **"The Art of Computer Programming"** by Donald E. Knuth
- **"Operating System Design and Implementation"** by Andrew S. Tanenbaum and Maarten J. van Steen
- **"Linux Device Drivers"** by Jonathan Corbet, Alessandro Rubini, and Greg Kroah-Hartman

Diagrams and illustrations are available online at [insert link].
