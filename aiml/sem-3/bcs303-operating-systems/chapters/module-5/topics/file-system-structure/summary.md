# File System Structure - Summary

## Key Definitions and Concepts

- **File System Structure**: The organizational layout of files and directories on secondary storage, defining how data is stored, accessed, and managed

- **Hierarchical Directory Structure**: Tree-like organization with root directory at the top and subdirectories branching below, enabling logical file grouping

- **Inode (Index Node)**: Data structure in Unix-like systems containing file metadata (permissions, ownership, timestamps, block pointers) except the filename

- **Contiguous Allocation**: File storage method assigning consecutive disk blocks to each file

- **Linked Allocation**: File storage method where blocks are scattered with pointers connecting them in a chain

- **Indexed Allocation**: File storage method using an index block to store pointers to all file data blocks

- **Virtual File System (VFS)**: Abstraction layer providing a standard interface for multiple file system types to coexist

- **Boot Block**: First disk sector containing bootstrap code for system initialization

- **Superblock**: File system metadata structure containing information about total blocks, free space, block size, and filesystem state

## Important Formulas and Theorems

- Maximum file size with inode pointers = 12×(block size) + 1×(block size)² + 1×(block size)³ + 1×(block size)⁴

- External fragmentation occurs in contiguous allocation but not in linked or indexed allocation

- Random access time: Contiguous O(1), Linked O(n), Indexed O(1)

- Directory search complexity: Linear list O(n), Hash table O(1) average, B-tree O(log n)

## Key Points

- File systems abstract physical storage details, providing logical file operations to users and applications

- The hierarchical directory model is the dominant organizational structure in modern operating systems

- Directories map human-readable filenames to internal identifiers (inode numbers or FAT entries)

- Each allocation method represents a different trade-off between access speed, storage efficiency, and implementation complexity

- Inodes separate file metadata from data storage, enabling efficient attribute management

- Modern file systems maintain multiple superblock copies for reliability and recovery

- VFS enables operating systems to support diverse file system types simultaneously through a unified API

- Path resolution involves traversing the directory tree from root (or current directory) to locate files

## Common Mistakes to Avoid

- Confusing logical file organization (directories visible to users) with physical file storage (how blocks are arranged on disk)

- Incorrectly stating that linked allocation supports efficient random access—it does not, as blocks must be traversed sequentially

- Mixing up boot block and superblock functions—they serve completely different purposes in system operation

- Assuming all file systems use inodes—Windows NTFS uses Master File Table (MFT), FAT uses file allocation table

- Forgetting that directories themselves are files containing metadata, not just organizational containers

## Revision Tips

- Practice drawing the inode structure diagram with all pointer types and their addressing capacities

- Create comparison tables for allocation methods covering fragmentation, access time, and use cases

- Trace through path resolution examples to understand how absolute and relative paths work

- Review how VFS handles multiple file system types by implementing a common interface

- Understand the relationship between directory entries, inodes, and data blocks through concrete examples