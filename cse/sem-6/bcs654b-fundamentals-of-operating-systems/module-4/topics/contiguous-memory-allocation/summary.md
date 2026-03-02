# Contiguous Memory Allocation - Summary

## Key Definitions and Concepts

- **Contiguous Allocation**: Memory management technique where each process occupies a single contiguous block of physical memory
- **Partitioning**: Division of memory into fixed/variable-sized sections for process allocation
- **Internal Fragmentation**: Wasted space within allocated memory blocks (block size > process size)
- **External Fragmentation**: Total free memory exists but not in contiguous blocks to satisfy requests
- **Memory Compaction**: Technique to reduce external fragmentation by relocating processes
- **Base & Limit Registers**: Hardware registers used for memory protection in contiguous allocation

## Important Formulas and Theorems

1. **Internal Fragmentation Calculation**:
   ```
   Internal Fragmentation = Block Size - Process Size
   ```
2. **External Fragmentation**:
   ```
   Total Free Memory = Σ(Free Blocks)
   Largest Contiguous Block = Max(Free Blocks)
   ```
3. **Memory Utilization**:
   ```
   Utilization = (Total Process Memory) / (Total Physical Memory) × 100%
   ```

## Key Points

- Three main allocation strategies:
  - **First Fit**: Allocate first available block ≥ required size
  - **Best Fit**: Allocate smallest block ≥ required size
  - **Worst Fit**: Allocate largest available block
- Fixed vs Variable Partitioning:
  - Fixed: Predefined equal/unequal partitions (OS/360)
  - Variable: Dynamic partition creation (Modern OS)
- Advantages:
  - Simple implementation
  - Fast memory access (sequential addressing)
- Disadvantages:
  - External fragmentation (50% rule: statistical average)
  - Memory waste from internal fragmentation
  - Difficult to implement for growing processes
- Modern Applications:
  - Embedded systems with fixed memory requirements
  - Boot loaders and real-time operating systems

## Common Mistakes to Avoid

1. Confusing internal vs external fragmentation:
   - Internal: Within allocated blocks
   - External: Between allocated blocks
2. Assuming best-fit always minimizes fragmentation:
   - Creates many small unusable blocks
3. Overlooking compaction overhead:
   - Requires process suspension and relocation
4. Mixing up allocation strategies:
   - First-fit: Fast but average utilization
   - Best-fit: Slower but better utilization
   - Worst-fit: Leaves large leftover blocks

## Revision Tips

1. Practice allocation simulations:
   - Create tables showing memory blocks before/after allocation
   - Calculate fragmentation for different strategies
2. Remember the "50% rule":
   - For N allocated blocks, expect N/2 blocks lost to external fragmentation
3. Compare with non-contiguous methods:
   - Paging: No external fragmentation
   - Segmentation: External fragmentation possible
4. Use mnemonics:
   - **FF**BFWF (First Fit, Best Fit, Worst Fit)
   - **B**est fit leaves **B**iggest holes (incorrect - actually creates small holes)
