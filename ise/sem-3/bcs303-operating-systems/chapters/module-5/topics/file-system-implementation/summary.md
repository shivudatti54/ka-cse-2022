# File System Implementation - Summary

## Key Definitions and Concepts

- FILE SYSTEM IMPLEMENTATION: The internal mechanisms by which operating systems organize, store, and retrieve data on secondary storage devices.

- LAYERED FILE SYSTEM ARCHITECTURE: Device driver → Basic file system → File organization module → Logical file system → Access control module.

- DIRECTORY IMPLEMENTATION: Techniques for storing and searching file name mappings, including linear lists (O(n) lookup) and hash tables (O(1) average lookup).

## Important Formulas and Theorems

- CONTIGUOUS ALLOCATION: Block location = starting_block + (offset / block_size)

- INDEXED ALLOCATION MAXIMUM FILE SIZE: Sum of (pointers × block_size) for all pointer levels in the inode structure.

- BIT VECTOR SPACE REQUIREMENT: One bit per disk block.

## Key Points

- CONTIGUOUS ALLOCATION provides excellent sequential access performance but suffers from external fragmentation and difficulty in file extension.

- LINKED ALLOCATION eliminates external fragmentation but has poor random access performance and loses space to block pointers.

- INDEXED ALLOCATION, used in Unix/Linux file systems (ext2, ext3, ext4), combines efficient random access with reasonable file size support through multi-level index blocks.

- INODES typically contain 12 direct pointers, single indirect, double indirect, and triple indirect pointers to support files ranging from a few KB to several GB.

- FREE SPACE MANAGEMENT techniques include bit vectors (fast allocation, higher memory usage), linked lists (low overhead, slower allocation), grouping, and counting.

- THE FAT FILE SYSTEM implements linked allocation with a central allocation table, storing one entry per disk block.

- INTERNAL FRAGMENTATION occurs when allocated blocks are larger than needed; external fragmentation occurs when free space becomes non-contiguous.

## Common Mistakes to Confuse

- Do not confuse internal fragmentation (wasted space within allocated blocks) with external fragmentation (free space that cannot be used due to being non-contiguous).

- Do not mistake contiguous allocation for indexed allocation—contiguous stores data in consecutive blocks; indexed uses an index block as an intermediary.

- Remember that hash tables provide only AVERAGE O(1) lookup time; worst-case can be O(n) with many collisions.

## Revision Tips

- Practice drawing diagrams showing how files appear on disk under each allocation method.

- Memorize the comparison table of allocation methods: contiguous vs. linked vs. indexed.

- Understand why modern file systems use indexed allocation as the default approach.

- Review the inode structure and calculate example maximum file sizes for different pointer configurations.