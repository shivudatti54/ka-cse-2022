# File Concept and Access Methods


## Table of Contents

- [File Concept and Access Methods](#file-concept-and-access-methods)
- [Introduction to Files](#introduction-to-files)
  - [File Attributes](#file-attributes)
- [File Operations](#file-operations)
- [File Access Methods](#file-access-methods)
  - [1. Sequential Access](#1-sequential-access)
  - [2. Direct Access (or Relative Access)](#2-direct-access-or-relative-access)
  - [3. Indexed Sequential Access Method (ISAM)](#3-indexed-sequential-access-method-isam)
- [Comparison of Access Methods](#comparison-of-access-methods)
- [Exam Tips](#exam-tips)

## Introduction to Files

In operating systems, a **file** is a logical collection of information stored on secondary storage (like a hard disk). Files are the fundamental unit of storage that the operating system manages. They provide a mechanism for storing data persistently, meaning the data remains intact even when the computer is powered off.

A file can contain various types of information: programs (executable code), text, images, videos, or any sequence of bits. From the operating system's perspective, a file is simply a sequence of bytes; the interpretation of those bytes is left to the application programs that use them.

### File Attributes

Each file is associated with a set of attributes, which are metadata about the file. These are typically stored in a structure called an **inode** (index node) in Unix-like systems or a **File Control Block (FCB)** in general. Key attributes include:

- **Name:** The human-readable identifier for the file.
- **Identifier:** A unique number (inode number) that identifies the file within the file system.
- **Type:** Needed for systems that support different file types (e.g., .txt, .exe).
- **Location:** A pointer to the location of the file on the secondary storage device.
- **Size:** The current size of the file, usually in bytes.
- **Protection:** Access-control information (read, write, execute permissions).
- **Timestamps:** Creation, last modification, and last access times.

```
+---------------------+
| File Name | -> "report.pdf"
+---------------------+
| Identifier | -> inode number 2567
+---------------------+
| Type | -> PDF document
+---------------------+
| Location | -> Pointer to disk blocks
+---------------------+
| Size | -> 1,542,890 bytes
+---------------------+
| Protection | -> rw- r-- r-- (owner:read/write, group:read, others:read)
+---------------------+
| Creation Time | -> 2023-10-26 14:30:02
+---------------------+
| Modification Time | -> 2023-10-27 09:15:44
+---------------------+
| Last Access Time | -> 2023-10-28 11:20:31
+---------------------+
 (File Attributes)
```

## File Operations

The operating system provides a set of system calls to manipulate files. These are the fundamental operations that can be performed on a file:

1. **Creating a file:** Allocates space for the file and creates an entry in the directory structure.
2. **Writing to a file:** Data is written to the file at a specified location (usually a write pointer is maintained).
3. **Reading from a file:** Data is read from the file, usually from the current location of a read pointer.
4. **Repositioning within a file (Seek):** Moves the current file pointer to a new location without reading or writing data. This is essential for non-sequential access.
5. **Deleting a file:** Deallocates the file's disk space and removes its directory entry.
6. **Truncating a file:** Erases the contents of a file but keeps its attributes. The file size is set to zero.

Other advanced operations include appending, renaming, and locking files for concurrent access control.

## File Access Methods

The method by which the records (or bytes) of a file are accessed is called the **file access method**. The access method is determined by the way information is to be used and stored. The three primary types are:

### 1. Sequential Access

This is the simplest and most common method. Data in the file is processed in order, one record after another. Most operating systems impose this model on all files.

**Analogy:** A magnetic tape. You must read through record 1, 2, ..., 999 to get to record 1000. You can't jump directly to record 1000.

**Operations:**

- `read next`: Read the next portion of the file and advance the pointer.
- `write next`: Write to the end of the file and advance the pointer.
- `rewind`: Reset the pointer to the beginning of the file.

**ASCII Diagram:**

```
Beginning of File End of File
 | |
 V V
+---------+---------+---------+---------+---------+---------+---------+-----+
| Record1 | Record2 | Record3 | .... | Recordn | Recordn+| Recordn+| ... |
+---------+---------+---------+---------+---------+---------+---------+-----+
 ^ ^
 | |
Read Pointer (starts here) Write Pointer (starts/ends here)
```

_Use Cases:_ Compiler reading source code, multimedia playback (music/video), reading log files.\*

### 2. Direct Access (or Relative Access)

This method allows records to be read or written in any arbitrary order. The file is viewed as a numbered sequence of blocks or records. The user can request to read block 14, then block 53, then block 7, without reading any blocks in between.

**Operations:**

- `read n`: Read block number `n`.
- `write n`: Write to block number `n`.
- `position to n`: Set the current pointer to block `n`.
- `read next` / `write next`: Read or write the next block relative to the current position.

**ASCII Diagram:**

```
File as an array of fixed-length blocks
+------+------+------+------+------+------+------+------+
| Blk0 | Blk1 | Blk2 | Blk3 | Blk4 | Blk5 | Blk6 | Blk7 | ...
+------+------+------+------+------+------+------+------+

User can directly request any block, e.g., "read 5", then "read 2", then "write 6".
```

_Use Cases: Databases, modern file systems (for user files), rapid data retrieval applications._

### 3. Indexed Sequential Access Method (ISAM)

This is a sophisticated method that builds an index on top of a sequentially organized file. The index contains pointers to various blocks in the data file, allowing for efficient direct access to records via a key (e.g., a student ID number). It combines the benefits of both sequential and direct access.

**How it works:**

1. The main data file is stored sequentially.
2. A separate, smaller index file is created. This index holds a key field and a pointer to the corresponding record in the main file.
3. To find a record, the system first searches the index (which is faster, often sorted). Once the correct index entry is found, it uses the pointer to directly access the record in the data file.

**ASCII Diagram:**

```
INDEX FILE (Sorted by Key) MAIN DATA FILE (Sequential)
+------------+-------------+ +-----------------------------+
| Key (e.g., | Pointer to | | Record with key=101 | Data |
| ID) | Data Record | +-----------------------------+
+------------+-------------+ | Record with key=105 | Data |
| 101 | -> |---------+ +-----------------------------+
+------------+-------------+ | | Record with key=110 | Data |
| 105 | -> |---------+| +-----------------------------+
+------------+-------------+ || | Record with key=120 | Data |
| 110 | -> |---------+|+->-----------------------------+
+------------+-------------+ |
| 120 | -> |---------+
+------------+-------------+
```

_Use Cases: Large databases where records are frequently accessed by a key field (e.g., customer ID, product code)._

## Comparison of Access Methods

| Feature                | Sequential Access                   | Direct Access                 | Indexed Sequential Access (ISAM)       |
| ---------------------- | ----------------------------------- | ----------------------------- | -------------------------------------- |
| **Access Pattern**     | In order, from start to finish      | Any order, by block number    | Any order, by a key field              |
| **Speed**              | Slow for random access              | Very fast for random access   | Fast for access by key                 |
| **Storage Overhead**   | Low                                 | Low                           | High (requires extra space for index)  |
| **Complexity**         | Simple                              | Simple                        | Complex                                |
| **Best For**           | Tape drives, streaming data         | Modern disks, databases       | Large databases requiring keyed access |
| **Example Operations** | `read next`, `write next`, `rewind` | `read n`, `write n`, `seek n` | `find Record(key)`, `read next`        |

## Exam Tips

- **Understand the Core Concept:** Be able to define a file and its key attributes (name, identifier, size, etc.). This is a common short-answer question.
- **Contrast the Methods:** You will almost certainly be asked to compare and contrast sequential, direct, and indexed access methods. Use a table in your answer for clarity.
- **Think Practically:** Relate each access method to a real-world device or application (e.g., sequential for tapes, direct for SSDs/HDDs, indexed for databases).
- **Operation Knowledge:** Know which system calls or operations are associated with each access method (e.g., `seek()` is crucial for direct access).
- **ISAM is a Hybrid:** Remember that ISAM is not a separate fundamental method but an implementation that uses an index to provide direct access to a sequentially stored file. Be prepared to explain the role of the index.
