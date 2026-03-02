# Resource Management and Operating System Structures

## Overview

Resource Management is the core function of an operating system, involving the allocation and deallocation of hardware resources (CPU, memory, disk, I/O devices) and software resources (processes, files) to programs and users. OS structures define how the OS is internally organized to perform these management tasks.

## Key Points

- **Four Resource Types**: Process Management (CPU time), Memory Management (RAM), File System Management (storage), Device Management (I/O devices)
- **Process Management**: Process scheduling, synchronization, and deadlock handling using algorithms like FCFS, SJF, Round Robin
- **Memory Management**: Allocation/deallocation, protection, and efficiency using paging and segmentation
- **File System Management**: File operations, disk scheduling (SSTF, SCAN, C-SCAN), and access control
- **Simple/Monolithic Structure**: Entire OS as single program - efficient but hard to maintain
- **Layered Approach**: OS broken into layers, each using services from layer below - easier debugging but performance overhead
- **Microkernel Structure**: Minimal kernel with non-essential components in user-space - improved modularity and security but increased overhead
- **Modular Kernel**: Hybrid approach with core services plus dynamically loaded modules - balance of performance and modularity

## Important Concepts

- OS acts as resource manager allocating CPU cycles, memory, storage, and I/O devices fairly
- System calls provide programming interface to OS services
- Different structures trade-off between performance, maintainability, and modularity
- Modern OS like Linux and macOS use modular kernel approach

## Notes

- Understand all four resource managers and their responsibilities
- Know characteristics, advantages, and disadvantages of each OS structure
- Be able to compare and contrast different structures (exam favorite)
- Remember examples: Early UNIX (monolithic), QNX (microkernel), Linux/macOS (modular)
