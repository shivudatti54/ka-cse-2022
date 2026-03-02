# Contiguous Memory Allocation - Summary

## Key Definitions and Concepts

- CONTIGUOUS MEMORY ALLOCATION: A memory management technique where each process is allocated a single continuous block of physical memory.

- FIXED PARTITIONING: Memory is divided into predetermined partitions at system startup; simple but suffers from internal fragmentation.

- VARIABLE PARTITIONING: Partitions are created dynamically based on process requirements; eliminates internal fragmentation but may cause external fragmentation.

- INTERNAL FRAGMENTATION: Wasted memory within an allocated partition due to fixed partition size being larger than process requirement.

- EXTERNAL FRAGMENTATION: Scattered free memory holes that cannot be used to satisfy a large process request even when total free memory is sufficient.

- COMPACTION: The process of moving all allocated memory blocks together to create one large contiguous hole, eliminating external fragmentation.

## Important Formulas and Theorems

- Physical Address = Base Register + Logical Address
- Valid Logical Address Range: [0, Limit Register - 1]
- Internal Fragmentation = Partition Size - Process Size (for fixed partitioning)
- Memory Utilization = (Allocated Memory / Total Memory) × 100%

## Key Points

- Contiguous memory allocation stores each process in a single continuous block of memory, simplifying address translation.

- Fixed partitioning limits the degree of multiprogramming to the number of partitions and causes internal fragmentation.

- Variable partitioning eliminates internal fragmentation but introduces external fragmentation through scattered holes.

- First Fit is generally the preferred algorithm due to its speed and good memory utilization in practice.

- Best Fit minimizes wasted space per allocation but creates more small holes and is slower.

- Worst Fit tends to worsen fragmentation and is not recommended for practical use.

- Base and limit registers provide both address translation and memory protection in contiguous allocation.

- Compaction can solve external fragmentation but requires significant CPU time and process relocation capability.

## Common Mistakes to Avoid

- Confusing internal and external fragmentation: Remember internal occurs within partitions (fixed), external occurs between partitions (variable).

- Forgetting to check address bounds before translation; always verify logical address is within limit register range.

- When solving allocation problems, not updating the hole list after each allocation; show all intermediate steps.

- Assuming compaction eliminates fragmentation entirely; it only temporarily solves external fragmentation and has overhead.

- In address translation questions, ensure you add base to logical address, not subtract.

## Revision Tips

- Practice drawing memory maps and hole configurations after multiple allocations using different algorithms.

- Create a comparison table of all allocation algorithms covering speed, fragmentation behavior, and use cases.

- Solve numerical problems involving address translation with various base and limit register values.

- Memorize the key differences between fixed and variable partitioning through a two-column comparison.

- Review past examination questions on this topic to understand the pattern and depth of questions asked.