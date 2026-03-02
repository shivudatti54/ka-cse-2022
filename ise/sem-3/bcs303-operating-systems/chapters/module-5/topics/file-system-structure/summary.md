# File System Structure - Summary

## Key Definitions and Concepts

- **File System**: A collection of algorithms and data structures that manages data storage, organization, access, and retrieval on secondary storage devices

- **Directory**: A special file system object that contains references to other files and directories, creating a hierarchical tree structure

- **Inode**: In Unix-like systems, a data structure that stores metadata and data block pointers for each file

- **Virtual File System (VFS)**: An abstraction layer providing unified interfaces for multiple different file system implementations

## Important Formulas and Theorems

- **Contiguous Allocation**: File stored as consecutive disk blocks; excellent random access but suffers from external fragmentation

- **Linked Allocation**: File stored as linked list of blocks; no external fragmentation but poor random access performance

- **Indexed Allocation**: Uses index block with pointers to all data blocks; efficient for both sequential and random access

- **Bitmap Method**: Each disk block represented by 1 bit; 0 = free, 1 = allocated

## Key Points

- File systems provide essential abstraction between logical file operations and physical storage operations

- The directory hierarchy organizes files in a tree structure starting from the root directory

- Indexed allocation balances performance and storage efficiency, making it popular in modern file systems

- Free space management is critical for preventing storage fragmentation and enabling efficient allocation

- Virtual File Systems enable multiple file system types to coexist on a single operating system

- Path resolution requires traversing the directory hierarchy from root or current directory to locate files

- File allocation method choice significantly impacts system performance based on access patterns

## Common Mistakes to Avoid

- Confusing file allocation methods with file organization methods—they are related but distinct concepts

- Assuming contiguous allocation is always bad—it excels for sequential access workloads

- Forgetting that directories themselves are files with special properties and permissions

- Overlooking the memory overhead of bitmaps when managing large disk spaces

## Revision Tips

- Draw diagram of directory tree structures to visualize hierarchical organization

- Create comparison tables for allocation methods covering access time, fragmentation, and efficiency

- Practice tracing file path resolution step-by-step through directory hierarchies

- Review how modern file systems (NTFS, ext4, APFS) implement these concepts in practice