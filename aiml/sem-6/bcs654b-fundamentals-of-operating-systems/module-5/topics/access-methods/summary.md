# Access Methods - Summary

## Key Definitions and Concepts

- **Sequential Access**: Data accessed in linear sequence (e.g., tape drives)
- **Direct Access (Random Access)**: Read/write at specific positions using addresses
- **Indexed Access**: Uses index table for rapid record location (e.g., databases)
- **File Pointer**: Tracks position in sequential access
- **Seek Operation**: Moves read/write head to specific disk position
- **Index Block**: Special block containing pointers to file blocks

## Important Formulas and Theorems

```markdown
1. Seek Time Formula:
   `Seek Time = (Number of tracks crossed) × Time per track movement`

2. Direct Access Address Calculation:
   `Address = Base Address + (Record Number × Record Size)`

3. Indexed Access Complexity:
   `Disk Accesses = log_fanout(N) + 1` (N = records, fanout = index entries/block)
```

## Key Points

- Sequential access is efficient for media with physical movement constraints (e.g., magnetic tapes)
- Direct access enables O(1) time complexity for record retrieval using calculated addresses
- Indexed access combines sequential and direct methods using multi-level indices
- Modern OS support multiple access methods simultaneously through file system APIs
- Access method choice impacts I/O performance and storage overhead
- File allocation table (FAT) is a common indexed implementation
- Memory-mapped files allow direct access through virtual memory addresses
- Database systems frequently use clustered indexes for optimized access

## Common Mistakes to Avoid

1. Confusing sequential access with serial processing (sequential can have random access patterns)
2. Ignoring sector/track geometry in direct access calculations
3. Overlooking index maintenance overhead in write operations
4. Assuming direct access always outperforms indexed (depends on record size and access patterns)

## Revision Tips

1. Memorize the 3 fundamental access methods with 2 real-world examples each
2. Practice numerical problems on address calculation and seek time estimation
3. Create comparison tables: Sequential vs Direct vs Indexed (speed, storage, use cases)
4. Review OS-specific implementations: NTFS (Windows) vs ext4 (Linux) access method handling
