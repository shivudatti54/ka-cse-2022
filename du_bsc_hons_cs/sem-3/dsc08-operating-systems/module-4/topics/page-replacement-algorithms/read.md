# Page Replacement Algorithms

## Comprehensive Study Material for Operating Systems (BSc Hons Computer Science - Delhi University, NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Background: Memory Management and Paging](#2-background-memory-management-and-paging)
3. [Page Replacement Algorithms](#3-page-replacement-algorithms)
   - [FIFO (First In First Out)](#31-fifo-first-in-first-out)
   - [LRU (Least Recently Used)](#32-lru-least-recently-used)
   - [Optimal Page Replacement](#33-optimal-page-replacement)
   - [LFU (Least Frequently Used)](#34-lfu-least-frequently-used)
4. [Comparative Analysis](#4-comparative-analysis)
5. [Concrete Examples with Code](#5-concrete-examples-with-code)
6. [Key Takeaways](#6-key-takeaways)
7. [Assessment Questions](#7-assessment-questions)
   - [Multiple Choice Questions (MCQs)](#71-multiple-choice-questions-mcqs)
   - [Flashcards](#72-flashcards)
8. [Delhi University Syllabus Reference](#8-delhi-university-syllabus-reference)

---

## 1. Introduction and Real-World Relevance

**Page Replacement Algorithms** are fundamental to modern computer systems, playing a critical role in **virtual memory management**. In an era where applications demand more memory than physically available, these algorithms determine which pages should remain in physical memory and which should be evicted when new pages must be loaded.

### Why This Topic Matters

- **Enables Multitasking**: Allows systems to run more processes than physical memory would otherwise permit
- **Performance Optimization**: Directly impacts system throughput, page fault rates, and response times
- **Real-World Applications**: Used in operating systems (Windows, Linux, macOS), database systems, web browsers, and mobile OS

### Real-World Scenario

Consider a web browser opening multiple tabs. Each tab represents a set of memory pages. When you open a new tab and memory is full, the browser (through the OS's page replacement) must decide which pages to keep in RAM. A good page replacement strategy keeps frequently accessed pages (like the current webpage) while evicting rarely-used ones.

---

## 2. Background: Memory Management and Paging

### Virtual Memory Concept

Virtual memory creates an illusion that each process has access to a large, contiguous address space. This is achieved through:

- **Paging**: Dividing both physical and logical memory into fixed-size blocks (typically 4KB)
- **Page Tables**: Mapping virtual pages to physical frames
- **Demand Paging**: Loading pages only when needed

### The Page Fault Problem

When a process accesses a page not currently in memory, a **page fault** occurs. The OS must:

1. Locate the page on disk (swap space)
2. Find a free physical frame
3. Load the page into memory
4. Update the page table
5. Resume the process

**When no free frames exist**, the OS must select a victim page to evict—the core function of page replacement algorithms.

### Belady's Anomaly

An interesting phenomenon where increasing the number of page frames can *increase* the number of page faults. This anomaly can occur with FIFO but NOT with stack algorithms like LRU.

---

## 3. Page Replacement Algorithms

### 3.1 FIFO (First In First Out)

#### Concept

The simplest page replacement algorithm evicts the page that has been in memory the longest. It maintains a queue of pages in memory order of arrival.

#### Algorithm Description

```
1. Maintain a queue of pages in memory (ordered by arrival time)
2. When a page fault occurs:
   a. If the page is already in memory → no action needed
   b. If there is a free frame → load page into frame
   c. If all frames are occupied → evict the oldest page (front of queue)
3. Add the newly loaded page to the back of the queue
```

#### Advantages
- Simple to implement (just a queue)
- Low overhead
- Good for systems with predictable access patterns

#### Disadvantages
- Suffers from Belady's Anomaly
- Doesn't consider page usage frequency
- May evict heavily used pages if they were loaded early

#### Example

**Reference String**: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
**Frames**: 3

| Access | Page Fault? | Frame 1 | Frame 2 | Frame 3 | Evicted |
|--------|--------------|---------|---------|---------|---------|
| 1      | ✓            | 1       | -       | -       | -       |
| 2      | ✓            | 1       | 2       | -       | -       |
| 3      | ✓            | 1       | 2       | 3       | -       |
| 4      | ✓            | 4       | 2       | 3       | 1       |
| 1      | ✓            | 4       | 1       | 3       | 2       |
| 2      | ✓            | 4       | 1       | 2       | 3       |
| 5      | ✓            | 5       | 1       | 2       | 4       |
| 1      | ✗            | 5       | 1       | 2       | -       |
| 2      | ✗            | 5       | 1       | 2       | -       |
| 3      | ✓            | 3       | 1       | 2       | 5       |
| 4      | ✓            | 3       | 4       | 2       | 1       |
| 5      | ✓            | 3       | 4       | 5       | 2       |

**Total Page Faults: 9**

---

### 3.2 LRU (Least Recently Used)

#### Concept

LRU evicts the page that has not been used for the longest time. This algorithm exploits the **temporal locality** principle—recently used pages are likely to be used again soon.

#### Algorithm Description

```
1. Maintain a history of page accesses (timestamp or stack)
2. When a page fault occurs:
   a. If the page is already in memory → update access time
   b. If there is a free frame → load page
   c. If all frames are occupied → evict page with oldest timestamp
3. Update timestamps for all pages on each access
```

#### Implementation Methods

- **Counter**: Each page has a counter incremented on every memory access
- **Stack**: Pages kept in a stack; most recently used always on top
- **Matrix**: n×n matrix for n frames; row i set to 1 when frame i accessed

#### Advantages
- Excellent performance in practice
- No Belady's Anomaly (stack algorithm)
- Reflects temporal locality well

#### Disadvantages
- Higher overhead than FIFO
- Requires hardware support for accurate timestamps
- Cannot be implemented perfectly in some systems

#### Example

**Reference String**: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
**Frames**: 3

| Access | Page Fault? | Frame 1 | Frame 2 | Frame 3 | Evicted |
|--------|--------------|---------|---------|---------|---------|
| 1      | ✓            | 1       | -       | -       | -       |
| 2      | ✓            | 1       | 2       | -       | -       |
| 3      | ✓            | 1       | 2       | 3       | -       |
| 4      | ✓            | 4       | 2       | 3       | 1       |
| 1      | ✓            | 4       | 1       | 3       | 2       |
| 2      | ✓            | 4       | 1       | 2       | 3       |
| 5      | ✓            | 5       | 1       | 2       | 4       |
| 1      | ✗            | 5       | 1       | 2       | -       |
| 2      | ✗            | 5       | 1       | 2       | -       |
| 3      | ✓            | 3       | 1       | 2       | 5       |
| 4      | ✓            | 3       | 4       | 2       | 1       |
| 5      | ✓            | 3       | 4       | 5       | 2       |

**Total Page Faults: 10**

---

### 3.3 Optimal Page Replacement

#### Concept

The optimal algorithm (OPT or MIN) evicts the page that will not be used for the longest time in the future. This is theoretically optimal but impossible to implement in practice.

#### Algorithm Description

```
1. Know the entire future reference string (oracle knowledge)
2. When a page fault occurs:
   a. If the page is already in memory → no action
   b. If there is a free frame → load page
   c. If all frames are occupied → for each page in memory:
      - Find its next use in the reference string
      - Evict the page with farthest (or no) future use
```

#### Why It's "Optimal"

- Produces the minimum possible page faults for any given reference string
- Serves as a **benchmark** to compare other algorithms
- Proves that better algorithms exist but cannot be achieved without future knowledge

#### Advantages
- Lowest page faults (theoretical minimum)
- No Belady's Anomaly
- Useful for algorithm analysis and comparison

#### Disadvantages
- Impossible to implement in real systems
- Requires future knowledge of memory accesses
- Only useful in simulations and algorithm research

#### Example

**Reference String**: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
**Frames**: 3

| Access | Page Fault? | Frame 1 | Frame 2 | Frame 3 | Evicted | Reasoning |
|--------|--------------|---------|---------|---------|---------|-----------|
| 1      | ✓            | 1       | -       | -       | -       |           |
| 2      | ✓            | 1       | 2       | -       | -       |           |
| 3      | ✓            | 1       | 2       | 3       | -       |           |
| 4      | ✓            | 4       | 2       | 3       | 1       | 1 used at 5,2 at 6,3 at 10 → evict 1 |
| 1      | ✓            | 4       | 1       | 3       | 2       | 4 at 11,3 at 10,2 at 6 → evict 2 |
| 2      | ✓            | 4       | 1       | 2       | 3       | 4 at 11,1 at 8,2 at 9 → evict 3 |
| 5      | ✓            | 5       | 1       | 2       | 4       | 5 at 12,1 at 8,2 at 9 → evict 4 |
| 1      | ✗            | 5       | 1       | 2       | -       |           |
| 2      | ✗            | 5       | 1       | 2       | -       |           |
| 3      | ✓            | 3       | 1       | 2       | 5       | 3 next,1 at 11,2 at 12 → evict 5 |
| 4      | ✓            | 3       | 4       | 2       | 1       | 4 next,3 later,2 later → evict 1 |
| 5      | ✓            | 3       | 4       | 5       | 2       | 5 next,3 later,4 later → evict 2 |

**Total Page Faults: 9**

---

### 3.4 LFU (Least Frequently Used)

#### Concept

LFU evicts the page that has been used the least number of times. It assumes pages with lower access counts are less important.

#### Algorithm Description

```
1. Maintain a counter for each page (frequency of use)
2. When a page fault occurs:
   a. If the page is already in memory → increment its counter
   b. If there is a free frame → load page with counter = 1
   c. If all frames are occupied → evict page with lowest counter
      (tie-breaking: FIFO or LRU)
```

#### Implementation Considerations

- **Counters**: Need to be adjusted periodically (aging) to reflect current usage
- **Tie-breaking**: When multiple pages have equal frequency, use FIFO or LRU
- **Aging**: Gradually reduce counters to give recently-used pages a chance

#### Advantages
- Keeps frequently-used pages in memory
- Good for systems with clear usage patterns
- More accurate than FIFO for some workloads

#### Disadvantages
- Higher overhead than FIFO
- May keep old, frequently-used pages even when no longer needed
- Requires counter maintenance

#### Example

**Reference String**: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
**Frames**: 3

| Access | Page Fault? | Frame 1 | Frame 2 | Frame 3 | Counters | Evicted |
|--------|--------------|---------|---------|---------|----------|---------|
| 1      | ✓            | 1       | -       | -       | 1:1      | -       |
| 2      | ✓            | 1       | 2       | -       | 1:1,2:1  | -       |
| 3      | ✓            | 1       | 2       | 3       | 1:1,2:1,3:1 | -   |
| 4      | ✓            | 4       | 2       | 3       | 4:1,2:1,3:1 | 1    |
| 1      | ✓            | 4       | 1       | 3       | 4:1,1:1,3:1 | 2    |
| 2      | ✓            | 4       | 1       | 2       | 4:1,1:1,2:1 | 3    |
| 5      | ✓            | 5       | 1       | 2       | 5:1,1:1,2:1 | 4    |
| 1      | ✗            | 5       | 1       | 2       | 5:1,1:2,2:1 | -    |
| 2      | ✗            | 5       | 1       | 2       | 5:1,1:2,2:2 | -    |
| 3      | ✓            | 3       | 1       | 2       | 3:1,1:2,2:2 | 5    |
| 4      | ✓            | 3       | 4       | 2       | 3:1,4:1,2:2 | 1    |
| 5      | ✓            | 3       | 4       | 5       | 3:1,4:1,5:1 | 2    |

**Total Page Faults: 10**

---

## 4. Comparative Analysis

| Algorithm | Page Faults | Belady's Anomaly | Implementation Complexity | Hardware Support |
|-----------|-------------|------------------|---------------------------|------------------|
| FIFO      | High        | Yes              | Very Low                  | Not Required     |
| LRU       | Low         | No               | High                      | Required         |
| Optimal   | Minimum     | No               | Impossible                | Oracle Required  |
| LFU       | Low-Medium  | No               | Medium                    | Required         |

### When to Use Each Algorithm

- **FIFO**: Embedded systems, simple implementations, educational purposes
- **LRU**: General-purpose operating systems, databases, caching systems
- **Optimal**: Research, algorithm benchmarking, theoretical analysis
- **LFU**: Web caching, CDN systems, file systems with known access patterns

---

## 5. Concrete Examples with Code

### Example 1: FIFO Implementation in Python

```python
class FIFOPageReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []  # Queue to store pages
        self.page_faults = 0
    
    def access_page(self, page):
        """Access a page and return whether a page fault occurred"""
        if page not in self.frames:
            self.page_faults += 1
            
            if len(self.frames) < self.num_frames:
                # Free frame available
                self.frames.append(page)
            else:
                # Evict oldest page (first in queue)
                self.frames.pop(0)
                self.frames.append(page)
            
            return True  # Page fault occurred
        
        return False  # No page fault
    
    def run_simulation(self, reference_string):
        """Simulate the entire reference string"""
        print(f"Simulation with {self.num_frames} frames")
        print(f"Reference String: {reference_string}")
        print("-" * 50)
        
        for i, page in enumerate(reference_string):
            fault = self.access_page(page)
            status = "FAULT" if fault else "HIT"
            print(f"Step {i+1}: Access Page {page} → {status}")
            print(f"  Frames: {self.frames}")
        
        print("-" * 50)
        print(f"Total Page Faults: {self.page_faults}")
        return self.page_faults


# Example usage
if __name__ == "__main__":
    fifo = FIFOPageReplacement(num_frames=3)
    reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    fifo.run_simulation(reference_string)
```

### Example 2: LRU Implementation in Python

```python
from collections import OrderedDict

class LRUPageReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = OrderedDict()  # Maintains insertion order
        self.page_faults = 0
    
    def access_page(self, page):
        """Access a page with LRU replacement"""
        if page in self.frames:
            # Move to end (most recently used)
            self.frames.move_to_end(page)
            return False  # No page fault
        
        # Page fault occurred
        self.page_faults += 1
        
        if len(self.frames) < self.num_frames:
            # Free frame available
            self.frames[page] = True
        else:
            # Evict least recently used (first item)
            self.frames.popitem(last=False)
            self.frames[page] = True
        
        return True
    
    def run_simulation(self, reference_string):
        """Simulate the entire reference string"""
        print(f"LRU Simulation with {self.num_frames} frames")
        print(f"Reference String: {reference_string}")
        print("-" * 50)
        
        for i, page in enumerate(reference_string):
            fault = self.access_page(page)
            status = "FAULT" if fault else "HIT"
            frame_list = list(self.frames.keys())
            print(f"Step {i+1}: Access {page} → {status} | Frames: {frame_list}")
        
        print("-" * 50)
        print(f"Total Page Faults: {self.page_faults}")
        return self.page_faults


# Example usage
if __name__ == "__main__":
    lru = LRUPageReplacement(num_frames=3)
    reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    lru.run_simulation(reference_string)
```

---

## 6. Key Takeaways

1. **Page Replacement** is essential when physical memory is full and a new page needs to be loaded
2. **FIFO** is simple but suffers from Belady's Anomaly; may evict frequently-used pages
3. **LRU** is practical and performs well by leveraging temporal locality; no Belady's Anomaly
4. **Optimal (OPT)** provides the theoretical minimum page faults but cannot be implemented
5. **LFU** tracks page usage frequency but requires counter management
6. Real OS implementations often use approximations (clock algorithm, aging) due to hardware limitations
7. The choice of algorithm significantly impacts system performance in memory-intensive applications

---

## 7. Assessment Questions

### 7.1 Multiple Choice Questions (MCQs)

**Question 1:** In which page replacement algorithm does increasing the number of page frames sometimes *increase* the number of page faults?
- a) LRU
- b) Optimal
- c) FIFO
- d) LFU

**Answer:** c) FIFO

---

**Question 2:** Which algorithm evicts the page that will not be used for the longest time in the future?
- a) LRU
- b) FIFO
- c) Optimal
- d) LFU

**Answer:** c) Optimal

---

**Question 3:** LRU (Least Recently Used) is based on which principle?
- a) Spatial Locality
- b) Temporal Locality
- c) Sequential Locality
- d) Random Locality

**Answer:** b) Temporal Locality

---

**Question 4:** Which of the following is NOT a real-world implementation of page replacement?
- a) Clock Algorithm
- b) Working Set Model
- c) Optimal Algorithm
- d) Aging

**Answer:** c) Optimal Algorithm

---

**Question 5:** What is a page fault?
- a) When the CPU generates an error
- b) When a requested page is not in physical memory
- c) When the page table is full
- d) When virtual memory is disabled

**Answer:** b) When a requested page is not in physical memory

---

**Question 6:** Which algorithm requires hardware support for accurate implementation?
- a) FIFO
- b) LRU
- c) Optimal
- d) None

**Answer:** b) LRU

---

**Question 7:** In the FIFO algorithm, which page is evicted when a page fault occurs and all frames are occupied?
- a) Most recently used
- b) Least frequently used
- c) Longest in memory
- d) Shortest in memory

**Answer:** c) Longest in memory

---

**Question 8:** Belady's Anomaly is also known as:
- a) Stack Algorithm
- b) FIFO Anomaly
- c) Paging Anomaly
- d) Inconsistency Anomaly

**Answer:** c) Paging Anomaly

---

**Question 9:** Which algorithm serves primarily as a theoretical benchmark?
- a) LRU
- b) FIFO
- c) Optimal
- d) LFU

**Answer:** c) Optimal

---

**Question 10:** The LFU algorithm maintains which of the following for each page?
- a) Timestamp
- b) Counter
- c) Priority
- d) Stack position

**Answer:** b) Counter

---

### 7.2 Flashcards

| # | Term | Definition |
|---|------|------------|
| 1 | **Page Fault** | An interrupt that occurs when a program accesses a page not in physical memory |
| 2 | **Virtual Memory** | A memory management technique that creates an illusion of larger memory using disk storage |
| 3 | **Belady's Anomaly** | The phenomenon where increasing frames can increase page faults (occurs in FIFO) |
| 4 | **Temporal Locality** | The tendency of a processor to access the same memory locations repeatedly |
| 5 | **Frame** | A fixed-size block of physical memory |
| 6 | **Page** | A fixed-size block of logical/virtual memory |
| 7 | **Thrashing** | Excessive page faults causing degraded system performance |
| 8 | **Working Set** | The set of pages actively used by a process |
| 9 | **Clock Algorithm** | A FIFO approximation using a circular buffer and reference bit |
| 10 | **Demand Paging** | Loading pages into memory only when they are needed |

---

## 8. Delhi University Syllabus Reference

### Topics as per Delhi University BSc (Hons) Computer Science Syllabus (NEP 2024 UGCF):

- **Unit III: Memory Management**
  - Paging and Segmentation
  - Page Replacement Algorithms (FIFO, LRU, Optimal)
  - Thrashing and Working Set Model
  - Real-world OS implementations

### Recommended References:

1. **Operating System Concepts** by Silberschatz, Galvin, Gagne
2. **Operating Systems: Design and Implementation** by Andrew Tanenbaum
3. **Modern Operating Systems** by Andrew Tanenbaum
4. **Operating System Principles** by Bic & Shaw

---

## Conclusion

Page Replacement Algorithms form a crucial part of operating system design, directly impacting system performance and user experience. While the Optimal algorithm provides the theoretical limit, LRU and its approximations are widely used in practice. Understanding these algorithms prepares you for advanced topics in systems programming and computer architecture.

**Happy Learning!**

---