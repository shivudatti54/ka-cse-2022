# File System Structure - Summary

## Key Definitions

- **File System**: OS component that provides persistent data storage through files and directories
- **inode**: Index node; metadata structure storing file attributes and data block pointers
- **Boot Block**: First disk sector(s) containing bootstrap code for system startup
- **Superblock**: File system metadata containing size, free blocks, and configuration information
- **Virtual File System (VFS)**: Abstraction layer providing unified interface for multiple file system types
- **Extent**: Contiguous range of blocks allocated to a file; reduces metadata overhead
- **Directory Entry**: Structure mapping file names to internal file identifiers

## Important Formulas

- Maximum file size with triple indirect addressing: d + (s² × b) + (s³ × b²), where d = direct blocks, s = single indirect block entries, b = block size
- Number of block pointers in n-level indirect: s^n (where s = entries per indirect block, typically 1024 for 4KB blocks)

## Key Points

- File systems use layered architecture to separate concerns and enable modular design
- Boot block and superblock are critical structures required for file system mounting
- Inodes use direct, single indirect, double indirect, and triple indirect pointers for scalability
- Free space management employs bit vectors, linked lists, or grouping techniques
- VFS enables multiple file systems to coexist through a common interface
- Directory structures map human-readable names to internal file identifiers
- Modern file systems use extent-based allocation for improved large file performance

## Common Mistakes

- Confusing the boot block (bootstrap code) with the superblock (file system metadata)
- Believing that directories contain actual file data instead of file metadata and pointers
- Assuming all file systems use inodes; FAT uses file allocation tables instead
- Overlooking the role of VFS in supporting multiple file system types
- Forgetting that inode metadata does not include the file name (stored in directory entries)