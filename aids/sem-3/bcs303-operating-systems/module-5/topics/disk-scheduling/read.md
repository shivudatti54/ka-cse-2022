# Disk Scheduling Algorithms


## Table of Contents

- [Disk Scheduling Algorithms](#disk-scheduling-algorithms)
- [Introduction](#introduction)
- [Key Terminology](#key-terminology)
- [Disk Scheduling Algorithms](#disk-scheduling-algorithms)
  - [1. FCFS (First Come First Served)](#1-fcfs-first-come-first-served)
  - [2. SSTF (Shortest Seek Time First)](#2-sstf-shortest-seek-time-first)
  - [3. SCAN (Elevator Algorithm)](#3-scan-elevator-algorithm)
  - [4. C-SCAN (Circular SCAN)](#4-c-scan-circular-scan)
  - [5. LOOK](#5-look)
  - [6. C-LOOK (Circular LOOK)](#6-c-look-circular-look)
- [Comparison of Disk Scheduling Algorithms](#comparison-of-disk-scheduling-algorithms)
- [Selecting a Disk Scheduling Algorithm](#selecting-a-disk-scheduling-algorithm)
- [Worked Numerical Example](#worked-numerical-example)
- [Key Points Summary](#key-points-summary)
- [Exam Tips](#exam-tips)

## Introduction

One of the responsibilities of the operating system is to use hardware efficiently. For hard disk drives (HDDs), this means minimizing the **seek time** -- the time for the disk arm to move to the desired cylinder. The OS achieves this through **disk scheduling algorithms** that determine the order in which disk I/O requests are serviced.

Disk access time has three components:

- **Seek time** -- time for the head to move to the correct cylinder (most expensive)
- **Rotational latency** -- time for the desired sector to rotate under the head
- **Transfer time** -- time to transfer data

Since seek time dominates, disk scheduling focuses on minimizing total head movement.

---

## Key Terminology

| Term              | Meaning                                            |
| :---------------- | :------------------------------------------------- |
| **Seek time**     | Time to move disk arm to the target cylinder       |
| **Cylinder**      | Set of tracks at the same position on all platters |
| **Request queue** | Queue of pending I/O requests (cylinder numbers)   |
| **Head position** | Current cylinder where the disk head is located    |
| **Head movement** | Total number of cylinders the head travels         |

---

## Disk Scheduling Algorithms

For all examples below, we use:

- **Request queue:** 98, 183, 37, 122, 14, 124, 65, 67
- **Initial head position:** 53
- **Disk range:** Cylinders 0 to 199

### 1. FCFS (First Come First Served)

Requests are serviced in the order they arrive in the queue. No reordering.

```
Head movement:

53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67

 53 ──→ 98 |45|
 98 ──→ 183 |85|
 183 ──→ 37 |146|
 37 ──→ 122 |85|
 122 ──→ 14 |108|
 14 ──→ 124 |110|
 124 ──→ 65 |59|
 65 ──→ 67 |2|
 ─────────────
 Total head movement = 640 cylinders
```

```
Direction of head movement (FCFS):

 0 14 37 53 65 67 98 122 124 183 199
 | | | | | | | | | | |
 . . . [S] . . . . . . .
 . . . └──────────→1 . . . .
 . . . . . . . . . 2←────┘ .
 . 4←┘ 3←──────────────┘ . . . .
 . 5←───────────────────┘ . . . .
 . └────────────────────────────→6 . .
 . . . . 7←────────────┘ . . .
 . . . . └→8 . . . . .

 [S] = Start position (53)
 Numbers = order of service
```

**Advantages:** Simple, fair (no starvation)
**Disadvantages:** Large total head movement, not optimized

---

### 2. SSTF (Shortest Seek Time First)

Service the request **closest** to the current head position. This is a form of greedy algorithm.

```
Head movement:

53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183

 53 ──→ 65 |12|
 65 ──→ 67 |2|
 67 ──→ 37 |30|
 37 ──→ 14 |23|
 14 ──→ 98 |84|
 98 ──→ 122 |24|
 122 ──→ 124 |2|
 124 ──→ 183 |59|
 ─────────────
 Total head movement = 236 cylinders
```

**Advantages:** Much better performance than FCFS, lower average seek time
**Disadvantages:** May cause **starvation** of requests far from the head. Not optimal (SJF problem).

---

### 3. SCAN (Elevator Algorithm)

The disk arm moves in one direction, servicing all requests in its path, then **reverses direction** and services requests on the return trip. Like an elevator.

```
Assuming head initially moves toward cylinder 0:

53 → 37 → 14 → 0 → 65 → 67 → 98 → 122 → 124 → 183

 53 ──→ 37 |16|
 37 ──→ 14 |23|
 14 ──→ 0 (reaches end) |14|
 0 ──→ 65 |65|
 65 ──→ 67 |2|
 67 ──→ 98 |31|
 98 ──→ 122 |24|
 122 ──→ 124 |2|
 124 ──→ 183 |59|
 ─────────────
 Total head movement = 236 cylinders
```

```
SCAN head movement diagram:

 0 14 37 53 65 67 98 122 124 183 199
 | | | | | | | | | | |
 . . . [S] . . . . . . .
 . . 2←┘ . . . . . . . .
 . 3←─┘ . . . . . . . . .
 4←──┘ . . . . . . . . . .
 └──────────────────→5 . . . . . .
 . . . . . └→6 . . . . .
 . . . . . . └──→7 . . . .
 . . . . . . . └───→8 9 . .
 . . . . . . . . └────────→10 .

 Head moves LEFT first to 0, then reverses RIGHT
```

**Advantages:** No starvation (every request eventually gets served), more uniform wait time than SSTF
**Disadvantages:** Unnecessary travel to end of disk even if no requests there. Requests at the far end just visited wait longest.

---

### 4. C-SCAN (Circular SCAN)

Like SCAN, but when the head reaches one end, it immediately returns to the **beginning** of the disk (without servicing requests on the return trip) and continues scanning in the same direction. Treats the cylinder space as circular.

```
Assuming head moves toward cylinder 199:

53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 0 → 14 → 37

 53 ──→ 65 |12|
 65 ──→ 67 |2|
 67 ──→ 98 |31|
 98 ──→ 122 |24|
 122 ──→ 124 |2|
 124 ──→ 183 |59|
 183 ──→ 199 (reaches end) |16|
 199 ──→ 0 (jump to start) |199|
 0 ──→ 14 |14|
 14 ──→ 37 |23|
 ─────────────
 Total head movement = 382 cylinders
```

**Advantages:** More uniform wait time than SCAN (no bias toward middle cylinders)
**Disadvantages:** More total head movement than SCAN. Return trip is wasted (no servicing).

---

### 5. LOOK

A practical improvement over SCAN. The head only goes as far as the **last request** in each direction, then reverses -- it does NOT go all the way to the disk end.

```
Assuming head initially moves toward cylinder 0:

53 → 37 → 14 → 65 → 67 → 98 → 122 → 124 → 183

 53 ──→ 37 |16|
 37 ──→ 14 (last request in this |23|
 direction, reverses)
 14 ──→ 65 |51|
 65 ──→ 67 |2|
 67 ──→ 98 |31|
 98 ──→ 122 |24|
 122 ──→ 124 |2|
 124 ──→ 183 |59|
 ─────────────
 Total head movement = 208 cylinders
```

**Advantages:** Avoids unnecessary travel to disk ends; better than SCAN
**Disadvantages:** Slightly more complex than SCAN

---

### 6. C-LOOK (Circular LOOK)

Like C-SCAN, but the head only goes as far as the last request in the current direction, then jumps to the first request in the opposite end (not cylinder 0 or 199).

```
Assuming head moves toward cylinder 199:

53 → 65 → 67 → 98 → 122 → 124 → 183 → 14 → 37

 53 ──→ 65 |12|
 65 ──→ 67 |2|
 67 ──→ 98 |31|
 98 ──→ 122 |24|
 122 ──→ 124 |2|
 124 ──→ 183 (last request, jump) |59|
 183 ──→ 14 (first request at |169|
 other end)
 14 ──→ 37 |23|
 ─────────────
 Total head movement = 322 cylinders
```

**Advantages:** Combines benefits of C-SCAN with LOOK optimization
**Disadvantages:** Jump from last to first request adds overhead

---

## Comparison of Disk Scheduling Algorithms

| Algorithm | Total Movement | Starvation? | Uniform Wait? | Implementation | Used In        |
| :-------- | :------------- | :---------- | :------------ | :------------- | :------------- |
| FCFS      | 640            | No          | No            | Very simple    | Simple systems |
| SSTF      | 236            | Yes         | No            | Moderate       | Some systems   |
| SCAN      | 236            | No          | Moderate      | Moderate       | Traditional OS |
| C-SCAN    | 382            | No          | Yes (best)    | Moderate       | Servers/DBs    |
| LOOK      | 208            | No          | Moderate      | Slightly more  | Most modern OS |
| C-LOOK    | 322            | No          | Yes           | Slightly more  | Modern systems |

> **Note:** Exact head movement values depend on initial direction assumed. The numbers above are for the specific worked example.

---

## Selecting a Disk Scheduling Algorithm

- **SSTF** is common and has a natural appeal but can cause starvation
- **SCAN and C-SCAN** perform better for systems that place a heavy load on the disk (like servers)
- **LOOK and C-LOOK** are practical improvements used in real systems
- Performance depends on the number and type of requests -- for heavy loads, SCAN/C-SCAN are preferred
- The disk scheduling algorithm is written as a separate module of the OS, allowing easy replacement
- Either **SSTF** or **LOOK** is a reasonable default choice

---

## Worked Numerical Example

**Problem:** Given a disk with 200 cylinders (0-199), request queue = {98, 183, 37, 122, 14, 124, 65, 67}, and initial head position = 53, calculate total head movement for FCFS and SSTF.

**FCFS Solution:**

```
Order: 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
Movement: |98-53| + |183-98| + |37-183| + |122-37| + |14-122| + |124-14| + |65-124| + |67-65|
 = 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2
 = 640 cylinders
```

**SSTF Solution:**

```
From 53: closest is 65 (dist=12)
From 65: closest is 67 (dist=2)
From 67: closest is 37 (dist=30)
From 37: closest is 14 (dist=23)
From 14: closest is 98 (dist=84)
From 98: closest is 122 (dist=24)
From 122: closest is 124 (dist=2)
From 124: closest is 183 (dist=59)

Total = 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 236 cylinders
```

---

## Key Points Summary

| Concept | Key Idea                                              |
| :------ | :---------------------------------------------------- |
| Goal    | Minimize seek time (head movement)                    |
| FCFS    | Serve in arrival order; fair but inefficient          |
| SSTF    | Serve closest request; fast but may starve            |
| SCAN    | Elevator; goes end-to-end then reverses               |
| C-SCAN  | One-direction only; more uniform wait times           |
| LOOK    | SCAN but reverses at last request, not disk end       |
| C-LOOK  | C-SCAN but jumps between last and first requests only |

---

## Exam Tips

1. **Worked numerical problems** are the most common exam question on this topic. Practice calculating total head movement for all six algorithms with a given request queue.
2. Always **state the initial head position and direction** before solving. If not given, state your assumption.
3. The **comparison table** (algorithm vs starvation vs performance) is a classic 5-10 mark theory question.
4. **SCAN vs C-SCAN** comparison is frequently asked. Key difference: C-SCAN provides more uniform wait time because it only services requests in one direction.
5. **LOOK vs SCAN** difference: LOOK only goes to the last request, not the end of the disk. This is a common trick question.
6. Remember: SSTF is similar to SJF in CPU scheduling -- both are greedy and can cause starvation.
7. Draw **head movement diagrams** in exams. They fetch extra marks and demonstrate understanding.
8. If the question says "SCAN" without specifying direction, state your assumed direction explicitly.
