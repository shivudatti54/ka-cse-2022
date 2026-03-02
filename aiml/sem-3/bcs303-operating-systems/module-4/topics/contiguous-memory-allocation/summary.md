# Contiguous Memory Allocation - Summary

## Key Definitions

- **Contiguous Memory Allocation**: A memory management technique where each process is allocated a single continuous block of physical memory.

- **Fixed Partitioning**: Memory divided into a predetermined number of partitions at system startup; each partition holds one process.

- **Variable Partitioning**: Partitions created dynamically based on exact process memory requirements.

- **Internal Fragmentation**: Wasted memory within an allocated partition due to the partition being larger than requested.

- **External Fragmentation**: Scattered free memory blocks that cannot satisfy a memory request despite total free memory being sufficient.

- **Compaction**: Process of moving allocated memory blocks to collect all free memory into one contiguous region.

## Important Formulas

- **Internal Fragmentation** = Partition Size - Process Size

- **External Fragmentation** = Sum of all free blocks - Total memory requested

- **Physical Address** = Base Register + Logical Address

- **Address Validity Check**: Logical Address < Limit Register

## Key Points

1. Contiguous allocation was the primary memory management technique in early operating systems.

2. Fixed partitioning eliminates external fragmentation but suffers from internal fragmentation.

3. Variable partitioning eliminates internal fragmentation but can lead to severe external fragmentation.

4. First fit is generally preferred due to its speed and reasonable fragmentation characteristics.

5. Best fit minimizes wasted space per allocation but maximizes external fragmentation over time.

6. The 50-percent rule states that average free block size stabilizes at half the largest block.

7. Compaction can eliminate external fragmentation but requires process relocation and causes system overhead.

8. Modern operating systems use paging and segmentation rather than pure contiguous allocation.

## Common Mistakes

1. **Confusing fragmentation types**: Students often confuse internal and external fragmentation; internal is wasted space within partitions, external is scattered free blocks between partitions.

2. **Forgetting compaction limitations**: Many students incorrectly assume compaction is always practical without considering the overhead and downtime.

3. **Ignoring address translation**: In base-register systems, physical addresses require adding the base register value to logical addresses.

4. **Algorithm selection errors**: Assuming best fit always produces less fragmentation than first fit; in practice, first fit often performs comparably or better.