# File System Structure

## Introduction

File system structure refers to the internal organization and architecture of how operating systems store, retrieve, and manage data on secondary storage devices. The file system serves as an abstraction layer between user applications and physical disk hardware, providing a logical view of data organization while handling the complex details of physical storage management. Understanding file system structure is fundamental to comprehending how operating systems achieve persistent data storage, efficient file access, and reliable data protection.

The importance of file system structure in modern computing cannot be overstated. Every computing device from smartphones to enterprise servers relies on file systems to organize billions of bytes of data. The choice of file system structure directly impacts performance, reliability, storage efficiency, and the types of features available to users and administrators. Different operating systems have evolved distinct file system structures optimized for their specific use cases, ranging from the simple FAT file system used in embedded devices to the sophisticated NTFS and ext4 file systems found in modern operating systems.

This topic examines the various components that comprise file system architecture, including the layered design of file systems, the structure of file control blocks, directory implementation techniques, file allocation methods, and free space management strategies. These concepts form the foundation for understanding how operating systems implement persistent storage and are essential for anyone studying operating system design and implementation.

## Key Concepts

### Layered Architecture of File Systems

File systems are typically implemented using a layered architecture that separates concerns and provides modularity. The lower layers handle physical disk operations, while upper layers provide user-friendly file and directory abstractions. Understanding this layered approach is crucial for comprehending how file systems function internally.

The lowest layer is the device driver layer, which interfaces directly with hardware controllers for disks and other storage devices. This layer handles physical I/O operations, data transfer between memory and disk, and device-specific details. Above the device driver is the basic file system, which issues generic commands to device drivers without knowledge of file system structure. The file organization module manages the logical organization of files, including free block management and allocation. The logical file system handles metadata operations and maintains the directory structure. Finally, the application interface layer provides system calls and APIs for user programs to interact with files.

### File Control Block and Inode Structure

The file control block (FCB) is the fundamental data structure that stores all information about a file. Each file in the system has an associated FCB that contains metadata such as file name, file type, file permissions, creation/modification timestamps, file size, and pointers to data blocks. When a file is opened, the operating system loads the FCB into memory to facilitate quick access to file metadata.

Modern file systems use a more sophisticated structure called the inode (index node). The inode is a fixed-size data structure that contains direct pointers to data blocks, as well as single, double, and triple indirect pointers for larger files. This design allows efficient access to file data while minimizing the overhead of storing metadata. Unix-like file systems extensively use the inode concept, where each file is identified by an inode number, and multiple directory entries can point to the same inode (creating hard links).

### Directory Implementation

The directory structure provides the namespace for organizing files and implementing file naming. Directories are themselves files that contain entries mapping file names to their FCBs or inodes. The implementation of directories significantly impacts file system performance and capabilities.

In the simplest implementation, directories are linear lists of entries containing file names and FCB pointers. This approach is easy to implement but becomes inefficient for large directories. More sophisticated implementations use hash tables to provide faster name lookup. Some file systems support hierarchical directories with unlimited nesting, while others have simpler tree structures.

Directory entries typically store the file name, inode number, and possibly additional metadata like file attributes. The operating system maintains a current working directory for each process, and path resolution can be absolute (starting from root) or relative (starting from current directory).

### File Allocation Methods

The method used to allocate disk space to files fundamentally affects file system performance and storage efficiency. Three primary allocation methods are commonly used in file systems.

Contiguous allocation assigns consecutive disk blocks to each file. This method provides excellent sequential access performance because the disk head rarely needs to move between blocks. However, it suffers from external fragmentation and the difficulty of finding space for new files. The linked allocation method stores each file as a linked list of disk blocks, with each block containing a pointer to the next block. This eliminates external fragmentation and simplifies file expansion, but random access performance is poor since blocks must be accessed sequentially. The indexed allocation method uses an index block that contains pointers to all data blocks of a file. This provides both efficient random access and eliminates external fragmentation, though it requires additional storage for index blocks and may have issues with very large files.

Modern file systems often use variants of these basic methods. Unix file systems employ an indexed approach with direct, single indirect, double indirect, and triple indirect pointers to handle files of various sizes efficiently.

### Free Space Management

Efficient management of free disk space is essential for file system operation. Several methods exist for tracking available blocks, each with different trade-offs between complexity and efficiency.

The bit vector (bitmap) method uses a bitmap where each disk block is represented by one bit. A value of 0 indicates a free block, while 1 indicates an allocated block. This method is efficient for finding consecutive blocks and is relatively simple to implement, though it requires additional memory for the bitmap itself. The linked list method maintains a list of free blocks by linking them together, requiring minimal overhead but making it difficult to find consecutive free blocks. The grouping method stores addresses of n free blocks in the first free block, combining the benefits of both previous methods.

## Examples

### Example 1: Directory Entry Structure

Consider a simple directory entry in a Unix-like file system. Suppose we have a directory containing three files: "report.txt" (inode 1024), "data.csv" (inode 1025), and "notes.doc" (inode 1026). The directory file would contain entries like the following:

Each directory entry is 32 bytes, with 4 bytes for inode number, 2 bytes for record length, 1 byte for name length, 1 byte for file type, and the remaining 24 bytes for the file name. For "report.txt" with 10 characters, the entry would contain: inode=1024, record length=16, name length=10, file type=1 (regular file), name="report.txt", followed by padding bytes. When the operating system needs to access "data.csv", it reads the directory file sequentially or uses a hash structure to locate the entry with the matching name, then uses the inode number to access the file's metadata and data blocks.

### Example 2: Indexed File Allocation Analysis

Consider a file system with the following parameters: block size = 4 KB, block pointer = 4 bytes, and an index block can contain 1024 pointers (4 KB / 4 bytes). For a file containing 3500 KB of data, we can calculate the number of blocks required as 3500 KB / 4 KB = 875 data blocks.

With direct pointers only (assuming 12 direct pointers in the inode), we can address only 12 × 4 KB = 48 KB directly. For a 3500 KB file, we need the single indirect pointer. The single indirect block can point to 1024 data blocks, providing up to 1024 × 4 KB = 4096 KB of storage. Since our file is 3500 KB, we use all 12 direct pointers (48 KB), the entire single indirect block (1024 pointers pointing to 1024 blocks = 4096 KB worth, but we only need 875 - 12 = 863 more blocks), and no double indirect blocks are needed. The total blocks accessed: 12 (direct) + 863 (single indirect) + 1 (index block itself) = 876 blocks.

### Example 3: Free Space Bitmap Operation

Consider a disk with 1000 blocks managed using a bitmap. Initially, all bits are 0 (all blocks free). When allocating a file requiring 5 consecutive blocks starting at block 50, the file system scans the bitmap to find 5 consecutive 0s. Finding them at positions 50-54, it sets bits 50-54 to 1. The bitmap now shows: bits 0-49 = 0, bits 50-54 = 1, bits 55-999 = 0. When another file needs 3 consecutive blocks, the system finds the first sequence of 3 consecutive zeros. If blocks 0-2 become free and are now 0, but blocks 50-54 are still 1, it would allocate blocks 0-2. This demonstrates how bitmaps enable efficient allocation but can suffer from external fragmentation when large consecutive regions are not available.

## Exam Tips

Understanding file system structure is crucial for DU semester examinations. The following points will help you prepare effectively.

First, ALWAYS draw the layered architecture diagram when answering questions about file system organization. Examiners expect a clear diagram showing the progression from device drivers through basic file system, file organization module, logical file system to the application interface.

Second, REMEMBER that the inode structure is a favorite topic in DU exams. Be thorough with direct, single indirect, double indirect, and triple indirect pointers. Practice calculating maximum file size for given block and pointer sizes.

Third, WHEN comparing allocation methods, mention both advantages and disadvantages. Contiguous allocation scores points for sequential access but loses marks if you forget to mention external fragmentation.

Fourth, FOR directory implementation questions, distinguish between linear search and hash-based directories. Understand that modern file systems often use B+ trees for efficient directory operations.

Fifth, FREE space management questions frequently ask you to calculate the number of bits needed for a bitmap given the disk size. Always show your working: if disk size is 16 GB with 4 KB blocks, you need (16 × 1024 × 1024 × 1024) / (4 × 1024) = 4,194,304 bits.

Sixth, KEY differences between FAT and NTFS or ext file systems often appear in exam questions. Know the specific structural differences and their performance implications.

Seventh, PRACTICE numerical problems on file allocation. Questions asking for number of disk accesses or maximum file size are common and carry significant weight.

Eighth, when answering protection-related questions, remember that file system structure includes permission bits and access control mechanisms. The directory entry typically stores ownership information.