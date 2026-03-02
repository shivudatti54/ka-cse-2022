# Module 3: Files and Directories in UNIX System Programming

## Introduction

In UNIX and Linux, everything is treated as a file—a principle that simplifies many system operations. This includes not just regular data files, but also directories, devices, pipes, and sockets. Understanding how the system manages these files and directories is fundamental for system programming. This module covers the core system calls and library functions used to manipulate the file system's metadata and structure, enabling you to build tools that can navigate, inspect, and modify the file system programmatically.

## Core Concepts and System Calls

### 1. The UNIX File System Structure

The file system is organized in a hierarchical, tree-like structure starting from the root directory (`/`). Each file and directory is identified by a unique **pathname**. An **inode** (index node) is a critical data structure on disk that stores all metadata about a file (like permissions, ownership, size, timestamps) except its name. The directory entry simply maps a filename to its inode number.

### 2. File Metadata: The `stat` Family of Functions

The metadata of a file is accessed using the `stat()`, `fstat()`, and `lstat()` system calls. They populate a `struct stat` with information about the file.

*   `int stat(const char *pathname, struct stat *statbuf);`
    *   Gets information about the file specified by `pathname`.
*   `int lstat(const char *pathname, struct stat *statbuf);`
    *   Similar to `stat`, but if the path is a symbolic link, it returns information about the link itself, not the file it points to.
*   `int fstat(int fd, struct stat *statbuf);`
    *   Gets information about a file using an open file descriptor `fd`.

**Example: Displaying File Size**