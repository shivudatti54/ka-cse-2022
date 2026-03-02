# **UNIX SYSTEM PROGRAMMING Revision Notes - Chapter 10**

## **Table of Contents**

- [Overview](#overview)
- [Key Concepts](#key-concepts)
- [Important Formulas and Definitions](#important-formulas-and-definitions)
- [Theorems](#theorems)

## **Overview**

- Chapter 10 of UNIX System Programming focuses on the UNIX operating system's boot process, process management, and memory management.

## **Key Concepts**

- Boot process: System initialization, boot loader, kernel loading, and system startup.
- Process management: Process creation, process scheduling, process synchronization, and process termination.
- Memory management: Memory allocation, memory protection, and memory deallocation.

## **Important Formulas and Definitions**

- **Boot process:**
  - Boot loader: loads the kernel into memory.
  - Kernel: the core system software that manages the system hardware.
- **Process management:**
  - Process creation: `fork()` and `exec()`.
  - Process scheduling: round-robin scheduling, priority scheduling, and multi-threading.
- **Memory management:**
  - Memory allocation: `malloc()`, `calloc()`, and `realloc()`.
  - Memory protection: page tables, segmentation, and virtual memory.

## **Theorems**

- **Theorem 1:** A process can create at most 20 child processes.
- **Theorem 2:** A process can allocate a maximum of 4GB of virtual memory.

## **Key Unix Commands**

- `fork()`: creates a new process.
- `exec()`: replaces the current process image with a new one.
- `malloc()`: allocates memory for a process.
- `free()`: deallocates memory for a process.
- `pipe()`: creates a pipe for inter-process communication.

## **Revision Tips**

- Review the boot process and kernel loading.
- Focus on process creation, scheduling, and synchronization.
- Understand memory allocation, protection, and deallocation.
