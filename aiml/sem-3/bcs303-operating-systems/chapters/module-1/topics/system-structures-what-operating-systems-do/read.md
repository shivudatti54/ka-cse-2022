# **System Structures: What Operating Systems Do**

## **Introduction**

An operating system (OS) is a software that manages computer hardware resources and provides services to computer programs. In this module, we will explore the different system structures that operating systems provide and why they are essential for efficient computer operation.

## **File System Structure**

A file system is a critical component of an operating system, responsible for storing and managing files on a computer. The file system structure consists of the following components:

### File System Hierarchy Standard (FSHS)

The FSHS is a standard for organizing files on a computer. It consists of the following hierarchy:

- Root directory (/)
- Directories (e.g., Documents, Pictures, etc.)
- Files (e.g., text documents, images, etc.)

Example of a file system hierarchy:

```markdown
/
|-- Documents
| |-- report.txt
| |-- presentation.pptx
|-- Pictures
| |-- vacation.jpg
|-- Videos
| |-- movie.mp4
```

### File System Types

There are two main types of file systems:

- **FAT (File Allocation Table)**: used by Windows operating systems
- **NTFS (New Technology File System)**: used by Windows operating systems

### File System Operations

File system operations include:

- **Create**: creates a new file or directory
- **Delete**: deletes a file or directory
- **Read**: retrieves the contents of a file
- **Write**: updates the contents of a file

## **Process Management Structure**

Process management is responsible for managing the execution of programs on a computer. The process management structure consists of the following components:

### Process Scheduling

Process scheduling is responsible for allocating system resources to processes. There are two main scheduling algorithms:

- **First-Come-First-Served (FCFS)**: processes are executed in the order they are received
- **Shortest Job First (SJF)**: processes with the shortest execution time are executed first

### Process Synchronization

Process synchronization is responsible for coordinating the execution of multiple processes. Synchronization techniques include:

- **Mutual Exclusion**: ensures that only one process can access a shared resource at a time
- **Semaphores**: used to control access to shared resources

### Process Communication

Process communication is responsible for exchanging data between processes. Techniques include:

- **Sockets**: used for network communication
- **Shared Memory**: used for direct memory access

## **Memory Management Structure**

Memory management is responsible for managing the allocation and deallocation of memory for programs. The memory management structure consists of the following components:

### Memory Allocation

Memory allocation is responsible for allocating memory to programs. Techniques include:

- **Static Memory Allocation**: memory is allocated at compile-time
- **Dynamic Memory Allocation**: memory is allocated at runtime

### Memory Deallocation

Memory deallocation is responsible for freeing memory from programs. Techniques include:

- **Stack**: memory is allocated on the system call stack
- **Heap**: memory is allocated on the heap

### Page Replacement

Page replacement is responsible for managing the memory hierarchy. Techniques include:

- **LRU (Least Recently Used)**: the least recently used page is replaced
- **LRU Cache**: the least recently used page is stored in a cache

## **I/O Management Structure**

I/O management is responsible for managing input/output operations between devices and programs. The I/O management structure consists of the following components:

### I/O Devices

I/O devices include:

- **Keyboard**: input device
- **Monitor**: output device
- **Hard Drive**: storage device

### I/O Operations

I/O operations include:

- **Read**: retrieves data from a device
- **Write**: updates data in a device
- **Interrupt**: signal to the operating system that an I/O operation is complete

## **Conclusion**

In conclusion, the system structures provided by operating systems are essential for efficient computer operation. The file system structure manages files on a computer, process management structures manage program execution, memory management structures manage memory allocation and deallocation, and I/O management structures manage input/output operations. Understanding these system structures is crucial for designing and implementing efficient operating systems.

**Key Concepts:**

- System structures
- File system hierarchy standard (FSHS)
- File system types (FAT, NTFS)
- Process scheduling algorithms (FCFS, SJF)
- Process synchronization techniques (mutual exclusion, semaphores)
- Process communication techniques (sockets, shared memory)
- Memory allocation techniques (static, dynamic)
- Memory deallocation techniques (stack, heap)
- Page replacement techniques (LRU, LRU cache)
- I/O devices and operations (keyboard, monitor, hard drive, read, write, interrupt)
