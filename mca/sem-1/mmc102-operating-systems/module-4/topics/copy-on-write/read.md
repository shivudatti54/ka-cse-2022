# Copy On Write


## Table of Contents

- [Copy On Write](#copy-on-write)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The Fundamental Mechanism](#the-fundamental-mechanism)
  - [Implementation Requirements](#implementation-requirements)
  - [COW in fork() and exec()](#cow-in-fork-and-exec)
  - [COW in Virtualization](#cow-in-virtualization)
  - [COW in File Systems](#cow-in-file-systems)
- [Examples](#examples)
  - [Example 1: fork() with COW](#example-1-fork-with-cow)
  - [Example 2: Multiple fork() with COW](#example-2-multiple-fork-with-cow)
  - [Example 3: COW in Container Memory Efficiency](#example-3-cow-in-container-memory-efficiency)
- [Exam Tips](#exam-tips)

## Introduction

Copy On Write (COW) is an optimization technique used extensively in modern operating systems for efficient memory management. The fundamental principle behind COW is deceptively simple: instead of immediately copying data when a process requests a copy of a memory page, the operating system shares the same physical memory pages between the original and the copy. The actual copying of data occurs only when either process attempts to modify its copy of the data. This lazy evaluation approach dramatically reduces memory overhead and improves performance in scenarios involving multiple processes that initially share identical data.

The technique became particularly prominent with the introduction of the fork() system call in UNIX systems, where traditional copying of the entire parent process address space would be extremely wasteful, especially considering that most child processes immediately call exec() to replace their address space with a new program. Without COW, fork() would duplicate all memory pages, only to have most of them discarded moments later. Copy On Write transforms this inefficient pattern into a highly optimized operation where memory is shared until actual modification is required.

In contemporary operating systems including Linux, Windows, and macOS, Copy On Write has evolved beyond just fork() to become a foundational mechanism in virtualization technologies, containerization, and memory-efficient data processing. Understanding COW is essential for computer science students because it represents a critical intersection of memory management, process control, and system optimization principles that appear consistently in operating system examinations and professional practice.

## Key Concepts

### The Fundamental Mechanism

Copy On Write operates at the page level of memory management. When a process forks, the operating system creates a child process that initially shares all the parent's memory pages. Both processes reference the same physical memory frames, but the memory management unit (MMU) is configured so that both pages are marked as read-only. Any attempt by either process to write to these pages triggers a page fault.

Upon receiving the page fault, the operating system performs the actual copying operation. It allocates a new physical page, copies the original data into it, and then remaps the faulting process's virtual address to point to this new page. The other process continues to share the original page, and both pages are now marked as writable. This lazy copying approach ensures that memory is duplicated only when absolutely necessary.

### Implementation Requirements

The successful implementation of Copy On Write requires several architectural components working in concert. The Memory Management Unit (MMU) plays a crucial role by providing hardware support for page protection. Modern MMUs include bits in page table entries that indicate whether a page is readable, writable, or executable. When a COW page is created, both the parent and child process page tables point to the same physical frame, and the writable bit is cleared.

The operating system kernel must maintain reference counting for shared pages. Each physical page frame includes a counter tracking how many processes currently share that page. When a process forks, the reference count increments. When a process exits or modifies a COW page, the reference count decrements. The page can only be freed when the reference count reaches zero, indicating no process still needs it.

Page fault handling is another critical component. The kernel's page fault handler must distinguish between different types of faults and specifically identify when a fault occurred on a COW page. This requires maintaining additional metadata about which pages are subject to COW semantics versus pages that are genuinely read-only.

### COW in fork() and exec()

The traditional UNIX fork() system call creates a child process with an exact copy of the parent's address space. In early UNIX implementations, this meant literally copying every writable page from parent to child, an operation that could be extremely slow for large processes. With COW optimization, fork() becomes much more efficient.

When fork() returns in a COW-enabled system, the child receives its own page tables, but all entries initially point to the same physical pages as the parent's. Both parent and child can read from these shared pages without triggering faults. The copying occurs only when either process writes to a page, at which point that specific page gets duplicated. If the child immediately calls exec() to load a new program, the vast majority of copied pages are never actually copied, because exec() replaces the entire address space with new pages.

### COW in Virtualization

Virtual machine monitors (VMMs) and container runtimes extensively use Copy On Write for efficient resource allocation. Virtual machines using COW-based snapshots can create new VM instances that share most of their memory with the base image. This allows hosting providers to run numerous virtual machines while keeping memory usage manageable.

Linux's kernel same-page merging (KSM) daemon automatically identifies identical memory pages across different processes and merges them using COW semantics. When a process modifies a merged page, the kernel transparently creates a private copy for that process. This optimization is particularly valuable in server environments running multiple instances of the same application.

### COW in File Systems

File systems implement Copy On Write semantics for data integrity and efficient snapshots. When a file is modified in a COW file system, the old data blocks are never overwritten in place. Instead, new blocks are allocated for the modified data, and the metadata is updated to point to these new blocks. The old blocks remain unchanged, enabling features like point-in-time snapshots and crash consistency.

Btrfs, ZFS, and Copy-On-Write databases leverage these semantics extensively. The primary benefit is that operations can be committed atomically—if a system crash occurs during a write, either the old or new version of the data is accessible, but never a corrupted partial write.

## Examples

### Example 1: fork() with COW

Consider a parent process with a large data array of 1000 pages. When the parent calls fork():

Step 1: The kernel creates a child process and duplicates the parent's page tables.
Step 2: For each of the 1000 pages, the child's page table entry points to the same physical frame as the parent's.
Step 3: Both parent and child page table entries have the read-only bit set.
Step 4: The reference count for each physical page increments to 2.

When the child writes to a single page (say, page 500):
Step 1: The CPU attempts to write to the page, triggering a page fault.
Step 2: The kernel's page fault handler identifies this as a COW fault.
Step 3: A new physical page is allocated, and the contents of page 500 are copied to it.
Step 4: The child's page table entry is updated to point to the new page.
Step 5: The new page is marked as writable.
Step 6: The reference count on the original page decrements to 1.

Result: Only 1 page was physically copied, not 1000. Memory savings: 99.9%.

### Example 2: Multiple fork() with COW

Consider a process that forks twice in succession, creating three processes (parent and two children) all sharing the same memory:

Initial state: Parent process P has a memory region R mapped to physical page frame A.
After fork(): Child C1 is created, sharing frame A. Reference count = 2. Page is read-only.
After second fork(): Child C2 is created, also sharing frame A. Reference count = 3. Page remains read-only.

When P reads from R: No fault occurs, page is shared.
When C1 reads from R: No fault occurs, page is shared.
When C2 writes to R: COW fault triggers. New frame B is allocated, data copied. C2's page table updated to point to B. P and C1 continue using A. Reference count on A = 2, reference count on B = 1.

### Example 3: COW in Container Memory Efficiency

A container runtime launches 10 containers running identical Python interpreters. Without COW optimization, this would require 10 copies of the Python memory footprint (typically 50-100 MB). With COW and KSM:

Step 1: First container loads Python interpreter into memory.
Step 2: Subsequent containers share the same read-only pages with the first container.
Step 3: Reference counts track sharing for each page.
Step 4: When container 5 imports a custom module, that specific page triggers a COW fault.
Step 5: Only the affected pages are copied for container 5.

Result: Total memory usage might be 120 MB instead of 500-1000 MB, representing 75-85% memory savings.

## Exam Tips

1. Remember that COW is a lazy copying optimization—the actual copy happens only on write, not at fork time. This is the core concept that examiners test.

2. The page fault handler is responsible for performing the actual copy when a write attempt occurs on a COW page. Understand the sequence: write attempt → page fault → kernel copies page → remap → continue execution.

3. COW pages are marked as read-only in the page table. This protection can be at the page level or even at the segment level in older systems.

4. Reference counting is essential for COW implementation. Know that each shared physical page maintains a count of how many processes reference it, and pages are freed only when this count reaches zero.

5. The primary benefit of COW in fork() is that the child can often exec() a new program without any copying overhead, making fork-exec a very efficient combination.

6. COW is not limited to process creation—it is also used in memory-mapped file systems, database systems, and virtualization for similar efficiency gains.

7. Be prepared to explain why COW improves performance: it reduces memory usage, eliminates unnecessary copying, and speeds up fork() operations significantly.

8. In exam questions, if asked about fork() behavior, always consider whether COW optimization applies and how it affects the number of page faults and actual memory copies.

9. Linux's KSM (Kernel Same-page Merging) is an example of COW applied to anonymous memory pages across different processes for memory optimization.