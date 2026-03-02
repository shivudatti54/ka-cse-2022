# Virtual Memory Management

## Introduction

Virtual Memory Management is a critical component of modern operating systems that allows processes to execute without being entirely loaded into physical memory. It creates an abstraction layer between the logical memory perceived by processes and the physical memory hardware, enabling efficient memory utilization and multiprogramming.

The key advantages include:

1. **Memory Isolation**: Processes operate in separate address spaces
2. **Overcommitment**: Total virtual memory can exceed physical RAM
3. **Simplified Programming**: Developers work with contiguous logical addresses
4. **Demand Paging**: Load only required pages into memory

This concept is fundamental for implementing features like file memory mapping, process checkpointing, and efficient context switching. exams frequently test page replacement algorithms, effective access time calculations, and thrashing analysis.

## Key Concepts

### 1. Demand Paging

Load pages into memory only when needed (on page fault). Uses a **valid-invalid bit** in page tables:

- Valid: Page is in memory
- Invalid: Page not loaded or invalid

**Page Fault Handling Process**:

1. Check internal page table
2. If invalid, trap to OS
3. Find free frame (or page out)
4. Load required page
5. Update page table
6. Restart instruction

Effective Access Time (EAT) Formula:

```
EAT = (1 - p) × ma + p × page_fault_time
Where:
p = page fault rate (0 ≤ p ≤ 1)
ma = memory access time
```

### 2. Copy-on-Write (COW)

Optimization technique where parent and child processes initially share the same physical pages. Copies are made only when either process modifies a page. Crucial for:

- Efficient `fork()` implementation
- Memory sharing in multithreaded apps
- Snapshot creation in databases

### 3. Page Replacement Algorithms

Used when free frames are unavailable during page faults:

#### FIFO (First-In First-Out)

- Replace oldest page
- Suffers from **Belady's Anomaly** (more frames → more faults)
- Example: Queue implementation

#### Optimal Algorithm

- Replace page not used for longest future time
- Theoretical (requires future knowledge)
- Serves as benchmark

#### LRU (Least Recently Used)

- Track page usage with counters/stack
- Approximates Optimal
- Implementation methods:
- Counter-based: Timestamp each reference
- Stack implementation: Move accessed page to top

#### Clock Algorithm (Second Chance)

- Circular queue with reference bit
- If R=1: Give second chance, clear bit
- If R=0: Replace page

### 4. Thrashing

When system spends more time paging than executing due to:

- Over-commitment of memory
- Low CPU utilization
- High page fault rate

**Solutions**:

- Working Set Model: Track pages used in time window
- Page Fault Frequency (PFF): Adjust allocated frames
- Limit multiprogramming level

## Examples

### Example 1: Page Replacement (FIFO vs Optimal vs LRU)

**Reference String**: 7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1
**Frame Count**: 3

**FIFO Solution**:

```
Step | Frames | Fault
-----|-------------|-----
1 | [7] | Yes
2 | [7,0] | Yes
3 | [7,0,1] | Yes
4 | [0,1,2] | Yes (Replace 7)
5 | [0,1,2] | No
... Continue tracking...
Total Page Faults = 15
```

**Optimal Solution**:

```
Step | Frames | Fault
-----|-------------|-----
1 | [7] | Yes
2 | [7,0] | Yes
3 | [7,0,1] | Yes
4 | [0,1,2] | Yes (7 not used soonest)
... Continue tracking...
Total Page Faults = 9
```

**LRU Solution**:

```
Step | Frames | Fault
-----|-------------|-----
1 | [7] | Yes
2 | [7,0] | Yes
3 | [7,0,1] | Yes
4 | [0,1,2] | Yes (7 least recently used)
... Continue tracking...
Total Page Faults = 12
```

### Example 2: Effective Access Time Calculation

Given:

- Memory access time = 200ns
- Page fault service time = 8ms
- Page fault rate = 0.1%

```
EAT = (1 - 0.001) × 200ns + 0.001 × 8,000,000ns
 = 0.999 × 200 + 0.001 × 8,000,000
 = 199.8 + 8,000
 = 8,199.8ns ≈ 8.2μs
```

## Real-World Applications

1. **Database Systems**: Use demand paging for large query result sets
2. **Virtualization**: Hypervisors implement nested page tables
3. **Mobile OS**: Aggressive page replacement for battery optimization
4. **Cloud Computing**: Memory overcommitment in VMs
5. **Game Engines**: Texture streaming using virtual memory

## Exam Tips

1. **Page Replacement Algorithms**: Practice solving numericals for FIFO, LRU, and Optimal. often gives reference strings with 3-4 frames.
2. **Formula Recall**: Memorize EAT formula and thrashing equations.
3. **COW Identification**: Look for keywords like "fork()", "shared memory", or "zero-fill-on-demand".
4. **Belady's Anomaly**: Only FIFO exhibits this. Be prepared to demonstrate with example.
5. **Thrashing Solutions**: Working set model and PFF are frequent 5-mark questions.
6. **TLB Impact**: Remember TLB hit/miss affects effective access time.
7. **Linux Specifics**: Know the CLOCK-Pro algorithm (modified Clock) used in practice.
