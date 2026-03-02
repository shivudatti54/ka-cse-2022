# File System Implementation - Summary

## Key Definitions

- **File System**: The part of the operating system responsible for storing, retrieving, and managing files on secondary storage devices.

- **Inode**: In Unix-like systems, a data structure that stores metadata about a file including permissions, timestamps, size, and pointers to data blocks.

- **External Fragmentation**: Waste of storage space that occurs when free disk blocks are scattered throughout the disk, preventing allocation of large contiguous regions.

- **Free Block List**: A data structure maintained by the operating system to track which disk blocks are available for allocation.

- **Disk Cache**: A portion of main memory used to store frequently accessed disk blocks, reducing physical I/O operations.

- **Mount Point**: A directory in the existing file system hierarchy where a new file system is attached.

## Important Formulas

- **Maximum file size with single-level indexed allocation**: Block size × (Pointers per block)
- **Disk arm movement (SCAN)**: Sum of absolute differences between consecutive head positions
- **Average seek time**: Total movement / Number of seeks
- **Effective access time**: Cache hit rate × Cache access time + (1 - Cache hit rate) × Disk access time

## Key Points

1. File system implementation uses a layered architecture separating user interface, logical file system, file organization module, access methods, and physical file system.

2. Directory implementations range from simple linear lists to sophisticated B-tree structures, with choice impacting lookup performance significantly.

3. Contiguous allocation provides excellent sequential access but suffers from external fragmentation and difficulties in file expansion.

4. Linked allocation eliminates external fragmentation but performs poorly for random access due to sequential block traversal requirements.

5. Indexed allocation supports efficient random access while eliminating external fragmentation, though it requires additional disk I/O for index blocks.

6. Free space management techniques trade off between storage overhead (bit vectors) and allocation speed (grouping and counting methods).

7. SCAN and C-SCAN algorithms significantly reduce disk arm movement compared to FCFS, with SCAN providing better overall throughput.

8. File system mounting integrates multiple file systems into a unified directory hierarchy, enabling support for diverse storage devices.

9. Modern file systems use journaling to ensure consistency and enable fast recovery after system crashes.

10. Buffer caching dramatically improves performance by keeping frequently accessed data in memory, reducing physical disk operations.

## Common Mistakes

1. Confusing internal and external fragmentation: Internal fragmentation occurs within allocated blocks due to block sizing, while external fragmentation occurs in free space between allocated blocks.

2. Believing linked allocation supports direct access: Linked allocation requires sequential traversal of pointers, making random access O(n) rather than O(1).

3. Assuming larger cache always improves performance: Excessive cache size can increase memory pressure on running processes and delay garbage collection of stale blocks.

4. Forgetting that disk scheduling operates on cylinder numbers, not block numbers, and that rotational positioning affects actual access time.

5. Overlooking the fact that mount points must be directories and that mounting overwrites the directory's visibility until unmounting occurs.