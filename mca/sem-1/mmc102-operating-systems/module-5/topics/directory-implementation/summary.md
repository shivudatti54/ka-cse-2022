# Directory Implementation - Summary

## Key Definitions and Concepts

- **Directory:** A special file containing metadata about other files, including names, attributes, and pointers to file data locations.

- **Directory Entry (File Descriptor):** A data structure within a directory that stores information about a single file, typically including the file name, attributes, and FCB/i-node pointer.

- **File Control Block (FCB):** The data structure containing all file metadata such as permissions, timestamps, size, and disk block pointers.

- **I-Node (Index Node):** Used in Unix-like systems, containing file metadata and direct/indirect block pointers; directory entries store only the i-node number.

- **Hard Link:** Multiple directory entries pointing to the same i-node; shares the same file data.

- **Symbolic Link:** A special file containing a pathname string; acts as a pointer to another file.

## Important Formulas and Techniques

- **Linear List Search Complexity:** O(n) where n is the number of files in the directory

- **Hash Table Average Search Complexity:** O(1) with good hash function distribution

- **Hash Table Worst-Case Complexity:** O(n) when all entries collide

- **Entries per Block Calculation:** Block size / Directory entry size

## Key Points

1. Directory implementation addresses how file metadata is organized and searched, separate from how file data blocks are allocated on disk.

2. Tree-structured directories provide hierarchical organization and are used in all modern operating systems (Unix, Windows, macOS).

3. Linear list directories are simple to implement but suffer from O(n) search complexity, making them unsuitable for large directories.

4. Hash table directories offer O(1) average-case lookup but require collision handling mechanisms like chaining or open addressing.

5. Acyclic graph directories support file sharing through symbolic or hard links without creating circular references.

6. Directory operations include create, delete, search, list, rename, link, and unlink—each with specific implementation requirements.

7. Modern file systems (NTFS, ext4, Btrfs) use sophisticated indexing structures (B+trees) rather than simple hash tables for optimal performance across various directory sizes.

8. Path resolution requires traversing directory hierarchy from root to target, with each level potentially requiring disk I/O.

9. Directory caching in main memory significantly improves performance by avoiding repeated disk reads for frequently accessed directories.

10. Access permissions can be enforced at directory level, controlling which users can traverse or modify directory contents.

## Common Mistakes to Avoid

- Confusing directory structure (hierarchical organization) with directory implementation (physical storage method)

- Assuming hash tables always provide O(1) performance without considering collision impact

- Forgetting that symbolic links and hard links behave differently regarding file system boundaries and directory links

- Overlooking the relationship between directory entries and underlying file allocation methods

## Revision Tips

1. Draw and trace through examples of each directory structure type, understanding traversal requirements.

2. Practice calculating expected disk I/O for file lookup in linear list versus hash table implementations.

3. Compare real file system implementations (ext4, NTFS) to reinforce theoretical concepts with concrete examples.

4. Review directory operation algorithms by stepping through create, search, and delete operations on paper.