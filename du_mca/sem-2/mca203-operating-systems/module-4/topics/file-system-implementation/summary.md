# File System Implementation - Summary

## Key Definitions and Concepts
- **Inode**: Data structure storing file metadata and block pointers
- **Superblock**: File system metadata container
- **Journaling**: Transaction logging for crash recovery
- **Extent**: Contiguous block allocation unit
- **Fragmentation**: Wasted space (external) or split files (internal)

## Important Formulas and Theorems
- **Max File Size (Indexed)**: 
  (Direct + (BlockSize/4) + (BlockSize/4)^2) * BlockSize
- **Bitmap Size**: ceil(TotalBlocks / 8) bytes
- **FAT Entry Count**: DiskSize / BlockSize
- **Seek Time**: Proportional to head movement distance (for HDDs)

## Key Points
- Contiguous allocation suffers from external fragmentation
- Linked allocation has O(n) access time for random access
- Indexed allocation enables O(1) access with multi-level indirection
- Bitmaps allow faster free space lookup than linked lists
- Journaling maintains atomic operations through transaction logs
- Directory hashing reduces search time from O(n) to O(1)
- Copy-on-write (ZFS) prevents data corruption but increases write amplification

## Common Mistakes to Avoid
- Confusing inode numbers with file names
- Assuming all file systems use 512-byte sectors
- Overlooking metadata updates in crash scenarios
- Misinterpreting indirect block levels in size calculations

## Revision Tips
1. Practice block allocation diagrams for different methods
2. Compare ext4's extent tree with NTFS's B+ tree implementation
3. Use `debugfs` (Linux) or `fsutil` (Windows) to inspect real file systems
4. Solve previous DU papers on fragmentation calculations
5. Create comparison charts for FAT32 vs NTFS vs ext4 features

Length: 650 words