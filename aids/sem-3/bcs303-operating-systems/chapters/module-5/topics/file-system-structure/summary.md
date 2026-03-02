# File System Structure - Summary

## Key Definitions and Concepts

- File System: An abstraction layer that provides persistent storage organization, allowing users and applications to store and retrieve data without understanding physical disk details.

- File Control Block (FCB): The primary data structure containing all file metadata including name, permissions, timestamps, size, and pointers to data blocks.

- Inode (Index Node): A fixed-size structure in Unix-like file systems containing direct, single indirect, double indirect, and triple indirect pointers to file data blocks.

- Directory: A special file containing entries that map file names to their corresponding inodes or FCBs, enabling hierarchical file organization.

- Allocation Method: The technique used to assign disk blocks to files, with three primary methods being contiguous, linked, and indexed allocation.

- Free Space Management: The system for tracking available disk blocks using techniques like bit vectors (bitmap), linked lists, or grouping.

## Important Formulas and Theorems

- Maximum file size with indexed allocation = (Number of direct blocks × block size) + (Number of single indirect × block size²) + (Number of double indirect × block size³) + (Number of triple indirect × block size⁴)

- Bitmap size (in bits) = Total number of disk blocks

- Number of disk accesses for contiguous allocation (sequential) = Number of blocks in file

- Number of disk accesses for linked allocation (sequential) = Number of blocks in file

- Number of disk accesses for indexed allocation (random) = 2 (index block + data block)

## Key Points

- FILE SYSTEMS use a layered architecture separating physical device handling from logical file operations.

- THE INODE structure uses multiple levels of indirection to efficiently handle files of varying sizes while maintaining fixed inode size.

- DIRECTORIES can be implemented as simple linear lists or sophisticated hash tables, with modern file systems using B+ trees for performance.

- CONTIGUOUS allocation provides excellent sequential read performance but suffers from external fragmentation and difficulty in file expansion.

- LINKED allocation eliminates external fragmentation but performs poorly for random access since blocks must be traversed sequentially.

- INDEXED allocation combines good random access with no external fragmentation but requires additional storage for index blocks.

- FREE SPACE bitmaps provide efficient allocation decisions but require additional memory proportional to disk size.

- MODERN file systems combine multiple allocation methods, using contiguous allocation for small files and indexed methods for larger files.

## Common Mistakes to Avoid

- CONFUSING file allocation with free space management; these are separate but related concepts in file system structure.

- FORGETTING that linked allocation cannot support random access efficiently despite the presence of pointers in each block.

- IGNORING the overhead of index blocks when calculating storage requirements for indexed allocation.

- ASSUMING all file systems use inodes; Windows file systems like NTFS use different structures (Master File Table).

- OVERLOOKING that directory entries store file names and inode numbers, not the complete file metadata.

## Revision Tips

- PRACTICE drawing and explaining the file system layer diagram until it becomes automatic; this appears frequently in exams.

- MEMORIZE the inode pointer structure and practice numerical problems calculating maximum file sizes for different pointer configurations.

- COMPARE allocation methods using a table format listing advantages, disadvantages, and suitable use cases for each method.

- UNDERSTAND bitmap calculations thoroughly; these are straightforward marks if you remember the formula and show working.

- REVIEW how real file systems (ext4, NTFS, FAT32) implement these concepts to reinforce theoretical understanding with practical examples.