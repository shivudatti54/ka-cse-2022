# File System Structure

### Overview

- A file system is a hierarchical organization of files and directories on a storage device.

### Key Components

- **Root Directory**: The topmost directory in the file system hierarchy.
- **Inode**: A data structure that contains metadata for a file or directory.
- **Block**: A fixed-size area of storage used to hold a file's data.
- **File System Tree**: A hierarchical representation of the file system.

### File System Structure Types

- **Simple File System**: Uses a single block per file.
- **Linked File System**: Uses a pointer to another block to store a file.

### File System Organization

- **Block Allocation**: Allocating blocks to files.
- **File Allocation Table (FAT)**: A table that maps file IDs to block locations.
- **Directory Allocation Table (DAT)**: A table that maps directory entries to block locations.

### Important Formulas and Definitions

- **File Size Formula**: `File Size = (Number of Blocks * Block Size)`
- **Directory Entry Formula**: `Directory Entry = (File ID + Offset)`

### Theorems

- **Directory Traversal Theorem**: A file system traversal is valid if it is possible to traverse the directory structure without encountering a cycle.
- **Inode Validation Theorem**: An inode is valid if it is possible to recover the file data from the corresponding block locations.

### Important Concepts

- **File System Permissions**: Access control mechanisms for files and directories.
- **File System Quotas**: Limits on file size, space usage, and other file system attributes.
- **File System Backup**: The process of creating a copy of the file system for recovery purposes.
