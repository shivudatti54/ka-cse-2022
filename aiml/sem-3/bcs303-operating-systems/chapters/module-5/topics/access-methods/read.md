# Access Methods

## Introduction

Access methods represent one of the most fundamental aspects of file system design in operating systems. When we create files and store them on secondary storage devices like hard disks, we need systematic approaches to retrieve the stored information efficiently. The way data is accessed directly impacts the performance, efficiency, and practicality of file operations in any computing environment.

In the context of operating systems, an access method refers to the technique or mechanism used to read from or write to a file stored on a storage device. The choice of access method depends heavily on the nature of the data being stored, the type of operations frequently performed, and the performance requirements of the system. Different access methods offer different trade-offs between speed, storage efficiency, and implementation complexity.

Understanding access methods is crucial for computer science students because file systems are ubiquitous in computing. Every application, from simple text editors to complex database management systems, relies on some form of file access mechanism. Moreover, as modern applications deal with increasingly large volumes of data, the efficiency of access methods becomes critical for system performance. This topic forms the backbone of file system implementation and is essential for comprehending how operating systems manage persistent data.

## Key Concepts

### Sequential Access Method

Sequential access is the simplest and most fundamental access method where files are accessed in a sequential manner, one record after another, starting from the beginning of the file. This method treats the file as a linear sequence of records, and the system maintains a pointer to the current position in the file. Each read operation retrieves the next record in sequence, advancing the file pointer automatically.

In sequential access, to read the nth record, the system must first read all (n-1) records that precede it. This approach is similar to reading a cassette tape or scanning through a document from the start. The primary operations supported are read next, write next, and reset (return to the beginning). Operating systems typically provide functions like fseek() in C or seek() in Python to manipulate the file pointer for sequential access.

Sequential access offers several advantages: it is extremely simple to implement, requires minimal overhead in terms of metadata and index structures, and provides excellent performance for operations that process entire files or large portions of files sequentially. However, its major drawback is poor random access performance—accessing a specific record in the middle of a large file requires scanning through all preceding records.

### Direct Access Method

Direct access, also known as random access or relative access, allows files to be accessed in any order without sequential progression. This method treats the file as a collection of fixed-size blocks or records, each identifiable by a unique number or address. The system can directly jump to any record using its relative record number (RN), making it possible to read or write at any position within the file.

In direct access, each record is assigned a relative record number starting from 0 or 1. The physical location of a record can be calculated using the formula: physical location = starting address + (record number × record size). This allows the operating system to calculate the exact byte offset and seek directly to that position using disk seek operations. The main operations include read(n), write(n), and seek(n) where n represents the relative record number.

Direct access is particularly valuable for applications requiring frequent random access to records, such as database systems, airline reservation systems, and transaction processing systems. It provides constant-time access to any record regardless of file size, dramatically improving performance for certain workloads. However, it requires files to be organized in fixed-length records and may suffer from external fragmentation.

### Indexed Access Method

Indexed access combines the benefits of both sequential and direct access methods by using an index structure to locate records quickly. The system maintains an index—a separate data structure containing pointers to the actual data records in the file. This index is typically smaller than the main file and can be searched much faster, either sequentially or using more advanced search algorithms like B-trees.

When a record needs to be accessed, the system first consults the index to find the pointer to that record's physical location, then directly accesses the record. This two-step process adds some overhead but enables efficient access based on key values rather than just positional numbers. Multiple indexes can be created for different keys, providing flexibility in how files are accessed.

The most common implementation uses a primary index on a primary key field and possibly secondary indexes on other frequently searched fields. For example, in a student database file, one might create an index on student ID for direct access and another index on department for querying all students in a particular department. Indexed access is extensively used in database management systems and provides the foundation for sophisticated query processing.

### Keyed Access Method

Keyed access is an advanced form of access that retrieves records based on their content or key value rather than their position in the file. Users specify search criteria or key values, and the system locates matching records without requiring knowledge of their physical arrangement. This method is particularly powerful for database applications where queries are based on data content.

In keyed access, the file system maintains additional metadata about record keys and their relationships. When a search request is made, the system uses this metadata to locate relevant records efficiently. Modern database systems implement sophisticated keyed access using hash tables, B-trees, and other data structures to achieve near-constant time lookups based on key values.

## Examples

### Example 1: Sequential Access in Practice

Consider a log file containing system events recorded throughout a day, where each line represents one event. To analyze the entire day's activity, sequential access is ideal because we need to process all records in chronological order.

```
File: system_log.txt (contains 10,000 event records)

Operation: Read all records starting from the beginning

Step 1: Open file and set pointer to position 0
Step 2: Read first record (pointer automatically advances)
Step 3: Continue reading until end-of-file is reached

Pseudocode:
open("system_log.txt")
while not EOF:
    record = read_next()
    process(record)
close()
```

This approach is memory-efficient as it only needs to hold one record at a time and provides maximum throughput when scanning the entire file. The time complexity for accessing the nth record is O(n).

### Example 2: Direct Access for Transaction Processing

An airline reservation system maintains a file where each record represents a seat on a flight. Using direct access, we can instantly check seat availability or book a specific seat without scanning through all seats.

```
File: Flight_101_seats.dat
- Total seats: 200
- Record size: 100 bytes
- Record 0: Seat 1A, Record 1: Seat 1B, ..., Record 199: Seat 10F

Operation: Book seat 5C (relative record number 4)

Calculation:
Offset = 4 × 100 = 400 bytes from file start
seek(400)  // Move directly to seat 5C's position
write(record_with_booking_info)

Time complexity: O(1) - constant time regardless of file size
```

This direct access approach enables the system to handle thousands of concurrent booking requests efficiently, as each operation requires only one disk seek instead of scanning potentially millions of seat records.

### Example 3: Indexed Access for Database Queries

A university student database contains 50,000 student records, each 200 bytes in size. Without indexing, finding a student by ID would require scanning up to 50,000 records. With indexing, this becomes nearly instantaneous.

```
File: students.dat (50,000 records × 200 bytes = 10 MB)
Index: student_id_index (50,000 entries × 8 bytes = 400 KB)

Operation: Find student with ID "STU2024001234"

Step 1: Search index for key "STU2024001234"
       Index entry found at position 12450
       Contains pointer: byte offset 2,490,000
Step 2: Seek directly to byte offset 2,490,000
Step 3: Read the single record

Without index: Average 25,000 record reads = ~50,000 I/O operations
With index: 1 index search + 1 record read = 2 I/O operations

Performance improvement: 25,000 times faster
```

This example demonstrates why indexed access is essential for large-scale data processing applications, providing dramatic performance improvements for key-based lookups.

## Exam Tips

1. Understand the fundamental difference between sequential and direct access: sequential processes records in order while direct access can jump to any record using relative record numbers.

2. Remember that sequential access is optimal for batch processing and complete file scans, while direct access suits interactive applications requiring random record access.

3. Know that indexed access provides a balance between the two, offering efficient key-based retrieval at the cost of maintaining additional index structures.

4. In exam questions, carefully identify whether the scenario describes sequential, direct, or indexed access based on the operations described.

5. For direct access calculations, remember the formula: byte offset = relative record number × record size.

6. Recognize that indexed access requires two I/O operations: one for the index and one for the actual data record.

7. Understand the trade-offs: sequential access has no storage overhead but poor random access; direct access provides fast access but requires fixed-length records; indexed access offers flexibility but needs additional storage and maintenance.

8. Real-world applications often combine these methods—databases typically use indexed access while also supporting sequential scans for range queries.