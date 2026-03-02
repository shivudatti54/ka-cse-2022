# Swapping in Operating Systems - Summary

## Key Definitions and Concepts

- **Swapping**: A memory management technique where an entire process memory is moved between primary memory (RAM) and secondary storage (disk) to allow more processes to run than physical memory would permit.

- **Swap Area**: A reserved portion of secondary storage that serves as backing store for memory pages that cannot fit in physical RAM.

- **Thrashing**: A severe performance degradation that occurs when the system spends excessive time swapping pages in and out of memory rather than executing processes.

- **Demand Paging**: Modern approach where individual memory pages are swapped as needed, rather than swapping entire processes.

## Important Formulas and Theorems

- Swap-out time = Process size / Disk transfer rate
- Effective access time with swapping = (1 - p) × memory access + p × (swap-in time + memory access), where p is the probability of page fault
- Swap space recommendation = Typically 1-2× physical RAM, but varies based on workload

## Key Points

- Swapping enables multiprogramming beyond physical memory limits by treating disk as extended memory

- Pure swapping moves entire process images, while paging moves fixed-size pages (typically 4KB)

- Modern operating systems use demand paging rather than full process swapping for better performance

- Swap space is created as separate partitions (Linux) or page files (Windows)

- Thrashing occurs when physical memory is so constrained that the system constantly swaps pages

- Working set model and page fault frequency are common algorithms to prevent thrashing

- Disk I/O for swapping is orders of magnitude slower than memory access, making swap operations expensive

- The term "swap" in modern systems typically refers to page-level operations, not entire process swapping

## Common Mistakes to Avoid

- Confusing swapping with paging: Swapping = entire process; Paging = individual pages

- Assuming swap space is always bad: Swap space is essential for systems and enables important features like memory overcommit

- Ignoring the performance cost: Excessive swapping severely degrades performance; this is tested frequently

- Mixing up swap area and virtual memory: Swap is one component of virtual memory, which also includes address translation and protection

## Revision Tips

- Practice drawing diagrams showing how a process moves between RAM and swap area

- Memorize the key differences between swapping and paging with concrete examples

- Review thrashing prevention methods as this is a commonly asked exam question

- Understand commands like mkswap, swapon (Linux) and page file configuration (Windows)

- Solve numerical problems involving swap time calculations using given process sizes and disk speeds