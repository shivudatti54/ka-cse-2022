# Directory Implementation

## Introduction

Directory implementation is a fundamental aspect of modern file systems that manages the organization, storage, and retrieval of file metadata. When you create, delete, or access files on your computer, the directory structure facilitates these operations by maintaining crucial information such as file names, locations, sizes, creation timestamps, and access permissions. Without efficient directory implementations, file systems would be unable to provide the seamless user experience we expect when managing thousands or millions of files on our storage devices.

In the context of operating systems, a directory serves as a mapping between file names and their corresponding file control blocks (FCBs) or inodes. The implementation strategy chosen for directories directly impacts the performance of file operations like search, creation, deletion, and listing. Modern operating systems support various directory structures, from simple single-level directories to complex hierarchical and graph-based structures. Understanding these implementation techniques is essential for computer science students, as it provides insight into how operating systems manage secondary storage and optimize data access patterns.

This topic becomes particularly relevant when considering real-world applications. When you use command-line tools like `ls` in Linux or explore folders in Windows Explorer, the underlying directory implementation determines how quickly these operations complete. For instance, searching for a file in a directory containing thousands of files requires efficient lookup mechanisms, which directory implementation techniques directly address.

## Key Concepts

### Directory Structure Overview

A directory is essentially a special type of file that contains information about other files. In UNIX-like systems, everything is treated as a file, including directories themselves. Each directory entry typically contains the file name and a pointer to the file's metadata or data blocks. The operating system maintains several attributes for each file, including:

- File name and extension
- Unique identifier (inode number or FCB index)
- File type (regular file, directory, device file, etc.)
- File size in bytes
- Timestamps (creation, modification, access)
- Owner and group information
- Permission bits (read, write, execute)
- Pointers to data blocks

### Single-Level Directory Implementation

The simplest directory implementation uses a single-level structure where all files reside in one directory. This approach, also known as the flat directory structure, maintains a linear list of all file entries. The directory contains an array or linked list where each entry stores the file name and associated metadata.

In a single-level directory, file name uniqueness is critical since all files share the same namespace. This simplicity makes implementation straightforward but creates significant limitations. Searching for a specific file requires scanning the entire directory, resulting in O(n) time complexity where n represents the total number of files. File creation involves checking all existing entries to ensure no name conflicts. This approach works only for very small systems with limited file counts, making it impractical for modern computing environments.

### Two-Level Directory Implementation

Two-level directories introduce user isolation by providing separate directories for each user. The system maintains a master directory (also called the user directory table) that points to each user's home directory. This structure prevents users from accessing or conflicting with other users' files, providing basic security and organization.

When a user logs in, the system locates their personal directory through the master directory and sets it as the current working directory. File access within a user's directory is straightforward, while accessing other users' files requires explicit path specification. The MS-DOS operating system historically used each this approach, where disk contained a root directory and user-created subdirectories.

### Hierarchical Directory Structure

Modern file systems employ hierarchical (tree-structured) directories that allow unlimited nesting of subdirectories. This structure provides excellent organization capabilities, allowing users to categorize files logically. The directory structure forms a tree where directories are internal nodes and files are leaf nodes.

In this implementation, each directory entry points to either a file or another directory. Path resolution becomes essential: absolute paths specify the complete path from the root directory, while relative paths specify locations relative to the current working directory. When you execute commands like `cd /home/student/documents`, the operating system traverses each component of the path, looking up directory entries at each level.

### Implementation Using Linear List

The most straightforward implementation uses a linear list (array or linked list) to store directory entries. Each entry contains the file name and metadata pointer. Searching requires traversing the list sequentially, resulting in O(n) complexity for both lookups and insertions. Deletion involves either marking entries as free or maintaining a free list to reuse slots.

Despite the performance limitations, linear lists offer simplicity and work adequately for directories with few files. The linked list variant provides dynamic sizing without pre-allocating fixed space, though it suffers from poor locality of reference since entries may be scattered across storage.

### Hash Table Based Implementation

Hash table implementations dramatically improve search performance by converting file names into array indices using a hash function. When searching for a file, the system computes the hash of the file name and directly accesses the corresponding bucket. This approach reduces average search time to O(1), though collisions (different file names producing the same hash) require resolution strategies.

Separate chaining handles collisions by maintaining linked lists within each bucket. When multiple files hash to the same index, they form a chain that must be searched sequentially. Open addressing, an alternative approach, stores colliding entries in alternative positions determined by the hash function and a probing sequence.

Hash tables introduce additional complexity regarding directory size management. The hash table must be sized appropriately, and rehashing becomes necessary when the load factor exceeds thresholds. Additionally, hash functions must minimize collisions while distributing entries uniformly across buckets.

### File Allocation Table (FAT) Implementation

The FAT file system, used historically by MS-DOS and early Windows versions, implements directories using the File Allocation Table structure. Each directory entry contains the file name, attributes, timestamps, starting cluster number, and file size. The FAT itself is a table stored separately that tracks which clusters belong to each file.

Directory entries in FAT point to the first cluster of each file, with subsequent clusters identified through FAT entries forming a chain. The root directory has a fixed location and size, while other directories are stored as regular files. This linked-list based approach provides flexibility but requires traversing cluster chains to access file data.

The simplicity of FAT made it popular for removable media, though it suffers from limitations including maximum file size constraints and performance degradation with fragmented files.

### UNIX Inode Implementation

UNIX-like file systems use an inode (index node) structure for storing file metadata. Each file has a unique inode number that serves as an identifier within the file system. Directory entries map file names to inode numbers rather than containing metadata directly.

The inode structure contains direct pointers to data blocks, single, double, and triple indirect pointers for larger files, and metadata including file size, timestamps, ownership, and permissions. This design separates metadata from data storage, allowing efficient access to file attributes without reading actual file content.

Directories in UNIX are implemented as special files containing directory entries. Each entry stores the inode number and file name. The directory implementation typically uses linear lists for smaller directories and may employ hash tables or B-trees for larger ones to optimize lookup performance.

### Directory Operations Implementation

The implementation must support fundamental directory operations efficiently:

**Create**: Allocate a new directory entry, initialize metadata, and add to the directory structure. This requires finding a free slot and ensuring name uniqueness.

**Delete**: Remove the directory entry and release associated resources. In hierarchical structures, this may require recursive deletion of subdirectories.

**Search**: Locate a file by name within the directory. Performance depends entirely on the implementation method chosen.

**List**: Retrieve all entries within a directory for display or processing.

**Rename**: Change the file name stored in the directory entry without affecting file content or metadata.

**Traverse**: Navigate through the directory hierarchy to locate files using path names.

## Examples

### Example 1: Linear List Directory Search

Consider a directory implemented as a linear list containing 1000 file entries. To locate a file named "assignment.pdf", the system must examine each entry sequentially until finding a match.

```
Directory Entry Structure:
[File Name (50 bytes) | Inode Pointer (4 bytes) | Attributes (14 bytes)]

Starting from index 0:
Entry 0: "syllabus.doc" → not matching
Entry 1: "notes.txt" → not matching
...
Entry 537: "assignment.pdf" → FOUND after 538 comparisons
```

The time complexity is O(n) where n equals 1000 in this case. If each entry comparison takes approximately 0.001 milliseconds, the total search time becomes about 0.538 milliseconds. While this seems fast, the time grows linearly with directory size, making it unsuitable for directories containing millions of files.

### Example 2: Hash Table Directory Lookup

Using a hash table with 256 buckets, the same search for "assignment.pdf" works as follows:

```
Hash Function: sum of character ASCII values mod 256

"assignment.pdf":
a(97) + s(115) + s(115) + i(105) + g(103) + n(110) + m(109) + e(101) + 
n(110) + t(116) + .(46) + p(112) + d(100) + f(102) = 1341
Hash = 1341 mod 256 = 77

Directly access bucket 77:
Bucket 77 entries: ["project.pdf", "assignment.pdf", "notes.txt"]

Search within bucket: 3 comparisons
```

The average case requires O(1) access time plus searching through the bucket's collision chain. With proper hash function design and adequate bucket count, collisions remain minimal, providing significantly better performance than linear lists.

### Example 3: Hierarchical Path Resolution

When a process requests file "/home/student/courses/cs101/assignment.pdf", the operating system performs the following steps:

```
1. Start at root directory (/)
2. Look up "home" in root → returns inode for /home
3. Navigate to /home directory
4. Look up "student" in /home → returns inode for /home/student
5. Navigate to /home/student directory
6. Look up "courses" → returns inode for /home/student/courses
7. Navigate to /home/student/courses directory
8. Look up "cs101" → returns inode for /home/student/courses/cs101
9. Navigate to /home/student/courses/cs101 directory
10. Look up "assignment.pdf" → returns inode with file metadata
11. Access file data using the inode's block pointers
```

Each directory lookup may involve linear search or more efficient structures depending on implementation. Modern file systems optimize frequently accessed directories using caching mechanisms to reduce disk I/O operations.

## Exam Tips

For DU semester examinations, remember these key points regarding directory implementation:

1. **Directory vs. File**: A directory is a special file containing metadata about other files, not the actual file data itself. Understanding this distinction is crucial for conceptual questions.

2. **Time Complexity Comparison**: Be prepared to compare different implementations. Linear lists provide O(n) search, while hash tables offer O(1) average case. Tree-based structures provide O(log n) performance for large directories.

3. **Path Resolution**: Understand how absolute paths (starting from root) and relative paths (starting from current directory) are processed. The kernel traverses each directory component sequentially.

4. **UNIX inode vs. FAT**: The inode approach stores metadata separately from directory entries, while FAT stores file metadata within directory entries. Each has distinct advantages regarding performance and flexibility.

5. **Directory Operations**: Memorize the fundamental operations—create, delete, search, list, rename—and understand how each interacts with the underlying implementation structure.

6. **Collision Handling**: For hash table implementations, know the difference between separate chaining and open addressing, including their respective advantages regarding insertion, deletion, and memory usage.

7. **Hierarchical Advantages**: Recognize why modern operating systems use tree-structured directories—improved organization, natural categorization, and support for multi-user environments with isolated namespaces.

8. **Name Length Limitations**: Directory entry structures impose maximum file name lengths. Understand how this constraint affects directory implementation design and compatibility between different file systems.