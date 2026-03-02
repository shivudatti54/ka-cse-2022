# Thrashing

## Introduction

Thrashing is one of the most critical performance degradation phenomena in virtual memory management systems. When a computer system uses demand paging (loading pages only when needed), it relies on having sufficient physical memory to hold the working sets of active processes. However, when the system experiences excessive paging activity due to insufficient memory allocation, it enters a state called thrashing. In this condition, the CPU spends more time swapping pages in and out of memory rather than executing user instructions, leading to severely diminished system throughput and responsiveness.

Understanding thrashing is essential for computer science students because it represents a fundamental trade-off in operating system design between memory efficiency and processor utilization. Modern operating systems must carefully balance multiprogramming degrees to prevent thrashing while maximizing resource utilization. The concepts surrounding thrashing also appear frequently in university examinations, making this topic crucial for academic success in operating system courses at Delhi University.

## Key Concepts

### Definition of Thrashing

Thrashing occurs when a computer system spends more time swapping pages in and out of physical memory than executing actual computational work. In a paging system, each process has a working set—the set of pages that a process is currently using. When the total working set size of all processes in the system exceeds the available physical memory, the system repeatedly generates page faults. Each page fault requires disk I/O to bring the needed page into memory, but before the process can use that page, it may be evicted again to make room for another page. This creates a vicious cycle where processes spend most of their time waiting for page transfers rather than executing instructions.

The fundamental cause of thrashing is over-commitment of physical memory. When too many processes compete for limited RAM, the operating system must constantly swap pages to disk, creating a severe bottleneck since disk I/O is orders of magnitude slower than memory access.

### The Relationship Between CPU Utilization and Degree of Multiprogramming

The relationship between CPU utilization and the degree of multiprogramming (number of processes in memory) follows a characteristic curve that demonstrates thrashing. Initially, as more processes are loaded into memory, CPU utilization increases because the CPU can keep busy while one process waits for I/O. However, when too many processes compete for limited memory, thrashing occurs, and CPU utilization drops dramatically.

At low multiprogramming levels, CPU utilization is low because the CPU often waits for I/O. As the degree of multiprogramming increases, CPU utilization improves. Eventually, when memory becomes over-committed, thrashing sets in, and CPU utilization plummets because the system spends most of its time servicing page faults rather than executing user code.

### Working Set Model

The working set model, proposed by Peter Denning, provides a theoretical framework for understanding and preventing thrashing. The working set of a process is the set of pages that the process has referenced during a specific time interval called the working set window. The key insight is that a process executes efficiently only when its working set is resident in physical memory.

If the total working set size of all processes exceeds the available physical memory, thrashing is inevitable. The operating system can prevent thrashing by adjusting the degree of multiprogramming—removing processes from memory when their working sets cannot be accommodated. The working set size for process i is denoted as WSS_i, and the total demand for memory is ΣWSS_i. If this sum exceeds available memory, thrashing occurs.

### Page Fault Frequency Model

The page fault frequency (PFF) model offers another approach to controlling thrashing. This model directly monitors the page fault rate of each process. When the page fault rate exceeds an upper threshold, the process needs more frames (memory allocation). When the page fault rate falls below a lower threshold, the process has more frames than it needs, and some frames can be reclaimed.

The relationship between page faults and allocated frames follows a characteristic pattern. Initially, as a process receives more frames, its page fault rate decreases dramatically. Eventually, the curve flattens out, indicating diminishing returns from additional memory allocation. The goal is to keep each process in the "knee" of this curve—enough frames to maintain reasonable page fault rates without wasting memory.

### Cause of Thrashing

Thrashing occurs due to several interrelated factors. First, when a new process is brought into memory, it starts with no pages in memory and generates many page faults as it loads its initial working set. If the system is already near capacity, this additional demand pushes it over the edge into thrashing. Second, when a process that was swapped out is brought back into memory, it must reload its entire working set, generating a burst of page faults. Third, changes in program behavior can cause working sets to expand, increasing memory demand. Finally, inadequate frame allocation policies can cause some processes to receive too little memory while others have excess, leading to inefficient overall memory utilization.

### Effects of Thrashing

The effects of thrashing are severe and easily observable. User programs execute extremely slowly as they spend most of their time waiting for disk I/O. The disk drive shows constant activity as the system continuously reads and writes pages. System responsiveness deteriorates dramatically, and interactive programs become unusable. The effective memory access time increases dramatically, often by factors of 10 to 1000 or more compared to normal operation.

## Examples

### Example 1: Working Set Calculation

Consider a system with 1000 frames of physical memory. Three processes P1, P2, and P3 have the following working set sizes: WSS₁ = 300 frames, WSS₂ = 400 frames, and WSS₃ = 500 frames. Determine whether the system will experience thrashing.

Solution:
Total working set demand = WSS₁ + WSS₂ + WSS₃ = 300 + 400 + 500 = 1200 frames
Available physical memory = 1000 frames

Since the total demand (1200 frames) exceeds available memory (1000 frames), thrashing will definitely occur. The system must reduce the degree of multiprogramming by swapping out at least one process, or reduce the working set sizes by encouraging locality of reference in the processes.

### Example 2: Page Fault Frequency Analysis

A process generates 200 page faults in 100,000 memory references. Calculate the page fault rate and determine whether thrashing is likely if the acceptable page fault rate should be below 0.5%.

Solution:
Page fault rate = Number of page faults / Total memory references = 200 / 100,000 = 0.002 = 0.2%

Since 0.2% < 0.5%, the page fault rate is within acceptable limits, and thrashing is unlikely for this process. The process likely has an adequate number of frames allocated to maintain its working set in memory.

### Example 3: Effective Access Time Calculation During Thrashing

Assume normal memory access time is 100 nanoseconds. The time to service a page fault (including disk I/O) is 10 milliseconds (10,000,000 nanoseconds). If 5% of memory accesses result in page faults due to thrashing, calculate the effective access time.

Solution:
Effective access time = (1 - p) × memory_access_time + p × page_fault_time
where p is the page fault probability

Effective access time = (1 - 0.05) × 100 + 0.05 × 10,000,000
= 0.95 × 100 + 0.05 × 10,000,000
= 95 + 500,000
= 500,095 nanoseconds ≈ 500 microseconds

This represents a 5000x slowdown compared to normal memory access, clearly demonstrating why thrashing destroys system performance.

## Exam Tips

For Delhi University examinations, thoroughly understand the relationship between degree of multiprogramming and CPU utilization. The curve showing this relationship is a standard examination question—be prepared to sketch and explain it.

Remember the working set formula: Working Set Size (WSS) = Σ pages referenced in the last τ time units. Questions frequently ask you to calculate whether thrashing will occur given the total working set demand and available memory.

The page fault frequency control algorithm uses upper and lower thresholds. Know how the operating system responds when page fault rates exceed or fall below these thresholds—this is a common short-answer question.

In numerical problems, apply the effective access time formula: Effective Access Time = (1 - p) × Ma + p × Mt, where p is the page fault rate, Ma is memory access time, and Mt is page fault service time. Pay attention to units—convert everything to the same scale (nanoseconds or milliseconds).

Understand the difference between global replacement and local replacement. Global replacement allows any process to take frames from any other process, while local replacement only allows a process to take frames from itself. Global replacement can lead to thrashing more easily.

The causes of thrashing include: insufficient frames allocated to a process, a sudden burst of new processes, working set expansion, and inadequate replacement algorithms. Be prepared to explain these in examination answers.

To prevent thrashing, operating systems can employ: working set model, page fault frequency model, and controlling the degree of multiprogramming. Know these prevention strategies thoroughly.

Finally, remember that thrashing increases the page fault rate, which in turn increases the effective memory access time. This creates a feedback loop that further degrades performance.