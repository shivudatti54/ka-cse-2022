# File Systems: Directory Structures

## Comprehensive Study Material for Ge5A Operating Systems

---

## 1. Introduction

In the realm of operating systems, **file systems** constitute one of the most fundamental and essential components that enable users and applications to store, retrieve, and manage data on secondary storage devices. A file system provides the mechanism for organizing and accessing data stored on disk drives, solid-state drives, and other storage media. Without an efficient file system, the vast amounts of data generated daily in computing environments would be impossible to manage effectively.

The **directory structure** is a critical aspect of any file system, serving as the organizational framework that maintains the mapping between logical file names and their physical locations on storage devices. Directories, often referred to as **folders** in modern graphical user interfaces, provide a hierarchical namespace that allows users to organize their files in a logical and intuitive manner.

### Real-World Relevance

Consider the everyday scenario of organizing documents on a personal computer. A user typically creates folders like "Documents," "Photos," "Downloads," and subfolders within these for further categorization. This hierarchical organization mirrors the tree-structured directory systems used in modern operating systems. When a user saves a file named "Project_Report.docx" in the path `C:\Users\Student\Documents\College\Semester5\`, the operating system uses its directory structure to maintain the association between this logical path and the physical disk sectors where the file's content is stored.

In enterprise environments, directory structures become even more critical. Consider a banking system that must maintain millions of transaction records, customer accounts, and audit logs. An efficient directory structure enables quick file retrieval, supports proper access control, and ensures data integrity—all essential requirements for financial institutions operating under strict regulatory compliance.

For Delhi University students pursuing BSc Physical Science (CS) under NEP 2024, understanding directory structures is not merely an academic exercise. This knowledge forms the foundation for comprehending how operating systems manage storage, which is essential for system programming, database management, and software development courses that follow in the curriculum.

---

## 2. Need for Directory Structures

The primary purpose of a directory structure in a file system is to achieve the following objectives:

1. **Logical Organization**: Directories allow users to organize files based on functionality, project, date, or any other meaningful criterion rather than forcing them to maintain a flat list of all files.

2. **Name Resolution**: The directory structure enables the system to resolve file paths (like `/home/student/project/main.c`) to their physical locations on disk.

3. **Access Control**: Directories can implement permissions and access control lists, ensuring that only authorized users can access certain files or directories.

4. **Efficient Search**: Hierarchical directories enable efficient searching and browsing of files, as users can navigate through the tree structure rather than scanning an entire flat list.

5. **Namespace Management**: Directories prevent name collisions by providing separate namespaces within different directory contexts. Two different users can have files named "report.txt" in their respective home directories without conflict.

6. **File Metadata Storage**: Directories maintain metadata about files, including attributes like creation time, modification time, file size, owner information, and file type.

---

## 3. Types of Directory Structures

The evolution of file system design has produced several distinct types of directory structures, each with its own advantages and limitations. Understanding these structures is essential for comprehending how different operating systems organize files.

### 3.1 Single-Level Directory

The **single-level directory** is the simplest form of directory structure, where all files are contained in one flat directory. In this model, every file must have a unique name because there is no mechanism to differentiate files with the same name stored in different locations.

```
[Root Directory]
├── file1.txt
├── file2.doc
├── program.exe
├── data.csv
└── image.jpg
```

**Advantages**:
- Simple to implement
- Requires minimal system overhead for name resolution
- Suitable for very simple systems or embedded devices

**Disadvantages**:
- Name collision problem: cannot have two files with the same name
- Becomes unwieldy as the number of files grows
- No mechanism for logical organization

**Example Implementation in C**:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_FILES 100
#define MAX_FILENAME 50

typedef struct {
    char filename[MAX_FILENAME];
    int file_size;
    int start_block;
    int is_occupied;
} FileEntry;

typedef struct {
    FileEntry files[MAX_FILES];
    int total_files;
} SingleLevelDirectory;

void initializeDirectory(SingleLevelDirectory *dir) {
    dir->total_files = 0;
    for (int i = 0; i < MAX_FILES; i++) {
        dir->files[i].is_occupied = 0;
    }
}

int addFile(SingleLevelDirectory *dir, char *filename, int size, int start_block) {
    // Check for duplicate names
    for (int i = 0; i < dir->total_files; i++) {
        if (dir->files[i].is_occupied && 
            strcmp(dir->files[i].filename, filename) == 0) {
            printf("Error: File '%s' already exists!\n", filename);
            return -1;
        }
    }
    
    // Find empty slot
    for (int i = 0; i < MAX_FILES; i++) {
        if (!dir->files[i].is_occupied) {
            strcpy(dir->files[i].filename, filename);
            dir->files[i].file_size = size;
            dir->files[i].start_block = start_block;
            dir->files[i].is_occupied = 1;
            dir->total_files++;
            printf("File '%s' added successfully.\n", filename);
            return 0;
        }
    }
    
    printf("Error: Directory is full!\n");
    return -1;
}

int main() {
    SingleLevelDirectory myDir;
    initializeDirectory(&myDir);
    
    addFile(&myDir, "notes.txt", 1024, 10);
    addFile(&myDir, "project.c", 2048, 20);
    addFile(&myDir, "data.csv", 512, 30);
    
    // This will fail - duplicate name
    addFile(&myDir, "notes.txt", 256, 40);
    
    return 0;
}
```

### 3.2 Two-Level Directory

The **two-level directory** structure addresses some limitations of the single-level approach by introducing separate directories for different users or purposes. Each user gets their own private directory (also known as a **User File Directory** or UFD), while the system maintains a **Master File Directory** (MFD) that indexes these user directories.

```
[Master File Directory]
├── User: Alice  → [User Directory: Alice]
│   ├── file1.txt
│   └── project.doc
├── User: Bob    → [User Directory: Bob]
│   ├── report.xls
│   └── notes.txt
└── User: System → [User Directory: System]
    └── config.ini
```

**Advantages**:
- Eliminates name collisions between users
- Provides basic user isolation
- Simple to implement while offering improved organization

**Disadvantages**:
- Users cannot create their own subdirectories
- Limited flexibility for organizing personal files
- The MFD can become a bottleneck if there are many users

### 3.3 Hierarchical (Tree-Structured) Directory

The **hierarchical directory structure** extends the two-level model by allowing unlimited nesting of subdirectories. This creates a tree-like structure where directories can contain both files and other directories. This is the standard model used by virtually all modern operating systems, including Windows, macOS, and Linux.

```
[Root Directory]
├── bin/
│   ├── ls
│   ├── cp
│   └── mv
├── home/
│   ├── student/
│   │   ├── Documents/
│   │   │   ├── Project/
│   │   │   │   └── report.pdf
│   │   │   └── Notes/
│   │   │       └── lecture.txt
│   │   ├── Pictures/
│   │   │   └── vacation.jpg
│   │   └── .bashrc
│   └── admin/
└── etc/
    └── config
```

**Key Concepts**:
- **Current Working Directory (CWD)**: The directory in which a user is currently located. Users can reference files relative to this directory using relative paths.
- **Absolute Path**: The complete path from the root directory to a specific file or directory, starting with `/` (on Unix/Linux) or a drive letter (on Windows).
- **Relative Path**: The path relative to the current working directory.

**Advantages**:
- Highly flexible organization
- Supports unlimited nesting
- Enables logical grouping of related files
- Natural representation of real-world hierarchical relationships

**Disadvantages**:
- More complex implementation
- Path resolution requires more processing
- Deleting a directory requires careful handling to avoid orphaned files

### 3.4 Acyclic Graph Directory

The **acyclic graph directory** structure extends the hierarchical model by allowing directories to be shared through shortcuts or aliases. This creates a directed graph structure where directories can have multiple parent directories, but cycles (infinite loops) are prevented.

```
          [Root]
            │
      ┌─────┴─────┐
      │           │
   [home]      [shared]
      │           │
   ┌──┴──┐      ┌─┴──┐
[docs] [proj] [proj] [data]
   │      │     │
   └──────┴─────┘
      (shared)
```

In this example, the `proj` directory appears in both `/home/` and `/shared/`, but there is no cycle—accessing `proj` through either path leads to the same files without creating an infinite loop.

**Implementation using Symbolic Links (Unix/Linux)**:

```bash
# Creating a symbolic link
ln -s /home/student/projects /shared/projects

# This creates a symbolic link allowing access to the same directory
# through two different paths
cd /home/student/projects  # Original location
cd /shared/projects        # Symbolic link location - same files!
```

**Advantages**:
- Allows file/directory sharing without duplication
- Maintains logical organization
- Supports efficient resource sharing

**Disadvantages**:
- More complex path resolution
- Must prevent cycles during traversal
- Deletion semantics become complicated (when is storage actually freed?)

### 3.5 General Graph Directory

The **general graph directory** structure allows for cycles to exist within the directory structure, meaning a directory can eventually reference itself through a chain of links. This is more flexible but requires sophisticated algorithms to prevent infinite loops during directory traversal.

```
[Root] → [A] → [B] → [C] → [A] (cycle!)
```

Modern operating systems typically prevent such cycles in user-accessible directory structures by using mechanisms like symbolic links with special flags or by implementing cycle-detection algorithms.

---

## 4. File Allocation Methods

The method used to allocate disk space to files significantly impacts file system performance. Three primary allocation methods are discussed below:

### 4.1 Contiguous Allocation

In **contiguous allocation**, each file occupies a set of consecutive disk blocks. This is analogous to storing a document in consecutive pages of a notebook.

```
Disk Blocks:  [0][1][2][3][4][5][6][7][8][9][10][11][12][13][14][15]
                ↑
File A (3 blocks): occupies blocks 2, 3, 4
File B (2 blocks): occupies blocks 5, 6
File C (4 blocks): occupies blocks 9, 10, 11, 12
```

**Advantages**:
- Excellent sequential access performance
- Simple to implement
- Minimal seek time for sequential reads
- Supports direct access (random access)

**Disadvantages**:
- Suffers from external fragmentation
- Difficulty in allocating space for growing files
- Requires knowledge of final file size at creation time

### 4.2 Linked Allocation

In **linked allocation**, each file consists of a linked list of disk blocks. Each block contains a pointer to the next block in the chain.

```
File D: [block 2] → [block 5] → [block 8] → [block 14] → NULL
         ↓           ↓           ↓           ↓
Blocks:  [2][*]    [5][*]    [8][*]    [14][X]
                  (pointers stored in each block)
```

**Advantages**:
- No external fragmentation
- Efficient for sequential access
- File can grow dynamically
- Simple directory entry (only needs starting block)

**Disadvantages**:
- Poor random access performance
- Pointer overhead reduces usable storage
- Reliability issues if pointers become corrupted
- No support for local block access

### 4.3 Indexed Allocation

**Indexed allocation** addresses the limitations of linked allocation by using an **index block** that contains pointers to all the data blocks of a file.

```
Directory Entry for "file.txt":
┌─────────────────────┐
│ File Name: file.txt │
│ Index Block: #7     │
└─────────────────────┘

Index Block (#7):     Data Blocks:
┌──────────────────┐  ┌────────┐
│ Pointer to #10   │→ │ Block 10│
│ Pointer to #15   │→ │ Block 15│
│ Pointer to #22   │→ │ Block 22│
│ Pointer to #28   │→ │ Block 28│
│ Pointer to #31   │→ │ Block 31│
│ ...              │  │ ...    │
└──────────────────┘  └────────┘
```

**Advantages**:
- Supports both sequential and direct (random) access
- No external fragmentation
- More reliable than linked allocation
- Efficient block access

**Disadvantages**:
- Index block overhead
- For large files, may require multiple index levels (multi-level indexing)
- Additional disk I/O to read index block

**Example: UNIX Inode Structure (Simplified)**:

```c
#define MAX_DIRECT_BLOCKS 12
#define POINTER_SIZE 4  // bytes

typedef struct {
    // File metadata
    short inode_mode;          // File type and permissions
    short inode_uid;           // Owner user ID
    int inode_size;            // File size in bytes
    int inode_atime;           // Last access time
    int inode_mtime;           // Last modification time
    int inode_ctime;           // Creation time
    short inode_gid;          // Group ID
    short inode_links_count;  // Hard link count
    int inode_blocks;         // Blocks allocated
    
    // Data block pointers
    int direct_blocks[MAX_DIRECT_BLOCKS];  // Direct pointers
    int indirect_block;                     // Single indirect
    int double_indirect_block;              // Double indirect
    int triple_indirect_block;              // Triple indirect
} inode_t;

// The inode structure in UNIX-like systems supports:
// - 12 direct block pointers
// - 1 single indirect pointer (can address BLOCK_SIZE/4 blocks)
// - 1 double indirect pointer
// - 1 triple indirect pointer
// This allows addressing files of enormous size
```

---

## 5. Free Space Management

Efficient management of free disk space is crucial for file system performance. Several methods exist for tracking available storage:

### 5.1 Bit Vector (Bitmap)

A **bit vector** (or bitmap) maintains one bit for each disk block, where `1` indicates the block is allocated and `0` indicates it is free.

```
Block Number:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
Bitmap:        1  1  0  0  1  1  1  0  1  1  0  0  1  0  1  1
               ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑
             allocated  free for new files
```

**Advantages**:
- Simple and efficient
- Supports fast allocation and deallocation
- Enables various allocation strategies (first-fit, best-fit)

**Disadvantages**:
- Requires storing the entire bitmap
- For very large disks, the bitmap itself becomes significant

### 5.2 Linked List

The **linked list** method maintains a linked list of free disk blocks. The first few bytes of each free block contain pointers to other free blocks.

```
Free List:  [3] → [4] → [7] → [9] → [10] → NULL
             ↓     ↓     ↓     ↓     ↓
Blocks:    [3]   [4]   [7]   [9]   [10]
           (free list stored in the blocks themselves)
```

**Advantages**:
- No additional space required for management
- Simple to implement

**Disadvantages**:
- Poor performance for finding consecutive free blocks
- Sequential traversal required

### 5.3 Grouping

**Grouping** modifies the linked list approach by storing addresses of multiple free blocks in the first free block.

```
Free Block #3 contains:
┌────────────────────────────────────┐
│ Pointer to next group: #7          │
│ List of free blocks: [4, 5, 6,     │
│                      8, 9, 10, ...]│
└────────────────────────────────────┘
```

**Advantages**:
- Faster allocation (can find multiple blocks at once)
- Combines benefits of bitmap and linked list

### 5.4 Counting

**Counting** maintains entries that record the starting block and length of consecutive free regions.

```
Free Space Table:
┌────────────┬─────────┐
│ Start Block│ Length  │
├────────────┼─────────┤
│ 15         │ 3       │
│ 20         │ 5       │
│ 100        │ 10      │
└────────────┴─────────┘

Means: blocks 15-17 free, 20-24 free, 100-109 free
```

**Advantages**:
- Efficient for sequential allocations
- Reduces number of entries needed
- Good when blocks are frequently allocated/deallocated in groups

---

## 6. Directory Implementation

Directories must support various operations while maintaining efficiency. Two primary implementation approaches exist:

### 6.1 Linear List Implementation

The simplest approach stores directory entries in a linear list. Each entry contains the file name, file attributes, and the FCB (File Control Block) or i-node pointer.

```c
#define MAX_ENTRIES 100
#define MAX_NAME_LENGTH 255

typedef struct {
    char filename[MAX_NAME_LENGTH];
    int inode_number;        // Pointer to file's inode/FCB
    time_t creation_time;
    time_t modification_time;
    int file_size;
    unsigned short permissions;
    unsigned char file_type;
} DirectoryEntry;

typedef struct {
    DirectoryEntry entries[MAX_ENTRIES];
    int entry_count;
} Directory;

// Searching for a file - O(n) complexity
int findFile(Directory *dir, char *filename) {
    for (int i = 0; i < dir->entry_count; i++) {
        if (strcmp(dir->entries[i].filename, filename) == 0) {
            return i;  // Found at index i
        }
    }
    return -1;  // Not found
}
```

**Advantages**:
- Simple implementation
- Low overhead for small directories

**Disadvantages**:
- Linear search time O(n)
- Performance degrades with large directories

### 6.2 Hash Table Implementation

A **hash table** uses a hash function to map file names to directory entry locations, providing faster search times.

```c
#define TABLE_SIZE 256

typedef struct HashEntry {
    char filename[MAX_NAME_LENGTH];
    int inode_number;
    struct HashEntry *next;  // For collision handling
} HashEntry;

typedef struct {
    HashEntry *table[TABLE_SIZE];
} HashDirectory;

unsigned int hashFunction(char *filename) {
    unsigned int hash = 5381;
    int c;
    while ((c = *filename++)) {
        hash = ((hash << 5) + hash) + c;  // hash * 33 + c
    }
    return hash % TABLE_SIZE;
}

int findFileHash(HashDirectory *dir, char *filename) {
    unsigned int index = hashFunction(filename);
    HashEntry *entry = dir->table[index];
    
    while (entry != NULL) {
        if (strcmp(entry->filename, filename) == 0) {
            return entry->inode_number;
        }
        entry = entry->next;
    }
    return -1;
}
```

**Advantages**:
- Average case O(1) search time
- Efficient for large directories

**Disadvantages**:
- More complex implementation
- Collision handling overhead
- Fixed table size

---

## 7. Practical Examples: Specific OS File Systems

### 7.1 FAT (File Allocation Table)

The **FAT file system**, originally designed for MS-DOS and still used in USB drives and memory cards, uses a simple linked allocation scheme with a central File Allocation Table.

```
┌────────────────────────────────────────────────────────────┐
│                    FAT File System                         │
├────────────────────────────────────────────────────────────┤
│ Boot Sector                                                │
├────────────────────────────────────────────────────────────┤
│ FAT (File Allocation Table) - Linked List of Clusters     │
│ ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐       │
│ │  2 │  5 │EOF │  8 │ 10 │EOF │    │  3 │  9 │EOF │       │
│ └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘       │
├────────────────────────────────────────────────────────────┤
│ Root Directory                                             │
│ ┌───────────┬────────┬────────┐                            │
│ │ FILE.TXT  │→Cluster 2│                              │
│ │ DATA.DAT  │→Cluster 5│                              │
│ └───────────┴────────┴────────┘                            │
├────────────────────────────────────────────────────────────┤
│ Data Region (Clusters)                                      │
└────────────────────────────────────────────────────────────┘
```

**Key Features**:
- Uses File Allocation Tables to track cluster allocation
- Supports FAT12, FAT16, and FAT32 variants
- Simple and widely compatible
- Limited to 8.3 filename convention (older versions)

### 7.2 NTFS (New Technology File System)

**NTFS**, the default file system for Windows NT and later versions, is a more sophisticated journaling file system.

**Key Features**:
- **Master File Table (MFT)**: Central database storing file metadata
- **Journaling**: Logs changes before committing to prevent corruption
- **Compression and Encryption**: Built-in support
- **Access Control Lists (ACLs)**: Advanced security
- **Sparse Files**: Efficient handling of files with large zero-filled regions
- **Disk Quotas**: Limiting per-user disk space

### 7.3 ext4 (Fourth Extended Filesystem)

The **ext4** file system, used by most Linux distributions, is an evolution of ext2 and ext3.

```bash
# Example: Creating an ext4 filesystem (requires root)
sudo mkfs.ext4 /dev/sdb1

# Checking ext4 filesystem properties
dumpe2fs -h /dev/sdb1 | head -20

# Example inode structure concept
# Each file has an inode containing:
# - File mode (type and permissions)
# - Owner UID and GID
# - File size
# - Timestamps (access, modify, change)
# - Direct/Indirect block pointers (like the earlier code example)
# - Extended attributes
```

**Key Features**:
- Journaling for improved reliability
- Extents (contiguous block allocation) for large files
- Delayed allocation for better performance
- Support for files up to 16TB and volumes up to 1EB
- Backward compatibility with ext2/ext3

### 7.4 APFS (Apple File System)

**APFS**, introduced by Apple for macOS, iOS, and related systems, emphasizes encryption and snapshot capabilities.

**Key Features**:
- Built-in encryption (AES-256)
- Cloning for efficient file copies
- Snapshots for system backup
- Space sharing between volumes
- Fusion drives support for hybrid storage

---

## 8. Key Takeaways

1. **Directory structures** provide the organizational framework for file systems, evolving from simple single-level designs to complex hierarchical and graph-based structures.

2. **Types of directory structures** include:
   - Single-Level: Simple but limited (name collisions, no organization)
   - Two-Level: Introduces user directories (MFD + UFD)
   - Hierarchical (Tree-Structured): Standard modern approach with unlimited nesting
   - Acyclic Graph: Allows sharing through aliases without cycles
   - General Graph: Maximum flexibility but requires cycle prevention

3. **File allocation methods** determine how disk space is assigned to files:
   - Contiguous: Fast but suffers from fragmentation
   - Linked: Simple but poor random access
   - Indexed: Supports direct access, used in modern systems

4. **Free space management** techniques include bit vectors (most common), linked lists, grouping, and counting—each with distinct performance trade-offs.

5. **Directory implementation** typically uses linear lists (simple, O(n) search) or hash tables (efficient, O(1) average search).

6. **Real-world file systems** like FAT, NTFS, ext4, and APFS implement variations of these concepts, with modern systems adding journaling, encryption, and advanced features.

7. Understanding these foundational concepts is essential for system programming, database management, and troubleshooting storage-related issues in any operating system environment.

---

## 9. Self-Assessment Questions

### Multiple Choice Questions

**Question 1**: Which directory structure allows a file to appear in multiple directories without duplication?

A) Single-Level Directory  
B) Two-Level Directory  
C) Hierarchical Directory  
D) Acyclic Graph Directory  

**Correct Answer**: D) Acyclic Graph Directory

---

**Question 2**: In the context of file allocation, which method provides the best random access performance?

A) Contiguous Allocation  
B) Linked Allocation  
C) Indexed Allocation  
D) Linked List Allocation  

**Correct Answer**: C) Indexed Allocation

---

**Question 3**: What is the primary advantage of a bit vector (bitmap) for free space management?

A) Requires minimal memory overhead  
B) Supports fast allocation and deallocation  
C) Eliminates external fragmentation completely  
D) Works only with small disk sizes  

**Correct Answer**: B) Supports fast allocation and deallocation

---

**Question 4**: In UNIX/Linux file systems, what data structure stores file metadata and block pointers?

A) File Allocation Table (FAT)  
B) Master File Table (MFT)  
C) Inode (Index Node)  
D) Directory Entry  

**Correct Answer**: C) Inode (Index Node)

---

**Question 5**: Which file system journaling technique records the intended operation before executing it?

A) Write-back journaling  
B) Write-through journaling  
C) Metadata-only journaling  
D) Ordered journaling  

**Correct Answer**: A) Write-back journaling

---

**Question 6**: What is the maximum depth of directory nesting allowed in modern hierarchical file systems?

A) 1  
B) 10  
C) 64  
D) No fixed limit (theoretically unlimited)  

**Correct Answer**: D) No fixed limit (theoretically unlimited)

---

**Question 7**: The FAT file system uses which allocation method?

A) Contiguous Allocation  
B) Linked Allocation  
C) Indexed Allocation  
D) None of the above  

**Correct Answer**: B) Linked Allocation

---

**Question 8**: What problem is associated with contiguous file allocation?

A) Internal fragmentation  
B) External fragmentation  
C) Poor sequential access  
D) Difficult random access  

**Correct Answer**: B) External fragmentation

---

## References and Further Reading

1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. Stallings, W. (2018). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson.
3. Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems* (4th ed.). Pearson.
4. Delhi University NEP 2024 Syllabus - Ge5A Operating Systems
5. Linux Kernel Documentation - ext4 Filesystem
6. Microsoft Documentation - NTFS Technical Reference

---

*This study material has been prepared for BSc Physical Science (CS) students at Delhi University under NEP 2024, covering all aspects of File Systems Directory Structures as per the Ge5A Operating Systems syllabus.*