# Contiguous Memory Allocation - Summary

## Key Definitions and Concepts

- **Contiguous Memory Allocation**: A memory management technique where each process is allocated a single continuous block of physical memory.

- **Fixed Partitioning**: Memory is divided into a predetermined number of partitions at system startup. Each partition can hold one process.

- **Variable Partitioning**: Memory partitions are created dynamically based on the exact size requested by each process.

- **Internal Fragmentation**: Wasted memory within an allocated block due to the allocated partition being larger than required.

- **External Fragmentation**: Free memory scattered in small, non-contiguous blocks that cannot satisfy a large allocation request.

- **Base Register**: Holds the starting physical address of a process's memory block.

- **Limit Register**: Holds the size of the allocated memory region for a process.

## Important Formulas and Theorems

- **Physical Address Calculation**: Physical Address = Base Register + Logical Address (Offset)

- **Address Validity Check**: Valid if 0 ≤ Logical Address < Limit Register

- **Internal Fragmentation**: Allocated Block Size - Actual Request Size

- **External Fragmentation**: Exists when total free memory > request but no single contiguous block is large enough

## Key Points

- Contiguous allocation provides simple and fast memory access with minimal overhead.

- Fixed partitioning limits the number of concurrent processes and suffers from internal fragmentation.

- Variable partitioning eliminates internal fragmentation but introduces external fragmentation.

- First-fit is the fastest allocation strategy and performs well in practice.

- Best-fit minimizes wasted space but requires searching all free holes.

- Memory protection is implemented efficiently using base and limit registers.

- Compaction can resolve external fragmentation but at high processing cost.

- Address translation in contiguous allocation is a simple addition operation.

## Common Mistakes to Avoid

- Confusing internal and external fragmentation: Internal happens within partitions; external happens between them.

- Forgetting to check address validity against the limit register before memory access.

- Assuming that external fragmentation can be eliminated completely without using non-contiguous allocation.

- Overlooking that compaction requires updating all process memory references, making it expensive.

- Believing that best-fit always provides better memory utilization than first-fit (in practice, first-fit is often preferable).

## Revision Tips

- Practice numerical problems involving allocation and deallocation sequences to calculate fragmentation.

- Draw memory layout diagrams to visualize how processes occupy contiguous blocks.

- Memorize the address translation formula and the address validity condition.

- Compare allocation strategies with small examples to understand their behavior intuitively.

- Review how protection works with base and limit registers for exam questions on memory security.