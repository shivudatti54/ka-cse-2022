# Implementation of File System: File System: File Concept

==============================================

### Overview

---

- A file is a collection of related data stored as a single unit in a file system.
- File system provides a way to organize, manage and store files on a computer.

### Key Points

---

- **File Structure**:
  - File header: contains metadata about the file (name, size, permissions, etc.)
  - File data: actual data stored in the file
  - File trailer: contains control information for the file (e.g., file system metadata)

- **File Types**:
  - Fixed-length files
  - Variable-length files
  - Compressed files
  - Encrypted files

- **File Operations**:
  - Create: creates a new file
  - Delete: deletes a file
  - Read: retrieves the contents of a file
  - Write: updates the contents of a file
  - Copy: copies the contents of one file to another
  - Move: relocations the contents of one file to another

- **File Permissions**:
  - Read permission
  - Write permission
  - Execute permission
  - Owner, group, and world permissions

- **File Systems**:
  - File allocation table (FAT)
  - Inode-based file systems
  - Directory-based file systems

- **File System Algorithms**:
  - File allocation algorithms (FAT, inode allocation, etc.)
  - File searching algorithms (indexing, hashing, etc.)

### Important Formulas and Theorems

---

- **Inode allocation formula**:
  - Inode = File ID \* File size
- **File searching formula**:
  - File ID = Hash (File name) \* File size

### Definitions

---

- **File**: a collection of related data stored as a single unit in a file system.
- **File System**: a collection of files and directories that are managed by an operating system.
- **Inode**: a data structure that contains metadata about a file.
