# **Memory Management: Memory Management Strategies: Background**

## **Key Concepts:**

- **Demand Paging**: When a process needs to access a page that is not in memory, the operating system loads the page from disk into memory.
- **Page Replacement Algorithms**: Used to replace pages in memory when the system is out of space. Examples include:
  - First-In-First-Out (FIFO)
  - Least Recently Used (LRU)
  - Optimal (OPT)
- **Virtual Memory**: A combination of physical RAM and disk space used to simulate a large address space.
- **Paging**: The process of dividing a program into fixed-size blocks called pages, and storing them in RAM or on disk.

## **Definitions:**

- **Page Size**: The number of bytes allocated to each page.
- **Frame Size**: The size of RAM or disk space allocated for a page.
- **Page Table**: A data structure used to map virtual addresses to physical addresses.

## **Theorems:**

- **Thompson's Page Replacement Algorithm**: A page replacement algorithm that uses the least recently used page as the replacement algorithm.

## **Important Formulas:**

- **Page Replacement Formula**: `P = (current_page, new_page, page_table)`

- `P = current_page + \delta * new_page`

### Delta (δ) represents the probability of choosing a new page over the current one.

- **Page Fault Rate**: The rate at which pages are replaced in memory.

- `PF = P/(P + N)`

where N is the total number of pages in memory.

### Key Points:

- Memory management is a critical component of operating systems.
- Memory management strategies include demand paging and page replacement algorithms.
