# Directory and Disk Structure - Summary

## Key Definitions and Concepts

- **Directory**: A special file containing metadata about other files, including file names, attributes, and pointers to file control blocks or i-nodes.
- **Single-Level Directory**: The simplest structure with one directory containing all files, limited by naming conflicts and poor scalability.
- **Two-Level Directory**: Creates separate user directories under a master directory, providing user isolation but lacking subdirectory support.
- **Hierarchical Directory**: A tree-structured organization starting from root, supporting unlimited directory depth and logical file grouping.
- **Acyclic Graph Directory**: Extends hierarchical structure with symbolic and hard links, allowing directory sharing without cycles.
- **Contiguous Allocation**: Assigns consecutive disk blocks to files, offering fast sequential access but suffering from external fragmentation.
- **Linked Allocation**: Stores files as linked lists of blocks, eliminating fragmentation but performing poorly for random access.
- **Indexed Allocation**: Uses index blocks to store pointers to all file blocks, enabling efficient random access at the cost of index overhead.
- **Bit Vector**: Free space management technique using one bit per block to track allocation status.
- **Disk Scheduling**: Algorithms ordering pending I/O requests to minimize seek time and improve throughput.

## Important Formulas and Theorems

- **Indexed File Maximum Size**: Maximum file size = (direct blocks × block size) + (single indirect × pointers × block size) + (double indirect × pointers² × block size) + (triple indirect × pointers³ × block size)
- **Disk Access Time**: Total access time = seek time + rotational latency + transfer time
- **SCAN Head Movement**: Move head in one direction, servicing all requests, then reverse direction

## Key Points

- Directory structures provide logical file organization while disk structures manage physical data placement.
- Hierarchical directories are the dominant organizational paradigm in modern operating systems.
- Symbolic links create new directory entries referencing paths, while hard links create additional references to the same i-node.
- Indexed allocation (i-node based) provides the best balance between sequential and random access performance.
- Bit vectors enable O(1) allocation checking but require memory proportional to disk size.
- SCAN and C-SCAN algorithms significantly outperform FCFS in reducing average seek distance.
- Partitioning enables multiple independent file systems and operating systems on a single disk.

## Common Mistakes to Avoid

- Confusing logical directory structure with physical disk organization—they serve different purposes.
- Forgetting that hard links cannot reference directories or span partitions.
- Overlooking the index block overhead in indexed allocation when calculating storage efficiency.
- Assuming that deleting a symbolic link deletes the target file—only the link itself is removed.
- Neglecting rotational latency and transfer time when calculating total disk access time.

## Revision Tips

1. Draw diagrams of each directory structure type to reinforce visual understanding of the organizational differences.

2. Practice calculating total head movement for all disk scheduling algorithms with example request queues.

3. Create a comparison table of file allocation methods with performance characteristics and suitable use cases.

4. Trace through hard link and symbolic link behaviors in file deletion scenarios to understand reference counting.

5. Review the relationship between i-node pointers and maximum file size to understand indexed allocation limits.