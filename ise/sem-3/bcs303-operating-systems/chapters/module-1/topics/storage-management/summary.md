# Storage Management - Summary

## Key Definitions and Concepts

- STORAGE HIERARCHY: The organization of storage devices in levels based on speed, cost, and capacity, from fastest (CPU registers) to slowest but largest (magnetic tapes/cloud storage).
- DISK SCHEDULING: The process of determining the order in which disk I/O requests are serviced to minimize seek time and improve throughput.
- FILE SYSTEM: The OS mechanism for storing and organizing data on secondary storage, providing files, directories, and access control.
- CONTIGUOUS ALLOCATION: Method where each file occupies consecutive disk blocks, enabling fast sequential access but causing external fragmentation.
- LINKED ALLOCATION: Method where file blocks are linked via pointers, allowing non-contiguous storage but poor random access performance.
- INDEXED ALLOCATION: Method using an index block to store pointers to all file blocks, enabling direct access at the cost of additional index overhead.
- FREE SPACE MANAGEMENT: Techniques for tracking available storage blocks, including bit vectors, linked lists, and grouping methods.

## Important Formulas and Theorems

- AVERAGE SEEK TIME = (sum of all seek distances) / number of seeks
- DISK ACCESS TIME = seek time + rotational delay + transfer time
- ROTATIONAL DELAY = (1/2) × (rotation time per revolution)
- BLOCKS REQUIRED = ceil(file size / block size)
- BIT VECTOR SIZE = number of disk blocks / (bits per word × words per block)

## Key Points

- THE THREE MAJOR DISK SCHEDULING ALGORITHMS ARE FCFS (simplest but slowest), SSTF (optimal seek time but starvation possible), AND SCAN (fair and consistent performance).
- SEEK TIME DOMINATES DISK ACCESS TIME, making seek minimization the primary goal of disk scheduling.
- CONTIGUOUS ALLOCATION PROVIDES FASTEST ACCESS but suffers from external fragmentation and difficulty in file growth.
- INDEXED ALLOCATION IS USED IN UNIX INODES and provides good performance for both sequential and random access.
- BIT VECTORS ENABLE FAST ALLOCATION but require additional storage space proportional to disk size.
- CACHING AND BUFFERING are essential techniques that bridge the speed gap between fast main memory and slower secondary storage.
- MODERN FILE SYSTEMS LIKE NTFS AND EXT4 use journaling to ensure file system consistency after crashes.

## Common Mistakes to Avoid

- CONFUSING ROTATIONAL DELAY WITH SEEK TIME: Remember that seek time (head movement) typically dominates disk access time.
- FORGETTING THAT SCAN AND C-SCAN DIFFER: SCAN services in both directions while C-SCAN only services in one direction and returns quickly to the beginning.
- IGNORING EXTERNAL FRAGMENTATION: Contiguous allocation creates holes that cannot be used for larger files even when total free space exceeds file size.
- OVERLOOKING THE COST OF INDEX BLOCKS: Indexed allocation requires an extra I/O operation to read the index block before accessing file data.

## Revision Tips

- PRACTICE DISK SCHEDULING CALCULATIONS by working through numerical examples with different request sequences and initial head positions.
- CREATE A COMPARISON TABLE for allocation methods covering access time, space overhead, fragmentation, and file growth support.
- MEMORIZE THE DISK SCHEDULING ALGORITHMS using mnemonics: FCFS (First Come First Served), SSTF (Shortest Seek Time First), SCAN (like an elevator).
- UNDERSTAND THE RELATIONSHIP between storage management and virtual memory since these topics frequently appear together in exams.
- REVISE PREVIOUS YEAR EXAM QUESTIONS as disk scheduling and allocation methods are frequently tested topics with standard solution approaches.