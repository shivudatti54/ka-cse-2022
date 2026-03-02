# Deadlock Detection and Recovery from Deadlock


## Table of Contents

- [Deadlock Detection and Recovery from Deadlock](#deadlock-detection-and-recovery-from-deadlock)
- [Introduction](#introduction)
- [System Model for Detection](#system-model-for-detection)
- [Deadlock Detection Algorithms](#deadlock-detection-algorithms)
  - [Single Instance Resources (Wait-For Graph)](#single-instance-resources-wait-for-graph)
- [Algorithm to detect cycles in wait-for graph](#algorithm-to-detect-cycles-in-wait-for-graph)
  - [Multiple Instance Resources (Banker's Variant)](#multiple-instance-resources-bankers-variant)
- [Deadlock Recovery Methods](#deadlock-recovery-methods)
  - [Process Termination](#process-termination)
  - [Resource Preemption](#resource-preemption)
- [Examples](#examples)
  - [Example 1: Wait-For Graph Detection](#example-1-wait-for-graph-detection)
  - [Example 2: Multiple Resource Detection](#example-2-multiple-resource-detection)
  - [Example 3: Recovery Cost Calculation](#example-3-recovery-cost-calculation)
- [Real-World Implementations](#real-world-implementations)
- [Exam Tips](#exam-tips)
- [Diagrams (Textual Description)](#diagrams-textual-description)
- [Advanced Concepts](#advanced-concepts)

## Introduction

Deadlock detection and recovery form the third strategy in deadlock handling, complementing prevention and avoidance techniques. While prevention focuses on eliminating one of the four necessary deadlock conditions and avoidance uses algorithms like Banker's to ensure safe resource allocation, detection actively monitors the system state to identify deadlocks after they occur. Recovery mechanisms then work to restore normal system operation.

This approach is particularly valuable in systems where resource usage patterns are dynamic and unpredictable. Modern applications like database management systems (Oracle, MySQL) and real-time systems (automotive control systems) employ sophisticated detection algorithms combined with transaction rollback features for recovery.

The detection-recovery strategy offers flexibility at the cost of potential performance overhead. According to syllabus requirements, students must understand both the theoretical foundations and practical implementation aspects of these mechanisms.

## System Model for Detection

For deadlock detection, we model the system using:

- Process set P = {P₁, P₂, ..., Pₙ}
- Resource types R = {R₁, R₂, ..., Rₘ}
- Available vector Available[1..m]
- Allocation matrix Alloc[n×m]
- Request matrix Request[n×m]

**Detection Invocation Triggers:**

1. When a process waits longer than specified timeout
2. Periodic system health checks
3. After resource allocation requests

## Deadlock Detection Algorithms

### Single Instance Resources (Wait-For Graph)

```python
# Algorithm to detect cycles in wait-for graph
def detect_deadlock(wait_for_graph):
 for each process P in graph:
 visited = set()
 if dfs(P, visited):
 return True
 return False

def dfs(node, visited):
 if node in visited:
 return True
 visited.add(node)
 for neighbor in node.waiting_for:
 if dfs(neighbor, visited):
 return True
 visited.remove(node)
 return False
```

**Complexity:** O(n²) for n processes

### Multiple Instance Resources (Banker's Variant)

1. Initialize Work = Available
2. Find Pᵢ where Request[i] ≤ Work
3. If found, add Alloc[i] to Work and mark as finished
4. Repeat until no more processes can finish
5. If unfinished processes remain → deadlock

**Formula for Safety Check:**
∑(Alloc[i]) + Available = Total_Resources

## Deadlock Recovery Methods

### Process Termination

1. **Abort All Deadlocked Processes**

- Guaranteed resolution but maximum impact

2. **Partial Termination**

- Cost factors for selection:
- Process priority
- Computation time used
- Resources held
- Interactive vs batch

### Resource Preemption

1. **Victim Selection**

- Minimum cost calculation:
  Cost = Σ(wᵢ \* resources_held)
  where wᵢ = weight for resource type i

2. **Rollback**

- Full rollback: Restart process
- Partial rollback: Checkpoint recovery

3. **Starvation Prevention**

- Maintain rollback count in process control block
- Limit rollbacks per process

## Examples

### Example 1: Wait-For Graph Detection

**System State:**

- Processes: P1 → P2 → P3 → P1 (circular wait)
- Resources: Single instance each

**Detection Steps:**

1. Build adjacency list:
   P1: [P2]
   P2: [P3]
   P3: [P1]
2. DFS traversal from P1:
   P1 → P2 → P3 → P1 (cycle detected)
3. Deadlock confirmed

### Example 2: Multiple Resource Detection

**System Parameters:**

- Resources: R1(3), R2(2), R3(2)
- Allocation Matrix:
  P1: [1, 0, 1]
  P2: [2, 1, 0]
  P3: [0, 1, 0]
- Request Matrix:
  P1: [1, 1, 0]
  P2: [0, 0, 0]
  P3: [1, 0, 1]
- Available: [0, 0, 0]

**Detection Process:**

1. Work = Available = [0,0,0]
2. P2's Request [0,0,0] ≤ Work → Mark finished
   Work += Alloc[P2] = [2,1,0]
3. Now Work = [2,1,0]
4. P1's Request [1,1,0] ≤ [2,1,0] → Mark finished
   Work += [1,0,1] → [3,1,1]
5. P3's Request [1,0,1] ≤ [3,1,1] → Mark finished
   **Result:** No deadlock (all processes finished)

### Example 3: Recovery Cost Calculation

**Deadlocked Processes:**

- P1: Holds R1(2), Priority=5
- P2: Holds R2(3), Priority=3
- Resource Weights: R1=10, R2=5

**Cost Analysis:**

- Cost(P1) = 2\*10 = 20
- Cost(P2) = 3\*5 = 15
  **Decision:** Terminate P2 (lower cost)

## Real-World Implementations

1. **Oracle DBMS**: Uses wait-for graph with timeout

- Automatic victim selection based on UNDO size

2. **Linux Kernel**: Detection through lockdep subsystem

- Circular lock dependency tracking

3. **Automotive Systems**: CAN bus arbitration

- Priority-based preemption

## Exam Tips

1. **Detection vs Avoidance**: Detection allows deadlocks to occur then finds them, while avoidance prevents using algorithms like Banker's
2. **Wait-For Graph**: Only for single-instance resources; cycle = deadlock
3. **Recovery Costs**: Always mention both process termination and resource preemption methods
4. **Formulas to Memorize**:

- Safety condition: ΣAlloc + Available = Total
- Cost function: Σ(wᵢ \* resources_held)

5. **Banker's Algorithm**: Detection version uses Request matrix instead of Need matrix
6. **Starvation Prevention**: Essential to mention when discussing rollback
7. **Real-World Systems**: Be prepared to give examples of detection/recovery implementations

## Diagrams (Textual Description)

**Wait-For Graph:**

```
P1 → P2 → P3
↑ |
└─────────┘
```

- Circular chain indicates deadlock
- Nodes represent processes
- Edges show "waiting for" relationships

**Resource Allocation Graph:**

```
(P1)──Holds──→R1
 │
Requests
 ↓
R2←──Holds──(P2)
```

- Squares = Resources
- Circles = Processes
- Solid arrows = Resource held
- Dashed arrows = Resource requested

## Advanced Concepts

**Distributed Deadlock Detection:**

- Chandy-Misra-Haas algorithm
- Edge chasing mechanism
- Challenges in global state maintenance

**Timeout-Based Detection:**

- Practical implementation method
- Setting appropriate timeout values
- Trade-off between responsiveness and false positives

**Machine Learning Approaches:**

- Pattern recognition in resource requests
- Predictive deadlock avoidance
- Neural networks for dynamic weight assignment
