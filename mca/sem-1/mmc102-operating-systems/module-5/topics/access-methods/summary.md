# Access Methods in File Systems - Summary

## Key Definitions and Concepts

- SEQUENTIAL ACCESS: File reading/writing where records are processed in consecutive order, advancing a file pointer sequentially from start to end.

- DIRECT ACCESS (Random Access): File access method enabling immediate retrieval of any record using its record number, treating the file as an array of fixed-length records.

- INDEXED ACCESS: File access method using auxiliary index structures (typically B-trees) that map keys to record pointers, enabling efficient random and range queries.

- FILE POINTER: A maintained position indicator tracking the current location in a file for sequential read/write operations.

## Important Formulas and Theorems

PHYSICAL ADDRESS FOR DIRECT ACCESS = STARTING ADDRESS + (RECORD NUMBER × RECORD SIZE)

This formula enables O(1) constant-time access to any record in directly organized files by calculating byte offsets mathematically.

## Key Points

- SEQUENTIAL ACCESS provides highest throughput for processing all records but requires O(n) time to reach the nth record.

- DIRECT ACCESS offers constant-time O(1) access to any record but requires fixed-length records for position calculation.

- INDEXED ACCESS combines advantages of both methods through B-tree or hash structures, at the cost of additional storage and index maintenance overhead.

- CONTIGUOUS FILE ALLOCATION simplifies direct access because physical locations map directly to logical positions.

- LINKED ALLOCATION prevents direct access since record locations must be discovered through pointer chains.

- DENSE INDEXES contain entries for every record; SPARSE indexes contain entries for data blocks only.

- OPERATING SYSTEMS provide primitive system calls (read, write, lseek) that applications use to implement higher-level access logic.

## Common Mistakes to Avoid

- CONFUSING file access methods with file allocation methods—they are related but distinct concepts.

- ASSUMING direct access works with variable-length records without understanding position calculation requirements.

- OVERLOOKING the storage overhead of indexes when comparing access methods.

- BELIEVING that indexed access is always superior—it adds complexity and is only beneficial for large files with appropriate query patterns.

## Revision Tips

- MEMORIZE the three access methods and their time complexities: Sequential O(n), Direct O(1), Indexed O(log n) for point queries.

- PRACTICE calculating direct access positions using the formula with different record sizes and record numbers.

- UNDERSTAND that real systems often combine methods: indexes for directory lookup, direct access for data blocks, sequential access for scanning.

- REMEMBER that sequential access remains optimal for batch processing and full-file scans regardless of other method availability.