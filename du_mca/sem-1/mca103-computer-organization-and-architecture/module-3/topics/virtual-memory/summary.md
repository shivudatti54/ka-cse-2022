# Virtual Memory - Summary

## Key Definitions and Concepts
- Page Fault: Trap when accessed page not in memory
- Dirty Bit: Indicates modified page needing writeback
- Belady's Anomaly: FIFO can increase faults with more frames
- Copy-on-Write: Memory optimization in process forking
- Swap Space: Disk area for page storage

## Important Formulas and Theorems
- Effective Access Time: EAT = (1-p)*TM + p*TD (p=page fault rate)
- Working Set Window: W(t, Δ) = {pages in (t-Δ, t)}
- Locality Principle: Processes access memory in localized patterns
- Page Fault Frequency Algorithm: Adjusts frame allocation dynamically

## Key Points
- Virtual memory enables processes to exceed physical memory limits
- TLB reduces address translation overhead through caching
- LRU approximates OPT but requires hardware support
- Multi-level page tables save space for sparse address spaces
- Thrashing reduces CPU utilization due to excessive paging
- Modern systems use combined paging/segmentation (e.g., x86-64)
- Page size selection involves tradeoffs between fragmentation and table size

## Common Mistakes to Avoid
- Confusing page faults with TLB misses
- Forgetting to update reference/dirty bits in algorithms
- Assuming Optimal replacement is implementable in practice
- Neglecting disk I/O time in performance calculations
- Mixing physical and virtual addresses in diagrams

## Revision Tips
- Practice page replacement algorithms with different reference strings
- Memorize EAT formula components and typical values
- Compare Windows/Linux page file management strategies
- Use memory hierarchy diagrams to visualize caching layers
- Solve previous years' DU questions on TLB calculations

Length: 400-800 words