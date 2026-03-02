# Allocation of Frames

## Introduction

In a paging system, physical memory is divided into fixed-size blocks called FRAMES. The operating system must decide how to allocate these frames among competing processes. This decision is critical because improper frame allocation leads to poor system performance, excessive page faults, and thrashing. Understanding frame allocation is essential for any computer science student, as it forms the foundation of efficient virtual memory management.

When a process executes, it generates memory references that may or may not be in physical memory. If the referenced page is not loaded in a frame, a page fault occurs, and the system must bring the page from secondary storage into a free frame. The efficiency of this process directly depends on how frames are allocated to processes. Too few frames cause frequent page faults; too many frames may lead to internal fragmentation and reduced multiprogramming level.

This topic becomes particularly important in modern computing environments where multiple processes run simultaneously, each requiring memory. Operating systems like Linux, Windows, and macOS implement sophisticated frame allocation algorithms to balance performance, fairness, and system throughput. For DU semester examinations, students must understand both the theoretical foundations and practical implications of frame allocation strategies.

## Key Concepts

### Frames and Page Tables

A frame is the physical counterpart of a page. While pages are logical divisions of a process's address space, frames are physical memory blocks of identical size. The page table maps virtual pages to physical frames. When the CPU generates a logical address, the memory management unit (MMU) uses the page table to translate it to a physical address by replacing the page number with the corresponding frame number.

The size of frames (and pages) is typically a power of 2, commonly 4KB in modern systems. The total number of frames in physical memory equals physical memory size divided by frame size. For example, a system with 16MB of physical memory and 4KB frames has 4,096 frames available for allocation.

### Minimum Number of Frames

Every process must have a minimum number of frames to function correctly. This minimum is determined by the maximum number of pages that can be referenced by any single instruction. Consider an instruction that might access multiple memory operands—each operand might require a page table lookup. If an instruction can reference up to m pages directly or indirectly, the process needs at least m frames.

The minimum number of frames also depends on the instruction set architecture. Some processors have instructions that access memory multiple times, requiring more frames. Additionally, if the system uses a single-level page table, the page table itself might require frames. Violating this minimum causes immediate thrashing—the process cannot execute without constant page faults.

### Equal Allocation

Equal allocation is the simplest frame allocation strategy. Under this approach, each process receives an identical number of frames. If there are m frames available and n processes in memory, each process gets m/n frames.

The main advantage of equal allocation is simplicity—the operating system only needs to track how many processes are running. However, this approach ignores the actual memory requirements of different processes. A small process with modest memory needs receives the same frames as a large process that might benefit from more memory. This inefficiency leads to either wasted memory or insufficient frames for memory-intensive processes.

Equal allocation works reasonably well when all processes have similar memory demands and similar execution characteristics. However, in heterogeneous computing environments where processes vary significantly in size and behavior, this strategy often produces poor results.

### Proportional Allocation

Proportional allocation allocates frames based on process characteristics, typically the process size. A larger process receives more frames proportionally. If the total frames available is m and the total virtual memory size across all processes is S, a process with virtual size s receives (s/S) × m frames.

For instance, suppose a system has 100 frames and three processes with sizes 10KB, 20KB, and 70KB (total 100KB). The first process receives 10 frames, the second receives 20 frames, and the third receives 70 frames. This approach provides better utilization than equal allocation because memory is distributed according to actual needs.

However, proportional allocation based solely on process size has limitations. A small process that is actively executing might benefit from more frames than its size suggests, while a large process that is mostly waiting might not need all its allocated frames. More sophisticated approaches consider process priority and execution behavior.

### Priority-Based Allocation

In priority-based allocation, processes with higher priority receive more frames than those with lower priority. This approach recognizes that critical system processes or interactive applications should receive preferential treatment to improve overall system responsiveness.

When a page fault occurs in a high-priority process, the system might steal frames from a lower-priority process rather than from another high-priority process. This ensures that important work continues with minimal interruption. Some systems implement proportional allocation with priority weights—higher-priority processes receive a proportionally larger share of available frames.

Priority-based allocation raises important questions about fairness and starvation. Low-priority processes might suffer from excessive page faults if high-priority processes consume most available memory. Operating systems often implement aging mechanisms where process priority gradually increases over time to prevent indefinite starvation.

### Working Set Model

The working set model provides a dynamic approach to frame allocation. The working set of a process is the set of pages that the process has referenced during a recent time window. The idea is that processes should keep their working set in physical memory to minimize page faults.

If the total frames available is m, the system attempts to allocate enough frames to each process to hold its working set. When a process's working set grows beyond its allocated frames, page faults increase dramatically. The operating system monitors each process's page reference patterns and adjusts frame allocation dynamically.

The working set model helps prevent thrashing by ensuring that processes receive sufficient frames to maintain their working sets. However, it requires accurate estimation of working set sizes, which is challenging in practice. Systems often use approximations based on page fault frequencies or aging counters.

### Local versus Global Replacement

Frame allocation is closely related to page replacement policy. When a page fault occurs, the system must choose which page to replace. Local replacement selects a page from the faulting process's own pages, while global replacement can select any page from any process in memory.

With local replacement, each process's frame allocation remains fixed (or changes slowly), and the process only replaces its own pages. With global replacement, a process might lose frames to other processes, which can improve overall system utilization but makes frame allocation less predictable.

Most modern operating systems use global replacement because it generally provides better throughput. However, they implement mechanisms to ensure that each process receives a minimum number of frames regardless of replacement decisions.

## Examples

### Example 1: Equal Allocation Calculation

Consider a system with 64 frames and 4 processes in memory. Using equal allocation, calculate how many frames each process receives. If process P1 generates a page fault and requires a new frame, but all frames are occupied, explain what happens.

SOLUTION:
- Total frames: 64
- Number of processes: 4
- Frames per process: 64 ÷ 4 = 16 frames each

When P1 generates a page fault requiring a new frame, since all 64 frames are occupied, the system must perform page replacement. With local replacement, P1 replaces one of its own 16 pages. With global replacement, the system might replace a page from any process. The choice depends on the replacement algorithm (FIFO, LRU, Optimal, etc.) and whether the system uses local or global replacement.

### Example 2: Proportional Allocation

A system has 50 frames available. Three processes P1, P2, and P3 have virtual memory sizes of 100 KB, 200 KB, and 300 KB respectively. If page size is 10 KB, calculate the frame allocation for each process using proportional allocation.

SOLUTION:
- Total virtual memory: 100 + 200 + 300 = 600 KB
- Total frames: 50
- Page size: 10 KB (pages per KB: 0.1, so virtual pages = virtual KB / 10)

Process P1: Virtual pages = 100/10 = 10 pages
Proportional frames = (100/600) × 50 = 8.33 ≈ 8 frames

Process P2: Virtual pages = 200/10 = 20 pages
Proportional frames = (200/600) × 50 = 16.67 ≈ 17 frames

Process P3: Virtual pages = 300/10 = 30 pages
Proportional frames = (300/600) × 50 = 25 frames

Total allocated: 8 + 17 + 25 = 50 frames

Note: In practice, allocations must be integers, so the system might round differently or use additional rules to ensure all frames are allocated.

### Example 3: Minimum Frames Requirement

A system has an instruction format where one instruction can directly reference at most two memory addresses. What is the minimum number of frames required per process? If the system has only 10 frames total and 3 processes, can it run all processes without thrashing?

SOLUTION:
- Maximum memory references per instruction: 2
- Minimum frames needed: At least 2 frames (to hold the instruction and both operands)

However, if the instruction itself might be on a different page than both operands, we might need a third frame. Generally, the minimum is the maximum number of pages any single instruction can reference.

With 10 frames and 3 processes, equal allocation gives each process 10/3 ≈ 3 frames (with some variation). Since 3 frames is greater than the minimum of 2-3 frames, theoretically all processes can run. However, thrashing might still occur if the working sets exceed 3 frames each, or if processes actively use more than their allocated pages.

## Exam Tips

1. UNDERSTAND THE DIFFERENCE BETWEEN PAGES AND FRAMES: Pages are logical (virtual memory divisions), frames are physical. The page table maps pages to frames—this is a common exam question.

2. KNOW THE MINIMUM FRAMES CONCEPT: Remember that each process needs a minimum number of frames based on the maximum pages referenced by any instruction. This prevents thrashing at the most basic level.

3. COMPARISON IS KEY: In exams, expect questions comparing equal allocation versus proportional allocation. Know the advantages and disadvantages of each approach.

4. FORMULA FOR PROPORTIONAL ALLOCATION: Memorize the formula: Frames for process i = (virtual size of process i / total virtual size) × total available frames.

5. LOCAL VS GLOBAL REPLACEMENT: Understand how this relates to frame allocation. Local replacement maintains fixed allocations better, while global replacement provides better overall utilization.

6. THRASHING CONNECTION: Frame allocation directly affects thrashing. Too few frames cause excessive page faults. Be prepared to explain this relationship in exams.

7. PRIORITY CONSIDERATIONS: Remember that priority-based allocation gives more frames to higher-priority processes and can steal frames from lower-priority processes.

8. WORKING SET MODEL: Understand that this model allocates frames based on recent reference patterns rather than static process size. It aims to keep active pages in memory.

9. PRACTICAL EXAMPLE QUESTIONS: Study numerical problems similar to Example 2 above—these frequently appear in DU examinations.

10. REAL-WORLD CONTEXT: Be able to explain how modern operating systems like Linux implement frame allocation using techniques like the page cache and memory overcommit.