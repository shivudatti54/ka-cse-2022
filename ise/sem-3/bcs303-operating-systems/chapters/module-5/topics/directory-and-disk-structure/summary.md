# Directory and Disk Structure - Summary

## Key Definitions and Concepts

- **Directory**: A special file that maps file names to their metadata and data block locations through File Control Blocks (FCBs)
- **File Control Block (FCB)**: A data structure containing file metadata including name, size, creation time, permissions, and pointers to data blocks
- **Hierarchical Directory Structure**: A tree-like organization allowing unlimited nesting of subdirectories, used by all modern operating systems
- **Track**: Concentric circles on a disk surface containing data
- **Sector**: A wedge-shaped portion of a track, the smallest addressable unit on disk (typically 512 bytes)
- **Cylinder**: The collection of tracks at the same radius on all disk surfaces
- **Sector Interleaving**: Physical arrangement of sequential sectors with gaps to allow controller processing time

## Important Formulas and Theorems

- **Disk Access Time**: Seek time + Rotational delay + Transfer time
- **Average Rotational Delay**: Half of the time for one full rotation (1/(2 × RPM) × 60 seconds)
- **Seek Time**: Time for disk arm to move to the correct cylinder
- **Linear List Search Complexity**: O(n) where n is the number of files
- **Hash Table Average Complexity**: O(1) for lookups

## Key Points

- Single-level directories suffer from naming conflicts and poor scalability
- Hierarchical directory structures balance simplicity with organizational flexibility
- Directory implementations use either linear lists or hash tables for entry lookup
- Hash tables provide O(1) average lookup but require collision resolution strategies
- Disk scheduling algorithms aim to minimize seek time and rotational latency
- SCAN algorithm moves disk head in one direction, servicing all requests, then reverses
- C-SCAN (Circular SCAN) returns to starting position without servicing requests during return
- Free space management methods include bit vectors, linked lists, grouping, and counting
- Bit vectors allow quick searching for free blocks but require additional disk space
- Partitioning enables multiple logical disks on a single physical disk

## Common Mistakes to Avoid

1. Confusing logical directory structure with physical disk organization—they are separate concerns
2. Forgetting that directory entries contain metadata pointers, not the actual file data
3. Overlooking the difference between seek time and rotational delay in disk performance
4. Assuming all sectors on a disk have the same capacity—modern disks use zoned recording
5. Neglecting the impact of sector interleaving on sequential read performance

## Revision Tips

1. Practice drawing and navigating hierarchical directory trees for different operating systems
2. Solve numerical problems on disk scheduling—calculate head movement for various algorithms
3. Create comparison tables for directory structures and free space management methods
4. Understand the relationship between FCBs, inodes, and directory entries
5. Review how file system mounting connects physical partitions to the directory hierarchy