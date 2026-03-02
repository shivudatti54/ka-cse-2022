# Fundamentals of Operating Systems

## Virtual Memory Management: Background; Demand Paging; Copy-on-write; Page Replacement

### Chapter 10: Background and Fundamentals

### 10.1 Introduction to Virtual Memory

Virtual memory is a critical component of operating systems, allowing multiple applications to run concurrently on a single physical machine. It enables the operating system to manage the allocation and deallocation of memory for each application, even if the physical memory is insufficient.

**Historical Context**

The concept of virtual memory was first introduced in the 1950s by Maurice Wilkes, a British computer scientist. Initially, it was used in the EDSAC (Electronic Delay Storage Automatic Calculator) computer to provide a single address space for multiple programs. In the 1960s, virtual memory became a standard feature in operating systems, including Unix and Multics.

**Key Concepts**

- **Page**: A fixed-size block of memory, typically 4KB or 8KB.
- **Frame**: A contiguous block of physical memory.
- **Page Table**: A data structure that maps virtual pages to physical frames.
- **Page Fault**: An event that occurs when a program attempts to access a page that is not in physical memory.

### 10.2 Demand Paging

Demand paging is a technique used by operating systems to manage virtual memory. It works by only loading pages into physical memory when they are actually needed (i.e., when a page fault occurs).

**How Demand Paging Works**

1. The operating system maps a program's virtual pages to physical frames using a page table.
2. When a program accesses a virtual page, the operating system checks if the page is in physical memory.
3. If the page is not in memory, a page fault occurs.
4. The operating system loads the page from disk into physical memory.

**Advantages and Disadvantages**

Advantages:

- **Reduced Memory Usage**: Demand paging reduces the amount of physical memory required by an operating system.
- **Improved Performance**: Demand paging improves performance by reducing the number of page faults.

Disadvantages:

- **Increased Disk I/O**: Demand paging increases disk I/O because pages are loaded from disk when they are accessed.
- **Increased Cache Misses**: Demand paging increases cache misses because pages are not in memory.

### 10.3 Page Replacement Algorithms

Page replacement algorithms are used to manage page faults in virtual memory. They determine which page to replace when the physical memory is full.

**Common Page Replacement Algorithms**

- **First-In-First-Out (FIFO)**: The algorithm replaces the page that has been in memory the longest.
- **Least Recently Used (LRU)**: The algorithm replaces the page that has not been accessed recently.
- **Optimal**: The algorithm selects the page that will not be accessed in the near future.

### 10.4 Copy-on-Write

Copy-on-write is a technique used to manage the sharing of data in virtual memory. It works by creating a copy of a page when it is first written.

**How Copy-on-Write Works**

1. The operating system creates a copy of a page when it is first written.
2. The copy is stored in physical memory.
3. When the original page is modified, the operating system creates a new copy of the modified page.
4. The new copy is stored in physical memory, while the original page remains unchanged.

**Advantages and Disadvantages**

Advantages:

- **Improved Sharing**: Copy-on-write improves sharing by allowing multiple processes to share the same page.
- **Reduced Memory Usage**: Copy-on-write reduces memory usage by only storing one copy of each page.

Disadvantages:

- **Increased Complexity**: Copy-on-write increases complexity by requiring additional memory and processing power.

### Chapter 13: Page Replacement and Memory Management

### 13.1 Page Replacement Algorithms

Page replacement algorithms are used to manage page faults in virtual memory. They determine which page to replace when the physical memory is full.

**Common Page Replacement Algorithms**

- **First-In-First-Out (FIFO)**: The algorithm replaces the page that has been in memory the longest.
- **Least Recently Used (LRU)**: The algorithm replaces the page that has not been accessed recently.
- **Optimal**: The algorithm selects the page that will not be accessed in the near future.

### 13.2 Page Replacement Strategies

Page replacement strategies are used to determine which algorithm to use in a system.

**Common Page Replacement Strategies**

- **Greedy Algorithm**: The algorithm chooses the best algorithm based on the current memory usage.
- **Adaptive Algorithm**: The algorithm adapts to changing memory usage and chooses the best algorithm accordingly.

### 13.3 Page Replacement Policies

Page replacement policies are used to determine which pages to replace when the physical memory is full.

**Common Page Replacement Policies**

- **MPL (Most Recently Used)**: The algorithm replaces the page that has been accessed most recently.
- **MRU (Minimum Reference)**: The algorithm replaces the page that has been referenced the least.

### 13.4 Page Replacement Analysis

Page replacement analysis is used to evaluate the performance of page replacement algorithms.

**Key Performance Metrics**

- **Page Fault Rate**: The rate at which page faults occur.
- **Memory Usage**: The amount of physical memory used by the system.
- **Cache Hit Rate**: The percentage of cache hits.

### Case Studies

- **Journaling File Systems**: Journaling file systems use a variant of copy-on-write to manage file system metadata.
- **Virtual Machines**: Virtual machines use demand paging to manage virtual memory.

### Applications

- **Cloud Computing**: Demand paging is used in cloud computing to manage virtual memory.
- **Virtual Desktops**: Demand paging is used in virtual desktops to manage virtual memory.

### Further Reading

- **"Operating System Concepts" by Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne**: This textbook provides a comprehensive overview of operating systems, including virtual memory management.
- **"Virtual Memory" by Donald B. Johnson and Larry L. Peterson**: This paper provides a detailed analysis of virtual memory management, including demand paging and page replacement algorithms.
- **"Page Replacement Algorithms" by S. S. Iyer and S. S. Iyer**: This paper provides a comprehensive overview of page replacement algorithms, including FIFO, LRU, and optimal algorithms.

### Diagrams

- **Page Table Diagram**: A diagram showing the page table and its mapping of virtual pages to physical frames.
- **Demand Paging Diagram**: A diagram showing the demand paging process, including the page fault and page loading.
- **Page Replacement Algorithm Diagram**: A diagram showing the page replacement algorithm, including the FIFO, LRU, and optimal algorithms.
