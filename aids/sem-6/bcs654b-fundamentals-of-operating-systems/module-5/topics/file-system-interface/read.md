# File System Interface


## Table of Contents

- [File System Interface](#file-system-interface)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [File Concept](#file-concept)
  - [File Access Methods](#file-access-methods)
  - [File Operations](#file-operations)
  - [Directory Structure](#directory-structure)
  - [Protection Mechanisms](#protection-mechanisms)
- [Examples](#examples)
  - [Example 1: Sequential File Processing](#example-1-sequential-file-processing)
  - [Example 2: Random Access File Processing](#example-2-random-access-file-processing)
  - [Example 3: File Metadata Operations](#example-3-file-metadata-operations)
- [Exam Tips](#exam-tips)

## Introduction

The File System Interface is the layer of the operating system that provides the abstraction of persistent storage to users and applications. It serves as the bridge between the user view of data stored in files and the physical implementation of that data on storage devices. The file system interface defines how files are named, accessed, protected, and managed, creating an illusion of simple linear or direct data storage despite the complex underlying hardware architecture.

Operating systems provide two distinct perspectives on the file system: the user's view and the system's view. From the user's perspective, files appear as named collections of related information that can be created, deleted, opened, and modified. From the system's perspective, the file system must handle complex tasks including space allocation, directory management, and ensuring data integrity. The interface abstracts these complexities, allowing users to interact with files using high-level operations without concern for the physical details of storage media.

The importance of a well-designed file system interface cannot be overstated in modern computing. It enables data persistence across system reboots, facilitates sharing of data between processes and users, and provides protection against unauthorized access. Understanding the file system interface is essential for both system programmers who implement file operations and application developers who utilize these operations in their software.

## Key Concepts

### File Concept

A file is the fundamental unit of data storage in any operating system. From the user's perspective, a file represents a collection of logically related information that can be referenced by a name. Files can contain various types of data including text documents, images, executable programs, or any other form of information that needs to be stored persistently. The operating system treats each file as a linear array of bytes, with the internal structure and meaning of the data being determined by the application that creates or uses the file.

Files possess several essential attributes that define their characteristics and state:

- **Name**: A unique identifier that allows users to reference the file
- **Identifier**: An internal, unique number (inode number in Unix systems) that identifies the file within the file system
- **Type**: Indicates the file format and contents (regular file, directory, special file, etc.)
- **Location**: A pointer to the physical location of the file's data on the storage device
- **Size**: The current amount of data in the file, typically measured in bytes
- **Protection**: Access control information specifying who can read, write, or execute the file
- **Timestamps**: Information about creation time, last modification time, and last access time
- **Owner**: The user or process that owns the file and has primary control over it

### File Access Methods

The file system interface supports multiple methods for accessing file data, each suited to different usage patterns and performance requirements.

**Sequential Access** is the simplest and most common access method. In this method, files are processed from the beginning to the end, with data being read or written in a sequential manner. Operations typically involve reading the next n records or writing the next n records, with the file pointer automatically advancing after each operation. This method is ideal for batch processing and applications that naturally process data in order, such as log files or transaction records. The operations supported are typically `read next`, `write next`, and `reset` to return to the beginning.

**Direct Access** (also known as random access) allows files to be read or written in any arbitrary order without sequential processing. This method treats the file as a numbered sequence of fixed-size blocks, enabling applications to directly access any block by its number. The `seek` operation is used to position the file pointer to a specific block number before performing read or write operations. Direct access is essential for database systems and applications requiring fast access to specific data items, such as airline reservation systems or inventory management applications.

**Indexed Access** provides an additional level of abstraction by maintaining an index structure that maps keys or offsets to physical block locations. This method combines the benefits of direct access with more efficient searching capabilities, particularly for large files. The system maintains one or more index blocks that contain pointers to the actual data blocks, allowing applications to locate specific records without scanning the entire file.

### File Operations

The file system interface provides a set of primitive operations that form the foundation for all file manipulations:

**Create**: Establishes a new file with a specified name and initial attributes. The system allocates necessary directory structure and prepares space for file metadata.

**Delete**: Removes a file from the file system, releasing all allocated space and removing the file's entry from the parent directory.

**Open**: Prepares a file for access by checking permissions, loading file metadata into memory, and creating a file descriptor or handle that the process will use for subsequent operations. The open operation returns a reference that must be used in all subsequent operations on that file.

**Close**: Terminates access to an open file, updating metadata such as timestamps and size, flushing any buffered data to disk, and releasing system resources associated with the file descriptor.

**Read**: Retrieves data from an open file, starting from the current file position. The operation transfers a specified number of bytes from the file to the application's buffer.

**Write**: Transfers data from an application's buffer to an open file, starting from the current file position. The operation may extend the file size if data is written beyond the current end of file.

**Seek**: Repositions the file pointer to a specific location within an open file, enabling random access to any position within the file.

**Truncate**: Reduces the size of a file to a specified length, discarding any data beyond the new end of file.

**Get Attributes** and **Set Attributes**: Retrieve or modify the metadata associated with a file, such as permissions, timestamps, or ownership information.

### Directory Structure

Directories provide the hierarchical organization mechanism for files within the file system. The directory structure defines how files are named, organized, and accessed within the system. Common directory implementations include:

**Single-Level Directory**: All files exist in a single directory, providing simplicity but leading to naming conflicts as files cannot share names.

**Two-Level Directory**: Separate directories for each user, preventing naming conflicts between users while maintaining simplicity.

**Hierarchical Directory**: A tree-structured organization allowing logical grouping of related files into subdirectories. This is the most common structure in modern operating systems.

**Acyclic Graph Directory**: Allows directories to share subtrees, enabling multiple paths to reference the same file or directory while preventing cycles that would complicate traversal.

### Protection Mechanisms

The file system interface incorporates protection mechanisms to control access to files and directories. These mechanisms ensure that only authorized users can perform specific operations on protected resources.

**Access Control Lists (ACL)** specify exactly which users or groups can perform which operations on a file. Each file maintains a list of permissions associated with specific users or groups, providing fine-grained control over file access.

**Permission Bits** provide a simpler protection mechanism, typically with three sets of permissions (owner, group, and others) and three types of access (read, write, execute). Unix-like systems use this model with permissions represented as rwxr-xr-x notation.

**Password Protection** requires users to provide authentication before gaining access to protected files or directories, though this method is less commonly used in modern systems.

## Examples

### Example 1: Sequential File Processing

Consider a program that processes a transaction log file sequentially to generate a daily summary:

```c
FILE *logFile;
char buffer[256];

// Open file in read mode
logFile = fopen("transactions.log", "r");

if (logFile == NULL) {
 printf("Error opening file\n");
 return 1;
}

// Sequential access - read line by line
while (fgets(buffer, sizeof(buffer), logFile) != NULL) {
 processTransaction(buffer);
}

// Close the file
fclose(logFile);
```

In this example, the file is opened once and processed sequentially from beginning to end. The file pointer automatically advances with each read operation. This pattern is efficient for processing data in order and represents the most common use case for file operations.

### Example 2: Random Access File Processing

Consider a database application that needs to update specific records in a fixed-length record file:

```c
#define RECORD_SIZE 100

// Open file for read and write
int fileDesc = open("database.dat", O_RDWR);

if (fileDesc == -1) {
 perror("Error opening file");
 return 1;
}

// Update record at position 5 (6th record)
int recordNumber = 5;
char record[RECORD_SIZE];

// Seek to the beginning of record 5
lseek(fileDesc, recordNumber * RECORD_SIZE, SEEK_SET);

// Read existing record
read(fileDesc, record, RECORD_SIZE);

// Modify the record
modifyRecord(record);

// Seek back to same position (read moved the pointer)
lseek(fileDesc, recordNumber * RECORD_SIZE, SEEK_SET);

// Write updated record
write(fileDesc, record, RECORD_SIZE);

close(fileDesc);
```

This example demonstrates direct access where any record can be accessed directly by computing its offset. The `lseek` operation positions the file pointer to the exact byte location of the desired record, enabling efficient random access without processing preceding records.

### Example 3: File Metadata Operations

Consider a backup application that needs to copy files while preserving their attributes:

```c
struct stat fileStat;

if (stat("source.txt", &fileStat) == 0) {
 printf("File Size: %ld bytes\n", fileStat.st_size);
 printf("Permissions: %o\n", fileStat.st_mode);
 printf("Last Modified: %s", ctime(&fileStat.st_mtime));
 printf("Last Accessed: %s", ctime(&fileStat.st_atime));

 // Preserve permissions when copying
 chmod("destination.txt", fileStat.st_mode);
}
```

This example shows how to query and manipulate file attributes using system calls. The `stat` function retrieves complete metadata about a file, which can then be used to make decisions about file handling or to preserve attributes when copying files.

## Exam Tips

1. **Distinguish between file attributes and file operations**: Remember that attributes describe the file itself (name, size, permissions), while operations are actions performed on files (read, write, open, close).

2. **Understand the relationship between open and close**: The open operation creates a file descriptor and loads metadata into memory, while close releases these resources. Failing to close files can lead to resource leaks.

3. **Know when to use sequential vs. direct access**: Sequential access is appropriate for batch processing and streaming data; direct access is necessary for database systems and applications requiring random access to specific records.

4. **Remember that file pointers are per-process**: Each process maintains its own file position pointer, so opening the same file multiple times creates separate file descriptors with independent positions.

5. **Understand the difference between delete and truncate**: Delete removes the file entirely from the file system, while truncate merely reduces the file size to zero or a specified length, preserving the file.

6. **Protection mechanisms may use different approaches**: ACLs provide fine-grained control with specific permissions for each user, while permission bits provide simpler coarse-grained control based on owner, group, and others.

7. **File systems treat files as byte arrays**: The internal structure of file data is determined by applications, not the operating system. The OS simply treats all files as sequences of bytes.

8. **Directory operations are distinct from file operations**: Directories are themselves special files that maintain mappings between file names and their internal identifiers. Operations like mkdir, rmdir, and readdir are specific to directories.
