# Demand Paging

## Overview

Demand paging loads pages into memory only when needed during execution, rather than loading entire program. This reduces memory requirements, increases multiprogramming degree, and allows programs larger than physical memory through effective use of virtual memory.

## Key Points

- **Lazy Swapper**: Only loads page when referenced, never swaps page before needed
- **Page Fault**: Occurs when CPU references page not in memory, triggers page load from disk
- **Valid-Invalid Bit**: In page table entry, indicates if page is in memory (valid) or on disk (invalid)
- **Page Fault Handling**: Trap to OS, save state, check validity, find free frame, load page from disk, update page table, restart instruction
- **Effective Access Time**: EAT = (1-p) × memory_access + p × page_fault_time, where p = page fault rate
- **Pure Demand Paging**: Start process with no pages in memory, load on demand
- **Prepaging**: Load likely-needed pages in advance to reduce page faults
- **Thrashing**: System spends more time paging than executing, occurs when working set doesn't fit in memory

## Important Concepts

- Page fault service time dominates effective access time (disk access very slow)
- Demand paging enables virtual memory larger than physical memory
- Working set: set of pages process actively uses, must fit in memory to avoid thrashing
- Locality of reference: programs tend to access small portion of address space at any time

## Notes

- Practice EAT calculations: if p=0.01 and page fault takes 8ms, EAT significantly increases
- Understand page fault handling sequence step by step
- Know thrashing symptoms: high page fault rate, low CPU utilization
- Remember demand paging key to virtual memory systems
