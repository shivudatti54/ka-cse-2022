# Storage Management - Summary

## Key Definitions and Concepts

- STORAGE MANAGEMENT: The OS function responsible for organizing, controlling, and maintaining data on secondary storage devices through file system implementation.

- FILE SYSTEM: The component of the OS that provides the interface for storing, organizing, and accessing files on secondary storage.

- INODE: The data structure in UNIX-based that stores metadata systems about a file, including pointers to data blocks.

- EXTERNAL FRAGMENTATION: The situation where free disk space is fragmented into small non-contiguous chunks, making it difficult to allocate contiguous space for large files.

- DISK SCHEDULING: The process of determining the order in which pending I/O requests are serviced to optimize disk throughput and response time.

## Important Formulas and Theorems

- SEEK TIME CALCULATION: Seek time = |current track - target track| × time per track movement

- CONTIGUOUS ALLOCATION: File of n bytes requires ceil(n/block_size) blocks of contiguous space

- LINKED ALLOCATION: Effective data per block = block_size - pointer_size

- INDEXED ALLOCATION: Supports efficient random access through index block pointers; typically uses multi-level indexing (direct, single indirect, double indirect, triple indirect)

- BITMAP STORAGE: One bit per block; bitmap size = number of blocks / 8 bytes

## Key Points

- The file system provides an abstraction layer that transforms physical storage into logical files and directories, hiding hardware complexities from users and applications.

- CONTIGUOUS ALLOCATION offers excellent sequential access but suffers from external fragmentation requiring periodic compaction.

- LINKED ALLOCATION eliminates external fragmentation but provides poor random access performance and loses space to pointers.

- INDEXED ALLOCATION combines benefits of both methods using index blocks, though it adds overhead for small files.

- FREE SPACE BITMAPS provide efficient tracking of available storage through compact bit representations.

- FCFS is fair but inefficient; SSTF minimizes seek time but may cause starvation; SCAN and C-SCAN provide better overall performance with reduced starvation.

- Directory implementations range from simple linear lists to hash tables and B-trees, affecting search performance for large directories.

- Modern file systems like NTFS and ext4 use variations of indexed allocation with advanced features like journaling for crash recovery.

## Common Mistakes to Avoid

- Confusing internal and external fragmentation: internal fragmentation occurs within allocated units due to block rounding; external fragmentation occurs in free space between allocated files.

- Forgetting that linked allocation pointers occupy space within data blocks, reducing effective storage capacity.

- Assuming SSTF always provides optimal performance: while generally better than FCFS, it can perform poorly when request distribution is skewed.

- Ignoring the fact that C-SCAN provides uniform response times by treating all tracks equally, while SCAN favors tracks in the middle of the disk.

## Revision Tips

- Practice numerical problems on disk scheduling by writing out each head movement step-by-step and calculating cumulative seek time.

- Create comparison tables for file allocation methods, listing advantages, disadvantages, and suitable use cases for each method.

- Understand the trade-offs between different free space management techniques rather than memorizing which is "best" — the optimal choice depends on the specific system requirements.

- Review real file systems (FAT, NTFS, ext4) to see how theoretical concepts are implemented in practice.