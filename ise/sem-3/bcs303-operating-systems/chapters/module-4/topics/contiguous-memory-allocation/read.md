# Contiguous Memory Allocation

## Introduction

Contiguous memory allocation is one of the earliest and most fundamental memory management techniques used in operating systems. In this approach, each process is allocated a single continuous block of physical memory that is sufficient to hold the entire process. This means that when a program is loaded into memory, it occupies a single, unbroken region of RAM from its starting address to its ending address.

The significance of contiguous memory allocation lies in its simplicity and efficiency. When a process has all its instructions and data stored in consecutive memory locations, the CPU can access any memory location within that process using a simple calculation: the physical address is obtained by adding the base register (holding the starting address) to the logical address offset. This direct mapping makes memory access extremely fast, with no additional overhead for page table lookups or translation lookaside buffers.

However, contiguous memory allocation faces two critical challenges that have led to the development of more sophisticated techniques like paging and segmentation. The first problem is **external fragmentation**, where free memory exists in small, scattered chunks that cannot satisfy a large process request even though the total free memory would be sufficient. The second challenge is **internal fragmentation**, which occurs when allocated memory blocks are larger than what the process actually requires, resulting in wasted space within each partition. Understanding these trade-offs is essential for appreciating why modern operating systems employ more complex memory management strategies while still using contiguous allocation as a foundational concept.

## Key Concepts

### Fixed Partitioning

Fixed partitioning was the earliest implementation of contiguous memory allocation, where the operating system divides physical memory into a predetermined number of partitions at system startup. These partitions can be of equal size or unequal sizes defined by the system administrator. When a process needs to be loaded, the system selects a partition that is large enough to accommodate the process.

In equal-sized fixed partitioning, any process can be loaded into any available partition, which simplifies the allocation algorithm but leads to significant internal fragmentation. If a process requires only 10 MB but is loaded into a 50 MB partition, 40 MB of memory is wasted. Unequal-sized partitions attempt to mitigate this problem by providing a variety of partition sizes, allowing the system to choose a partition that more closely matches the process requirements.

The major advantage of fixed partitioning is the simplicity of implementation. The memory manager only needs to track which partitions are occupied and which are free. However, the number of partitions also limits the maximum number of processes that can run concurrently, and the severe internal fragmentation makes this approach highly inefficient for modern systems.

### Variable Partitioning

Variable partitioning, also known as dynamic or可变分区, represents an improvement over fixed partitioning by allocating exactly the amount of memory requested by each process. The operating system maintains a list of free memory holes and allocates space from these holes based on process requirements. When a process terminates, its memory is returned to the pool of free holes, which may then be combined with adjacent free holes through a process called **coalescing**.

Variable partitioning eliminates internal fragmentation since each process gets exactly what it needs. However, it introduces external fragmentation because the free memory becomes fragmented into holes of varying sizes. Over time, as processes are loaded and terminated, the memory may consist of many small holes that cannot satisfy large allocation requests even when the total free memory is sufficient.

### Allocation Strategies

When a process requests memory, the operating system must decide which free hole to use. Three primary strategies exist:

**First-fit**: The system scans the list of free holes from the beginning and allocates the first hole that is large enough to satisfy the request. This strategy is fast because it minimizes the search time, and in practice, it tends to allocate memory quickly to most requests.

**Best-fit**: The system searches through all free holes and selects the smallest one that can accommodate the request. This approach tries to leave larger holes for future use, but it requires scanning the entire free list and tends to create small, less usable holes over time.

**Worst-fit**: The system selects the largest available hole for allocation. The rationale is that the remaining portion of a large hole will still be substantial enough to be useful for future allocations. However, worst-fit also requires scanning the entire list and may not perform well in practice.

Simulations and empirical studies have shown that first-fit and best-fit generally perform better than worst-fit in terms of memory utilization. First-fit is often preferred due to its speed, while best-fit may achieve slightly better memory utilization at the cost of more processing time.

### Memory Protection

In contiguous memory allocation, protection is implemented using **boundary registers**. The operating system maintains a pair of registers for each process: a **base register** containing the starting physical address of the process's memory block, and a **limit register** containing the size of the allocated region. Every memory access by the process is validated by checking whether the logical address falls within the range from 0 to the limit. If an attempt is made to access memory outside the allocated region, a memory protection fault is generated, preventing one process from accessing another's memory.

This protection mechanism is extremely efficient because it requires only two comparisons for each memory access. The base register is added to the logical address to generate the physical address, and the limit check ensures that the offset does not exceed the allocated size.

### External Fragmentation

External fragmentation occurs when free memory is divided into small, non-contiguous blocks. Even though the total free memory might exceed the request, no single block is large enough. External fragmentation is measured by the percentage of total memory that is unusable for allocation.

Two solutions exist for external fragmentation. The first is **compaction**, where the operating system periodically moves all allocated processes in memory to consolidate free space into one large block. However, compaction is expensive because it requires copying entire processes and updating all memory references, including base registers and any cached addresses. The second solution is to employ non-contiguous allocation schemes like paging or segmentation, which allow a process to be allocated in multiple separate memory blocks.

### Internal Fragmentation

Internal fragmentation occurs in fixed partitioning when the allocated partition is larger than the requested memory. The difference between the partition size and the actual request size represents wasted memory that cannot be used by other processes. For example, if a 16 MB partition is allocated to a process requiring 12 MB, 4 MB is internally fragmented.

The formula for internal fragmentation is straightforward: Internal Fragmentation = Allocated Block Size - Actual Request Size. With variable partitioning, internal fragmentation is minimal or zero since exactly the requested amount is allocated. However, many systems use variable partitioning with a minimum allocation unit or header overhead, which can still introduce some internal fragmentation.

## Examples

### Example 1: Fixed Partitioning Allocation

Consider a system with fixed partitions of sizes: 10 MB, 20 MB, 30 MB, and 40 MB. Three processes arrive with memory requirements: P1 = 8 MB, P2 = 25 MB, P3 = 15 MB.

**Solution**:
- P1 (8 MB) can be loaded into partition 1 (10 MB) - 2 MB internal fragmentation
- P2 (25 MB) can be loaded into partition 3 (30 MB) - 5 MB internal fragmentation
- P3 (15 MB) can be loaded into partition 2 (20 MB) - 5 MB internal fragmentation

Total internal fragmentation = 2 + 5 + 5 = 12 MB. The system cannot accommodate a fourth process requiring 35 MB because no single partition is large enough, even though total used memory is only 8 + 25 + 15 = 48 MB out of 100 MB total, with 52 MB free but distributed across partitions.

### Example 2: First-Fit Allocation

Memory state: Free holes at addresses [100-200], [400-450], [600-800], [1000-1200] with sizes 100, 50, 200, and 200 respectively.

Process A requests 80 MB: First-fit selects hole [100-200], allocates at base 100, remaining free space is [180-200] = 20 MB.

Process B requests 120 MB: First-fit scans [180-200] (too small), [400-450] (too small), [600-800] (sufficient), allocates at base 600, remaining free space is [720-800] = 80 MB.

Process C requests 60 MB: First-fit selects [180-200], allocates at base 180, remaining free space is [240-200] (impossible - less than request, so no allocation). The algorithm moves to [400-450], allocates at base 400, remaining free space is [460-450] (negative, so hole is exhausted).

### Example 3: External Fragmentation Analysis

Consider a system with variable partitioning where processes are allocated and deallocated in the following sequence:

1. Allocate P1: 100 KB - occupies [0-100]
2. Allocate P2: 50 KB - occupies [100-150]
3. Allocate P3: 150 KB - occupies [150-300]
4. P2 terminates - free at [100-150]
5. Allocate P4: 80 KB - occupies [100-180]
6. P1 terminates - free at [0-100]
7. Allocate P5: 200 KB

For P5's allocation of 200 KB:
- First-fit: Checks [0-100] (100 KB - insufficient), then [180-300] (120 KB - insufficient). Cannot allocate despite total free memory being 100 + 120 = 220 KB.
- If P4 also terminates: Free holes at [0-100] and [180-300], totaling 220 KB but non-contiguous.
- Compaction could combine these into [0-220], allowing P5 to be allocated.

## Exam Tips

1. **Distinguish between internal and external fragmentation**: Internal fragmentation occurs within allocated blocks (fixed partitioning), while external fragmentation occurs between allocated blocks (variable partitioning).

2. **Remember the protection mechanism**: Base and limit registers provide memory protection in contiguous allocation. Every address is checked against the limit before being added to the base.

3. **Allocation strategy comparisons**: First-fit is fastest and generally performs well; best-fit minimizes wasted space but requires more search time; worst-fit rarely performs best in practice.

4. **Quantify fragmentation**: Internal fragmentation = allocated size - requested size. External fragmentation is measured as the percentage of total memory that cannot be used.

5. **Address translation**: Physical Address = Base Register + Logical Address (offset). The offset must be less than the limit register value.

6. **Compaction as a solution**: Know that compaction addresses external fragmentation but at significant processing cost and requires updating all memory references.

7. **Variable vs. fixed partitioning trade-offs**: Fixed partitioning has internal fragmentation but no external fragmentation; variable partitioning has external fragmentation but minimal internal fragmentation.

8. **Real-world relevance**: While modern operating systems use paging, contiguous allocation forms the foundation for understanding memory management and is still used in embedded systems and specific memory regions like kernel memory allocation.