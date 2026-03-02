# File System

## Introduction

A file system is a fundamental component of any operating system that provides the mechanism for storing, organizing, and retrieving data on secondary storage devices such as hard disks, solid-state drives, and USB drives. The file system serves as an abstraction layer between applications and the physical hardware, allowing users and programs to interact with data using logical names and structures rather than dealing with raw disk sectors and physical addresses.

The importance of file systems in modern computing cannot be overstated. Every piece of data stored on a computer, from a simple text document to complex database applications, is managed by the file system. File systems determine how efficiently data is stored and accessed, how files are protected from unauthorized access, and how multiple users can share data securely. In the context of the University of Delhi's Computer Science curriculum, understanding file systems is essential for comprehending how operating systems manage resources and provide services to user applications.

This topic covers the theoretical foundations and practical implementations of file systems, including the file concept, access methods, directory structures, and various allocation techniques used to manage disk space effectively.

## Key Concepts

### File Concept

A file is the basic unit of data storage in a computer system. From the user's perspective, a file is a named collection of related information that can be created, modified, deleted, and accessed. From the operating system's perspective, a file is an abstract data type that provides a logical view of storage while hiding the physical details of how data is actually stored on disk.

Files possess several attributes that describe their characteristics:

NAME: Every file has a symbolic filename that identifies it within a given directory. Filenames typically consist of a base name and an extension that indicates the file type.

IDENTIFIER: The system assigns a unique internal identifier (usually a number) to each file to distinguish it from all other files, even if multiple files share the same name in different directories.

TYPE: Files can be of various types including regular files (containing user data), directory files (containing file references), special files (representing devices), and others.

LOCATION: A pointer to the physical location of the file on the storage device.

SIZE: The current size of the file in bytes.

PROTECTION: Access control information specifying who can read, write, or execute the file.

TIMESTAMP: Information about creation time, last modification time, and last access time.

### File System Structure

A file system is organized in a hierarchical structure consisting of multiple levels of abstraction. The boot block contains the initial bootstrap program that loads the operating system. The superblock holds metadata about the file system including its size, free block count, and inode table information. The inode table contains file metadata structures called inodes, where each inode stores attributes and block pointers for one file. The data blocks constitute the actual file content storage area.

The directory structure provides the namespace for organizing files. Modern file systems use hierarchical directories (folders) that allow users to create a tree-like organization of files. Each directory entry maps a filename to its corresponding inode number, enabling efficient file lookup and management.

### Access Methods

Operating systems provide various methods for accessing file data, each suited to different usage patterns and performance requirements:

SEQUENTIAL ACCESS: This is the simplest access method where data is read or written in sequential order, starting from the beginning of the file. The system maintains a file pointer that advances through the file as operations are performed. Sequential access is efficient for processing large amounts of data in order and is commonly used in batch processing and log file operations.

DIRECT ACCESS (RANDOM ACCESS): This method allows any record in the file to be accessed directly without first reading preceding records. The file is viewed as a sequence of numbered blocks, and the system can seek to any block immediately using its block number. Direct access is essential for database systems and applications requiring frequent random access to specific data locations.

INDEXED ACCESS: This method uses an index structure to improve access speed. An index file contains pointers to the actual data blocks, allowing the system to locate data more quickly than sequential or direct methods alone. For large files, multiple levels of indexing may be used to create a tree-like structure that provides efficient search capabilities.

### Directory Structure

The directory structure defines how files are organized and accessed within the file system. Several directory organization schemes exist:

SINGLE-LEVEL DIRECTORY: The simplest structure where all files reside in a single directory. While easy to implement, this approach creates naming conflicts and cannot scale beyond a small number of files.

TWO-LEVEL DIRECTORY: Introduces a separate directory for each user, solving the naming conflict problem but still limiting organizational flexibility.

TREE-STRUCTURED DIRECTORY: A hierarchical organization allowing unlimited depth in file categorization. This is the most common structure in modern operating systems, enabling logical grouping of related files into directories and subdirectories.

Acyclic-Graph Directory: Allows directories to share subdirectories and files, creating a directed acyclic graph structure. This provides flexibility in file sharing but requires careful handling to avoid circular references.

General-Graph Directory: Permits cycles in the directory structure, offering maximum flexibility but requiring sophisticated algorithms to prevent infinite loops during directory traversal.

## Examples

### Example 1: Sequential File Access

Consider a log file "system.log" containing timestamped events. To process all events sequentially:

```
Initialize file pointer to beginning
WHILE NOT end-of-file:
    Read next line from file
    Process the event timestamp
    Move file pointer forward
END WHILE
Close file
```

If the file contains 1000 lines and each line is 80 bytes, reading all records sequentially requires 80,000 byte reads. The file pointer automatically advances after each read operation, making this access method highly efficient for processing complete files.

### Example 2: Direct Access for Database Operations

A banking application needs to access account records directly using account numbers. If each account record is 512 bytes and account numbers range from 1 to 10,000:

To access account number 5000:
- Calculate byte offset: (5000 - 1) × 512 = 2,559,488 bytes
- Seek directly to this offset using the seek operation
- Read the 512-byte record containing account information

This direct access method allows the system to retrieve any account in constant time, O(1), regardless of the total number of accounts, making it ideal for transaction processing systems.

### Example 3: File Allocation Methods

Consider a disk with 1000 blocks. If a file requires 50 blocks, different allocation methods yield different results:

CONTIGUOUS ALLOCATION: Allocate blocks 100-149 consecutively. This provides excellent read performance (single seek operation) but suffers from external fragmentation and difficulty in expanding the file.

LINKED ALLOCATION: Distribute the 50 blocks randomly across the disk, with each block containing a pointer to the next block. This eliminates external fragmentation but results in poor random access performance since each block access may require a separate disk seek.

INDEXED ALLOCATION: Create an index block containing pointers to all 50 data blocks. The file's inode points to this index block, allowing all 50 block locations to be known immediately. This combines good random access capability with efficient sequential reading.

## Exam Tips

Understanding file systems is crucial for operating system examinations. Here are key points to remember:

1. Know the difference between file attributes and file types. File attributes include name, identifier, location, size, protection, and timestamps, while types include regular files, directories, and special files.

2. Remember that sequential access uses a file pointer that advances automatically, while direct access allows seeking to any block number directly using the seek operation.

3. Understand why indexed allocation is preferred over linked allocation in modern file systems: indexed allocation provides both random and sequential access efficiency without the reliability issues of linked lists.

4. The hierarchical directory structure is the most commonly used organization in contemporary operating systems due to its flexibility and intuitive nature.

5. Be able to calculate file access times for different allocation methods. Contiguous allocation offers the fastest access times, while linked allocation has the slowest due to multiple disk seeks.

6. Remember that the superblock contains critical file system metadata including total disk size, free space information, and inode table location.

7. Understand the trade-offs between different directory structures: single-level is simple but inflexible, while general-graph offers maximum flexibility but requires cycle-detection algorithms.

8. File system mounting allows multiple file systems to be integrated into a single hierarchical namespace, which is essential for modern operating systems with multiple storage devices.