# File System - Summary

## Key Definitions and Concepts

FILE: A named collection of related information stored on secondary storage, providing logical data storage abstraction.

FILE SYSTEM: The operating system component that provides file management services including creation, deletion, organization, and access control.

INODE: The fundamental data structure in UNIX-like file systems that stores file metadata and pointers to data blocks.

DIRECTORY: A special file type that contains entries mapping filenames to their corresponding inode numbers.

## Important Formulas and Theorems

- Block offset calculation: Byte offset = (block_number - 1) × block_size
- Direct access time: O(1) constant time for any block when using indexed allocation
- Sequential access: File pointer automatically advances after each read/write operation
- Contiguous allocation: Best performance but suffers from external fragmentation

## Key Points

- File systems provide abstraction between logical file operations and physical disk storage
- File attributes include name, identifier, type, location, size, protection, and timestamps
- Three primary access methods: sequential, direct (random), and indexed access
- File system structure consists of boot block, superblock, inode table, and data blocks
- Hierarchical directory structure is the most widely used organization in modern OS
- Indexed allocation combines the advantages of both contiguous and linked allocation
- The superblock contains critical metadata about the file system including free space information

## Common Mistakes to Avoid

- Confusing sequential access with direct access: sequential uses a moving file pointer while direct allows random positioning
- Believing that linked allocation provides efficient random access: it requires traversing all pointers from the beginning
- Ignoring the importance of the superblock: it contains essential file system metadata
- Forgetting that directories themselves are files with special handling by the operating system

## Revision Tips

- Draw the file system structure diagram showing boot block, superblock, inode table, and data blocks
- Compare allocation methods using a table showing advantages, disadvantages, and use cases
- Practice calculating disk access times for different allocation and access method combinations
- Review real-world file systems like FAT, NTFS, and ext4 to understand how theoretical concepts are implemented