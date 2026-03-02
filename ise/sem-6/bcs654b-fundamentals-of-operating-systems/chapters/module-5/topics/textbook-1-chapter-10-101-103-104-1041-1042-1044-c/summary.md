# **Virtual Memory Management: Quick Revision Notes**

## **Chapter 10: Background**

- **Definition:** Virtual memory is a combination of physical memory and disk storage.
- **Key Concepts:**
  - Page replacement algorithms
  - Page fault handling
  - Memory management units (MMUs)
- **Important Formulas:**
  - Page replacement algorithm metrics (e.g. LRU, OPT, FIFO)
  - Page fault rate formula

## **Chapter 10: Demand Paging**

- **Definition:** Demand paging is a technique where pages are only loaded into physical memory when they are needed.
- **Key Concepts:**
  - Page fault handling
  - Page replacement algorithms
  - Page tables
- **Important Formulas:**
  - Page fault rate formula
  - Memory usage formulas (e.g. percentage of physical memory used)

## **Chapter 10: Copy-on-Write**

- **Definition:** Copy-on-write is a technique where a copy of a modified page is created before modifying it.
- **Key Concepts:**
  - Memory protection
  - Page tables
  - Copy-on-write algorithms
- **Important Formulas:**
  - Page fault rate formula
  - Memory usage formulas (e.g. percentage of physical memory used)

## **Chapter 13: Page Replacement Algorithms**

- **LRU (Least Recently Used) Algorithm:**
  - Page replacement metric: last access time
  - Page replacement strategy: replace least recently used page
- **OPT (Optimal Page Replacement) Algorithm:**
  - Page replacement metric: expected page fault rate
  - Page replacement strategy: replace page with minimum expected page fault rate
- **FIFO (First-In-First-Out) Algorithm:**
  - Page replacement metric: first access time
  - Page replacement strategy: replace first page in queue

## **Chapter 13: Page Fault Handling**

- **Page Fault Handling:** handling of page faults (e.g. page replacement, page faults)
- **Key Concepts:**
  - Page tables
  - Memory management units (MMUs)
  - Page fault rates
- **Important Formulas:**
  - Page fault rate formula
  - Memory usage formulas (e.g. percentage of physical memory used)
