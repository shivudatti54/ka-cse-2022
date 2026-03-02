# Page Replacement Algorithms - Summary

## Key Definitions and Concepts

- **Page Fault:** Occurs when a process accesses a page not currently in physical memory
- **Page Replacement:** Selecting a victim page to evict when all frames are occupied
- **Reference String:** The sequence of page numbers accessed by a process
- **Belady's Anomaly:** The counterintuitive phenomenon where increasing frames increases page faults (FIFO only)
- **Thrashing:** Severe performance degradation due to excessive paging activity

## Important Formulas and Theorems

- **Page Fault Rate:** (Page Faults / Total Memory References) × 100%
- **Hit Ratio:** 1 - Page Fault Rate
- **Belady's Anomaly:** Only affects FIFO; LRU and Optimal are anomaly-free

## Key Points

1. **FIFO** replaces the oldest page in memory; simple but suffers from Belady's Anomaly

2. **Optimal (OPT)** replaces the page not used for longest time in future; minimum faults but unrealizable

3. **LRU** replaces least recently used page; good approximation of OPT, no anomaly

4. **Clock Algorithm** uses reference bits to approximate LRU with lower overhead; used in real OS

5. **NRU/ Aging** classifies pages by reference and modified bits; priority-based replacement

6. **LRU requires special hardware** (counters or stacks) due to implementation overhead

7. **Thrashing occurs** when demand exceeds physical memory capacity, causing constant page swapping

8. **Modern OS use hybrid approaches** combining Clock with other techniques

## Common Mistakes to Avoid

- Confusing page fault with page hit—always check if page exists in frames
- Forgetting to update reference bits when using Clock algorithm
- Thinking Optimal can be implemented (it requires future knowledge)
- Believing all algorithms suffer from Belady's Anomaly (only FIFO does)

## Revision Tips

1. Practice 3-4 numerical problems with different reference strings and frame counts
2. Create a comparison table of all algorithms covering advantages, disadvantages, and implementation complexity
3. Remember: Optimal ≤ LRU ≤ FIFO (in terms of page faults) for the same reference string
4. Understand that "recently used" in LRU refers to time of last reference, not last replacement