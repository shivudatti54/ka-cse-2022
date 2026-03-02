# Directory and Disk Structure

## Introduction

Directory and disk structure forms the fundamental organizational backbone of any modern file system. When you save a document, create a folder, or access data from your computer's storage, you are directly interacting with directory structures and disk organization mechanisms. Understanding how operating systems manage these structures is crucial for any computer science student, as it explains the invisible architecture that makes persistent data storage possible.

The directory structure, often visualized as an inverted tree, provides a hierarchical organization mechanism that allows users and applications to organize files logically into folders and subfolders. Meanwhile, the disk structure concerns itself with how files are physically stored on the storage medium, including how free space is tracked, how files are allocated, and how the disk is divided into manageable sections. Together, these components determine the efficiency, reliability, and performance of file operations.

In the context of the University of Delhi's Computer Science curriculum, this topic builds upon the foundational file concept and access methods covered earlier. The knowledge gained here is essential for understanding how file systems are implemented and how they protect data while providing efficient access mechanisms.

## Key Concepts

### Directory Structure

A directory is a special type of file that contains information about other files, including their names, locations, attributes, and metadata. The directory structure defines how these directories are organized and how users navigate through the file system hierarchy.

**Single-Level Directory**: The simplest form of directory organization where all files are placed in a single directory. While easy to implement, this approach creates significant problems as the number of files grows, particularly naming conflicts and inability to group related files.

**Two-Level Directory**: Introduces a separate directory for each user, solving the naming conflict problem but still lacking the ability to create nested hierarchies. Each user has their own private directory, and file access requires specifying either an absolute or relative path.

**Hierarchical Directory (Tree-Structured)**: The most common and practical approach, where directories can contain subdirectories, forming a tree-like structure. This allows for logical organization of files into categories, projects, or any user-defined grouping. The root directory serves as the topmost level, and every file has a unique path from the root.

**Acyclic Graph Directory**: Allows directories to share subdirectories and files through shortcuts or links, creating a directed acyclic graph structure. This enables multiple paths to access the same file without duplicating data, though it introduces complexity in deletion and traversal operations.

**General Graph Directory**: Permits cycles in the directory structure, meaning a directory can reference itself directly or indirectly. While powerful, this structure requires careful handling to avoid infinite loops during directory traversal and complex memory management during cleanup operations.

### Directory Implementation

**Linear List Implementation**: The simplest method where directory entries are stored as a linked list or array. Searching requires linear time complexity O(n), where n is the number of entries. This approach is straightforward but becomes inefficient for large directories with thousands of files.

**Hash Table Implementation**: Uses a hash function to map file names to directory entries, providing average O(1) lookup time. The main challenges include handling hash collisions and managing the fixed size of the hash table. This implementation significantly improves performance for large directories.

**Information Stored in Directory Entries**: Each directory entry typically contains the file name, file control block (FCB) or inode number, file type, file size, creation/modification timestamps, access permissions, and pointers to actual data blocks. The exact structure varies depending on the file system design.

### Disk Structure

**Physical Disk Organization**: A disk is divided into concentric circles called tracks, and each track is divided into sectors. The combination of tracks and sectors creates a grid of storage units. Modern disks use zones where outer tracks contain more sectors than inner tracks to maximize storage capacity.

**Disk Partitioning**: The disk is divided into partitions, with each partition acting as an independent storage unit. A partition may contain a file system, be used as raw storage, or serve as swap space. The partition table, stored in the master boot record (MBR) or GUID partition table (GPT), maintains information about these divisions.

**Boot Block**: The first sector of the disk or partition that contains the bootstrap loader, the small program that initiates the operating system startup process. This critical structure ensures the system can boot after power-on.

**Superblock**: Contains file system metadata including the file system type, size, number of free blocks, free inode count, and other critical parameters. The superblock is typically duplicated across multiple locations for redundancy.

**Free Space Management**: The file system maintains data structures to track which disk blocks are available for allocation. Common methods include bit vectors (bitmap), linked lists, and group counting. Each method has different trade-offs in terms of space efficiency and allocation speed.

### Mounting and Path Resolution

**File System Mounting**: Before a file system can be accessed, it must be mounted at a specific directory point, known as the mount point. The operating system attaches the file system's root directory to this point in the existing directory tree, creating a unified namespace.

**Path Resolution**: When a process requests access to a file, the operating system must resolve the pathname to the actual file location. This involves parsing the path components, checking permissions at each directory level, and locating the final file's inode or FCB.

## Examples

### Example 1: Hierarchical Directory Navigation

Consider the directory structure:

```
/ (root)
├── home/
│   ├── student/
│   │   ├── documents/
│   │   │   ├── assignment.txt
│   │   │   └── notes.pdf
│   │   ├── pictures/
│   │   │   └── photo.jpg
│   │   └── downloads/
│   └── admin/
└── etc/
    └── config.conf
```

When the user requests access to "/home/student/documents/assignment.txt", the operating system performs the following steps:

1. Starting from the root directory (/), locate the "home" entry
2. Within "home", find the "student" subdirectory
3. Navigate to "student" and locate the "documents" directory
4. Finally, locate "assignment.txt" within "documents" and retrieve its metadata

Each component requires a directory lookup operation, demonstrating how path length directly impacts file access time.

### Example 2: Directory Entry Structure

Assume a UNIX-style inode-based file system where each directory entry contains:

- Inode number (4 bytes)
- File name (255 bytes maximum)
- Entry length

For a file named "data.txt" with inode number 1042, the directory entry would be structured as:

```
| Inode Number (1042) | Entry Length (260) | Name Length (8) | File Type | "data.txt" |
| 4 bytes             | 2 bytes            | 1 byte          | 1 byte    | 8 bytes   |
```

The directory file containing this entry would have the inode table pointing to actual data blocks, where the file's content is stored. To read the file, the system first reads the directory entry to get the inode number, then accesses the inode to find data block pointers.

### Example 3: Free Space Bitmap Calculation

Consider a disk with 1 million blocks. Using a bitmap for free space management:

- Total bitmap size = 1,000,000 bits = 125,000 bytes ≈ 122 KB
- Each bit represents one disk block
- If block 0 is allocated and block 1 is free: bitmap starts as "10..."

To allocate a file requiring 500 contiguous blocks:
1. Scan the bitmap for 500 consecutive 1s (representing free blocks)
2. Once found, mark these bits as 0 (allocated)
3. Update the superblock with the starting block number

This approach provides O(1) allocation checking for any specific block and O(n) scanning for finding contiguous space, where n is the total number of blocks.

## Exam Tips

1. **Understand Directory vs. Disk Structure**: Remember that directories are logical organizational structures for files, while disk structure refers to the physical organization of storage media. Both work together but serve distinct purposes.

2. **Know All Directory Structure Types**: Be prepared to draw and explain each type (single-level, two-level, hierarchical, acyclic graph, general graph) with their advantages and disadvantages. This is a frequently asked question in DU examinations.

3. **Time Complexity Matters**: For directory implementation, remember that linear list provides O(n) search time while hash table provides O(1) average case. Consider the trade-offs when choosing between implementations.

4. **Directory Entry Contents**: Memorize what information is stored in a directory entry: file name, inode/FCB number, file type, size, timestamps, and permissions. This information is essential for understanding file system operations.

5. **Boot Block and Superblock Functions**: These are critical disk structures. The boot block initiates system startup, while the superblock contains file system metadata. Never confuse their purposes.

6. **Mount Point Concept**: When explaining file system mounting, emphasize that mounting attaches one file system's root to a directory in another file system, creating a unified namespace.

7. **Path Resolution Process**: Be able to explain step-by-step how the OS resolves a file path to its actual location, including the operations performed at each directory level.

8. **Free Space Management Methods**: Understand the three main approaches (bit vector/bitmap, linked list, and grouping) and their respective strengths. The bitmap method is most commonly implemented in modern file systems.

9. **Real-World Example Connection**: Relate concepts to familiar file systems like NTFS, ext4, or FAT32 to demonstrate practical understanding. Know that NTFS uses MFT (Master File Table), while ext4 uses inodes.

10. **Answer Structure for Long Questions**: For 10-15 mark questions, always begin with definitions, followed by diagrams where applicable, then explanations with examples, and conclude with advantages and limitations.