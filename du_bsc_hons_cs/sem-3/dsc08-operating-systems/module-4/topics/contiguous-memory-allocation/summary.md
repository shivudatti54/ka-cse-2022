# Contiguous Memory Allocation - Summary

## Key Definitions and Concepts

- **Contiguous Memory Allocation**: A memory management technique where each process is allocated a single continuous block of physical memory addresses.

- **Fixed Partitioning**: Divides memory into predetermined partitions at system startup; each partition holds one process.

- **Variable Partitioning**: Creates partitions dynamically based on exact process requirements, eliminating internal fragmentation.

- **Internal Fragmentation**: Wasted space within an allocated partition due to the partition being larger than requested.

- **External Fragmentation**: Scattered free memory blocks that cannot satisfy large process requests despite sufficient total free memory.

- **Compaction**: Moving all allocated memory blocks together to consolidate free space into one contiguous block.

## Important Formulas and Theorems

- **Physical Address Translation**: Physical Address = Base Register + Logical Address
- **Validity Check**: Logical Address must be < Limit Register
- **Internal Fragmentation** (fixed partitioning) = Partition Size - Process Size

## Key Points

- Contiguous allocation provides simple implementation and fast memory access but suffers from fragmentation issues.

- Fixed partitioning allows limited multiprogramming (maximum = number of partitions) but wastes memory through internal fragmentation.

- Variable partitioning minimizes wasted space but can lead to severe external fragmentation over time.

- First Fit is fastest (O(n)); Best Fit minimizes leftover holes but creates more fragments; Worst Fit is generally inefficient.

- Base and limit registers provide both relocation capability and memory protection against unauthorized access.

- External fragmentation can be solved through compaction, though this requires stopping all processes.

- Internal fragmentation can be reduced by having more, smaller partitions but increases overhead.

## Common Mistakes to Avoid

- Confusing internal and external fragmentation—internal occurs within partitions, external occurs between them.

- Forgetting to check if logical address is within bounds (less than limit register) before translation.

- Assuming Best Fit always gives the best memory utilization—it often creates many small unusable fragments.

- Confusing the roles of base and limit registers—both are essential for proper memory management.

## Revision Tips

1. Practice numerical problems with different allocation algorithms to build speed and accuracy.

2. Create a comparison table for all allocation algorithms covering time complexity, advantages, and disadvantages.

3. Draw memory diagrams showing allocation states after each process arrives.

4. Memorize the address translation formula and always verify logical address validity.

5. Review past DU question papers to understand the exam pattern and difficulty level for this topic.