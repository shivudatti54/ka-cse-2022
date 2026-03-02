# **Virtual Memory Management: Quick Revision Notes**

### Background

- **Demand Paging**: A page fault occurs when a page is accessed for the first time.
- **Page Table**: Maps virtual addresses to physical addresses.
- **Page Replacement Policies**: Optimal, FIFO, LRU, and Random Replacement Policies.

### Demand Paging (Chapter 10.1-10.3)

- **Page Fault**: Occurs when a page is not in memory.
- **Page Fault Resolution**: Read the page from disk, replace the page in memory.
- **Page Replacement Algorithms**:
  - **Optimal**: Replaces the page with the least recently used page.
  - **FIFO**: Replaces the page at the front of the queue.
  - **LRU**: Replaces the page with the least recently used page.
  - **Random**: Replaces a page at random.

### Copy-on-Write (Chapter 10.4)

- **Copy-on-Write**: Creates a copy of a page when it's first modified.
- **Benefits**: Reduces page faults, improves performance.
- **Disadvantages**: Increases memory usage, slower.

### Page Replacement (Chapter 13.3)

- **Page Replacement Formula**:
  - **OPTIMAL**: `OPTIMAL = max (p[i], p[j + 1], ..., p[n])`
  - **FIFO**: `FIFO = FQ[i]`
  - **LRU**: `LRU = LRU[i]`
  - **Random**: `Random = random(i, j, n)`

### Page Replacement Algorithms (Chapter 13.3)

- **Page Replacement Algorithms**:
  - **Optimal**: Replaces the page with the minimum cost.
  - **FIFO**: Replaces the page at the front of the queue.
  - **LRU**: Replaces the page with the least recently used page.
  - **Random**: Replaces a page at random.

### Page Replacement Policies (Chapter 13.4)

- **Page Replacement Policies**:
  - **Optimal**: Replaces the page with the minimum cost.
  - **FIFO**: Replaces the page at the front of the queue.
  - **LRU**: Replaces the page with the least recently used page.
  - **Random**: Replaces a page at random.

### Important Formulas and Definitions

- **Page Fault Rate**: Measures the number of page faults per page request.
- **Page Replacement Rate**: Measures the number of page replacements per page fault.

### Theorem

- **Bloom Filter**: A data structure used to determine if an element is a member of a set.
