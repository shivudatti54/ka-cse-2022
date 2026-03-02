# Operating System Operations

## Overview

Operating System Operations encompass all activities performed by the OS to manage hardware and software resources effectively. These include process management, memory management, file system operations, I/O device management, protection and security, and system monitoring.

## Key Points

- **Process Operations**: Creation (fork), scheduling (CPU allocation), termination (resource release), and IPC (shared memory, message passing)
- **Memory Operations**: Allocation (contiguous/non-contiguous), deallocation (freeing memory), virtual memory (page fault handling, swapping)
- **File Operations**: Create, open, read, write, close, delete files and directories
- **I/O Operations**: Buffering (speed mismatch management), spooling (printer queuing), interrupt handling
- **Dual-Mode Operation**: User Mode (limited privileges) vs Kernel Mode (full privileges), protected by mode bit
- **Protection Mechanisms**: Authentication (password/biometric), authorization (ACL, permissions), encryption
- **Timer Operations**: Prevents infinite loops, implements time-sharing, tracks system time

## Important Concepts

- System calls provide the interface between user programs and kernel services
- Process states: New → Ready → Running → Waiting → Terminated
- IPC mechanisms include shared memory, message passing, pipes, sockets, and signals
- Page fault handling: trap to OS, save state, read page from disk, update page table, resume
- Mode switching occurs via system calls (user→kernel→user) or interrupts

## Notes

- Understand the complete process lifecycle from creation to termination
- Know different IPC mechanisms and when to use each
- Be able to explain dual-mode operation and why it's necessary for system security
- Practice drawing process state diagrams and mode switching sequences
