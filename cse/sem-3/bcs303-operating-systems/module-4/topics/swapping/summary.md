# Swapping - Summary

## Key Definitions
- **Swapping**: A memory management technique that temporarily moves processes or portions of processes from main memory to secondary storage.
- **Swap Space**: Reserved area on disk (partition or file) where swapped-out memory is stored.
- **Swap Out**: Operation of writing a process's memory image from RAM to swap space.
- **Swap In**: Operation of reading a process's memory image from swap space back into RAM.
- **Swap Area**: The portion of secondary storage designated for swapping operations.
- **Roll Out/Roll In**: Another term for partial swapping where only portions of a process are moved.

## Important Formulas
- No specific mathematical formulas are associated with swapping, but conceptually:
  - Effective Access Time with Swapping = (1 - p) × memory_access + p × (swap_in + swap_out)
  - Where p is the probability of a page/process being swapped out

## Key Points
1. Swapping is one of the earliest virtual memory techniques, enabling execution of programs larger than physical memory.
2. The entire process (or significant portions) is moved between memory and disk as an atomic unit.
3. Swap space must be allocated on fast storage devices to minimize performance degradation.
4. Modern operating systems primarily use paging rather than process-level swapping, though swapping concepts persist.
5. Swapping involves significant I/O overhead due to moving large amounts of data.
6. The operating system maintains data structures (PCB) to track swap locations and process states.
7. Linux implements swapping at page level through swap areas and the swappiness parameter.
8. Windows uses page files (pagefile.sys) for swap space management.
9. Swapping provides complete process isolation when moving to/from disk.
10. Swapping may occur at process level in extreme memory pressure situations.

## Common Mistakes
1. **Confusing swapping with paging**: Swapping moves entire processes, while paging moves fixed-size pages—these are fundamentally different approaches.
2. **Assuming swapping is obsolete**: While less prominent, swapping is still used in modern systems as a fallback mechanism.
3. **Ignoring the performance cost**: Swapping involves disk I/O which is orders of magnitude slower than memory access; excessive swapping severely degrades performance.
4. **Believing swap space is RAM**: Swap space is on disk and has vastly different performance characteristics than physical memory.