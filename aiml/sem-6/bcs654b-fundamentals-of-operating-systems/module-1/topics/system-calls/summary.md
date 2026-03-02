# System Calls

## Overview

A system call is a programmed request to the operating system kernel to perform a privileged task on behalf of a calling process. System calls are the fundamental interface between user applications and the OS kernel, enabling secure transition from user mode to kernel mode.

## Key Points

- **Definition**: Only entry points into the kernel, implemented as software interrupts (trap mechanism)
- **System Call Process**: Invocation → Preparation → Trap (mode switch) → Execution → Return
- **Categories**: Process Control (fork, exec), File Management (open, read, write), Device Management (ioctl), Information Maintenance (getpid), Communication (pipe, shmget), Protection (chmod)
- **Dual-Mode Operation**: User Mode (restricted) vs Kernel Mode (privileged), system calls bridge the gap
- **Trap Mechanism**: Software interrupt triggers hardware-assisted switch from user to kernel mode
- **API vs System Call**: API defines interface (the "what"), System Call implements it (the "how")

## Important Concepts

- Each system call has unique number identifier stored in register (e.g., eax)
- System call mechanism ensures security by preventing direct hardware access
- API functions may wrap one or multiple system calls or no system calls
- Examples: printf() API uses write() system call, fork() creates new process

## Notes

- Understand step-by-step system call process: library function → trap instruction → kernel handler → return
- Memorize main categories with 2-3 examples each for exam
- Know the difference: API is contract, system call is implementation
- Link system calls to dual-mode operation - this is why they exist
