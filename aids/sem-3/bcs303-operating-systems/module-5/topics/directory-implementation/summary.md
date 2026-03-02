# Directory Implementation - Summary

## Key Definitions

- **Directory**: A special file that maintains a mapping between file names and their metadata, including attributes and pointers to data blocks
- **Directory Entry**: A record within a directory containing file name, attributes, and data block pointers
- **Linear List**: A directory implementation that stores entries sequentially, requiring O(n) search time
- **Hash Table**: A directory implementation using hash functions to index entries, providing O(1) average search time
- **Collision**: When two different file names produce the same hash value
- **Dentry Cache**: A kernel-level cache maintaining recently accessed directory entries in memory for faster lookup
- **Bucket**: A slot in a hash table that may contain one or more directory entries

## Important Formulas

- **Linear Search**: Time complexity = O(n), where n is number of files
- **Hash Table Search (Average)**: Time complexity = O(1)
- **Hash Table Search (Worst)**: Time complexity = O(n)
- **Hash Function**: index = hash(filename) mod table_size
- **Expected bucket size**: n / b, where n = entries, b = buckets
- **Disk I/O for path resolution**: 1 + depth of file in directory tree

## Key Points

1. Directory implementation determines how file metadata is organized and accessed efficiently
2. Linear list is simple to implement but inefficient for large directories (O(n) search)
3. Hash tables provide O(1) average search but require collision handling
4. Modern file systems combine disk-based linear lists with memory-based hash caches
5. The dentry cache in Linux maintains directory entry objects with parent-child relationships
6. Hash functions should minimize collisions while being computationally efficient
7. Chaining (linked lists in buckets) is preferred over open addressing for directory hash tables
8. Directory operations include create, delete, search, rename, list, and attribute management
9. Variable-length file names require careful length field management in directory entries
10. Directory implementation significantly impacts overall file system performance

## Common Mistakes

1. **Confusing directory structure with directory implementation**: Directory structure (single-level, hierarchical) is different from the underlying implementation (linear list, hash table)

2. **Ignoring collision handling**: Many students forget that hash tables must handle collisions, which can degrade performance to O(n)

3. **Assuming hash tables are always faster**: For small directories with few files, linear lists may actually be faster due to no hash computation overhead

4. **Forgetting disk vs memory**: The on-disk directory structure may differ from the in-memory representation; file systems use caches to bridge this gap

5. **Overlooking cache coherency**: When files are modified, the directory entry cache must be properly updated or invalidated to maintain consistency