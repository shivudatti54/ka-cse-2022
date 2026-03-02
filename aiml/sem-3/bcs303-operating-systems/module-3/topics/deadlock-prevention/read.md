# Deadlock Prevention


## Table of Contents

- [Deadlock Prevention](#deadlock-prevention)
- [Introduction](#introduction)
- [Breaking Mutual Exclusion](#breaking-mutual-exclusion)
- [Eliminating Hold and Wait](#eliminating-hold-and-wait)
  - [Protocol 1: Request All Resources at Start](#protocol-1-request-all-resources-at-start)
  - [Protocol 2: Release Before Requesting](#protocol-2-release-before-requesting)
  - [Disadvantages](#disadvantages)
- [Allowing Preemption (Breaking No Preemption)](#allowing-preemption-breaking-no-preemption)
  - [Protocol](#protocol)
  - [Alternative Protocol](#alternative-protocol)
  - [Limitation](#limitation)
- [Breaking Circular Wait](#breaking-circular-wait)
  - [Protocol](#protocol)
  - [Example](#example)
  - [Why This Prevents Circular Wait](#why-this-prevents-circular-wait)
  - [Disadvantages](#disadvantages)
- [Comparison of Prevention Strategies](#comparison-of-prevention-strategies)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

**Deadlock prevention** is a strategy that ensures deadlocks can never occur by ensuring that at least one of the four necessary conditions for deadlock cannot hold. This is a **proactive, restrictive** approach — the system is designed with constraints that make deadlock structurally impossible.

Recall the four necessary conditions for deadlock:

1. Mutual Exclusion
2. Hold and Wait
3. No Preemption
4. Circular Wait

Deadlock prevention works by **breaking** (negating) one or more of these conditions.

## Breaking Mutual Exclusion

**Mutual exclusion** states that at least one resource must be non-sharable — only one process can use it at a time.

**Approach:** Make resources sharable wherever possible.

- **Read-only files** can be shared by multiple processes simultaneously — no mutual exclusion needed
- **Spooling** can make non-sharable devices appear sharable:

```
Without spooling:
 Process A ---> Printer (blocked if busy)
 Process B ---> Printer (must wait)

With spooling:
 Process A ---> Spool (disk buffer) ---> Printer
 Process B ---> Spool (disk buffer) ----^
 (Both processes "print" without waiting for each other)
```

**Limitation:** Not all resources can be made sharable. A mutex lock, by definition, must be held exclusively. We **cannot** generally deny the mutual exclusion condition — some resources are inherently non-sharable.

## Eliminating Hold and Wait

**Hold and Wait** states that a process holding at least one resource is waiting to acquire additional resources held by other processes.

**Approach:** Ensure that whenever a process requests a resource, it does not hold any other resources.

### Protocol 1: Request All Resources at Start

A process must request and be allocated **all** its resources before it begins execution.

```
Process P1 needs: Printer, Scanner, Disk

Protocol 1:
 P1 requests {Printer, Scanner, Disk} at start
 → If ALL available: allocate all, P1 runs
 → If ANY unavailable: P1 waits (holds nothing)
```

### Protocol 2: Release Before Requesting

A process can request resources only when it holds **none**. It must release all current resources before making a new request.

```
Protocol 2:
 P1 requests {Printer, Scanner} → allocated
 P1 uses Printer and Scanner
 P1 releases {Printer, Scanner}
 P1 requests {Disk} → allocated
 P1 uses Disk
```

### Disadvantages

| Disadvantage                 | Explanation                                                                                                                      |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **Low resource utilization** | Resources allocated early may sit idle until the process actually needs them                                                     |
| **Starvation**               | A process needing many popular resources may wait indefinitely because all required resources are never simultaneously available |

## Allowing Preemption (Breaking No Preemption)

**No Preemption** states that resources cannot be forcibly taken away from a process — they can only be released voluntarily.

**Approach:** Allow the OS to preempt (forcibly take back) resources.

### Protocol

1. If process Pi requests a resource that is **not available**:
2. All resources Pi **currently holds** are **preempted** (released)
3. Pi is placed on the waiting list
4. Pi restarts only when it can get **both** its old resources **and** the new one

```
P1 holds {R1, R2}, requests R3
R3 is not available
→ Preempt R1 and R2 from P1
→ P1 waits until R1, R2, AND R3 are all available
→ P1 restarts with all three
```

### Alternative Protocol

If Pi requests a resource held by **another waiting process** Pj, preempt that resource from Pj and give it to Pi. (Only works if Pj is also waiting, not actively using the resource.)

### Limitation

This approach is **only practical for resources whose state can be easily saved and restored**:

| Preemptable           | Not Preemptable         |
| :-------------------- | :---------------------- |
| CPU registers         | Printer (mid-print job) |
| Memory pages          | Mutex locks             |
| CPU time (scheduling) | Tape drive (mid-write)  |

## Breaking Circular Wait

**Circular Wait** states that there exists a circular chain of processes, each waiting for a resource held by the next process in the chain.

**Approach:** Impose a **total ordering** on all resource types, and require processes to request resources in strictly increasing order.

### Protocol

1. Assign each resource type a unique number: F(Ri) = integer
2. A process can only request resources in **increasing** order of their assigned numbers
3. If a process holds resource Ri, it can only request Rj where **F(Rj) > F(Ri)**
4. To request a resource with a lower number, the process must first **release** all resources with higher numbers

### Example

```
Resource ordering:
 F(Scanner) = 1
 F(Printer) = 2
 F(Tape Drive) = 3
 F(Disk) = 4

Valid request sequence:
 P1: Request Scanner(1) → Request Printer(2) → Request Disk(4) ✓

Invalid request sequence:
 P1: Request Printer(2) → Request Scanner(1) ✗ (1 < 2, violates ordering)
```

### Why This Prevents Circular Wait

**Proof by contradiction:**

Assume circular wait exists: P0 → R0 → P1 → R1 → P2 → ... → Pn → Rn → P0

- P0 holds R0 and waits for R1, so F(R0) < F(R1)
- P1 holds R1 and waits for R2, so F(R1) < F(R2)
- ...
- Pn holds Rn and waits for R0, so F(Rn) < F(R0)

This gives: F(R0) < F(R1) < F(R2) < ... < F(Rn) < F(R0)

This is a contradiction (F(R0) cannot be less than itself). Therefore, circular wait **cannot exist** under this ordering.

### Disadvantages

| Disadvantage                        | Explanation                                                                         |
| :---------------------------------- | :---------------------------------------------------------------------------------- |
| **Inconvenient for programmers**    | Must know the ordering and plan resource requests accordingly                       |
| **Resource numbering is arbitrary** | No universally "correct" ordering — different orderings suit different applications |
| **May force early requests**        | A process may need to request resources earlier than necessary to maintain ordering |

## Comparison of Prevention Strategies

| Condition Denied | Method                                        | Practical?      | Side Effects                            |
| :--------------- | :-------------------------------------------- | :-------------- | :-------------------------------------- |
| Mutual Exclusion | Make resources sharable                       | Rarely possible | Some resources are inherently exclusive |
| Hold and Wait    | Request all at start / release before request | Yes             | Low utilization, possible starvation    |
| No Preemption    | Forcibly take resources                       | Sometimes       | Only for save/restore-able resources    |
| Circular Wait    | Impose total ordering                         | Yes             | Inconvenient for programmers            |

## Summary

| Concept             | Key Point                                                       |
| :------------------ | :-------------------------------------------------------------- |
| Deadlock prevention | Break at least one of the four necessary conditions             |
| Mutual exclusion    | Hard to deny — some resources are inherently exclusive          |
| Hold and wait       | Request all resources upfront, or release all before requesting |
| No preemption       | Preempt resources from waiting processes                        |
| Circular wait       | Impose total ordering on resource types                         |
| Most practical      | Breaking hold-and-wait or circular wait                         |

## Exam Tips

1. **List all four strategies** — Be able to explain how each necessary condition is denied and the trade-offs of each approach.
2. **Circular wait proof** — The proof by contradiction is a classic exam question. Practice writing it out cleanly.
3. **Hold and wait protocols** — Know both protocols (request all at start, release before requesting) and their disadvantages.
4. **Preemption limitation** — Always mention that preemption only works for resources whose state can be saved and restored. Give examples (CPU registers = yes, printer = no).
5. **Spooling example** — Use the printer spooling example to explain how mutual exclusion can sometimes be avoided.
6. **Know which strategy breaks which condition** — This is the most frequently asked question format: "Which deadlock condition does [strategy X] prevent?"
