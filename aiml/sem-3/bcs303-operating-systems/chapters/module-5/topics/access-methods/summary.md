# Access Methods - Summary

## Key Definitions and Concepts

- Access Method: The technique used by an operating system to read from or write to files stored on secondary storage devices.

- Sequential Access: A method where files are accessed one record after another in sequence, using a file pointer that advances with each read operation.

- Direct Access (Random Access): A method that allows accessing any record directly using its relative record number, treating the file as a collection of fixed-size blocks.

- Indexed Access: A method that uses index structures containing pointers to records, enabling efficient key-based retrieval through a two-step lookup process.

- Keyed Access: An advanced method that retrieves records based on content or key values rather than physical positions.

## Important Formulas and Theorems

- Direct Access Byte Offset: Physical location = Starting address + (Relative record number × Record size)

- Sequential Access Complexity: O(n) time to access the nth record, where n is the position in file

- Direct Access Complexity: O(1) constant time for any record regardless of position

- Indexed Access I/O: Requires 2 I/O operations (1 for index + 1 for data) for single record retrieval

## Key Points

- Sequential access is simplest to implement with minimal overhead but poor random access performance

- Direct access requires fixed-length records and provides constant-time access to any record

- Indexed access balances performance and flexibility using auxiliary index structures

- The choice of access method depends on application requirements: sequential for batch processing, direct for transaction systems, indexed for database queries

- Modern file systems often combine multiple access methods to handle diverse workloads

- Index structures require additional storage space and must be maintained when records are inserted, deleted, or updated

- External fragmentation is a concern in direct access files when records are deleted or vary in size

## Common Mistakes to Avoid

- Confusing sequential access with no access—sequential access DOES allow moving through files, just not randomly

- Forgetting that direct access requires calculation of byte offsets before seeking

- Overlooking the storage overhead of indexes in indexed access systems

- Assuming one access method is universally superior—context determines the best choice

## Revision Tips

- Practice calculating byte offsets for direct access problems using different record sizes

- Create comparison tables distinguishing features of each access method

- Visualize how each access method works with simple examples using small files

- Review operating system laboratory exercises that implement file access operations

- Remember that real-world systems combine these methods rather than using them in isolation