# Page Replacement Algorithms

## Introduction

Memory management is a critical aspect of modern operating systems, and when a process requires more pages than are physically available in RAM, the system must decide which pages to retain in memory and which to evict. This is where **Page Replacement Algorithms** come into play. These algorithms determine which existing page in memory should be replaced when a new page needs to be loaded but no free frames are available.

The importance of efficient page replacement cannot be overstated in the context of system performance. When the **page fault rate** is high, the system spends significant time waiting for pages to be fetched from secondary storage (typically the hard disk), leading to **thrashing**—a severe degradation in performance where the CPU is constantly busy swapping pages rather than executing useful instructions. For University of Delhi's Computer Science students, understanding these algorithms is fundamental to grasping how virtual memory systems operate and how to optimize system performance.

This topic builds directly upon the concepts of paging, virtual memory, and page tables covered in earlier modules. We will examine both theoretical algorithms (like Optimal and LRU) that serve as benchmarks and practical algorithms (like FIFO and Clock) that are actually implemented in real-world operating systems.

## Key Concepts

### The Page Replacement Problem

In a paged virtual memory system, when a process accesses a page that is not currently in physical memory, a **page fault** occurs. The operating system must then:
1. Locate the required page in secondary storage
2. Find a free frame in physical memory (if none exists, select a victim page)
3. Load the required page into the freed frame
4. Update the page table
5. Resume the process execution

The core challenge is step 3: **which page should be replaced?** The goal is to minimize future page faults by selecting the page that will not be needed for the longest time in the future (or has not been used recently).

### Types of Page Replacement Algorithms

#### 1. FIFO (First In First Out)

The **FIFO** algorithm is the simplest approach: the page that has been in memory the longest is replaced first. It maintains a queue of pages in memory ordered by their arrival time.

**Advantages:** Simple to implement, low overhead
**Disadvantages:** Suffers from **Belady's Anomaly**—sometimes replacing more pages can lead to MORE page faults

**Example:** If frames contain pages A, B, C (in that order), and A needs to be replaced, we remove A (the oldest).

#### 2. Optimal Page Replacement (OPT)

This algorithm replaces the page that will not be used for the longest time in the future. While theoretically optimal (minimum possible page faults), it requires **future knowledge** of page references and is impossible to implement in practice. It serves as a theoretical benchmark.

**Key Insight:** OPT demonstrates the upper bound of algorithm performance and is used to evaluate how well practical algorithms perform.

#### 3. LRU (Least Recently Used)

**LRU** replaces the page that has not been used for the longest time in the past. It assumes that pages used recently will likely be used again soon—a principle known as **locality of reference**.

**Implementation challenges:** 
- **Counter implementation:** Each page has a counter incremented on every memory access
- **Stack implementation:** Pages kept in a stack; on access, moved to top
- Both require hardware support for efficiency

**Advantages:** Good approximation of OPT, no Belady's Anomaly
**Disadvantages:** Higher overhead than FIFO, requires special hardware

#### 4. LFU (Least Frequently Used)

LFU replaces the page with the lowest usage count. It assumes that pages used frequently will continue to be used. A variant called **Most Frequently Used (MFU)** is also studied.

#### 5. Second Chance (Clock) Algorithm

This is a practical approximation of LRU. Pages are kept in a circular list, and each page has a **reference bit**:
- On page access, set reference bit to 1
- On replacement, scan circular buffer
- If reference bit = 0, replace this page
- If reference bit = 1, clear it and move to next page

This gives "second chances" to frequently used pages.

#### 6. NRU (Not Recently Used) / Aging

Pages are classified based on two bits:
- **Reference bit (R):** Set when page is accessed
- **Modified bit (M):** Set when page is written to

Classes (in priority order for replacement):
1. Not referenced, not modified (00)
2. Not referenced, modified (01)
3. Referenced, not modified (10)
4. Referenced, modified (11)

Linux and Windows use variants of this approach.

### Belady's Anomaly

This counterintuitive phenomenon occurs in FIFO: sometimes increasing the number of frames leads to MORE page faults. This happens because FIFO doesn't consider page usage patterns. LRU and OPT do not suffer from this anomaly.

### Thrashing

When the page fault rate is very high, the system spends most of its time swapping pages in and out of memory, with little actual computation occurring. This is called **thrashing**. It occurs when:
- Processes demand more pages than available physical memory
- Degree of multiprogramming is too high
- Working set of processes exceeds physical memory

## Examples

### Example 1: FIFO Page Replacement

**Reference String:** 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
**Number of Frames:** 3

**Step-by-Step Solution:**

| Reference | Frame 1 | Frame 2 | Frame 3 | Page Fault |
|-----------|---------|---------|---------|------------|
| 7 | 7 | - | - | ✓ |
| 0 | 7 | 0 | - | ✓ |
| 1 | 7 | 0 | 1 | ✓ |
| 2 | 2 | 0 | 1 | ✓ (replace 7) |
| 0 | 2 | 0 | 1 | ✓ (replace 7 - already gone) |
| 3 | 2 | 3 | 1 | ✓ (replace 0) |
| 0 | 2 | 3 | 0 | ✓ (replace 1) |
| 4 | 4 | 3 | 0 | ✓ (replace 2) |
| 2 | 4 | 2 | 0 | ✓ (replace 3) |
| 3 | 4 | 2 | 3 | ✓ (replace 0) |
| 0 | 0 | 2 | 3 | ✓ (replace 4) |
| 3 | 0 | 2 | 3 | No fault |
| 2 | 0 | 2 | 3 | No fault |

**Total Page Faults = 12**

### Example 2: LRU Page Replacement

**Same Reference String:** 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
**Number of Frames:** 3

**Step-by-Step Solution:**

| Reference | Frame 1 | Frame 2 | Frame 3 | Page Fault |
|-----------|---------|---------|---------|------------|
| 7 | 7 | - | - | ✓ |
| 0 | 7 | 0 | - | ✓ |
| 1 | 7 | 0 | 1 | ✓ |
| 2 | 2 | 0 | 1 | ✓ (replace 7 - LRU) |
| 0 | 2 | 0 | 1 | No fault |
| 3 | 2 | 3 | 1 | ✓ (replace 0 - LRU) |
| 0 | 2 | 3 | 0 | ✓ (replace 1 - LRU) |
| 4 | 4 | 3 | 0 | ✓ (replace 2 - LRU) |
| 2 | 4 | 2 | 0 | ✓ (replace 3 - LRU) |
| 3 | 4 | 2 | 3 | ✓ (replace 0 - LRU) |
| 0 | 0 | 2 | 3 | ✓ (replace 4 - LRU) |
| 3 | 0 | 2 | 3 | No fault |
| 2 | 0 | 2 | 3 | No fault |

**Total Page Faults = 11** (slightly better than FIFO)

### Example 3: Optimal Page Replacement

**Same Reference String:** 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
**Number of Frames:** 3

**Step-by-Step Solution:**

At reference 2 (when we need to replace):
- Page 7: used at position ∞ (never again)
- Page 0: used at positions 5, 7, 11
- Page 1: used at position ∞ (never again)
→ Replace page 1 (furthest in future)

At reference 3:
- Page 7: never again
- Page 0: used again at 5, 7, 11
- Page 2: used again at 9, 13
→ Replace page 7

Continue similarly...

**Total Page Faults = 9** (optimal result)

## Exam Tips

1. **Draw frame tables clearly:** For exam problems, always draw a table showing frame contents after each reference. This helps avoid errors and shows your working.

2. **Understand the difference between hit and fault:** A page hit means the page is already in memory (no fault). A page fault means we need to load from secondary storage.

3. **Remember Belady's Anomaly only applies to FIFO:** If asked which algorithm suffers from Belady's Anomaly, answer FIFO. LRU and Optimal do not have this problem.

4. **Optimal is unrealizable but serves as benchmark:** In exam questions, if you need to compare algorithm efficiency, Optimal will always have the fewest faults.

5. **LRU approximates Optimal well:** In practice, LRU gives results close to Optimal and is implementable with hardware support.

6. **Clock algorithm is practical:** Modern OSes use Clock/Second Chance because it approximates LRU with lower overhead—just remember the reference bit mechanism.

7. **Watch for the reference string pattern:** When solving problems, identify repeating patterns in the reference string. Pages referenced frequently (like 0 in our examples) will often stay in memory.

8. **Know why thrashing occurs:** Be prepared to explain that thrashing happens when processes don't have enough frames, leading to excessive page I/O.

9. **Allocation of frames matters:** Understand the difference between equal allocation and proportional allocation of frames to processes.