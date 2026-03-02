# File System Implementation

## Introduction

File system implementation is a critical component of modern operating systems, serving as the bridge between user-level file operations and the physical storage devices where data persists. When you create, read, write, or delete files, the operating system relies on a well-designed file system to manage these operations efficiently and reliably. The implementation of a file system involves complex algorithms for space allocation, directory management, free space tracking, and data protection.

In the context of the University of Delhi's Computer Science curriculum, understanding file system implementation is essential for comprehending how operating systems provide file abstraction to users and applications. The file system essentially creates a virtual view of storage, abstracting away the physical details of disk geometry, sector sizes, and storage media characteristics. This abstraction allows users and programmers to work with familiar concepts like files and folders without worrying about the underlying hardware complexities. The study of file system implementation encompasses several interconnected components including the overall structure of file systems, methods for allocating disk space to files, techniques for managing free disk space, and the implementation of directory structures that organize files logically.

## Key Concepts

### File System Structure

The file system is organized in multiple layers, each providing specific functionality. At the lowest level, the device driver interacts directly with the physical storage hardware, handling read and write operations at the sector level. Above this lies the basic file system, which issues block-level commands to the device driver. The file organization module understands the logical organization of files and translates logical block addresses to physical block addresses. The logical file system manages metadata including file attributes, access permissions, and directory structures. Finally, the application program interface provides system calls for file operations.

The actual on-disk structure of a file system typically includes several key components. The boot control block contains information needed to boot the system from that partition. The superblock contains file system metadata including the total size of the file system, the number of free blocks, the size of the block, and pointers to free blocks. The free space management structure tracks which blocks are free and available for allocation. The inode structure contains information about each file, including ownership, permissions, timestamps, and pointers to data blocks. The directory structure organizes files into a hierarchical structure.

### Directory Implementation

Directories serve as the organizational backbone of any file system, mapping file names to their internal identifiers. Several approaches exist for implementing directories. In the linear list approach, directory entries are stored as a simple list of file names with pointers to the associated metadata. While simple to implement, this approach suffers from linear search time for file lookup, making it inefficient for directories containing many files.

The hash table approach uses a hash function to compute the location of a file entry within the directory. This provides constant-time average lookup performance, though collision handling adds complexity. Modern file systems like NTFS and ext4 use B+ tree structures for directory indexing, providing efficient lookup even for directories containing millions of files.

The directory entry typically stores the file name, file attributes, and a pointer to the file's metadata structure (often called the inode in UNIX-like systems). In UNIX file systems, each file has an inode containing metadata and data block pointers, while the directory simply maps names to inode numbers.

### Allocation Methods

The method chosen for allocating disk space to files significantly impacts both storage efficiency and access performance. Three primary allocation methods are widely used in file system implementations.

Contiguous allocation assigns each file a set of consecutive disk blocks. This method offers excellent read performance since blocks can be read sequentially without head movement delays. However, it suffers from severe external fragmentation, where free space becomes divided into small non-contiguous chunks. File creation also requires finding a contiguous region of sufficient size, which becomes increasingly difficult as the disk fills up. The compacting or defragmentation process can reclaim contiguous space but requires significant time and temporary disk space.

Linked allocation stores each file as a list of disk block pointers, where each block contains a pointer to the next block in the chain. This eliminates external fragmentation completely and allows files to grow dynamically. However, random access becomes extremely slow since blocks must be traversed sequentially from the beginning. The reliability concern is significant: if any pointer is damaged, the remaining file becomes inaccessible. File allocation table (FAT) file systems use a variation of linked allocation where pointers are stored in a central table in memory, improving reliability and allowing some random access capability.

Indexed allocation addresses the limitations of linked allocation by using an index block that contains pointers to all the file's data blocks. This allows both sequential and random access efficiently. However, the index block itself consumes space, and for very small files, this represents significant overhead. Multiple index block schemes address this by using a hierarchical index structure, where the first-level index block contains pointers to second-level index blocks, which in turn point to data blocks. UNIX inode structures implement this multi-level index approach, with direct pointers for small files, single indirect pointers for medium files, and double/triple indirect pointers for large files.

### Free Space Management

Efficient tracking of free disk space is essential for file system operation. Several techniques are employed in practice.

The bit vector (bitmap) approach uses one bit for each disk block, where 0 indicates free and 1 indicates allocated. This method is simple and allows quick allocation of blocks, though it requires keeping the entire bitmap in memory for large file systems. Finding consecutive free blocks for contiguous allocation becomes efficient with bit vector search.

The linked list approach maintains a list of free blocks by storing a pointer to the first free block in each free block itself. This requires minimal overhead but makes it difficult to find contiguous free space. The free list must be periodically saved to disk to survive system crashes.

The grouping method combines advantages of both approaches. Free blocks are organized into groups, where each group contains pointers to other groups. This allows quick allocation while maintaining reasonable efficiency for finding free space.

The counting method maintains entries for contiguous free regions, storing the starting block number and the count of consecutive free blocks. This is efficient for file systems using contiguous allocation.

## Examples

### Example 1: Indexed Allocation with Single-Level Index

Consider a file system with block size of 4KB and each block pointer occupying 4 bytes. A single-level index block can therefore hold 1024 pointers (4096/4 = 1024). If a file needs to store 5000 blocks of data, we need one index block plus 5 data blocks to store the pointers (5000/1024 = 4.88, requiring 5 index blocks for the data). Wait, let's recalculate: With a single-level index, we have one index block that can point to 1024 data blocks. Since the file needs 5000 blocks, we need additional index blocks. The file will have one index block containing 1024 pointers, but this is insufficient. The system would typically use a multi-level index structure. For this example, assume we use a two-level index: the first-level index has pointers to second-level index blocks, each second-level index block points to data blocks. With 1024 pointers per block, we can have 1024 second-level index blocks, each pointing to 1024 data blocks, giving us capacity for over one million data blocks. For our 5000-block file, we need one first-level index block, approximately 5 second-level index blocks, and 5000 data blocks.

### Example 2: Free Space Bit Vector Operation

Consider a disk with 16 blocks (numbered 0-15) managed using a bit vector. Suppose the current bit vector is: 1,1,0,1,1,1,0,0,1,1,1,1,0,0,1,1 (where 1=allocated, 0=free). The free blocks are 2, 6, 7, 12, and 13. When allocating 3 consecutive blocks for a file requiring contiguous allocation, the system scans the bit vector and finds blocks 6 and 7 are consecutive free blocks but block 5 is allocated, so only 2 consecutive blocks are available. The next available consecutive region is blocks 12 and 13. Since we need 3 consecutive blocks and none exist, the allocation would fail or require defragmentation. For non-contiguous allocation, blocks 2, 6, 7, 12, and 13 can be allocated individually to the file.

### Example 3: Directory Entry Lookup

In a UNIX-style file system, when a process attempts to open "/home/student/data.txt", the kernel performs the following steps. First, it locates the root directory (typically inode 2) and searches for "home" in the root directory entries. Finding the inode number for "home", it reads the inode and searches the home directory for "student". This continues until finding the inode for "data.txt". The kernel then verifies permissions, creates a file descriptor, and returns it to the process. If any component of the path does not exist or permission is denied, the open fails with an appropriate error code (ENOENT or EACCES). This sequential lookup of each path component is why deep directory hierarchies can slow file access.

## Exam Tips

For the University of Delhi semester examinations, several key points deserve special attention. First, understand the fundamental differences between contiguous, linked, and indexed allocation methods, including their respective advantages and disadvantages in terms of access time, external fragmentation, and reliability. Examiners frequently ask students to compare these methods or select appropriate methods for specific scenarios.

Second, be thorough with free space management techniques. Understand how bit vectors work mathematically—if a disk has n blocks, the bit vector requires n bits of memory, which is remarkably efficient. Practice problems involving finding free blocks using bit vectors are common.

Third, directory implementation questions often require understanding how file names are mapped to data blocks. Be prepared to explain why linear search becomes problematic for large directories and how hash tables or tree structures solve this problem.

Fourth, remember that inode structures in UNIX use a combination of direct, single indirect, double indirect, and triple indirect pointers. Calculate maximum file sizes given the block size and pointer size. This is a favorite examination question.

Fifth, understand the concept of file system mounting and how multiple file systems are integrated into a single namespace. The mount point mechanism is important for exam questions.

Sixth, be familiar with the various levels of the file system architecture. Questions may ask you to identify which layer performs specific functions like logical-to-physical address translation or directory management.

Seventh, file protection mechanisms including access control lists (ACLs) and permission bits (read, write, execute for owner, group, others) are important. Understand how UNIX permission bits work and how they are checked during file operations.

Finally, practice drawing and interpreting file system structures. Questions often provide hypothetical scenarios and ask you to trace through operations or identify resulting structures.