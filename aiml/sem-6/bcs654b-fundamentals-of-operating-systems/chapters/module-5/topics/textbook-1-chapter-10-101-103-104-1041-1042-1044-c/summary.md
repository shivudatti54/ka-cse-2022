### Virtual Memory Management: Background

#### Chapter 10 (10.1-10.3, 10.4)

- **Definition:** Virtual Memory: The combination of physical RAM and secondary storage (hard disk) that provides a large address space to the operating system.
- **Page Table:** A data structure used to map virtual addresses to physical addresses in main memory.
- **Page Replacement Algorithm:** A scheme for replacing pages in main memory when the system runs low on physical memory.

#### Key Concepts

- **Page Fault:** An event that occurs when a page is accessed, but not present in main memory.
- **Paging:** A technique of dividing a program into fixed-size blocks called pages.
- **Segmentation:** A technique of dividing a program into fixed-size blocks called segments.

#### Chapter 13 (13.1, 13.2, 13.3)

- **Demand Paging:** A page replacement algorithm that replaces pages when a page fault occurs.
- **Copy-on-Write (COW):** A technique used to emulate multiple processes on a single process by making a copy of the page when a process writes to it.
- **Page Replacement Algorithms:**
  - **First-In-First-Out (FIFO):** Replaces the first page that was brought into memory.
  - **Least Recently Used (LRU):** Replaces the page that was least recently used.
  - **Optimal:** Replaces the page that will be least needed in the future.

#### Key Concepts

- **Page Table Entry:** An entry in the page table that maps a virtual address to a physical address.
- **Translation Lookaside Buffer (TLB):** A small cache that stores recently accessed page table entries.
- **Page Fault Handling:** A mechanism for handling page faults, including page replacement and page loading.

### Important Formulas and Definitions

- **Page Fault Rate:** The rate at which page faults occur.
- **Page Fault Cost:** The cost of handling a page fault, including page replacement and page loading.
- **VM Size:** The total amount of virtual memory available to the operating system.
