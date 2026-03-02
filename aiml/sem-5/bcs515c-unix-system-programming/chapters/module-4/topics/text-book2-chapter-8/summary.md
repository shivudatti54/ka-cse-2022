# **UNIX SYSTEM PROGRAMMING: Process Control - Chapter 8 Summary**

### Introduction

- Process control in UNIX is the mechanism for controlling process behavior.
- Processes can be created, identified, and terminated.

### Key Concepts

- **Process Identifier (PID)**:
  - Unique identifier for each process.
  - Used to identify a process.
  - Process ID 0 represents the init process.
- **fork()**:
  - System call to create a new process.
  - Creates a copy of the current process.
  - Returns the PID of the new process.
- **vfork()**:
  - Similar to fork(), but also copies the parent process's memory.
  - Used when parent and child processes need to access the same memory.
- **exit()**:
  - System call to terminate a process.
  - Returns the exit status of the process.
- **wait()**:
  - System call to wait for a child process to terminate.
  - Returns the exit status of the child process.
- **waitpid()**:
  - Similar to wait(), but allows specifying the PID of the child process to wait for.
  - Returns the exit status of the child process.
- **wait3()**:
  - Similar to waitpid(), but also provides an option to specify a signal to kill the child process if it does not terminate normally.

### Important Formulas and Definitions

- **Process Creation**: `fork()` system call.
- **Process Termination**: `exit()` system call.
- **Process Waiting**: `wait()`, `waitpid()`, `wait3()` system calls.

### Theorems

- **Theorem 8.1**: `fork()` system call returns the PID of the new process.
- **Theorem 8.2**: `wait()` system call returns the exit status of the child process.

### Quick Revision Tips

- Understand the difference between `fork()` and `vfork()`.
- Know when to use `exit()`, `wait()`, `waitpid()`, and `wait3()` system calls.
- Practice using these system calls to create, identify, and terminate processes.
