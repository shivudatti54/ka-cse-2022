# System Programs & OS Structure

## Introduction

System programs (system software) form the critical interface between computer hardware and user applications. The operating system (OS) provides the foundation for this interaction, managing hardware resources while providing services to application programs. Understanding OS structure is essential for comprehending how modern computer systems function efficiently.

---

## Key Concepts

### System Programs

- **Definition**: Software that provides platform for running application programs
- **Types of System Programs**:
  - **Language Translators**: Assemblers, compilers, interpreters
  - **Utility Programs**: File management, disk formatting, backup tools
  - **Device Drivers**: Interface between OS and hardware peripherals
  - **System Management Programs**: Task managers, performance monitors
  - **Command Interpreters**: Shell programs (Bash, Command Prompt)

### Operating System Structure

- **Main Functions**:
  - Process Management (scheduling, creation, termination)
  - Memory Management (allocation, deallocation, virtual memory)
  - File Management (organization, access, protection)
  - Device Management (I/O scheduling, buffering)
  - Security & Protection (user authentication, access control)

### OS Architecture Models

- **Simple/Monolithic Structure**: Single kernel with all functions (early UNIX)
- **Layered Structure**: Hierarchical layers with defined interfaces
  - Hardware → Kernel → System Programs → User Programs → Users
- **Microkernel Architecture**: Minimal kernel with user-space servers (Mach, MINIX)
- **Client-Server Model**: Distributed computing approach
- **Modular/Object-Oriented**: Loadable kernel modules (Linux, Windows NT)

### System Calls & API

- **System Calls**: Interface between user programs and OS kernel
  - Process control (fork, exec, wait)
  - File management (open, read, write, close)
  - Device communication (read, write, ioctl)
  - Information maintenance (getpid, getuid)
  - Communication (pipe, socket)
- **POSIX API**: Standard portable interface for UNIX systems

### Boot Process

- **BIOS/UEFI** → Bootloader → Kernel Loading → Init Process → Runlevel/Services

---

## Conclusion

System programs and OS structure form the backbone of computer system functionality. The layered architecture ensures modularity, while system calls provide controlled access to hardware resources. For exams, focus on understanding the different OS architectures, system call categories, and the role of system programs in resource management and providing user interfaces.