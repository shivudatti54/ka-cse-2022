# **Textbook 1: Chapter 10: 10.1-10.3, 10.4 (10.4.1, 10.4.2, 10.4.4) Chapter 13: 13.1, 13.2, 13.3 (13.3.1, 13.3.2, 13.3.3), 13.4 (13.4.1, 13.4.2) Chapter**

## **Virtual Memory Management: Background; Demand Paging; Copy-on-write; Page Replacement**

### 10.1: Introduction to Virtual Memory

Virtual memory is a fundamental concept in operating system design that enables a computer to use more memory than is physically available in the system. It allows the operating system to manage a large amount of memory by dividing it into smaller, more manageable chunks called pages.

#### Historical Context

The concept of virtual memory was first introduced in the 1950s by IBM, and it was later popularized by the development of the Unix operating system in the 1970s. The idea of virtual memory was to provide a way for multiple users to share the same physical memory, while still allowing each user to have a dedicated virtual address space.

#### Modern Developments

Today, virtual memory is a ubiquitous feature in modern operating systems, and it plays a critical role in ensuring efficient use of system resources. The development of virtual memory has also enabled the creation of large-scale applications that can run on smaller systems, such as laptops and mobile devices.

### 10.2: Types of Virtual Memory

There are two main types of virtual memory:

1. **Page-based virtual memory**: This type of virtual memory divides the physical memory into fixed-size blocks called pages. Each page is assigned a unique virtual address, and the operating system maps multiple pages to a contiguous block of physical memory.
2. **Segment-based virtual memory**: This type of virtual memory divides the address space into smaller segments, each of which is assigned a unique set of permissions and access rights.

#### Advantages of Page-based Virtual Memory

Page-based virtual memory has several advantages, including:

- **Efficient use of physical memory**: By dividing the physical memory into fixed-size pages, page-based virtual memory enables efficient use of physical memory, even in systems with limited resources.
- **Improved performance**: Page-based virtual memory can improve performance by reducing the number of page faults, which occur when the operating system needs to access a page that is not in physical memory.

#### Disadvantages of Page-based Virtual Memory

Page-based virtual memory also has several disadvantages, including:

- **Complexity**: Page-based virtual memory can be complex to implement, especially in systems with large address spaces.
- **Page faults**: Page faults can occur when the operating system needs to access a page that is not in physical memory, which can lead to performance degradation.

### 10.3: Demand Paging

Demand paging is a technique used in page-based virtual memory to reduce the number of page faults. The technique works as follows:

1. **Page table**: The operating system maintains a page table, which maps virtual addresses to physical page numbers.
2. **Page fault**: When the operating system needs to access a page that is not in physical memory, it generates a page fault.
3. **Page loading**: The operating system loads the requested page into physical memory.
4. **Update page table**: The operating system updates the page table to reflect the new physical page number.

#### Advantages of Demand Paging

Demand paging has several advantages, including:

- **Reduced page faults**: Demand paging reduces the number of page faults, which can improve system performance.
- **Improved memory utilization**: Demand paging can improve memory utilization by allowing the operating system to load pages into physical memory only when needed.

#### Disadvantages of Demand Paging

Demand paging also has several disadvantages, including:

- **Increased complexity**: Demand paging can increase complexity, especially in systems with large address spaces.
- **Increased memory requirements**: Demand paging can increase memory requirements, especially in systems with limited physical memory.

### 10.4: Copy-on-Write

Copy-on-write is a technique used in page-based virtual memory to reduce the number of page faults and improve memory utilization. The technique works as follows:

1. **Original page**: The operating system maintains a copy of the original page in physical memory.
2. **Write operation**: When a write operation is performed on a page, the operating system creates a copy of the page in a new physical location.
3. **Update original page**: The operating system updates the original page with the new copy.
4. **Delete original page**: The operating system deletes the original page from physical memory.

#### Advantages of Copy-on-Write

Copy-on-write has several advantages, including:

- **Reduced page faults**: Copy-on-write reduces the number of page faults, which can improve system performance.
- **Improved memory utilization**: Copy-on-write can improve memory utilization by allowing the operating system to reuse memory.

#### Disadvantages of Copy-on-Write

Copy-on-write also has several disadvantages, including:

- **Increased complexity**: Copy-on-write can increase complexity, especially in systems with large address spaces.
- **Increased memory requirements**: Copy-on-write can increase memory requirements, especially in systems with limited physical memory.

### 13.1: Page Replacement Algorithms

Page replacement algorithms are used in virtual memory management to select the pages to be replaced when the system is running low on physical memory. The following are some common page replacement algorithms:

#### First-Fit

The first-fit algorithm works as follows:

1. **Scan physical memory**: The operating system scans physical memory to find a free block of memory that is large enough to accommodate the page.
2. **Replace page**: The operating system replaces the selected page with the new page.

#### Best-Fit

The best-fit algorithm works as follows:

1. **Scan physical memory**: The operating system scans physical memory to find the free block of memory that is the largest.
2. **Replace page**: The operating system replaces the selected page with the new page.

#### Optimal-Fit

The optimal-fit algorithm works as follows:

1. **Scan physical memory**: The operating system scans physical memory to find the free block of memory that is the smallest.
2. **Replace page**: The operating system replaces the selected page with the new page.

#### Time-Ordered Least Recently Used (TLRU)

The TLRU algorithm works as follows:

1. **Keep track of page usage**: The operating system keeps track of the usage of each page.
2. **Scan physical memory**: The operating system scans physical memory to find the page that has been used the least recently.
3. **Replace page**: The operating system replaces the selected page with the new page.

#### Least Recently Used (LRU)

The LRU algorithm works as follows:

1. **Keep track of page usage**: The operating system keeps track of the usage of each page.
2. **Scan physical memory**: The operating system scans physical memory to find the page that has been used the least.
3. **Replace page**: The operating system replaces the selected page with the new page.

### 13.2: Page Replacement Metrics

Page replacement metrics are used to evaluate the performance of page replacement algorithms. The following are some common page replacement metrics:

#### Page Fault Rate

The page fault rate is the number of page faults per unit of time.

#### Average Page Fault Time

The average page fault time is the average time it takes to access a page.

#### Average Page Fault Count

The average page fault count is the average number of page faults per unit of time.

#### Page Replacement Rate

The page replacement rate is the number of pages replaced per unit of time.

### 13.3: Page Replacement Strategies

Page replacement strategies are used to select the pages to be replaced based on certain criteria. The following are some common page replacement strategies:

#### Serial Replacement

Serial replacement is a strategy that replaces pages in the order they are accessed.

#### Random Replacement

Random replacement is a strategy that replaces pages randomly.

#### Optimal Replacement

Optimal replacement is a strategy that replaces pages based on the minimum number of page faults.

#### Greedy Replacement

Greedy replacement is a strategy that replaces pages based on the most recently used page.

### 13.4: Page Replacement Algorithms with Multiple Metrics

Page replacement algorithms with multiple metrics are used to select the pages to be replaced based on multiple criteria. The following are some common page replacement algorithms with multiple metrics:

#### Page Replacement Algorithm with Page Fault Rate and Average Page Fault Time

This algorithm works as follows:

1. **Scan physical memory**: The operating system scans physical memory to find the page that has the highest page fault rate and average page fault time.
2. **Replace page**: The operating system replaces the selected page with the new page.

#### Page Replacement Algorithm with Page Fault Rate and Average Page Fault Count

This algorithm works as follows:

1. **Scan physical memory**: The operating system scans physical memory to find the page that has the highest page fault rate and average page fault count.
2. **Replace page**: The operating system replaces the selected page with the new page.

#### Page Replacement Algorithm with Page Fault Rate and Page Replacement Rate

This algorithm works as follows:

1. **Scan physical memory**: The operating system scans physical memory to find the page that has the highest page fault rate and page replacement rate.
2. **Replace page**: The operating system replaces the selected page with the new page.

#### Page Replacement Algorithm with Multiple Metrics

This algorithm works as follows:

1. **Scan physical memory**: The operating system scans physical memory to find the page that has the highest score based on multiple metrics.
2. **Replace page**: The operating system replaces the selected page with the new page.

#### Further Reading

- "Operating System Concepts" by Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne
- "Virtual Memory Management" by Thomas E. Anderson
- "Page Replacement Algorithms" by Kenneth C. Brown

This concludes the chapter on virtual memory management, demand paging, copy-on-write, and page replacement algorithms. We have covered the background, types of virtual memory, demand paging, copy-on-write, page replacement algorithms, page replacement metrics, page replacement strategies, and page replacement algorithms with multiple metrics. We have also discussed the historical context, modern developments, advantages, disadvantages, and further reading for each topic.
