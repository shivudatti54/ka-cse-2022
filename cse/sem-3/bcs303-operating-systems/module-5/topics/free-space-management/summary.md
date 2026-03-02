# Free Space Management - Summary

## Key Definitions

- **Free Space Management**: The technique of tracking available disk blocks and allocating them to files while reclaiming space from deleted files.

- **Bit Vector (Bitmap)**: A data structure where each disk block is represented by one bit; 0 indicates free, 1 indicates allocated.

- **Linked List (Free List)**: A method where each free block contains a pointer to the next free block, forming a chain of available space.

- **Grouping**: An enhancement to linked lists where the first free block stores addresses of multiple other free blocks.

- **Counting**: A technique that maintains a table of starting block addresses and counts of consecutive free blocks.

## Important Formulas

- **Bit Vector Size**: For a disk with N blocks, bitmap requires N bits of storage.

- **Memory for Bitmap**: Memory = (Disk Size / Block Size) / 8 bytes

- **Example**: 1 TB disk with 4 KB blocks = (1,099,511,627,776 / 4096) / 8 ≈ 32 MB

## Key Points

1. Free space management tracks which disk blocks are available for file allocation.

2. Bit vectors provide O(1) access to block status but require proportional memory (1 bit per block).

3. Linked lists minimize overhead (1 pointer per free block) but suffer from poor locality and sequential access performance.

4. Grouping combines advantages of bit vectors and linked lists by storing multiple free block addresses.

5. Counting is most efficient when free space exists in large contiguous regions.

6. The choice of free space management affects fragmentation, allocation speed, and memory overhead.

7. Modern file systems often use hybrid approaches combining multiple techniques.

## Common Mistakes

1. Confusing bit values (remember: 0 = free, 1 = allocated in many implementations, but verify the convention used).

2. Forgetting that the free space management data structure itself requires disk space.

3. Not considering the disk I/O cost when evaluating free space management methods.

4. Assuming one method is universally best; the optimal choice depends on specific use cases and constraints.