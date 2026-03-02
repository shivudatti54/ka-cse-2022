# File System - Summary

## Key Definitions and Concepts

- **File**: A named collection of related information stored on secondary storage, providing logical view of data storage.

- **File System**: The OS component that provides file management services, including creation, deletion, reading, writing, and protection of files.

- **Directory**: A special file that contains entries mapping file names to their metadata and locations, enabling hierarchical organization.

- **inode**: The index node in Unix-like systems that stores file metadata and pointers to data blocks.

- **Mount Point**: The directory location where a file system is attached to make its contents accessible.

## Important Formulas and Theorems

- **Direct Access Position**: block_address = starting_address + (record_number × record_size)

- **Pointers per Index Block**: block_size / pointer_size (e.g., 4KB / 4B = 1024 pointers)

- **Indexed File Size**: Direct blocks + (single_indirect × block_size) + (double_indirect × block_size²) + (triple_indirect × block_size³)

- **File Access Time**: Seek time + Rotational delay + Transfer time

## Key Points

1. Files have attributes including name, identifier, type, location, size, protection info, timestamps, and owner information.

2. Three access methods: Sequential (linear), Direct/Random (by record number), and Indexed (using index blocks).

3. File system layers: Application → Logical File System → File Organization → Basic File System → Device Driver → Physical I/O.

4. Directory structures: Single-level (flat), Two-level (per-user), Tree-structured (hierarchical), Acyclic-graph (shared).

5. Allocation methods: Contiguous (fast but fragmentation), Linked (flexible but slow random access), Indexed (good all-round but space overhead).

6. Free space management: Bit vector (fast allocation), Linked list (simple), Grouping (efficient multi-block), Counting (contiguous tracking).

7. FAT file systems maintain allocation table in memory; inode systems use fixed-size metadata structures with direct/indirect pointers.

8. File system mounting attaches a file system's root to a point in the existing directory tree.

9. Protection mechanisms include access control lists (ACL) and permission bits for owner/group/others.

10. Buffer caching improves performance by keeping frequently accessed blocks in main memory.

## Common Mistakes to Avoid

1. Confusing file allocation method with directory structure—they are separate components of file system design.

2. Assuming indexed allocation always outperforms contiguous allocation—index blocks add overhead for small files.

3. Forgetting that linked allocation cannot support direct access efficiently since blocks must be traversed sequentially.

4. Overlooking the fact that bit vectors require significant memory for large disks (one bit per block).

5. Misunderstanding that tree-structured directories do not allow cycles, while acyclic-graph directories do permit sharing.

## Revision Tips

1. Draw diagrams of each directory structure to visualize how files are organized and accessed.

2. Create a comparison table for allocation methods showing pros, cons, and ideal use cases.

3. Practice calculating maximum file sizes for inode-based systems with different block sizes.

4. Review real-world file systems (NTFS, ext4, FAT32) and identify which concepts they implement.

5. Understand the complete path resolution process from root directory to target file.