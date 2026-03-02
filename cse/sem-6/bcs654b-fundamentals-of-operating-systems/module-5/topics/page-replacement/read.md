# Page Replacement Algorithms

## Introduction to Page Replacement

Page replacement is a critical component of virtual memory management in modern operating systems. When physical memory (RAM) becomes full, the OS must decide which pages to evict to make space for new pages required by running processes. The efficiency of this process directly impacts system performance, as frequent page faults lead to increased disk I/O and reduced throughput.

The primary challenge lies in selecting victim pages that are least likely to be used in the near future. Different algorithms employ various strategies to predict future page usage patterns based on past behavior. The choice of algorithm affects:

- Overall system performance
- Memory utilization efficiency
- Process execution speed
- Hardware resource management

Modern operating systems implement sophisticated page replacement strategies to balance between:

1. Computational overhead of the algorithm
2. Accuracy in predicting future page needs
3. Hardware support requirements
4. Adaptability to different workload patterns

## Key Concepts and Algorithms

### FIFO (First-In, First-Out)

**Principle:** Replace the page that has been in memory longest
**Implementation:** Maintains a queue of pages in memory
**Characteristics:**

- Simple to implement (uses a pointer/circular buffer)
- Suffers from Belady's Anomaly
- Poor correlation between page age and future usage

**Example Calculation:**

```
Reference String: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
Frame Count: 3

Page Faults: 15
```

### Optimal Page Replacement

**Principle:** Replace the page that will not be used for the longest time in the future
**Implementation:** Requires future knowledge of reference string
**Characteristics:**

- Theoretical upper bound for performance
- Impossible to implement in practice
- Useful for comparison studies

**Example Calculation (Same Reference String):**

```
Page Faults: 9
```

### LRU (Least Recently Used)

**Principle:** Replace the page that has not been used for the longest time
**Implementation:** Maintains access timestamps or stack ordering
**Characteristics:**

- Closer to optimal performance
- Higher implementation overhead
- Requires hardware support (counters/registers)

**Variants:**

1. Counter-based implementation
2. Stack implementation

**Example Calculation (Same Reference String):**

```
Page Faults: 12
```

### Clock (Second Chance)

**Principle:** Circular buffer with reference bits (approximates LRU)
**Implementation Steps:**

1. Arrange pages in circular list
2. Check reference bit of current page
3. If 0 → replace, if 1 → set to 0 and move pointer
4. Repeat until page with 0 found

**Characteristics:**

- Lower overhead than true LRU
- Reasonable performance
- Used in Windows and Linux kernels

**Example Calculation (Same Reference String):**

```
Page Faults: 13
```

## Belady's Anomaly

**Definition:** The phenomenon where increasing the number of frames can lead to more page faults
**Occurs In:** FIFO and other stackless algorithms
**Example Demonstration:**

```
Reference String: 1 2 3 4 1 2 5 1 2 3 4 5

With 3 frames: 9 page faults
With 4 frames: 10 page faults
```

## Performance Comparison

| Algorithm | Page Faults (Example) | Implementation Complexity | Belady's Anomaly | Real-World Usage |
| --------- | --------------------- | ------------------------- | ---------------- | ---------------- |
| FIFO      | 15                    | Low                       | Yes              | Rare             |
| Optimal   | 9                     | Impossible                | No               | Theoretical      |
| LRU       | 12                    | High                      | No               | Common           |
| Clock     | 13                    | Moderate                  | No               | Widespread       |

## Real-World Applications

1. Database caching (LRU variants)
2. Web server caching (Adaptive replacement)
3. Mobile OS memory management (Clock algorithm)
4. Virtual machine hypervisors (Combined approaches)

## Worked Examples

### Example 1: FIFO with 4 Frames

**Reference String:** 0 1 2 3 0 1 4 0 1 2 3 4
**Solution:**

```
Step-by-Step:
0 [0] - Fault
1 [0,1] - Fault
2 [0,1,2] - Fault
3 [0,1,2,3] - Fault
0 [1,2,3,0] - Fault (Replace 0)
1 [2,3,0,1] - Fault (Replace 1)
4 [3,0,1,4] - Fault (Replace 2)
0 [0,1,4,0] - No change
... Continue pattern
Total Page Faults: 8
```

### Example 2: LRU with 3 Frames

**Reference String:** 7 0 1 2 0 3 0 4
**Solution:**

```
7 [7] - Fault
0 [7,0] - Fault
1 [7,0,1] - Fault
2 [0,1,2] - Fault (Replace 7)
0 [1,2,0] - Update order
3 [2,0,3] - Fault (Replace 1)
0 [2,3,0] - Update order
4 [3,0,4] - Fault (Replace 2)
Total Page Faults: 7
```

## Exam Tips

1. Always start page fault calculations from empty memory state
2. For FIFO, maintain strict insertion order (use arrow diagrams)
3. In LRU, track exact reference sequence (stack implementation works best)
4. Clock algorithm's reference bits reset periodically (explain the circular scan)
5. Belady's Anomaly identification: Check if increasing frames increases faults in FIFO
6. Optimal algorithm gives minimum possible faults - use it as reference
7. Real systems combine algorithms: e.g., Linux uses modified Clock (Two-List strategy)

## Memory Management Formulas

1. **Effective Access Time (EAT):**

```
EAT = (1 - p) × Memory Access Time + p × Page Fault Time
Where p = page fault rate
```

2. **Page Fault Calculation:**

```
Total Page Faults = ∑ (Page not found in memory)
```

3. **Dirty Page Modification:**

```
Page Replace Time = 2 × Transfer Time (if dirty) + Seek Time
```

## Advanced Concepts

- Working Set Model
- Page Buffering (Keep replaced pages in cache)
- Thrashing Detection and Prevention
- NUMA-aware Page Replacement
