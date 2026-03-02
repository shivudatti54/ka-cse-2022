# Allocation Methods - Summary

## Key Definitions and Concepts

- CONTIGUOUS ALLOCATION: Each file occupies a single continuous set of disk blocks; directory stores starting block and length.

- LINKED ALLOCATION: File stored as linked list of blocks; each block contains pointer to next block; directory stores only first block pointer.

- INDEXED ALLOCATION: Uses an index block containing pointers to all file blocks; directory stores pointer to index block.

- EXTERNAL FRAGMENTATION: Free disk space divided into non-contiguous chunks; occurs in contiguous allocation.

- INTERNAL FRAGMENTATION: Wasted space within allocated blocks due to fixed block sizes; occurs in indexed allocation.

## Important Formulas and Theorems

- External Fragmentation Condition: Fragmentation exists when total free space > largest contiguous free block, yet no single free block can accommodate a new file.

- Indexed Allocation Maximum File Size: For single-level with b bytes per block and pointer size p: Maximum blocks = b/p, Maximum file size = (b/p) × b

- Two-level Indexed Maximum: Maximum file size = (b/p) × (b/p) × b

## Key Points

- Contiguous allocation offers FASTEST ACCESS but suffers from external fragmentation and difficulty in file growth.

- Linked allocation ELIMINATES FRAGMENTATION but has poor random access performance (O(n) for n-th block).

- Indexed allocation provides efficient RANDOM ACCESS (O(1) after index in memory) but wastes space for small files.

- First-fit is FAST but creates fragmentation; best-fit MINIMIZES WASTE but is slower; worst-fit creates larger remaining spaces.

- FAT file systems use LINKED ALLOCATION with centralized table allowing caching in memory.

- UNIX inode uses HYBRID approach with direct pointers (for speed) and indirect pointers (for large files).

- Index block overhead makes indexed allocation inefficient for very small files relative to block size.

## Common Mistakes to Avoid

Confusing external and internal fragmentation: external is free space too scattered; internal is allocated space not fully used.

Assuming linked allocation has no overhead: each block loses space for the pointer (typically 4 bytes).

Forgetting that indexed allocation requires TWO I/O operations minimum: one for index block, one for data block.

Ignoring the impact of caching: FAT and index blocks cached in memory dramatically improve practical performance.

## Revision Tips

MEMORIZE THE COMPARISON: Contiguous = fast but fragmented; Linked = no fragmentation but slow random; Indexed = balanced but overhead.

Remember that linked allocation stores pointers WITHIN data blocks, while indexed allocation uses a SEPARATE INDEX BLOCK.

Practice calculating maximum file sizes for different allocation methods using block size and pointer size.

Visualize how each method handles file extension: contiguous requires MOVING the file; linked and indexed can EXTEND in place.