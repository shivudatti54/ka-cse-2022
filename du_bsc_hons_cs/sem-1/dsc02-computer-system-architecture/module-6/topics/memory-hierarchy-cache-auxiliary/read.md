# Memory Hierarchy and Cache Memory

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction to Memory Hierarchy

### 1.1 What is Memory Hierarchy?

Memory hierarchy is a concept in computer architecture that organizes different types of memory in a tiered structure, balancing the trade-offs between **speed**, **capacity**, and **cost**. The fundamental principle behind memory hierarchy is that faster memory is more expensive and therefore available in smaller quantities, while slower memory is cheaper and available in larger quantities.

### 1.2 Why Do We Need Memory Hierarchy?

In modern computer systems, there is a massive speed gap between the CPU (which can execute billions of instructions per second) and the main memory (RAM). Without an intermediate fast memory layer (cache), the CPU would spend most of its time waiting for data from slower memory, severely degrading performance.

**Real-World Relevance:**

- When you open a web browser, the recently used tabs remain in cache memory for instant access
- Loading a game: frequently accessed textures and game data are cached for smooth gameplay
- Database queries: frequently accessed database pages are cached to reduce disk I/O
- Operating systems: recently used applications remain in RAM for quick relaunching

### 1.3 Levels of Memory Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                        CPU Registers                            │
│                    (Fastest, Smallest)                          │
├─────────────────────────────────────────────────────────────────┤
│                     Level 1 Cache (L1)                          │
│                  (On-chip, ~64KB)                               │
├─────────────────────────────────────────────────────────────────┤
│                     Level 2 Cache (L2)                          │
│                  (On-chip/Off-chip, ~256KB-2MB)                 │
├─────────────────────────────────────────────────────────────────┤
│                     Level 3 Cache (L3)                          │
│                  (Shared, ~4MB-64MB)                             │
├─────────────────────────────────────────────────────────────────┤
│                      Main Memory (RAM)                          │
│                  (GB sized, ~100ns access)                       │
├─────────────────────────────────────────────────────────────────┤
│                    Secondary Storage                            │
│              (HDD/SSD - TB sized, ~ms access)                   │
├─────────────────────────────────────────────────────────────────┤
│                     Tertiary Storage                             │
│              (Magnetic Tape, Optical - Offline)                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Locality of Reference

**Locality of Reference** (also called the **principle of locality**) is the phenomenon where the CPU tends to access the same memory locations repeatedly over a short period, or tends to access memory locations that are close to each other.

### 2.1 Types of Locality

#### **Temporal Locality**
Recently accessed memory locations are likely to be accessed again in the near future.

**Example:** In a loop, the loop counter variable is accessed repeatedly.

```c
// Example of Temporal Locality
for (int i = 0; i < 1000; i++) {
    sum += array[i];  // 'sum' is accessed repeatedly (temporal locality)
}
```

#### **Spatial Locality**
If a memory location is accessed, nearby memory locations are likely to be accessed soon.

**Example:** Sequential array access or instruction sequential execution.

```c
// Example of Spatial Locality
int array[1000];
for (int i = 0; i < 1000; i++) {
    array[i] = i;  // Accessing consecutive memory locations (spatial locality)
}
```

#### **Sequential Locality**
Instructions are executed sequentially (unless branch instructions change this), leading to predictable memory access patterns.

### 2.2 Why Locality Matters for Cache

Cache memory is designed to exploit locality of reference:

- **Temporal Locality → Keep recently accessed data in cache**
- **Spatial Locality → Fetch entire cache blocks (lines) containing the accessed word**

---

## 3. Cache Memory

### 3.1 Cache Fundamentals

**Cache** is a small, fast memory placed between the CPU and main memory. It stores frequently accessed data and instructions to reduce memory access time.

**Key Terminology:**

- **Cache Hit**: When the requested data is found in the cache
- **Cache Miss**: When the requested data is not found in the cache
- **Hit Rate**: Percentage of memory accesses that result in cache hits
- **Miss Rate**: Percentage of memory accesses that result in cache misses (Miss Rate = 1 - Hit Rate)
- **Hit Time**: Time to access data in the cache
- **Miss Penalty**: Additional time required when a cache miss occurs

### 3.2 Cache Mapping Techniques

#### **3.2.1 Direct Mapping**

In direct mapping, each main memory block can be placed in **only one specific cache line**. The cache line is determined by:

```
Cache Line Index = (Block Address) mod (Number of Cache Lines)
```

**Structure of a Cache Line:**
```
┌─────────────┬──────────────┬─────────────┐
│    Tag      │   Index      │    Offset   │
└─────────────┴──────────────┴─────────────┘
```

**Example:**
- Main Memory: 16 blocks (0-15)
- Cache: 4 lines (0-3)

```
Block 0 → Cache Line 0
Block 1 → Cache Line 1
Block 2 → Cache Line 2
Block 3 → Cache Line 3
Block 4 → Cache Line 0
Block 5 → Cache Line 1
... and so on
```

#### **3.2.2 Fully Associative Mapping**

In fully associative mapping, any main memory block can be placed in **any cache line**. This provides maximum flexibility but requires comparison with all cache tags, making it expensive to implement.

**Advantages:** Maximum hit rate, no collision
**Disadvantages:** Complex hardware, expensive

#### **3.2.3 Set-Associative Mapping**

This is a compromise between direct mapping and fully associative mapping. Cache is divided into **sets**, and each set contains **n ways** (n-way set-associative).

```
Number of Sets = (Number of Cache Lines) / (Number of Ways)
```

**Example:** 8-line cache with 2-way set-associativity
- 4 sets (8/2 = 4)
- Each set has 2 lines

```
Set 0: Lines 0, 1
Set 1: Lines 2, 3
Set 2: Lines 4, 5
Set 3: Lines 6, 7
```

Memory block can be placed in any line within the determined set.

### 3.3 Hit/Miss Calculations

**Example Problem 1:**

A system has:
- L1 Cache: 64 KB, 4-way set-associative, 64-byte line size
- Main Memory: 4 GB
- Cache access time: 1 ns
- Memory access time: 100 ns

Calculate the **Average Memory Access Time (AMAT)** if the hit rate is 95%.

**Solution:**

```
AMAT = Hit Time + (Miss Rate × Miss Penalty)
     = 1 ns + (0.05 × 100 ns)
     = 1 ns + 5 ns
     = 6 ns
```

**Example Problem 2:**

A 2-way set-associative cache has 4 sets. Main memory addresses are 16 bits. Determine:
a) Number of offset bits
b) Number of index (set) bits
c) Number of tag bits

**Solution:**

- Offset bits = log₂(line size). Assuming 4 bytes per line: log₂(4) = 2 bits
- Index bits = log₂(number of sets) = log₂(4) = 2 bits
- Tag bits = Address bits - Offset bits - Index bits = 16 - 2 - 2 = **12 bits**

### 3.4 Cache Replacement Policies

When a cache miss occurs and all lines in the set are occupied, the cache controller must decide which block to replace.

#### **Least Recently Used (LRU)**

Replace the block that has not been accessed for the longest time.

```python
# Simplified LRU implementation concept
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key: address, value: (data, timestamp)
        self.time = 0
    
    def access(self, address):
        self.time += 1
        if address in self.cache:
            # Update timestamp (most recently used)
            self.cache[address] = (self.cache[address][0], self.time)
            return True  # Hit
        else:
            # Miss - need to load
            if len(self.cache) >= self.capacity:
                # Find and remove LRU item
                lru_addr = min(self.cache.keys(), 
                              key=lambda k: self.cache[k][1])
                del self.cache[lru_addr]
            self.cache[address] = (data, self.time)
            return False  # Miss
```

#### **First In First Out (FIR/FIFO)**

Replace the block that has been in the cache the longest.

#### **Least Frequently Used (LFU)**

Replace the block that has been accessed the least number of times.

### 3.5 Write Policies

Write policies determine how data is written to cache and main memory.

#### **3.5.1 Write-Through**

Data is written to both cache and main memory simultaneously.

- **Advantage:** Data consistency between cache and memory
- **Disadvantage:** Higher memory write traffic

```
CPU Write → Cache Update → Main Memory Update
```

#### **3.5.2 Write-Back**

Data is written only to the cache. The modified (dirty) block is written to main memory only when it is replaced.

- **Advantage:** Reduces memory write traffic
- **Advantage:** Faster write operations
- **Disadvantage:** Potential data inconsistency

```
CPU Write → Cache Update (Mark as Dirty)
           → Main Memory Update (only on eviction)
```

#### **3.5.3 Write-Allocate**

On a write miss, the block is first loaded into cache, then written to.

#### **3.5.4 No-Write-Allocate**

On a write miss, the data is written directly to main memory without loading into cache.

**Common Combinations:**
- Write-Through + No-Write-Allocate
- Write-Back + Write-Allocate

---

## 4. Auxiliary Memory (Secondary Storage)

Auxiliary memory provides permanent storage for data and programs. It is non-volatile and has large capacity.

### 4.1 Magnetic Disk

#### **4.1.1 Structure**

A magnetic disk consists of:
- **Platters**: Circular magnetic storage surfaces
- **Spindle**: Rotates the platters (typically 5400-15000 RPM)
- **Read/Write Head**: Reads/writes data magnetically
- **Actuator Arm**: Moves heads across the platter
- **Tracks**: Concentric circles on the platter
- **Sectors**: Pie-shaped divisions of tracks (typically 512-4096 bytes)
- **Cylinders**: Collection of tracks at the same position on all platters

#### **4.1.2 Disk Access Time**

```
Access Time = Seek Time + Rotational Latency + Transfer Time

Where:
- Seek Time: Time to move read/write head to correct track (5-15 ms)
- Rotational Latency: Time waiting for correct sector to rotate under head
                       (half of one rotation = ½ × (60/RPM) seconds)
- Transfer Time: Time to read/write the data
```

**Example Problem:**

A hard disk has:
- Seek time: 10 ms
- Rotational speed: 7200 RPM
- Transfer rate: 50 MB/s
- Sector size: 512 bytes

Calculate the time to read 10 sectors.

**Solution:**

```
Rotational Latency = (½) × (60/7200) = 4.17 ms

Transfer Time = (10 × 512 bytes) / (50 × 10⁶ bytes/s) = 0.1024 ms

Total Access Time = 10 + 4.17 + 0.1024 = 14.27 ms
```

### 4.2 Solid State Drives (SSD)

#### **4.2.1 Key Features**

- No moving parts (flash memory)
- Faster access times (< 0.1 ms vs 5-10 ms for HDD)
- Lower power consumption
- More expensive per GB
- Limited write cycles (wear leveling required)

#### **4.2.2 SSD vs HDD Performance**

| Metric | HDD | SSD |
|--------|-----|-----|
| Seek Time | 5-10 ms | < 0.1 ms |
| Sequential Read | 100-200 MB/s | 500-3500 MB/s |
| Random Read IOPS | 100-200 | 10,000-100,000 |
| Latency | ~10 ms | ~0.1 ms |

### 4.3 RAID (Redundant Array of Independent Disks)

RAID combines multiple physical disk drives into a single logical unit for improved performance, reliability, or both.

#### **RAID Levels:**

| Level | Description |冗余 | Performance |
|-------|-------------|-----|-------------|
| RAID 0 | Striping | No | Excellent |
| RAID 1 | Mirroring | Yes | Good |
| RAID 5 | Striping + Distributed Parity | Yes | Good |
| RAID 6 | Double Parity | Yes | Good |
| RAID 10 | Striping + Mirroring | Yes | Excellent |

---

## 5. Virtual Memory

Virtual memory is a technique that allows the execution of processes that may not be completely in physical memory. It provides the illusion of a larger, contiguous address space.

### 5.1 Why Virtual Memory?

- Allows programs larger than physical memory
- Provides memory protection between processes
- Simplifies memory allocation for programs
- Enables demand paging (load pages only when needed)

### 5.2 Paging

#### **5.2.1 Key Concepts**

- **Physical Memory**: Divided into fixed-size frames
- **Virtual Memory**: Divided into fixed-size pages
- **Page Table**: Maps virtual pages to physical frames
- **Page Size**: Typically 4KB, 8KB, or larger

#### **5.2.2 Address Translation**

```
Virtual Address = Virtual Page Number (VPN) + Offset
Physical Address = Physical Frame Number (PFN) + Offset
```

**Example:**

Virtual address: 32 bits
Page size: 4 KB = 2¹² bytes
Offset bits: 12
VPN bits: 32 - 12 = 20 bits
Physical memory: 4 GB = 2³² bytes
Frame size: 4 KB
PFN bits: 32 - 12 = 20 bits

### 5.3 Page Replacement Algorithms

#### **FIFO (First In First Out)**

Replace the oldest page in memory.

```python
def fifo_replace(pages, frame_count):
    frames = []
    page_faults = 0
    
    for page in pages:
        if page not in frames:
            page_faults += 1
            if len(frames) >= frame_count:
                frames.pop(0)  # Remove oldest
            frames.append(page)
    
    return page_faults

# Example
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frame_count = 3
print(f"Page Faults: {fifo_replace(pages, frame_count)}")  # Output: 9
```

#### **LRU (Least Recently Used)**

Replace the page that was least recently used.

#### **Optimal (OPT)**

Replace the page that will not be used for the longest time in the future (theoretical benchmark).

---

## 6. Numerical Problems for University Assessment

### Problem 1: Cache Hit Rate Calculation

A computer system has a cache memory with an access time of 10 ns and main memory with an access time of 100 ns. The average access time is observed to be 18 ns. Calculate the cache hit rate.

**Solution:**

```
AMAT = Hit Time + (Miss Rate × Miss Penalty)
18 = 10 + (Miss Rate × 90)
8 = Miss Rate × 90
Miss Rate = 8/90 = 0.0889
Hit Rate = 1 - 0.0889 = 0.9111 = 91.11%
```

### Problem 2: Cache Size Calculation

A cache has 64 lines and is 4-way set-associative. Each cache line stores 16 bytes of data plus a valid bit, tag, and other control information. If the tag is 12 bits and each line has 1 valid bit, calculate the total cache size in bytes.

**Solution:**

```
Number of sets = 64/4 = 16 sets

Per cache line:
- Data: 16 bytes
- Tag: 12 bits = 1.5 bytes
- Valid bit: 1 bit = 0.125 bytes
- Assuming other control: 1 byte

Total per line = 16 + 1.5 + 0.125 + 1 = 18.625 bytes

Total cache size = 64 × 18.625 = 1,192 bytes ≈ 1.2 KB
```

### Problem 3: Virtual Memory Translation

A system uses paging with a page size of 8 KB. The virtual address space is 32-bit, and physical memory is 16 MB. For the virtual address 0x1234A567, determine:
a) Virtual page number
b) Offset
c) Number of bits in page table entry

**Solution:**

```
Page size = 8 KB = 2¹³ bytes
Offset bits = 13 bits

Virtual page number = (0x1234A567 >> 13) & 0x7FFFF = 0x245A (partial)
Offset = 0x1234A567 & 0x1FFF = 0x0A567

Physical frames = 16 MB / 8 KB = 2048 frames = 2¹¹ frames
Bits for frame number = 11 bits

Page table entry needs: 11 bits (frame number) + 1 bit (valid) = 12 bits minimum
```

---

## 7. Multiple Choice Questions (MCQs)

### MCQ 1: Cache Mapping
In a direct-mapped cache with 64 cache lines, which main memory block can be placed in cache line 17?
- (a) Block 17 only
- (b) Block 17, 81, 145, ...
- (c) Block 17, 49, 81, ...
- (d) Any block

**Answer: (b)** Block = (Cache Line Number) + (n × Number of Cache Lines) = 17 + 64n

### MCQ 2: Write Policy
Which write policy provides the fastest write performance?
- (a) Write-Through
- (b) Write-Back
- (c) Write-Allocate
- (d) No-Write-Allocate

**Answer: (b)** Write-Back writes only to cache, deferring main memory writes until block replacement.

### MCQ 3: Locality of Reference
Which type of locality is exhibited by array traversal in a loop?
- (a) Temporal locality only
- (b) Spatial locality only
- (c) Both temporal and spatial
- (d) Sequential locality

**Answer: (c)** Array elements are accessed sequentially (spatial) and the same loop variables are reused (temporal).

### MCQ 4: Page Replacement
In the optimal page replacement algorithm, the page to be replaced is:
- (a) The oldest page in memory
- (b) The least recently used page
- (c) The page not used for the longest time in the future
- (d) Any page

**Answer: (c)** OPT selects the page that will not be referenced for the longest time in the future.

### MCQ 5: Cache Performance
If a cache has a 90% hit rate and miss penalty of 100 cycles, what is the average memory access time? (Assume hit time = 1 cycle)
- (a) 10.9 cycles
- (b) 91 cycles
- (c) 100 cycles
- (d) 110 cycles

**Answer: (a)** AMAT = 1 + (0.1 × 100) = 1 + 10 = 11 cycles (approximately 10.9 if considering more precision)

### MCQ 6: RAID
Which RAID level provides the best performance for read operations with redundancy?
- (a) RAID 0
- (b) RAID 1
- (c) RAID 5
- (d) RAID 6

**Answer: (b)** RAID 1 (mirroring) provides excellent read performance as data can be read from either mirror disk.

### MCQ 7: Virtual Memory
What is the main advantage of virtual memory?
- (a) Faster execution
- (b) Larger address space than physical memory
- (c) Reduced hardware cost
- (d) Elimination of page faults

**Answer: (b)** Virtual memory allows programs to use more memory than physically available.

### MCQ 8: Associativity
A 16 KB cache with 64-byte lines is 4-way set-associative. How many sets does it have?
- (a) 64
- (b) 256
- (c) 4
- (d) 16

**Answer: (a)** Lines = 16 KB / 64 B = 256 lines. Sets = 256 / 4 = 64 sets.

---

## 8. Flashcards

### Flashcard 1
**Q: What is the difference between temporal and spatial locality?**

**A:** Temporal locality means recently accessed items will likely be accessed again (e.g., loop variables). Spatial locality means items near recently accessed locations will likely be accessed soon (e.g., sequential array access).

### Flashcard 2
**Q: Why is write-back faster than write-through?**

**A:** Write-back only writes to cache and delays writing to main memory until block replacement. Write-through must write to both cache and main memory on every write, causing more memory traffic.

### Flashcard 3
**Q: What is the purpose of the tag field in a cache?**

**A:** The tag field uniquely identifies which memory block is stored in a cache line. During a cache access, the CPU compares the tag portion of the address with the stored tag to determine a hit or miss.

### Flashcard 4
**Q: Define cache miss penalty.**

**A:** Cache miss penalty is the additional time required to fetch data from main memory when a cache miss occurs. It includes the time to access main memory and load the required block into cache.

### Flashcard 5
**Q: What is the advantage of set-associative mapping over direct mapping?**

**A:** Set-associative mapping reduces conflict misses by allowing each memory block to be placed in one of multiple lines within a set, rather than being restricted to a single cache line like in direct mapping.

### Flashcard 6
**Q: What is wear leveling in SSDs?**

**A:** Wear leveling is a technique that ensures write operations are distributed evenly across all memory cells in an SSD, preventing certain cells from wearing out faster than others and extending the drive's lifespan.

### Flashcard 7
**Q: What is a page fault?**

**A:** A page fault occurs when a process accesses a memory page that is not currently in physical memory (RAM). The operating system must then load the required page from secondary storage, causing significant delay.

### Flashcard 8
**Q: Explain the working of TLB (Translation Lookaside Buffer).**

**A:** TLB is a hardware cache that stores recent virtual-to-physical address translations. It speeds up memory access by avoiding page table lookups for frequently used virtual addresses.

---

## 9. Key Takeaways

1. **Memory Hierarchy**: Modern computers use a hierarchical structure (registers → cache → RAM → secondary storage) to balance speed, capacity, and cost.

2. **Locality of Reference**: The principle that programs tend to access the same or nearby memory locations repeatedly. This is the fundamental reason caching works.

3. **Cache Memory**:
   - **Mapping**: Direct, fully-associative, and set-associative mapping techniques determine where blocks can be placed
   - **Write Policies**: Write-through and write-back determine how writes are handled
   - **Replacement**: LRU, FIFO, and LFU are common algorithms when evicting blocks

4. **Performance Metrics**:
   - Hit Rate + Miss Rate = 1
   - AMAT = Hit Time + (Miss Rate × Miss Penalty)

5. **Auxiliary Memory**:
   - Magnetic disks: Seek time + rotational latency + transfer time
   - SSDs: Faster but more expensive; use flash memory
   - RAID: Provides redundancy and performance improvements

6. **Virtual Memory**:
   - Enables execution of programs larger than physical memory
   - Paging divides memory into fixed-size pages and frames
   - Page replacement algorithms (FIFO, LRU, OPT) manage which pages to evict

7. **Delhi University Syllabus Alignment**: This topic covers essential concepts in Computer System Architecture, including memory organization, cache design, and virtual memory management as per the NEP 2024 UGCF curriculum.

---

*Study Material prepared for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)*