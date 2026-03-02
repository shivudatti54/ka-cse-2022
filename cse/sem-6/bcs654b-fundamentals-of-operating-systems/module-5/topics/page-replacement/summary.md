# Page Replacement - Summary

## Key Definitions and Concepts

- **Page Fault**: Occurs when a process accesses a page not in physical memory
- **Victim Frame**: Selected page frame to be replaced when memory is full
- **Dirty Bit**: Flag indicating if a page has been modified (requires write-back if set)
- **Reference String**: Sequence of page numbers accessed by a process
- **Belady's Anomaly**: Phenomenon where increasing frames _increases_ page faults (FIFO specific)
- **Working Set**: Collection of pages actively used by a process

## Important Formulas and Theorems

```plaintext
1. Page Fault Rate = (Number of Page Faults) / (Total Memory Accesses)
2. FIFO Algorithm: Queue-based replacement (oldest page first)
3. OPT Algorithm: Replace page not used for longest future time (optimal but unrealizable)
4. LRU Algorithm: Track recent usage with counters/stack (past → future prediction)
5. Clock Algorithm: Circular queue with reference bit (second-chance FIFO)
6. Belady's Theorem: OPT and LRU don't suffer from Belady's Anomaly
```

## Key Points

- FIFO uses queue structure but suffers from Belady's Anomaly
- OPT requires future knowledge (used as theoretical benchmark)
- LRU approximates OPT using past access patterns
- Clock algorithm balances efficiency and implementation cost
- Modified pages (dirty bit=1) take 2x I/O time (write-back + read)
- Global vs Local replacement: OS-level vs process-level frame allocation
- Thrashing occurs when page fault rate becomes excessively high
- LRU implementations use: Counter registers, Matrix method, or Stack approach
- Page fault handling involves: Trap, Disk I/O, and TLB update
- Aging technique approximates LRU using reference bits shifted periodically

## Common Mistakes to Avoid

1. Confusing FIFO (queue-based) with LRU (time-based) replacement
2. Forgetting to check/modify dirty bit during page write-back
3. Assuming all page replacements require disk write (only modified pages do)
4. Miscalculating LRU order when multiple pages have same last-used time
5. Overlooking Belady's Anomaly in FIFO-based frame allocation questions

## Revision Tips

1. Practice calculating page faults using 3-frame examples for all algorithms
2. Create comparison table: FIFO vs OPT vs LRU vs Clock (Complexity, Belady's, Implementation)
3. Memorize Belady's Anomaly example: Reference string (1,2,3,4,1,2,5,1,2,3,4,5) with 3 vs 4 frames
4. Focus on LRU implementation details (counter vs stack) and Clock algorithm's circular scan
5. Remember OPT is unrealizable but useful for performance comparison
