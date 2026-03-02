# File Allocation Methods - Summary

## Key Definitions

- **Contiguous Allocation:** A method where each file occupies a set of consecutive disk blocks
- **External Fragmentation:** Wasted disk space occurring when free blocks are scattered and cannot satisfy large allocation requests
- **Linked Allocation:** A method where each block contains a pointer to the next block in the file
- **File Allocation Table (FAT):** A system-wide table containing pointers for linked allocation, stored at the beginning of a partition
- **Indexed Allocation:** A method using an index block that contains pointers to all data blocks of a file
- **Inode:** In UNIX systems, a data structure containing file metadata and data block pointers

## Important Formulas

- **Contiguous Last Block:** Last block = Starting block + Length - 1
- **Linked Access Time:** Time to access block N = N × (seek + rotational delay + transfer time)
- **Indexed Access Time:** Time = Index block access + Data block access (typically 2 I/O operations)
- **Multi-level Index Pointers:** Pointers per block = Block size / Pointer size (e.g., 4096/4 = 1024 for 4KB block)

## Key Points

1. Contiguous allocation provides the fastest sequential and random access but suffers from external fragmentation requiring periodic compaction.

2. Linked allocation eliminates external fragmentation but cannot support efficient random access and wastes space for pointers.

3. Indexed allocation enables efficient random access but requires additional disk I/O for large files and consumes overhead for index blocks.

4. FAT-based linked allocation is simple but creates a single point of failure and performance bottleneck at the disk's beginning.

5. UNIX inodes use a multi-level indexed structure supporting files up to several terabytes through direct, single, double, and triple indirect pointers.

6. Modern file systems (NTFS, ext4, XFS) use hybrid approaches combining contiguous allocation for small files, indexed allocation for random access, and extent-based allocation for sequential workloads.

7. The choice of allocation method significantly impacts system performance for different access patterns—sequential versus random, read versus write intensive.

## Common Mistakes

1. Confusing external fragmentation with internal fragmentation—contiguous allocation has external, indexed has internal.

2. Assuming linked allocation cannot do random access at all—it can, but very slowly (O(n) complexity).

3. Forgetting that pointer overhead in linked allocation reduces effective storage capacity.

4. Overlooking the fact that multi-level indexed allocation may require multiple disk I/O operations for a single data block access in large files.