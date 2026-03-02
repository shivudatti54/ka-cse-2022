# Deadlocks in Operating Systems


## Table of Contents

- [Deadlocks in Operating Systems](#deadlocks-in-operating-systems)
- [Introduction](#introduction)
- [System Model and Characterization](#system-model-and-characterization)
  - [Resource Allocation Graph (RAG)](#resource-allocation-graph-rag)
  - [Coffman Conditions (Necessary Conditions)](#coffman-conditions-necessary-conditions)
- [Deadlock Handling Strategies](#deadlock-handling-strategies)
  - [1. Deadlock Prevention](#1-deadlock-prevention)
  - [2. Deadlock Avoidance (Banker's Algorithm)](#2-deadlock-avoidance-bankers-algorithm)
  - [3. Deadlock Detection & Recovery](#3-deadlock-detection--recovery)
- [Examples](#examples)
  - [Example 1: Banker's Algorithm Safety Check](#example-1-bankers-algorithm-safety-check)
  - [Example 2: Deadlock Detection](#example-2-deadlock-detection)
- [Real-World Applications](#real-world-applications)
- [Exam Tips](#exam-tips)

## Introduction

Deadlocks represent a fundamental challenge in operating system design where multiple processes become permanently blocked waiting for resources held by each other. This stalemate condition brings system operations to a halt and requires sophisticated management strategies.

In modern computing systems where resources like memory, I/O devices, and files are shared among competing processes, deadlocks can cripple system efficiency. The study of deadlock mechanisms is crucial for designing reliable operating systems - from embedded devices to cloud servers. 's syllabus emphasizes four key aspects: characterization, prevention, avoidance, and recovery, which form the pillars of deadlock management.

Real-world analogy: Imagine four cars at a four-way intersection, each waiting for the car on their right to move first. This circular wait creates a traffic deadlock. Similarly, in computing, processes waiting for non-sharable resources in circular dependency create system deadlocks.

## System Model and Characterization

### Resource Allocation Graph (RAG)

Visual representation of system state using:

- **Circles (○)** = Processes
- **Rectangles (□)** = Resource types
- **Instances**: Dots inside rectangles represent resource instances
- **Request Edge**: Process → Resource (dashed arrow)
- **Assignment Edge**: Resource → Process (solid arrow)

**Deadlock Condition in RAG**:

```
Deadlock exists ⇨ RAG contains cycle AND
All resources in cycle are non-sharable
```

### Coffman Conditions (Necessary Conditions)

Four conditions that must **all** hold simultaneously:

1. **Mutual Exclusion**

- At least one resource must be non-sharable
- Example: Printer cannot be simultaneously used by multiple processes

2. **Hold and Wait**

- Processes hold resources while waiting for others
- Formula: ∃ Pᵢ | Allocation(Pᵢ) ≠ ∅ ∧ Request(Pᵢ) ≠ ∅

3. **No Preemption**

- Resources cannot be forcibly removed
- Only voluntarily released by holding process

4. **Circular Wait**

- ∃ set {P₁, P₂,..., Pₙ} where
  P₁ waits for P₂'s resources,
  P₂ waits for P₃'s resources, ...,
  Pₙ waits for P₁'s resources

## Deadlock Handling Strategies

### 1. Deadlock Prevention

**Approach**: Design system to violate at least one Coffman condition

| Condition        | Prevention Technique                          |
| ---------------- | --------------------------------------------- |
| Mutual Exclusion | Allow resource sharing (where possible)       |
| Hold and Wait    | Acquire all resources initially (All-or-None) |
| No Preemption    | Allow temporary resource revocation           |
| Circular Wait    | Impose total ordering of resource requests    |

**Engineering Tradeoff**: Reduced system throughput due to strict policies

### 2. Deadlock Avoidance (Banker's Algorithm)

**Key Concept**: Resource allocation decisions based on **safe states**

#### Data Structures:

- **Available[m]**: Available instances of each resource type
- **Max[n][m]**: Maximum demand of each process
- **Allocation[n][m]**: Currently allocated resources
- **Need[n][m]**: Remaining resource needs (Need = Max - Allocation)

#### Safety Algorithm:

1. Initialize Work = Available, Finish[i] = false ∀ i
2. Find process Pᵢ where:

- Finish[i] == false
- Need[i] ≤ Work

3. If found:

- Work += Allocation[i]
- Finish[i] = true
- Repeat step 2

4. System is safe iff ∀i, Finish[i] == true

#### Resource-Request Algorithm:

When process Pᵢ makes request Requestᵢ:

1. If Requestᵢ ≤ Needᵢ → proceed, else error
2. If Requestᵢ ≤ Available → proceed, else wait
3. Tentatively allocate:

- Available -= Requestᵢ
- Allocation[i] += Requestᵢ
- Need[i] -= Requestᵢ

4. Check if resulting state is safe

- If safe → commit allocation
- Else → rollback and make Pᵢ wait

### 3. Deadlock Detection & Recovery

#### Detection Algorithms:

- **Single Instance per Resource**:
  Use wait-for graph + cycle detection (DFS-based)
- **Multiple Instances**:
  Modified Banker's algorithm to detect deadlocks

#### Recovery Methods:

1. **Process Termination**:

- Abort all deadlocked processes
- Abort one process at a time until deadlock resolved

2. **Resource Preemption**:

- Select victim process
- Rollback process state
- Return resources to pool
- Restart process

**Victim Selection Criteria**:

- Process priority
- Computation time used
- Resources held
- Interactive vs batch processes

## Examples

### Example 1: Banker's Algorithm Safety Check

Consider system with:

- 3 resource types: R1(10), R2(5), R3(7)
- 5 processes with current allocation and max:

| Process | Allocation (R1,R2,R3) | Max (R1,R2,R3) |
| ------- | --------------------- | -------------- |
| P0      | (0,1,0)               | (7,5,3)        |
| P1      | (2,0,0)               | (3,2,2)        |
| P2      | (3,0,2)               | (9,0,2)        |
| P3      | (2,1,1)               | (2,2,2)        |
| P4      | (0,0,2)               | (4,3,3)        |

**Step 1**: Calculate Need matrix (Max - Allocation)

| Process | Need (R1,R2,R3) |
| ------- | --------------- |
| P0      | (7,4,3)         |
| P1      | (1,2,2)         |
| P2      | (6,0,0)         |
| P3      | (0,1,1)         |
| P4      | (4,3,1)         |

Available = (3,3,2)

**Safety Check**:

1. Work = (3,3,2)
2. P3's Need (0,1,1) ≤ Work → allocate
   Work += (2,1,1) → (5,4,3)
3. P1's Need (1,2,2) ≤ Work → allocate
   Work += (2,0,0) → (7,4,3)
4. P0's Need (7,4,3) ≤ Work → allocate
   Work += (0,1,0) → (7,5,3)
5. P2's Need (6,0,0) ≤ Work → allocate
6. P4's Need (4,3,1) ≤ Work → allocate

**Safe Sequence**: <P3, P1, P0, P2, P4>

### Example 2: Deadlock Detection

System has:

- 4 processes (P0-P3)
- 3 resource types (A,B,C)
- Current state:
  Available = (2,1,0)
  Allocation Matrix:
  P0: (1,0,1)
  P1: (2,0,0)
  P2: (0,1,2)
  P3: (1,1,0)
  Request Matrix:
  P0: (0,0,0)
  P1: (2,1,0)
  P2: (0,0,1)
  P3: (1,0,1)

**Detection Steps**:

1. Work = Available = (2,1,0)
2. Mark P0 (Request = 0)
3. Work += P0's Allocation → (3,1,1)
4. Compare remaining requests:

- P2's Request (0,0,1) ≤ Work → Mark P2
- Work += (0,1,2) → (3,2,3)

5. P3's Request (1,0,1) ≤ Work → Mark P3
6. Work += (1,1,0) → (4,3,3)
7. P1's Request (2,1,0) ≤ Work → Mark P1

**Conclusion**: No deadlock (all processes marked)

## Real-World Applications

1. **Database Systems**: Use wait-for graphs for deadlock detection
2. **Network Routing**: Deadlock avoidance in packet switching
3. **Automated Manufacturing**: Resource allocation in robotic systems
4. **Cloud Computing**: Deadlock prevention in distributed resource management

## Exam Tips

1. **Four Coffman Conditions**: MEMORIZE the exact conditions and their order (Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait). often asks to list with examples.

2. **Banker's Algorithm Steps**:

- Always start with calculating Need matrix
- Safety algorithm uses Need ≤ Work check
- Resource request algorithm includes tentative allocation

3. **Detection vs Prevention**:

- Prevention: Proactive (design-time)
- Avoidance: Runtime (using safe state checks)
- Detection: Periodic checks + recovery

4. **Wait-For Graph**:

- Only for single-instance resources
- Cycle ⇨ Deadlock
- Use DFS for cycle detection

5. **Recovery Methods**:

- Two main approaches: Process termination & Resource preemption
- Understand victim selection criteria

6. **Resource Allocation Graphs**:

- Practice drawing RAGs from given scenarios
- Cycle with all single-instance resources ⇨ Deadlock

7. **Numerical Problems**:

- Banker's algorithm calculations (80% probability in exams)
- Safe sequence determination
- Maximum additional requests possible without deadlock

8. **Phantom Deadlocks**:

- Can occur in distributed systems due to message delays
- Detection algorithms must handle false positives
