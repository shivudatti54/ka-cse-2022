# File System Implementation

## Overview

File system implementation covers allocation methods (contiguous, linked, indexed), free space management (bitmap, linked list), directory implementation (linear, hash table), and efficiency/performance optimizations (caching, read-ahead, write-behind).

## Key Points

- **Contiguous Allocation**: Files occupy consecutive blocks, fast sequential access, external fragmentation, difficult to grow files
- **Linked Allocation**: Each block contains pointer to next, no external fragmentation, slow random access, pointer overhead
- **Indexed Allocation**: Index block contains pointers to all file blocks, supports random access, index overhead
- **Multilevel Index**: Large files use multiple index levels (inode structure in Unix)
- **Free Space Management**: Bitmap (bit per block), linked list (free blocks linked), grouping, counting
- **Directory Implementation**: Linear list (simple, slow search), hash table (fast search, collisions)
- **Caching**: Buffer cache in memory holds frequently accessed blocks
- **Read-Ahead**: Fetch next blocks before requested, exploits sequential access patterns

## Important Concepts

- Contiguous allocation fast but inflexible, linked flexible but slow random access
- Indexed allocation balances access speed and flexibility, used by most modern file systems
- Bitmap efficient for small disks, linked list for large disks with high contiguity
- Caching dramatically improves performance by avoiding disk I/O

## Notes

- Know allocation method trade-offs: access speed, fragmentation, growth
- Understand inode structure: direct pointers, single/double/triple indirect
- Practice calculating index levels needed for file size
- Remember unified buffer cache serves file data and metadata
