# Operating System Structure

### Overview

- An operating system (OS) is a software that manages computer hardware and software resources.
- It acts as an intermediary between hardware and application software.

### System Components

- **Hardware Components**:
  - Central Processing Unit (CPU)
  - Memory (RAM)
  - Input/Output (I/O) Devices
  - Storage Devices (e.g., hard disk, solid-state drive)
- **Software Components**:
  - Kernel (core OS)
  - Device Drivers
  - System Libraries
  - Applications

### Operating System Structure

- **Monolithic Operating System**:
  - Single kernel manages all system resources
  - Advantages: simplicity, fast boot time
  - Disadvantages: difficult to modify, limited scalability
- **Microkernel Operating System**:
  - Small kernel manages minimal system resources
  - Advantages: scalability, flexibility, and fault tolerance
  - Disadvantages: complex, slower boot time

### Key Concepts

- **Process Scheduling**:
  - Round Robin Scheduling: each process gets equal time slices
  - Priority Scheduling: processes with higher priority get priority
- **Memory Management**:
  - Virtual Memory: uses secondary storage for main memory
  - Page Replacement Algorithms: LRU, FIFO, Optimal
- **File System**:
  - File Allocation Table (FAT): maps files to disk locations
  - File System Hierarchical Structure (FSH): organizes files in a tree-like structure

### Important Formulas and Definitions

- **Page Fault**: occurs when a process accesses a page that is not in memory
- **Swap Space**: a portion of memory used to store pages of a process not in main memory
- **Memory Virtualization**: a technique to provide multiple virtual machines on a single physical machine

### Theorems

- **Amdahl's Law**: limits the performance of a parallel algorithm due to serial components
- **Gilder's Law**: predicts the speedup of a parallel algorithm based on the number of processors and the serial components.
