# Computer System Architecture


## Table of Contents

- [Computer System Architecture](#computer-system-architecture)
- [Introduction](#introduction)
- [Single-Processor Systems](#single-processor-systems)
- [Multiprocessor Systems (Parallel Systems)](#multiprocessor-systems-parallel-systems)
  - [Advantages of Multiprocessor Systems](#advantages-of-multiprocessor-systems)
  - [Types of Multiprocessor Systems](#types-of-multiprocessor-systems)
  - [SMP vs AMP Comparison](#smp-vs-amp-comparison)
- [Multicore Systems](#multicore-systems)
- [Blade Servers](#blade-servers)
- [Non-Uniform Memory Access (NUMA)](#non-uniform-memory-access-numa)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

Computer system architecture refers to the structure and organization of computing hardware, particularly with respect to the number and arrangement of processors. The architecture of a system directly influences the design of the operating system that manages it. This topic covers the three major categories of computer system architecture: single-processor systems, multiprocessor systems, and clustered systems (corresponding to Section 1.3 of Silberschatz).

## Single-Processor Systems

Until recently, most computer systems used a single processor. A **single-processor system** has one main CPU capable of executing a general-purpose instruction set, including instructions from user processes.

```
Single-Processor System:

 +-------------------+
 | Main CPU | ← Executes user programs and OS
 +-------------------+
 |
 +-------------------+
 | Main Memory |
 +-------------------+
 |
 +-------------------+
 | I/O Devices |
 +-------------------+
```

Most single-processor systems also have **special-purpose processors** that are dedicated to specific devices:

- Disk controllers have microprocessors that manage disk operations
- Keyboard controllers handle key presses
- Graphics controllers process display output

These special-purpose processors do **not** run user processes. They run a limited instruction set and are managed by the OS. The system is still classified as single-processor because only one general-purpose CPU exists.

## Multiprocessor Systems (Parallel Systems)

**Multiprocessor systems** (also called parallel systems or tightly coupled systems) have two or more processors in close communication, sharing the computer bus, clock, memory, and peripheral devices.

### Advantages of Multiprocessor Systems

| Advantage                 | Description                                                                                                                                             |
| :------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Increased throughput**  | More processors means more work done in less time. However, the speedup is not linear — N processors do NOT give N times the speedup due to overhead.   |
| **Economy of scale**      | Multiprocessor systems cost less than multiple single-processor systems because they share peripherals, storage, and power supplies.                    |
| **Increased reliability** | If one processor fails, the system does not halt — remaining processors share the load. This is called **graceful degradation** or **fault tolerance**. |

### Types of Multiprocessor Systems

#### 1. Asymmetric Multiprocessing (AMP)

Each processor is assigned a **specific task**. A **boss processor** controls the system and assigns work to **worker processors**.

```
Asymmetric Multiprocessing:

 +--------+
 | Boss | ← Controls system, assigns tasks
 | CPU |
 +--------+
 / | \
 v v v
+---+ +---+ +---+
|W1 | |W2 | |W3 | ← Worker CPUs execute assigned tasks
+---+ +---+ +---+
```

- The boss-worker relationship means the boss can become a **bottleneck**
- If the boss fails, the entire system may fail
- Simpler to design and implement

#### 2. Symmetric Multiprocessing (SMP)

**All processors are peers** — each processor performs all tasks, including OS functions and user processes. There is no boss-worker relationship.

```
Symmetric Multiprocessing:

 +------+ +------+ +------+
 | CPU1 | | CPU2 | | CPU3 |
 +------+ +------+ +------+
 | | |
 +-----------+-----------+
 |
 +-------------+
 | Shared |
 | Memory |
 +-------------+
```

- Each processor has its own set of registers and private (local) cache
- All processors share **main memory** and **I/O devices**
- The OS must be carefully designed to prevent two processors from choosing the same process to run or modifying the same data simultaneously
- Most modern operating systems (Windows, Linux, macOS) support SMP

### SMP vs AMP Comparison

| Aspect              | Asymmetric (AMP)             | Symmetric (SMP)              |
| :------------------ | :--------------------------- | :--------------------------- |
| **Processor roles** | Boss + workers               | All peers (equal)            |
| **Task assignment** | Boss assigns tasks           | Any CPU runs any task        |
| **Bottleneck**      | Boss CPU can be a bottleneck | No single bottleneck         |
| **Failure impact**  | Boss failure is critical     | Any CPU failure is tolerable |
| **Complexity**      | Simpler OS design            | More complex OS design       |
| **Modern usage**    | Less common                  | Standard in modern systems   |

## Multicore Systems

A recent trend in CPU design is to place **multiple computing cores on a single chip**. These are called **multicore processors**. Each core has its own registers and local cache, but all cores share the main memory.

```
Multicore Processor (Dual-Core):

+------------------------------------------+
| Single Chip |
| |
| +----------+ +----------+ |
| | Core 0 | | Core 1 | |
| |----------| |----------| |
| | Registers| | Registers| |
| | L1 Cache | | L1 Cache | |
| +----------+ +----------+ |
| | | |
| +--------+-----------+ |
| | |
| +-------------+ |
| | L2 Cache | (shared) |
| +-------------+ |
+------------------------------------------+
 |
 +-------------+
 | Main Memory |
 +-------------+
```

**Why multicore?**

- Multicore is more efficient than multiple separate chips because **on-chip communication is faster** than between-chip communication
- Uses **less power** than multiple single-core chips

From the OS perspective, a multicore processor with N cores appears as N standard processors, so the OS uses SMP techniques to manage them.

## Blade Servers

A **blade server** is a modular server design where multiple **blade** processing boards are placed in a single chassis. Each blade boots independently and can run its own operating system.

- Some blade chassis include a **backplane** that connects all blades via a high-speed network
- Blades can be individually managed, added, or removed without affecting others
- Used in data centers for high-density computing

## Non-Uniform Memory Access (NUMA)

As the number of CPUs increases, contention for the shared system bus becomes a bottleneck in traditional SMP. **NUMA** addresses this by giving each CPU its own local memory:

```
NUMA Architecture:

 +------+------+ +------+------+
 | CPU1 | Mem1 | | CPU2 | Mem2 |
 +------+------+ +------+------+
 | |
 +----------+-----------+
 |
 Interconnect
```

- Each CPU can access its own local memory **fast**
- Accessing another CPU's memory is possible but **slower** (non-uniform access time)
- The OS must be NUMA-aware to place process data in the memory closest to the CPU running the process

## Summary

| Architecture               | Key Characteristic                | Example                     |
| :------------------------- | :-------------------------------- | :-------------------------- |
| Single-processor           | One general-purpose CPU           | Older PCs, embedded systems |
| Asymmetric multiprocessing | Boss CPU assigns tasks to workers | Some older mainframes       |
| Symmetric multiprocessing  | All CPUs are peers; share memory  | Modern desktops, servers    |
| Multicore                  | Multiple cores on one chip        | Intel Core i7, AMD Ryzen    |
| NUMA                       | Each CPU has fast local memory    | Large-scale servers         |
| Blade servers              | Modular boards in a chassis       | Data centers                |

## Exam Tips

1. **SMP vs AMP** — This is a very common comparison question. Know the boss-worker vs peer model, and why SMP is preferred in modern systems.
2. **Three advantages of multiprocessor systems** — Increased throughput, economy of scale, increased reliability (graceful degradation). Memorize these with explanations.
3. **Multicore diagram** — Be able to draw a multicore processor showing cores with private caches and shared L2 cache. This is frequently asked.
4. **Graceful degradation** — Know this term: the ability of a system to continue operating (at reduced performance) when a processor fails. Also called fault tolerance.
5. **Single-processor special-purpose processors** — Remember that disk controllers and keyboard controllers have their own microprocessors, but the system is still classified as single-processor because only one general-purpose CPU exists.
6. **NUMA** — Understand why it exists (bus contention in large SMP systems) and how it works (fast local memory, slow remote memory).
