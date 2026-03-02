# Directory Implementation - Summary

## Key Definitions and Concepts

- DIRECTORY: A data structure that maintains mappings between file names and their associated file metadata, including attributes and disk locations.

- DIRECTORY ENTRY: A record within a directory containing the file name and pointer to file control information (inode or equivalent structure).

- INODE (Index Node): A data structure in UNIX-like systems that stores file attributes and pointers to data blocks; directory entries reference files through inode numbers.

- PATH RESOLUTION: The process of converting a path name into a specific directory entry by traversing the directory hierarchy.

- HARD LINK: Multiple directory entries pointing to the same inode, representing the same file with different names.

- SYMBOLIC LINK: A special file type containing a path name that redirects to another file location when accessed.

## Important Formulas and Theorems

- Linear list search complexity: O(n) where n is the number of files in the directory
- Hash table average search complexity: O(1) with good hash function and reasonable load factor
- Hash table worst-case complexity: O(n) when all keys hash to same bucket
- Directory entry size typically ranges from 32 to 128 bytes depending on file system design

## Key Points

- Directory implementation directly impacts file system performance for all file operations (create, delete, search, access).

- LINEAR LIST implementation provides simple insertion (O(1)) but slow search (O(n)), suitable for small directories with frequent insertions.

- HASH TABLE implementation offers fast average-case search (O(1)) but requires collision handling and additional overhead for hash structure maintenance.

- Directory entries contain file names, attributes, timestamps, permissions, and pointers to file data or inode numbers.

- Hierarchical directories use "." (self-reference) and ".." (parent-reference) special entries to enable navigation.

- Path resolution involves sequentially looking up each component of the path, starting from root (absolute) or current directory (relative).

- Operating systems use directory entry caches (dentry cache) to optimize path resolution performance by storing recently resolved paths.

- Different file systems (FAT, NTFS, ext4) use different directory implementation strategies optimized for their specific requirements.

## Common Mistakes to Avoid

- Confusing directory entries with inodes—remember that in many systems, directory entries only contain names and inode pointers, not complete file metadata.

- Assuming hash tables are always faster—in very small directories, linear search may actually be faster due to no hash computation overhead.

- Forgetting that hash table performance degrades with high load factors—most systems keep load factor below 0.75 to maintain performance.

- Overlooking the need for collision resolution in hash table implementations—understanding chaining versus open addressing is essential.

## Revision Tips

- Practice drawing directory entry structures for both simple (FAT-style) and UNIX-style (with separate inodes) file systems.

- Work through example path resolution sequences step-by-step to understand how hierarchical directories function.

- Compare time complexities of operations under both implementation approaches until you can recite them confidently.

- Review how directory caching improves performance and understand its interaction with the virtual file system layer.