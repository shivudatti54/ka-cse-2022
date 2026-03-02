# Allocation of Frames in Operating Systems

## Introduction

In a virtual memory system using paging, the main memory is divided into fixed-length blocks called **frames**. The logical address space of a process is divided into same-size blocks called **pages**. When a process is to be executed, its pages are loaded into these available free frames. However, the number of frames in the physical memory is limited. A critical task of the operating system is to decide **how many frames to allocate to each process** and **how to distribute these frames** among the different pages of a single process. This decision directly impacts system performance, as improper allocation can lead to a high rate of page faults, causing excessive disk I/O and severely degrading system throughput.

## Core Concepts of Frame Allocation

The primary goal of frame allocation is to minimize the overall page-fault rate. There are two fundamental considerations:

1. **The Number of Frames per Process:** How many frames should be given to a specific process?
2. **The Type of Allocation:** Should frames be allocated in a fixed (static) or variable (dynamic) manner?

Let's explore the main allocation schemes.

### 1. Fixed Allocation Schemes

In fixed allocation, the number of frames given to a process is decided initially and does not change during the process's lifetime.

#### a) Equal Allocation

The simplest method is to divide the available frames equally among all processes in the system.

- **Example:** If there are 100 free frames and 5 processes, each process gets 20 frames.
- **Drawback:** This is inherently unfair. A large process with a complex working set will suffer a high page fault rate with its 20 frames, while a small process may have frames to spare.

#### b) Proportional Allocation

Here, frames are allocated proportional to the size of the process. A larger process gets more frames, and a smaller one gets fewer.

- **Calculation:** Let the size of process $p_i$ be $s_i$, and the total memory size for all processes be $S = \sum s_i$. If the total number of available frames is $m$, the allocation for process $p_i$ is $a_i = (s_i / S) * m$.
- **Example:** Process P1 has 100 pages, P2 has 50 pages. Total pages = 150. Available frames (m) = 60.
- Frames for P1: (100 / 150) \* 60 = 40 frames
- Frames for P2: (50 / 150) \* 60 = 20 frames
- **Advantage:** More fair than equal allocation as it considers process needs.

### 2. Priority Allocation

This scheme uses the process priority rather than its size. A higher-priority process is given more frames to keep it in memory and allow it to run faster, improving overall system responsiveness. This is a form of proportional allocation where the proportion is based on priority.

### 3. Variable (Dynamic) Global vs. Local Allocation

This is not a specific algorithm but a crucial policy decision that affects how page replacement operates.

- **Global Replacement:** A process can select a victim frame from the set of _all_ frames in the system, even if that frame currently belongs to another process.
- **Advantage:** More flexible. It allows a process to adjust its frame allocation based on the system's overall workload and memory pressure.
- **Disadvantage:** A process cannot control its own page-fault rate. One process's behavior can adversely affect the performance of others.

- **Local Replacement:** A process must select a victim frame _only from the set of frames currently allocated to itself_.
- **Advantage:** The number of frames allocated to a process remains constant, and its performance is isolated from the behavior of other processes.
- **Disadvantage:** May hinder performance if the working set of a process changes, as it cannot "borrow" frames from an idle process.

Most modern systems (like Linux and Windows) use **global replacement** with a variable allocation strategy because it generally provides better system throughput.

## The Working Set Model

A sophisticated approach to dynamic allocation is the **Working Set Model**. It is based on the principle of locality. The working set $W(t, \Delta)$ of a process at time $t$ is the set of pages referenced in the last $\Delta$ time units (the "window size"). The goal of the OS is to track the working set of each active process and ensure it is fully resident in memory. If the working set is in memory, the process will run without many page faults. If not, it will thrash.

- **How it works:** The OS approximates the working set and allocates enough frames to hold it. If the cumulative working sets of all processes exceed the total available frames, the OS must suspend a process (swap it out), freeing all its frames for the remaining processes.

## Key Points & Summary

| Concept                     | Description                                                                         | Key Takeaway                                                         |
| :-------------------------- | :---------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| **Equal Allocation**        | Divides available frames equally among all processes.                               | Simple but inefficient and unfair for processes of differing sizes.  |
| **Proportional Allocation** | Allocates frames based on the size of each process.                                 | Fairer than equal allocation, as it considers the process's needs.   |
| **Priority Allocation**     | Allocates more frames to higher-priority processes.                                 | Used to improve system responsiveness for critical tasks.            |
| **Global Replacement**      | A process can replace any frame in memory, regardless of owner.                     | More flexible and common in modern OSes, but can cause interference. |
| **Local Replacement**       | A process can only replace pages from its own allocated set.                        | Isolates process performance but can be less efficient.              |
| **Working Set Model**       | A model that allocates enough frames to hold the pages a process is actively using. | Aims to prevent thrashing by keeping the "working set" in memory.    |

**Summary:** The allocation of frames is a critical OS task balancing fairness, priority, and performance. While simple schemes like equal and proportional allocation are foundational concepts, modern systems typically employ **dynamic global allocation** policies, often guided by principles like the working set model, to efficiently manage limited physical memory among competing processes and minimize the page fault rate.
