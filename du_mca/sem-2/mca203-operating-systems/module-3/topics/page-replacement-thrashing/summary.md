# Page Replacement & Thrashing - Summary

## Key Definitions and Concepts
- **Page Fault**: Occurs when requested page not in physical memory
- **Thrashing**: Excessive paging degrading system performance
- **Working Set**: Set of pages process needs in Δ time window
- **Belady's Anomaly**: More frames leading to more page faults (FIFO specific)

## Important Formulas and Theorems
- Page Fault Rate = (Page Faults / Memory Accesses) × 100
- Working Set Window: W(t, Δ) = {pages i | referenced in (t-Δ, t]}
- Thrashing Condition: ∑WSSᵢ > Available Physical Frames
- Optimal Algorithm: Minimizes future page faults

## Key Points
- LRU approximates OPT but requires hardware support (reference bits)
- Global replacement allows dynamic frame allocation between processes
- Thrashing detected when CPU utilization drops despite ready processes
- Working set model prevents thrashing by monitoring process locality
- Page Fault Frequency (PFF) algorithm adjusts allocation dynamically
- Load control suspends processes to reduce memory pressure
- Linux uses modified CLOCK algorithm (approximates LRU)

## Common Mistakes to Avoid
- Confusing FIFO's Belady's anomaly with LRU behavior
- Ignoring process locality in working set calculations
- Treating LFU as stack algorithm (it isn't)
- Forgetting to convert process memory needs to page counts

## Revision Tips
1. Practice 5+ numerical problems for each replacement algorithm
2. Create comparison tables of algorithms (implementation, overhead, use cases)
3. Study real-world cases: Windows memory manager vs Linux swap daemon
4. Use memory profiling tools (Valgrind, vmstat) to observe thrashing patterns