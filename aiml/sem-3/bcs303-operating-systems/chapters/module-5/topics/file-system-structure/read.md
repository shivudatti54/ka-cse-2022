# File System Structure

## Introduction

File system structure refers to the organization and layout of data on secondary storage devices, enabling efficient storage, retrieval, and management of files. In operating systems, the file system serves as the interface between users/applications and the physical storage medium, abstracting the complexities of disk management into logical file operations. Understanding file system structure is fundamental to comprehending how operating systems handle persistent data, manage storage space, and provide file access mechanisms.

The importance of file system structure in computer science cannot be overstated. Every computing device, from smartphones to enterprise servers, relies on file systems to organize billions of bytes of data. For students at the University of Delhi, this topic forms a critical component of the Operating System curriculum, with direct practical implications in system programming, database management, and software development. The file system structure determines crucial system characteristics including access speed, storage efficiency, data reliability, and security mechanisms.

Modern file systems have evolved significantly since the early days of computing, progressing from simple flat structures to sophisticated hierarchical organizations supporting millions of files. This evolution reflects the increasing demands for data management in contemporary computing environments, where users routinely handle terabytes of information across distributed systems.

## Key Concepts

### Hierarchical Directory Structure

The most common file system structure is the hierarchical directory model, organizing files in a tree-like structure with a root directory at the top and subdirectories branching below. This structure begins at the root directory (represented by "/" in Unix/Linux and "\" in Windows), from which all other directories and files originate. Each directory can contain both files and subdirectories, creating a parent-child relationship throughout the filesystem.

The hierarchical structure provides several advantages: intuitive organization reflecting human mental models, efficient search operations through path traversal, and logical grouping of related files. For instance, a typical user's directory might contain subdirectories like Documents, Downloads, Pictures, and Music, each organizing specific file types. The absolute path from root to any file uniquely identifies its location, while relative paths specify locations relative to the current working directory.

### Directory Implementation

Directories in file systems function as special files containing metadata about other files. Several methods exist for implementing directories:

**Linear List Implementation**: Stores directory entries as a linear list of file names with pointers to corresponding metadata blocks. While simple to implement, search operations require linear time O(n), making this inefficient for directories containing thousands of files.

**Hash Table Implementation**: Uses a hash function to map file names to locations within the directory, enabling average-case constant time O(1) lookups. Hash collisions must be handled appropriately, and the hash table typically requires periodic resizing as the directory grows.

**B-Tree Based Implementation**: Modern file systems like NTFS and ext4 employ B-tree structures for directories, providing efficient ordered traversal, range queries, and logarithmic search complexity. This approach balances performance with storage efficiency.

### File Allocation Methods

How files are physically stored on disk significantly impacts system performance:

**Contiguous Allocation**: Assigns each file a single continuous block of disk sectors. This method offers excellent sequential access performance and simple directory entries storing only the starting block and length. However, it suffers from external fragmentation and difficulty in determining optimal file size at creation time.

**Linked Allocation**: Stores each file as a collection of disk blocks scattered across the device, with each block containing a pointer to the next block. This eliminates external fragmentation and simplifies file growth but provides poor random access performance since blocks must be traversed sequentially. File allocation table (FAT) file systems exemplify this approach.

**Indexed Allocation**: Maintains an index block containing pointers to all data blocks comprising a file. This approach supports direct random access while avoiding external fragmentation but requires additional storage for index blocks and has size limitations for very large files. Solutions include multi-level index blocks and linked index blocks.

### Inode Structure

The inode (index node) is a fundamental data structure in Unix-like file systems, containing all metadata about a file except its name. Each file is associated with exactly one inode, identified by an inode number. Inodes typically store:

- File type (regular file, directory, symbolic link, device file)
- File permissions (read, write, execute for owner, group, others)
- Ownership information (UID, GID)
- File size in bytes
- Timestamps (creation, modification, access)
- Link count (number of hard links pointing to this inode)
- Pointers to data blocks (direct, single indirect, double indirect, triple indirect)

The inode structure exemplifies the separation between the logical file concept and physical data storage, with the directory entry mapping human-readable file names to inode numbers.

### Boot Block and Superblock

File systems contain specific system areas critical to functionality:

**Boot Block**: The first sector of the disk (or partition), containing bootstrap code used to initialize the system. Only the boot block of the bootable partition contains executable code; other partitions may have unused boot blocks.

**Superblock**: Contains file system metadata including total inode and data block counts, free inode and block counts, block size, filesystem state, and magic number identifying the file system type. Multiple copies of the superblock are typically maintained for redundancy, distributed across the partition.

### Virtual File System (VFS)

Modern operating systems implement VFS as an abstraction layer allowing multiple file system types to coexist. VFS defines a standard interface that all file systems must implement, enabling transparent access to files regardless of underlying structure. This design supports diverse file systems including ext4, NTFS, FAT32, NFS, and procfs within the same system.

## Examples

### Example 1: Analyzing a Simple Hierarchical File System

Consider a directory structure for a university course:

```
/home/cs student/
├── Documents/
│   ├── Assignments/
│   │   ├── Assignment1.pdf
│   │   └── Assignment2.pdf
│   ├── Notes/
│   │   ├── OS_lecture1.txt
│   │   └── OS_lecture2.txt
│   └── Project/
│       └── report.docx
├── Pictures/
│   ├── diagram.png
│   └── screenshot.jpg
└── Downloads/
    └── software.zip
```

**Absolute Path**: /home/cs student/Documents/Assignments/Assignment1.pdf
**Current Directory**: /home/cs student/Documents
**Relative Path to diagram.png**: ../Pictures/diagram.png

When the user accesses Assignment1.pdf, the operating system performs these steps:
1. Locate root directory (starting point)
2. Traverse to "home" subdirectory
3. Navigate to "cs student" directory
4. Enter "Documents" subdirectory
5. Access "Assignments" subdirectory
6. Finally locate "Assignment1.pdf"

### Example 2: Contiguous vs Linked Allocation

Suppose we need to store a 400KB file on a disk with 100KB block size:

**Contiguous Allocation**: Requires 4 consecutive blocks, say blocks 10-13.
Directory entry: {filename: "data.txt", start: 10, length: 4}
Access time to block 3: Direct access to block 12 (start + 3)

**Linked Allocation**: Blocks can be scattered anywhere on disk, say blocks 5, 17, 23, and 31.
Directory entry: {filename: "data.txt", start: 5}
Access to block 3: Read block 5 → follow pointer to block 17 → follow pointer to block 23 → follow pointer to block 31 (requires 4 disk I/O operations)

For sequential access, both methods perform similarly. For random access, contiguous allocation dramatically outperforms linked allocation.

### Example 3: Inode Pointer Structure

In a Unix-like file system with 4KB blocks and 32-bit block pointers:

- Direct pointers: 12 pointers (48KB directly addressable)
- Single indirect: 1 pointer to index block (1024 pointers × 4KB = 4MB)
- Double indirect: 1 pointer to level-1 index (1024 × 1024 × 4KB = 4GB)
- Triple indirect: 1 pointer to level-2 index (1024³ × 4KB = 4TB)

Maximum file size = 48KB + 4MB + 4GB + 4TB (practically limited by other factors)

To read byte 5,000,000 of a file:
- Offset 5,000,000 / 4096 = block 1220 (1220 > 12, requires single indirect)
- Read inode → read single indirect block → follow pointer to data block 1220

## Exam Tips

1. **DRAW DIAGRAMS REGULARLY**: In exams, always include visual representations of directory structures, inode layouts, and allocation method diagrams. examiners appreciate well-labeled diagrams that clearly demonstrate understanding.

2. **DISTINGUISH BETWEEN LOGICAL AND PHYSICAL**: Remember that file system structure operates at two levels—logical organization (hierarchical directories visible to users) and physical organization (how data blocks are actually stored on disk). Questions frequently test understanding of this distinction.

3. **COMPARISON QUESTIONS ARE COMMON**: Be prepared to compare contiguous, linked, and indexed allocation in terms of external fragmentation, access time, random access support, and storage efficiency. A table comparing these methods is often expected in answers.

4. **UNDERSTAND THE ROLE OF DIRECTORIES**: Directories are not merely folders—they are data structures containing mappings between file names and metadata (inode numbers or FAT entries). Explain this distinction clearly in answers.

5. **VFS CONCEPT FOR MODERN SYSTEMS**: With increasing emphasis on modern operating systems, understanding Virtual File System as an abstraction layer enabling multiple file system types is crucial. Explain how VFS provides portability and flexibility.

6. **SUPERBLOCK AND BOOT BLOCK FUNCTIONS**: Never confuse these two critical structures—the boot block handles system startup while the superblock contains file system metadata. Both are essential for system operation.

7. **TIME COMPLEXITY ANALYSIS**: Be prepared to analyze search, insert, and delete operations in different directory implementations. Linear search is O(n), hash-based is O(1) average case, and tree-based provides O(log n) complexity.