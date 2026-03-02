# File System Structure

## Introduction

File systems provide an efficient and convenient mechanism for storing, retrieving, and managing data on secondary storage (hard disks, SSDs). The file system must solve two fundamental design problems:

1. **How the file system should look to the user** -- defining files, attributes, operations, and directory structure
2. **How to map the logical file system onto physical storage devices** -- using algorithms and data structures

To manage this complexity, file systems are organized as a series of **layers**, where each layer uses the features of lower layers to create new features for higher layers. This layered design reduces complexity and redundancy.

---

## Layered File System Architecture

The file system is implemented in a layered structure, where each layer handles a specific responsibility:

```
┌─────────────────────────────────────────────────┐
│ Application Programs │
│ (user programs, shell, editors) │
├─────────────────────────────────────────────────┤
│ Logical File System │
│ (metadata, protection, FCB management) │
├─────────────────────────────────────────────────┤
│ File-Organization Module │
│ (logical blocks ↔ physical blocks, allocation) │
├─────────────────────────────────────────────────┤
│ Basic File System │
│ (generic read/write to physical blocks) │
├─────────────────────────────────────────────────┤
│ I/O Control │
│ (device drivers, interrupt handlers) │
├─────────────────────────────────────────────────┤
│ Devices │
│ (disk, SSD, tape, etc.) │
└─────────────────────────────────────────────────┘
```

### Layer-by-Layer Description

#### 1. Application Programs (Top Layer)

- User-level programs that use files (editors, compilers, databases)
- Issue file operations through system calls: `open()`, `read()`, `write()`, `close()`
- Have no knowledge of how files are stored on disk

#### 2. Logical File System

- Manages all **metadata** -- information about files, not the file data itself
- Maintains the **directory structure** and maps file names to file metadata
- Manages the **File Control Block (FCB)** which contains file attributes (ownership, permissions, timestamps, size, data block locations)
- Handles **protection and security** checks -- verifies that the requesting process has permission to perform the requested operation
- This is the layer that knows about files as logical entities

#### 3. File-Organization Module

- Translates **logical block addresses** to **physical block addresses**
- Knows about file allocation methods (contiguous, linked, indexed)
- Manages the **free-space manager** -- tracks which blocks on disk are unallocated
- Given a logical block number within a file, determines which physical disk block corresponds to it

#### 4. Basic File System

- Issues generic commands to the device driver to read and write **physical blocks** on the disk
- Identifies blocks by their physical disk address (e.g., drive 1, cylinder 73, track 2, sector 10)
- Manages **memory buffers and caches** that hold disk blocks in transit between memory and disk
- Does not understand files or directories -- just reads/writes raw blocks

#### 5. I/O Control

- Consists of **device drivers** and **interrupt handlers**
- Translates high-level commands (e.g., "read block 123") into low-level, hardware-specific instructions for the disk controller
- Writes specific bit patterns to I/O controller memory locations to tell the hardware which device location to read/write

#### 6. Devices (Bottom Layer)

- The physical storage hardware: magnetic disks, SSDs, optical drives
- Data is transferred in units of **sectors** (typically 512 bytes or 4KB)

---

## File Control Block (FCB) / Inode

The **File Control Block (FCB)** is the fundamental data structure in a file system that stores all metadata about a file. In Unix/Linux systems, the FCB is called an **inode** (index node).

```
┌──────────────────────────────────────┐
│ File Control Block (FCB) │
├──────────────────────────────────────┤
│ File permissions (rwxrwxrwx) │
│ File owner (user ID, group ID) │
│ File size (bytes) │
│ File timestamps: │
│ - Creation time │
│ - Last access time │
│ - Last modification time │
│ Link count (hard links) │
│ Number of data blocks allocated │
│ Pointers to data blocks: │
│ - Direct pointers (12) │
│ - Single indirect pointer │
│ - Double indirect pointer │
│ - Triple indirect pointer │
└──────────────────────────────────────┘
```

**Important:** The FCB/inode does NOT store the file name. File names are stored in directory entries that map names to FCB/inode numbers.

---

## On-Disk Structures

These data structures reside on the disk and persist across reboots:

### 1. Boot Control Block (per volume)

- Contains information needed to boot the OS from that volume
- In UFS (Unix File System): called the **boot block**
- In NTFS: called the **partition boot sector**
- Usually the first block of the volume
- Empty if the volume does not contain an OS

### 2. Volume Control Block (per volume)

- Contains volume-level details: total number of blocks, block size, free-block count, free-block pointers, free-FCB count, free-FCB pointers
- In UFS: called the **superblock**
- In NTFS: stored in the **Master File Table (MFT)**

### 3. Directory Structure (per file system)

- Organizes the files within the file system
- Contains file names and associated inode/FCB numbers
- In UFS: includes file names and inode numbers
- In NTFS: stored in the MFT

### 4. Per-File FCB (one per file)

- Contains detailed metadata about each file
- In UFS: the **inode** (with a unique inode number)
- In NTFS: stored as a row in the MFT, identified by a file ID

```
On-Disk Structures Summary:
┌────────────────────────────────────────────────────────┐
│ DISK VOLUME │
├──────────────┬───────────────┬──────────┬──────────────┤
│ Boot Control │ Volume Control│ Directory│ Per-File │
│ Block │ Block │ Structure│ FCBs │
│ (boot blk) │ (superblock) │ (names │ (inodes) │
│ │ │ → inodes)│ │
├──────────────┴───────────────┴──────────┴──────────────┤
│ DATA BLOCKS │
│ (actual file contents) │
└────────────────────────────────────────────────────────┘
```

---

## In-Memory Structures

These data structures are created in RAM when the file system is mounted or files are opened. They improve performance by caching frequently accessed information.

### 1. Mount Table

- Contains information about each mounted volume
- Stores the volume's type, size, and pointers to other relevant data structures

### 2. Directory Structure Cache

- Holds directory information for recently accessed directories
- Avoids repeated disk reads when navigating directory paths

### 3. System-Wide Open File Table

- Contains a copy of the FCB for **every currently open file** in the system
- Also stores the **open count** (how many processes have the file open)
- Shared across all processes

### 4. Per-Process Open File Table

- Each process has its own open file table
- Each entry contains a pointer to the corresponding entry in the system-wide open file table
- Also stores: **current file position pointer**, **access mode** (read/write), and the **file descriptor** number

```
In-Memory Structures:

 Per-Process System-Wide
 Open File Table Open File Table
 ┌──────────────┐ ┌─────────────────────┐
 │ fd 0 ──────────────────→ │ FCB copy of file A │
 │ fd 1 ──────────────────→ │ FCB copy of file B │
 │ fd 2 ────────┐ │ FCB copy of file C │
 └──────────────┘ │ │ ... │
 │ └─────────────────────┘
 Per-Process │ │
 Open File Table │ │
 (another process)│ ▼
 ┌──────────────┐ │ ┌─────────────────────┐
 │ fd 0 ──────────→│ │ On-Disk FCB/Inode │
 │ fd 1 ───────────┘ │ (actual disk data) │
 └──────────────┘ └─────────────────────┘
```

---

## How File Operations Work Through the Layers

### File Open Operation

When a process calls `open("myfile.txt", O_RDWR)`:

```
Step 1: Logical File System
 - Search directory structure for "myfile.txt"
 - Find the file's inode/FCB number from the directory
 - Check permissions (does the process have read/write access?)

Step 2: If file not already open by another process:
 - Read the FCB/inode from disk into memory
 - Create an entry in the system-wide open file table
 - Set the open count to 1

Step 3: If file already open by another process:
 - Find existing entry in system-wide open file table
 - Increment the open count

Step 4: Create an entry in the per-process open file table
 - Store pointer to system-wide table entry
 - Set current file position to 0
 - Store access mode (read/write)

Step 5: Return file descriptor (fd) to the application
```

### File Read Operation

When a process calls `read(fd, buffer, 100)`:

```
Step 1: Per-Process Open File Table
 - Use fd to find the entry
 - Get current file position and pointer to system-wide table

Step 2: Logical File System
 - Use FCB to determine which logical block to read
 - Verify the read does not exceed file size

Step 3: File-Organization Module
 - Translate logical block number to physical block number
 - (Uses allocation method: contiguous, linked, or indexed)

Step 4: Basic File System
 - Check if the physical block is in the buffer cache
 - If cache hit: return data from cache
 - If cache miss: issue I/O request

Step 5: I/O Control
 - Device driver translates to hardware commands
 - DMA transfers data from disk to memory buffer

Step 6: Data returned to application's buffer
 - File position pointer is updated in per-process table
```

---

## Comparison: UFS vs NTFS Terminology

| Structure            | UFS (Unix)     | NTFS (Windows)          |
| :------------------- | :------------- | :---------------------- |
| Boot Control Block   | Boot block     | Partition boot sector   |
| Volume Control Block | Superblock     | Master File Table (MFT) |
| Per-File FCB         | Inode          | MFT row (file record)   |
| Directory Structure  | Name + inode # | Stored in MFT           |
| File System Type     | ext2/3/4, UFS  | NTFS, FAT32             |

---

## Key Points Summary

| Concept                     | Key Idea                                                 |
| :-------------------------- | :------------------------------------------------------- |
| Layered design              | Each layer builds on the one below; reduces complexity   |
| Logical File System         | Manages metadata, directories, FCBs, protection          |
| File-Organization Module    | Maps logical blocks to physical blocks                   |
| Basic File System           | Issues raw block read/write; manages buffer cache        |
| I/O Control                 | Device drivers; hardware-specific I/O                    |
| FCB / Inode                 | Per-file metadata structure (everything except the name) |
| On-disk structures          | Boot block, superblock, directory, inodes, data blocks   |
| In-memory structures        | Mount table, directory cache, open file tables           |
| System-wide open file table | One entry per open file; shared across all processes     |
| Per-process open file table | One per process; stores fd, position, access mode        |

---

## Exam Tips

1. **Layered file system diagram** is a high-frequency question. Memorize all six layers in order from top (application) to bottom (devices), and know each layer's function.
2. **FCB/inode contents** may be asked as a short-answer question. List the key fields: permissions, owner, size, timestamps, block pointers.
3. **On-disk vs. in-memory structures** is a classic comparison question. Know the four on-disk structures and four in-memory structures with their purposes.
4. **File open operation** steps are commonly asked. Trace through the layers showing how the directory is searched, FCB is loaded, and file descriptor is returned.
5. **Per-process vs. system-wide open file table** -- understand why both exist. The system-wide table avoids duplicating FCB data; the per-process table tracks each process's own file position.
6. Remember: the **inode does NOT store the file name**. The directory maps names to inode numbers. This is a frequently tested concept.
7. **UFS vs NTFS terminology** mapping (superblock vs MFT, inode vs file record) may appear in comparison questions.
