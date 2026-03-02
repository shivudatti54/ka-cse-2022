# Implementing File System - Summary

## Key Definitions and Concepts

- **File System Structure**: The layered architecture consisting of device drivers, basic file system, file organization module, directory management, and access control layers.
- **I-Node (Index Node)**: The fundamental metadata structure in UNIX file systems containing file attributes and pointers to data blocks.
- **Contiguous Allocation**: Assigning consecutive disk blocks to each file for fast sequential access.
- **Linked Allocation**: Storing files as linked lists of disk blocks, eliminating fragmentation.
- **Indexed Allocation**: Using index blocks to store pointers to all file data blocks, enabling random access.
- **Buffer Cache**: Memory region caching frequently accessed disk blocks to reduce I/O operations.
- **Journaling**: Logging metadata changes before applying them to ensure file system consistency after crashes.

## Important Formulas and Theorems

- **Maximum File Size (i-node structure)** = (12 × Block_Size) + (N × Block_Size) + (N² × Block_Size) + (N³ × Block_Size), where N = Block_Size / Pointer_Size (typically 1024 for 4KB blocks with 4-byte pointers)

## Key Points

- File system implementation bridges user file operations and physical disk storage through multiple abstraction layers.
- Directory entries map human-readable filenames to internal i-node numbers used by the operating system.
- Indexed allocation (i-node structure) efficiently supports both small files (through direct pointers) and very large files (through multi-level indirect pointers).
- Free space management using bit vectors enables fast allocation decisions but requires proportional memory.
- In-memory caching is essential for performance but introduces consistency challenges between cached data and on-disk structures.
- Journaling file systems provide crash recovery guarantees by logging operations before committing them.
- External fragmentation occurs in contiguous allocation; internal fragmentation occurs when allocated units contain unused space.

## Common Mistakes to Avoid

- Confusing internal fragmentation with external fragmentation—they are fundamentally different concepts.
- Assuming linked allocation provides efficient random access—it requires sequential traversal.
- Forgetting that directory entries contain only filenames and i-node numbers, not the actual file data.
- Overlooking the overhead of index blocks in indexed allocation for small files.
- Assuming cached data is automatically written to disk—write-back policies vary by implementation.

## Revision Tips

1. Practice tracing through file creation to understand all the steps involved and where disk I/O occurs.
2. Draw the i-node structure with direct and indirect pointers to visualize how file size limits are calculated.
3. Compare allocation methods side-by-side, focusing on the trade-offs between speed, fragmentation, and reliability.
4. Remember that the buffer cache solves performance problems but creates consistency challenges—understand the resolution strategies.
5. Review the relationship between directory structures and i-nodes, as this connection is fundamental to file system operation.