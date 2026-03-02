# File System Concepts

## 1. Introduction to Files

A **file** represents the fundamental abstraction for persistent storage in computer systems. Formally defined, a file is a named collection of logically related information stored on secondary storage devices (such as hard disks, solid-state drives, or magnetic tapes). The operating system provides file-oriented interfaces that enable applications to store and retrieve data without requiring knowledge of the underlying physical storage mechanisms.

Files serve as the primary mechanism for data persistence across program executions, allowing information to outlive the processes that created them. The file system, as the component responsible for file management, provides essential services including file creation, deletion, naming, organization, and protection.

## 2. File Attributes

Every file maintains a collection of metadata known as **file attributes**, which describe various characteristics of the file. This metadata is essential for effective file management and access control.

| Attribute | Description | Implementation |
|-----------|-------------|----------------|
| **Name** | Human-readable identifier; follows naming conventions (case-sensitive in Unix, case-insensitive in Windows) | String stored in directory entry |
| **Identifier** | Unique system-assigned identifier (inode number in Unix, MFT entry in Windows NTFS) | Integer value |
| **Type** | File format indicating content organization (text, binary, executable, directory) | Enum or magic bytes |
| **Location** | Pointer(s) to physical storage blocks on disk | Block addresses in FCB/inode |
| **Size** | Current file length measured in bytes; may include allocated but unused blocks | Integer (file length) |
| **Protection** | Access control permissions specifying read/write/execute rights for owner, group, and others | Bitmask (rwxr-xr-x) |
| **Timestamps** | Three temporal attributes: creation time, modification time, and access time | UNIX timestamps |

The collection of file attributes is stored in a data structure called the **File Control Block (FCB)** in traditional file systems, or an **inode** in Unix-like systems. This structure is typically maintained in memory when the file is open and persisted on disk as part of the file system metadata.

## 3. File Operations

The operating system provides a set of primitive operations that applications can perform on files. These operations map to system calls that transition from user mode to kernel mode.

### 3.1 Primitive File Operations

1. **Create**: Allocates disk space for file data, creates a directory entry, and initializes the file control block with default attributes and empty content.

2. **Open**: Locates the file by name in the directory structure, loads the file control block into memory, allocates a file descriptor in the per-process open file table, and returns the descriptor to the calling process.

3. **Read**: Transfers a specified number of bytes from the file's current position to a user-space buffer, advancing the read pointer accordingly. May involve buffering and caching mechanisms.

4. **Write**: Transfers data from user memory to the file, allocating additional disk blocks as necessary and updating file size. Write operations may be synchronous (immediate disk persistence) or asynchronous (buffered).

5. **Seek (Lseek)**: Repositions the read/write pointer to a specified offset within the file, enabling random access patterns. Returns the new pointer position.

6. **Close**: Decrements the open file reference count, removes the file descriptor from the process's table, and writes modified metadata back to disk if necessary. When reference count reaches zero, system-wide table entry is freed.

7. **Delete**: Removes the directory entry and marks all allocated blocks as free in the file system's allocation bitmap.

### 3.2 Derived Operations

Additional operations implemented through combinations of primitives include:
- **Append**: Seek to end-of-file followed by write
- **Truncate**: Set file size to zero while preserving attributes
- **Rename**: Modify directory entry without changing file content

## 4. File Access Methods

The method selected for file access significantly impacts performance and is determined by the access patterns and storage medium characteristics.

### 4.1 Sequential Access

Sequential access is the simplest method, where file records are processed in order from beginning to end. The file maintains a **current position pointer** that advances with each read operation.

```
Algorithm: Sequential Read
1. Check if current position < file length
2. Read block at current position
3. Advance position by number of bytes read
4. Return data to caller
```

**Characteristics:**
- Ideal for batch processing, log files, and streaming data
- Minimizes disk seek operations when reading consecutive blocks
- Supported by all storage devices including magnetic tape
- Example applications: text editors, compilers, log processors

### 4.2 Direct (Random) Access

Direct access permits reading or writing at any arbitrary position within the file without sequential progression. This requires the file to be organized as a collection of fixed-size **records** or **blocks** that can be directly addressed.

```
Algorithm: Direct Read(record_number)
1. offset ← record_number × record_size
2. Seek to offset
3. Read record_size bytes
4. Return data
```

**Characteristics:**
- Essential for database management systems requiring indexed access
- Enables efficient implementation of search algorithms
- Requires knowledge of record structure
- Performance dependent on block size selection

### 4.3 Indexed Access

Indexed access combines an **index structure** (typically a B-tree or hash table) with direct access methods. The index stores key-to-location mappings, allowing efficient lookup operations.

```
Algorithm: Indexed Read(key)
1. Search index for key
2. Retrieve block pointer from index entry
3. Seek to block location
4. Read and return record
```

**Characteristics:**
- Supports complex queries and multiple access paths
- Requires additional storage for index structures
- Common in database systems (ISAM, indexed files)
- Index maintenance overhead on updates

## 5. File Types

### 5.1 Classification by Content

- **Regular Files**: Contain user data in either text (ASCII, UTF-8, UTF-16) or binary format. Binary files follow specific format conventions (ELF executables, JPEG images, PDF documents).
- **Directories**: Special file types that maintain mappings between file names and inode numbers, establishing the hierarchical file system organization.
- **Special Files**: Device files (character device, block device) and named pipes providing interface to I/O devices and inter-process communication.

### 5.2 Classification by Extension

| Extension | File Type | Internal Format |
|-----------|-----------|-----------------|
| .txt, .log | Plain text | ASCII/UTF-8 characters |
| .c, .py, .java | Source code | Language-specific syntax |
| .pdf | Document | PDF structure |
| .jpg, .png | Image | JPEG/PNG compression |
| .mp3, .mp4 | Multimedia | Audio/video encoding |
| .out, .exe | Executable | Machine instructions |

## 6. File Structure

File structure defines the internal organization of data within a file, determining how records or bytes are arranged.

- **Unstructured (Byte Sequence)**: Unix philosophy treats files as uninterpreted byte arrays. The file system imposes no structure; interpretation is solely the responsibility of application software. This provides maximum flexibility.
- **Simple Record Structure**: Files contain records of fixed or variable length. Fixed-length records simplify random access; variable-length records require delimiter-based or length-prefixed parsing.
- **Complex Structures**: Database files employ sophisticated organization including B-tree indices, heap files, and hashed files to optimize query performance.

## 7. Open File Table Structure

When a process opens a file, the operating system creates entries in two distinct tables:

### 7.1 Per-Process Open File Table
- **File Descriptor**: Integer index in the process's file descriptor table
- **Access Mode**: Read-only, write-only, or read-write
- **Current Position**: Read/write pointer offset within file
- **Pointer to System-Wide Entry**: Reference to shared system table

### 7.2 System-Wide Open File Table
- **Open Count**: Number of processes currently with this file open
- **Disk Location**: Pointer to file control block/inode
- **Access Permissions**: Original permissions at open time
- **Synchronization**: Locks, flags for O_SYNC, O_APPEND

This dual-table design enables file sharing between processes while maintaining per-process state. The **fork()** operation demonstrates this: child inherits parent's file descriptors, causing both processes to share system-wide entries (open count incremented).