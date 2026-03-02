# Operating System Design and Implementation

## Introduction

Designing an operating system is a challenging engineering task. There is no single "correct" way to design an OS, but there are well-established principles and approaches that guide the process. This topic covers the design goals, the important distinction between mechanisms and policies, and the choice of implementation languages.

> **Key Insight:** The design of an OS is influenced by the choice of hardware, the type of system (batch, time-sharing, real-time, embedded), and the intended users.

## Design Goals

The first problem in designing an OS is defining the goals and specifications. These requirements can be divided into two groups:

### User Goals

User goals define what users want from the operating system:

- The OS should be **convenient to use** (easy to learn, easy to navigate)
- The OS should be **reliable** (should not crash frequently)
- The OS should be **safe** and **fast** (responsive performance)
- The OS should be easy to use and not interfere with the user's work

### System Goals

System goals define what system designers, developers, and administrators want:

- The OS should be **easy to design, implement, and maintain**
- The OS should be **flexible** (adaptable to new requirements)
- The OS should be **reliable** and **error-free**
- The OS should be **efficient** in resource utilization
- The OS should be **secure** and resistant to attacks

### The Challenge

```
+------------------------------------------+
| DESIGN GOALS |
+------------------------------------------+
| |
| User Goals System Goals |
| +-------------+ +---------------+ |
| | Convenient | | Easy to | |
| | Reliable | | design | |
| | Safe | | Flexible | |
| | Fast | | Efficient | |
| | Easy to use | | Maintainable | |
| +-------------+ +---------------+ |
| |
| Problem: These goals are vague and |
| can conflict with each other! |
| |
| No unique solution exists. |
+------------------------------------------+
```

> **Important:** There is no unique solution to the problem of defining requirements for an OS. The requirements are vague (e.g., "convenient," "efficient") and can be interpreted differently. This is why there are so many different operating systems.

## Mechanisms vs Policies

One of the most important principles in OS design is the **separation of mechanism and policy**.

### Definitions

| Concept       | Definition                                           | Example                                                |
| ------------- | ---------------------------------------------------- | ------------------------------------------------------ |
| **Mechanism** | **How** something is done -- the method or procedure | Timer interrupt mechanism for CPU scheduling           |
| **Policy**    | **What** will be done -- the decision or rule        | Which scheduling algorithm to use (FCFS, RR, Priority) |

### Why Separate Mechanism and Policy?

```
+------------------------------------------+
| MECHANISM vs POLICY |
+------------------------------------------+
| |
| Mechanism (HOW) Policy (WHAT) |
| +--------------+ +---------------+ |
| | Timer | | Round Robin | |
| | interrupt | | scheduling | |
| | for CPU | | with quantum | |
| | preemption | | = 100ms | |
| +--------------+ +---------------+ |
| |
| SAME mechanism can support DIFFERENT |
| policies. This makes the OS FLEXIBLE. |
+------------------------------------------+
```

**Benefits of separation:**

- **Flexibility:** Changing the policy does not require changing the mechanism
- **Modularity:** Mechanisms can be reused with different policies
- **Maintainability:** Policies can be updated without rewriting core code

### Examples

| Area                    | Mechanism                            | Policy                                            |
| ----------------------- | ------------------------------------ | ------------------------------------------------- |
| CPU Scheduling          | Timer interrupt to preempt processes | Which algorithm: FCFS, SJF, Round Robin, Priority |
| Memory Management       | Page table for virtual memory        | Page replacement algorithm: FIFO, LRU, Optimal    |
| File Access             | Access control lists (ACLs)          | Who gets read/write/execute permissions           |
| I/O Scheduling          | Disk scheduling mechanism            | Which algorithm: FCFS, SSTF, SCAN, C-SCAN         |
| Process Synchronization | Semaphore mechanism                  | When to signal/wait                               |

> **Microkernel approach** is a good example of mechanism-policy separation. The microkernel provides the mechanism (IPC, scheduling), while user-space servers implement the policies (file system policy, security policy).

### Policy Changes Over Time

Policies may need to change based on:

- Workload characteristics
- System usage patterns
- Security requirements
- Performance goals

If mechanism and policy are tightly coupled (mixed together), changing a policy requires modifying the entire mechanism. If they are separated, policies can be swapped without touching the mechanism code.

## Implementation Languages

### Historical Perspective

| Era                      | Language          | Example OS                                               |
| ------------------------ | ----------------- | -------------------------------------------------------- |
| Early days (1950s-1970s) | Assembly language | Early UNIX, OS/360                                       |
| 1970s onwards            | C language        | UNIX (rewritten in C by Dennis Ritchie)                  |
| Modern era               | C, C++, some Rust | Linux (C), Windows (C, C++), macOS (C, C++, Objective-C) |

### Assembly Language

**Advantages:**

- Maximum control over hardware
- Highest possible performance
- Direct access to CPU-specific instructions

**Disadvantages:**

- Extremely difficult to write and debug
- Not portable (specific to one CPU architecture)
- Time-consuming to develop
- Hard to maintain and modify

### High-Level Languages (C, C++)

The major advantage of using a high-level language like C or C++ for OS implementation:

**Advantages:**

| Advantage                | Explanation                                                                  |
| ------------------------ | ---------------------------------------------------------------------------- |
| **Faster development**   | Code is written faster in C than assembly                                    |
| **Easier to understand** | C code is more readable than assembly                                        |
| **Easier to debug**      | High-level debuggers and tools available                                     |
| **Easier to maintain**   | Modifications are simpler                                                    |
| **Portability**          | C code can be compiled for different hardware platforms with minimal changes |
| **Compact code**         | Modern compilers generate efficient machine code                             |

**Disadvantages:**

| Disadvantage              | Explanation                                                   |
| ------------------------- | ------------------------------------------------------------- |
| **Slightly slower**       | Generated code may not be as optimal as hand-crafted assembly |
| **Larger footprint**      | May use more memory than assembly equivalent                  |
| **Less hardware control** | Some hardware-specific operations require assembly            |

### The UNIX Story

UNIX was originally written in **assembly language** by Ken Thompson in 1969. It was rewritten in **C** by Dennis Ritchie in 1973. This made UNIX **portable** -- it could be moved to new hardware by recompiling the C code with a new compiler, rather than rewriting everything in the new assembly language.

```
1969: UNIX written in PDP-7 assembly (not portable)
 |
1973: UNIX rewritten in C by Dennis Ritchie
 |
 Now UNIX can be PORTED to new hardware by:
 1. Writing a C compiler for the new hardware
 2. Recompiling the UNIX source code
 (Only small assembly portions need rewriting)
```

### Modern OS Implementation

Modern operating systems use a mix of languages:

| OS          | Primary Language               | Assembly Used For                                |
| ----------- | ------------------------------ | ------------------------------------------------ |
| **Linux**   | C                              | Boot code, context switching, interrupt handlers |
| **Windows** | C, C++                         | Boot code, low-level kernel operations           |
| **macOS**   | C, C++, Objective-C, Swift     | Boot code, hardware-specific operations          |
| **Android** | Java/Kotlin (apps), C (kernel) | Low-level kernel, drivers                        |

> **Key Point for :** Assembly language is still needed for a small portion of the OS -- specifically the parts that interact directly with hardware (boot code, context switch, interrupt handling). But the vast majority (95%+) of modern OS code is in C/C++.

## Summary

```
+--------------------------------------------------+
| OS Design & Implementation Summary |
+--------------------------------------------------+
| |
| Design Goals: |
| - User goals: convenient, reliable, safe, fast |
| - System goals: flexible, efficient, secure |
| - No unique solution (goals are vague) |
| |
| Mechanisms vs Policies: |
| - Mechanism = HOW (e.g., timer interrupt) |
| - Policy = WHAT (e.g., Round Robin scheduling) |
| - Separation provides flexibility |
| |
| Implementation: |
| - Assembly: fast but not portable |
| - C/C++: portable, maintainable, preferred |
| - Modern OS: mostly C with small assembly parts |
+--------------------------------------------------+
```

## Exam Tips

1. **User goals vs System goals** is a common 5-mark question. List at least 4-5 points for each with clear distinction.
2. **Mechanism vs Policy** is a very important concept. frequently asks "Explain the difference between mechanism and policy with examples." Give at least 3 examples.
3. **Why high-level languages?** Be prepared to explain why modern OSes are written in C/C++ rather than assembly. Mention portability, maintainability, faster development, and that compilers generate efficient code.
4. **UNIX rewrite in C:** This is a classic example -- UNIX was rewritten from assembly to C in 1973, making it portable. This is frequently cited in textbooks and exams.
5. **Assembly still needed:** Remember that boot code, context switching, and interrupt handlers are still written in assembly because they require direct hardware access.
6. **Separation principle:** The mechanism-policy separation principle allows the OS to be flexible. Same mechanism (timer) can support different policies (FCFS, RR, Priority) without code changes to the mechanism.
7. ** commonly asks:** "Discuss the design and implementation issues of an operating system" or "Differentiate between mechanism and policy with suitable examples."
