# Contiguous Memory Allocation - Summary

## Key Definitions and Concepts

- CONTIGUOUS MEMORY ALLOCATION: A memory management technique where each process occupies a single continuous block of physical memory throughout its execution lifetime.

- FIXED PARTITIONING: Memory divided into a predetermined number of partitions at system startup; can be equal-sized or unequal-sized.

- VARIABLE PARTITIONING: Partitions created dynamically based on exact memory requirements of processes; number and size vary during system operation.

- INTERNAL FRAGMENTATION: Unused memory space within an allocated partition when the partition exceeds process requirements (occurs in fixed partitioning).

- EXTERNAL FRAGMENTATION: Scattered free memory blocks that cannot satisfy large memory requests despite total free memory being sufficient (occurs in variable partitioning).

- BASE REGISTER: Holds the starting physical address of a process's partition for address translation.

- LIMIT REGISTER: Contains the size of a process's partition for bounds checking and memory protection.

## Important Formulas and Theorems

- MEMORY UTILIZATION = (Memory allocated to processes) / (Total partition size or total memory)

- INTERNAL FRAGMENTATION = Sum of (Allocated partition size - Actual process size) for all processes

- 50-PERCENT RULE: First fit allocation produces external fragmentation consuming approximately 50% of total memory on average

## Key Points

- Contiguous allocation provides SIMPLE address translation using only base and limit registers, making hardware implementation straightforward.

- Fixed partitioning always produces internal fragmentation regardless of process sizes, while variable partitioning eliminates internal fragmentation but introduces external fragmentation.

- FIRST FIT is the fastest allocation algorithm with O(n) average search time, making it commonly used in practice.

- BEST FIT minimizes wasted space within individual allocations but may produce more small fragments and requires searching all free blocks.

- WORST FIT attempts to leave large free blocks for future large allocations but often creates small unusable fragments.

- NEXT FIT distributes allocations more evenly by maintaining a circular scanning position, potentially improving performance in certain scenarios.

- COALESCING merges adjacent free blocks when processes terminate, but external fragmentation may still prevent satisfying large requests.

- MEMORY COMPACTION can eliminate external fragmentation but requires stopping all processes and involves significant overhead.

## Common Mistakes to Avoid

- Confusing internal and external fragmentation—remember internal occurs WITHIN partitions while external occurs BETWEEN partitions.

- Assuming best fit always provides better memory utilization than first fit; in practice, the difference is often negligible while best fit has higher computational cost.

- Forgetting that base and limit registers provide both address translation AND memory protection by preventing access outside allocated partitions.

- Overlooking that total free memory being sufficient does NOT guarantee an allocation can succeed due to external fragmentation.

## Revision Tips

- Practice numerical problems involving partition allocation, fragmentation calculation, and memory utilization computation.

- Create a comparison table of all four allocation algorithms covering speed, fragmentation impact, and use cases.

- Remember that real-world systems often use combinations—fixed partitions as a template with variable sizing within partitions—to balance simplicity and flexibility.

- Review the relationship between contiguous allocation limitations and the motivation for paging/segmentation techniques.