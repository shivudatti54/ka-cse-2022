# **System Structures: What Operating Systems Do**

## **Introduction**

Operating systems (OS) are software programs that manage computer hardware and software resources. In this module, we will explore the different system structures that operating systems use to manage these resources.

## **System Structures**

There are several system structures that operating systems use to manage computer resources. These include:

### 1. **Process Structure**

A process structure refers to the way in which an operating system manages multiple processes (programs) running on the computer.

- **Process Scheduling**: This is the process by which the operating system assigns a specific time slice (called a time quantum) to each process, allowing it to execute for a short period before being interrupted by another process.
-     **Process Communication**: This refers to the way in which processes can exchange data with each other.
- **Process Synchronization**: This is the process by which the operating system ensures that multiple processes accessing shared resources do not interfere with each other.

**Example:**
Suppose we have two processes, P1 and P2, running on a computer. Process P1 is a web browser, and process P2 is a word processor. The operating system assigns a time quantum of 100 milliseconds to process P1, allowing it to execute for 100 milliseconds before being interrupted by process P2.

### 2. **Thread Structure**

A thread structure refers to the way in which an operating system manages multiple threads (small, independent programs) running on the computer.

- **Thread Scheduling**: This is the process by which the operating system assigns a specific time slice to each thread, allowing it to execute for a short period before being interrupted by another thread.
- **Thread Communication**: This refers to the way in which threads can exchange data with each other.
- **Thread Synchronization**: This is the process by which the operating system ensures that multiple threads accessing shared resources do not interfere with each other.

**Example:**
Suppose we have two threads, T1 and T2, running on a computer. Thread T1 is responsible for rendering a web page, and thread T2 is responsible for handling user input. The operating system assigns a time quantum of 50 milliseconds to thread T1, allowing it to execute for 50 milliseconds before being interrupted by thread T2.

### 3. **Job Structure**

A job structure refers to the way in which an operating system manages multiple jobs (programs) running on the computer.

- **Job Scheduling**: This is the process by which the operating system assigns a specific time slice to each job, allowing it to execute for a short period before being interrupted by another job.
- **Job Communication**: This refers to the way in which jobs can exchange data with each other.
- **Job Synchronization**: This is the process by which the operating system ensures that multiple jobs accessing shared resources do not interfere with each other.

**Example:**
Suppose we have two jobs, J1 and J2, running on a computer. Job J1 is a compiler, and job J2 is a debugger. The operating system assigns a time quantum of 200 milliseconds to job J1, allowing it to execute for 200 milliseconds before being interrupted by job J2.

### 4. **File Structure**

A file structure refers to the way in which an operating system manages files (collections of data) on the computer.

- **File Organization**: This refers to the way in which files are stored and accessed on the computer.
- **File Access Control**: This is the process by which the operating system regulates access to files.
- **File Protection**: This is the process by which the operating system ensures that files are protected from unauthorized access or modification.

**Example:**
Suppose we have a file called "document.txt" that contains a collection of text data. The operating system stores the file on a hard drive and organizes it in a hierarchical structure, allowing users to access and modify the file as needed.

### 5. **Memory Structure**

A memory structure refers to the way in which an operating system manages physical memory (RAM) on the computer.

- **Memory Allocation**: This is the process by which the operating system assigns a specific block of memory to a process or program.
- **Memory Protection**: This is the process by which the operating system ensures that processes do not access each other's memory.
- **Memory Virtualization**: This is the process by which the operating system provides a virtualized view of physical memory, allowing multiple processes to share the same physical memory.

**Example:**
Suppose we have a process that requires a block of memory to execute. The operating system allocates a specific block of memory to the process and protects it from other processes that may try to access it.

### 6. **Input/Output Structure**

An input/output (I/O) structure refers to the way in which an operating system manages input/output operations between the computer and external devices.

- **I/O Scheduling**: This is the process by which the operating system assigns a specific time slice to each I/O operation, allowing it to execute for a short period before being interrupted by another I/O operation.
- **I/O Buffering**: This is the process by which the operating system temporarily stores data in a buffer before transferring it to external devices.
- **I/O Error Handling**: This is the process by which the operating system detects and handles I/O errors.

**Example:**
Suppose we have a printer that needs to print a document. The operating system schedules the I/O operation and assigns a specific time slice to the printer, allowing it to execute for a short period before completing the print job.

### 7. **Interrupt Structure**

An interrupt structure refers to the way in which an operating system manages interrupts (synchronous and asynchronous events) that occur while a process is running.

- **Interrupt Handling**: This is the process by which the operating system handles interrupts and schedules the affected process to resume execution.
- **Interrupt Priority**: This is the process by which the operating system assigns a specific priority to each interrupt, allowing it to interrupt processes in a specific order.
- **Interrupt Masking**: This is the process by which the operating system masks interrupts that do not need to be handled, preventing them from interrupting processes.

**Example:**
Suppose we have a process that is executing a program and receives an interrupt from a keyboard input. The operating system handles the interrupt, schedules the process to resume execution, and allows other processes to interrupt the process if necessary.

### 8. **Deadlock Structure**

A deadlock structure refers to the way in which an operating system manages deadlocks ( situations in which two or more processes are blocked indefinitely due to a circular wait).

- **Deadlock Detection**: This is the process by which the operating system detects potential deadlocks in a system.
- **Deadlock Prevention**: This is the process by which the operating system prevents deadlocks from occurring in the first place.
- **Deadlock Recovery**: This is the process by which the operating system recovers from a deadlock, allowing processes to resume execution.

**Example:**
Suppose we have two processes, P1 and P2, that are holding resources in a circular wait. The operating system detects the deadlock and prevents it from occurring, allowing processes to resume execution.

## **Conclusion**

In conclusion, operating systems use various system structures to manage computer resources. These include process structure, thread structure, job structure, file structure, memory structure, input/output structure, interrupt structure, and deadlock structure. Understanding these system structures is essential for developing efficient and effective operating systems.
