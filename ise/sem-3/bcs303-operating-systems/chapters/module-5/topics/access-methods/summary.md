# Access Methods - Summary

## Key Definitions and Concepts

- **Sequential Access**: A method where records are accessed in order, starting from the beginning, requiring all preceding records to be read first.

- **Direct Access (Random Access)**: A method allowing any record to be accessed directly through its relative record number using calculated disk addresses.

- **Indexed Access**: A two-level method using an index file that maps keys to data locations, enabling efficient random access with ordered traversal capability.

## Important Formulas and Theorems

- **Direct Access Address Calculation**: Physical Address = Starting Address + (Record Number - 1) × Record Size

- **Sequential Access Complexity**: O(n) where n is the number of records to skip before reaching the target record

- **Indexed Access Complexity**: O(log n) for index search + O(1) for data retrieval using the index pointer

## Key Points

- Sequential access mirrors magnetic tape organization and excels for batch processing of complete files.

- Direct access requires fixed-length records to enable direct physical address calculation through simple arithmetic.

- Indexed access adds a lookup table layer that trades storage overhead for dramatically improved random access performance.

- The file pointer in sequential access tracks current position and automatically advances after each read/write operation.

- Operating systems support all access methods through standard file APIs including fseek(), read(), and write().

- Indexed sequential access combines sequential ordering with random access through clustered and non-clustered indexes.

- Multi-level indexes (like B-trees) reduce index search complexity from linear to logarithmic, handling millions of records efficiently.

## Common Mistakes to Avoid

Confusing sequential access with direct access is a frequent error. Sequential requires reading through records, while direct allows jumping directly to any record number.

Forgetting that direct access requires fixed-length records is a critical mistake. Variable-length records cannot use the simple address calculation formula.

Assuming indexed access is always superior ignores the storage overhead and maintenance complexity of maintaining index structures.

Overlooking the practical use cases for sequential access in modern systems leads to misunderstanding - many applications naturally process data sequentially.

## Revision Tips

Practice calculating direct access addresses using the formula: Starting Address + (Record Number - 1) × Record Size.

Create a comparison table of the three access methods covering time complexity, storage requirements, advantages, disadvantages, and suitable applications.

Remember that real-world systems often combine these methods rather than using them in isolation.

Review file system implementation concepts to understand how access methods interact with allocation methods (contiguous, linked, indexed allocation) and directory structures.