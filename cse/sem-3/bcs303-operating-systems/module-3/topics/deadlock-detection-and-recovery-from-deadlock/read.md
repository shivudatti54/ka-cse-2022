# Deadlock Detection and Recovery

## Introduction to Deadlock Detection

Deadlock detection is an alternative approach to handling deadlocks in operating systems. Unlike prevention and avoidance strategies that aim to stop deadlocks from occurring, detection and recovery allows the system to enter a deadlocked state but provides mechanisms to identify and resolve it.

This approach is particularly useful in systems where:

- The resource allocation pattern is unpredictable
- The cost of prevention/avoidance is too high
- The system can tolerate occasional deadlocks

## The Deadlock Detection Algorithm

Operating systems use resource allocation graphs to detect deadlocks. For single instances of each resource type, the system can use a variant of the resource allocation graph. For multiple instances, it uses the Banker's algorithm approach.

### Wait-For Graph (Single Instance)

For systems where each resource type has only one instance, we can use a simplified version called the Wait-For Graph:

```
Process A → Process B (A is waiting for a resource held by B)
Process B → Process C (B is waiting for a resource held by C)
Process C → Process A (C is waiting for a resource held by A)
```

This creates a cycle: A → B → C → A

**ASCII Diagram:**

```
 +---+ waits for +---+
 | A | --------------->| B |
 +---+ +---+
 ^ |
 | |
 | waits for | waits for
 | |
 | v
 +---+ +---+
 | C |<----------------| |
 +---+ +---+
```

### Detection Algorithm for Multiple Instances

For systems with multiple instances of resource types, the algorithm resembles the safety algorithm but works in reverse:

1. Let **Available** be a vector of length m indicating available resources
2. Let **Allocation** be an n × m matrix defining allocated resources
3. Let **Request** be an n × m matrix indicating current requests

**Algorithm Steps:**

```
1. Initialize Work = Available
 Mark all processes as unfinished

2. Find an index i such that:
 a. Process i is not marked finished
 b. Request[i] ≤ Work

3. If such a process exists:
 Work = Work + Allocation[i]
 Mark process i as finished
 Go back to step 2

4. If no such process exists, check if all processes are finished:
 - If yes: no deadlock
 - If no: the unfinished processes are deadlocked
```

## Example of Deadlock Detection

Consider a system with 4 processes (P0-P3) and 3 resource types (A, B, C) with instances: A(7), B(2), C(6).

**Current Allocation Matrix:**

```
 A B C
P0 0 1 0
P1 2 0 0
P2 3 0 3
P3 2 1 1
```

**Request Matrix:**

```
 A B C
P0 0 0 0
P1 2 0 2
P2 0 0 0
P3 1 0 0
```

**Available Resources:** (0, 0, 0)

Let's apply the detection algorithm:

1. Work = Available = (0, 0, 0)
   Mark all processes as unfinished

2. Check P0: Request[0] = (0,0,0) ≤ Work = (0,0,0) ✓
   Work = Work + Allocation[0] = (0,0,0) + (0,1,0) = (0,1,0)
   Mark P0 as finished

3. Check P1: Request[1] = (2,0,2) ≤ Work = (0,1,0) ✗ (2 > 0)
   Check P2: Request[2] = (0,0,0) ≤ Work = (0,1,0) ✓
   Work = Work + Allocation[2] = (0,1,0) + (3,0,3) = (3,1,3)
   Mark P2 as finished

4. Check P1: Request[1] = (2,0,2) ≤ Work = (3,1,3) ✓
   Work = Work + Allocation[1] = (3,1,3) + (2,0,0) = (5,1,3)
   Mark P1 as finished

5. Check P3: Request[3] = (1,0,0) ≤ Work = (5,1,3) ✓
   Work = Work + Allocation[3] = (5,1,3) + (2,1,1) = (7,2,4)
   Mark P3 as finished

All processes are finished ⇒ **No deadlock exists**

## When to Invoke Detection?

The operating system must decide when to run the detection algorithm:

- **Periodically**: Every hour or every few minutes
- **When CPU utilization drops**: If CPU usage becomes low, it might indicate processes are blocked
- **When a process times out**: If a process doesn't complete within expected time

## Recovery from Deadlock

Once a deadlock is detected, the system must recover using one of these approaches:

### 1. Process Termination

**Abort all deadlocked processes**: This breaks the deadlock but loses all completed work.

**Abort one process at a time**: Until the deadlock is broken. This requires rerunning the detection algorithm after each abortion.

**Which process to abort?**

- Priority (lowest priority first)
- Computation time (least time invested)
- Resources held (processes holding many resources)
- Interactive vs batch processes

### 2. Resource Preemption

Temporarily take resources from processes and give them to others until the deadlock is broken.

**Issues with preemption:**

- **Selection of victim**: Which resource/process to preempt from?
- **Rollback**: The preempted process must be rolled back to a safe state
- **Starvation**: Ensuring the same process isn't always chosen as victim

**Recovery mechanisms:**

- **Total rollback**: Abort the process and restart it
- **Partial rollback**: Roll back to a safe state before acquiring the resource
- **Checkpointing**: Periodically save process state to enable rollback

## Comparison of Deadlock Handling Methods

| Method         | Approach                                       | Advantages                                       | Disadvantages                                  |
| -------------- | ---------------------------------------------- | ------------------------------------------------ | ---------------------------------------------- |
| **Prevention** | Design system to avoid one of the 4 conditions | Guaranteed no deadlocks                          | Low device utilization, reduced throughput     |
| **Avoidance**  | Use Banker's algorithm to avoid unsafe states  | Better resource utilization                      | Requires knowing max resource needs in advance |
| **Detection**  | Allow deadlocks, then detect and recover       | No advance knowledge needed, maximum flexibility | Recovery has overhead, potential work loss     |

## Implementation Considerations

**Cost of detection**: The detection algorithm has O(m × n²) complexity where m is resource types and n is processes. This can be expensive for large systems.

**Recovery overhead**: The cost of process termination or rollback must be considered.

**False positives**: The algorithm might detect false deadlocks in some scenarios.

## Real-World Examples

**Database systems**: Often use detection and recovery with transaction rollbacks.

**Network systems**: Use timeout-based detection when requests don't complete.

**Operating systems**: Typically use combination of prevention and detection.

## Exam Tips

1. **Remember the detection algorithm steps**: Work through examples methodically.
2. **Understand the difference**: Between prevention, avoidance, and detection approaches.
3. **Know the recovery options**: Process termination vs resource preemption.
4. **Practice with examples**: Create your own allocation/request matrices and test the algorithm.
5. **Compare costs**: Be prepared to discuss trade-offs between different deadlock handling methods.
6. **Watch for trick questions**: Sometimes a system might appear deadlocked but actually be in a safe state.
