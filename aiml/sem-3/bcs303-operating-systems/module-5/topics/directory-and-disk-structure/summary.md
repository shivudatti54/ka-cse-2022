# Directory and Disk Structure - Summary

## Key Definitions

- **Directory**: A special file that contains information about other files, including their names, attributes, and pointers to data blocks
- **Inode**: Index node; a data structure in UNIX-like file systems that contains metadata and block pointers for each file
- **Boot Block**: The first sector of disk containing bootstrap code for system initialization
- **Superblock**: File system structure containing metadata including size, block size, and free space information
- **FAT (File Allocation Table)**: An array structure used in FAT file systems to track cluster allocation
- **Cylinder**: The collection of tracks at a given radial distance across all disk surfaces
- **Hard Link**: Multiple directory entries pointing to the same inode
- **Symbolic Link**: A special file containing a path to another file

## Important Formulas

- **Maximum file size with inode addressing**: For a file system with 4KB block size and 32-bit block pointers:
- Direct blocks: 12 × 4KB = 48KB
- Single indirect: 1024 × 4KB = 4MB
- Double indirect: 1024² × 4KB = 4GB
- Triple indirect: 1024³ × 4KB = 4TB

- **Disk access time**: T = T_seek + T_rotation + T_transfer

## Key Points

- Directory structures evolved from simple single-level to hierarchical tree structures, with modern systems supporting acyclic graphs for flexible file sharing
- Tree-structured directories provide efficient O(depth) path resolution and support natural file organization
- Hash table directory implementation provides O(1) average lookup time versus O(n) for linear lists
- Disk geometry (cylinders, tracks, sectors) directly impacts file system performance due to seek time characteristics
- Boot blocks and superblocks are critical structures stored at fixed locations for system initialization and file system management
- Inodes use a combination of direct and indirect pointers to address data blocks, balancing efficiency for small and large files
- FAT file systems use linked allocation where each cluster points to the next, while inode-based systems use indexed allocation
- Directory entries store file metadata including name, inode number, and attributes needed for file access

## Common Mistakes

1. **Confusing logical and physical file organization**: Students often mix up the directory structure (logical organization) with disk allocation methods (physical organization)

2. **Ignoring directory entry deletion semantics**: When deleting a file with multiple hard links, only the link count decrements; the inode and data blocks persist until the count reaches zero

3. **Overlooking superblock replication**: Many students forget that superblocks are duplicated across the disk for fault tolerance, which is critical for file system recovery

4. **Misunderstanding symbolic vs hard links**: Hard links cannot span partitions (same inode number), while symbolic links are separate files containing paths

5. **Assuming directory structures are the same as file allocation**: The directory structure manages naming and organization, while allocation methods determine how disk blocks are assigned to files
