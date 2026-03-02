# Page Replacement & Thrashing

## Introduction
Page replacement is a critical mechanism in modern operating systems that manages memory allocation when physical memory becomes full. When a process requests a page not currently in memory (page fault), the OS must select a victim page to replace. The efficiency of this process directly impacts system performance, making replacement algorithms fundamental to memory management.

Thrashing occurs when a system spends more time swapping pages between memory and disk than executing useful work. This pathological condition arises when processes compete for insufficient physical memory, leading to severe performance degradation. Understanding thrashing is crucial for designing robust systems, particularly in memory-intensive applications like database management and virtualized environments.

The combination of effective page replacement policies and thrashing prevention mechanisms forms the backbone of modern virtual memory systems. These concepts are especially relevant in cloud computing environments where resource allocation directly impacts operational costs and service quality.

## Key Concepts
1. **Page Replacement Algorithms**:
   - **FIFO (First-In First-Out)**: Replaces oldest page in memory
   - **Optimal Algorithm**: Theoretical model replacing page not used longest in future
   - **LRU (Least Recently Used)**: Uses past usage to predict future needs
   - **LFU (Least Frequently Used)**: Counts page references for replacement decisions

2. **Thrashing**:
   - Occurs when ∑(Working Sets) > Physical Memory
   - Characterized by high page fault rate (>90% CPU utilization in paging)
   - Detected via locality model and working set analysis

3. **Working Set Model**:
   - Δ (window size) defines process's memory needs over time
   - WSSᵢ (Working Set Size) for process i
   - If ∑WSSᵢ > m (physical frames), thrashing occurs

4. **Prevention Techniques**:
   - Local vs Global allocation policies
   - Page fault frequency thresholding
   - Load control through process suspension

## Examples

**Example 1: LRU vs FIFO Comparison**
Reference string: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2
3 frames: 

LRU Solution:
Page Faults = 9
Final frames: [1, 2, 0]

FIFO Solution:
Page Faults = 12
Final frames: [3, 0, 4]

**Example 2: Thrashing Analysis**
System with 4GB RAM running:
- Database (WS=2.5GB)
- Web Server (WS=1.8GB)
- Analytics Tool (WS=1.0GB)

Total WS = 5.3GB > 4GB → Thrashing occurs
Solution: Suspend analytics tool (new WS=4.3GB) + Add 1GB swap space

**Example 3: Optimal Algorithm**
Reference string: 1 3 0 3 5 6 3
3 frames:

Optimal replacements:
1, 3, 0 → Page fault
Replace 1 (next use at ∞) with 3
Final frames: [3, 0, 5] with 6 page faults

## Exam Tips
1. Always draw page tables for replacement algorithm problems
2. For thrashing questions, calculate ∑WSS first before suggesting solutions
3. Optimal algorithm gives theoretical lower bound - use it as reference
4. Remember Belady's anomaly occurs in FIFO but not LRU/OPT
5. Working set window (Δ) is crucial for thrashing detection - mention its role
6. In numerical problems, track both page faults and frame allocations
7. Real-world applications: Mention cloud VM allocation and container memory limits