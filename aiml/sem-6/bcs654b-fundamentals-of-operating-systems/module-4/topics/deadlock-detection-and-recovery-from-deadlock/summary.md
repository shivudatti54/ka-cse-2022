# Deadlock Detection and Recovery from Deadlock - Summary

## Key Definitions and Concepts

- **Deadlock**: System state where ≥2 processes wait indefinitely for resources held by others (Coffman conditions: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait).
- **Deadlock Detection**: Periodic check for deadlocks using algorithms (Resource Allocation Graphs for single instances, matrix-based methods for multiple instances).
- **Recovery Methods**:
- **Process Termination**: Abort all deadlocked processes (costly) or abort one at a time (overhead).
- **Resource Preemption**: Temporarily take resources from processes (requires rollback mechanisms).
- **Wait-for Graph**: Directed graph showing process dependencies (cycle = deadlock in single-instance systems).
- **Safe State**: System can allocate resources without causing deadlock.

## Important Formulas and Theorems

1. **Deadlock Detection Algorithm (Multiple Instances)**:

```python
# Input: Available[m], Allocation[n][m], Request[n][m]
Work = Available.copy()
Finish = [False] * n

while ∃i where Finish[i]==False and Request[i] ≤ Work:
Work += Allocation[i]
Finish[i] = True

if any Finish[i]==False: DEADLOCK DETECTED
```

2. **Wait-for Graph Cycle Detection**:

- Use DFS or topological sorting to detect cycles in O(n²) time.

## Key Points

- Detection is used when systems allow deadlock conditions (no prevention/avoidance).
- **Single resource instances**: Use wait-for graphs (cycle = deadlock).
- **Multiple instances**: Use matrix-based detection algorithm.
- Recovery methods have tradeoffs: Process termination impacts throughput, preemption requires rollback.
- Detection frequency balances overhead vs responsiveness.
- Real-world use cases: Database transactions, network resource management.
- System must maintain resource allocation tables for detection.
- Recovery requires careful logging for rollback consistency.

## Common Mistakes to Avoid

1. Confusing **detection** (post-facto) with **avoidance** (Banker's algorithm, pre-runtime).
2. Assuming all four Coffman conditions are required for detection (detection works regardless).
3. Overlooking preemption costs: Rollback may require transaction logs or checkpoints.
4. Claiming "wait-for graphs work for multiple instances" (only for single-instance resources).

## Revision Tips

1. **Practice Algorithms**: Simulate detection steps using sample Allocation/Request matrices.
2. **Graph Skills**: Draw wait-for graphs for given scenarios and identify cycles.
3. **Compare Strategies**: Make a table contrasting prevention/avoidance/detection methods.
4. **Case Studies**: Study real examples like Oracle DB deadlock resolution for practical context.
