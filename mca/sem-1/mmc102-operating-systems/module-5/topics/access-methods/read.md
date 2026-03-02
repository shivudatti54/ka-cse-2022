# Access Methods in File Systems


## Table of Contents

- [Access Methods in File Systems](#access-methods-in-file-systems)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Sequential Access](#sequential-access)
  - [Direct Access](#direct-access)
  - [Indexed Access](#indexed-access)
- [Examples](#examples)
  - [Example 1: Sequential Access Implementation](#example-1-sequential-access-implementation)
  - [Example 2: Direct Access Calculation](#example-2-direct-access-calculation)
  - [Example 3: Indexed Access for Efficient Range Queries](#example-3-indexed-access-for-efficient-range-queries)
- [Indexed access concept for range query](#indexed-access-concept-for-range-query)
- [Query: Find all products with price between $100 and $500](#query-find-all-products-with-price-between-100-and-500)
- [Navigate to first leaf node >= min_price](#navigate-to-first-leaf-node--minprice)
- [Exam Tips](#exam-tips)

## Introduction

Access methods define the techniques by which files stored on secondary storage devices can be read from or written to by the operating system. The choice of an appropriate access method significantly impacts the efficiency of file operations and overall system performance. In modern computing environments, where massive amounts of data are processed daily, understanding different access methods becomes crucial for system designers and software developers alike.

File access methods evolved from simple sequential processing in early computing systems to sophisticated indexed and direct access mechanisms in contemporary storage systems. The operating system provides abstraction layers that hide the physical details of storage devices from users and applications, presenting files as linear sequences of bytes or records. Different access methods optimize for different use cases: some excel at processing large datasets sequentially, while others provide rapid random access to specific records within files. The file system, as part of the operating system, implements these access methods and manages the complex mapping between logical file structures and physical storage locations on disks or other storage media.

This topic examines the three primary file access methods—sequential access, direct access, and indexed access—analyzing their implementations, performance characteristics, and optimal application scenarios. Each method represents a different approach to balancing access speed, storage efficiency, and implementation complexity.

## Key Concepts

### Sequential Access

Sequential access is the most fundamental file access method, where records are accessed in a consecutive order, one after another. Starting from the beginning of the file, the system reads or writes each record in sequence, advancing a file pointer that tracks the current position. To access a specific record in a sequentially organized file, the system must read all preceding records, making this method inefficient for random access scenarios.

The read-next operation in sequential access retrieves the next record in the file, automatically advancing the file pointer. Similarly, the write-next operation appends new records to the end of the file. Some sequential access implementations support rewind and backspace operations, allowing the file pointer to be reset to the beginning or moved backward by one or more records. Magnetic tape storage historically exemplified sequential access devices, where physical tape movement was necessary to reach different positions.

Operating systems implement sequential access through various mechanisms. The read() system call, when applied to files without random access positioning, typically performs sequential reading. Buffering plays a crucial role in sequential access performance, where the operating system prefetches subsequent blocks while the application processes current data, reducing the perceived latency of physical disk operations. Sequential access remains highly efficient for batch processing tasks, log file analysis, and scenarios where entire files must be processed systematically.

### Direct Access

Direct access, also known as random access or relative access, enables files to be read from or written to any position without requiring the system to process preceding records. Each record in a directly accessible file possesses a unique identifier, typically a record number, that allows immediate retrieval of the desired record. This method treats the file as a collection of fixed-length records, where the physical location of any record can be calculated mathematically using the record number and record size.

The fundamental formula for direct access positioning is: PHYSICAL ADDRESS = STARTING ADDRESS + (RECORD NUMBER × RECORD SIZE). For example, if a file contains 100-byte records and we wish to access record number 5, the system calculates the position as the file's starting address plus 400 bytes. This mathematical relationship between logical record numbers and physical locations enables the operating system to perform seek operations directly to the desired position.

Direct access files require that all records be of fixed length, allowing precise calculation of offsets. Variable-length records complicate direct access because their positions cannot be predetermined without additional indexing structures. The operating system provides the lseek() system call in Unix-like systems or SetFilePointer() in Windows to position the file pointer for subsequent read or write operations. Disk storage naturally supports direct access through random seek capabilities, making this method highly efficient for applications requiring frequent access to specific records, such as database systems, inventory management, and transaction processing.

Implementation of direct access requires careful consideration of file organization on disk. Contiguous allocation simplifies direct access because the physical location is directly calculable from the logical record number. With linked allocation, direct access becomes impossible because physical locations must be discovered by following pointers. Indexed allocation supports direct access when the index structure maps directly to data blocks.

### Indexed Access

Indexed access combines the benefits of sequential processing with random access capabilities through the use of index structures. An index is a separate data structure that maps keys or record identifiers to their physical locations within the file. The main file contains the actual data records, while the index file contains pointers to these records, organized in a searchable structure typically resembling a B-tree or hash table.

When an application requests access to a specific record, the operating system first consults the index to find the pointer to the desired record's location, then performs the actual data access. This two-step process introduces overhead compared to pure direct access but provides significant advantages for large files where searching through the entire file would be prohibitively slow.

Multiple indexes can exist for a single file, each organized differently and optimized for different access patterns. A personnel file might have separate indexes on employee ID, department, and date of hire, allowing efficient queries based on any of these criteria. This multi-index capability makes indexed access particularly valuable for database systems and information retrieval applications.

The index itself requires management: it must be updated whenever records are inserted or deleted, and it occupies additional storage space. Indexes can be dense or sparse. A dense index contains an entry for every record in the data file, while a sparse index contains entries only for data blocks or segments. Sparse indexes require less space but may require additional searching within data blocks to locate specific records.

B-trees and B+ trees represent the most common index structures in modern file systems due to their balanced performance characteristics. These tree structures maintain logarithmic search complexity regardless of file size and support efficient insertion, deletion, and range queries. The ext4 and NTFS file systems employ B+ tree indexes for directory indexing, enabling fast file lookup even in directories containing millions of files.

## Examples

### Example 1: Sequential Access Implementation

Consider a log file containing system events stored as fixed-length records of 256 bytes each. An application needs to scan all records to find entries with error severity.

```c
// Sequential access example in C
int fd = open("system_log.dat", O_RDONLY);
char buffer[256];
int record_number = 0;

while (read(fd, buffer, 256) > 0) {
    if (buffer[0] == 'E') {  // Error severity marker
        printf("Error at record %d: %.10s\n", record_number, buffer + 1);
    }
    record_number++;
}
close(fd);
```

The system performs 256-byte reads sequentially, advancing the file pointer automatically after each read operation. For a file with 10,000 records, this requires approximately 2.56 MB of sequential disk reads. The operating system likely buffers these reads, combining multiple logical reads into efficient disk I/O operations. Accessing record number 7,500 would require reading all 7,500 preceding records, demonstrating sequential access's limitation for random access patterns.

### Example 2: Direct Access Calculation

A banking application stores account records in a fixed-length format of 512 bytes per account. The accounts file starts at disk block 1000 (block size 4096 bytes). To access account number 1500:

RECORD SIZE = 512 bytes
RECORD NUMBER = 1500
STARTING OFFSET = 1500 × 512 = 768,000 bytes

The system calculates: PHYSICAL OFFSET = 768,000 bytes from file beginning. Converting to block-relative terms: block number = 768000 / 4096 = 187, offset within block = 768000 % 4096 = 2888.

```c
// Direct access in C using lseek
int fd = open("accounts.dat", O_RDWR);
int account_number = 1500;
int record_size = 512;
off_t position = account_number * record_size;

lseek(fd, position, SEEK_SET);  // Direct seek to record
read(fd, buffer, 512);          // Read specific record
```

This operation requires exactly one seek and one read, regardless of which record is accessed. Direct access provides constant-time O(1) access to any record, making it ideal for transaction processing where random account access is frequent.

### Example 3: Indexed Access for Efficient Range Queries

An e-commerce database stores product records in a data file and maintains a secondary index on product prices to enable efficient price-range queries. The index structure uses a B+ tree where leaf nodes contain price-pointer pairs sorted by price.

```python
# Indexed access concept for range query
# Query: Find all products with price between $100 and $500

def range_query(index_root, min_price, max_price):
    # Navigate to first leaf node >= min_price
    current = find_leaf(index_root, min_price)
    
    results = []
    while current is not None:
        for key, pointer in current.entries:
            if key > max_price:
                return results  # Exceeded range
            if key >= min_price:
                record = read_data_record(pointer)
                results.append(record)
        current = current.next_leaf
    return results
```

For a file with one million products, a linear scan would require examining all records. With indexed access, the system navigates the B+ tree in O(log n) time (approximately 20 steps for one million records) to find the first qualifying record, then sequentially reads only the matching records. This demonstrates how indexes transform expensive full-file scans into targeted data retrievals.

## Exam Tips

Understanding file access methods requires knowing the precise characteristics and trade-offs of each approach. Sequential access, direct access, and indexed access each optimize for different access patterns, and exam questions frequently test the ability to select appropriate methods for given scenarios.

WHEN CHOOSING ACCESS METHODS, consider the typical access pattern of the application. Sequential access suits batch processing and complete file scans. Direct access excels when applications need to access random records frequently. Indexed access provides the best of both worlds when applications require both random access and range queries, at the cost of additional storage and maintenance overhead.

DIRECT ACCESS REQUIRES FIXED-LENGTH RECORDS because the physical location must be calculable from the record number. This fundamental requirement frequently appears in exam questions as a key limitation of direct access methods.

INDEX STRUCTURES TRADE SPACE FOR TIME. While indexes consume additional storage and require maintenance during insertions and deletions, they provide dramatically faster access for large files. Understanding this trade-off is essential for system design questions.

MANY REAL-WORLD SYSTEMS COMBINE ACCESS METHODS. Database systems typically use indexed access at the record level while storing data in files that support direct access. File systems may use B-trees for directory indexing while allowing direct access to file data blocks.

THE OPERATING SYSTEM PROVIDES PRIMITIVES, BUT APPLICATIONS IMPLEMENT LOGIC. System calls like read(), write(), and lseek() provide basic capabilities; applications must implement the logic for sequential traversal, direct record numbering, or index traversal on top of these primitives.

UNDERSTAND THE DISK ACCESS COST HIERARCHY. Seek time dominates access cost, followed by rotational delay, then transfer time. Sequential access minimizes seek operations, making it most efficient for bulk transfers. Direct access may incur seek costs for each record, while indexed access adds index traversal overhead before data retrieval.

RECOGNIZE THAT TAPE STORAGE INHERENTLY SUPPORTS ONLY SEQUENTIAL ACCESS. While disk-based storage supports all three methods, magnetic tapes remain fundamentally sequential devices, which explains why early operating systems emphasized sequential processing.