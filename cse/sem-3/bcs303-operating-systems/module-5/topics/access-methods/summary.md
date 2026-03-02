# Access Methods - Summary

## Key Definitions
- **Sequential Access**: A file access method where records are accessed in linear order, requiring all preceding records to be read to reach a specific record.
- **Direct Access**: A file access method allowing records to be accessed directly using record numbers, assuming fixed-length records and computed physical addresses.
- **Indexed Access**: A file access method that uses auxiliary index structures to locate records, providing efficient random access while supporting range queries.
- **Record Blocking**: Grouping multiple logical records into single physical blocks to improve I/O efficiency.

## Important Formulas
- **Direct Access Address Calculation**: Physical Address = Base Address + (Record Number × Record Size)
- **Direct Access Time Complexity**: O(1) for any record position
- **Sequential Access Time Complexity**: O(n) in worst case, where n is the number of records to scan

## Key Points
1. Sequential access is the simplest method, ideal for batch processing but inefficient for random access to specific records.
2. Direct access provides constant-time O(1) access but requires fixed-length records and pre-allocated file space.
3. Indexed access combines direct access speed with flexibility, using tree-based structures for efficient search.
4. The choice of access method significantly impacts application performance based on access patterns.
5. Modern operating systems provide multiple access methods to support diverse application requirements.
6. Indexed access incurs storage overhead for maintaining index structures but dramatically improves selective query performance.
7. B-trees and B+trees are commonly used for indexed access due to their balanced performance characteristics.

## Common Mistakes
1. Confusing sequential access with the inability to skip records—sequential access can skip forward efficiently but cannot go backward without repositioning.
2. Assuming direct access always outperforms sequential access—for processing entire files, sequential access is often superior due to reduced seek overhead.
3. Ignoring the storage overhead of indexed access when evaluating system requirements.
4. Forgetting that indexed access typically requires two disk operations (index lookup + data retrieval) compared to one for direct access.
5. Overlooking the impact of record size on direct access efficiency—larger records reduce the number of records per block but increase per-record access time.