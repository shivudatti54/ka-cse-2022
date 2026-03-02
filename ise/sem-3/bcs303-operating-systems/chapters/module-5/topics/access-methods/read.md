# Access Methods

## Introduction

Access methods define how data is retrieved from and written to secondary storage devices in a computer system. In operating systems, the file system provides the abstraction layer that enables users and applications to interact with data stored on disks without understanding the physical details of storage media. Access methods represent one of the most fundamental aspects of file system design, determining not only how efficiently data can be retrieved but also influencing the overall performance of the entire computing system.

The choice of an appropriate access method has profound implications for system performance, storage efficiency, and application suitability. Different access methods have emerged to address varying requirements - from simple sequential processing of log files to rapid random access needed by database systems. Understanding these methods is essential for computer science students because file I/O operations constitute a significant portion of most application workloads, and selecting the wrong access method can dramatically degrade system performance.

In the context of the University of Delhi's Computer Science curriculum, this topic builds upon the foundational concepts of file systems and prepares students to understand how operating systems manage the critical task of data persistence and retrieval. The three primary access methods - Sequential Access, Direct Access, and Indexed Access - each represent different trade-offs between complexity, speed, and storage overhead that system designers must carefully consider.

## Key Concepts

### Sequential Access

Sequential access is the oldest and simplest method of accessing files stored on magnetic media. In this approach, records are processed in the order they appear in the file, starting from the beginning and proceeding through each record until the desired record is found. This method mirrors the physical characteristics of magnetic tape, where accessing a specific record requires reading all preceding records.

The fundamental operation in sequential access is the READ NEXT operation, which retrieves the next record in the file. To access a record at position n, the system must read all records from position 1 through n-1. Similarly, WRITE NEXT appends data to the end of the file. While this may seem inefficient for random access scenarios, sequential access offers significant advantages in certain contexts: it provides excellent performance for batch processing, simplifies file organization, and requires minimal metadata overhead.

Operating systems implement sequential access through file pointers that track the current position in the file. Each read operation advances the pointer by the size of the record being read. Modern operating systems still support sequential access as the default mode because many applications naturally process data sequentially - consider processing log files, analyzing sensor data streams, or reading configuration files.

The time complexity for finding a record at position n in a sequential file is O(n), making this method inefficient for random access patterns. However, for complete file scans, sequential access achieves optimal disk I/O performance because the read head moves in a continuous path, minimizing seek operations.

### Direct Access

Direct access, also known as random access or relative access, allows records to be accessed in any order without reading intermediate records. This method treats the file as a collection of fixed-size records, each accessible through its record number or relative position. The file is conceptualized as a numbered sequence of blocks, and any block can be directly accessed by computing its physical location on the storage medium.

The fundamental operation in direct access is the READ(n) operation, which directly retrieves the record with relative record number n. Similarly, WRITE(n) writes data to record number n. The physical location of record n is calculated using the formula: starting address + (n × record size). This direct computation eliminates the need to scan through preceding records, providing constant-time access O(1) to any record regardless of its position.

Direct access files are particularly suitable for applications requiring frequent random access patterns. Database management systems extensively use direct access methods because they often need to retrieve specific records based on primary keys or indexed attributes. Transaction processing systems, airline reservation systems, and banking applications all rely on the ability to quickly access arbitrary records.

However, direct access has certain limitations. The file must be organized with fixed-length records to enable direct calculation of physical addresses. Additionally, maintaining data integrity requires careful handling of concurrent access and system crashes, as partial writes can corrupt the file structure. Operating systems provide file system calls like lseek() in Unix or SetFilePointer() in Windows to support direct access by repositioning the file pointer to any offset within the file.

### Indexed Access

Indexed access combines the benefits of sequential and direct access methods through a two-level structure. An index file serves as a lookup table that maps key values or record numbers to physical locations in the data file. This additional layer of indirection enables efficient access to records based on search keys while maintaining the ability to traverse records in order.

The index itself is typically a small file that can be loaded into memory, containing pairs of key values and corresponding record pointers. When accessing a record, the system first searches the index to find the appropriate entry, then uses the pointer to directly access the record in the data file. This two-step process dramatically reduces the number of disk I/O operations required, especially for large files.

Several variations of indexed access exist to address different requirements. The simplest form uses a single-level index, where one index file provides direct access to the data file. More sophisticated implementations employ multi-level indexes, where a primary index points to secondary indexes, which in turn point to the actual data records. This hierarchical structure, similar to a B-tree or B+tree, enables efficient handling of millions of records with only a few disk accesses.

Indexed sequential access is a particularly important variant that combines sequential and indexed access. Files organized in this manner can be processed sequentially in key order or accessed randomly through the index. Database systems extensively use this approach, maintaining clustered indexes that determine the physical order of records and non-clustered indexes that provide alternative access paths.

The trade-off with indexed access is the storage overhead required for maintaining the index structure. Additionally, index files must be updated whenever records are inserted, deleted, or modified, adding complexity to write operations. Despite these costs, indexed access remains the preferred method for applications requiring both efficient random access and ordered traversal of records.

### Comparison of Access Methods

Understanding when to use each access method requires analyzing the access patterns of the application. Sequential access excels when processing all records or when access naturally follows the file order. Direct access provides the best performance when records are accessed randomly but the record structure is simple. Indexed access offers the greatest flexibility at the cost of additional storage and maintenance overhead.

Operating systems typically provide APIs that support all three access methods. The choice of which method to use depends on factors including the expected access pattern, file size, required access time, and the frequency of insert and delete operations. Modern file systems often combine these methods, providing sequential access as the default while offering indexed access through database engines or specialized file formats.

## Examples

### Example 1: Sequential Access Implementation

Consider a log file containing system events, where each record is 128 bytes. To find the 1000th event, a sequential access program would need to read and discard the first 999 records (approximately 127,872 bytes) before reaching the desired record.

```c
// Sequential access example in C
FILE *logfile = fopen("system.log", "r");
char buffer[128];

// Move to beginning (implicit)
fseek(logfile, 0, SEEK_SET);

// Read first 999 records and discard
for (int i = 0; i < 999; i++) {
    fread(buffer, 128, 1, logfile);
}

// Now read the 1000th record
fread(buffer, 128, 1, logfile);
printf("Event: %s\n", buffer);

fclose(logfile);
```

In this scenario, if each disk read operation transfers 4KB (the typical filesystem block size), reading 999 records would require approximately 32 disk I/O operations. The time complexity is O(n) where n is the record number.

### Example 2: Direct Access Calculation

Using direct access with 128-byte fixed records, the 1000th record is located at byte offset 127,872 (0-indexed: (1000-1) × 128 = 127,872). The system can seek directly to this position.

```c
// Direct access example in C
FILE *datafile = fopen("records.dat", "r");
char buffer[128];
int recordNumber = 1000;

// Calculate offset: (recordNumber - 1) * recordSize
long offset = (recordNumber - 1) * 128;

// Seek directly to the record
fseek(datafile, offset, SEEK_SET);

// Read the record in one operation
fread(buffer, 128, 1, datafile);
printf("Record: %s\n", buffer);

fclose(datafile);
```

This operation requires exactly one disk seek and one read operation, providing O(1) access time regardless of the record number. The improvement over sequential access is dramatic for large files with random access patterns.

### Example 3: Indexed Access for Database Query

Consider a student database file with 10,000 records, each 256 bytes. Without an index, finding a student by registration number would require scanning up to 10,000 records (O(n) complexity). With a primary index on registration number:

The index file contains 10,000 entries, each 12 bytes (8-byte key + 4-byte pointer), totaling 120KB. This index fits in memory. To find a specific student:

1. Binary search the index: log₂(10,000) ≈ 14 comparisons
2. Read the single data block containing the record

Total disk I/O: 1 (index search in memory) + 1 (data record) = 2 operations. This represents a 5,000x improvement over linear search in the worst case.

## Exam Tips

For University of Delhi semester examinations, students should focus on the following key aspects of access methods:

Understanding the fundamental difference between sequential and direct access forms the core of this topic. Sequential access requires reading through all preceding records (O(n) complexity), while direct access provides constant-time retrieval (O(1) complexity) through direct calculation of physical addresses.

The three primary access methods - Sequential, Direct, and Indexed - each have specific use cases that students must memorize. Sequential is ideal for batch processing and log files, Direct suits database applications with random access patterns, and Indexed provides flexibility for both random access and ordered traversal.

Students should be able to explain why direct access requires fixed-length records. The ability to compute physical addresses as (starting address + record number × record size) depends on uniform record sizes.

The concept of file pointers in sequential access is important. The operating system maintains a read/write pointer that advances automatically after each operation, and this pointer can be repositioned using SEEK_SET, SEEK_CUR, and SEEK_END operations.

Indexed access introduces the concept of a two-level structure with an index file providing a mapping between keys and data locations. Students should understand how this reduces disk I/O operations from linear to logarithmic complexity.

Time complexity analysis for different access methods frequently appears in examinations. Be prepared to compare the number of disk operations required to find the nth record using each method.

The trade-offs between access methods - storage overhead, access speed, and maintenance complexity - are commonly tested through short answer and reasoning questions.

Understanding that modern operating systems provide APIs supporting all access methods demonstrates practical knowledge. Functions like fseek() and ftell() in C support both sequential and direct access modes.