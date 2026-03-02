# File Allocation Methods

## 1. Contiguous Allocation

Each file occupies contiguous blocks on disk.

**Directory Entry**: (filename, start_block, length)

**Advantages**:

- Simple implementation
- Excellent read performance (sequential access)
- Supports direct access

**Disadvantages**:

- External fragmentation
- File size must be known at creation
- Difficult to grow files

## 2. Linked Allocation

Each block contains pointer to next block.

**Directory Entry**: (filename, start_block, end_block)

**Advantages**:

- No external fragmentation
- Files can grow dynamically
- Simple allocation

**Disadvantages**:

- No direct access (must traverse)
- Pointer space overhead
- Reliability issues (one bad pointer loses rest)

**FAT (File Allocation Table)**:
Move pointers to separate table for faster access.

## 3. Indexed Allocation

Index block contains all pointers to data blocks.

**Directory Entry**: (filename, index_block)

**Advantages**:

- Direct access supported
- No external fragmentation
- Easy file growth

**Disadvantages**:

- Index block overhead
- Index block size limits file size

### Handling Large Files

**Linked Index**: Index blocks linked together

**Multi-level Index**: Index of indexes

```
Index block → [ptr to index block] → [data block pointers]
```

**Combined (Unix inode)**:

- 12 direct pointers
- 1 single indirect
- 1 double indirect
- 1 triple indirect

## Comparison

| Method     | Fragmentation | Direct Access | Growth    |
| ---------- | ------------- | ------------- | --------- |
| Contiguous | External      | Yes           | Difficult |
| Linked     | None          | No            | Easy      |
| Indexed    | None          | Yes           | Easy      |

## Unix Inode Example

With 4KB blocks and 4-byte pointers:

- Direct: 12 × 4KB = 48KB
- Single indirect: 1024 × 4KB = 4MB
- Double indirect: 1024² × 4KB = 4GB
- Triple indirect: 1024³ × 4KB = 4TB

Maximum file size ≈ 4TB
