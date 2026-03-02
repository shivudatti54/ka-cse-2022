# File Concepts, Attributes, and Access Methods - Summary

## Key Definitions and Concepts

- **File**: A named collection of related information stored on secondary storage, representing the basic unit of data storage from a user's perspective.

- **File Attribute**: Metadata that describes properties of a file including name, identifier, type, location, size, timestamps, owner, and protection information.

- **File Access Method**: The technique used to read from or write to a file—sequential, direct (random), or indexed.

- **File Directory**: A data structure that maps file names to their attributes and locations, organizing files hierarchically.

## Important Formulas and Theorems

- **Direct Access Address Calculation**: For a file with fixed-length records of size S bytes, the byte offset for record number n (0-indexed) is: `address = base_address + (n × S)`

- **Sequential Access Complexity**: O(n) to access the nth record; O(1) amortized for consecutive records.

- **Indexed Access Complexity**: O(log n) for index search + O(1) for data access = O(log n) total.

## Key Points

1. Files provide an abstraction layer between users/applications and physical storage devices.

2. Common file attributes include name, unique identifier, type, location (pointer to data blocks), size, timestamps (creation, modification, access), owner, and protection permissions.

3. **Sequential Access**: Records accessed in order; simple to implement; efficient for batch processing and log files; file pointer advances after each operation.

4. **Direct Access**: Records accessed by relative number; requires fixed-length records; enables O(1) access to any record; suitable for database and transaction processing systems.

5. **Indexed Access**: Uses a separate index structure (B-tree, hash table) to map keys to record locations; trade-off between faster access and additional storage overhead for the index.

6. Protection information in UNIX systems uses 9 bits: 3 for owner (rwx), 3 for group (rwx), 3 for others (rwx).

7. Time stamps include creation time, last modification time, and last access time—each updated under different conditions.

8. Directory files contain entries mapping file names to their i-nodes or FAT entries.

9. The choice of access method depends on application requirements—sequential for ordered processing, direct for random access, indexed for large files requiring search operations.

## Common Mistakes to Avoid

1. Confusing file name with file identifier—the name is for users, the identifier is the internal numeric reference used by the system.

2. Assuming all access methods provide the same performance—sequential access to the 1000th record requires reading 999 preceding records, while direct access reaches it directly.

3. Forgetting that indexed access requires additional storage space for the index structure.

4. Overlooking the requirement for fixed-length records in pure direct access implementations.

5. Not distinguishing between modification time (file content changed) and access time (file was read or executed).

## Revision Tips

1. Practice calculating direct access addresses: given record size and record number, compute the byte offset.

2. Create a comparison table of access methods covering efficiency, storage overhead, and use cases.

3. Review the UNIX file permission representation (rwxr-xr-x format) and understand what each permission means.

4. Remember that directories in most OSs are implemented as special files containing file entry listings.

5. Solve previous year DU exam questions on file attributes and access methods to understand the exam pattern and important topics.