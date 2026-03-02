# File System Implementation - Summary

## Key Definitions and Concepts

- File System: The component of an operating system that provides persistent storage and organized access to files, abstracting physical storage details.

- Inode: The data structure in UNIX file systems that stores metadata about a file including permissions, timestamps, size, and pointers to data blocks.

- External Fragmentation: The phenomenon where free disk space becomes divided into small non-contiguous pieces, preventing allocation of large files.

- Internal Fragmentation: Wasted space within allocated blocks due to rounding up of file sizes to block boundaries.

- Mount Point: A directory in one file system onto which another file system is attached, creating a unified namespace.

## Important Formulas and Theorems

- Maximum file size with multi-level index: For an inode with D direct blocks, single indirect pointers (S), double indirect pointers (D2), and block size B with pointers of size P, maximum file size = (D + S + D2) × B. With triple indirect, add D3 × B² terms.

- Bit vector size: For a disk with n blocks, bit vector requires n bits (n/8 bytes), making it highly space-efficient.

- Block pointers per index block: With block size B and pointer size P, each index block can hold B/P pointers.

## Key Points

- File systems use a layered architecture with distinct responsibilities at each level: device drivers, basic file system, file organization module, logical file system, and application interface.

- Contiguous allocation provides excellent sequential access but suffers from external fragmentation and difficulty in file expansion.

- Linked allocation eliminates external fragmentation but prevents random access and has reliability concerns if pointers are damaged.

- Indexed allocation supports both sequential and random access efficiently, though it has overhead for small files and complex structures for very large files.

- Directory implementation evolved from simple linear lists to hash tables and B+ trees for handling millions of files efficiently.

- Free space management using bit vectors allows quick allocation decisions but requires significant memory for large disks.

- UNIX inodes use a hybrid approach with direct, single indirect, double indirect, and triple indirect pointers to efficiently handle files of all sizes.

- File system mounting allows multiple partitions and devices to appear as a single coherent directory tree.

## Common Mistakes to Avoid

- Confusing internal and external fragmentation: Internal is wasted space within allocated blocks; external is scattered free space that cannot be used.

- Assuming linked allocation allows efficient random access—it requires sequential traversal of all preceding blocks.

- Forgetting that directory entries typically store only names and inode numbers, not the actual file data.

- Overlooking the fact that bit vectors must be cached in memory for performance, requiring careful synchronization with disk state.

- Not considering that file system metadata itself requires storage space, reducing usable capacity.

## Revision Tips

- Practice calculating maximum file sizes for different inode configurations—these problems appear frequently in examinations.

- Draw diagrams of the three allocation methods to visualize how blocks are linked and accessed.

- Create a comparison table of allocation methods listing advantages, disadvantages, and best use cases.

- Understand the complete path lookup process from root to target file, as this integrates multiple concepts.

- Review past University of Delhi examination papers to identify the question patterns and important topics.