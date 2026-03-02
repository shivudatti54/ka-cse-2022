# Implementing File System - Summary

## Key Definitions and Concepts

- **File System**: The part of the operating system responsible for file storage, retrieval, update, and protection on secondary storage devices
- **Inode**: In Unix-like systems, a data structure that stores metadata about a file including permissions, timestamps, and pointers to data blocks
- **Allocation Method**: The technique used to assign disk blocks to files (contiguous, linked, or indexed)
- **Free Space Management**: Methods to track available disk blocks including bit vectors, linked lists, and counting
- **Directory**: A special file that maps file names to internal identifiers and provides organizational structure

## Important Formulas and Theorems

- **Maximum file size with indexed allocation**: Sum of (pointers × block size) for all pointer types
- **Number of blocks required**: ceil(file_size / block_size)
- **Block pointer calculation**: block_number = floor(byte_offset / block_size)
- **Bit vector size**: Equal to number of disk blocks (1 bit per block)
- **Inode pointers**: 10 direct + 1 single indirect + 1 double indirect + 1 triple indirect (typical Unix)

## Key Points

- File systems use layered architecture separating logical file system from physical file system operations
- Directory implementation options include linear lists (O(n) search), hash tables (O(1) average), and variable-length entries
- Contiguous allocation provides excellent sequential access but suffers from external fragmentation
- Linked allocation eliminates external fragmentation but has poor random access performance
- Indexed allocation combines good random access with no external fragmentation but has index block overhead
- Bit vector free space management provides O(1) allocation but requires significant memory for large disks
- Unix inodes use multi-level indirect pointers to support both small and very large files efficiently
- File system mounting integrates multiple file systems into a unified directory hierarchy

## Common Mistakes to Avoid

- Confusing contiguous allocation with sequential allocation - contiguous can support both sequential and random access efficiently
- Forgetting that linked allocation pointers consume space within each data block
- Not considering that block size affects both internal fragmentation and number of disk accesses
- Overlooking the fact that inode numbers, not file names, uniquely identify files within a file system
- Assuming larger block sizes always improve performance - they may increase internal fragmentation

## Revision Tips

- Practice drawing and analyzing inode structures with different file sizes
- Solve numerical problems involving disk access calculations for all three allocation methods
- Create comparison tables for allocation methods and free space management techniques
- Understand how the superblock, inode table, and data blocks are organized on disk
- Review the trade-offs between performance, storage efficiency, and implementation complexity