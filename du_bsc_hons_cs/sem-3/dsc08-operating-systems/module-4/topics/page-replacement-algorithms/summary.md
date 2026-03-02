# Page Replacement Algorithms — Quick Revision Summary

## Introduction

In a demand paging system, when a process references a page that is not present in physical memory, a **page fault** occurs. The operating system must then bring the required page from secondary storage into a free frame. If no frame is free, a page must be replaced. The strategy used to select a victim page for replacement is called a **page replacement algorithm** — a core component of virtual memory management in operating systems.

---

## Key Concepts

- **Page Fault**: Occurs when a requested page is not in memory (RAM).
- **Frame**: Fixed-size block of physical memory into which pages are loaded.
- **Victim Page**: The page selected for replacement to free a frame.
- **Reference String**: The sequence of page references used to evaluate algorithm performance.
- **Belady's Anomaly**: The counter-intuitive increase in page faults when increasing the number of frames (observed in FIFO).

---

## Major Page Replacement Algorithms

- **FIFO (First-In-First-Out)**: The oldest page in memory is replaced first. Simple to implement but suffers from Belady's anomaly and does not consider page usage frequency.

- **Optimal Page Replacement (OPT)**: Replaces the page that will not be used for the longest time in the future. Provides the lowest possible page faults but is impractical — used primarily as a theoretical benchmark.

- **LRU (Least Recently Used)**: Replaces the page that has not been referenced for the longest time. Closely approximates OPT and performs well in practice. Requires hardware support (counters or stack).

- **LFU (Least Frequently Used)**: Replaces the page with the lowest reference count. Can suffer from performance issues if a page was heavily used earlier but is no longer needed.

- **Second Chance (Clock) Algorithm**: A variant of FIFO that checks if the reference bit is set; pages with the bit set get a second chance and are moved to the back of the queue.

- **NRU (Not Recently Used)**: Classifies pages based on reference and modify bits, replacing the lowest-priority class. Simple and effective.

---

## Comparison and Practical Notes

| Algorithm | Advantage | Disadvantage |
|---|---|---|
| FIFO | Easy to implement | Suffers Belady's anomaly |
| OPT | Minimum page faults | Impossible to implement in practice |
| LRU | Good approximation of OPT | High overhead |
| Second Chance | Efficient, uses reference bit | Approximate only |

Algorithms like **LRU** and **Second Chance** are widely used in real systems due to their practical balance of performance and implementation cost.

---

## Conclusion

Page replacement algorithms are essential for managing virtual memory efficiently. While **FIFO** is the simplest, **LRU** and **Clock** algorithms offer better real-world performance. Understanding these algorithms is critical for minimizing page faults and optimizing system throughput — a key topic in the Delhi University Operating Systems syllabus (Unit–IV: Memory Management).