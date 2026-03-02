# Thrashing


## Table of Contents

- [Thrashing](#thrashing)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Understanding Thrashing](#understanding-thrashing)
  - [The Working Set Model](#the-working-set-model)
  - [Page Fault Frequency](#page-fault-frequency)
  - [Causes and Symptoms of Thrashing](#causes-and-symptoms-of-thrashing)
  - [Detection and Recovery](#detection-and-recovery)
- [Examples](#examples)
  - [Example 1: Working Set Calculation](#example-1-working-set-calculation)
  - [Example 2: Page Fault Frequency Control](#example-2-page-fault-frequency-control)
  - [Example 3: Thrashing Recovery](#example-3-thrashing-recovery)
- [Exam Tips](#exam-tips)

## Introduction

Thrashing is a critical phenomenon in virtual memory systems that occurs when a computer experiences excessive paging activity, severely degrading system performance. In modern operating systems, virtual memory allows processes to use more memory than physically available by swapping pages between RAM and secondary storage. However, when the system spends more time managing page transfers than executing useful work, the system enters a state of thrashing. This concept is fundamental to understanding memory management strategies and is essential for designing efficient computing systems.

The significance of thrashing extends beyond academic interest—it directly impacts system responsiveness and throughput in real-world computing environments. Database servers, web applications, and interactive systems can become unusable when thrashing occurs. Understanding thrashing helps system administrators configure appropriate memory allocation and helps developers write memory-efficient code. For computer science students preparing for examinations, thrashing represents a key topic that connects theoretical concepts of virtual memory with practical system behavior.

This chapter examines the causes, detection, and mitigation strategies for thrashing. We explore the working set model, page fault frequency analysis, and various algorithms designed to prevent thrashing. Through detailed examples and step-by-step explanations, we develop a comprehensive understanding of how operating systems manage the delicate balance between memory utilization and system performance.

## Key Concepts

### Understanding Thrashing

Thrashing occurs when the system spends a disproportionate amount of time servicing page faults rather than executing instructions. The fundamental cause is insufficient allocation of physical memory to active processes. When a process's working set—the set of pages it actively uses—exceeds the allocated physical memory, the process encounters page faults repeatedly. Each page fault requires expensive disk I/O operations to bring the required page from secondary storage into RAM. If another page must be evicted to make room, additional page faults occur, creating a vicious cycle.

Consider a scenario where a process needs 10 pages in its working set but is allocated only 5 frames in physical memory. The process will access pages that are not in memory, causing page faults. When the page fault handler brings in a new page, it must evict an existing page. Subsequently, the evicted page may be needed again, causing another page fault. This continuous cycle of evictions and page faults consumes CPU time that could otherwise be used for productive computation. The CPU utilization drops dramatically because it is constantly waiting for disk I/O operations to complete.

The thrashing threshold varies depending on system configuration, but it typically manifests when page fault rates exceed certain values. Modern systems use various heuristics to detect thrashing, including monitoring page fault frequencies and CPU idle time during page I/O operations.

### The Working Set Model

The working set model, introduced by Peter Denning in 1968, provides a theoretical framework for understanding and preventing thrashing. A process's working set is defined as the set of pages that the process has referenced during the most recent τ (tau) time units, where τ is the working set window. The working set represents the minimum amount of memory a process needs to function efficiently without excessive page faults.

The key insight of the working set model is that if the total working set sizes of all processes exceed the available physical memory, thrashing is inevitable. The operating system must either reduce the degree of multiprogramming (the number of processes running simultaneously) or allocate more memory to processes. Most operating systems implement some form of working set approximation using algorithms that track page reference patterns.

For example, if τ = 1000 memory references and a process has referenced 150 unique pages in the last 1000 references, its working set size is 150 pages. If the system has only 100 frames available for this process, thrashing will likely occur because the working set cannot fit in memory. The operating system must either suspend some processes or swap out this process entirely.

### Page Fault Frequency

The page fault frequency (PFF) approach provides a practical method for controlling thrashing. Rather than explicitly calculating working sets, this approach monitors the page fault rate for each process. When the page fault rate exceeds an upper threshold, the system allocates more frames to the process. When the page fault rate falls below a lower threshold, the system reclaims frames from that process.

The page fault frequency approach has several advantages over the working set model. It directly addresses the symptom (high page fault rate) rather than requiring estimation of an indirect measure (working set). It responds quickly to changing workload characteristics. However, it requires careful selection of threshold values, which may need tuning for different workloads.

For instance, if a process experiences more than 5 page faults per thousand memory references (or another appropriate threshold), the operating system allocates additional frames. If the fault rate drops below 1 per thousand references, frames are removed. This dynamic allocation ensures that processes receive memory proportional to their actual needs, minimizing thrashing while maximizing overall system utilization.

### Causes and Symptoms of Thrashing

Several factors contribute to thrashing in computer systems. Understanding these causes helps in designing systems that avoid thrashing and in diagnosing when thrashing occurs.

The primary cause is insufficient physical memory relative to the memory demands of concurrently running processes. When too many processes compete for limited memory, each receives fewer frames than needed to hold its working set. This competition creates the conditions for thrashing.

Another cause is poorly designed memory allocation algorithms. If the system allocates frames based on fixed proportions rather than actual needs, some processes receive more memory than they need while others suffer from memory shortage. Additionally, if the page replacement algorithm selects victim pages poorly, it may evict pages that will be needed soon, increasing page fault rates unnecessarily.

The symptoms of thrashing are distinctive and observable. CPU utilization drops significantly as the processor spends most of its time waiting for disk I/O. The disk I/O queue length increases as the system attempts to service page faults. System response time becomes extremely poor, and interactive applications become unresponsive. The disk activity indicator shows constant activity as pages are swapped in and out continuously.

### Detection and Recovery

Operating systems employ various techniques to detect thrashing and take corrective action. The detection mechanisms typically monitor system-wide and per-process metrics. Whenashing is detected, thr the system initiates recovery procedures to restore normal operation.

One common detection method involves tracking the number of page faults over time periods. If the page fault rate exceeds a defined threshold and CPU utilization is low, thrashing is likely occurring. Some systems track the percentage of time spent in page fault handling versus actual computation. Another approach monitors disk queue lengths and service times, flagging thrashing when disk activity remains high for extended periods.

Once thrashing is detected, recovery involves either reducing memory demand or increasing available memory. The most common recovery action is to suspend or swap out one or more processes, reducing the degree of multiprogramming. This action frees physical memory for the remaining processes, allowing them to hold their working sets in memory. The suspended processes can resume when memory becomes available.

Another recovery approach involves adjusting the priority of processes. Lower priority processes may be swapped out first, while interactive processes (typically given higher priority) retain their memory allocation. Some systems also use adaptive algorithms that temporarily reduce the time slice given to processes experiencing high page fault rates, reducing their memory consumption.

## Examples

### Example 1: Working Set Calculation

Consider a system with physical memory of 100 frames and three processes P1, P2, and P3. Using the working set model with τ = 5000 references, we calculate the working set sizes based on the following page reference history in the last 5000 references:

- P1 has referenced pages: {1, 2, 3, 4, 5, 6, 7} (7 unique pages)
- P2 has referenced pages: {1, 2, 8, 9, 10} (5 unique pages)
- P3 has referenced pages: {4, 5, 6, 11, 12, 13, 14, 15} (8 unique pages)

Total working set requirement = 7 + 5 + 8 = 20 frames

Since only 100 frames are available, this workload does not cause thrashing. The working set easily fits in physical memory.

Now consider a scenario where the reference pattern changes:

- P1 now references pages: {1-25} (25 unique pages)
- P2 now references pages: {1-20} (20 unique pages)
- P3 now references pages: {15-35} (21 unique pages)

Total working set requirement = 25 + 20 + 21 = 66 frames

This still fits within 100 frames, but with less margin. If P1's working set increases to 40 pages and P2's to 35 pages, the total becomes 40 + 35 + 21 = 96 frames, leaving only 4 frames for system overhead. Any slight increase in working set sizes will cause thrashing.

### Example 2: Page Fault Frequency Control

A system uses page fault frequency control with thresholds of 0.05 (upper) and 0.01 (lower). Initially, Process A is allocated 10 frames and experiences a page fault rate of 0.08 faults per memory reference. Since 0.08 exceeds the upper threshold of 0.05, the system allocates additional frames to Process A.

After allocating 5 more frames (total 15), Process A's page fault rate decreases to 0.03. This falls below the lower threshold of 0.01, so the system begins reclaiming frames. It removes one frame, leaving 14 frames. The new page fault rate becomes approximately 0.04, which falls within the acceptable range between 0.01 and 0.05.

This dynamic adjustment continues as the process's behavior changes. If the application accesses new data structures, its page fault rate may increase again, triggering additional frame allocation. The system maintains the page fault rate within the desired range, preventing thrashing while avoiding memory waste.

### Example 3: Thrashing Recovery

A multi-user system with 4 GB of physical RAM is running multiple database queries. The workload increases as more users connect, causing total working set demand to exceed available memory. The system exhibits the following symptoms:

- CPU utilization: 15% (normally 70%)
- Disk I/O: Constant activity with average queue length of 25 requests
- Page fault rate: 500 faults per second

The system detects thrashing through its monitoring subsystem. To recover, it takes the following steps:

1. Identifies the three processes with the lowest priority and largest memory footprints
2. Suspends these processes, freeing approximately 1.2 GB of physical memory
3. Allocates the freed memory to active processes, allowing them to hold their working sets

After recovery:
- CPU utilization: 65%
- Disk I/O: Normal activity with average queue length of 3 requests
- Page fault rate: 25 faults per second

The system has successfully recovered from thrashing by reducing the degree of multiprogramming. The suspended processes remain swapped out until sufficient memory becomes available, at which point they can resume execution.

## Exam Tips

Understanding thrashing requires connecting multiple concepts from memory management. The following points highlight essential knowledge for examination success:

First, thrashing is fundamentally caused by excessive paging activity where the time spent on page faults exceeds productive computation time. Remember that thrashing is a system-wide phenomenon occurring when total working set sizes exceed available physical memory.

Second, the working set model defines the working set as pages referenced within a time window τ. The key principle is that a process should receive at least enough frames to hold its working set. If this condition is violated for any process, thrashing will occur for that process.

Third, page fault frequency control directly monitors page fault rates rather than estimating working sets. When the fault rate exceeds an upper threshold, allocate more frames; when below a lower threshold, reclaim frames. This approach directly addresses thrashing by maintaining acceptable page fault rates.

Fourth, common symptoms of thrashing include low CPU utilization despite high disk activity, rapidly increasing disk queue lengths, and extremely poor response times. These symptoms help in diagnosing thrashing in practical scenarios.

Fifth, the primary recovery mechanism is reducing the degree of multiprogramming by suspending or swapping out some processes. This frees physical memory for remaining processes, breaking the thrashing cycle.

Sixth, remember that thrashing can be prevented through proper memory management. Adequate physical memory, appropriate page replacement algorithms, and careful workload management all contribute to avoiding thrashing.

Seventh, for numerical problems, be prepared to calculate working set sizes from reference strings, determine if thrashing will occur given memory constraints, and analyze the effectiveness of different page replacement algorithms in preventing thrashing.