# File System Analysis: NTFS, FAT, ext4

## Introduction to File Systems in Forensics

A file system is a method and data structure an operating system uses to control how data is stored and retrieved on a storage device. In digital forensics, understanding file systems is paramount, as they govern where data is stored, how it is named, what metadata is associated with it, and crucially, what remnants of data (artifacts) are left behind after deletion or modification. This analysis forms the bedrock of disk forensics, allowing investigators to recover evidence, establish timelines, and understand user activity.

This module focuses on three of the most prevalent file systems encountered in forensic investigations: **FAT** (File Allocation Table), **NTFS** (New Technology File System), and **ext4** (Fourth Extended Filesystem).

## Key Concepts and Components

All file systems share some common conceptual components that a forensic analyst must understand:

- **Volume:** A logical storage unit, often a partition, formatted with a specific file system.
- **Partition:** A contiguous block of space on a physical disk. A disk can have multiple partitions, each with a different file system.
- **Boot Sector:** The first sector of a volume, containing essential code for booting and information about the file system layout.
- **Clusters/Blocks:** The fundamental unit of disk space allocation for files and directories. A cluster (FAT/NTFS) or block (ext4) consists of one or more contiguous sectors.
- **Metadata:** Data about data. This includes file names, sizes, timestamps (Created, Modified, Accessed, Entry Modified), and permissions.
- **Slack Space:** The unused space between the end of a file and the end of the last cluster allocated to that file. This space can contain data from previously deleted files.
- **Unallocated Space:** Clusters/blocks on the disk that are not currently allocated to any live file. This space contains the contents of deleted files until they are overwritten.

## File Allocation Table (FAT)

The FAT file system is simple, old, and widely supported across operating systems, making it common on removable media like USB drives, SD cards, and older systems.

### Structure and Layout

```
+----------------+---------------------+----------------------+-------------------+
| Boot Sector &  | Primary FAT (Copy 1)| Secondary FAT (Copy 2)| Root Directory   | Data Area (File  |
| BIOS Parameter |                     |                      | (FAT12/16 only)  | & Dir Contents)  |
| Block (BPB)    |                     |                      |                  |                  |
+----------------+---------------------+----------------------+-------------------+-------------------+
```

- **BIOS Parameter Block (BPB):** Located in the boot sector, it contains vital information about the volume (e.g., bytes per sector, sectors per cluster, size of FAT, root directory entries).
- **File Allocation Table (FAT):** This is the core of the file system. It is a map of the data area, where each entry corresponds to a cluster. The value in the entry indicates the status of the cluster:
  - `0`: Free cluster.
  - `BAD`: Cluster is damaged and shouldn't be used.
  - `EOF`: Marks the end of a file's cluster chain.
  - Any other value: The cluster number of the next cluster in the file's chain.
- **Root Directory:** In FAT12 and FAT16, this is a fixed-size table located after the FATs. In FAT32, the root directory can be located anywhere and can grow like any other directory.
- **Data Area:** Where the actual content of files and subdirectories is stored.

### FAT Versions

| Version | Max Volume Size (Theoretical) | Max File Size | Key Differentiator                     |
| :------ | :---------------------------- | :------------ | :------------------------------------- |
| FAT12   | ~16 MB                        | 4 GB          | Uses 12-bit FAT entries. For floppies. |
| FAT16   | 2 GB (4 GB with 64k clusters) | 4 GB          | Uses 16-bit FAT entries.               |
| FAT32   | 2 TB                          | 4 GB          | Uses 32-bit FAT entries (28-bit used). |

### Directory Entries and Timestamps

A FAT directory entry is 32 bytes long and contains:

- File Name (8 bytes) and Extension (3 bytes) – 8.3 format.
- Attribute Byte (e.g., Archive, Read-only, Hidden, System, Directory, Volume Label).
- **Timestamps:**
  - **Created:** File creation time/date.
  - **Modified:** Last time the file's content was modified.
  - **Accessed:** Last time the file was read (date only, no time on older FAT).
- Starting Cluster (points to the first cluster in the FAT chain).
- File Size.

### Forensic Considerations for FAT

- **Deletion:** When a file is deleted, the first character of its filename is replaced with a `0xE5` (σ), marking the entry as deleted. The cluster chain in the FAT is zeroed out, marking those clusters as free. The file data remains in the data area until overwritten. Recovery involves finding deleted entries and walking the now-erased FAT chain before it's overwritten.
- **Fragmentation:** Files can be non-contiguous, with their cluster chains scattered across the disk.
- **Limited Metadata:** Lacks advanced permissions, alternate data streams, and provides less precise timestamps than NTFS.

## NTFS (New Technology File System)

NTFS is the default file system for modern Windows operating systems. It is a journaling, high-performance file system that supports large volumes, advanced metadata, security, and reliability features.

### Master File Table (MFT)

The MFT is the heart of NTFS. It is a relational database where every file and directory (including the MFT itself) is a record. The first 16 records are reserved for metadata files, prefixed with `$`.

```
+----+---------------------+-----------------------------------------+
| ID | Record Name         | Description                             |
+----+---------------------+-----------------------------------------+
| 0  | $MFT               | The Master File Table itself.           |
| 1  | $MFTMirr           | A backup copy of the first few MFT recs.|
| 2  | $LogFile           | Journaling/log file for transactions.   |
| 3  | $Volume            | Volume information (serial, label).     |
| 4  | $AttrDef          | Attribute definitions.                  |
| 5  | . (Root Directory) | The root directory.                     |
| 6  | $Bitmap            | Cluster allocation status bitmap.       |
| 7  | $Boot             | Boot sector and bootstrap code.         |
| 8  | $BadClus          | List of bad clusters on the volume.     |
| 9  | $Secure           | Security descriptors for files.         |
| 10 | $UpCase           | Uppercase character mapping table.     |
| 11 | $Extend           | Directory for optional extensions.      |
+----+---------------------+-----------------------------------------+
```

### MFT Record Structure and Attributes

Each MFT record is typically 1024 bytes. A file's data and metadata are stored in **attributes**.

- **$STANDARD_INFORMATION (0x10):** Contains fundamental timestamps (Created, Modified, Accessed, Entry Modified), owner ID, security ID, and flags (e.g., read-only, hidden).
- **$FILE_NAME (0x30):** Contains the file name in Unicode, parent directory reference, and another set of timestamps (Created, Modified, Accessed, Entry Modified).
- **$DATA (0x80):** Contains the file's data. A file can have multiple DATA attributes (e.g., for Alternate Data Streams).
- **Resident vs. Non-Resident Data:** Small files (typically < ~700 bytes) can have their data stored directly within the MFT record (**resident**). Larger files have their data stored in external clusters, and the MFT record contains a **runlist** (a list of cluster extents) pointing to that data (**non-resident**).

### Key NTFS Features

- **Alternate Data Streams (ADS):** NTFS allows multiple data streams to be associated with a single filename. The default stream is `:DATA`. A hidden stream could be `file.txt:secret.txt`. ADS is a common technique for hiding data.
- **Journaling ($LogFile):** NTFS logs metadata transactions to ensure file system integrity in case of a crash. This log can sometimes contain forensic artifacts of recent changes.
- **Advanced Permissions:** Uses Access Control Lists (ACLs) for detailed security policies.
- **Large File and Volume Support.**

### Forensic Considerations for NTFS

- **Deletion:** When a file is deleted, its MFT record is marked as free. The bitmap (`$Bitmap`) is updated to mark the clusters as unallocated. The record and data persist until overwritten. The `$I30` index entries within directories are also manipulated.
- **Timestamps:** The existence of two timestamp sets (`$STANDARD_INFORMATION` and `$FILE_NAME`) is critical. `$SI` timestamps are often updated by system processes, while `$FN` timestamps are more user-centric and can be harder to alter. Discrepancies between them can be suspicious.
- **INDX Buffers:** These are indexes for directories, allowing for efficient searching. They can contain remnants of deleted filenames, providing evidence of past activity.
- **MFT Analysis:** Analyzing the `$MFT` file itself is a core forensic technique, allowing for file enumeration, timeline creation, and recovery of deleted entries.

## ext4 (Fourth Extended Filesystem)

ext4 is the default file system for most Linux distributions. It is an evolution of ext3, offering improved performance, reliability, and larger volume support.

### Structure and Layout

```
+-----------+-----------+-------------+-----------+-------------------+-------------------+
| Boot      | Block     | Block       | Block     | Block Group 0     | Block Group 1     |
| Block     | Group 0   | Group 1     | Group N   | +----------------+| +----------------+|
|           | Descriptor| Descriptor  | Descriptor| | Superblock     || | ...            ||
|           | Table     | Table       | Table     | | Group Desc.    || |                ||
|           |           |             |           | | Data Block Bitm|| |                ||
|           |           |             |           | | inode Bitmap   || |                ||
|           |           |             |           | | inode Table    || |                ||
|           |           |             |           | | Data Blocks    || |                ||
|           |           |             |           | +----------------+| +----------------+|
+-----------+-----------+-------------+-----------+-------------------+-------------------+
```

- **Superblock:** Contains global information about the file system (e.g., total blocks, free blocks, inode count, block size). Copies are stored in several block groups for redundancy.
- **Block Group Descriptor Table:** Describes the layout and status of each block group.
- **Block Bitmap:** A bitmap tracking the allocation status of each block in the block group.
- **inode Bitmap:** A bitmap tracking the allocation status of each inode in the block group.
- **inode Table:** A table containing all the inodes for that block group.
- **Data Blocks:** The blocks containing actual file and directory data.

### inodes and Directory Entries

- **inode (Index Node):** A data structure (typically 128 or 256 bytes) that describes a file or directory. It contains:
  - Metadata: Permissions, owner/group IDs, size.
  - **Timestamps:** `i_ctime` (inode change time), `i_mtime` (modification time), `i_atime` (access time), `i_crtime` (creation time - ext4 only).
  - Pointers to the data blocks storing the file's content.
- **Directory Entries (`dentry`):** A directory is a special file containing a list of `dentry` structures. Each entry maps a filename to its corresponding inode number.

### Key ext4 Features

- **Extents:** Instead of listing individual blocks (like block maps in ext2/3), ext4 uses **extents** – contiguous ranges of blocks. This improves performance for large files and reduces fragmentation.
- **Journaling:** ext4 uses a journal to record metadata (or optionally data+metadata) changes before committing them to the main file system, ensuring consistency.
- **Persistent Pre-allocation:** Allows pre-allocating disk space for a file before writing to it, useful for databases and media recording.
- **Delayed Allocation:** Data is cached in memory before being written to disk, improving performance. This can complicate forensic analysis as data might not be on disk immediately.

### Forensic Considerations for ext4

- **Deletion:** When a file is deleted, its inode is marked as free in the inode bitmap, and the corresponding blocks are marked free in the block bitmap. The pointer to the data blocks in the inode is typically zeroed out. The data remains on disk until overwritten. The directory entry is also removed.
- **Journal Analysis:** The journal (`journal`) can contain traces of recent file operations (create, delete, modify), which can be crucial for recovering recent activity, especially after an unclean shutdown.
- **`i_crtime`:** The creation timestamp (often called "birth time") is a valuable forensic artifact, though not all utilities or system calls record or report it.
- **Slack Space:** Can be analyzed for data remnants, similar to other file systems.

## Comparative Analysis

| Feature                | FAT32                          | NTFS                                        | ext4                                |
| :--------------------- | :----------------------------- | :------------------------------------------ | :---------------------------------- |
| **Primary OS**         | Windows 9x, DOS, Removable Med | Windows NT, 2000, XP, Vista, 7, 8, 10, 11   | Linux                               |
| **Max File Size**      | 4 GB                           | 16 EB (Exabytes)                            | 16 TB                               |
| **Max Volume Size**    | 2 TB                           | 16 EB (Exabytes)                            | 1 EB (Exabyte)                      |
| **Journaling**         | No                             | Yes                                         | Yes                                 |
| **Permissions**        | Basic (R/O, Hidden, etc.)      | ACLs (Access Control Lists)                 | Unix Permissions (RWX) & ACLs       |
| **Metadata**           | Limited                        | Extensive (Multiple Timestamps, ADS)        | Extensive (Multiple Timestamps)     |
| **Deletion Artifact**  | `0xE5` filename, FAT zeroed    | MFT record marked free, Bitmap updated      | inode marked free, Bitmaps updated  |
| **Fragmentation Mgmt** | Linked List (FAT)              | Runlists in MFT                             | Extents                             |
| **Forensic Focus**     | Simple recovery, USB drives    | MFT analysis, ADS, INDX buffers, Timestamps | inode analysis, Journal, `i_crtime` |

## Exam Tips

1.  **Timestamps are Key:** Know the difference between `$STANDARD_INFORMATION` and `$FILE_NAME` timestamps in NTFS. For ext4, know what `i_atime`, `i_mtime`, `i_ctime`, and `i_crtime` represent.
2.  **Understand Deletion:** Be able to describe step-by-step what happens when a file is deleted on each file system. This is a common exam question.
3.  **Core Structures:** Memorize the core structures: **FAT** for FAT, **MFT** for NTFS, and **inode** for ext4. Know what they contain and their role.
4.  **Compare and Contrast:** Be prepared to write a short comparison table highlighting the differences between the three file systems, focusing on limits, features, and forensic implications.
5.  **Think Like an Analyst:** Questions often present a scenario (e.g., "a file was deleted from a USB drive"). Your answer should identify the file system first (FAT) and then explain the relevant forensic process for that system.
