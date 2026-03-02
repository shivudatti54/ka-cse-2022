# Storage Management

## Introduction

Storage management is a fundamental component of modern operating systems, responsible for the efficient organization, access, and maintenance of data on secondary storage devices. While primary memory (RAM) provides fast access to data, it is volatile and limited in capacity. Secondary storage, primarily hard disk drives and solid-state drives, offers persistent data storage at a lower cost per byte. The operating system must abstract the physical complexities of storage devices and provide a seamless interface for users and applications to store and retrieve information.

The file system represents the most visible aspect of storage management, creating an abstraction layer that transforms physical storage devices into logical collections of files and directories. This abstraction allows users to interact with data using meaningful names and hierarchical structures, rather than dealing with raw disk sectors and physical addresses. Modern operating systems support multiple file systems simultaneously, each optimized for different use cases, performance requirements, and storage media types.

Storage management encompasses several critical functions including file creation, deletion, and modification, directory management, free space tracking, disk scheduling, and data integrity maintenance. The efficiency of these operations directly impacts system performance, as disk I/O remains significantly slower than CPU operations. Understanding storage management mechanisms is essential for developing efficient applications and for system administrators managing storage resources.

## Key Concepts

### File System Architecture

The file system architecture consists of multiple layers that work together to provide storage services. At the lowest level, the device driver interacts directly with the storage hardware, handling device-specific commands and data transfer protocols. Above this, the device management layer handles queuing, scheduling, and error recovery for I/O requests. The file organization module translates logical file operations into physical disk blocks, determining how data is stored and retrieved. Finally, the logical file system manages metadata including file names, permissions, timestamps, and directory structures.

The operating system maintains several data structures to manage storage effectively. The inode (index node) structure stores metadata about each file, including file size, ownership, permissions, timestamps, and pointers to data blocks. The directory entry maps file names to inode numbers, enabling name-based file access. The free space bitmap or linked list tracks available disk blocks, enabling efficient allocation of storage space for new files.

### File Allocation Methods

The method chosen for allocating disk space to files significantly impacts file system performance and storage efficiency. CONTIGUOUS ALLOCATION assigns each file a set of consecutive disk blocks. This method offers excellent sequential access performance since the disk head moves minimally when reading consecutive blocks. However, contiguous allocation suffers from external fragmentation, where free space becomes fragmented into small non-contiguous chunks, making it difficult to allocate space for large files. Compaction operations are periodically required to combat this fragmentation.

LINKED ALLOCATION solves the external fragmentation problem by storing each file as a linked list of disk blocks scattered throughout the disk. Each block contains a pointer to the next block in the file. This method eliminates external fragmentation and simplifies file expansion, as new blocks can be added anywhere in the free space. However, linked allocation suffers from poor random access performance, as accessing a block in the middle of a file requires traversing all preceding blocks. Additionally, pointers occupy space within data blocks, reducing usable storage capacity.

INDEXED ALLOCATION addresses the limitations of both previous methods by using an index block that contains pointers to all the blocks belonging to a file. Each file has its own index block, stored in the inode structure. This enables efficient random access while eliminating external fragmentation. The main drawback is the overhead of maintaining index blocks, particularly problematic for small files where a single index block may contain many unused pointers. Modern file systems use variations of indexed allocation, such as the UNIX inode structure that uses direct pointers, single indirect pointers, double indirect pointers, and triple indirect pointers to handle files of various sizes efficiently.

### Free Space Management

The operating system must track which disk blocks are available for allocation to new or expanding files. Several techniques exist for free space management, each with different trade-offs between efficiency and complexity.

The BITMAP METHOD uses a bitmap or bit vector where each disk block is represented by one bit. A value of 0 indicates the block is free, while 1 indicates it is allocated. Bitmaps are compact and enable fast allocation through bit manipulation operations. However, scanning for a sufficient number of consecutive free blocks (for contiguous allocation) can be time-consuming.

The LINKED LIST METHOD maintains a linked list of all free disk blocks. A special free block contains pointers to other free blocks, creating a chain of available space. This method is simple to implement but inefficient for finding large contiguous regions of free space, as the entire list must be traversed.

The GROUPING METHOD stores addresses of n free blocks in the first free block. The first n-1 blocks are actual free blocks, while the nth block contains addresses of another n free blocks. This hierarchical structure enables quick acquisition of multiple free blocks when needed.

### Disk Scheduling Algorithms

When multiple I/O requests are pending, the operating system must determine the order in which to service these requests. The choice of disk scheduling algorithm significantly affects system throughput and response time, particularly for systems with heavy I/O loads.

The FCFS (FIRST-COME-FIRST-SERVED) algorithm services requests in the order they arrive. This approach is fair and simple to implement but typically results in poor performance when the disk head must make long seek movements between requests.

The SSTF (SHORTEST SEEK TIME FIRST) algorithm selects the request closest to the current head position, minimizing seek time. This algorithm provides better throughput than FCFS but may cause starvation for requests located far from the current head position.

The SCAN algorithm, also known as the elevator algorithm, moves the disk head in one direction servicing all requests until it reaches the end, then reverses direction. This approach reduces starvation while providing good average performance. The C-SCAN (CIRCULAR SCAN) variant services requests in one direction only, returning to the beginning without servicing requests during the return trip, providing more uniform response times.

The LOOK algorithm is a variation of SCAN that only travels as far as the last request in each direction, avoiding unnecessary head movement to the disk edges.

### Directory Implementation

Directories store file names and associated metadata, enabling users to organize files in meaningful hierarchies. Several data structures can be used for directory implementation.

In the LINEAR LIST implementation, directory entries are stored as a simple list containing file names and inode numbers. Searching for a file requires linear traversal, resulting in O(n) search time where n is the number of files in the directory.

The HASH TABLE implementation uses a hash function to compute the location of file entries within the directory. This provides O(1) average search time but requires handling hash collisions and managing table size dynamically.

Modern file systems often use B-TREE or B+ -TREE structures for directories, enabling efficient search, insertion, and deletion operations even for directories containing millions of files.

## Examples

### Example 1: Calculating Disk Seek Time

Consider a disk with 200 tracks (numbered 0-199) and a disk head currently at track 50. The following requests arrive in the order given: 90, 30, 100, 45, 120. Calculate the total seek time using FCFS and SSTF algorithms, assuming the time to move between adjacent tracks is 1 millisecond.

**FCFS Algorithm Solution:**

The head moves from track 50 to 90: |90 - 50| = 40 tracks = 40 ms
From 90 to 30: |30 - 90| = 60 tracks = 60 ms
From 30 to 100: |100 - 30| = 70 tracks = 70 ms
From 100 to 45: |45 - 100| = 55 tracks = 55 ms
From 45 to 120: |120 - 45| = 75 tracks = 75 ms

Total seek time = 40 + 60 + 70 + 55 + 75 = 300 ms

**SSTF Algorithm Solution:**

Starting from track 50, the closest request is track 45.
Head moves from 50 to 45: |45 - 50| = 5 tracks = 5 ms
Next closest to 45 is track 30 (from original queue).
Head moves from 45 to 30: |30 - 45| = 15 tracks = 15 ms
Next closest to 30 is track 90.
Head moves from 30 to 90: |90 - 30| = 60 tracks = 60 ms
Next closest to 90 is track 100.
Head moves from 90 to 100: |100 - 90| = 10 tracks = 10 ms
Finally, move from 100 to 120.
Head moves from 100 to 120: |120 - 100| = 20 tracks = 20 ms

Total seek time = 5 + 15 + 60 + 10 + 20 = 110 ms

SSTF significantly reduces total seek time in this example by prioritizing nearby requests.

### Example 2: File Allocation Table Analysis

Consider a file system using linked allocation with a block size of 512 bytes. Each block contains 4 bytes for the next block pointer. A file contains exactly 3000 bytes of data.

**Calculating the number of blocks required:**

Each block can store 512 - 4 = 508 bytes of actual data (excluding pointer).
Number of data blocks needed = ceil(3000 / 508) = ceil(5.905) = 6 blocks

The file will occupy 6 data blocks, with the last block's pointer set to NULL (end of file).

**Calculating storage overhead:**

Total data stored = 3000 bytes
Total pointer overhead = 6 × 4 = 24 bytes
Total file size on disk = 3000 + 24 = 3024 bytes

Overhead percentage = (24 / 3024) × 100 = 0.79%

For very small files, the pointer overhead becomes more significant. If the file contained only 100 bytes, it would still require 1 block:
Overhead percentage = (4 / 512) × 100 = 0.78%

The overhead remains small, but the primary disadvantage is poor random access performance. To read byte 2000 (approximately in block 4), the system must read and process blocks 1, 2, and 3 sequentially to follow the pointers.

### Example 3: Free Space Bitmap Operations

Consider a disk with 16 blocks (numbered 0-15). The current bitmap is: 1111000111110000

The 1s represent allocated blocks, and 0s represent free blocks.

**Question 1:** How many free blocks are available?
Counting the zeros: 4 free blocks (positions 4, 5, 6, 11)

**Question 2:** If a new file requires 3 consecutive blocks, can it be allocated using contiguous allocation?

Scanning the bitmap for 3 consecutive zeros: positions 4, 5, 6 are three consecutive zeros. YES, contiguous allocation is possible.

**Question 3:** Allocate these blocks and update the bitmap.

After allocating blocks 4, 5, and 6:
Bitmap becomes: 1111111111110000

Now only block 11 remains free. If the file needs to expand by 1 more block, contiguous allocation is no longer possible. The system must either use linked allocation (scattered blocks) or perform compaction to create a larger contiguous free region.

## Exam Tips

For DU semester examinations, focus on understanding the fundamental concepts of storage management rather than memorizing definitions. Questions frequently ask students to compare different file allocation methods, analyze free space management techniques, and calculate seek times for disk scheduling algorithms.

When answering questions about file allocation methods, always mention both advantages and disadvantages. For instance, when discussing indexed allocation, explain its efficient random access capability while acknowledging the overhead of index blocks. Similarly, while explaining linked allocation, highlight its elimination of external fragmentation alongside its poor random access performance.

In disk scheduling problems, clearly show each step of the calculation. Students often lose marks by directly jumping to the answer without demonstrating the intermediate head movements. Remember that the absolute difference between track numbers equals the seek time in your calculations.

Understanding the relationship between file system design and system performance is crucial. Explain how directory implementation affects file search operations and how free space management impacts disk fragmentation. Real-world examples using popular file systems like NTFS, ext4, or FAT32 can strengthen your answers.

For long-answer questions, structure your response with clear headings and logical flow. Begin with defining the concept, then explain the mechanism, followed by advantages, disadvantages, and practical applications. This systematic approach demonstrates comprehensive understanding and earns better marks.