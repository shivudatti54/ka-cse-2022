# **Virtual Memory Management: Background**

### 10.1 Introduction to Virtual Memory

Virtual memory is a memory management technique that allows a computer to use more memory than is physically available in the system's RAM. It does this by temporarily transferring pages of memory to a storage device, such as a hard drive, when the RAM is full.

### 10.2 Demand Paging

Demand paging is a technique used in virtual memory management to minimize the number of pages that need to be transferred to disk. It works by:

- Loading pages into RAM as needed (i.e., when a program requests them)
- Replacing pages in RAM with new pages when the RAM is full
- Transferring pages from disk to RAM only when they are needed

**Key Concepts:**

- **Demand Paging**: A technique used in virtual memory management to minimize the number of pages that need to be transferred to disk
- **Page Replacement**: The process of replacing pages in RAM with new pages when the RAM is full
- **Page Fault**: An event that occurs when a program requests a page that is not in RAM

### 10.3 Page Replacement Algorithms

Page replacement algorithms are used to decide which pages to replace in RAM when the RAM is full. There are several algorithms, including:

- **First-In-First-Out (FIFO)**: Replace the first page that was brought into RAM
- **Least Recently Used (LRU)**: Replace the page that has not been used in the longest time
- **Optimal**: Replace the page that will not be needed for the longest time

**Key Concepts:**

- **Page Replacement Algorithm**: An algorithm used to decide which pages to replace in RAM when the RAM is full
- **FIFO**: A page replacement algorithm that replaces the first page that was brought into RAM
- **LRU**: A page replacement algorithm that replaces the page that has not been used in the longest time

### 10.4 Copy-on-Write

Copy-on-write is a technique used to minimize the number of pages that need to be transferred to disk. It works by:

- Creating a copy of a page in RAM when it is modified
- Transferring the modified page to disk only when the original page is no longer needed

**Key Concepts:**

- **Copy-on-Write**: A technique used to minimize the number of pages that need to be transferred to disk
- **Page Copy**: The process of creating a copy of a page in RAM when it is modified
- **Modified Page**: A page that has been modified since it was last transferred to disk

**Chapter 13: Page Replacement Algorithms**

### 13.1 Page Replacement Algorithms

Page replacement algorithms are used to decide which pages to replace in RAM when the RAM is full. There are several algorithms, including:

- **First-In-First-Out (FIFO)**: Replace the first page that was brought into RAM
- **Least Recently Used (LRU)**: Replace the page that has not been used in the longest time
- **Optimal**: Replace the page that will not be needed for the longest time

### 13.2 Page Replacement Strategies

Page replacement strategies are used to decide which pages to replace in RAM when the RAM is full. There are several strategies, including:

- **Short-Term Strategy**: Replace the page that will not be needed for the shortest time
- **Long-Term Strategy**: Replace the page that will not be needed for the longest time

### 13.3 Page Replacement Policies

Page replacement policies are used to decide which pages to replace in RAM when the RAM is full. There are several policies, including:

- **Policy-Based Replacement**: Replace the page based on a set of rules
- **Threshold-Based Replacement**: Replace the page when a certain threshold is reached

**Key Concepts:**

- **Page Replacement Algorithm**: An algorithm used to decide which pages to replace in RAM when the RAM is full
- **FIFO**: A page replacement algorithm that replaces the first page that was brought into RAM
- **LRU**: A page replacement algorithm that replaces the page that has not been used in the longest time

### 13.4 Page Replacement Evaluation

Page replacement evaluation is used to evaluate the effectiveness of a page replacement algorithm. There are several metrics, including:

- **Page Fault Rate**: The number of page faults per unit time
- **Average Page Fault Time**: The average time it takes to retrieve a page from disk
- **Average Page Replacement Time**: The average time it takes to replace a page in RAM

**Key Concepts:**

- **Page Replacement Evaluation**: The process of evaluating the effectiveness of a page replacement algorithm
- **Page Fault Rate**: The number of page faults per unit time
- **Average Page Fault Time**: The average time it takes to retrieve a page from disk
