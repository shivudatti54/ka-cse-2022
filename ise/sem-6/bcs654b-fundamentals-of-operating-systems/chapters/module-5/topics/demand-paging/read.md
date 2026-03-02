# Demand Paging: A Core Virtual Memory Technique

## 1. Introduction to Demand Paging

Demand paging is a fundamental memory management scheme used by modern operating systems to implement virtual memory. It is a type of lazy loading where pages are only brought into physical memory (RAM) when they are explicitly demanded by a process, i.e., when the process attempts to access them.

The core idea is to avoid loading all pages of a process into memory at the start of execution. Instead, the executable resides on the disk (the swap space or backing store), and pages are swapped in on an as-needed basis. This allows a system to run processes that are larger than the available physical memory, as only the actively used parts need to reside in RAM at any given time.

```
+---------------------+     +-----------------+
|   Process Virtual   |     |   Physical      |
|     Address Space   |     |   Memory (RAM)  |
|                     |     |                 |
|  +---------------+  |     |  +-----------+  |
|  | Page 0 (Code) |----|----->| Frame X   |  |  // Page is valid & in memory
|  +---------------+  |     |  +-----------+  |
|                     |     |                 |
|  +---------------+  |     |                 |
|  | Page 1 (Data) |--|--X  |                 |  // Page is not in memory
|  +---------------+  |     |                 |
|                     |     |                 |
|  +---------------+  |     |  +-----------+  |
|  | Page 2 (Code) |----|----->| Frame Y   |  |  // Page is valid & in memory
|  +---------------+  |     |  +-----------+  |
|                     |     |                 |
+---------------------+     +-----------------+
         ^                           ^
         |                           |
         |                           |
    On Disk (Backing Store)     In RAM
```

## 2. How Demand Paging Works

The operation of demand paging relies on cooperation between the hardware (MMU - Memory Management Unit) and the operating system software.

### 2.1. The Page Table Entry (PTE) and Valid-Invalid Bit

Each entry in a process's page table contains more than just the frame number. A crucial piece of information is the **valid-invalid bit**.
*   **Valid (V):** The associated page is currently in memory (in a frame) and is legal to access.
*   **Invalid (I):** The associated page is either not in memory (it's still on disk) or is not a valid part of the process's address space.

A typical Page Table Entry (PTE) structure for demand paging includes:
```
+-----------------------------------------------------------------------+
| Valid-Invalid (V/I) |  Protection  |  Referenced  |  Modified (Dirty) |  ...  |  Frame Number  |
+-----------------------------------------------------------------------+
```

### 2.2. The Steps of a Page Fault

When a process tries to access a page marked as 'invalid' in its page table, a **page fault** trap is generated. This is a special type of interrupt handled by the operating system's page fault handler. The sequence of events is as follows:

1.  **Memory Access:** The process issues a memory reference.
2.  **PTE Check:** The MMU translates the virtual address. It finds the PTE and sees the valid-invalid bit is set to 'I' (invalid).
3.  **Page Fault Trap:** The MMU raises a page fault exception, transferring control to the OS kernel.
4.  **Verify Legality:** The OS checks its internal data structures to determine if this is a valid memory access for the process. If it's invalid (e.g., an out-of-bounds error), the process is terminated. If it's valid but just not in memory, proceed.
5.  **Find Free Frame:** The OS finds a free frame in physical memory. If no free frame exists, it must run a **page replacement algorithm** to victimize an existing page and free a frame.
6.  **Schedule Disk Operation:** The OS schedules a disk I/O operation to read the required page from the backing store (disk) into the newly allocated free frame.
7.  **Context Switch:** The process that caused the fault is put into a blocked state, and the CPU is given to another process while waiting for the I/O to complete. This allows for efficient CPU utilization.
8.  **I/O Completion:** The disk interrupt signals that the I/O is complete. The OS updates its tables to reflect that the page is now in memory (in the specific frame).
9.  **Update Page Table:** The OS updates the process's page table entry for this page:
    *   Sets the valid-invalid bit to 'V' (Valid).
    *   Sets the frame number to the newly allocated frame.
    *   Resets other bits (e.g., referenced, modified).
10. **Restart Instruction:** The process that caused the page fault is moved back to the ready state. When it is scheduled to run again, the instruction that caused the fault is **restarted**. This time, the page is in memory, and the memory access completes successfully.

The following flowchart illustrates this process:
```
+------------------------+
| Process references     |
| memory address in Page X|
+------------------------+
            |
            v
+------------------------+ Yes    +-------------------+
| Is Page X Valid & in   |------->| Access completed  |
| Memory? (V-bit = 1)    |        | successfully      |
+------------------------+        +-------------------+
            | No
            v
+------------------------+
| Page Fault Occurs      |
| (Trap to OS)           |
+------------------------+
            |
            v
+------------------------+ No     +-------------------+
| Is memory access legal?|------->| Terminate process |
| (Within process addr.) |        | (segmentation fault)
+------------------------+        +-------------------+
            | Yes
            v
+------------------------+
| Find a free frame      |
| (or run page replacement|
| algo to free one)      |
+------------------------+
            |
            v
+------------------------+
| Schedule disk read to  |
| bring page into frame  |
+------------------------+
            |
            v
+------------------------+
| Block process & wait   |
| for I/O completion     |
+------------------------+
            |
            v
+------------------------+
| I/O complete (interrupt)|
| Update page table:      |
| Set V-bit, frame number|
+------------------------+
            |
            v
+------------------------+
| Restart the instruction |
| that caused the fault  |
+------------------------+
```

## 3. Performance of Demand Paging

The performance of a demand-paged system is critically dependent on the **page fault rate** `p`, where `0 <= p <= 1.0`.
*   If `p = 0`, no page faults occur.
*   If `p = 1.0`, every memory access causes a page fault (this is intolerable).

We can calculate the **Effective Access Time (EAT)** for memory. Let:
*   `ma` = Memory Access Time (e.g., 100 nanoseconds for RAM)
*   `p` = Probability of a page fault (0 < p < 1)
*   `Page Fault Overhead` = Time to handle a page fault (which includes time to trap to the OS, swap the page in, and restart the process). This is dominated by the time to service the disk I/O, which can be around 10 milliseconds (10,000,000 ns).

The Effective Access Time is:
`EAT = (1 - p) * ma + p * (Page Fault Overhead)`

**Example Calculation:**
*   `ma` = 100 ns
*   `Page Fault Overhead` = 10,000,000 ns (10 ms)
*   Acceptable performance degradation is often considered to be less than 10%. So we want `EAT <= 110 ns`.

`EAT = (1 - p) * 100ns + p * 10,000,000ns`
`110ns = 100ns - 100p ns + 10,000,000p ns`
`10ns = 9,999,900p ns`
`p = 10 / 9,999,900 ≈ 0.000001`

This means to keep degradation under 10%, we must have a page fault rate lower than **1 in 1,000,000 memory accesses**. This highlights why keeping the page fault rate extremely low is crucial for performance. High page fault rates lead to a condition called **thrashing**.

## 4. Copy-on-Write (COW)

Copy-on-Write is an optimization technique often used in conjunction with demand paging, particularly for the `fork()` system call.

### 4.1. The Problem with `fork()`
The `fork()` system call creates a new child process that is an exact duplicate of the parent process. A naive implementation would immediately copy all pages of the parent to the child. This is inefficient because:
*   It uses a lot of memory and time.
*   Often, the child process immediately calls `exec()` to replace its memory space with a new program, making the copy operation completely wasted.

### 4.2. The COW Solution
Copy-on-Write allows the parent and child to initially share all pages in memory. These shared pages are marked as **copy-on-write** for both processes.

*   **As long as both processes only read from these pages,** they continue to share the same physical frames efficiently.
*   **If either process attempts to write to a shared page,** a page fault occurs. The OS page fault handler then:
    1.  Recognizes this is a COW page.
    2.  Creates a **brand new copy** of that specific page in memory for the writing process.
    3.  Updates the page table of the writing process to point to this new copy.
    4.  Marks the new page as writable (and no longer COW).
    5.  Restarts the write instruction, which now succeeds without faulting.

This approach significantly improves performance and reduces memory usage when processes are forked.

## 5. Page Replacement

When a page fault occurs and there are no free frames available, the OS must select a **victim page** to evict from memory to free up a frame for the new page. This is the role of the page replacement algorithm. The goal is to choose a page that is unlikely to be needed again soon, minimizing the number of page faults.

The steps for page replacement are:
1.  Find the location of the desired page on the disk.
2.  Find a free frame:
    a.  If there is a free frame, use it.
    b.  If there is no free frame, use a page replacement algorithm to select a victim frame. Write the victim page to the disk **only if it has been modified** (the dirty bit is set). This saves unnecessary disk writes.
3.  Bring the new page into the newly freed frame; update the page and frame tables.
4.  Restart the user process.

Common page replacement algorithms include FIFO (First-In, First-Out), Optimal, LRU (Least Recently Used), and many approximations of LRU.

## 6. Advantages and Disadvantages

| Advantage | Disadvantage |
| :--- | :--- |
| **Allows efficient use of memory.** More processes can be resident in memory, increasing CPU utilization and throughput. | **Overhead.** Page table management and page fault handling require CPU cycles and OS complexity. |
| **Enables running programs larger than physical memory.** The logical address space is no longer constrained by physical RAM size. | **Performance degradation.** If the page fault rate becomes too high, the system can thrash, spending more time paging than executing. |
| **Faster process start-up.** Only the first few pages of a program need to be loaded to begin execution. | **Requires specialized hardware support.** An MMU with a valid-invalid bit and a mechanism to raise page faults is essential. |

## 7. Exam Tips and Summary

*   **Key Concept:** Understand that demand paging is "lazy loading" – pages are loaded into memory only when accessed.
*   **Page Fault Flow:** Be able to describe the step-by-step process of handling a page fault in detail. This is a common exam question.
*   **EAT Calculation:** Practice calculating Effective Access Time. Remember that the disk access time (ms) is orders of magnitude larger than memory access time (ns).
*   **COW:** Understand why Copy-on-Write is used for `fork()` and how it works. It's an optimization to avoid unnecessary copying.
*   **Valid-Invalid Bit:** Know its role. 'Invalid' doesn't always mean illegal; it usually means "not present in memory."
*   **Thrashing:** If a process doesn't have enough of its "working set" (the pages it needs right now) in memory, it will page fault constantly. This high-rate paging is called thrashing and kills system performance. The solution is often to reduce the degree of multiprogramming.