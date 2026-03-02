# Virtual Memory: Demand Paging

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University

---

## 1. Introduction

**Virtual Memory** is one of the most significant concepts in modern operating systems, enabling programs to execute even when the physical RAM is smaller than the program's size. It creates an illusion for users that their system has unlimited memory by using a combination of hardware and software to manage memory pages between RAM and secondary storage (usually a disk).

**Demand Paging** is a virtual memory management technique where pages are brought into memory only when they are needed (i.e., when a page fault occurs). This approach optimizes memory usage by loading data on-demand rather than loading entire programs at startup.

### Real-World Relevance

- **Modern Computing**: Every smartphone, laptop, and desktop computer uses demand paging. When you open a 2GB application on a system with 4GB RAM, demand paging allows it to run efficiently.
- **Multitasking**: Enables running multiple applications simultaneously without worrying about physical memory constraints.
- **Cloud Computing**: Virtual machines use demand paging to overcommit resources efficiently.
- **Application Performance**: Lazy loading in web applications mirrors the demand paging philosophy.

---

## 2. Fundamentals of Virtual Memory

### 2.1 What is Virtual Memory?

Virtual memory creates a logical address space that is larger than the physical address space. The operating system maintains a **page table** that maps virtual addresses to physical addresses.

**Key Components:**
- **Virtual Address Space**: Address space as seen by the process
- **Physical Address Space**: Actual RAM locations
- **Page Table**: Mapping structure between virtual and physical pages
- **Translation Lookaside Buffer (TLB)**: Hardware cache for page table entries

### 2.2 How Virtual Memory Works

```
Virtual Address → [MMU] → Physical Address
                        ↑
                  Page Table
```

The Memory Management Unit (MMU) translates virtual addresses to physical addresses using the page table.

---

## 3. Demand Paging: The Concept

### 3.1 What is Demand Paging?

Demand paging is a page loading strategy where pages are loaded into memory **only when a process references them**. This follows the principle of **locality of reference** — programs tend to access only a small portion of their address space at any given time.

### 3.2 How Demand Paging Works

1. **Process Starts**: Only a few initial pages are loaded
2. **Page Fault Occurs**: When a process accesses a page not in memory
3. **OS Intervention**: Operating system loads the required page from secondary storage
4. **Page Table Update**: Valid/Invalid bit set to valid, frame number updated
5. **Restart Instruction**: The instruction that caused the fault is re-executed

### 3.3 Page Fault Handling Steps

```
1. Trap to OS (page fault interrupt)
2. OS determines the virtual address that caused fault
3. OS checks if reference is valid and finds free frame
4. If no free frame, select victim page using replacement algorithm
5. If victim page is dirty, write it to disk (page replacement)
6. Load required page into selected frame
7. Update page table
8. Restart the interrupted instruction
```

---

## 4. Performance of Demand Paging

### 4.1 Effective Access Time (EAT)

The effective access time is crucial for understanding demand paging performance.

**Formula:**
```
EAT = (1 - p) × Memory Access Time + p × Page Fault Time
```

Where:
- `p` = page fault rate (0 ≤ p ≤ 1)
- Memory Access Time typically = 100-200 nanoseconds
- Page Fault Time includes: disk I/O (8-10 ms) + OS overhead

**Note**: For Delhi University exams, remember that disk access time dominates!

### 4.2 Numerical Example 1: Basic EAT Calculation

**Problem**: A system has memory access time of 100 ns. The average page fault service time is 10 ms (10,000,000 ns). Calculate the effective access time if the page fault rate is 0.001 (0.1%).

**Solution**:

```
EAT = (1 - p) × Memory Access Time + p × Page Fault Time
EAT = (1 - 0.001) × 100 ns + 0.001 × 10,000,000 ns
EAT = 0.999 × 100 + 10,000
EAT = 99.9 + 10,000
EAT = 10,099.9 ns ≈ 10.1 μs
```

**Observation**: Even with a 0.1% page fault rate, access time increases from 100 ns to over 10,000 ns (100x slower)!

### 4.3 Numerical Example 2: Finding Maximum Page Fault Rate

**Problem**: Memory access time is 200 ns. We want EAT to be at most 400 ns. Page fault time is 10 ms. What is the maximum allowable page fault rate?

**Solution**:

```
EAT = (1 - p) × Memory Time + p × Page Fault Time
400 = (1 - p) × 200 + p × 10,000,000
400 = 200 - 200p + 10,000,000p
400 - 200 = 10,000,000p - 200p
200 = 9,999,800p
p = 200 / 9,999,800
p ≈ 0.00002 = 0.002%
```

**Maximum page fault rate = 0.002%**

---

## 5. Page Replacement Algorithms

When a page fault occurs and all frames are occupied, the operating system must select a victim page to replace. This is where page replacement algorithms come in.

### 5.1 First In First Out (FIFO)

**Principle**: Replace the oldest page in memory.

**Example with frames = 3**:

Reference String: **7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2**

| Reference | Frame 1 | Frame 2 | Frame 3 | Page Fault |
|-----------|---------|---------|---------|------------|
| 7 | **7** | - | - | ✓ |
| 0 | 7 | **0** | - | ✓ |
| 1 | 7 | 0 | **1** | ✓ |
| 2 | **2** | 0 | 1 | ✓ |
| 0 | 2 | **0** | 1 | ✗ |
| 3 | 2 | 0 | **3** | ✓ |
| 0 | 2 | **0** | 3 | ✗ |
| 4 | **4** | 0 | 3 | ✓ |
| 2 | 4 | 0 | **2** | ✓ |
| 3 | 4 | 0 | 2 | ✓ |
| 0 | 4 | **0** | 2 | ✗ |
| 3 | 4 | 0 | **3** | ✓ |
| 2 | 4 | 0 | **2** | ✓ |

**Page Faults = 9**

### 5.2 Optimal Page Replacement (OPT)

**Principle**: Replace the page that will not be used for the longest time in the future.

**Note**: This is theoretical — impossible to implement in practice but used as a benchmark.

### 5.3 Least Recently Used (LRU)

**Principle**: Replace the page that has not been used for the longest time.

**Same Example with LRU**:

| Reference | Frame 1 | Frame 2 | Frame 3 | Page Fault |
|-----------|---------|---------|---------|------------|
| 7 | **7** | - | - | ✓ |
| 0 | 7 | **0** | - | ✓ |
| 1 | 7 | 0 | **1** | ✓ |
| 2 | **2** | 0 | 1 | ✓ |
| 0 | 2 | **0** | 1 | ✗ |
| 3 | 2 | 0 | **3** | ✓ |
| 0 | 2 | **0** | 3 | ✗ |
| 4 | **4** | 0 | 3 | ✓ |
| 2 | 4 | **2** | 3 | ✓ |
| 3 | 4 | 2 | **3** | ✗ |
| 0 | **0** | 2 | 3 | ✓ |
| 3 | 0 | 2 | **3** | ✗ |
| 2 | 0 | **2** | 3 | ✗ |

**Page Faults = 8**

### 5.4 Other Algorithms

- **Second Chance (Clock)**: FIFO with reference bit check
- **Not Recently Used (NRU)**: Based on reference and modify bits
- **Most Recently Used (MRU)**: Opposite of LRU

### 5.5 Belady's Anomaly

Belady's anomaly is a phenomenon where increasing the number of page frames can **increase** the number of page faults with FIFO algorithm.

**Example**: Reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

- With 3 frames: 9 page faults
- With 4 frames: 10 page faults

---

## 6. Thrashing

### 6.1 What is Thrashing?

Thrashing occurs when a computer spends more time **swapping pages in and out of memory** than executing processes. It's a severe performance degradation caused by excessive paging.

### 6.2 Causes of Thrashing

1. **Insufficient Frames**: Process doesn't have enough frames for its working set
2. **High Degree of Multiprogramming**: Too many processes competing for limited memory
3. **Poor Page Replacement Algorithm**: Selecting wrong victim pages

### 6.3 Symptoms of Thrashing

- High CPU utilization suddenly drops
- Constant disk I/O (paging activity)
- Processes seem to be running but make little progress
- System becomes extremely slow and unresponsive

### 6.4 Solution to Thrashing

1. **Working Set Model**: Keep pages that processes have recently used in memory
2. **Page Fault Frequency**: Control page fault rate by adjusting degree of multiprogramming
3. **Priority Scheduling**: Give more frames to higher priority processes
4. **Increase Physical Memory**: Add more RAM (hardware solution)

### 6.5 Working Set Model

The **working set** is the set of pages a process has used in the last τ (tau) time units.

- **WS**: Working set size
- **τ (tau)**: Window size
- If working set > available frames → thrashing

```
If Σ(WS of all processes) > Total Frames → Thrashing
Suspend some processes until Σ(WS) < Total Frames
```

---

## 7. Allocation of Frames

### 7.1 Fixed Allocation

Each process receives a fixed number of frames regardless of its needs.

### 7.2 Priority Allocation

Processes with higher priority get more frames.

### 7.3 Global vs Local Replacement

- **Global Replacement**: Process can select victim from any frame in the system
- **Local Replacement**: Process can only select from its own allocated frames

---

## 8. Additional Concepts for Delhi University

### 8.1 Copy-on-Write

When a parent process forks a child, pages are initially shared. If either process modifies a page, a separate copy is created for that process.

### 8.2 Memory-Mapped Files

Files are mapped to virtual addresses, allowing file I/O through memory operations.

### 8.3 Prepaging

Loading pages before they're needed to reduce page faults (opposite of demand paging).

---

## 9. Key Takeaways

1. **Demand Paging** loads pages only when referenced, optimizing memory usage
2. **Page Fault** occurs when a requested page is not in memory
3. **Effective Access Time (EAT)** = (1-p) × memory access + p × page fault time
4. **FIFO** is simple but suffers from Belady's anomaly
5. **LRU** approximates OPT but has higher overhead
6. **Thrashing** occurs when excessive paging degrades performance
7. **Working Set Model** helps prevent thrashing by maintaining recently used pages
8. Page fault service time is dominated by disk I/O (typically 8-10 ms)

---

## 10. Delhi University Exam Focus Points

- Numerical problems on EAT calculation
- Page replacement algorithm problems (FIFO, LRU, OPT)
- Belady's anomaly identification
- Thrashing causes and solutions
- Page fault handling procedure
- Working set calculations

---

## 11. Multiple Choice Questions (MCQs)

### Basic Level

**Q1. In demand paging:**
- (a) All pages are loaded at process startup
- (b) Pages are loaded only when referenced ✓
- (c) Pages are never loaded from disk
- (d) Pages are loaded before they are needed

**Q2. A page fault occurs when:**
- (a) The requested page is in memory
- (b) The requested page is not in memory ✓
- (c) The CPU fails
- (d) The page table is empty

**Q3. Which of the following has the lowest page fault rate?**
- (a) FIFO
- (b) LRU
- (c) Optimal ✓
- (d) Random

### Intermediate Level

**Q4. If memory access time is 100 ns and page fault time is 10 ms, calculate EAT when page fault rate is 0.5%:**
- (a) 100 ns
- (b) 50,100 ns ✓
- (c) 10,000 ns
- (d) 100.5 ns

**Solution**: EAT = 0.995 × 100 + 0.005 × 10,000,000 = 99.5 + 50,000 = 50,099.5 ns ≈ 50,100 ns

**Q5. Belady's anomaly is associated with:**
- (a) LRU
- (b) Optimal
- (c) FIFO ✓
- (d) Stack algorithms

**Q6. Thrashing is caused by:**
- (a) Excessive page faults ✓
- (b) Low CPU utilization
- (c) Too few processes
- (d) High memory speed

**Q7. Working set model is used to:**
- (a) Increase CPU speed
- (b) Prevent thrashing ✓
- (c) Improve cache performance
- (d) Reduce disk capacity

### Advanced Level

**Q8. A system has 3 frames. Reference string: 1,2,3,4,1,2,5,1,2,3,4,5. Using FIFO, page faults are:**
- (a) 9 ✓
- (b) 8
- (c) 10
- (d) 7

**Q9. Which is NOT a valid page replacement algorithm?**
- (a) LRU
- (b) FIFO
- (c) SJF ✓
- (d) Optimal

**Q10. The valid-invalid bit in page table indicates:**
- (a) Whether the page is dirty
- (b) Whether the page is in memory ✓
- (c) Whether the page is shared
- (d) Whether the page is protected

**Q11. If effective access time increases from 100 ns to 1 μs with page faults, and page fault time is 10 ms, find page fault rate:**
- (a) 0.009%
- (b) 0.009 ✓
- (c) 0.9%
- (d) 9%

**Solution**: 1000 = (1-p)×100 + p×10,000,000; 1000 ≈ p×10,000,000; p ≈ 0.0001 = 0.01% (closest is 0.009%)

**Q12. TLB stands for:**
- (a) Translation Lookaside Buffer ✓
- (b) Time Loop Buffer
- (c) Transient Local Buffer
- (d) Translation Local Buffer

**Q13. In global page replacement:**
- (a) Process can only use its own frames
- (b) Process can use any frame ✓
- (c) No replacement occurs
- (d) Only OS pages are replaced

**Q14. Copy-on-write is used in:**
- (a) Process scheduling
- (b) Fork operations ✓
- (c) Disk scheduling
- (d) CPU scheduling

**Q15. The page fault service time is dominated by:**
- (a) CPU time
- (b) OS overhead
- (c) Disk I/O ✓
- (d) Network delay

---

## 12. Flashcards

| Term | Definition |
|------|------------|
| **Virtual Memory** | Memory management technique that creates illusion of larger memory using disk |
| **Demand Paging** | Loading pages into memory only when referenced |
| **Page Fault** | Interrupt when requested page is not in memory |
| **Effective Access Time** | Weighted average of memory access and page fault times |
| **FIFO** | Page replacement - oldest page replaced first |
| **LRU** | Page replacement - least recently used page replaced |
| **Thrashing** | Excessive paging causing performance degradation |
| **Working Set** | Set of pages recently used by a process |
| **Belady's Anomaly** | Paradox where more frames cause more page faults |
| **TLB** | Hardware cache for page table entries |
| **Valid-Invalid Bit** | Page table bit indicating if page is in memory |
| **Clean Page** | Page in memory not modified |
| **Dirty Page** | Page in memory modified, needs writing to disk |
| **Local Replacement** | Process selects victim from its own frames only |
| **Global Replacement** | Process can select victim from any frame |

---

## 13. Summary for Quick Revision

```
┌─────────────────────────────────────────────────────────────┐
│                  DEMAND PAGING SUMMARY                      │
├─────────────────────────────────────────────────────────────┤
│  Page Fault Rate (p) → EAT Impact                           │
│  p = 0     → EAT = Memory Access Time                       │
│  p = 1     → EAT = Page Fault Time (dominantly disk I/O)    │
│                                                             │
│  Algorithms (by performance):                               │
│  Optimal > LRU > Second Chance > FIFO                      │
│                                                             │
│  Thrashing Solutions:                                       │
│  • Working Set Model                                        │
│  • Page Fault Frequency Control                            │
│  • Increase Physical Memory                                 │
│  • Reduce Degree of Multiprogramming                        │
└─────────────────────────────────────────────────────────────┘
```

---

*Prepared for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)*
*Virtual Memory — Demand Paging*