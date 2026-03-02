# Memory Management

## Introduction

Memory management is one of the most critical functions of any operating system. In simple terms, it refers to the process of controlling and coordinating computer memory, allocating portions called blocks to various running programs to optimize overall system performance. Without effective memory management, a computer system would be severely limited in its ability to run multiple programs simultaneously, leading to inefficient utilization of available resources.

The importance of memory management becomes evident when we consider the fundamental constraint in computer systems: physical memory (RAM) is finite and expensive, while the demand for memory from applications is virtually unlimited. Modern operating systems address this imbalance through various sophisticated techniques that create an illusion of abundant memory through virtual memory systems. This allows programs larger than physical memory to execute, enables process isolation, and facilitates efficient sharing of memory between processes.

For students preparing for DU semester examinations, understanding memory management is essential not only because it carries significant weightage in exams but also because it forms the foundation for comprehending how operating systems abstract hardware complexities. The concepts learned here directly relate to system programming, software development, and troubleshooting performance issues in real-world applications.

## Key Concepts

### Memory Management Unit (MMU)

The Memory Management Unit is a hardware component that translates virtual addresses used by programs into physical addresses in RAM. When a CPU executes an instruction that references a memory location, the MMU intercepts this request and performs address translation using a page table or segment table. This translation happens transparently, allowing programs to use virtual addresses while the system manages physical memory allocation. The MMU also provides memory protection by ensuring processes can only access their allocated memory regions.

### Contiguous Memory Allocation

In contiguous memory allocation, each process is stored in a single continuous block of memory. This method was common in early operating systems and is conceptually simple. The operating system maintains a table of allocated and free memory blocks. When a process requests memory, the system searches for a contiguous block large enough to accommodate it. Three strategies are used for selection: FIRST FIT allocates the first block of sufficient size, BEST FIT searches for the smallest block that fits (minimizes wasted space), and WORST FIT chooses the largest available block (leaves larger remaining fragments).

However, contiguous allocation suffers from external fragmentation—where free memory is divided into small non-contiguous blocks that cannot satisfy large requests even when total free memory is sufficient. This leads to inefficient memory utilization over time.

### Swapping

Swapping is a technique where entire processes are moved between main memory and secondary storage (typically disk). When physical memory becomes full, the operating system may swap out least-recently-used processes to a swap area on the disk to free up RAM for currently active processes. When a swapped-out process needs to run again, it is swapped back into memory. While swapping enables systems to run more processes than physical memory would normally allow, it introduces significant overhead due to disk I/O operations. Modern systems use more sophisticated virtual memory techniques rather than full process swapping.

### Paging

Paging eliminates external fragmentation by dividing both physical and virtual memory into fixed-size blocks called pages (virtual memory) and frames (physical memory). The size of pages is typically a power of 2, ranging from 4KB to 2MB depending on system architecture. Each process has its own page table that maps virtual page numbers to physical frame numbers. When a process accesses a virtual address, the MMU uses the page table to translate it to a physical address.

The key advantage of paging is that it allows non-contiguous allocation of physical memory—a process's pages can be scattered across any available frames in physical memory. This completely eliminates external fragmentation. However, paging introduces internal fragmentation (wasted space within allocated units) and requires additional memory for page tables.

### Segmentation

Segmentation is a memory management technique that divides memory into variable-sized segments based on logical divisions of a program such as code, data, stack, and heap. Each segment has a name (or number) and a length, and programs reference memory locations using segment name and offset within that segment. This matches how programmers naturally think about memory—functions, arrays, objects each occupy distinct logical units.

Segmentation provides natural protection because different segments can have different access permissions (read-only code, read-write data). It also facilitates sharing—multiple processes can share code or data segments. The main challenge is that, like contiguous allocation, segmentation can suffer from external fragmentation as segments of varying sizes are allocated and deallocated.

### Virtual Memory

Virtual memory is an abstraction that gives each process the illusion of having exclusive access to a large, contiguous address space, regardless of actual physical memory configuration. It combines paging and segmentation (or paging alone) with demand loading—pages are loaded into physical memory only when referenced. If a process accesses a page not currently in memory, a page fault occurs, and the operating system loads the required page from secondary storage.

Virtual memory enables several critical capabilities: it allows programs larger than physical memory to execute, provides process isolation by ensuring each process has its own virtual address space, simplifies programming by eliminating need for memory management at application level, and enables efficient sharing of code segments between multiple processes.

### Page Replacement Algorithms

When physical memory is full and a page fault occurs, the operating system must evict an existing page to make room for the new page. Page replacement algorithms determine which page to remove. The optimal algorithm (BELADY'S ANOMALY) evicts the page that will not be referenced for the longest time in the future, achieving the fewest page faults but being unrealizable in practice.

FIFO (First-In-First-Out) evicts the oldest page in memory, simple to implement but often performs poorly. LRU (Least Recently Used) tracks page usage and evicts the least recently accessed page, providing good approximation to optimal but requiring hardware support for accurate implementation. CLOCK (Second Chance) uses a reference bit to approximate LRU without heavy overhead—the algorithm cycles through pages, giving pages with reference bit set a second chance while evicting those with bit clear. Other algorithms include Optimal Page Replacement, Not Recently Used (NRU), and Working Set models.

### Thrashing

Thrashing occurs when a system spends most of its time swapping pages in and out of memory rather than executing useful work. This typically happens when there are too many processes competing for limited physical memory, causing excessive page faults. As the degree of multiprogramming increases, CPU utilization drops dramatically because processes spend waiting for disk I/O rather than computing. The operating system may respond by increasing multiprogramming further, worsening the problem. Solutions include working set models, page fault frequency control, and adjusting the priority of processes exhibiting thrashing behavior.

## Examples

### Example 1: Working with Page Tables

Consider a system with 16-bit virtual addresses and 4KB pages. Calculate the number of entries in the page table and the memory overhead if each page table entry is 4 bytes.

SOLUTION: With 4KB (4096 bytes) pages and 16-bit addresses, we have 2^16 = 65536 bytes of virtual address space. Each page is 4096 bytes = 2^12 bytes, so the number of pages is 2^16 / 2^12 = 2^4 = 16 pages. The page table therefore has 16 entries. Memory overhead per process = 16 entries × 4 bytes = 64 bytes. For 100 processes, this is 6.4KB of overhead—a small price for eliminating external fragmentation.

### Example 2: Page Fault Calculation

A process references pages in this sequence: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5. Assuming 3 frames of physical memory, calculate page faults using FIFO and LRU algorithms.

SOLUTION:

FIFO:
- Frame 1: Reference 1 → Page fault (load page 1)
- Frame 2: Reference 2 → Page fault (load page 2)
- Frame 3: Reference 3 → Page fault (load page 3)
- Frame 4: Reference 4 → Page fault (evict 1, load 4)
- Reference 1 → Page fault (evict 2, load 1)
- Reference 2 → Page fault (evict 3, load 2)
- Reference 5 → Page fault (evict 4, load 5)
- Reference 1 → Hit (1 in memory)
- Reference 2 → Hit (2 in memory)
- Reference 3 → Page fault (evict 1, load 3)
- Reference 4 → Page fault (evict 2, load 4)
- Reference 5 → Page fault (evict 3, load 5)

Total page faults (FIFO): 10

LRU:
- Same sequence through reference 4 (first 4 faults)
- Reference 1 → Page fault (evict 4, load 1) — 4 was used 4th, least recent
- Reference 2 → Hit
- Reference 5 → Page fault (evict 3, load 5)
- Reference 1 → Hit
- Reference 2 → Hit
- Reference 3 → Page fault (evict 2, load 3)
- Reference 4 → Page fault (evict 1, load 4)
- Reference 5 → Hit

Total page faults (LRU): 8

### Example 3: Understanding Virtual Address Translation

Given a system with 32-bit virtual addresses, 4KB pages, and 2GB physical memory, determine the structure of a virtual address and calculate the number of entries in the page table.

SOLUTION: Page size = 4KB = 2^12 bytes, so offset bits = 12. Virtual address bits = 32, so VPN (Virtual Page Number) bits = 32 - 12 = 20 bits. Number of virtual pages = 2^20 = 1,048,576 pages. Physical memory = 2GB = 2^31 bytes. Number of frames = 2^31 / 2^12 = 2^19 = 524,288 frames. Each page table entry must store a 19-bit frame number plus status bits (typically rounded to 4 bytes). Page table size per process = 2^20 × 4 bytes = 4MB. This illustrates why multi-level page tables are essential for large address spaces.

## Exam Tips

1. UNDERSTAND THE DIFFERENCE BETWEEN INTERNAL AND EXTERNAL FRAGMENTATION—contiguous allocation suffers from external fragmentation while paging suffers from internal fragmentation. This is a frequently asked question in DU exams.

2. MEMORIZE THE PAGE REPLACEMENT ALGORITHMS AND THEIR CHARACTERISTICS—FIFO is simple but can exhibit Belady's anomaly (more frames can cause more page faults), while LRU approximates optimal but is harder to implement.

3. KNOW HOW TO CALCULATE PAGE FAULTS FOR DIFFERENT ALGORITHMS—practice numerical problems involving FIFO, LRU, and optimal replacement. This carries significant weightage in examination.

4. UNDERSTAND THE ROLE OF THE MMU IN ADDRESS TRANSLATION—be clear about how virtual addresses are translated to physical addresses using page tables.

5. BE PREPARED TO COMPARE DIFFERENT MEMORY MANAGEMENT TECHNIQUES—advantages and disadvantages of paging vs segmentation, contiguous vs non-contiguous allocation.

6. KNOW WHAT THRASHING IS AND HOW TO ADDRESS IT—understand the relationship between degree of multiprogramming, page fault rate, and CPU utilization.

7. REMEMBER THAT VIRTUAL MEMORY ENABLES PROCESSES TO USE MORE MEMORY THAN PHYSICALLY AVAILABLE—this is achieved through demand paging and page replacement.

8. UNDERSTAND THE CONCEPT OF LOCALITY OF REFERENCE—why programs tend to access a small subset of pages at any given time, making caching and page replacement feasible.

9. KNOW ABOUT MULTI-LEVEL PAGE TABLES—why they are needed for large address spaces and how they reduce memory overhead.

10. DIFFERENTIATE BETWEEN SWAPPING AND PAGING—swapping moves entire processes while paging moves individual pages. This distinction is important for conceptual questions.