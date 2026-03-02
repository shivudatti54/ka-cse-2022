# Peterson's Solution


## Table of Contents

- [Peterson's Solution](#petersons-solution)
- [Introduction](#introduction)
- [Shared Variables](#shared-variables)
- [The Algorithm](#the-algorithm)
  - [Structure for Process Pi (where j = 1 - i)](#structure-for-process-pi-where-j--1---i)
  - [How It Works — Step by Step](#how-it-works--step-by-step)
- [Why It Works — Proving the Three Requirements](#why-it-works--proving-the-three-requirements)
  - [1. Mutual Exclusion](#1-mutual-exclusion)
  - [2. Progress](#2-progress)
  - [3. Bounded Waiting](#3-bounded-waiting)
- [Walkthrough Example](#walkthrough-example)
  - [Scenario 1: Only P0 wants to enter](#scenario-1-only-p0-wants-to-enter)
  - [Scenario 2: Both P0 and P1 want to enter](#scenario-2-both-p0-and-p1-want-to-enter)
  - [Key Insight](#key-insight)
- [Limitations of Peterson's Solution](#limitations-of-petersons-solution)
- [Peterson's Solution vs Hardware Solutions](#petersons-solution-vs-hardware-solutions)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

**Peterson's Solution** is a classic software-based solution to the **critical section problem** for two processes. It was proposed by Gary Peterson in 1981. It is a simple and elegant algorithm that guarantees mutual exclusion, progress, and bounded waiting — the three requirements for a correct critical section solution.

Peterson's solution is important historically and conceptually, even though modern hardware provides better primitives (like atomic instructions). It demonstrates that the critical section problem can be solved purely in software using shared variables.

**Note:** Peterson's solution is restricted to **two processes** that alternate execution between their critical sections and remainder sections. The two processes are numbered P0 and P1, or Pi and Pj where j = 1 - i.

## Shared Variables

Peterson's solution uses two shared variables:

```
int turn; // Whose turn is it to enter the critical section?
boolean flag[2]; // flag[i] = true means process Pi wants to enter
```

| Variable  | Purpose                                                                                                        |
| :-------- | :------------------------------------------------------------------------------------------------------------- |
| `turn`    | Indicates whose turn it is to enter the critical section. If `turn == i`, then process Pi is allowed to enter. |
| `flag[i]` | Indicates that process Pi is ready and wants to enter its critical section.                                    |

## The Algorithm

### Structure for Process Pi (where j = 1 - i)

```c
do {
 flag[i] = TRUE; // Step 1: Pi announces interest
 turn = j; // Step 2: Pi gives priority to Pj (courtesy)

 while (flag[j] == TRUE && turn == j)
 ; // Step 3: Busy wait (spin) if Pj is interested AND it's Pj's turn

 // === CRITICAL SECTION ===
 // Access shared resources safely here

 flag[i] = FALSE; // Step 4: Pi signals it is done

 // === REMAINDER SECTION ===

} while (TRUE);
```

### How It Works — Step by Step

1. **`flag[i] = TRUE`** — Process Pi raises its flag, announcing: "I want to enter the critical section."
2. **`turn = j`** — Process Pi sets `turn` to the other process, effectively saying: "But you can go first if you also want to enter."
3. **`while (flag[j] && turn == j)`** — Pi waits (spins) only if **both** conditions are true:

- Pj also wants to enter (`flag[j] == TRUE`)
- It is Pj's turn (`turn == j`)

4. If either condition becomes false (Pj doesn't want to enter, or turn changes to i), Pi exits the loop and enters the critical section.
5. **`flag[i] = FALSE`** — After finishing the critical section, Pi lowers its flag.

## Why It Works — Proving the Three Requirements

### 1. Mutual Exclusion

Both Pi and Pj cannot be in the critical section at the same time.

**Proof:** For both to enter, both `flag[i]` and `flag[j]` must be `TRUE`. But `turn` can only be either `i` or `j` — not both. So one process must be blocked by the while loop.

- If `turn == j`, then Pi spins and waits (Pj enters)
- If `turn == i`, then Pj spins and waits (Pi enters)

Therefore, only one process can be in the critical section at any time.

### 2. Progress

If no process is in the critical section and some process wants to enter, the selection of which process enters cannot be postponed indefinitely.

**Proof:** If only Pi wants to enter (flag[j] == FALSE), Pi's while loop condition is immediately false, so Pi enters without delay. If both want to enter, the value of `turn` decides — one of them will proceed.

### 3. Bounded Waiting

After process Pi requests entry, there is a bound on the number of times Pj can enter before Pi does.

**Proof:** After Pi sets `flag[i] = TRUE` and `turn = j`, if Pj enters the critical section, Pj will set `turn = i` when it tries to re-enter. This means Pi's while condition becomes false (turn is no longer j), so Pi enters next. Pj can enter at most **once** before Pi gets its turn.

## Walkthrough Example

### Scenario 1: Only P0 wants to enter

```
P0: flag[0] = TRUE
P0: turn = 1
P0: Check while(flag[1] == TRUE && turn == 1)
 → flag[1] is FALSE (P1 doesn't want to enter)
 → Condition is FALSE → P0 enters critical section immediately
```

### Scenario 2: Both P0 and P1 want to enter

```
P0: flag[0] = TRUE P1: flag[1] = TRUE
P0: turn = 1 P1: turn = 0

Suppose P1 executes "turn = 0" LAST (overwrites P0's "turn = 1"):
 turn = 0

P0: Check while(flag[1] && turn == 1) → turn is 0, not 1 → FALSE
 → P0 enters critical section

P1: Check while(flag[0] && turn == 0) → flag[0] is TRUE and turn is 0
 → TRUE → P1 spins and waits

P0 finishes: flag[0] = FALSE
P1: Check while(flag[0] && turn == 0) → flag[0] is FALSE → FALSE
 → P1 enters critical section
```

### Key Insight

The line `turn = j` is the "courtesy" step — each process offers to let the other go first. Since `turn` is a single variable, the **last writer loses** (must wait). This is what breaks the tie when both processes want to enter simultaneously.

## Limitations of Peterson's Solution

| Limitation               | Explanation                                                                                        |
| :----------------------- | :------------------------------------------------------------------------------------------------- |
| **Only 2 processes**     | Does not generalize easily to N processes                                                          |
| **Busy waiting**         | The while loop wastes CPU cycles (spinning)                                                        |
| **Memory reordering**    | Modern processors may reorder instructions, breaking the algorithm unless memory barriers are used |
| **Not used in practice** | Modern OS kernels use hardware atomic instructions (test-and-set, compare-and-swap) instead        |

## Peterson's Solution vs Hardware Solutions

| Aspect              | Peterson's Solution      | Hardware (test_and_set)        |
| :------------------ | :----------------------- | :----------------------------- |
| **Type**            | Software-based           | Hardware-based                 |
| **Processes**       | 2 only                   | Any number                     |
| **Busy waiting**    | Yes                      | Yes (spinlock)                 |
| **Modern usage**    | Educational              | Practical (used in OS kernels) |
| **Memory ordering** | Vulnerable to reordering | Atomic — no reordering issue   |

## Summary

| Concept          | Key Point                                                    |
| :--------------- | :----------------------------------------------------------- |
| Purpose          | Solve critical section problem for 2 processes               |
| Shared variables | `turn` (whose turn) and `flag[2]` (who wants to enter)       |
| Key idea         | Each process offers the other priority (`turn = j`)          |
| Mutual exclusion | Guaranteed — `turn` can only equal one value                 |
| Progress         | Guaranteed — if only one wants in, it enters immediately     |
| Bounded waiting  | Guaranteed — at most one entry by the other before your turn |
| Limitation       | Only works for 2 processes; uses busy waiting                |

## Exam Tips

1. **Write the complete algorithm** — frequently asks you to write Peterson's solution with explanation. Memorize the 4 key lines: `flag[i]=TRUE`, `turn=j`, `while(flag[j] && turn==j)`, `flag[i]=FALSE`.
2. **Prove all three properties** — Be prepared to prove mutual exclusion, progress, and bounded waiting. The mutual exclusion proof (turn can only be i or j, not both) is most commonly asked.
3. **Trace through an example** — Practice tracing execution when both processes try to enter simultaneously. Show which process enters and why.
4. **Know the limitations** — Especially that it only works for 2 processes and uses busy waiting. Compare with hardware solutions.
5. **Understand `turn = j`** — This is the key insight. The process that sets `turn` **last** is the one that waits. This is the "courtesy" that makes the algorithm work.
