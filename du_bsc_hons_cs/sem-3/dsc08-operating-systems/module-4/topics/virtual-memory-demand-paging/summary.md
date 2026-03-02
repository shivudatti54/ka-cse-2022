# Virtual Memory — Demand Paging

## Introduction
Virtual Memory is a memory management technique that allows execution of processes that may not be completely in physical memory. **Demand Paging** is a virtual memory implementation where pages are loaded into memory only when requested by a running process (i.e., on demand), enabling efficient use of limited physical memory.

---

## Key Concepts

### 1. Basic Terminology
- **Page**: Fixed-size logical block of a process
- **Frame**: Fixed-size physical memory block
- **Page Table**: Maps virtual pages to physical frames
- **Valid/Invalid Bit**: Indicates whether page is in memory
- **Dirty Bit**: Tracks if page was modified

### 2. Demand Paging Mechanism
- Process starts with no pages in memory
- Page fault occurs when referenced page is not in memory (invalid bit)
- OS loads required page from secondary storage (disk) into a free frame
- Page table is updated; valid bit set
- Instruction is restarted

### 3. Page Fault Handling Steps
1. Trap to OS; save registers/process state
2. Check validity of memory reference
3. Locate required page on disk
4. Find free frame; if none, apply replacement algorithm
5. Read page from disk into frame
6. Update page table
7. Restart interrupted instruction

### 4. Performance — Effective Access Time (EAT)
```
EAT = (1 - p) × memory_access_time + p × page_fault_time
```
Where **p** = page fault rate. Goal: minimize p for faster execution.

### 5. Page Replacement Algorithms
- **FIFO**: Replace oldest page (simple, but suffers from Belady's Anomaly)
- **Optimal (OPT)**: Replace page not used for longest time (theoretical benchmark)
- **LRU (Least Recently Used)**: Approximates OPT; uses stack property
- **Second Chance / Clock**: Modified FIFO with reference bit
- **NFU**: Not Frequently Used; uses counter

### 6. Frame Allocation
- **Fixed Allocation**: Equal frames per process
- **Proportional Allocation**: Frames based on process size
- **Priority Allocation**: Larger allocation to higher-priority processes

### 7. Thrashing
- Excessive page fault activity due to insufficient frames
- CPU utilization drops; performance degrades
- **Working Set Model**: Keeps active pages in memory
- **Page Fault Frequency**: Controls degree of multiprogramming

---

## Conclusion
Demand Paging is fundamental to modern OS memory management, enabling processes larger than physical memory to execute efficiently. Understanding page replacement algorithms, frame allocation, and thrashing is essential for exam success and system design.

---

*Reference: Delhi University BSc (Hons) CS — NEP 2024 UGCF Syllabus (Operating Systems Unit: Memory Management)*