# Access Methods

## Introduction

Access methods in operating systems define how data is stored and retrieved from secondary storage devices. As a critical component of file system implementation, access methods bridge the gap between physical storage characteristics and application requirements, determining how processes read/write data efficiently.

Modern operating systems support multiple access methods to accommodate different data patterns:

- Sequential processing of large datasets
- Random access for database systems
- Indexed access for rapid information retrieval
- Memory-mapped access for high-performance applications

Understanding access methods is crucial for:

1. Optimizing I/O performance in resource-constrained systems
2. Designing efficient database management systems
3. Implementing file systems that match application requirements
4. Reducing latency in data-intensive applications

## Key Concepts

### 1. Sequential Access

**Definition:** Strictly ordered data access where records are processed in linear sequence

**Characteristics:**

- Read/write operations proceed from beginning to end
- File pointer maintains current position
- Requires rewinding for repeated access
- Analogous to magnetic tape storage

**Implementation:**

```c
// Typical file operations
FILE *fp = fopen("data.txt", "r");
fseek(fp, 0, SEEK_SET); // Reset to beginning
while(fread(&record, sizeof(record), 1, fp)) {
 // Process record
}
```

**Use Cases:**

- Log file processing
- Backup systems
- Media streaming

### 2. Direct (Random) Access

**Definition:** Immediate access to any record through calculated addressing

**Key Components:**

- Fixed-length records
- Logical block addressing
- Seek operation for position adjustment

**Address Calculation:**

```
Block Address = Starting Address + (Record Number × Record Size)
```

**Implementation Diagram:**

```
[File Header] -> [Block 0] <-> [Block 1] <-> ... <-> [Block N]
 ↑
 Current position
```

**Advantages:**

- Constant time access (O(1))
- Suitable for real-time systems
- Efficient for database operations

### 3. Indexed Sequential Access Method (ISAM)

**Definition:** Hybrid approach combining sequential and direct access using index structures

**Components:**

1. Primary data area (sequential)
2. Index file (direct access)
3. Overflow area (handles new records)

**Access Process:**

1. Search index for key value
2. Retrieve physical address from index
3. Access data block directly

**Example Index Structure:**
| Key Value | Block Address |
|-----------|---------------|
| 1001 | 0x45A2 |
| 1005 | 0x45B6 |
| 1010 | 0x45C8 |

### 4. Memory-Mapped Access

**Definition:** File contents mapped directly to process address space

**Implementation Steps:**

1. Map file to memory range
2. Access file through pointers
3. Synchronize changes with storage

**System Call Example:**

```c
void *addr = mmap(NULL, length, PROT_READ, MAP_PRIVATE, fd, 0);
char *data = (char *)addr; // Access as memory array
```

**Advantages:**

- Eliminates user-space buffers
- Enables shared memory between processes
- Simplifies random access patterns

## Examples

### Example 1: Direct Access Calculation

**Problem:** File with 512-byte blocks contains records of 128 bytes each. Find physical address of record 25.

**Solution:**

```
Block Size = 512 bytes
Records per Block = 512 / 128 = 4
Block Number = 25 / 4 = 6 (integer division)
Offset = (25 % 4) * 128 = 3 * 128 = 384
Physical Address = (Block Number × Block Size) + Offset
 = (6 × 512) + 384 = 3072 + 384 = 3456
```

### Example 2: Indexed Sequential Search

**Problem:** Find student record with ID 20230045 in ISAM structure:

- Primary index: 20230000-20230099 → Block 45
- Block 45 contains records 20230040-20230059

**Solution:**

1. Binary search in index finds block 45
2. Linear search within block finds record 45
3. Access time = Index search + Block search = O(log n) + O(m)

## Real-World Applications

1. **Database Systems:** Direct access for OLTP transactions
2. **Video Editing:** Memory-mapped access for large media files
3. **Scientific Computing:** Indexed access for large datasets
4. **File Systems:** NTFS uses B+ trees for efficient indexing

## Exam Tips

1. **Comparison Matrix:** Memorize key differences between access methods:
   | Method | Access Time | Storage Overhead | Best Use Case |
   |---------------|-------------|-------------------|---------------------|
   | Sequential | O(n) | None | Log processing |
   | Direct | O(1) | Low | Databases |
   | Indexed | O(log n) | High | ISAM files |
   | Memory-Mapped | O(1) | Medium | Shared memory |

2. **Formula Recall:** Remember direct access formula:
   `Physical Address = Base + (Record_Number × Record_Size)`

3. **Index Structure:** Understand multi-level indexes for large files

4. **Page Faults:** Memory-mapped files can cause page faults - mention in answers

5. ** Favorite:** Be prepared to draw and explain ISAM structure diagrams

6. **Recent Trends:** Know memory-mapped I/O advantages for big data applications

7. **Numerical Practice:** Master address calculation problems (like Example 1)
