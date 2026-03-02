# File Concept - Summary

## Key Definitions and Concepts

A FILE is a named collection of related information stored on secondary storage media, treated as a single unit by the operating system. It provides non-volatile, persistent data storage that survives system reboots.

FILE ATTRIBUTES (metadata) include: name (symbolic identifier), identifier (internal numeric tag like inode), type (regular, directory, device), location (pointer to physical storage), size (length in bytes), protection (access permissions), and timestamps (creation, modification, access times).

## Important Formulas and Theorems

File access methods determine how data is retrieved from files:

- SEQUENTIAL ACCESS: Read/write proceeds consecutively from current position, advancing automatically
- DIRECT ACCESS: Files treated as numbered blocks, allowing immediate access via block number
- INDEXED ACCESS: Uses auxiliary index structure to locate data, then direct access for retrieval

## Key Points

Files abstract physical storage complexity, presenting a logical byte-stream interface to users and applications.

Seven primitive file operations form the foundation: CREATE, DELETE, OPEN, CLOSE, READ, WRITE, and SEEK.

File descriptors are process-specific handles returned by OPEN, while inodes are system-wide metadata structures.

Sequential access suits batch processing and tape storage; direct access enables database operations; indexed access optimizes key-based lookups.

File extensions are user-level conventions—the OS treats all files as unstructured byte sequences.

File operations may be buffered for performance, requiring explicit flushing or closing to ensure data reaches disk.

## Common Mistakes to Avoid

Confusing file operations with system calls—open/close manage connections, while read/write transfer data.

Assuming file extensions enforce type restrictions—they are merely naming conventions.

Overlooking the distinction between logical file organization (user view) and physical file organization (storage details).

Forgetting that sequential access can use seek for repositioning, while direct access requires fixed-size blocks.

## Revision Tips

Practice writing C programs that demonstrate all file operations to reinforce theoretical concepts.

Create comparison tables of file access methods, noting advantages, disadvantages, and ideal use cases.

Memorize the complete list of file attributes and understand why each is necessary for file management.

Review how file operations map to system calls in Unix-like operating systems.