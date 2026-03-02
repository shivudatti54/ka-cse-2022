# Fundamentals of Operating Systems

## Virtual Memory Management: Background; Demand Paging; Copy-on-Write; Page Replacement

### Introduction

Virtual memory is a crucial component of operating systems, allowing multiple processes to share the same physical memory while minimizing the overhead of memory management. In this chapter, we will delve into the background of virtual memory, discuss demand paging and copy-on-write, and explore page replacement algorithms.

### 10.1: Background of Virtual Memory

Virtual memory is a combination of physical memory (RAM) and secondary storage (hard disk). The operating system uses a combination of these two to provide a virtual address space to each process. The virtual address space is divided into pages, and each page is mapped to a physical frame in memory.

**Diagram 1: Virtual Memory Hierarchy**

```
+---------------+
|  Virtual     |
|  Address Space |
+---------------+
         |
         | Mapping Table
         v
+---------------+
|  Physical    |
|  Memory     |
+---------------+
         |
         | Pages
         v
+---------------+
|  Disk Storage |
+---------------+
```

The virtual memory hierarchy consists of the following components:

- **Virtual Address Space**: The virtual address space is the address space allocated to each process. It is divided into pages, and each page is assigned a unique virtual address.
- **Mapping Table**: The mapping table is a data structure that maps virtual addresses to physical addresses. It is also known as the page table.
- **Physical Memory**: Physical memory is the actual RAM used by the system.
- **Disk Storage**: Disk storage is where the system stores data that is not currently in physical memory.

### 10.2: Demand Paging

Demand paging is a technique used to manage virtual memory. It involves loading pages into physical memory only when they are needed by a process.

**Algorithm 1: Demand Paging**

```
1.  Process executes and accesses a page.
2.  Check if the page is in physical memory.
3.  If the page is not in physical memory:
    *   Read the page from disk storage.
    *   Load the page into physical memory.
3.  If the page is in physical memory:
    *   Check if the page is dirty (modified).
    *   If the page is dirty, write it to disk storage.
4.  Update the mapping table to reflect the new page in physical memory.
```

Demand paging is a simple and efficient technique for managing virtual memory. However, it can lead to high page fault rates, which can decrease system performance.

### 10.3: Copy-on-Write

Copy-on-write is a technique used to manage virtual memory that is more efficient than demand paging. It involves creating a copy of a page only when it is modified.

**Algorithm 2: Copy-on-Write**

```
1.  Process executes and accesses a page.
2.  Check if the page is in physical memory.
3.  If the page is not in physical memory:
    *   Read the page from disk storage.
    *   Load the page into physical memory.
4.  If the page is in physical memory:
    *   Check if the page is dirty (modified).
    *   If the page is dirty:
        *   Create a copy of the page in physical memory.
        *   Update the mapping table to reflect the new page in physical memory.
5.  If the page is not dirty, simply update the mapping table to reflect the new page in physical memory.
```

Copy-on-write is more efficient than demand paging because it reduces the number of page faults. However, it can lead to higher memory usage if multiple processes modify the same page.

### 10.4: Page Replacement Algorithms

Page replacement algorithms are used to manage physical memory when it is full and a page needs to be evicted. The most common page replacement algorithms are:

**Algorithm 3: First-In-First-Out (FIFO)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has been in physical memory the longest (first-in-first-out).
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

**Algorithm 4: Least Recently Used (LRU)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has not been in physical memory the longest (least recently used).
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

**Algorithm 5: Optimal Page Replacement (OPR)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that will be needed the earliest in the future.
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

### 13.1: Page Replacement Algorithms

Page replacement algorithms are used to manage physical memory when it is full and a page needs to be evicted. The most common page replacement algorithms are:

**Algorithm 6: First-In-First-Out (FIFO)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has been in physical memory the longest (first-in-first-out).
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

**Algorithm 7: Least Recently Used (LRU)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has not been in physical memory the longest (least recently used).
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

**Algorithm 8: Optimal Page Replacement (OPR)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that will be needed the earliest in the future.
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

### 13.2: Page Replacement Algorithms

Page replacement algorithms are used to manage physical memory when it is full and a page needs to be evicted. The most common page replacement algorithms are:

**Algorithm 9: Second-Chance (SC)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has been in physical memory the longest (first-in-first-out).
    *   Check if the page has been accessed recently.
    *   If the page has not been accessed recently:
        *   Evict the page from physical memory.
    *   Otherwise, do nothing.
3.  Otherwise, do nothing.
```

**Algorithm 10: Random Replacement (RR)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has not been in physical memory the longest (least recently used).
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

### 13.3: Page Replacement Algorithms

Page replacement algorithms are used to manage physical memory when it is full and a page needs to be evicted. The most common page replacement algorithms are:

**Algorithm 11: Least Frequently Used (LFU)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has not been accessed the least.
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

**Algorithm 12: Most Recently Used (MRU)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has been accessed the most recently.
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

### 13.4: Page Replacement Algorithms

Page replacement algorithms are used to manage physical memory when it is full and a page needs to be evicted. The most common page replacement algorithms are:

**Algorithm 13: Clock Algorithm (CA)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has been in physical memory the longest (first-in-first-out).
    *   Check if the page has been accessed recently.
    *   If the page has not been accessed recently:
        *   Evict the page from physical memory.
    *   Otherwise, do nothing.
3.  Otherwise, do nothing.
```

**Algorithm 14: Least Lately Used (LLU)**

```
1.  Check if the physical memory is full.
2.  If the physical memory is full:
    *   Find the page that has not been in physical memory the longest (least recently used).
    *   Evict the page from physical memory.
3.  Otherwise, do nothing.
```

### Further Reading

- "Operating System Concepts" by Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne
- "Virtual Memory" by Andrew S. Tanenbaum
- "Page Replacement Algorithms" by Maurice Wilkes

In conclusion, virtual memory management is a critical component of operating systems. Demand paging, copy-on-write, and page replacement algorithms are used to manage virtual memory. Understanding these concepts is essential for designing and implementing efficient operating systems.
