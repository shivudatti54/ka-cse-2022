# Directory Implementation

## Introduction

Directory implementation is a fundamental aspect of file system design in operating systems. A directory is a data structure that maps file names to their associated metadata and disk locations, enabling users and applications to organize, locate, and manage files efficiently. Without directories, users would need to memorize exact disk addresses for every file, making file management virtually impossible. The way directories are implemented directly impacts file system performance, storage efficiency, and the operations supported by the file system.

In the context of University of Delhi's Computer Science curriculum, understanding directory implementation is essential for comprehending how modern operating systems manage secondary storage. This topic builds upon the foundational concepts of file systems and introduces the practical mechanisms that operating systems employ to maintain hierarchical file organizations. The implementation choices made by system designers affect everything from simple operations like creating a new file to complex tasks like maintaining security permissions and tracking file sharing across multiple users.

Directory implementation serves as the bridge between the logical view of files that users interact with and the physical reality of data stored on disk. When you create, delete, or search for a file, the directory implementation determines how quickly these operations complete and what resources they consume. Understanding these implementation details prepares you to evaluate file system designs critically and make informed decisions in system programming and administration roles.

## Key Concepts

### Linear List Implementation

The simplest approach to directory implementation uses a linear list (or unordered list) to store directory entries. Each entry contains the file name, file attributes, and a pointer to the file's data blocks. When searching for a file, the system must traverse the list sequentially until a matching file name is found. This implementation is straightforward to understand and code, making it a common choice in early file systems and educational contexts.

The primary advantage of linear list implementation is its simplicity. Adding a new file entry involves simply appending to the end of the list, which is an O(1) operation. However, file lookup operations require scanning through the list, resulting in O(n) time complexity where n represents the number of files in the directory. In directories containing thousands of files, this linear search becomes a significant performance bottleneck. Additionally, deleting a file requires either marking the entry as available or shifting subsequent entries to fill the gap, both of which have implementation complexities.

Modern operating systems rarely use pure linear lists for large directories due to performance concerns. However, this approach remains relevant in scenarios where directories contain very few files or where implementation simplicity is prioritized over performance. Understanding this basic implementation also provides a foundation for appreciating more sophisticated techniques.

### Hash Table Implementation

Hash table-based directory implementation addresses the performance limitations of linear lists by providing faster file lookup operations. In this approach, a hash function computes an index into the directory based on the file name. The hash function maps file names to bucket locations, allowing direct access to potential file entries rather than requiring a complete search. This reduces average-case lookup time to O(1), making it significantly faster for directories with many files.

When implementing a hash table directory, the system must handle hash collisions—situations where different file names produce the same hash value. Several collision resolution techniques exist, including chaining (where each bucket contains a linked list of entries) and open addressing (where the system searches for alternative slots when a collision occurs). The choice of hash function and collision resolution strategy significantly impacts overall directory performance.

Hash table implementations require additional overhead for maintaining the hash structure itself. The system must allocate space for the hash table, manage collision chains, and handle table resizing when directories grow beyond initial capacity estimates. Despite these complexities, the performance benefits make hash tables the preferred choice for directories that may contain hundreds or thousands of files.

### Directory Entry Structure

A directory entry contains all information needed to identify and manage a file. The exact structure varies between file systems, but most include the following components: the file name (typically limited to a fixed maximum length), file attributes (such as read-only, hidden, system flags), timestamps (creation, modification, access times), owner and group identifiers, access permissions, and pointers to file data blocks or index nodes.

In UNIX-like systems, directory entries are remarkably simple—they contain only the file name and an inode number. The inode (index node) is a separate data structure that holds all file attributes and pointers to data blocks. This separation allows multiple directory entries to reference the same inode, implementing hard links efficiently. When the system needs file information, it first reads the directory entry to obtain the inode number, then accesses the inode to retrieve complete file metadata.

Windows FAT file systems use a different approach, storing file attributes directly in directory entries without a separate inode structure. Each directory entry contains the file name, starting cluster number, file size, and various attribute flags. This monolithic approach simplifies some operations but makes implementing advanced features like hard links more difficult.

### Directory Operations

Operating systems provide a set of primitive operations for manipulating directories. These typically include creating a new directory (mkdir), removing an existing directory (rmdir), reading directory contents (ls or dir), searching for specific files within a directory, renaming files or directories, and navigating the directory hierarchy (changing the current working directory).

The implementation of these operations varies based on the underlying directory structure. Creating a directory involves allocating space for the directory entry, initializing the directory's contents (including the special entries for "." and ".."), and updating parent directory structures. Deleting a directory requires checking that the directory is empty (or handling recursive deletion), removing all associated entries, and releasing allocated space.

Modern file systems support additional operations beyond these basics. Hard links allow multiple directory entries to reference the same file, while symbolic links create special file entries that point to other path names. Access control lists (ACLs) provide fine-grained permission management beyond the traditional UNIX permission model. The directory implementation must support all these operations efficiently while maintaining data consistency.

### Hierarchical Directory Structures

Most modern operating systems implement hierarchical (tree-structured) directory systems, allowing users to organize files in nested directories (also called folders). This hierarchical structure provides natural categorization capabilities, enabling users to group related files together and establish logical organization schemes that mirror real-world filing systems.

The implementation of hierarchical directories requires tracking parent-child relationships between directories. Each directory contains special entries "." (referring to itself) and ".." (referring to its parent), enabling navigation up and down the directory tree. Path name resolution—the process of converting a textual path like "/home/student/documents/report.txt" into a specific directory entry—involves parsing the path components and following the directory relationships sequentially.

The root directory serves as the starting point for all absolute paths in the system. Operating systems maintain a pointer to the root directory and use it for resolving paths that begin with the path separator character. Relative paths are resolved starting from the current working directory, which each process maintains individually, allowing different processes to operate in different parts of the file system simultaneously.

## Examples

### Example 1: Linear Search in a Directory

Consider a directory containing 1000 files, and we need to locate a file named "assignment.pdf". With linear list implementation, the worst-case scenario requires examining all 1000 entries sequentially:

```
function findFileLinear(directory, targetName):
    for each entry in directory:
        if entry.name == targetName:
            return entry  // Found after up to 1000 comparisons
    
    return NOT_FOUND  // File does not exist
```

If the average position of a file is halfway through the directory, we perform approximately 500 comparisons. Assuming each comparison takes 1 microsecond due to string comparison overhead and potential disk I/O, the average search time is 500 microseconds or 0.5 milliseconds. In contrast, a hash table implementation with 1000 buckets would typically complete the same search in constant time, regardless of file position.

This example illustrates why linear list implementations become problematic as directories grow. In early computer systems with limited storage and small directories, linear search was acceptable. Modern systems with millions of files require more sophisticated approaches.

### Example 2: Hash Table Directory Operations

Suppose we implement a hash table directory with 256 buckets and use a simple hash function that sums character values modulo 256:

```
function hashFunction(fileName):
    sum = 0
    for each character in fileName:
        sum = sum + ASCII value of character
    return sum mod 256

function insertEntry(directory, fileName, metadata):
    bucketIndex = hashFunction(fileName)
    bucket = directory.buckets[bucketIndex]
    
    // Check for existing entry with same name
    for each entry in bucket:
        if entry.name == fileName:
            entry.metadata = metadata  // Update existing
            return
    
    // Add new entry to bucket
    newEntry = {name: fileName, metadata: metadata}
    bucket.append(newEntry)
```

When inserting 1000 files with varied names, the hash function distributes them across buckets. If names are reasonably random, each bucket contains approximately 4 entries on average (1000/256). Searching or inserting requires examining only these 4 entries, dramatically reducing operation time compared to the linear approach.

The effectiveness of hash table implementation depends heavily on the hash function quality. A poor hash function that clusters many files into the same buckets degenerates to linear search performance. Good hash functions produce uniform distribution across buckets, maintaining O(1) average performance.

### Example 3: Path Resolution in Hierarchical Directory

Consider resolving the absolute path "/usr/local/bin/python". The operating system performs the following steps:

1. Begin at the root directory (stored as system-wide reference)
2. Look up "usr" in root directory → obtains inode for /usr
3. Navigate to /usr directory, look up "local" → obtains inode for /usr/local
4. Navigate to /usr/local directory, look up "bin" → obtains inode for /usr/local/bin
5. Navigate to /usr/local/bin directory, look up "python" → obtains final file entry

Each component lookup requires a directory search. If each lookup uses hash table with 1000 buckets and finds entries in the first bucket examined, path resolution completes in 5 hash table operations. With linear lists containing 1000 files each, the same resolution could require 5000 file name comparisons, significantly impacting performance for deeply nested paths.

Operating systems optimize path resolution through caching. The system maintains a directory entry cache (dentry cache in Linux) that stores recently resolved path components, avoiding repeated disk accesses and lookup operations for frequently accessed paths.

## Exam Tips

For DU semester examinations, focus on the following key areas:

1. UNDERSTAND THE TRADE-OFFS between linear list and hash table implementations. Linear lists offer simple implementation but poor performance for large directories, while hash tables provide fast lookup but require additional overhead for collision handling.

2. MEMORIZE THE COMPLEXITY DIFFERENCES: Linear list search is O(n), insertion is O(1), and deletion is O(n). Hash table operations average O(1) but worst-case O(n) when collisions are excessive.

3. KNOW THE COMPONENTS of a directory entry—file name, file attributes, data block pointers, owner information, and timestamps. Be prepared to draw and explain a directory entry structure diagram.

4. UNDERSTAND PATH RESOLUTION PROCESS—know how the operating system navigates from root or current directory through each path component to locate a file.

5. DISTINGUISH BETWEEN HARD LINKS AND SYMBOLIC LINKS in terms of directory implementation. Hard links share the same inode, while symbolic links contain a path name that the system must resolve.

6. BE FAMILIAR WITH DIRECTORY OPERATIONS—create, delete, rename, list, and search. Know what each operation involves in terms of directory structure modifications.

7. UNDERSTAND WHY DIRECTORY IMPLEMENTATION MATTERS for file system performance. The choice of directory structure affects every file access operation in the system.

8. KNOW THE SPECIAL ENTRIES "." and ".." in hierarchical directories and understand their roles in navigation and path resolution.