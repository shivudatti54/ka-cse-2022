# Module 3: Files and Directories in UNIX System Programming

## Introduction

In UNIX, the philosophy is that "everything is a file." This includes not just text documents and programs, but also hardware devices, directories, and even system information. A deep understanding of how the operating system manages these files and directories is fundamental for system programming. This module covers the core system calls and library functions used to manipulate the file system, allowing you to create, navigate, read, write, and query files and directories from within your C programs.

## Core Concepts and System Calls

### 1. File Descriptors

A **file descriptor** is a small, non-negative integer used by a process to identify an open file. When a process opens a file, the kernel returns a file descriptor, which is then used for all subsequent I/O operations (like `read` and `write`).

- **Standard Descriptors**: Every process is automatically given three open file descriptors:
  - `0` (STDIN_FILENO): Standard Input
  - `1` (STDOUT_FILENO): Standard Output
  - `2` (STDERR_FILENO): Standard Error

### 2. Basic File Operations

- **`open()` and `creat()`**: Used to open or create a file.
  - `open()` returns a file descriptor for the specified pathname.
  - `creat()` is equivalent to `open()` with flags `O_CREAT | O_WRONLY | O_TRUNC`. It's often simpler to just use `open()`.
- **`read()` and `write()`**: Perform unbuffered input and output.
  - `read()` reads data from a file descriptor into a buffer.
  - `write()` writes data from a buffer to a file descriptor.
- **`close()`**: Closes an open file descriptor, freeing it for reuse.

**Example: Copying a File (like `cp`)**
